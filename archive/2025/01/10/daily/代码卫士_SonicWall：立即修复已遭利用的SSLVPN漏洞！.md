---
title: SonicWall：立即修复已遭利用的SSLVPN漏洞！
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522025&idx=1&sn=5fd3517667080fa3c953fe0d2afa966b&chksm=ea94a783dde32e9525f0fb0b763e86e9b9f4e7b2b0e8472055ffc4a880291d848b42241fefb1&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-10
fetch_date: 2025-10-06T20:09:02.054889
---

# SonicWall：立即修复已遭利用的SSLVPN漏洞！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQ8fh197ibfsdMWeicqHI7zHib4FIGOIgicqTzKjQooTPK3ugUeFCwcmv0jibkARablAj8h8XD81nAgwGQ/0?wx_fmt=jpeg)

# SonicWall：立即修复已遭利用的SSLVPN漏洞！

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**SonicWall 公司向客户发送邮件，督促他们升级防火墙的 SonicOS 固件，修复位于SSL VPN和SSH 管理中的一个“疑似遭真实利用的”认证绕过漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ8fh197ibfsdMWeicqHI7zHibBAib0KqYKM4b2ic0xSAaHj4KscgW4kGic4BMibtkj5IhTzhYaxCPH85Ppw/640?wx_fmt=gif&from=appmsg)

SonicWall 公司向客户发送邮件称，补丁已在当地时间昨天推出，所有受影响客户应当立即安装这些补丁以阻止漏洞遭利用。邮件提到，“我们已发现一个高危（CVSS评分8.2）防火墙漏洞，启用了SSL VPN或SSH 管理功能的客户易受影响，用户应立即升级至将于明天（2025年1月7日）发布的最新固件版本进行缓解。该固件升级还包含了对于其它严重程度较低漏洞的缓解措施。”

SonicWall 公司发布安全通告，为该漏洞分配编号CVE-2024-53704（CVSS v3.0评分8.2，高危级别）并表示，它影响多个第六代和第七代防火墙，即运行6.5.4.15-117n及和老旧版本以及7.0.1-5161和更老旧版本。

建议受影响用户升级至如下版本，修复该安全更新：

* Gen 6 / 6.5 硬件防火墙：SonicOS 6.5.5.1-6n 或更新版本
* Gen 6 / 6.5 NSv 防火墙：SonicOS 6.5.4.v-21s-RC2457 或更新版本
* Gen 7 防火墙：SonicOS 7.0.1-5165或更新版本；7.1.3-7015或更高版本
* TZ80：SonicOS 8.0.0-8037或更新版本

此外，该公告还列出了三个中危或高危漏洞，概述如下：

* CVE-2024-40762：SSL VPN 认证令牌生成器使用了一个若加密伪随机数生成器，在某些情况下可导致攻击者预测令牌并绕过认证。
* CVE-2024-53705：SonicOS SSH 管理界面中存在一个服务器端伪造漏洞，可导致远程攻击者与任意IP地址和端口建立TCP连接，不过前提是攻击者已登录至防火墙。
* CVE-2024-53706：Gen7 SonicOS Cloud NSv（AWS和Azure版本）中存在一个漏洞，可导致低权限的认证攻击者提升至根权限，可能导致代码执行后果。

SonicWall 公司还列出了一些缓解措施，如限制对受信任来源的访问权限，并在非必要条件下限制来自互联网的访问。要缓解这些SSH漏洞，建议管理员限制防火墙SSH管理访问并考虑禁用来自互联网的访问。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[SonicWall 修复Secure Access Gateway 中的6个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521726&idx=2&sn=4020dbda138c28b7da91666b33eb120a&scene=21#wechat_redirect)

[SonicWall 提醒注意严重的SonicOS 访问控制漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520613&idx=1&sn=dc30b8ece16a42c6097ccba6e9284aa9&scene=21#wechat_redirect)

[SonicWall紧急提醒：速修复多个严重的认证绕过漏洞！](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517034&idx=1&sn=278a8688600c329d28ed0d3b4a718a2f&scene=21#wechat_redirect)

[SonicWall：速修复这个严重的SQL 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513049&idx=2&sn=9b4e39de28718716d2dad0696dbb15ff&scene=21#wechat_redirect)

[SonicWall 防火墙曝严重漏洞，有些设备仍无补丁](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511136&idx=1&sn=b9b7456e062bb08200fdbdc2eaa75ecc&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/sonicwall-urges-admins-to-patch-exploitable-sslvpn-bug-immediately/

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