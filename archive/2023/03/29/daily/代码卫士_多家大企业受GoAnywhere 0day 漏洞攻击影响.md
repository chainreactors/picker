---
title: 多家大企业受GoAnywhere 0day 漏洞攻击影响
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516064&idx=1&sn=7fab64273f8adce01a48faf50055431f&chksm=ea948ecadde307dcd53290844da902ec142820effb62c358fda87676545eb9c2424da1575e72&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-29
fetch_date: 2025-10-04T11:01:20.291524
---

# 多家大企业受GoAnywhere 0day 漏洞攻击影响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQ8wujiaicZ3m2DgID1dCtK0lAobMWoJt434G2FGQ98pczqiaBVDMeSRv1x82LHmd1MmxibBVMYwSfZiaw/0?wx_fmt=jpeg)

# 多家大企业受GoAnywhere 0day 漏洞攻击影响

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQ8wujiaicZ3m2DgID1dCtK0l0cwpcFYKVQCxDD8iaxJmGXlrLS0hyr77a8yqevrOj1zMiclWpribSDpWQ/640?wx_fmt=png)

**越来越多的企业开始证实遭 Fortra 公司 GoAnywhere 文件转移管理 (MFT) 软件0day 漏洞 (CVE-2023-0669) 的攻击。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQ8wujiaicZ3m2DgID1dCtK0lpV0uRvHy419pZ2xX5T3860AphSsOsZLfo82195qkaYguWjXCbQAjyw/640?wx_fmt=png)

该漏洞在今年2月初被公开披露，一周后该漏洞的利用和补丁也发布。不久，俄罗斯威胁组织 Silence 被指利用该漏洞分发 Cl0p 勒索软件。

上周，该勒索团伙在其基于 Tor 的泄漏网站上公布了受该事件影响的组织机构，包括多伦多市、奢侈品牌零售商萨克斯第五大道、美国教育平台 Pluralsight、消费者商品巨头宝洁、矿产公司力拓和英国的养老金保护基金 (PPF)。此前，可持续能源巨头日立能源、加州数字化公司 Hatch Bank、网络安全公司 Rubrik 和医疗提供商社区健康系统均证实受 GoAnywhere 攻击影响。

多伦多市证实，因第三方厂商（但并未指明是 Fortra 公司的 GoAnywhere 服务）事件，其某些数据被陷。多伦多市的一名官员表示，“访问权限仅限于无法通过该第三方安全文件传输系统处理的文件。本市正在调查所识别文件的详情。” 萨克斯第五大道证实称，GoAnywhere 事件之后，某些数据被盗但表示真实的客户数据并不受影响。该公司指出，“Fortra 是 Saks 和其它很多家企业的一家供应商，最近遭受了一起数据安全事件，导致萨克斯使用的某存储位置中的客户数据被盗。被盗数据不包括真实的客户获支付卡信息，仅用于模拟客户订单的测试目的。” Pluralsight 表示，获悉 Fortra 事件后立即停止使用 GoAnywhere，该公司还通知了所有受影响的客户。PPF 在网站发布声明指出，员工数据遭泄漏，获悉事件后立即停用Anywhere。宝洁证实称某些员工数据被盗，但表示客户数据、社保号或金融信息并不受影响。

Virgin 公司不仅证实受该事件影响，还证实称 Cl0p 团伙直接联系他们声称掌握被盗数据，“自称为 Cl0p 的勒索组织最近与我们联系称，通过供应商 GoAnywhere 攻击非法获取某些 Virgin Red 文件。这些文件中并不包含个人数据，因此并不影响客户或员工。”

法国数字化转型和混合云公司 Atos 在上周五表示，事件影响与 Nimbix 文件传输应用相关的数据。该公司表示，“我们的网络安全团队发现了2016年的一份备份文件夹可能遭暴露，与 Cl0p 组织利用的0day 有关。我们已与相关客户取得联系。”

路透社报道称，力拓公司上周通知员工称，GoAnywhere 攻击导致内部数据如薪资信息被盗，声称为此事负责的攻击者威胁公开这些数据。该公司尚未就此事做出回应。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[日立能源证实受GoAnywhere攻击影响，数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515971&idx=1&sn=eec17b15763175ee40e7ceff0749f511&chksm=ea948e29dde3073f5b0f7a3684d38fd09d8ea2a1545f32fdb0d03f46cd192742987741c20e29&scene=21#wechat_redirect)

[遭活跃利用的GoAnyWhere MFT 0day 补丁发布](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515504&idx=2&sn=59769cc0918ffbe4502f46bca1f3a6a9&chksm=ea948c1adde3050ccb386f6f3f2e1851f4b3aec399d1c496bf1ed6b4355e88d7aeb87a86d249&scene=21#wechat_redirect)

[Supermicro服务器被曝 UBAnywhere 漏洞，可导致 USB 遭远程访问](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247490754&idx=2&sn=2bc2929e850c6e7bcdddf8ba82edc869&chksm=ea972da8dde0a4bec1d67c36bc87f69bbdcba3c3531763212c292b24460142c241a6d1456fde&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/goanywhere-zero-day-attack-hits-major-orgs/

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