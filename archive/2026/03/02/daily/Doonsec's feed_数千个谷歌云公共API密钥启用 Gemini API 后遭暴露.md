---
title: 数千个谷歌云公共API密钥启用 Gemini API 后遭暴露
url: https://mp.weixin.qq.com/s/cO1e0S2-WieIO7aWOhPtTg
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:08:44.660916
---

# 数千个谷歌云公共API密钥启用 Gemini API 后遭暴露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUd03F2wAkxoklPMKcDrIZQVDhjU5hwBRq6ykFtQWO9E4J6iaX9ScgAZLOA0GmtXzt5EBLto9lBtcIibjVZTBD3cNiaibXnehL6ic4U/0?wx_fmt=jpeg)

# 数千个谷歌云公共API密钥启用 Gemini API 后遭暴露

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**最新研究发现，通常仅被指定为用于计费的项目标识符的谷歌云API密钥，可能会被滥用于对敏感的Gemini端点进行身份验证并访问私有数据。**

Truffle Security公司在客户端代码中发现了近3000个谷歌API密钥（通过前缀“AIza”识别），这些密钥用于在网站上提供地图嵌入等谷歌相关服务。安全研究员乔 Joe Leon 表示：“攻击者可通过合法密钥访问上传文件、缓存数据，并将大语言模型的使用费用记到用户账上。现在也能对Gemini进行身份验证，尽管它们原本并非为此目的而设计。”

当用户在谷歌云项目中启用Gemini API（即Generative Language API）时，就会发生该问题，导致项目中现有的API密钥（包括通过网站JavaScript代码可访问的那些密钥）在没有任何警告或通知的情况下，获得对Gemini端点的隐蔽访问权限。这实际上使得任何爬取网站的攻击者都能获取此类API密钥，并用于恶意目的和配额窃取，包括通过/files和/cachedContents端点访问敏感文件，以及调用Gemini API，给受害者造成巨额账单。此外，研究人员还发现，在谷歌云中创建新的API密钥时，默认设置为“无限制”，意味着它适用于项目中包括 Gemini 在内的所有已启用API。

Leon表示：“结果导致数以千计原本作为无害计费令牌部署的API密钥，现在变成了公开在互联网上的有效Gemini凭证。”该公司称，总共在公共互联网上发现了2863个有效的密钥，其中一个还与谷歌旗下的网站有关。

该消息披露之际，Quokka公司也发布了一份类似的报告称，在扫描的25万个Android应用中，发现了超过3.5万个唯一的谷歌API密钥。该移动安全公司表示：“除了通过自动化大语言模型请求造成的潜在成本滥用之外，组织机构还必须考虑支持AI的端点可能如何与提示词、生成的内容或连接的云服务进行交互，从而扩大密钥泄露后的影响范围。即使无法直接访问客户数据，但推理访问权限、配额消耗以及与更广泛的谷歌云资源可能存在的集成组合所构成的风险状况，与开发人员最初依赖的计费标识符模型相比，已发生了实质性的变化。”尽管最初认为此行为符合预期，但谷歌现已介入以解决该问题。

谷歌的一名发言人表示，“我们已知悉此报告，并已与研究人员合作解决了该问题。保护用户的数据和基础设施安全是我们的首要任务。我们已经采取主动措施来检测并阻止已泄露的API密钥尝试访问Gemini API。”

目前尚不清楚该问题是否已在现实环境中被利用。不过，一名用户在两天前发布的一篇Reddit帖子中称，一个被盗谷歌云API密钥导致其在2026年2月11日至12日期间产生了82314.44美元的费用，而其平时的月支出仅为180美元。谷歌尚未就此事置评。

已设置谷歌云项目的用户，应建议检查其API和服务，并核实是否已启用与AI相关的API。如果这些API已启用且可公开访问（无论是在客户端JavaScript中，还是被检入公共代码库），应更换这些密钥。

研究人员提到，“从最旧的密钥开始处理，它们最有可能是在旧观念即认为API密钥可以安全共享下被公开部署的，当所在团队有人启用该API时，它们就追溯性地获得了Gemini的权限。”

Wallarm 公司的安全策略师 Tim Erlin 提到，“这一例子很好地说明了风险是动态变化的，以及API事后可能变得权限过大。必须持续开展安全测试、漏洞扫描和其它评估活动。API尤其棘手，因为它们在操作或可访问数据方面的变化不一定是漏洞，但却会直接增加风险。在这些API上运行并使用它们的AI的普及，只会加速问题的恶化。对API来说，仅仅发现漏洞是不够的。组机构织必须分析相关行为和数据访问，识别异常并主动拦截恶意活动。”

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[谷歌云漏洞奖励计划发布，最高赏金101010美元](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521197&idx=2&sn=f0f32cd958563d41b14cb555f2762a85&scene=21#wechat_redirect)

[谷歌 Gemini 提示注入漏洞可用于暴露私有日历数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524925&idx=2&sn=f89ae14d71d858aa5b0a3b1ba66faf9d&scene=21#wechat_redirect)

[谷歌Gemini Enterprise存在漏洞，可导致企业数据遭暴露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524630&idx=2&sn=be82a743b4b79c2cc101a8757cb82cc4&scene=21#wechat_redirect)

[Google Calendar 邀请被用于劫持 Gemini，泄露用户数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523771&idx=1&sn=202844570d8eb4bdbaf371dc692e7896&scene=21#wechat_redirect)

[Gemini CLI AI 编程助手中存在严重漏洞 可导致代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523673&idx=1&sn=e9be201d67d443c5563ef93eab78ef92&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/02/thousands-of-public-google-cloud-api.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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