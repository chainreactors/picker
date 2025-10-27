---
title: SonicWall 提醒注意严重的SonicOS 访问控制漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520613&idx=1&sn=dc30b8ece16a42c6097ccba6e9284aa9&chksm=ea94a00fdde32919dccc17f899e4d9558219f654e103df2e221227381caaf4269a2ee6a1a5d5&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-29
fetch_date: 2025-10-06T18:05:09.787073
---

# SonicWall 提醒注意严重的SonicOS 访问控制漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSwic8nfoftiaOqRzibJpyh8DHBPyicyCVjHrhSOf6XjSRwaaNQ1SniaXFTqPyjTicwOBSwPicX6yIYld1iag/0?wx_fmt=jpeg)

# SonicWall 提醒注意严重的SonicOS 访问控制漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**SonicWall 公司的 SonicOS 产品易受一个严重的访问能控制漏洞(CVE-2024-40766) 影响，可导致攻击者获得对资源的越权访问权限或导致防火墙崩溃。**

该漏洞的CVSS v3评分为9.3，其攻击向量基于网络、复杂度低、无需认证或用户交互。SonicWall 公司在安全通告中提到，“SonicWall SonicOS 管理访问权限中存在一个访问控制不当漏洞，可导致越权访问资源，在某些情况下还可导致防火墙崩溃。该漏洞影响 SonicWall Gen5 和 Gen6 设备以及运行 SonicOS 7.0.1-5035和更早版本的 Gen7 设备。”

受影响的机型包括：

* Gen 5：运行5.9.2.14-12o 及更早版本的SOHO设备
* Gen 6：运行6.5.4.14-109n 及更早版本的Various TZ、NSA和 SM 机型
* Gen 7：运行SonicOS build 7.0.1-5035及更早版本的TZ和NSA机型

建议系统管理员升级至如下已修复该漏洞的版本：

* Gen 5设备升级至：5.9.2.14-13o
* Gen 6设备升级至：6.5.4.15.116n
* SM9800、NSsp 12400和NSsp 12800设备升级至：6.5.2.8-2n
* Gen 7设备升级至：SonicOS 固件版本高于7.0.1-5035的设备

用户可通过 mysonicwall.com下载这些安全更新。建议无法立即应用这些修复方案的用户将防火墙管理接口限制到可信来源或禁止从互联网访问WAN管理访问权限。SonicWall 公司还在帮助页面发布了相关指南。

SonicWall 防火墙广泛用于大量业务关键行业和企业环境中，常被用于获得对企业网络的初始访问权限。美国网络安全和基础设施安全局 (CISA) 自2022年起就提醒注意 SonicWall 设备漏洞遭活跃利用的情况。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[SonicWall紧急提醒：速修复多个严重的认证绕过漏洞！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517034&idx=1&sn=278a8688600c329d28ed0d3b4a718a2f&chksm=ea94b200dde33b16a06dee1ccc74e730dbb4bc108f1ca32266a7baf602bd1ef37e83faf331e1&scene=21#wechat_redirect)

[SonicWall：速修复这个严重的SQL 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513049&idx=2&sn=9b4e39de28718716d2dad0696dbb15ff&chksm=ea9482b3dde30ba55fbdc6aea7895291e3f8acb934a5200d4ee93d5c849936ba0a05ff2b45d0&scene=21#wechat_redirect)

[SonicWall 防火墙曝严重漏洞，有些设备仍无补丁](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511136&idx=1&sn=b9b7456e062bb08200fdbdc2eaa75ecc&chksm=ea949d0adde3141ca564f0fa7af067b5cc82bbb8299d4462c5f18a441e7f041dd23bd011b8a7&scene=21#wechat_redirect)

[SonicWall：速度修复这些严重的 SMA 100 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509639&idx=1&sn=6d251b70361554026c59db894db7d09f&chksm=ea9497eddde31efb4dd8258dbf09b60f21790f32504e477ebc9e952bf89a05f2c1e38d6e0a3e&scene=21#wechat_redirect)

[SonicWall 紧急提醒：EOL 设备正遭勒索攻击！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506376&idx=2&sn=ae05ce4a02a7c67ce2b51c8666d9d55d&chksm=ea94e8a2dde361b442b0e183dd82340ba45f3fb441a98add4376def73c8dedc58d1a577714d1&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-critical-access-control-flaw-in-sonicos/

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