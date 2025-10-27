---
title: F5 BIG-IP 修复高危提权漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521146&idx=1&sn=9082baa037a6e59fedb1cd685658ae1c&chksm=ea94a210dde32b06c309bdfeedbfb7bd2cf44ef71cdb29f41dc41e4af7102a5f3336ac6a51b3&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-19
fetch_date: 2025-10-06T18:52:48.613108
---

# F5 BIG-IP 修复高危提权漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTGcUT8A7hNUn6waAHhyqpMG5lSveHTLFic74f0mtFXuPgloEavibsw1H3iayLuUiaWzOrjRORkoibKjXA/0?wx_fmt=jpeg)

# F5 BIG-IP 修复高危提权漏洞

ByIonut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTGcUT8A7hNUn6waAHhyqpMaoYRyafO0SqIT6iaTjickLwCnicZ3rng5EhFnvaMfOjgWs2q65D5f1HVQ/640?wx_fmt=gif&from=appmsg)

**本周三，F5发布2024年10月季度安全通知，修复了位于BIG-IP和BIG-IQ企业产品中的两个漏洞。**

BIG-IP 更新修复了一个高危安全漏洞CVE-2024-45844，影响设备的监控功能，可导致认证攻击者提权并更改配置。F5公司在安全公告中提到，“该漏洞可能导致具有管理者 (Manager) 角色或更高权限的认证攻击者访问配置 (Configuration) 工具或 TMOS Shell (tmsh)，提升权限并贡献 BIG-IP系统。目前尚未出现数据暴露情况，只是控制面板问题。”

该漏洞已在 BIG-IP 版本17.1.1.4、16.1.5和15.1.10.5中修复，其它F5应用或服务并不受影响。组织机构可通过仅限可靠网络或设备访问BIG-IP 配置工具和通过SSH访问命令行来缓解该问题。使用自有IP地址访问该工具和SSH会被拦截。

F5公司表示，“由于该攻击是由合法的认证用户执行的，因此不存在允许用户访问配置工具或通过SSH 访问命令行的可行缓解措施。唯一的缓解措施是删除完全不可信用户的访问权限。”

CVE-2024-47139影响 BIG-IQ，是位于该设备用户界面未披露页面中的一个存储型XSS漏洞。具有管理员权限的攻击者如成功利用该漏洞，可以目前已登录用户的身份运行 JavaScript。

F5公司解释称，“认证攻击者可通过在BIG-IQ 用户界面存储恶意HTML或 JavaScript 代码的方式利用该漏洞。如成功利用，攻击者可在当前已登录用户的上下文，运行 JavaScript。如管理员用户能够访问 Advanced Shell (bash)，攻击者可利用该漏洞攻陷 BIG-IP系统。”

该漏洞已在 BIG-IQ 中心化管理版本 8.2.0.1和8.3.0中修复。作为缓解措施，建议用户在使用 BIG-IQ 用户界面后登出并关闭web浏览器，并使用其它 web 浏览器管理 BIG-IQ 用户界面。

F5公司并未说明这两个漏洞是否已遭在野利用。可参考该公司发布的季度安全通知公告了解其它信息。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA：黑客滥用F5 BIG-IP cookie 映射内部服务器](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521056&idx=1&sn=87bda00602d2d1a2718a0d4d0aef6585&chksm=ea94a24adde32b5c9d17667624bfb3939b23bdfacadb88d7c4951c0084e42f7a5753504eaf86&scene=21#wechat_redirect)

[F5修复BIG-IP 和 NGINX Plus 中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520531&idx=1&sn=3711327c08007954c754b1a665f4b963&chksm=ea94a079dde3296fb3e16aed65fdb526227e260cd11c96212ca1fd8bbde8380e989c2c1c2f57&scene=21#wechat_redirect)

[F5修复可导致RCE的 BIG-IP 认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518011&idx=2&sn=bc312f0c5810515223f4c329eb996ee3&chksm=ea94b651dde33f47c81f15553198c52a0b6b0ced84cf7a06c3f8cca4a506c0b5a7b5f9aa959c&scene=21#wechat_redirect)

[F5 BIG-IP 高危漏洞可导致拒绝服务和代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=1&sn=300b30047d4cb364fa903361e05d3052&chksm=ea948c2edde30538eab915c12ac7b6a1d83fe856638e1a22d727813fb060b9c1ad7f612dfa10&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/f5-big-ip-updates-patch-high-severity-elevation-of-privilege-vulnerability/

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