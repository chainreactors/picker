---
title: 朝鲜APT被指利用IE 0day 发动供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521165&idx=1&sn=7b3b7e63cd3887724011c1eb4c584441&chksm=ea94a2e7dde32bf12a8f6cd4ff3687c49864e1369095f8f1fad77a56829cf6a8b8d01cf23abd&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-22
fetch_date: 2025-10-06T18:51:54.587762
---

# 朝鲜APT被指利用IE 0day 发动供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQMmELRlnGCmKmc9MJEIRgibIuDpvIFIg2uDYgT8gchKvC8tUPCIJDtV6B4ibe3zO4K82YlvsJmmO8Q/0?wx_fmt=jpeg)

# 朝鲜APT被指利用IE 0day 发动供应链攻击

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQMmELRlnGCmKmc9MJEIRgibibyn5HwHicewAFT52I312H7R9YM4L1CO2ShlZFyvOSFADf1WMKERIypA/640?wx_fmt=gif&from=appmsg)

**威胁情报公司 AhnLab 和韩国国家网络安全中心 (NCSC) 指出，朝鲜黑客组织被指利用 IE 0day (CVE-2024-38178) 发动供应链攻击。**

该漏洞被描述为脚本引擎内存损坏漏洞，可导致远程攻击者在以IE模式下使用 Edge 的目标系统上执行任意代码。

该漏洞的补丁已在8月13日发布，当时微软提到成功利用该漏洞需要用户点击一个构造的URL。AhnLab 和 NCSC 发现并报送了该漏洞，并在报告中提到该朝鲜威胁行动者被指为 APT37，也被称为 “RedEyes”、“Reaper”、”ScarCruft”、“Group123”和 “TA-RedAnt”等，在攻陷了一家广告公司后在一次零点击攻击中利用了该漏洞。

AhnLab 解释称，“该行动利用IE中的一个0day漏洞，利用安装在多款免费软件中安装中的某个特定 Toast 广告程序。”由于使用基于IE的WebView 来渲染 web 内容以展示广告的任何程序都易受 CVE-2024-38178的攻击，因此APT37 攻陷Toast 广告程序背后的在线广告机构，将其作为初始访问向量。

虽然微软在2022年终结了对IE的支持，但该易受攻击的 IE 浏览器引擎 (jscript9.dll) 仍然位于该广告程序中并仍然可在很多其它应用中找到。该公司解释称，“TA-RedAnt 第一次攻击韩国在线广告机构服务器获取广告程序来下载广告内容，之后将漏洞代码注入该服务器的广告内容脚本中。当该广告程序下载并渲染该广告内容时，该漏洞遭利用。因此，在无需任何用户交互的情况下，发生了零点击攻击。”

朝鲜APT组织利用该漏洞诱骗受害者将恶意软件下载到安装了 Toast 广告程序的系统上，可能接管受陷机器。

AhnLab 公司还发布一份朝语报告，详述了所观察到的活动，还提到了妥协指标 (IoCs)，帮助组织机构和用户寻找潜在的攻陷。APT37组织已活跃十多年并因在攻击中利用 IE 0day 而为人所知，它一直在攻击韩国个体、朝鲜叛逃者、活动家、记者和政策制定者等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[谷歌：早在这个0day 补丁发布前几周，朝鲜国家黑客就已利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511095&idx=2&sn=7814402f965bb0841c66bffe46cf37a2&chksm=ea949d5ddde3144b616fe4b6b99c041734a0422f8c93509bff8ea27f8635e579a8fc8f07af03&scene=21#wechat_redirect)

[朝鲜黑客被指从黑市购买Oracle Solaris 0day，入侵企业网络](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247496657&idx=2&sn=27658cff17f89a0c1f5e185c4bd67a56&chksm=ea94c2bbdde34badf6d540a96b351fcb3be1fa6e2ee4b3d009ab07196ec71ab4a302c1448f3b&scene=21#wechat_redirect)

[和谈之际还不厚道？朝鲜黑客被指利用 ActiveX 0day 漏洞攻击韩国](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487296&idx=3&sn=6a17c1b21061085bbd7af02709f0ed83&chksm=ea973e2adde0b73cb7a6628d7c57db1bd21829b5873bc14f68c8ca6135265a09e3597080661f&scene=21#wechat_redirect)

[朝鲜黑客被指利用 Adobe Flash 0day 漏洞攻击韩国](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486370&idx=1&sn=ef4326d743fb2b44f5c1039b20528db4&chksm=ea973ac8dde0b3de9a12e80d66cdd66eaffd9ddde2afe40382fa6ba823795d5a6b718d723303&scene=21#wechat_redirect)

[朝鲜利用韩国最受欢迎文字处理器中的0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485887&idx=1&sn=935927831636fd67535adddb3334bdbe&chksm=ea9738d5dde0b1c30b0f3ab6c92b0bc4d26e32899ef6b82211e678f2728eb943827c9700f266&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/north-korean-apt-exploited-ie-zero-day-in-supply-chain-attack/

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