---
title: Yac 3.0 发布：常见缓存负载吞吐提升 42%
url: https://www.laruence.com/2026/10/19/7656.html
source: 风雪之隅
date: 2026-10-19
fetch_date: 2026-10-20T06:52:20.081348
---

# Yac 3.0 发布：常见缓存负载吞吐提升 42%

[Press "Enter" to skip to content](#main)

[风雪之隅](https://www.laruence.com)

左手代码右手诗

open menu

mobile menu toggle button

* [主页](http://www.laruence.com/)
* [PHP源码分析](http://www.laruence.com/php-internal)
* [PHP应用](http://www.laruence.com/php)
* [JS/CSS](http://www.laruence.com/jscss)
* [随笔](http://www.laruence.com/notes)
* [留言](https://www.laruence.com/guestbook)
* [博客地图](https://www.laruence.com/sitemap)

# Yac 3.0 发布：常见缓存负载吞吐提升 42%中文EN

Published on [19 October 2026](https://www.laruence.com/2026/10) by [laruence](https://www.laruence.com/author/laruence)

* 本文地址: [https://www.laruence.com/2026/10/19/7656.html](https://www.laruence.com/2026/10/19/7656.html "Permanet Link to Yac 3.0 发布：常见缓存负载吞吐提升 42%")
* 转载请注明出处

Yac 2.4.0 发布时，我做的重点是小值：`null`、布尔值、小整数、短字符串、空数组，能不进入 values 区就不进去。

当时叫 embedded。做法很简单：slot 里的 `val` 本来是一个指针，8 字节对齐，低 3 bit 永远空着，拿它们做类型标记，剩下的 bit 放数据。这样一个小值不必分配 block，不必写 values 区，也不必再拷贝一次。

但这个方案遗留了一个问题：扣掉类型标记后，`val` 只剩 61 bit payload。大部分整数够用，`true`/`false`/`null` 更没问题，短字符串也能塞一点；`double` 不行。

`double` 要保留完整的 IEEE 754 64 bit。少 3 bit 就不是原来的数了，不能为了省一个 block 把 `3.1415926` 读回来变成别的东西。2.4 的 embedded 因此只能让 `0.0` 走特例，其他 `double` 还是得进block values 区。

我后来又想了一下：Yac 的 key 上限是 48 字节，但实际 key 大多数根本用不满。比如 `foo`、`alloptions`、`is_blog_installed`，后面还空着一大截。既然 slot 已经固定分了 48 字节给 key，为什么不把足够短的 key 后面那段空间拿来放 value？

于是有了 3.0 的 **inline**。

## Short values Inline

inline 把 value 紧跟在 key 后面放进同一个 slot。只要：

```

strlen($key) + strlen($value) <= 48
```

就不用进 values 区。

这样除了短字符串，`double` 也能 inline：

```

$yac->set('pi', 3.1415926);     // key 很短，8 字节 double 直接放 slot 尾部
$yac->set('status', 'ok');      // 短字符串也一样
$yac->set('feature:new_checkout', true);
```

key 越短，留给 value 的空间越大；key 恰好 48 字节，inline 就没有空间，照旧分配 values block。这个限制很自然，也不用改变 slot 布局。

带来的收益和 embedded 一样：少一次分配，少一次拷贝，少占一点 values 内存。对 WordPress 特别有用，短 option、开关值，短状态、空结果之类的东西不会再挤占真正热数据的位置。

3.0.0 继续往下做，另一个重点是读路径。

## Versioned Snapshot

Yac 的 key 区是一张共享 hash 表，每个条目一个 slot。以前读一个 slot 时，除了取 key 和元数据，还要经过一次CAS协调，这样有一个问题，对于高并发的场景，还是会有读写排队问题；在3.0里，我完全重构了它，把它换成了 versioned snapshot。

这个思路来自 Linux 内核常用的 `seqcount`/`seqlock`：Writer 更新前把 Sequence 改成奇数，完成后改回偶数；Reader 前后各读一次 sequence，中间拷贝数据。两次读到的数相同且为偶数，说明这次拿到的是完整快照；否则重试，整个过程Reader完全不需要排队。

```

seq1 = read_seq();
if (seq1 & 1) {
    retry;
}

copy_slot();
seq2 = read_seq();

if (seq1 != seq2) {
    retry;
}
```

PHP-FPM 的典型场景本来就是读远多于写。当没有写入相撞时，Reader再也不需要做多余的协调动作；真的撞上了，也只是重读 slot，不会返回半截 key、TTL 或 value metadata。

这个改动的并不复杂，但它是 3.0 最主要的来源之一。

## Epoch-based CRC

Yac 的block values 区会循环复用。在高并发的场景下，可能会出现一个 Reader 拿着 value block 读数据时，另一个 worker 可能正在让某个 segment 进入下一轮使用。

以前，Yac会读 block 时做 CRC-32C 校验，宁可把可疑数据当 miss，也不把错误的数据交给 PHP， 从而避免recycles带来的可能的脏数据。

但其实，对于写少读多的情况，recycles之间一定会有一段“安全时间”

于是在3.0，我重构了这部分，加入了 epoch/segment state。当一次读完，CRC校验没问题以后，就记录下当前的recycle epoch，下次读的时候，如果epoch没有变更，那就是安全的。 于是只要 Reader 能证明 block 在整个读取期间都稳定时，就不算 CRC；证明不了时，仍然走 CRC fallback。

也就是说，快路径少做事，边界情况照样验。

## New serializer

之前的Yac用php serialize， 或者json\_encode来做序列化，但是这些通用的方法要考虑序列化的结果要能导入导出，要能易读。并且会同样追求序列化的性能。

但考虑到Yac的缓存场景，写少读多，也就是序列化少，反序列化多，并且缓存的实际内容对用户层透明，所以不需要是易读，索性我就在Yac 3.0，做了一个Yac自己的serializer，在反序列化追求更好的性能。

为了平衡实现的复杂度，这个序列化器，支持的最常见的 array 和 `stdClass`，包括内容可支持的引用值。这涵盖了绝大部分的缓存情况；当然，对于不支持的对象和值，仍然回退到 PHP 原生序列化。

能快的走快路，不能快的照旧。

以前的 `yac.serializer`、JSON、MsgPack、igbinary 三套可选 serializer，以及相应的编译选项，在 3.0 里都没了：

```

; 3.0 起删除，不要再配置
; yac.serializer = igbinary
```

也一定程度降低了维护复杂度。

## Yac::has()，以及属性判断

3.0 新增了 `Yac::has()`：

```

$yac = new Yac();
$yac->set('flag', false);

var_dump($yac->has('flag'));    // bool(true)
var_dump($yac->has('missing')); // bool(false)
```

`false`、`null` 都可以是正常缓存值，用 `get()` 判断“到底有没有”总是不够顺手。现在直接用 `has()` 就行。

和get不同，它不更新 `atime` 和 `hits`。不会把缓存条目搞成“刚被访问过”。

属性形式也一样：

```

$yac->set('n', null);
$yac->set('f', false);
$yac->set('e', '');

isset($yac->n);                 // false
isset($yac->f);                 // true
empty($yac->n);                 // true
empty($yac->f);                 // true
empty($yac->e);                 // true
property_exists($yac, 'n');     // true
property_exists($yac, 'none');  // false
```

从 3.0 开始，这些检查也不会影响 LRU 信息。

## dump()

`dump()` 是我自己排查缓存时最常用的东西，在Wodpress的Yac插件里它也是后台管理工具最重要的方法。在3.0 里它多了三个字段：

* `kind`：值类型；
* `loc`：值放在哪里；
* `enc`：值用什么方式编码。

```

Array
(
    [kind] => 5
    [loc] => 1
    [enc] => 0
    [key] => foo
)
```

`loc` 里，`YAC_LOC_BLOCK` 是 values 区的 block，`YAC_LOC_VALWORD` 是 slot value word，`YAC_LOC_INLINE` 是 slot 内的短字符串。

`enc` 里，`YAC_ENC_NONE` 表示没有序列化，`YAC_ENC_PHP` 表示 PHP serializer，`YAC_ENC_YAC` 表示 Yac 内部 serializer。

老的 `embedded` 字段停在 2.4.2，3.0 看 `loc` 就够了。

还有一个小变化：带 prefix 的实例，`dump()` 现在返回调用方实际传入的 key，不再带内部 prefix。

```

$yac = new Yac('app:');
$yac->set('foo', 'bar');

// 3.0 dump() 里：
// [key] => foo
```

## 性能

测试环境：MacBook Pro M5 Pro、PHP 8.5、16 个 worker、100:1 读写比；Yac/APCu 均使用 160MB 共享内存；压缩全部关闭。数字是所有 worker 的 aggregate ops/s，不是单进程跑出来再相加。

| Value size | Yac 3.0 | APCu 5.1.28 | Memcached 3.4.0 | Yac / APCu | Yac / Memcached |
| --- | --- | --- | --- | --- | --- |
| 6 B | **129.5M** | 1.19M | 0.105M | 108.4x | 1237.9x |
| 64 B | **99.1M** | 1.23M | 0.103M | 80.6x | 964.8x |
| 1 KB | **39.4M** | 1.29M | 0.106M | 30.6x | 371.8x |
| 8 KB | **15.5M** | 1.43M | 0.098M | 10.8x | 158.1x |
| 16 KB | **9.51M** | 1.36M | 0.093M | 7.0x | 101.9x |

可以看到，Yac 3.0 在全部测试尺寸上都明显领先 APCu 和本地 Memcached：相对 APCu 快 **7.0x 到 108.4x**，相对 Memcached 快 **101.9x 到 1237.9x**。

而与 Yac 2.4.2 相比，3.0 在 6B 到 8KB 的匹配负载中，几何平均吞吐提升 **42.3%**；布尔值、整数、开关和短值等 val-word 路径，最高提升 **95.4%**。

这组数据只用来说明 Yac 本身的读写能力。实际结果会受 CPU、PHP 版本、worker 数、key 分布、读写比、values 内存大小和你的数据形态影响。自己的机器、自己的负载，还是自己跑一遍最靠谱。

16KB以及再往上这类更大的值，我没有拿来凑平均数。这个尺寸下更容易碰到机器内存带宽上限，结果反映的是平台，而不只是缓存实现。

## 升级

当前正式版是 3.0.1。3.0.0 的主要读路径改造、API 和兼容性变化都已经包含在其中。

```

pecl upgrade yac

# 或者
pie install laruence/yac

# 源码安装指定版本
curl -LO https://github.com/laruence/yac/archive/refs/tags/3.0.1.tar.gz
tar xf 3.0.1.tar.gz && cd yac-3.0.1
phpize && ./configure && make && sudo make install
```

升级前建议搜一下配置：

```

grep -R "yac.serializer|enable-json|enable-msgpack|enable-igbinary" /etc/php* 2>/dev/null
```

找到就删掉。依赖 `dump()` 做分析的脚本，也要从 `embedded` 切到 `loc`，并注意 3.0 返回的 key 不再带 prefix。

Windows DLL 目前提供到 PHP 8.5：<https://github.com/laruence/yac/releases/>

## 最后

Yac 还是那个 Yac， 但是速度快了40%以上，升级试试吧。

项目地址：<https://github.com/laruence/yac>

### Related Posts

* [Yac 2.1 升级说明](https://www.laruence.com/2020/03/25/5657.html)
* [Yac (Yet Another Cache) - 无锁共享内存Cache](https://www.laruence.com/2013/03/18/2846.html)
* [Yac 2.4.0发布 - 小值读取性能提升64%](https://www.laruence.com/2026/08/26/6566.html)
* [用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html)
* [Yac 2.1 Upgrade Notes](https://www.laruence.com/en/2020/03/25/5657.html)
* [Yac 2.1 升级说明](https://www.laruence.com/2020/03/25/5657.html)
* [Yac (Yet Another Cache) - 无锁共享内存Cache](https://www.laruence.com/2013/03/18/2846.html)
* [Yac 2.4.0发布 - 小值读取性能提升64%](https://www.laruence.com/2026/08/26/6566.html)
* [用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html)
* [Yac 2.1 Upgrade Notes](https://www.laruence.com/en/2020/03/25/5657.html)

Filed in [AI Coding](https://www.laruence.com/category/ai-coding "View all posts in AI Coding"), [English](https://www.laruence.com/category/en "View all posts in English"), [PHP7](https://www.laruence.com/category/php7 "View all posts in PHP7"), [PHP8](https://www.laruence.com/category/php8 "View all posts in PHP8"), [PHP应用](https://www.laruence.com/category/php-usage "View all posts in PHP应用")

* [Apcu](https://www.laruence.com/tag/apcu "View all posts tagged Apcu")
* [cache](https://www.laruence.com/tag/cache "View all posts tagged cache")
* [memcache](https://www.laruence.com/tag/memcache "View all posts tagged memcache")
* [php cache](https://www.laruence.com/tag/php-cache "View all posts tagged php cache")
* [wordpress](https://www.laruence.com/tag/wordpress "View all posts tagged wordpress")
* [yac](https://www.laruence.com/tag/yac "View all posts tagged yac")

Previous Post
[Reconstructing a Real Apartment w...