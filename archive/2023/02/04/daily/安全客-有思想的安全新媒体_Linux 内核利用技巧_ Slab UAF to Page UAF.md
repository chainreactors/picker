---
title: Linux 内核利用技巧: Slab UAF to Page UAF
url: https://www.anquanke.com/post/id/285919
source: 安全客-有思想的安全新媒体
date: 2023-02-04
fetch_date: 2025-10-04T05:39:18.942070
---

# Linux 内核利用技巧: Slab UAF to Page UAF

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Linux 内核利用技巧: Slab UAF to Page UAF

阅读量**277363**

发布时间 : 2023-02-03 10:30:18

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

author: 熊潇 of [IceSword Lab](https://www.iceswordlab.com/about/)

本文研究了内核编译选项 `CONFIG_SLAB_MERGE_DEFAULT` 对 `kmem_cache` 分配的影响.

以及开启该配置的时候, slab UAF 的一种利用方案 ([方案来源](https://ruia-ruia.github.io/2022/08/05/CVE-2022-29582-io-uring/), 本文内容基于 Linux-5.10.90).

阅读前, 需要对 slab/slub, Buddy system 有基本的了解.

* Part. 1: 源码分析
* Part. 2: `CONFIG_SLAB_MERGE_DEFAULT` 配置对比测试
* Part. 3: 跨 slab 的 UAF 利用示例

## Part. 1

创建 `struct kmem_cache` 的时候，有两种情况:

* `__kmem_cache_alias` : 跟现有的共用（mergeable）
* `create_cache` : 创建一个新的

```
kmem_cache_create(..)
    kmem_cache_create_usercopy(..)
        if (!usersize) // usersize == 0
            s = __kmem_cache_alias(name, size, align, flags, ctor); // s 为 NULL 才会创建新的 slab
        if (s)
            goto out_unlock;
        create_cache()

// 进入 `__kmem_cache_alias` 看看
__kmem_cache_alias(..)
    // 检查 CONFIG_SLAB_MERGE_DEFAULT 配置；
    // 如果开启了，则通过 sysfs_slab_alias 找到已经创建的相同大小的 slab 作为替代
    s = find_mergeable(..)
        list_for_each_entry_reverse(s, &slab_caches, list) {
            if (slab_unmergeable(s)) // slab_nomerge 为 true 时 return 1;
                continue;
             ...
             return s;
        }
        return NULL; // slab_nomerge 为 true 的时候返回 NULL
    if(s)
       ...
       sysfs_slab_alias(..)
    return s;

// CONFIG_SLAB_MERGE_DEFAULT=y -> slab_nomerge == false
// CONFIG_SLAB_MERGE_DEFAULT=n -> slab_nomerge == true
static bool slab_nomerge = !IS_ENABLED(CONFIG_SLAB_MERGE_DEFAULT);

// https://cateee.net/lkddb/web-lkddb/SLAB_MERGE_DEFAULT.html
// CONFIG_SLAB_MERGE_DEFAULT: Allow slab caches to be merged

// For reduced kernel memory fragmentation, slab caches can be merged
// when they share the same size and other characteristics.
// This carries a risk of kernel heap overflows being able to
// overwrite objects from merged caches (and more easily control cache layout),
// which makes such heap attacks easier to exploit by attackers.
```

## Part.2

测试 `CONFIG_SLAB_MERGE_DEFAULT` 的影响

Host 主机(开启了配置)：

```
└─[$] uname -r
5.15.0-52-generic

└─[$] cat /boot/config-$(uname -r) |grep CONFIG_SLAB_MERGE_DEFAULT
CONFIG_SLAB_MERGE_DEFAULT=y
```

VM (未开启配置):

```
➜  ~ uname -r
5.10.90

└─[$] cat .config|grep CONFIG_SLAB_MERGE_DEFAULT
# CONFIG_SLAB_MERGE_DEFAULT is not set
```

* code

  ```
    #include <linux/module.h>
    #include <linux/kernel.h>
    #include <linux/init.h>
    #include <linux/mm.h>
    #include <linux/slab.h>
    #include <linux/slub_def.h>
    #include <linux/sched.h>

    #define OBJ_SIZE 256
    #define OBJ_NUM ((PAGE_SIZE/OBJ_SIZE) * 3)

    struct my_struct {
        char data[OBJ_SIZE];
    };

    static struct kmem_cache *my_cachep;
    static struct my_struct *ms[OBJ_NUM];

    static int __init km_init(void){
        int i, cpu;
        struct kmem_cache_cpu *c;
        struct page *pg;

        pr_info("Hello\n");

            my_cachep = kmem_cache_create("my_struct",
                sizeof(struct my_struct), 0,
                SLAB_HWCACHE_ALIGN | SLAB_PANIC | SLAB_ACCOUNT,
                NULL);

        pr_info("my_cachep: %px, %s\n", my_cachep, my_cachep->name);
        pr_info("my_cachep.size: %u\n", my_cachep->size);
        pr_info("my_cachep.object_size: %u\n", kmem_cache_size(my_cachep));

        cpu = get_cpu();
        pr_info("cpu: %d\n", cpu);

        c = per_cpu_ptr(my_cachep->cpu_slab, cpu);

        for(i = 0; i<OBJ_NUM; i++){
            ms[i] = kmem_cache_alloc(my_cachep, GFP_KERNEL);
            pg = virt_to_page(ms[i]);
            pr_info("[%02d] object: %px, page: %px(%px), %d\n", i, ms[i],
                    pg, page_address(pg),
                    (void *)pg == (void *)c->page);
        }

        return 0;

    }

    static void __exit km_exit(void)
    {
        int i;

        for( i = 0; i<OBJ_NUM; i++){
            kmem_cache_free(my_cachep, ms[i]);
        }
        kmem_cache_destroy(my_cachep);
        pr_info("Bye\n");
    }

    module_init(km_init);
    module_exit(km_exit);

    MODULE_LICENSE("GPL");
    MODULE_AUTHOR("X++D");
    MODULE_DESCRIPTION("Kernel xxx Module.");
    MODULE_VERSION("0.1");
  ```
* VM result

  分配的 object 地址和 page 的关系非常清晰

  ```
    ➜  ~ insmod slab-tc.ko
    [ 1184.983757] Hello
    [ 1184.984278] my_cachep: ffff8880096ea000, my_struct
    [ 1184.985568] my_cachep.size: 256
    [ 1184.986451] my_cachep.object_size: 256
    [ 1184.987488] cpu: 0
    **[ 1184.988945] [00] object: ffff888005c38000, page: ffffea0000170e00(ffff888005c38000), 1**
    [ 1184.991189] [01] object: ffff888005c38100, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1184.993438] [02] object: ffff888005c38200, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1184.995688] [03] object: ffff888005c38300, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1184.998018] [04] object: ffff888005c38400, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.000234] [05] object: ffff888005c38500, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.002529] [06] object: ffff888005c38600, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.004702] [07] object: ffff888005c38700, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.006841] [08] object: ffff888005c38800, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.008919] [09] object: ffff888005c38900, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.010944] [10] object: ffff888005c38a00, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.013021] [11] object: ffff888005c38b00, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.014904] [12] object: ffff888005c38c00, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.016926] [13] object: ffff888005c38d00, page: ffffea0000170e00(ffff888005c38000), 1
    [ 1185.018883] [14] object: ffff888005c38e00, page: ffffea0000170e00(ffff888005c38000), 1
    **[ 1185.020761] [15] object: ffff888005c38f00, page: ffffea0000170e00(ffff888005c38000), 1**
    **[ 1185.022735] [16] object: ffff88800953d000, page: ffffea0000254f40(ffff88800953d000), 1**
    [ 1185.024679] [17] object: ffff88800953d100, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.026579] [18] object: ffff88800953d200, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.028528] [19] object: ffff88800953d300, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.030443] [20] object: ffff88800953d400, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.032372] [21] object: ffff88800953d500, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.034263] [22] object: ffff88800953d600, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.036116] [23] object: ffff88800953d700, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.038086] [24] object: ffff88800953d800, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.039929] [25] object: ffff88800953d900, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.041944] [26] object: ffff88800953da00, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.043852] [27] object: ffff88800953db00, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.045736] [28] object: ffff88800953dc00, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.047678] [29] object: ffff88800953dd00, page: ffffea0000254f40(ffff88800953d000), 1
    [ 1185.049585] [30] object: ffff88800953de00, page: ffffea0000254f40(ffff88800953d000), 1
    **[ 1185.051391] [31] object: ffff88800953df00, page: ffffea0000254f40(ffff88800953d000), 1**
    **[ 1185.053206] [32] object: ffff888009543000, page: ffffea00002550c0(ffff888009543000), 1**
    [ 1185.055038] [33] object: ffff888009543...