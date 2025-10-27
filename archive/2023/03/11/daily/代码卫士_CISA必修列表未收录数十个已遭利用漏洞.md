---
title: CISA必修列表未收录数十个已遭利用漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515885&idx=2&sn=26d62bc99cdd37f8365bae8a9b94dba5&chksm=ea948f87dde30691fa7f9887c40e755916adb1ef81c320c67bd9cf032e3495edbc2c16f71288&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-11
fetch_date: 2025-10-04T09:16:22.527966
---

# CISA必修列表未收录数十个已遭利用漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSETROYJryuoTIGLozibBpYd1txG47PtyibSEILDHuqXUYGt3YsqPeqsOf0Ak3vibOia0uVlLnlibaDtuw/0?wx_fmt=jpeg)

# CISA必修列表未收录数十个已遭利用漏洞

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSETROYJryuoTIGLozibBpYdqnOY0kFYI6355vzpI9XjLVCCzziclkduic2CfgYXic8mcA7sjDJbTn9rA/640?wx_fmt=png)

漏洞情报公司VulnCheck 分析发现，很可能已遭在野利用的数十个漏洞在由CISA维护的“已知遭利用漏洞”分类列表中消失了。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSETROYJryuoTIGLozibBpYdSkTB8nLENXmia3FE3hjdmGXQEd4fFAYxNZV4OhwHCViarUbibUYgIK72A/640?wx_fmt=png)

该公司分析了CISA 在2022年新增到必修列表中的漏洞发现，CISA在去年新增了超过550个漏洞，其中42个漏洞很可能在2022年已遭在野利用且已获得CVE编号，但截止到2023年3月3日仍未被包含在列表中。

CISA的“已遭利用漏洞”分类表通常被称为“必修”列表，因为政府组织机构必须在指定的时间范围内修复某些漏洞，而私有企业也被强烈鼓励这么做。

**未被收录的漏洞分析**

在VulnCheck认为已遭利用但并未增加至必修列表的漏洞中，64%的漏洞与僵尸网络有关，其次是威胁行动者 (12%) 和勒索软件 (10%)，余下的未进行归属。

其中一个缺失的漏洞是CVE-2017-20149，影响 Mikrotik 路由器。该漏洞的相关信息出现在2017年，当时维基解密发布Vault7 文档。该漏洞在2022年才获得CVE编号但可追溯至2017年。

另外一个缺失的漏洞是CVE-2022-28810，它是位于ManageEngine ADSelfService Plus 中的一个漏洞。在VulnCheck 的报告发布前，CISA确实将该漏洞和CVE-2022-35914以及CVE-2022-33891一起增加至列表。CVE-2022-35914是一个GLPI漏洞，也属于未修复的42个漏洞。CVE-2022-33891是一个Apache Spark漏洞，微软在2022年12月发现该漏洞的利用。

去年，CISA澄清了漏洞收录标准，主要包括三个条件：漏洞必须具有CVE编号、必须具有在野利用的可靠证据以及必须具有补丁、缓解措施或应变措施。

目前尚不清楚这几十个已遭利用漏洞为何尚未被收录。CISA尚未就此回应。

分析还发现，四分之三的未收录漏洞可用于进行初始化利用，另外，其中31个漏洞具有公开exploit。例如，思科认为CVE-2022-2003已遭涉及Truebot恶意软件的利用。

报告提到，“CISA 的必修列表无疑是具有帮助的，也是行业的推动力。但是，只要其中缺失已遭活跃利用的漏洞，就无法成为已遭利用漏洞的权威分类。实践者们还应当查找附加来源或找到数据更全面的来源，增强漏洞管理计划。”

VulnCheck将在下周发布这42个未收录的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[CISA新增3个影响IT管理系统的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=3&sn=e59b1a83fa85ee490560066b8b39f535&chksm=ea948fbcdde306aa8791fa944d0c5db86f2535cd2381fc0dcc7d846cf5ee4c1686e12f3696d8&scene=21#wechat_redirect)

[美国CISA将设立供应链风险管理办公室](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=3&sn=e88c34df75275d13d1331d4c0714279e&chksm=ea948c2edde305385fc20864a696ea25c625a2e5604742d8d4cd5026ba6afa9d2223e94cf431&scene=21#wechat_redirect)

[CISA提醒注意西门子、通用数字和康泰克工控系统中的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515346&idx=2&sn=9c64d78059c7b3ee275ab9039c5b3544&chksm=ea948db8dde304aeca214fe6e90ce53733d06ee853e596d44400020349aeb9c8fd6ab433bba3&scene=21#wechat_redirect)

[CISA提醒注意日立能源产品中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=2&sn=df29998bb260f1c274b561d8d33c1ed7&chksm=ea948d0bdde3041d86dd780d173b82a65374d35b5fc063d67de6fb5a4dde1e81e6b3d7805a8c&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/dozens-of-exploited-vulnerabilities-missing-from-cisa-must-patch-list/

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