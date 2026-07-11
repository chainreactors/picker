---
title: PAN-OS 高危缓冲溢出漏洞可导致任意代码执行
url: https://mp.weixin.qq.com/s/JWa9J2xcEmj8JGIZQgAVZA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:01:10.001081
---

# PAN-OS 高危缓冲溢出漏洞可导致任意代码执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfVJIqnc0Ezl7BS0XrOPGiazZBn6GGU0BA4CCicIUjickvdANt1Ty35Ria3lIx4NYHJ5T8fKhdd33gjicpsibONyKOx8F6Nbw2frFsq3o/0?wx_fmt=jpeg)

# PAN-OS 高危缓冲溢出漏洞可导致任意代码执行

Do Son
Do Son

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Palo Alto Networks****公司披露了一个****PAN-OS****缓冲区溢出漏洞（****CVE-2026-0288****，****CVSS****评分****7.2****）。该漏洞位于****User-ID****终端服务器代理中。网络上的未认证攻击者可利用该漏洞导致防火墙崩溃或执行代码。该公司称尚未发现已知的利用行为。**

PAN-OS防火墙守护着众多企业网络的边界。因此，允许任意代码执行的漏洞尤为严重。该漏洞无需登录，也无需用户交互。值得注意的是，另一个相关的PAN-OS漏洞CVE-2026-0300已遭在野利用，并于2026年5月被列入CISA的KEV目录。这一前车之鉴提高了快速修补的紧迫性，尽管该漏洞目前尚无被利用的迹象。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWqYfaUve45wyHhzYqFYrd7Zz3XkuWsDLuRplt0ibMxmiaF7CiagmwBQMTuodgsVB0G3gE4qy6AL0D7CY5FNs82ISUloic2YTzS854/640?wx_fmt=gif&from=appmsg)

**攻击方式**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUXRrNAaI05W4icvLumsXvacqB2Prxf3o7OnkiaNH1kJL84tyP2XibhstJpFw8tWSicBsgMUDicubZBdrFDSVVfzjFsfXibApQf9b0Yc/640?wx_fmt=gif&from=appmsg)

该漏洞源于终端服务器代理中的一组缓冲区溢出。攻击者向TSA服务发送特殊构造的网络流量，这些输入会溢出缓冲区，导致拒绝服务，或可能实现任意代码执行。只有配置了至少一个TSA条目的设备才受影响。管理员可以在“设备 > 用户识别 > 终端服务器代理”下进行确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVkQby0J2FXwcL8mMXW8nSdHpSic3xDKUUYV9fq1ugoXoYnVOMPASM7EjlvIFY9cUp5c6NGe8AHpNCicibfzypK28qgqYjtyNHR1Q/640?wx_fmt=gif&from=appmsg)

**受影响版本**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUDQeBgGRgHhcXkzGsbeW1lBp5ic1VfvIcHn7IoLyBLicMErLP4ricggjuDba7ia0woq5xmIXBhtenubXhDYkD0VEV51NlyrI7CkuI/640?wx_fmt=gif&from=appmsg)

该漏洞影响PAN-OS 12.1、11.2、11.1和10.2的特定修复版本之前的版本。Cloud NGFW和Panorama不受影响。Prisma Access有两个分支被评为中等严重性。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWHY4RiaY1kmtJUaEmZWNvNicDByD4vXPubKluy1fLUYdtUwlnypM1D53WBics4ap10J8KpfjNgkw9SgibAKBLPibrXv8g3psQrALp0/640?wx_fmt=gif&from=appmsg)

**补丁与缓解措施**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXAXAZ0iauNR2pIkgy6u2dOdCsHIqrfpdc6KObX8H5uZB4Idpvriacv6REs3ZrT7ga6o71ZQ1uTx5BZReoUDk1HwnDkZc6CEcazg/640?wx_fmt=gif&from=appmsg)

用户应更新到已修复的版本，如12.1.8、11.2.13、11.1.16或10.2.18-h8。用户需在Palo Alto的安全公告中确认所用分支的确切修复版本。在完成修补之前，应将TSA连接限制为受信任的内部IP地址。仅此一步即可大幅降低该PAN-OS缓冲区溢出漏洞带来的风险。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[PAN-OS GlobalProtect 认证绕过漏洞已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526149&idx=1&sn=64865321252297906000fede942608f5&scene=21#wechat_redirect)

[Palo Alto 提醒注意严重的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525932&idx=2&sn=a1f8acec7865ec3eec445777c4ad6251&scene=21#wechat_redirect)

[Palo Alto Networks 修复PAN-OS 中的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522232&idx=2&sn=3bc7a4466c3c33ff643ca604524fa401&scene=21#wechat_redirect)

[Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/pan-os-cve-2026-0288/

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