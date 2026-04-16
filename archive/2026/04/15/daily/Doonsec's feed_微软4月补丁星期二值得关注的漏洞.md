---
title: 微软4月补丁星期二值得关注的漏洞
url: https://mp.weixin.qq.com/s/aQdij4SsQhbE840Nf-hehw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:40.009275
---

# 微软4月补丁星期二值得关注的漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXldUDl2sIfcCVaAhvsAzR922vT1CFk1d1ErhJL7us5TEjqkkoUF8PKXNJUEbm4VxRXUbJu6A8nFGuxBnYeDhuicQz5AhBBN32o/0?wx_fmt=jpeg)

# 微软4月补丁星期二值得关注的漏洞

综合编译
综合编译

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**微软4月补丁星期二共修复167个漏洞，其中包括2个0day漏洞。在这些漏洞中，8个为“严重”级别，其中7个是远程代码执行漏洞，另外一个是拒绝服务漏洞。**

这些漏洞共有93个提权漏洞，13个安全特性绕过漏洞，20个远程代码执行漏洞，21个信息泄露漏洞，10个拒绝服务漏洞和9个欺骗漏洞。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXwLT6bMgQwnoLRcJmJU8rRRIvltVIVXIJQ9ZB30wQInFRiapH2Cjicicf484h3prx9ISA9p6kLf9srawRiaxiarZVciaAVyKXGCz618/640?wx_fmt=gif&from=appmsg)

**值得关注的漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXiacYP2IG0jGd1tg2Hiaf0xSHMOictfWyjMbkzUAd8Yux7x0Q9Gx7h9BOMjo0b0rC8PHLEG0PQC98XeogKLrXJ6d4Bt88fXicvl9M/640?wx_fmt=gif&from=appmsg)

**CVE-2026-32201**是位于Microsoft SharePoint Server 中的欺骗漏洞。虽然微软披露的信息有限，但该欺骗漏洞通常表现为跨站脚本（XSS）问题。攻击者可借此查看或篡改信息。对于可联网的SharePoint服务器，建议尽快测试并部署修复程序。

**CVE-2026-33825****是位于Microsoft Defender 中的权限提升漏洞**。该漏洞已公开披露，虽当前利用存在一定可靠性问题，但影响确凿。若依赖Defender进行防护，应尽快测试并部署修复。

**CVE-2026-33827****是位于Windows TCP/IP 中的远程代码执行漏洞。**未认证的远程攻击者可在无需用户交互的情况下利用该漏洞，具备蠕虫传播特性（在启用IPv6与IPSec的系统上尤为明显）。尽管为竞争条件漏洞，CVSS可利用性评级为“高”，但此类漏洞在Pwn2Own中常被成功利用。若系统运行IPv6，建议在公开利用代码出现前迅速部署修复。

**CVE-2026-33824****是位于Windows Internet Key Exchange (IKE) 服务扩展中的远程代码执行漏洞。**这是本月第二个具备蠕虫传播能力的漏洞。受影响系统需启用IKE服务。目前的缓解措施是在外围网络阻断UDP 500与4500端口以阻止外部攻击，但内部威胁仍可用于横向移动。使用IKE的企业应尽快测试并部署修复。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[微软3月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525382&idx=1&sn=a2fde96ec371ca6512bbfc25b9f18f99&scene=21#wechat_redirect)

[微软2月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525101&idx=2&sn=973a3ab33cfe6290521da6d90b4c743e&scene=21#wechat_redirect)

[微软：AI已用于攻击的每个阶段](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525365&idx=2&sn=dff79e089be7ac2054e918366b567b52&scene=21#wechat_redirect)

[微软紧急修复已遭利用的 Office 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524977&idx=1&sn=60a6766757d720c5fdd8346ba3b98c0b&scene=21#wechat_redirect)

[微软2026年1月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524868&idx=1&sn=511dcdb0c6fcd3cd07ef7783b225bcf4&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/microsoft/microsoft-april-2026-patch-tuesday-fixes-167-flaws-2-zero-days/

https://www.zerodayinitiative.com/blog/2026/4/14/the-april-2026-security-update-review

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