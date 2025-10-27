---
title: D-Link 决定不修复这个严重漏洞，影响6万多台 NAS 设备
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=2&sn=1ddad70ced916d3fad493805c8d04d62&chksm=ea94a5cadde32cdc87209411ca0df0d1e6fb8603675b20af28c666afba8db536266ea1921ce3&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-12
fetch_date: 2025-10-06T19:19:17.672713
---

# D-Link 决定不修复这个严重漏洞，影响6万多台 NAS 设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTwbNlrPXlJtdcFv34QtDk4y6EwSgaujTqJGjfPKvfGibQfb1EsI4XBgJv71e35Z2qMMaicJkNLoecw/0?wx_fmt=jpeg)

# D-Link 决定不修复这个严重漏洞，影响6万多台 NAS 设备

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTwbNlrPXlJtdcFv34QtDk4sZDy0XFZiccKMvjtqfsnXLEvxD0ntBEFqiaNZ1RTIaCEmw0c7P0nPKNg/640?wx_fmt=gif&from=appmsg)

**超过6万台已达生命周期的 D-Link NAS 设备易受命令注入漏洞 (CVE-2024-10914) 影响且利用已公开。**

该漏洞的CVSS评分为9.2，位于 “cgi\_user\_add” 命令中，因该名称参数的清理不充分而导致。未认证攻击者可将特殊构造的HTTP GET 请求发送到设备，利用该漏洞注入任意 shell 命令。

该漏洞影响常被小企业使用的多款 D-Link NAS 设备：

* DNS-320 版本1.00
* DNS-320LW 版本 1.01.0914.2012
* DNS-325 版本1.01、1.02
* DNS-340L 版本 1.08

研究人员 Netsecfish 表示，利用该漏洞要求将“特殊构造的 HTTP GET 请求发送给NAS设备，其中名称参数中包含恶意输入”。

```
Curl "http://[Target-IP]/cgi-bin/account_mgr.cgi cmd=cgi_user_add&name=%27;<INJECTED_SHELL_COMMAND>;%27"
```

该研究员解释称，“该 curl 请求构建的URL，通过包含注入shell命令的名称参数，触发 cgi\_user\_add 命令。”

从FOFA平台上搜索易受该漏洞攻击的 D-Link 设备可看到，从41097个唯一IP地址返回61147个结果。D-Link 在安全公告中确认将不提供CVE-2024-10914的补丁，并建议用户弃用易受攻击的产品。如暂无法弃用，用户至少应当将其与公开互联网断开或将其置于更严格的访问条件下。

该研究员还在今年4月份发现了一个任意命令注入漏洞和硬编码后门漏洞CVE-2024-3273，影响的D-Link设备型号与CVE-2024-10914基本一样。当时FOFA扫描返回92589个结果。

D-Link 公司的一名发言人表示，该公司将不再制造NAS设备，受影响产品已到达生命周期且不再接受安全更新。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[D-Link 修复D-Link D-View 8软件中的认证绕过和 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516588&idx=1&sn=981ba7ac004cc1b05279618b3be57e1f&chksm=ea94b0c6dde339d00da0ef0e86a316035b22c4f86ccc177e5420b43bcffb6d47b13200edab35&scene=21#wechat_redirect)

[D-Link 修复多个硬编码密码漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506450&idx=3&sn=e93472d0452c2f5615ef9f11c0f4cb71&chksm=ea94eb78dde3626e9370f9fdd70b4dc576638d8253da74e5bd0a3e1371cf537b4869f1577713&scene=21#wechat_redirect)

[Synology：速修复零点击RCE漏洞，影响数百万 NAS 设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521406&idx=2&sn=1a37afaf7e8cd1893b64cc0183aae730&chksm=ea94a514dde32c02df3f45ffe36a3bc5f29632e75d87ca05c0296cf0f528796ba0a3a5facadd&scene=21#wechat_redirect)

[QNAP提醒注意NAS设备中严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519033&idx=2&sn=59f095fb0e0636ab2257aaf9cc7d7e27&chksm=ea94ba53dde333458f33894831a44c39ac69f925de1b9e7262ba526c9c4ebe0f113e84a4f2e5&scene=21#wechat_redirect)

[美国国家安全委员会不慎泄露2000多家机构凭据，包括NASA、特斯拉等](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517538&idx=1&sn=650f77bfd40168fc3045174a8fa46fda&chksm=ea94b408dde33d1eefe60a4a306a117abc75eb1f6bb4cddddacecf74cd9a39cab6d9f55a6d3f&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/d-link-wont-fix-critical-flaw-affecting-60-000-older-nas-devices/

题图：Pixabay License

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