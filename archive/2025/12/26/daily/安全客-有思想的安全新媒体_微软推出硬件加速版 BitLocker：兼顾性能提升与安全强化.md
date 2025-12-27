---
title: 微软推出硬件加速版 BitLocker：兼顾性能提升与安全强化
url: https://www.anquanke.com/post/id/314033
source: 安全客-有思想的安全新媒体
date: 2025-12-26
fetch_date: 2025-12-27T03:21:04.934095
---

# 微软推出硬件加速版 BitLocker：兼顾性能提升与安全强化

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

# 微软推出硬件加速版 BitLocker：兼顾性能提升与安全强化

阅读量**13385**

发布时间 : 2025-12-26 14:47:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/microsoft-hardware-accelerated-bitlocker/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软正式推出**硬件加速版 BitLocker**，这一重大安全升级旨在彻底消除现代高速 NVMe 硬盘因加密操作产生的性能瓶颈。

随着存储设备读写速度不断提升，加密带来的 CPU 占用问题愈发引发关注，对于运行游戏、视频剪辑等高性能负载的用户而言尤为明显，而这项新技术恰好能解决该痛点。

### 现代 NVMe 硬盘面临的性能难题

随着 NVMe 存储技术迭代升级，这类硬盘可提供超高速数据传输速率，将系统性能推向全新高度。

但传统 BitLocker 采用纯软件加密模式，需占用大量 CPU 算力来完成数据实时加解密。

这就给高速 NVMe 硬盘造成了**性能瓶颈**，加密操作会消耗大量 CPU 运算周期。

在进行大规模视频处理、代码编译、游戏运行等高强度任务时，用户会明显感受到卡顿延迟。

对比传统软件版与硬件加速版 BitLocker 架构可见，借助专用加密引擎，硬件加速方案实现了性能大幅提升。
![]()

全新硬件加速版 BitLocker 将加密负载从主 CPU 转移至**现代片上系统（SoC）处理器内置的专用加密引擎**，从根源上优化性能与安全。

该方案实现两大关键优化：其一，加密卸载技术将大批量加密操作交由专用硬件处理，释放 CPU 资源用于其他任务，同时有效延长设备续航；其二，采用硬件保护密钥机制，在硬件层面对 BitLocker 加密密钥进行封装保护。

结合既有的可信平台模块（TPM）防护，进一步降低密钥在 CPU 与内存中被窃取的风险。

硬件加速版 BitLocker 随 2025 年 9 月 Windows 11 24H2 及 Windows 11 25H2 版本更新正式上线。

该功能会在支持设备上自动激活，需满足配备 NVMe 硬盘与兼容 SoC 这两个条件，默认采用**XTS-AES-256 加密算法**。
![]()

搭载酷睿 Ultra 3 系列处理器的英特尔 vPro 设备率先支持该功能，后续还将适配更多厂商的硬件平台。

测试数据显示，开启硬件加速版 BitLocker 后，存储性能已无限接近未加密状态下的 NVMe 原生速度。

与软件版 BitLocker 相比，该技术可减少约**70% 的 CPU 运算占用**，不仅能延长设备续航，还能同步提升存储的连续读写与随机读写性能指标。

微软计划在 2026 年初春更新中自动升级密钥长度，进一步提升兼容性。用户可通过管理员命令提示符运行命令 **manage-bde -status**，验证硬件加速版 BitLocker 是否启用。

当 SoC 专用加密功能正常运行时，命令输出结果的 “加密方式” 一栏会显示 “Hardware accelerated”（硬件加速）。

企业管理员需注意：若组策略配置指定了不支持的加密算法或密钥长度，可能会导致硬件加速功能无法启用。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/microsoft-hardware-accelerated-bitlocker/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314033](/post/id/314033)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/microsoft-hardware-accelerated-bitlocker/)

如若转载,请注明出处： <https://cybersecuritynews.com/microsoft-hardware-accelerated-bitlocker/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **860**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24

### 相关文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24
* ##### [潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击](/post/id/314062)

  2025-12-26 14:49:22
* ##### [“莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据](/post/id/314059)

  2025-12-26 14:48:34

### 热门推荐

文章目录

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