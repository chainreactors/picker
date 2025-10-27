---
title: Abode 家庭安全包存在多个严重漏洞，可导致黑客劫持和禁用摄像头
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=4&sn=bb1d931819cef01583083f9eddee4a6d&chksm=ea9489a5dde300b349e85d3bf53d19d161712a5ac99dc81cf9fa3b09e54426e9bedd529d9889&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-10-26
fetch_date: 2025-10-03T20:55:59.342607
---

# Abode 家庭安全包存在多个严重漏洞，可导致黑客劫持和禁用摄像头

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJ9jzibl2KNqS9SCyy6w93ibibribRiaJmq7dQDYrk96yDk15Af4KKNjB6XWQ/0?wx_fmt=jpeg)

# Abode 家庭安全包存在多个严重漏洞，可导致黑客劫持和禁用摄像头

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

Abode Systems 修复了家庭安全包中的多个严重漏洞，其中一些漏洞可导致攻击者以根权限执行命令。

Abode Systems 是一家美国公司，出售智能DIY家庭安全系统和摄像头，其中包括可检测入侵或可疑行动的运动传感器。用户可通过应用或遥控器来安装或解除该系统。

用户可通过网站或手机上的应用来控制该系统，并将其与Amaza Alexa、Apple Homekit和Google Home集成。

思科Talos 团队的安全研究人员发现，该多功能安全包受多个漏洞影响，可导致攻击者更改用户密码、更改设备配置、注入任意代码、甚至完全关闭系统。攻击者可远程控制或禁用目标摄像头。

思科解释称，“这些设备中的多种软件功能中包含多个格式字符串注入漏洞，可导致内存损坏、信息泄露和拒绝服务后果。攻击者可发送恶意XML payload，触发这些漏洞。”

该家庭安全包中共有14个严重的操作系统命令注入漏洞（CVSS评分10分）。思科安全研究人员警告称，这些漏洞可导致攻击者以跟权限执行任意系统命令。

Abode Systems 包中还存在其它3个严重漏洞，分别是格式化字符串注入、认证绕过和整数溢出漏洞。9个漏洞是高危的格式化字符串注入漏洞，可通过特殊构造的HTTP请求、XCMD或配置值利用。其它高危漏洞还包括一个认证绕过漏洞、两个命令注入漏洞和一个双重释放漏洞。

思科已在7月份将这些漏洞告知Abode Systems公司并发布软件更新，修复所有漏洞。建议用户尽快更新至lota 6.9X或6.9Z版本。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[家庭路由器哪家强：固件漏洞多年不修复，更新无济于事](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493942&idx=1&sn=ed87582374731e65eebc4b72cb86ee0a&chksm=ea94d85cdde3514ab690bcb3520ce83e3d5fd43f1444197d7a32b6b65ffbb8ad88413e1c1db7&scene=21#wechat_redirect)

[遭暴露的神秘数据库把过半美国家庭的隐私翻了个底朝天](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489839&idx=1&sn=91affe20e0ccaf9aa2d68420b985f013&chksm=ea972845dde0a153d48b37d45e7d42a2ee2761ebaa24974302b85da1eef02b058a5ddc5f1522&scene=21#wechat_redirect)

[Guardzilla 家庭摄像头录像可遭任何人访问](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488844&idx=1&sn=fbae80922201e8dabe96492beef2d258&chksm=ea972426dde0ad30aa5fedefcb31663cf7e24bb79fe9703f2c0421985c12c09081ff5fa60637&scene=21#wechat_redirect)

[三星物联网中心竟然存在20个缺陷 多款著名智能家庭设备易遭攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487704&idx=2&sn=d48d5ffc3e09aada5e60ff4c65f6ac9a&chksm=ea9721b2dde0a8a4978647ee79cc17a92bea5b984b73fc6559d7398e367c902c983082774f1b&scene=21#wechat_redirect)

[罗技电子修复 Harmony Hub 家庭控制系统中的多个缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487056&idx=4&sn=8a384ae9a25d92d9603f48ec148ec9ff&chksm=ea973f3adde0b62c955176b813f3471ccbf35b787566f11b11595296caf9bc8c5ac2af60174b&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/critical-flaws-abode-home-security-kit-allow-hackers-hijack-disable-cameras

题图：Pixabay License

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