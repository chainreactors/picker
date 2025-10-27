---
title: GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘 - hac425
url: https://www.cnblogs.com/hac425/p/18543638/gpu-driver-vulnerability-technical-mystery-of-spying-on-driving-vulnerabilities-1c4woh
source: 博客园 - hac425
date: 2024-12-14
fetch_date: 2025-10-06T19:40:55.968975
---

# GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘 - hac425

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/hac425/)

# [hac425](https://www.cnblogs.com/hac425)

## 博客迁移自 blog.hac425.top， 部分博文由于新浪图床的限制无法显示图片。pdf 版本：https://gitee.com/hac425/data/tree/master/blog\_pdf

* [首页](https://www.cnblogs.com/hac425/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/hac425)
* 订阅
* [管理](https://i.cnblogs.com/)

# [GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘](https://www.cnblogs.com/hac425/p/18543638/gpu-driver-vulnerability-technical-mystery-of-spying-on-driving-vulnerabilities-1c4woh "发布于 2024-12-13 19:04")

# GPU 驱动漏洞：窥探驱动漏洞利用的技术奥秘

本文尝试以 GPU 漏洞为引介绍围绕 GPU 驱动这一攻击面，安全研究人员对内核漏洞利用技术做的一些探索。

## 背景介绍

目前移动 SOC 平台上由多个硬件模块组成，常见的硬件模块有：CPU、GPU、Modem基带处理器、ISP（图像处理器）等，这些硬件模块通过硬件总线互联，协同完成任务。

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121506299-911241268.png)​

对于 GPU 驱动漏洞研究来说，我们需要关注的一个关键特性是 GPU 和 CPU 共用同一块 RAM。 在 CPU 侧操作系统通过管理 CPU MMU 的页表来实现虚拟地址到物理地址的映射

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121507602-1460516708.png)​

GPU 也有自己的 MMU，不过 GPU 的页表由 CPU 内核中的 GPU 驱动管理，从而限制 GPU 能够访问的物理地址范围。

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121508439-136491192.png)​

在实际的业务使用中，一般是 CPU 侧分配一段物理内存，然后映射给 GPU ， GPU 从共享内存中取出数据完成计算、渲染后再将结果写回共享内存，从而完成 GPU 与 GPU 之间的交互。对于 GPU 驱动安全研究来说，特殊的攻击面在于由于其需要维护 GPU 页表，这个过程比较复杂，涉及到内核中的各个模块的配合，非常容易出现问题，历史上也出现了多个由于 GPU 页表管理失误导致的安全漏洞

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121509292-411636414.png)​

以 ARM Mali 驱动为例，这几年出现的几个比较有代表性的漏洞如下：

| 漏洞 | 类型 | 漏洞原语 |
| --- | --- | --- |
| CVE-2021-39793 | 页权限错误 | 篡改 只读映射到用户进程的物理页 |
| CVE-2021-28664 | 页权限错误 | 篡改 只读映射到用户进程的物理页 |
| CVE-2021-28663 | GPU MMU 操作异常 | 物理页 UAF |
| CVE-2023-4211 | 条件竞争 UAF | SLUB 对象 UAF |
| CVE-2023-48409 | 整数溢出 | 堆溢出 |
| CVE-2023-26083 | 内核地址泄露 | 内核地址泄露 |
| CVE-2022-46395 | 条件竞争 UAF | 物理页 UAF |

> 其中前 3 个漏洞是管理 GPU 页表映射时的漏洞，后面几个就是常规驱动漏洞类型

‍

## CVE-2021-28664

分析代码下载：<https://armkeil.blob.core.windows.net/developer/Files/downloads/mali-drivers/kernel/mali-bifrost-gpu/BX304L01B-SW-99002-r19p0-01rel0.tar>

先以最简单的漏洞开始讲起，这个漏洞算是 Mali 第一个出名的漏洞了，同期出道的还有 CVE-2021-28664，这个漏洞是由 [Project Zero](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-39793.html) 捕获的在野利用，该漏洞的 Patch 如下

```
 static struct kbase_va_region *kbase_mem_from_user_buffer(
                struct kbase_context *kctx, unsigned long address,
                unsigned long size, u64 *va_pages, u64 *flags)
 {
[...]
+       int write;
[...]
+       write = reg->flags & (KBASE_REG_CPU_WR | KBASE_REG_GPU_WR);
+
 #if KERNEL_VERSION(4, 6, 0) > LINUX_VERSION_CODE
        faulted_pages = get_user_pages(current, current->mm, address, *va_pages,
 #if KERNEL_VERSION(4, 4, 168) <= LINUX_VERSION_CODE && \
 KERNEL_VERSION(4, 5, 0) > LINUX_VERSION_CODE
-                       reg->flags & KBASE_REG_CPU_WR ? FOLL_WRITE : 0,
-                       pages, NULL);
+                       write ? FOLL_WRITE : 0, pages, NULL);
 #else
-                       reg->flags & KBASE_REG_CPU_WR, 0, pages, NULL);
+                       write, 0, pages, NULL);
 #endif
 #elif KERNEL_VERSION(4, 9, 0) > LINUX_VERSION_CODE
        faulted_pages = get_user_pages(address, *va_pages,
-                       reg->flags & KBASE_REG_CPU_WR, 0, pages, NULL);
+                       write, 0, pages, NULL);
 #else
        faulted_pages = get_user_pages(address, *va_pages,
-                       reg->flags & KBASE_REG_CPU_WR ? FOLL_WRITE : 0,
-                       pages, NULL);
+                       write ? FOLL_WRITE : 0, pages, NULL);
 #endif
```

