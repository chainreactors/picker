---
title: Linux 内核 14 年老漏洞可提权 root、逃出容器
url: https://mp.weixin.qq.com/s/XnQiwcBJ5vxSJQUtuirziQ
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:52.042103
---

# Linux 内核 14 年老漏洞可提权 root、逃出容器

# Linux 内核 14 年老漏洞可提权 root、逃出容器

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnvHNhv3tdSycy7UTMJetWPHKfIerYE0SXcr05s8PbBvqspzmyJrGTdricoUanpSwKJEDPiawFfoYj9ibnGWpV3nhc7F0YzHm2lMVw/640?wx_fmt=png&from=appmsg)

一个潜伏了 14 年的 Linux 内核漏洞，可让本地攻击者将权限提升至 root。在概念验证环境中，它甚至能逃出 Docker 容器，进而攻陷底层宿主机。

该缺陷存在于 Linux 的 AF\_ALG 用户态加密接口中，根源在于对同一 socket 进行并发写入不安全——这类 socket 通常用于 AES 加解密等操作。

由于无特权的本地进程就能访问该接口，它对内核研究者和攻击者而言都成了极具价值的攻击面。

### 14 年历史的 Linux 内核漏洞

STAR Labs 的安全研究员 Muhammad Alifa Ramdhan 于 2025 年在为 Google 的 kernelCTF 项目审计 Linux 内核代码时发现了该问题。他与同事 Bing-Jhong Billy Jheng 共同完成的研究表明，这个 bug 可以被开发成可靠的本地提权利用程序。据报道，这项 kernelCTF 提交获得了 113337 美元的奖励。

美国网络安全与基础设施安全局（CISA）也已将 CVE-2025-39964 列入“已在野被利用”的漏洞清单，进一步提高了修复的紧迫性。

### 漏洞原理：AF\_ALG 中的竞态条件

问题的核心在于 AF\_ALG 的 sendmsg() 处理路径存在竞态条件。正常情况下，内核会跨一个或多个请求收集加密输入，并使用分散 - 聚集列表（scatter-gather list）来追踪这些缓冲区。其中一个名为 merge 的上下文标志位，用于指示最后一个缓冲区还有未使用的页面空间，可以安全地追加新数据。

两个线程可以对同一个 AF\_ALG 操作 socket 发起写入。虽然 socket 锁能保护大多数状态变更，但内核在某个线程等待可写缓冲区空间时会释放这把锁——这就让另一个写入者有机会在原线程恢复执行前，篡改共享上下文。

据 IDNsec 的研究，攻击者可以通过操控时序，在最终 scatter-gather 列表没有任何有效条目的情况下，仍让 ctx->merge 保持启用状态。这会导致后续写入通过 sg[-1] 访问到目标数组之前的元数据。

这种越界访问之所以危险，是因为攻击者可控制的堆数据能够伪造 scatterlist 元数据。研究人员借此构造了一个 usercopy oracle，并最终推导出任意内核写原语。随后，利用程序覆盖了 core\_pattern——这是控制 Linux 如何处理进程 core dump 的内核设置。

当 core\_pattern 以管道符开头时，Linux 会将配置的程序作为 core dump 处理程序来执行。通过替换该值并触发子进程崩溃，概念验证代码便能以 root 权限运行攻击者指定的二进制文件。

由于容器与宿主机共享同一个内核，在受影响的配置下，同样的内核级原语也能实现 Docker 容器逃逸。

### 影响范围与修复

这段有问题的代码随 Linux 2.6.38 于 2011 年引入，暴露了约 14 年之久。受影响的版本包括各固定稳定版之前的内核（具体视发行版的 backport 情况而定）。公开公告指出的已修复版本包括 Linux 5.10.246、5.15.195、6.1.155、6.6.109、6.12.50 和 6.16.10。

Linux 上游开发者通过为 AF\_ALG 上下文增加排他性写所有权修复了该问题。补丁引入了 ctx->write 状态检查，使第二个并发写入者直接失败，而不再去改动 socket 的共享状态。

应尽快安装发行版提供的已修补内核包，并重启进入更新后的内核。组织应优先处理共享型 Linux 基础设施、容器宿主机、多用户系统，以及允许不受信任的本地代码或租户工作负载运行的环境。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过