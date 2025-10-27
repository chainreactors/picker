---
title: CISA新增3个影响IT管理系统的漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=3&sn=e59b1a83fa85ee490560066b8b39f535&chksm=ea948fbcdde306aa8791fa944d0c5db86f2535cd2381fc0dcc7d846cf5ee4c1686e12f3696d8&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-10
fetch_date: 2025-10-04T09:10:36.301465
---

# CISA新增3个影响IT管理系统的漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRMrrWLnahV80FeT4ZDEGsIxYfGJ0xUVmibYKlPXm9oI767Jb25qgjJic7HPn420FWXqEQYhunmN5LA/0?wx_fmt=jpeg)

# CISA新增3个影响IT管理系统的漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全和基础设施安全局 (CISA) 在“已知遭利用漏洞”列表中新增三个漏洞。**

这三个漏洞是：

* CVE-2022-35914（CVSS评分9.8）：Teclib GLPI 远程代码执行漏洞。
* CVE-2022-33891（CVSS评分8.8）：Apache Spark命令注入漏洞。
* CVE-2022-28810（CVSS评分6.8）：Zoho ManageEngine

  ADSelfService Plus远程代码执行漏洞。

其中，最严重的漏洞是CVE-2022-35914，它是开源资产和IT管理软件包Teclib GLPI第三方库Htmlawed 中的一个远程代码执行漏洞。

虽然尚不清楚攻击者的相关信息，但Shadowserver Foundation 在2022年10月提到，已发现针对蜜罐的利用尝试。之后，GitHub上就出现了基于cURL的一行PoC，并出现关于出售大量扫描器的广告。另外，GreyNoise 收集的数据显示，来自美国、荷兰、澳大利亚、保加利亚等地的40个恶意IP地址尝试利用该漏洞。

CVE-2022-33891是位于Apache Spark 中的一个未认证命令注入漏洞，遭Zerobot僵尸网络利用，发动DDoS攻击。CVE-2022-28810在2022年4月修复。CISA指出，“多款Zoho ManageEngine ADSelfService Plus 中存在一个未指定漏洞，可导致密码修改或重置时执行远程代码。”发现该漏洞的Rapid7 公司提到，检测到威胁者“执行任意OS命令，获得对底层系统的持久性并尝试进一步跳转到该环境中”。

与此同时，API安全公司Wallarm表示，2022年12月以来，两个VMware NSX Manager漏洞（CVE-2021-39144和CVE-2022-31678）可用于执行恶意代码并嗅探敏感数据。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[CISA提醒注意西门子、通用数字和康泰克工控系统中的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515346&idx=2&sn=9c64d78059c7b3ee275ab9039c5b3544&chksm=ea948db8dde304aeca214fe6e90ce53733d06ee853e596d44400020349aeb9c8fd6ab433bba3&scene=21#wechat_redirect)

[CISA提醒注意日立能源产品中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=2&sn=df29998bb260f1c274b561d8d33c1ed7&chksm=ea948d0bdde3041d86dd780d173b82a65374d35b5fc063d67de6fb5a4dde1e81e6b3d7805a8c&scene=21#wechat_redirect)

[CISA称两个JasperReports老旧漏洞遭在野利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515167&idx=2&sn=20af92858a0c19feb709a6d9fe2b8626&chksm=ea948d75dde3046329314ec3cdf0d4402e72468464a1d691d7674006d19ac7af82207ad2f131&scene=21#wechat_redirect)

[CISA：注意影响Advantech 和日立工业设备的多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514269&idx=3&sn=42277be117ca4047c20dedbf1712beee&chksm=ea9489f7dde300e1a90950387af6f1655ca62e307fbb6644d0534ad880c3e4b3c475bed3e5fa&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/03/cisas-kev-catalog-updated-with-3-new.html

题图：Pexels License

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