---
title: Google UAF漏洞利用缓解技术MiraclePtr
url: https://www.anquanke.com/post/id/283735
source: 安全客-有思想的安全新媒体
date: 2022-12-02
fetch_date: 2025-10-04T00:16:04.794411
---

# Google UAF漏洞利用缓解技术MiraclePtr

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

# Google UAF漏洞利用缓解技术MiraclePtr

阅读量**1165815**

发布时间 : 2022-12-01 14:30:17

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

2022年9月13日，Google安全团队在其安全博客中发布了一篇关于MiraclePtr的文章，介绍了Google Chrome安全团队在缓解UAF漏洞利用上的进展。由于MiraclePtr并不是单指某一种智能指针技术，而是包含了Google安全团队在缓解UAF利用上的多次实验和尝试，本文也仅针对其最新启用的BackupRef方案做介绍，如有疏漏错误，敬请斧正，共同交流探讨。

## MiraclePtr

首先需要明确，MiraclePtr与unique\_ptr、weak\_ptr等C++中的原始智能指针并不是同一概念，它是Google安全团队在缓解由指针引起的内存破坏漏洞过程中，提出的多种方案集合，其本质是希望将原始指针迁移到带缓解方案的智能指针类，通过引用计数、指针标记等方式阻止攻击者对内存破坏漏洞被利用，重点解决的是UAF类型漏洞的悬垂指针可被利用的问题。

![]()

如上图，Google安全团队认为攻击者在针对Chrome的攻击过程中，通常需要组合一个渲染器漏洞利用和一个沙箱逃逸漏洞来达到完整利用的目的，MiraclePtr可以通过缓解UAF漏洞利用，有效的阻止攻击者针对浏览器主进程中UAF漏洞的利用（上图蓝色部分），让攻击者无法实现完整的利用链，从而降低漏洞危害。

![]()

在对Chrome历史可利用漏洞统计中，UAF类型漏洞占了几乎一半，因此MiraclePtr也尝试了包含BackupRefPtr、BorrowPtr、SafePtr、CheckedPtr、MTECheckedPtr、ViewPtr在内的多种方式来缓解UAF类型的漏洞利用，并在对比了各方案在性能开销、内存开销、安全保护、开发人员便利性上的优缺点后，近期在Windows和Android的Chrome 102稳定版中启用了BackupRefPtr，下文只重点介绍BackupRefPtr，其他方案详细信息查看参考链接中的内容。

![]()

## BackupRefPtr方案

BackupRefPtr提出了依赖“确定性引用计数”的指针保护方案，主要借鉴了CheckedPtr2、SafePtr和BorrowPtr的思路，并且需要Chrome的堆内存分配器PartitionAlloc支持。在2020年，Google ProjectZero在博客公布的一篇采用CPU漏洞侧信道攻击来泄漏缓存数据，从而实现Chrome沙箱逃逸的文章，证明了依赖指针标记的方案有潜在的被通过侧信道攻击的风险，出于安全性考虑，确定性引用计数的方案成了优先选择。

PartitionAlloc是Chrome中自行实现的堆分配器，主要在分配效率、内存空间利用率和安全性上进行了优化。PartitionAlloc使用2MB大小的超级页面作为普通数据桶，每个超级页面被分割成多个分区。第一个和最后一个分区是永久不可访问的，用来当作保护页面，在第一个分区页中间的一个系统页面保存了元数据（metadata），这些元数据提供了对内存对象的跟踪能力，BackupRefPtr使用到的引用计数就存储在metadata中。

![]()

在Chromium的源码实现中，BackupRefPtr是一个线程安全的引用计数指针类，可以非常简单的替换原始指针，Chromium团队在引入BackupRefPtr时也一次性替换了源码之中超过15000个原始指针。BackupRefPtr的引用计数存储在PartitionAlloc元数据中（与CheckedPtr2方案使用同一标志位），如果在销毁一个对象时，它的引用计数不为零，则会将该对象标记为被污染，此时程序不会真正的释放该内存，而是在再次访问被破坏的对象时，程序将发生主动崩溃。

该方案PoC代码如下，具体实现可参考Chromium源码raw\_ptr.h中的BackupRefPtrImpl类：

