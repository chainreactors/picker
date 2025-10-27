---
title: OpenSSH 新漏洞使SSH服务器易受中间人和DoS 攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522278&idx=1&sn=7cfb4b23ad311c542e16a6d9517313ce&chksm=ea94a68cdde32f9ac833afa12536d7b2cd2202b3e8d1fa6d9863779bcceec652fa2982c74202&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-20
fetch_date: 2025-10-06T20:35:30.725412
---

# OpenSSH 新漏洞使SSH服务器易受中间人和DoS 攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQhr6jXufaic6PJrZauaJPDaNjOJpt2Nj37vgSHIA4vQd8ib390ekab5YqibpDgBzL16Qh1z2kpEsPyA/0?wx_fmt=jpeg)

# OpenSSH 新漏洞使SSH服务器易受中间人和DoS 攻击

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**OpenSSH 发布安全更新，修复了一个中间人攻击和一个拒绝服务 (DoS) 漏洞，其中一个在十几年前就被引入。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQhr6jXufaic6PJrZauaJPDaiaDfdBeSXS93vzibHhX1Kvdw2OicmKPt72n991gCXvqn6fIUtmR0dMFlQ/640?wx_fmt=gif&from=appmsg)

这两个漏洞由 Qualys 公司发现，该公司还向OpenSSH的维护人员演示了其可利用性。OpenSSH是SSH协议的免费开源实现，为通过不可信网络进行的安全远程访问、文件传输和隧道提供加密通信。它是全球使用最广泛的工具之一，广泛用于企业环境、IT、DevOps、云计算和网络安全应用中的Linux和基于Unix（BSD、macOS）系统。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQhr6jXufaic6PJrZauaJPDaD1ibGiaFMEGFsj7NfhCojnSXl4L07PJSBB07fT9Nq8ENpy0ywg1icNS0A/640?wx_fmt=gif&from=appmsg)

**两个漏洞**

中间人攻击漏洞CVE-2025-26465在2014年12月发布的OpenSSH 6.8p1中引入，因此存在的时间已超过十年。该漏洞影响启用“VerifyHostKeyDNS”选项的OpenSSH 客户端，可导致威胁行动者执行中间人攻击。

Qualys 公司提到，“不管VerifyHostKeyDNS 的选项被设置为 ’yes’ 还是’ask’（默认为’no’），针对OpenSSH客户端的攻击 (CVE-2025-36465) 都能执行成功，且无需用户交互，并不取决于DNS中的 SSHFP 资源记录（SSH指纹）是否存在。” 当启用客户端时，因错误处理不当问题，攻击者可在验证过程中强制出现内存错误，诱骗客户端接受恶意服务器的密钥。

通过拦截SSH连接并展示具有过多证书扩展的一个庞大的SSH密钥，攻击者可耗尽客户端的内存、绕过主机验证并劫持会话以窃取凭据、注入命令并提取数据。尽管OpenSSH默认禁用 “VerifyHostKeyDNS” 选项，但2013年至2023年的FreeBSD上是默认启用的，导致很多系统易受这些攻击影响。

第二个漏洞是CVE-2025-26466，它是在2023年8月发布的OpenSSH 9.5p1中引入的一个预认证拒绝服务漏洞。该漏洞是在密钥通信过程中由不受限内存分配问题造成的，可导致不受控制的资源耗尽。攻击者可反复发送小规模的16字节ping信息，强迫OpenSSH在没有即时限制的情况下缓冲256字节的响应。

在密钥通信过程中，这些响应被永久存储，导致内存过度耗尽和CPU过载，从而可能导致系统崩溃。虽然利用该漏洞的后果不如第一个中间人攻击漏洞的后果严重，但在认证前进行利用的情况仍然是造成破坏的高风险因素。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQhr6jXufaic6PJrZauaJPDaD1ibGiaFMEGFsj7NfhCojnSXl4L07PJSBB07fT9Nq8ENpy0ywg1icNS0A/640?wx_fmt=gif&from=appmsg)

**安全更新发布**

OpenSSH 团队刚刚发布了9.9p2版本，修复了上述两个漏洞，建议所有用户尽快更新至该版本。

另外，除非绝对必要，建议禁用VerifyHostKeyDNS，并依赖手动密钥指纹验证，确保SSH安全连接。建议管理员执行严格的连接率限制并监控SSH流量中的异常模式，提前阻止潜在的攻击活动。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[OpenSSH 易受RCE新漏洞影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520029&idx=2&sn=b58737a69aeafc6a694ae82500739603&scene=21#wechat_redirect)

[堪比 Log4Shell：数百万台 OpenSSH 服务器易受 regreSSHion 远程攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519949&idx=1&sn=c2f44f54f4920efad56874aada444bc2&scene=21#wechat_redirect)

[Terrapin 攻击可降低 OpenSSH 连接的安全性](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518446&idx=2&sn=97a0cfc5e54ab41c3e6241a76bd6a019&scene=21#wechat_redirect)

[OpenSSH 修复预认证双重释放漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515493&idx=1&sn=10c488e3633714016c305152a77ee339&scene=21#wechat_redirect)

[OpenSSH 后门来一打！保证你没见过!](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488712&idx=1&sn=d68bb7652919d3c237e635d24db38da0&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/new-openssh-flaws-expose-ssh-servers-to-mitm-and-dos-attacks/

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