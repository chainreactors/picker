---
title: “乌贼出血”漏洞：已存在29年，由 Mythos Preview 辅助发现
url: https://mp.weixin.qq.com/s/WmcKqoAe_SHdKu5cL7h6rQ
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:04:25.266993
---

# “乌贼出血”漏洞：已存在29年，由 Mythos Preview 辅助发现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfWw3uYMxN5SYmW9uIH1fWL4HzsXULKvicLFwCWFWEEOroE8K513elCUicgPfy3xrpKTNQJwDJrymWC0Uum1hoZrd7oB4TaQBpuCU/0?wx_fmt=jpeg)

# “乌贼出血”漏洞：已存在29年，由 Mythos Preview 辅助发现

Swati Khandelwal
Swati Khandelwal

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUDGcPcJNqP6Yhz5JbccfhibiaOVRo2tgvic15bqwLFpbHvvnalicvb2uu1dTemibPE4hExibfMaibzDLP2HYYsYstiboHCr0gKyWCVW5g/640?wx_fmt=gif&from=appmsg)

**Calif.io****公司的研究人员披露称，Squid web 代理中存在一个被称为“乌贼出血 (Squidbleed)”的堆越界读漏洞 (CVE-2026-47729)，可用于将其它用户的明文 HTTP 请求如任何凭据或会话令牌等泄露给有权限通过同一代理发送流量的任何人。该命名参考了以同样方式泄露内存的“心脏出血 (Heartbleed)”漏洞的命名方式。**

该漏洞可追溯至1997年的一项FTP解析更改，至今仍存在于Squid的默认配置中。Squid将该攻击描述为来自可信客户端的攻击：引发攻击的是已被允许使用该代理的人员，而非互联网上的任意随机主机。而这也符合Squid的常见部署场景，例如学校、办公室和公共Wi-Fi等共享网络。在这些环境中，攻击者只是同一代理的另一个用户。

该泄露也仅限于Squid能够读取的流量。常规HTTPS通过不透明的CONNECT隧道传输，因此Squid无法窥见其内部；被泄露的流量是明文HTTP，以及Squid进行解密和检查的TLS终止设置。攻击者还需要代理能够访问其控制的21端口的FTP服务器。FTP及其端口默认均为开启状态。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXRKeuWiaw3eVOO7UtuRLksSppianpPczpCTArvJAaV1ImKXMObvHEvUtUrAaErvDf7aJictblTv0yzYo0iaL7icnibW1q4dbkQGKlg4/640?wx_fmt=gif&from=appmsg)

**泄露如何发生**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfU0M0xJYQC8A7hLKuevZq8bFd14gdMgkk4Hpic6JjRsBIia6mYW4cRWnEVEqWTG2oRIOVrtIvv2NKT0iciaDZ0jyQKTK9vicP7emSibE/640?wx_fmt=gif&from=appmsg)

该漏洞位于Squid的FTP目录列表解析器中。为了处理那些在列表中添加额外空格以填充的旧版NetWare服务器，代码使用一个循环来跳过空白字符：while (strchr(w\_space, \*copyFrom)) ++copyFrom;。

如果攻击者的FTP服务器发送的列表行在时间戳之后立即结束，且没有文件名，那么copyFrom会落在字符串的空终止符上。strchr会将该终止NUL字符视为其搜索的字符串的一部分，因此它会返回一个指针而非NULL，并且循环永远不会停止。它会越过缓冲区末尾进行读取，然后xstrdup将后续内容作为文件名复制回给攻击者。

被泄露的字节即为有效信息。Squid在重用已释放的内存缓冲区时不会将其清零，因此一个4KB的缓冲区如果最近刚存放过受害者的HTTP请求，则其中大部分内容仍然保留。一条较短的FTP行只会覆盖前几个字节；越界读取则会返回剩余部分。

研究人员演示了如何从一个共享同一代理的受害者处提取Authorization头，以此冒充该用户。该漏洞的概念验证代码已公开，不过截至撰稿时，尚未有在野利用的报道。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfV5cqLywbE3OibfCNzrlhhNHNlu1ILxjKnCruX3Amo9y5domiaQehNDkdlH2gTiaDa6ERRyKRJdPkHABUIW28cXufPCmQRS8InYiaY/640?wx_fmt=gif&from=appmsg)

**应对措施**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWcpyLs95l6n0zGcHNAzYqXry8EcA1xIRFgMxQVdrSdCc6BRK3ktWcLv3zNElKCnxaU1sqiacsPBrgoRuAibSwdCynbDicPT9W31o/640?wx_fmt=gif&from=appmsg)

若用户选择修复，则需验证修复方案本身，而不仅仅是版本号。务必确认防护措施已存在于FtpGateway.cc中，或检查所使用的发行版向后移植的补丁——因为发行版会构建自己的版本（例如Debian打包了Squid 5.7）。

另外关于该漏洞的公开讨论情况仍存在不一致：维护者Amos Jeffries首先表示Sq uid 7.6携带了该修复，随后更正为7.7 版本；而在6月22日，Debian的Salvatore Bonaccorso指出，所引用的提交看起来已包含在7.6中。

该修复方案很小，即在易受攻击的strchr调用之前添加了一个空终止符检查。该修复于4月合并到开发分支，5月合并到v7分支。Squid 7.6确实单独修复了一个无关的cache\_digest堆溢出漏洞CVE-2026-50012。

研究人员推荐的更干净做法仍然是关闭FTP。Chromium多年前就已弃用FTP，大多数网络几乎不再使用它，因此无论用户运行何种构建版本，禁用它都可以免费消除此攻击面。

虽然该风险是真实存在的，但范围有限。SUSE将该漏洞的严重程度评级为中等即CVSS评分为6.5，而它的向量解释了该评分：攻击者需要代理访问权限（低权限），且仅影响机密性，不涉及完整性或可用性。

Calif公司致谢Anthropic公司的Claude Mythos Preview（即Project Glasswing背后的模型），称该模型几乎立即捕捉到了strchr的异常行为——这种深藏的解析器漏洞，而这正是AI代理在其他地方（包括FFmpeg）也持续发现的问题类型。Calif公司认为，Squid的FTP代码可能不会是它忘记停止读取的最后一个地方。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[“心脏出血”后，OpenSSL 起死回生靠什么？](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492028&idx=2&sn=086dfceed7b069ce172b93d1dbad66a8&scene=21#wechat_redirect)

[甲骨文紧急修复等同于“心脏出血”的JOLTandBleed漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485428&idx=1&sn=a5a9a311444fc8ee2a272a3317622594&scene=21#wechat_redirect)

[“心脏出血”漏洞依然活跃 20万台物联网设备易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485882&idx=4&sn=c71b98f006ae0f781e495a4a9ac5c5b9&scene=21#wechat_redirect)

[Stagefright: 比“心脏出血”更难修复的安卓漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485918&idx=1&sn=d8c69f27d8a4772f52500d7d9dddfc4a&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

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