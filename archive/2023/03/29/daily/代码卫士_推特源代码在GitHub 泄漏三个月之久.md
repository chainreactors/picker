---
title: 推特源代码在GitHub 泄漏三个月之久
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516064&idx=3&sn=1ee10d19e2269fa8cd24675a1e68c64e&chksm=ea948ecadde307dc4777959fc9483de5297fb419a29d3f05ab2d53e1d69e2929d4569cae5d0b&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-29
fetch_date: 2025-10-04T11:01:22.002272
---

# 推特源代码在GitHub 泄漏三个月之久

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQ8wujiaicZ3m2DgID1dCtK0lFUrDGHMZ8ib531iaIg31iavLYWEe5vF5oaVGvGpxsVVrMM4YyGJIvg6xw/0?wx_fmt=jpeg)

# 推特源代码在GitHub 泄漏三个月之久

Nate Nelson

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQ8wujiaicZ3m2DgID1dCtK0l0cwpcFYKVQCxDD8iaxJmGXlrLS0hyr77a8yqevrOj1zMiclWpribSDpWQ/640?wx_fmt=png)

**一份在3月24日提出的千年数字版权法下架请求文件显示，推特源代码在GitHub平台上泄漏了近3个月之久。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQ8wujiaicZ3m2DgID1dCtK0lpV0uRvHy419pZ2xX5T3860AphSsOsZLfo82195qkaYguWjXCbQAjyw/640?wx_fmt=png)

GitHub 是世界全球最大的代码托管平台，服务超过1亿名开发人员，共包括近400个仓库，隶属于微软。

3月24日，GitHub 按照一名推特员工的请求，删除了“推特平台和内部工具的专有源代码”。该代码由用户名为 FreeSpeechEnthusiast 发布在 “PublicSpace” 仓库中。这一名称显然是引用了马斯克在去年10月接管推特时的“战争借口”。

被泄露的代码位于四个文件夹中。尽管在3月24日已无法访问，但其中一些文件夹名称如 “auth” 和 “aws-dal-reg-svc” 似乎表明其中所含内容。

媒体Ars Technica报道称，FreeSpeechEnthusiast 在今年1月3日注册 GitHub 账号并在同一天提交了所有被泄代码。这意味着，在近三个月的时间里，公众可访问推特源代码。

**企业源代码泄漏事件为何发生**

主要软件公司都构建于数百万行代码的基础上，出于各种原因，其中某些代码遭泄露。GitGuardian 公司的开发倡导者 Dwayne McDaniel 提到，“当然恶意人员是主要原因。去年三星和优步事件就与 LapsusS 组织有关。”

然而，黑客并不一定总是事件参与者。在推特事件中，间接证据指向一名对公司不满的员工。他补充道，“就像丰田事件中一名承包商导致私密代码库被公开那样，很大一部分原因在于代码的最终非预期去处。Git 和 CI/CD 协作的复杂度，加上现代应用程序要处理的仓库数量不断增长，意味着非公开仓库中的代码可被不慎公开。”

Synopsys 网络安全研究中心的首席安全战略师 Tim Mackey 指出，“有必要牢记的一点是，源仓库中通常不仅包含代码，还可能包括测试用例、潜在的样本数据以及关于软件如何配置的详情。” 敏感的个人信息和验证信息也可能包含在内。例如，“对于无意交付客户的某些应用而言，源代码仓库中所包含的默认配置可能就是运行配置。”黑客可利用被盗的认证和配置数据执行更大规模的攻击，从而泄漏信息。

McDaniel 指出，这就是为何“企业应当采取更加安全的机密管理策略，将机密存储和机密检测结合的原因。组织机构还应当审计当前的机密泄漏情况，了解代码如被泄露后哪些系统位于风险之中，并了解应当优先处理的事项。”但如果泄漏源自内部，就像推特公司的案例这样，则需要额外注意。企业应当通过完整的威胁建模和分析，对源代码进行管理。

Mackey 提到，“这一点之所以重要的原因在于，如果有人可以触发源代码泄漏，则可能还具备更改源代码的能力。如果访问时未使用多因素认证机制，仅对获批准的用户执行限制访问、执行访问权限和访问监控，则无法完全了解其他人如何可利用开发团队在保护源代码仓库时所做的假设。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[前安全主管指责推特隐藏重大缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513659&idx=3&sn=83c9171a4f8f66638bcb11e45ba2c290&chksm=ea948751dde30e472e7875c8b3204ff855b8f1b5ddc5cf453365da35cdbbd8a84d71764425cb&scene=21#wechat_redirect)

[黑客利用推特漏洞，暴露540万个账户的信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513431&idx=5&sn=0346caf7c1c41c8422d1e72b5f8f2269&chksm=ea94843ddde30d2b2f9c5f09450d3fb86026d32586332c600d220fd63d917484996b91614e7b&scene=21#wechat_redirect)

[加拿大第二大电信运营商的源代码和员工数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515762&idx=3&sn=26f5b087e791a7161bd89b0e3702a8db&chksm=ea948f18dde3060e5240089e18dc49989ea692e539dac35579e8b91baa81345d11dc2c394944&scene=21#wechat_redirect)

[俄罗斯版“谷歌”Yandex源代码遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515387&idx=3&sn=28fb6538b4b168c8a79d6bace6795343&chksm=ea948d91dde30487738e1f1b496baddad423bc371bc08e152dd0dc1ceba25187f0f0c81d9a38&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/attacks-breaches/twitter-source-code-leak-github-potential-cyber-nightmare

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