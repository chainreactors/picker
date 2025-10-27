---
title: CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520886&idx=1&sn=d50fe47ebc8b4ad640aab8d8ead453e4&chksm=ea94a31cdde32a0a3cb660901fbb4949d1bd11b55a7718fcf71f3c28cf274e27bc3e091b0c27&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-24
fetch_date: 2025-10-06T18:27:44.675587
---

# CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT5Hh4Tiao2micCO7wrtDhBPRiaPU97aXp7V1Tia5uA8ayu7VVZa2Ey62WHY9Lpv5do6a0OS5T5r6wCMA/0?wx_fmt=jpeg)

# CISA 提醒注意已遭利用的 Apache HugeGraph-Server 漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全和基础设施局 (CISA) 将五个缺陷纳入必修清单，其中一个是影响 Apache HugeGraph-Server 的远程代码执行 (RCE) 漏洞CVE-2024-27348。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT5Hh4Tiao2micCO7wrtDhBPRfF47s6l2s8GJKeJ2WtiaT20PGYHIdRgeuUkQHhcFTLibfCEAWu1jletQ/640?wx_fmt=png&from=appmsg)

该漏洞是严重等级（CVSS v3.1 评分9.8）的访问控制不当漏洞，影响 HugeGraph-Server 1.0.0至1.3.0（不包括）版本。Apache 在2024年4月22日发布1.3.0修复该漏洞。除升级至最新版本外，用户也可使用 Java 11 并启用 Auth 系统。

另外，启用 “Whitelist-IP/port” 函数可提升 RESTful-API 执行的安全性，它也牵涉潜在的攻击链。CISA提醒称该漏洞已遭在野利用，联邦机构和其它关键基础设施在2024年10月9日前应采取缓解措施或停止使用该产品。

Apache HugeGraph-Server 是 Apache HugeGraph 项目的一个核心组件。该项目是一个开源的图形数据库，旨在处理高性能和高扩展性的大型图形数据，支持深层关系利用、数据集群和路径搜索所需的复杂操作。该产品供电信提供商用于欺诈检测和网络分析，供金融服务用于风险控制和交易模式分析，以及供社交网络用于连接分析和自动化推荐系统。

该漏洞已遭活跃利用，该产品用于高价值企业环境中，因此应尽快应用可用的安全更新和缓解措施。其它被纳入必修清单的四个漏洞为：

* CVE-2020-0618：微软SQL Server Reporting Services RCE漏洞
* CVE-2019-1069：微软 Windows Task Scheduler 提权漏洞
* CVE-2022-21445：Oracle JDeveloper RCE漏洞
* CVE-2020-14644：Oracle WebLogic Server RCE漏洞

这些老旧漏洞并非意味着近期遭利用，而是为了记录在过去某个节点这些漏洞已遭利用。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[承包商遭攻击，加拿大政府员工敏感信息被暴露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518185&idx=1&sn=9576830899e345f45902acb4d644d1fa&chksm=ea94b683dde33f958e17417395954cbe7fdbb09fd790c07bfa91b441217937531563efc21705&scene=21#wechat_redirect)

[美国国防承包商 L3Harris 拟收购以色列监控公司 NSO Group](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512362&idx=1&sn=06bd2eeaadd804ceab0abd0bc5096bd5&chksm=ea948040dde30956dbbb595f39ef95d8e5a254e3c441c891f7534b420ed6c7c297eab5090d81&scene=21#wechat_redirect)

[美国国会合同承包商遭勒索攻击，第三方软件安全亟需保障](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505497&idx=2&sn=2db6139a8951922f2fad96d5e91b42da&chksm=ea94e733dde36e25f5ff544ad2603f5a05300bec594edd4d5eb9aff1e68f0ca33ed355dffa89&scene=21#wechat_redirect)

[美国国防部设立承包商网络漏洞披露计划](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503282&idx=2&sn=7e81a7669ef3ec2303554cf5b56492f6&chksm=ea94fcd8dde375cefd686ef76400c5520a57d332010a1ad50a109249db2c9ad3daf2672f8d13&scene=21#wechat_redirect)

[出于安全考虑，英国防部要求承包商勿回答某些政府普查问题](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502622&idx=2&sn=bc2d05659af78c77c5c8bd48b3e516ca&chksm=ea94fa74dde37362ce1cb87574c85843c1dfa54e6ff9d0ceddaf3f71a2a132d643aec9894547&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-apache-hugegraph-server-bug/

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