Patch 的关键点在于将 get\_user\_pages 参数中的 `reg->flags & KBASE_REG_CPU_WR`​ 换成了 `reg->flags & (KBASE_REG_CPU_WR | KBASE_REG_GPU_WR)`​ ，这两个标记的作用如下：

* KBASE\_REG\_CPU\_WR：表示 reg 能够已写权限映射到用户态进程
* KBASE\_REG\_GPU\_WR: 表示 reg 能够已写权限映射到 GPU

reg 的类型为 `struct kbase_va_region`​ ， MALI 驱动中使用 kbase\_va\_region 管理物理内存，包括物理内存的申请/释放、GPU/CPU 页表映射管理等。

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121510526-964060115.png)​

图中的关键要素如下：

* kbase\_va\_region 中 cpu\_alloc 和 gpu\_alloc 指向 kbase\_mem\_phy\_alloc ，表示该 reg 拥有的物理页，且大部分场景下 cpu\_alloc = gpu\_alloc
* kbase\_va\_region 的 flags 字段控制驱动映射 reg 时的权限，假如 flags 为 KBASE\_REG\_CPU\_WR 表示该 reg 能够被 CPU 映射为可写权限，如果没有该 flag 则不允许将 reg 以可写模式映射到 CPU 进程，确保无法进程修改这些物理页

核心观点：驱动利用 kbase\_va\_region 表示一组物理内存，这组物理内存可以被 CPU 上的用户进程和 GPU 分别映射，映射的权限由 reg->flags 字段控制.

回到漏洞本身，其调用路径中的关键代码如下：

* kbase\_api\_mem\_import

  1. u64 flags = import->in.flags;
  2. kbase\_mem\_import(kctx, import->in.type, u64\_to\_user\_ptr(import->in.phandle), import->in.padding, &import->out.gpu\_va, &import->out.va\_pages, &flags);

     1. copy\_from\_user(&user\_buffer, phandle
     2. uptr = u64\_to\_user\_ptr(user\_buffer.ptr);
     3. kbase\_mem\_from\_user\_buffer(kctx, (unsigned long)uptr, user\_buffer.length, va\_pages, flags)

        1. struct kbase\_va\_region \*reg = kbase\_alloc\_free\_region(rbtree, 0, \*va\_pages, zone);
        2. kbase\_update\_region\_flags(kctx, reg, \*flags) // 根据用户态提供的 flags 设置 reg->flags
        3. faulted\_pages = get\_user\_pages(address, \*va\_pages, reg->flags & KBASE\_REG\_GPU\_WR, 0, pages, NULL);

漏洞在于传递 get\_user\_pages 参数是只考虑了 KBASE\_REG\_GPU\_WR 情况，没有考虑 KBASE\_REG\_CPU\_WR，当 reg->flags 为 KBASE\_REG\_CPU\_WR 时 get\_user\_pages 的第三个参数为 0

```
/*
 * This is the same as get_user_pages_remote(), just with a
 * less-flexible calling convention where we assume that the task
 * and mm being operated on are the current task's and don't allow
 * passing of a locked parameter.  We also obviously don't pass
 * FOLL_REMOTE in here.
 */
long get_user_pages(unsigned long start, unsigned long nr_pages,
		unsigned int gup_flags, struct page **pages,
		struct vm_area_struct **vmas)
{
	return __get_user_pages_locked(current, current->mm, start, nr_pages,
				       pages, vmas, NULL, false,
				       gup_flags | FOLL_TOUCH);
}
```

get\_user\_pages 的作用的是根据用户进程提供的 va （start）遍历进程页表，返回的是 va 对应物理地址对应的 page 结构体指针，结果保存到 pages 数组中。

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121511420-1384181063.png)​

> 即根据 task\_struct->mm 找到进程页表，遍历页表获取物理地址

其中如果 gup\_flags 为 1，表示获取 va 对应 page 后会写入 page 对应的物理页，然后在 get\_user\_pages 内部需要对只读页面和 COW 页面做额外处理，避免这些特殊 va 对应的物理页被修改导致非预期行为。

* 如果 vma 为只读，API 返回错误码
* VA 的映射为 COW 页，在 API 内会完成写时拷贝，并返回新分配的 page

​![image](https://img2023.cnblogs.com/blog/1454902/202411/1454902-20241113121512428-138218347.png)​

当 gup\_flags 为 0 时则直接返回页表遍历的结果（P0）

对于这个漏洞而言，我们可以创建一个 `reg->flags`​ 为 `KBASE_REG_CPU_WR`​ 的 `kbase_va_region`​，再导入页面时就可以获取进程中任...