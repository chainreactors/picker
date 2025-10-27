---
title: 思科满分漏洞可使黑客以root身份运行任意命令
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521416&idx=1&sn=dd174cdf4dec9fc76bae7be5c63bbd68&chksm=ea94a5e2dde32cf4e638ee3f72a13942731f386460354ea9e67337c58ebd9209a77a4d9c6b27&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-08
fetch_date: 2025-10-06T19:19:53.314338
---

# 思科满分漏洞可使黑客以root身份运行任意命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQpiac0ickgbnvticb5BSF2mkHACVV2MUc4ZkckMObhC1hPV1UzAqFmsLb3ibGJ9IEWXpI2UXkpic1xIvw/0?wx_fmt=jpeg)

# 思科满分漏洞可使黑客以root身份运行任意命令

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQpiac0ickgbnvticb5BSF2mkHfKzZYf9LTB8UUgibg34WhCxXfdN3NLhXUaXoVrFQpjtAjI7TwylZBicA/640?wx_fmt=gif&from=appmsg)

**思科修复了一个CVSS评分为10分的漏洞 (CVE-2024-20418)，它可导致攻击者以 root 权限在为工业无线自动化提供连接的易受攻击的 URWB 访问点上运行命令。**

该漏洞位于思科Unified Industrial Wireless Software 的 web 管理接口中。未认证的威胁行动者可在复杂度低的命令注入攻击中利用该漏洞，而无需用户交互。思科在本周三发布的安全公告中提到，“该漏洞是因为对 web 管理接口的输入验证不当造成的。攻击者可将构造的 HTTP 请求发送给受影响系统的 web 管理接口，利用该漏洞。成功利用将导致攻击者以 root 权限在受影响设备的底层操作系统上运行任意命令。”

思科解释称，该漏洞影响 Catalyst IW9165D Heavy Duty Access Points、Catalyst IW9165E Rugged Access Points and Wireless Clients 和 Catalyst IW9167E Heavy Duty Access Points，不过前提是它们在运行易受攻击的软件并启用了 URWB 操作模式。

思科产品安全事件响应团队 (PSIRT) 尚未发现公开的利用代码或该漏洞已遭利用的整局。

管理员可通过查看 “show mpls-config” CLI 命令是否可用的方式，判断 URWB 运营模式是否启用。如该命令不可用，URWB 未启用，则该设备不会受该漏洞影响。

思科还在7月份修复了位于思科 ASA 和 Firepower Threat Defense (FTD) 软件中的一个DoS 漏洞。该漏洞在4月份发现，当时被用于针对思科 VPN 设备的大规模暴力攻击活动中。

一个月之前，思科发布安全更新，修复了利用代码已公开的另外一个命令注入漏洞，可导致攻击者将在易受攻击系统上的权限提升为root。7月份，鉴于思科、Palo Alto 和 Ivanti 网络边缘设备遭多个漏洞（CVE-2024-20399、CVE-2024-3400和CVE-2024-21887）利用攻击，CISA和FBI 督促软件企业在交付前消除路径OS命令注入漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[思科紧急修复已遭利用的 ASA 和 FTD 软件漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521275&idx=1&sn=23094a8bbc6812308a558007e25112aa&chksm=ea94a291dde32b87e35eaab4a3eaca0db1c4a21c577bfdffa7e0bc64e4aa607f757182427737&scene=21#wechat_redirect)

[黑客在思科商店注入恶意JS，窃取信用卡和凭据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=3&sn=ca7a392b964011a90f44ef9b56046155&chksm=ea94a0c1dde329d7b3357897b0d476fbdcccdb403a0341d564f40687a51b08c0f26ca20939a6&scene=21#wechat_redirect)

[思科修复已有 PoC 的根提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=1&sn=00f735c28afb0e6cc70f919cade9dc5c&chksm=ea94a0c1dde329d7537d32cf0cc038587d8e6da619b0dc82fb99bb8917e432ece7028a7dd65c&scene=21#wechat_redirect)

[思科修复由NSA报送的两个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520566&idx=1&sn=74a7817b3955a25dccb8da1009e1b185&chksm=ea94a05cdde3294ad5842ade4355f86f5346f7c319e2260c6999b9fc84577eeff1b3f257c0f3&scene=21#wechat_redirect)

[思科：注意这些已达生命周期IP电话中的RCE 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=2&sn=bad61fd4a7dd0064d773564100fa0d93&chksm=ea94a1fbdde328ed9792a7787f0942bd8375dfb3d8e89c5d0413c4d48ad449acff958b59a1b2&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisco-bug-lets-hackers-run-commands-as-root-on-uwrb-access-points/

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