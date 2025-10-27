---
title: 【安全圈】账号和密钥明文存储，AI平台1.29T数据库裸奔
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066835&idx=3&sn=fcdc3e40ed3a097ec040c5421d6d41a4&chksm=f36e7853c419f14583ffa8b9691ab876598b252da75432fe0c0c7b309679f50d8baec344b093&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-24
fetch_date: 2025-10-06T19:40:37.861382
---

# 【安全圈】账号和密钥明文存储，AI平台1.29T数据库裸奔

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9dXTB1TNQ6MB0u1oVKic7yQ20Pjag74P8oXHzAQoLnNw6QPlTk4iaicTGg/0?wx_fmt=jpeg)

# 【安全圈】账号和密钥明文存储，AI平台1.29T数据库裸奔

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

### 核心摘要

* 未加密数据库泄露：Builder.ai 一个未加密的数据库被公开访问，包含超过300万条记录，总计1.29TB，导致客户和内部数据泄露。
* 敏感信息外泄：泄露信息包括发票、保密协议、税务文件、电子邮件截图和云存储密钥，使客户个人信息和公司内部运作面临风险。
* 潜在攻击风险：泄露可能导致钓鱼攻击、伪造发票欺诈、未经授权访问云存储，并对Builder.ai的声誉造成损害。
* 响应迟缓：Builder.ai在接到通知后近一个月才采取措施保护数据库，引发对其应急响应能力的质疑。

近日，网络安全研究员Jeremiah Fowler透露，一家总部位于英国伦敦的人工智能开发平台Builder.ai，由于数据库配置错误，该平台遭遇了重大数据泄露事件，共计泄露数据超过300万条，1.29TB。

Builder.ai是Microsoft Power Platform的一部分，在全球多个地区设有分支机构，它允许企业通过自动执行流程和预测结果来提高业务绩效。Builder.ai可以与Microsoft Dataverse以及各种云数据源（如SharePoint、OneDrive或Azure）集成，方便用户访问和管理业务数据。Builder.ai提供了多种预生成的AI模型，用户可以直接使用这些模型，而无需从头开始构建，用户可以根据业务需求创建自定义的AI模型，用于分析文本、图像、结构化数据等。

根据Fowler在Website Planet的报告，泄露的敏感信息包括客户成本提案、保密协议、发票、税务文件、内部沟通记录、秘密访问密钥、客户个人信息以及电子邮件往来截图。数据库中约有337434个发票（18GB）和32,810个文件（4GB），标记为主服务协议。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9BT0mG7BUdGPv791yDtoop4wIAqLnC7F1xnbfJqpHibcibqo8jmdFQUaw/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9jrSNnev8KBgfibWH4nDcqTzx3q2WgsjN6Oia02NSiakuS2FLyl4cpH2gg/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9ob5Vic54QZo265puYwIapskZWBhtVlMe8XOBnmxeObIsCHy1ibibBeEjQ/640?wx_fmt=jpeg&from=appmsg)

“将文档和访问密钥以明文形式存储在同一数据库中，可能造成严重的安全漏洞。如果数据库意外曝光或被未经授权访问，恶意攻击者可能利用这些密钥访问链接系统、云存储或其他敏感资源，无需额外身份验证。”

数据库配置错误是常见问题，但最新报告显示，即使是ShinyHunters和Nemesis这样的黑客组织也在积极入侵暴露的数据库，这表明如果数据库落入恶意威胁攻击者手中，可能会危及公司声誉和用户隐私。

泄露的文档对黑客来说是宝贵的资源，可以用于社交工程攻击。例如制作含有恶意软件的虚假发票，以欺骗Builder.ai的客户。此外数据中的内部信息可能被用来对Builder.ai员工发起有针对性的钓鱼攻击，泄露的云存储访问密钥还可能允许未经授权访问其他位置存储的更敏感数据。

更糟糕的是，Builder.ai 应急响应流程十分迟缓。在研究人员通知后，Builder.ai花了整整一个月才保护数据库，并称“复杂的系统依赖”是延迟的原因。尽管解释不够明确，但这表明数据库曝光可能涉及第三方承包商。

研究人员强调，在构建系统时减少依赖性的重要性，以避免妨碍应急响应。为了最小化风险，Fowler建议组织应安全存储管理凭据和访问密钥，对其进行加密，存储在专用系统中，并与其他敏感数据隔离，以防止被利用。

参考来源：https://hackread.com/builder-ai-database-misconfiguration-expose-tb-records/

***END***

阅读推荐

[【安全圈】谷歌测试在Chrome中启用人工智能检测诈骗 当发现钓鱼网站时弹出警告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=1&sn=dddcab37c43e140a04d10fdf74ccf0e4&scene=21#wechat_redirect)

[【安全圈】FortiWLM 曝关键漏洞，攻击者可获得管理员权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=2&sn=d36a351bfabba8d719c29fa871c22b3c&scene=21#wechat_redirect)

[【安全圈】Mozilla再次发文称禁止谷歌搜索向浏览器分成将威胁火狐等独立浏览器的生存](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=3&sn=5e35754a7884cd8ec8ef21319f9245ca&scene=21#wechat_redirect)

[【安全圈】罗马尼亚国民因 NetWalker 勒索软件攻击被判处 20 年监禁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=4&sn=86f5fdfe10bdcdd67c657f5b8141121d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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