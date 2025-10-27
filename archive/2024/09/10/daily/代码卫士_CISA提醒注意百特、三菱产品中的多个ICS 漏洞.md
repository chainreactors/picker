---
title: CISA提醒注意百特、三菱产品中的多个ICS 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520732&idx=2&sn=080d86bc26683d38189a49ac073be44c&chksm=ea94a0b6dde329a0e47b16a1c1c32be51890c7425e0aca2e0aed1907a6567ce9de33ff378023&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-10
fetch_date: 2025-10-06T18:28:08.523951
---

# CISA提醒注意百特、三菱产品中的多个ICS 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQCD1O2gZF63RXVQYzxpwDZia4lWIU1liafZudeSIn1oscMWicbyltr75S4zVn1F9K20qQLeERX6E6EA/0?wx_fmt=jpeg)

# CISA提醒注意百特、三菱产品中的多个ICS 漏洞

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周，美国网络安全和基础设施安全局（CISA）提醒注意，位于广泛用于医疗和关键制造业中的两个ICS漏洞易遭利用。**

这些漏洞影响 Baxter（百特）的Connex Health Portal 和 Mitsubishi（三菱）电机的MELSEC 可编程控制器产线。百特和三菱均已发布更新，并提出客户可进一步缓解风险的缓解措施。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQCD1O2gZF63RXVQYzxpwDZ0jnlBL5LJ63rklh6DabJ4gewSSyKZA5pfCWH99Cvlpficbb7PZdTPDA/640?wx_fmt=gif&from=appmsg)

**百特 Connex 漏洞**

CISA 在安全公告中提到，百特 Connex Health Portal 中存在两个可远程遭利用且攻击复杂度低的漏洞。其中一个漏洞CVE-2024-6795是一个CVSS满分的SQL注入漏洞，可被未认证攻击者用于在受影响系统上运行任意SQL查询。CISA提到该漏洞可导致攻击者访问、修改和删除敏感数据并采取其它管理员级别的操作如关闭数据库。

百特 Connex Health Portal 中的另一个漏洞CVE-2024-6796和访问控制不当有关，CVSS评分为8.2，可使攻击者访问敏感的病患信息和纠正信息，并修改或删除某些数据。和CVE-2024-6795一样，该漏洞也是远程可遭利用，攻击复杂度较低，且无需具有任何特殊权限。

百特已修复这两个漏洞，但CISA建议受影响组织机构同时将所有控制系统设备的网络暴露最小化并确保无法从互联网访问。CISA还希望组织机构部署防火墙并使用安全的远程访问方法如VPN等。

CISA提到截至目前，并未发现这两个漏洞遭利用的证据。但医疗技术已成为近年来网络犯罪分子的一个重大目标。单在今年，已发生多起设计大型医疗玩家的安全牛事件。其中最引人注意的是对医疗保险公司 Change Healthcare 的勒索攻击，导致该服务数天宕机。尽管最终向 BlackCat 支付2200万美元的赎金，在后者仍然在暗网上泄露了数百万美国人的敏感医疗信息。在另外一起攻击中，Rhysida 勒索组织被指导致芝加哥 Lurie Children’s 医院的系统宕机，攻陷超过79万名病患的记录。

医疗行业成为犯罪分子的首要目标有多方面的原因，如医疗组织机构通常掌握很多有价值的信息，尤其易受运营中断以及病患服务降级的影响等。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQCD1O2gZF63RXVQYzxpwDZ0jnlBL5LJ63rklh6DabJ4gewSSyKZA5pfCWH99Cvlpficbb7PZdTPDA/640?wx_fmt=gif&from=appmsg)

**三菱 MELSEC 漏洞**

CISA 提到，三菱电机的MELSEC工业自动化和控制应用可编程控制器和三菱此前发布的多个漏洞有关。其中一个安全公告和三菱在2020年披露的DoS漏洞（CVE-2020-5652）有关，当与该漏洞的相关新问题产生时，都会进行相关更新。最新安全公告将更多MELSECC产品哈如受影响技术名单，并提供了相关缓解信息。另外一个漏洞CVE-2022-33324也是一个DoS问题，不过源自资源关闭或发布不当。三菱首次在2022年12月发布该漏洞并一直保持更新。本次的最新更新是该公司在今年第三次对该漏洞的更新。

ICS和制造业其它信息技术产品中的漏洞受关注的原因有二。首先是超过75%的制造业企业环境中拥有未修复的高危漏洞：针对制造业企业的攻击在近年来激增。Armis 在今年早些时候发布报告时提到，2023年制造业企业遭受的攻击增长了165%，使其成为继公用设施以外的第二个遭受攻击最大的行业。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA：严重的 Jenkins 漏洞已被用于勒索攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520541&idx=2&sn=c8001046f4088bb94fd3ffcd7e6926b0&chksm=ea94a077dde32961061f5df3f34bcfb998ef7faf4faaf97b0d98fbf993523b5bcb3996850eb0&scene=21#wechat_redirect)

[CISA：多数重要的开源项目未使用内存安全代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519901&idx=1&sn=32d7347010a5e163854477e5c2232e19&chksm=ea94bff7dde336e13576de0daf2daadc290e35b0e3b4c7d7b385038100a61ef8c962de61267a&scene=21#wechat_redirect)

[CISA 的CSA工具遭攻陷 化工厂敏感数据或被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519838&idx=1&sn=de0b2d5074525381fb17b3e0ce5f7bc0&chksm=ea94bf34dde33622a402a66867560237468eaf95fc52683f2e9a0fa44591b58a3324fdf33086&scene=21#wechat_redirect)

[CISA提醒修复RAD SecFlow-2 工业交换机中的路径遍历漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519815&idx=1&sn=39b57daed4e444ed2e6237921fc44ab3&chksm=ea94bf2ddde3363b829e7d029196cf0e5a1792a12fde5361f1ee4ead26cdbcf0674f50c4bded&scene=21#wechat_redirect)

[CISA开展首次AI网络事件响应演习](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519781&idx=2&sn=98211ba85d9f4876a22cf14e43844295&chksm=ea94bf4fdde3365939e4cc2614def1213c00d4201e2a8fb7600761b18020027d18b4a4adcfe7&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/ics-ot-security/cisa-flags-ics-bugs-in-baxter-mitsubishi-products

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