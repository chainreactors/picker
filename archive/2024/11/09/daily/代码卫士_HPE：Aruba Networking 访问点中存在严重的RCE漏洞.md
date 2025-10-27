---
title: HPE：Aruba Networking 访问点中存在严重的RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521429&idx=1&sn=8d164e84c96d33be487787e9f3024b73&chksm=ea94a5ffdde32ce9ee2d699be9c9511a6937a03eb2f97cedf23574474bd5683d6d9375d453b4&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-09
fetch_date: 2025-10-06T19:19:19.876244
---

# HPE：Aruba Networking 访问点中存在严重的RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTlsP2JygJSIicfMfhx5FBVuay6rUo9POlT6icWPuicXOGuo6UHm9TzqR7zBMD6r7jz0VwwjiaAoictq4w/0?wx_fmt=jpeg)

# HPE：Aruba Networking 访问点中存在严重的RCE漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTlsP2JygJSIicfMfhx5FBVuib1JZmLR9lC1JsVnVqOxEh2GDicugag1ibbMrdpqhT0HvFtyQQmrupRUA/640?wx_fmt=gif&from=appmsg)

**HPE (慧与) 公司发布了 Instant AOS-8和AOS-10 软件更新，修复了位于 Aruba Networking Access Point 中的两个严重漏洞CVE-2024-42509和CVE-2024-47460，它们的CVSS评分分别是9.8和9.0。**

这两个漏洞可导致远程攻击者通过将特殊构造的数据包经由 UDP 端口8211发送到 Aruba 的访问点管理协议 (PAPI)，执行未认证命令注入。这两个漏洞位于通过 PAPI 协议访问的命令行接口 (CLI) 服务中。

该更新还修复了另外四个安全漏洞：

* CVE-2024-47461（CVSS评分7.2）：认证远程命令执行漏洞，可导致攻击者在底层操作系统上执行任意命令。
* CVE-2024-47462和CVE-2024-47463（CVSS评分7.2）：认证攻击者可创建任意文件，可能导致远程命令执行后果。
* CVE-2024-47464（CVSS评分6.8）：认证攻击者可利用该漏洞通过路径遍历漏洞访问越权文件。

所有这柳哥漏洞影响 AOS-10.4.x.x:10.4.1.4和更老旧版本、Instant AOS-8.12.x.x:8.12.0.2及以下版本以及 Instant AOS-8.10.x.x:8.10.0.13及老旧版本。

慧与公司在安全公告中提到，该软件的更多版本已到达维护最后期限，如也受影响则不会收到安全更新。

**修复方案和应变措施**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTlsP2JygJSIicfMfhx5FBVuITPRwVOTC3mDDekvBTXh9IeKZ01XaItqPRibx8HZc4lK6qMQ2weDBpw/640?wx_fmt=gif&from=appmsg)

为了修复 Aruba Networking Access Points 中的漏洞，慧与公司建议用户将设备更新到如下软件版本或更新版本：

* AOS-10.7.x.x: 更新至10.7.0.0 及后续版本
* AOS-10.4.x.x: 更新至10.4.1.5 及后续版本
* Instant AOS-8.12.x.x: 更新至 8.12.0.3 及后续版本
* Instant AOS-8.10.x.x: 更新至 8.10.0.14 及后续版本

慧与还提供了应变措施，以缓解无法立即安装软件更新的情况。对于这两个严重漏洞，提议的应变措施是从所有不可信网络中限制/拦截对 UDP 端口8211的访问权限。对于余下问题，厂商建议将CLI和基于web的管理接口放在专门的第2层片段或VLAN，限制对它们的访问权限，并在第3层及以上通过防火墙策略控制访问权限，从而限制潜在的暴露情况。

虽然目前还未看到漏洞遭活跃利用的情况，但仍强烈建议应用安全更新和/或缓解措施。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[HPE 发布严重的 RCE 0day 漏洞，影响服务器管理软件 SIM，无补丁](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247499209&idx=2&sn=c481c08557d40e5796397f548beee4fc&chksm=ea94cca3dde345b5c5840b2c0abf89211f573250f55769dc0faa115b998b8ed13c183603b869&scene=21#wechat_redirect)

[只要29个字符 “A”，HPE iLO4 服务器认证轻松绕](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487566&idx=3&sn=402304d9804967f02a7a5c6555dcef8f&chksm=ea972124dde0a83268526f3976386f280d773cdc68873fa8a7c13997c351feef653bb55cd9cb&scene=21#wechat_redirect)

[Aruba 修复EdgeConnect 中的严重RCE和认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514198&idx=2&sn=7355930428f40ec6edfaaa22d7aee746&chksm=ea94893cdde3002ae09057a6941995beea58bffa9829737ad255d7b107096c28655b9bb0dfb1&scene=21#wechat_redirect)

[严重漏洞 TLStorm 2.0 影响大量 Aruba 和 Avaya 网络交换机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=3&sn=dbd40a2f39fbe2dbc3f9c231419eeb3c&chksm=ea949f0bdde3161dcdb5174d3558c3061c592544166666e55d459619aa5a8da5b4e7b78dca18&scene=21#wechat_redirect)

[惠普企业警告：Sudo 漏洞可使攻击者获得 Aruba 平台的 root 权限](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507580&idx=2&sn=a556d290841b3c2b031726bc075c1f8e&chksm=ea94ef16dde36600a21ca747c0a372c113f1e3765ea65f22821ccb9d2107936899b88541454d&scene=21#wechat_redirect)

[Aruba访问策略平台修复多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485519&idx=4&sn=68db7cc19a8c96244c0dbfd2f6193ab5&chksm=ea973925dde0b03322cafce3ccc4e0244e24ffde736b84128935ef46069f385b1b5df3900dbc&scene=21#wechat_redirect)

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