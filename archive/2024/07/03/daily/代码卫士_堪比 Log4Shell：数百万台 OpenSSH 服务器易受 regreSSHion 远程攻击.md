---
title: 堪比 Log4Shell：数百万台 OpenSSH 服务器易受 regreSSHion 远程攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519949&idx=1&sn=c2f44f54f4920efad56874aada444bc2&chksm=ea94bfa7dde336b1cbb8ba0a2984f58e65499be25dd7790f20f76ed57c06f723e6a39508289f&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-03
fetch_date: 2025-10-06T17:43:21.230824
---

# 堪比 Log4Shell：数百万台 OpenSSH 服务器易受 regreSSHion 远程攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMScDwDbicqqelIwhMSyOfp4VicsMibP7azIdfv8lE3uO78ibpvmm5wFuvk0pHzUnZ0feFgXtP7mUNvuRQ/0?wx_fmt=jpeg)

# 堪比 Log4Shell：数百万台 OpenSSH 服务器易受 regreSSHion 远程攻击

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMScDwDbicqqelIwhMSyOfp4VDm49xdxhbzwgNyoVTD68ibAWxPXlzqdbkm95VoqFLUPhOjxvMyIsS1w/640?wx_fmt=gif&from=appmsg)

**数百台 OpenSSH 服务器可能受一个新漏洞 CVE-2024-6387 影响，可被用于实现未认证的远程代码执行 (RCE) 后果。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMScDwDbicqqelIwhMSyOfp4VDMvVfaVM5v24oIGwhjlYu1IVCYJLIPhcXcvoHahLGzqCcrVlYSlvrQ/640?wx_fmt=gif&from=appmsg)

CVE-2024-6387也被命名为 “regreSSHion”，由网络安全公司 Qualys 发现，严重程度堪比2021年出现的漏洞 Log4Shell。

研究人员发现，该OpenSSH 服务器进程 “sshd” 受一个信号句柄竞争条件影响，可导致攻击者以 root 权限在基于 glibc 的Linux 系统上实现未认证远程代码执行后果。目前尚不清楚该利用是否同样适用于 Windows 和 macOS 系统。利用该 regreSSHion 漏洞可导致系统遭完全接管，导致恶意代码安装和后门创建。

OpenSSH用于在客户端服务器架构中为不安全网络提供安全的信道，广泛用于企业中，用于远程服务器管理和安全数据通信。研究人员指出，通过Shodan 和 Censys 服务搜索发现互联网存在1400多万台易受攻击的 OpenSSH 实例。Qualys 公司自身的客户数据显示，约70万个暴露在互联网上的系统似乎易受攻击。

研究人员指出，CVE-2024-6387是此前已修复漏洞CVE-2006-5051的回归。具体而言，该漏洞在2020年10月发布的 OpenSSH 8.5p1中重新引入。Qualys 公司提到，OpenBSD 系统得益于2001年引入的一个机制，并不受影响。最近，该漏洞偶然在 9.8p 1 中被删除。无法立即升级的组织机构可应用各厂商不久将发布的补丁。

Qualys 公司已发布关于 regreSSHion 的技术详情，但并未分享 PoC 代码，以阻止恶意利用。不过该公司发布了 IoC，帮助组织机构检测潜在的攻击活动。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[开源意味着不问责，我们准备好应对比 Log4Shell 更大的安全危机了吗？｜Log4j 一周年特别报道](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515742&idx=1&sn=45dc56d00db3c88017cd5d4dee0e8856&chksm=ea948f34dde3062255b8a0f7bc4fa0927fa8e9588a21d7281d1e928901837ad2d236afe3689c&scene=21#wechat_redirect)

[速修复！Apache Commons Text 存在严重漏洞，堪比Log4Shell](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514246&idx=1&sn=05c9cf544ef37daf01a04001b22b2584&chksm=ea9489ecdde300fae250e9a720d8fb6ccb7704229f946b796c6aec685c3e6a9446169ec5ad12&scene=21#wechat_redirect)

[黑客组织利用Log4Shell 漏洞攻击美国能源企业](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513979&idx=2&sn=72d6d5f48f01c937bda9d937519e416b&chksm=ea948611dde30f07cbdbf693f897a3068064aeca2729ee662032e6292a8aaa911ce77b17f7e2&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/millions-of-openssh-servers-potentially-vulnerable-to-remote-regresshion-attack/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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