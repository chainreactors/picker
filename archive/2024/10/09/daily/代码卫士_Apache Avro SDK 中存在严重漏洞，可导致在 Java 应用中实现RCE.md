---
title: Apache Avro SDK 中存在严重漏洞，可导致在 Java 应用中实现RCE
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520994&idx=1&sn=0feb249fd14e6b8b07d5d6531f3287c2&chksm=ea94a388dde32a9eb0fccc6276a05b3ffc8ece88601d58cd5cded78e58234b59bfe4172d8caf&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-09
fetch_date: 2025-10-06T18:54:08.933346
---

# Apache Avro SDK 中存在严重漏洞，可导致在 Java 应用中实现RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS7euItcwX5GeUyNmUywibII1PNR5AA8nX363UUhHicdYr5VcVIoLOd9BNwyRzic8H98heMCpo5QoAug/0?wx_fmt=jpeg)

# Apache Avro SDK 中存在严重漏洞，可导致在 Java 应用中实现RCE

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache Avro Java SDK 中存在一个严重漏洞 (CVE-2024-47561)，如被成功利用可导致攻击者在可疑实例上执行任意代码。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS7euItcwX5GeUyNmUywibIImEcU8BbMwicmibzYs1w5BIRsiaY06tIdwd2AkOFjUm4gaQiaVkDuzuATibw/640?wx_fmt=png&from=appmsg)

该漏洞影响 Apahe Avro Java SDK所有1.11.4之前的版本。项目维护人员在上周发布的安全公告中提到，“在 Apache Avro 1.11.3和之前版本 Java SDK中的架构解析可导致恶意人员执行任意代码。建议用户升级至修复了该问题的1.11.4或1.12.0版本。”

Apache Avro 类似于谷歌的 Protocol Buffers (protobuf)，是一款向大规模数据处理提供不分语言的数据序列化框架。Avro 团队表示，任何一款应用只要允许用户提供自己的 Avro 图式进行解析，就会受影响。Databricks 安全团队的研究员 Kostya Kortchinsky 发现并报送了该漏洞。

作为缓解措施，建议用户在解析前清理图式，并避免解析由用户提供的图式。Qualys公司的威胁研究经历 Mayuresh Dani 在一份声明中提到，“CVE-2024-47561在反序列化通过 avroAvro 图示接收的输入时，影响 Apache Avro 1.11.3和之前版本。处理来自威胁行动者的此类输入导致代码执行后果。从我们的威胁情报来看，目前尚不存在 PoC，但通过 ReflectDat 和 SpecificData 指令处理包时会触发该漏洞，且该漏洞可通过 Kafka 进行利用。Apache Avro 是一款开源项目，很多组织机构都在使用它。从公开可获取的数据来看，这些机构多数位于美国。如不修复、不监督、不防范该漏洞，则会造成很多安全后果。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520886&idx=1&sn=d50fe47ebc8b4ad640aab8d8ead453e4&chksm=ea94a31cdde32a0a3cb660901fbb4949d1bd11b55a7718fcf71f3c28cf274e27bc3e091b0c27&scene=21#wechat_redirect)

[Apache 修复严重的 OFBiz 远程代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520714&idx=2&sn=a3784b5b2245f1449edaefa3064d676f&chksm=ea94a0a0dde329b6ca2b17012b7eb003867fd983c6abcc5e7fde821968dec1ea86592860496c&scene=21#wechat_redirect)

[【已复现】Apache OFBiz 授权不当致代码执行漏洞(CVE-2024-38856)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=2&sn=db306ee3ac03c2a6708b7ae1cc72beaf&chksm=ea94a124dde32832c4479a4e205381dc87f02c98b62b21ceb6a18b70624d029f055e06ba57b2&scene=21#wechat_redirect)

[Apache 修复 Apache HTTP Server 中的源代码泄露漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520009&idx=1&sn=b958a0460ffa3e890f8c189660f04487&chksm=ea94be63dde337752a7dace28761adae32e92abbff78ddbb4dba723691c1d4eb489dd3e5deb2&scene=21#wechat_redirect)

[【已复现】Apache OFBiz 路径遍历漏洞(CVE-2024-36104)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519685&idx=5&sn=cd7840386d236e97bc419b0a943f9d25&chksm=ea94bcafdde335b99fff79a2689e78cb78922997a12f87792bff03a1861af54f7ec49cf32f44&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/critical-apache-avro-sdk-flaw-allows.html

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