template <typename T>
class BackupRefPtr {
BackupRefPtr(T\* ptr) : ptr\_(ptr) {
if (!isSupportedAllocation(ptr))
return;

atomic*int& ref\_count = *(cast<atomic\_int*>(ptr) – 1);
CHECK(++ref\_count);
}
~BackupRefPtr() {
if (!isSupportedAllocation(ptr*))
return;

atomic*int& ref\_count = *(cast<atomic\_int*>(ptr) – 1);
if (—ref\_count == 0) // needed in case the BackupRefPtr outlives
// its pointee and has to free the slot
PartitionAlloc::ActuallyFree(ptr*);
}
T *operator->() { return ptr\_; }
T* ptr\_;
};

void *Alloc(size\_t size) {
void* ptr = ActuallyAlloc(size);
if (isSupportedAllocation(ptr)) {
int& ref\_count = *(cast<int*>(ptr) – 1);
ref\_count = 1; // We need to set the reference count to one initially
// otherwise |~BackupRefPtr| can trigger deallocation of
// an object that’s still alive.
}
return ptr;
}

void Free(void *ptr) {
if (isSupportedAllocation(ptr)) {
atomic\_int& ref\_count =* (cast<atomic\_int\*>(ptr) – 1);
if (ref\_count != 1)
memset(ptr, 0xcc, getAllocationSize(ptr));
if (—ref\_count != 0)
return;
}
ActuallyFree(ptr);
}

## 总结

BackupRefPtr通过上述机制，解决了悬垂指针（Dangling Pointer）被利用的问题，在该方案中，发生释放操作但引用计数不为0的对象并没有被真正释放，攻击者无法使用堆喷射等方式重新分配该对象的内存空间，并且在对象再次被访问时，该内存区域被填充了污染标志或发生主动崩溃，UAF漏洞被缓解为内存泄漏、断言失败或空指针等无法利用的崩溃。

整体而言，该机制的引入进一步降低了Chrome中可利用漏洞的比例，一定程度上提高了Chrome的安全性。

## 参考链接

1、Use-after-freedom: MiraclePtr

<https://security.googleblog.com/2022/09/use-after-freedom-miracleptr.html>

2、Pointer Safety Ideas [PUBLIC] – Comparison of Use-After-Free mitigation proposals

<https://docs.google.com/document/d/1qsPh8Bcrma7S-5fobbCkBkXWaAijXOnorEqvIIGKzc0/edit>

3、BackupRefPtr

<https://docs.google.com/document/d/1m0c63vXXLyGtIGBi9v6YFANum7-IRC3-dmiYBCWqkMk/edit#heading=h.jgclb3snutxw>

4、PartitionAlloc Design

[https://chromium.googlesource.com/chromium/src/+/main/base/allocator/partition\_allocator/PartitionAlloc.md](https://chromium.googlesource.com/chromium/src/%2B/main/base/allocator/partition_allocator/PartitionAlloc.md)

5、Escaping the Chrome Sandbox with RIDL

<https://googleprojectzero.blogspot.com/2020/02/escaping-chrome-sandbox-with-ridl.html>

6、MDS: Microarchitectural Data Samplin

<https://mdsattacks.com/>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**VLab**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283735](/post/id/283735)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t0155c2022df9e4d96d.png)VLab

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t0155c2022df9e4d96d.png)](/member.html?memberId=159421)

[VLab](/member.html?memberId=159421)

VLab 是墨云科技旗下的安全研究团队，专注于漏洞挖掘、红蓝对抗、APT攻防、前瞻性安全技术预研等方向。

* 文章
* **21**

* 粉丝
* **7**

### TA的文章

* ##### [远程办公，如何才能安枕无忧？方法来了](/post/id/277461)

  2023-01-11 14:00:47
* ##### [IP属地靠谱吗？或是一把双刃剑](/post/id/276005)

  2023-01-11 12:00:04
* ##### [如何提高漏洞挖掘效率？秘诀原来在Fuzzing里！](/post/id/273720)

  2023-01-09 14:41:03
* ##### [人人都说的SaaS，你真的了解它吗？](/post/id/276666)

  2023-01-07 10:26:52
* ##### [漏洞通告 | Oracle发布7月更新, 修复墨云科技报告的高危漏洞](/post/id/276830)

  2023-01-07 10:25:39

### 相关文章

* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃](/post/id/308349)

  2025-06-11 16:08:49
* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03

### 热门推荐

文章目录

* [MiraclePtr](#h2-0)
* [BackupRefPtr方案](#h2-1)
* [总结](#h2-2)
* [参考链接](#h2-3)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)