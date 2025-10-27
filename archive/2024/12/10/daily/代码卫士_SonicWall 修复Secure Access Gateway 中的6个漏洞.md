---
title: SonicWall 修复Secure Access Gateway 中的6个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521726&idx=2&sn=4020dbda138c28b7da91666b33eb120a&chksm=ea94a4d4dde32dc25a0dcbe4bb417dad621e9d9ab1c701a92e4cccf1dda90fcc8f7fc0d1eea9&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-10
fetch_date: 2025-10-06T19:40:02.578270
---

# SonicWall 修复Secure Access Gateway 中的6个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRfkdAjhq4h6zSDfhMlJwkuQ8fdcrYGw0hhiazicOrxQPnN9lcePC9OojeeWibVWice79k7dlZibJM19yg/0?wx_fmt=jpeg)

# SonicWall 修复Secure Access Gateway 中的6个漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**最近，SonicWall 公司修复了位于 SMA100 SSL-VPN安全访问网关中的多个漏洞，包括可导致远程代码执行的高危漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRfkdAjhq4h6zSDfhMlJwkuS4a4KVO57uPHNk8KiagiamlhDxAibJNMQvaRdOa52HbWqV5xGl0xz8r7Q/640?wx_fmt=gif&from=appmsg)

在这些漏洞中，最严重的是两个缓冲溢出漏洞，它们影响 web 管理界面和一个由 Apache web服务器加载的库。这两个漏洞的编号是CVE-2024-45318和CVE-2024-53703（CVSS评分8.1），可导致远程攻击者引发基于栈的缓冲溢出，从而可能导致代码执行后果。

该公司还修复了因使用 “strcpy” 函数引发的基于栈的缓冲溢出漏洞，CVE-2024-40763，它也可导致RCE后果。攻击者需要进行身份验证才能成功利用该漏洞。该公司修复的漏洞还包括位于 Apache HTTP Server 中的一个路径遍历漏洞CVE-2024-38475，可导致攻击者“将URL映射到可由服务器提供的文件系统位置”。另外，该公司还修复了一个高危的认证绕过漏洞CVE-2024-45319，可导致远程认证攻击者在认证过程中规避证书要求。

SonicWall 公司提到，SMA100 SSLVPN 备份代码生成器使用了可被攻击者预测的弱加密伪随机数生成器 (PRNG)，该漏洞编号为CVE-2024-53702。

这些漏洞影响运行固件版本 10.2.1.13-72sv和更早版本的SMA 100系列设备，已在固件10.2.1.14-75sv中修复。SMA1000 SSL VPN系列产品并未受影响。

SonicWall 公司表示尚未发现这些漏洞已遭在野利用的证据。鉴于攻击者一直以来针对已发布补丁的SonicWall漏洞，该公司建议用户尽快更新设备，以免遭攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[SonicWall 提醒注意严重的SonicOS 访问控制漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520613&idx=1&sn=dc30b8ece16a42c6097ccba6e9284aa9&scene=21#wechat_redirect)

[SonicWall紧急提醒：速修复多个严重的认证绕过漏洞！](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517034&idx=1&sn=278a8688600c329d28ed0d3b4a718a2f&scene=21#wechat_redirect)

[SonicWall：速修复这个严重的SQL 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513049&idx=2&sn=9b4e39de28718716d2dad0696dbb15ff&scene=21#wechat_redirect)

[SonicWall 防火墙曝严重漏洞，有些设备仍无补丁](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511136&idx=1&sn=b9b7456e062bb08200fdbdc2eaa75ecc&scene=21#wechat_redirect)

[SonicWall：速度修复这些严重的 SMA 100 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509639&idx=1&sn=6d251b70361554026c59db894db7d09f&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/sonicwall-patches-6-vulnerabilities-in-secure-access-gateway/

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