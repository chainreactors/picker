---
title: HyperSQL数据库存在严重漏洞，可导致RCE后果
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=2&sn=dcb724416b73a279ecc84b431bf4b120&chksm=ea9489a5dde300b3db050905faed63fce50f5ac9036956a0592ecb89ab79e60230ab4419c6a6&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-10-26
fetch_date: 2025-10-03T20:55:57.584650
---

# HyperSQL数据库存在严重漏洞，可导致RCE后果

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJFbDQdXdPpIQyDyCOaGvxlpE5EyA5YC7SXH12lV2icQjciciaLnxVSDicPw/0?wx_fmt=jpeg)

# HyperSQL数据库存在严重漏洞，可导致RCE后果

John Leyden

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJxBNhicvxPAjmd1GzkvnxWPHmiaaWMNe3m8MVKsMkFdcDg6yicZliaqnV5w/640?wx_fmt=png)

安全研究员在HyperSQL Database (HSQLDB) 中发现了一个严重漏洞，可带来远程代码执行 (RCE) 风险。

HSQLDB 提供基于Java的SQL关系数据库系统。该技术是第二大最热门的嵌入式SQL数据库，迄今为止下载量已有1亿次，它用于开发、测试和部署数据库应用程序。

HSQLDB用于超过3120个Maven程序包，包括LibreOffice、JBoss、Log4j、Hibernate 和 Spring-Boot 以及多种企业软件包。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJgXKHKBGQOVbpy1NwwVFr4mba5P50wbztgg5I7O6yHJZFvicYibGgDJPQ/640?wx_fmt=png)

**解析问题**

Code Intelligence 公司的安全研究员通过云心过一系列模糊测试而发现了该RCE漏洞 (CVE-2022-41853) ，它的CVSS评分为9.8分。

HSQLDB 版本2.7.0及其以前的所有版本均易受攻击。研究人员联系了 HSQL 开发组即HSQLDB的开发人员，后者迅速提供了修复方案和缓解措施。HSQLDB尚未就此事置评，不过Code Intelligence公司的研究人员表示补丁已在管道中。

研究人员指出，“该漏洞已在上游修复，将在下次发布时现身。从2.7.1版本开始，如果将任何Java静态方法用作HSQLDB例程目标，则属性hsqldb.method\_class\_names 必须以类名称或通配符的清单定义。”此前的实现引发了一个问题，原因是在不定义系统属性的前提下，不应当允许使用除了java.lang.Math中方法以外的 Java静态方法，否则会出现其它问题。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJgXKHKBGQOVbpy1NwwVFr4mba5P50wbztgg5I7O6yHJZFvicYibGgDJPQ/640?wx_fmt=png)

**根因**

研究人员发布博客文章，更加深入地解释了该问题的根因。

文章指出，“在默认情况下，SQL声明可用于从类路径中的任意Java类中调用任何静态方法。HSQLDB允许直接使用这些方法。”

该漏洞意味着，在HSQLDB的预打补丁的版本中使用具有不可信输入的java.sql.Statement 或 java.sql.PreparedStatement时，可能导致应用程序易受RCE攻击。

Code Intelligence 公司的联合创始人 Khaled Yakdan 解释称，造成这种问题并不一定要求app易受SQL注入攻击。他指出，“当前默认的配置情况允许使用类路径上的任何类的静态方法。此外，遗留兼容性可允许直接使用这些方法。”

虽然Yakden 拒绝猜测哪些流行应用可能易受攻击，但他解释称启用HyperSQL会导致何种影响，“我们仅专注于寻找漏洞而不会调查易受攻击的代码库。该CVE造成的影响是，如果你使用HyperSQL来处理包括（不可信）用户输入的查询，则攻击者可能能够使你的app执行任意代码。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[已存在数十年的PostgreSQL漏洞影响多家云厂商，企业数据库遭暴露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513590&idx=2&sn=d39361bd34d64d8416bb282dd8ccf9d6&chksm=ea94849cdde30d8a7154632057b0922178990c360416b3b71086143ba351c833dd86cf3bbc54&scene=21#wechat_redirect)

[Apache Cassandra 开源数据库软件修复高危RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510538&idx=2&sn=1d92fa67b48167800ad01baa90c58cbd&chksm=ea949b60dde312765657b9d469ce2b1b6befbad085737df863891995b40982a6109939fb82b2&scene=21#wechat_redirect)

[数据库配置不当，8.8亿条医疗记录遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508847&idx=2&sn=69fda91db14f44156bbda8c709543fd8&chksm=ea949205dde31b1380876edee60c97cca229f5f3ce33734d4a9ce744adcc15e3f2b001e582ea&scene=21#wechat_redirect)

[VirusTotal 共享8000万勒索软件样本分析数据库](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508375&idx=3&sn=2debe706e0c0168c7c552da517c32c42&chksm=ea9490fddde319eb61c3e23eb50a8f88ff044af6f274f73d0c6e27488338d4577d42b6cf2bde&scene=21#wechat_redirect)

[CVE-2021-2429：MySQL InnoDB Memcached 插件中的堆缓冲区溢出漏洞详解](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507667&idx=1&sn=9924d3749ef15cc36b3f13d7e72eb761&chksm=ea94efb9dde366af33f3d0c0ddbc7837e31a2848426fcff964fa62a5749ab5d743f53756aa83&scene=21#wechat_redirect)

**原文链接**

https://portswigger.net/daily-swig/hypersql-database-flaw-leaves-library-vulnerable-to-rce

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