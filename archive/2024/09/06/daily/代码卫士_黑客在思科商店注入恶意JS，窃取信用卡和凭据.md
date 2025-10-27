---
title: 黑客在思科商店注入恶意JS，窃取信用卡和凭据
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=3&sn=ca7a392b964011a90f44ef9b56046155&chksm=ea94a0c1dde329d7b3357897b0d476fbdcccdb403a0341d564f40687a51b08c0f26ca20939a6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-06
fetch_date: 2025-10-06T18:27:35.549677
---

# 黑客在思科商店注入恶意JS，窃取信用卡和凭据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT6xjqHOeO1vcMPdOia7sO53dBEn1ITus9WibQwST1XiaS3L3IgTRM3NrZl0AmQ1yPUjFFHEWuEZTibHg/0?wx_fmt=jpeg)

# 黑客在思科商店注入恶意JS，窃取信用卡和凭据

Ionut Ilascu

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**思科负责出售公司主题商品的网站目前已下线，处于维护状态，原因是黑客通过JavaScript 代码窃取结账时提供的客户敏感详情。**

目前尚不清楚思科商店中的恶意 JavaScript 从何而来，不过一名匿名研究员表示似乎是 CosmicSting 攻击 (CVE-2024-34102)。

思科商店 (Cisco Merchandise Store) 是一家礼品店，提供思科品牌的商品和配件（马克杯、瓶子、帽子、充电宝、包、贴纸、玩具）。截止本文写作之时，美国、欧洲和亚太、日本和中国的商店皆无法使用。

**窃取信用卡和登录凭据**

该 JavaScript 被严重混淆，并从在8月30日注册的域名 rextension.[et] 中传播，距离BleepingComputer获悉此攻击已过去两天的时间，说明攻击在上周末就已发生。

该恶意脚本被严重混淆，目的是收集在结账流程中提供的数据，如用于在线支付的所有信用卡详情。BleepingComputer 解混淆了部分脚本并发现它可窃取任何可用的额外信息如邮寄地址、电话号码、邮件地址以及用户的登录凭据。

发现该攻击的研究员表示，威胁行动者可能利用 CosmicSting 漏洞在思科商店中植入恶意 JavaScript。CosmicSting 是一个严重的安全问题，影响 Adobe Commerce (Magento) 商店平台。它是一个XXE漏洞，可导致攻击者读取私密数据。Sansec 的创始人兼架构师 Willem de Groot 指出，在 CosmicSting 攻击中，威胁行动者的目的是将 HTML 或 JavaScript 代码注入结账流程中渲染的CMS块。

虽然思科商店可能主要是由购买自用或送人的员工使用，但该恶意脚本可能导致攻击者收割思科员工的凭据。思科目前尚未就此置评。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[恶意NPM包窃取Discord 令牌和信用卡信息等](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513266&idx=3&sn=c97e5ef94cd87eeddc0b5f0a9f733dd3&chksm=ea9485d8dde30cceb12b05d4b5355bd947fca9397926cded6ae46e9c1797330882410b701b51&scene=21#wechat_redirect)

[KindleDrip：从邮件地址到信用卡盗刷的严重漏洞，值$1.8万奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247500895&idx=2&sn=a2fd1a8dc19b28d95b17be036d9736a3&chksm=ea94f535dde37c23e9a3ddccd0ef1c071066273346dbc4cb086343c9cd5bb53232f1134b42db&scene=21#wechat_redirect)

[谷歌会怎么修？黑客正在利用Analytics 服务窃取电商网站的信用卡数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493717&idx=1&sn=79635284f9470e843cd582cda7083d50&chksm=ea94d93fdde35029b6202f6a00e9e619e884358415b2b6572258d30f70d08438fc85ca78f7b4&scene=21#wechat_redirect)

[美国国防部数万官员旅行记录遭暴露 个人信息信用卡等受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488255&idx=4&sn=55b986f651bc28b84f81bb30fc57a44f&chksm=ea972395dde0aa83255ef70ee34669147a7fd068e818f778e1013933a8077a140d20b09e2a4b&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-inject-malicious-js-in-cisco-store-to-steal-credit-cards-credentials/

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