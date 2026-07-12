---
title: 从ISP路由器入侵到MediaTek内核0day：一位独立研究者的Linux内核远程代码执行
url: https://mp.weixin.qq.com/s/YwnRBHD5Gg8ioXwElwE3SQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:07.143722
---

# 从ISP路由器入侵到MediaTek内核0day：一位独立研究者的Linux内核远程代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0ETxmFbsz3iaoqMR6cwkJg5icZndnygOk4YGhricvPCsObjiaIjBynSrRTX8ufA1f0e8bwOza09sYcOVe1sfwCEBfAgVMkrF45ZmwI/0?wx_fmt=jpeg)

# 从ISP路由器入侵到MediaTek内核0day：一位独立研究者的Linux内核远程代码执行

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

摘要

在Linux内核安全与漏洞利用领域，远程代码执行（RCE）一直是研究者们追求的最高目标之一。2026年，独立安全研究员Victor Fresko（网名@hacefresko

）在其博客中详细记录了一次从个人ISP路由器入侵开始，最终发现并利用MediaTek内核0day漏洞的完整过程。该文章随后被收录进由知名研究员@andreyknvl 维护的《Linux内核利用资源合集》中的RCE章节，这标志着其工作获得了社区的高度认可。本文将深入剖析这一案例的技术细节、发现过程、利用技巧以及对内核安全研究的启示，旨在为漏洞研究者和内核开发者提供参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0Fud4kib9BMouRKntWem86KF8m084hhUKyzsJuVeUYZxyq2t7ycd2yBKibybuibyVUDmsuPSjcXcJdIsAcCmodBtws8uc16nACpZI/640?wx_fmt=png&from=appmsg)

引言

Linux内核作为现代操作系统的心脏，其安全性直接关系到无数设备和服务的稳定运行。然而，由于内核代码的复杂性和广泛使用，零日漏洞（0day）始终是攻击者眼中的“圣杯”。不同于实验室环境下的理论研究，真实世界的漏洞发现往往源于日常场景的意外发现。Victor Fresko的经历正是这样一个典型案例：他从自家ISP路由器的一次权限提升入手，逐步深入到MediaTek芯片的内核组件，最终实现了远程、未经身份验证的内核代码执行。

这一发现涉及多个CVE编号，包括CVE-2025-13942、CVE-2025-13943以及CVE-2026-20452。

这些漏洞的公开披露时间跨度较长，研究者也因此得以在负责任披露框架下完成详细的技术分析。Fresko的博客文章《From breaking into my ISP router to finding a MediaTek kernel 0day》不仅记录了技术路径，还展现了一名独立黑客在资源有限条件下的坚持与创新。

发现过程：从路由器到内核

一切始于Fresko对自家ISP提供的路由器的好奇。许多家庭路由器虽然表面上提供便利，但往往存在配置不当或固件漏洞。2025年底至2026年初，他在探索路由器时成功获得了初始访问权限。这一突破看似普通，却打开了通往更深层系统的大门。通过路由器，他发现了与MediaTek硬件组件的交互接口。

MediaTek作为全球领先的芯片设计厂商，其SoC广泛应用于路由器、智能设备和移动终端中，内核驱动代码自然成为重点攻击面。Fresko在后续帖子中提到，他首先定位到一个影响MediaTek特定组件的复杂bug。

该bug位于内核层面，初始表现为某种内存操作异常。从他的X平台记录来看，这一过程并非一帆风顺。2025年12月，他提到发现了一个更复杂的MediaTek内核bug，并预感利用它需要花费不少时间。

到了2026年1月，他获得了任意写原语（arbitrary write primitive），尽管可靠性不高，但这已经是重大进展——尤其考虑到这是一个完全远程、无需认证的漏洞。任意写原语的出现，让研究者能够尝试控制内核关键结构，如函数指针或关键数据区。2月，他宣布实现了远程代码执行（RCE）。

具体方法是结合任意读原语（arbitrary read），通过多次尝试覆盖函数指针，最终获得内核shell。这一阶段的挑战在于可靠性和稳定性：内核崩溃会重启设备，因此需要耐心调试和优化利用代码。3月，他透露下一篇详细博客正在撰写中，并计划在MediaTek官方披露漏洞后发布。整个过程体现了典型的“链式漏洞利用”思维：从外围设备切入，逐步提升权限，直至内核控制。

技术分析：利用原语与RCE实现

Fresko的利用策略核心在于原语构建（primitive construction）。在内核利用中，常见的路径包括：

* 信息泄露（Info Leak）：通过漏洞获得内核地址空间布局随机化（KASLR）的绕过信息。
* 任意读/写原语：这是本案例的关键。任意读允许研究者窥探内核内存，定位关键对象；任意写则能修改控制流。
* 函数指针劫持：通过覆盖内核中可预测或可定位的函数指针，实现代码执行跳转。

具体到MediaTek漏洞，CVE-2025-13942和CVE-2025-13943很可能涉及驱动层面的内存越界或不当处理，而CVE-2026-20452则可能是最终触发RCE的路径。Fresko提到，他最终使用任意读原语定位目标，并通过写操作覆盖函数指针。

这一技术在现代内核防护（如SMAP、SMEP、KPTI）日益加强的背景下显得尤为精巧。与传统本地提权不同，此漏洞的远程特性使其影响面极大。一台暴露在互联网上的受影响路由器或设备，可能成为攻击者进入内部网络的跳板。Fresko的利用还考虑了可靠性问题——内核panic会导致设备重启，这迫使他在利用代码中加入重试机制和状态恢复逻辑。

社区影响与资源收录2026年7月10日，Fresko在X平台发帖宣布，其MediaTek 0day分析文章被加入https://github.com/xairy/linux-kernel-exploitation仓库的RCE部分。

该仓库由@andreyknvl维护，是Linux内核安全领域公认的“传奇收藏”，收录了从2011年到2026年的诸多经典案例，包括BleedingTooth、Dirty Pipe等知名漏洞。这一收录具有里程碑意义。它不仅肯定了独立研究者的贡献，也为后来者提供了宝贵的第一手资料。仓库的RCE章节强调远程利用的技术演进，而Fresko的案例完美契合了“从现实设备出发”的趋势——现代攻击越来越倾向于供应链和嵌入式系统。

结论

Victor Fresko从一次ISP路由器入侵到MediaTek内核0day的完整旅程，生动诠释了现代内核利用研究的魅力与难度。其工作不仅技术含量高，更体现了开源安全社区的协作精神。当这篇文章被收录进经典资源库时，它已不再仅属于个人成就，而是成为Linux内核安全历史的一部分。对于有志于此领域的后来者，建议从阅读Fresko的原博客开始，结合xairy仓库的其他资源，动手实践（在合法测试环境）。安全研究之路漫长而充满挑战，但每一次发现都可能推动整个生态向更安全的方向迈进。

参考文献

* https://www.hacefresko.com/posts/rce-on-isp-router-and-mediatek-0day
* https://github.com/xairy/linux-kernel-exploitation

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EZbavcicHyUAZY4rRibfO31BULR8zBiaaD1FuXzD66rlu08borYqEI5Wjz6twL6z4Tgic4H4dlqHqYzwGC22OHyFpcIq3WwwYzjFA/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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