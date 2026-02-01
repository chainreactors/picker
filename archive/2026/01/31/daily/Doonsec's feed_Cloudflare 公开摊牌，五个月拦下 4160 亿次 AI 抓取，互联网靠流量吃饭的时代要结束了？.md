---
title: Cloudflare 公开摊牌，五个月拦下 4160 亿次 AI 抓取，互联网靠流量吃饭的时代要结束了？
url: https://mp.weixin.qq.com/s/nWoJ2QpSsag5QgTI4KVURw
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:23:40.826993
---

# Cloudflare 公开摊牌，五个月拦下 4160 亿次 AI 抓取，互联网靠流量吃饭的时代要结束了？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6OibpDQ66VYQkoaSybGI2FbAvxOzfIypfK1SJCh0JgyJ3uibyROb1KLqHicl3KJyzXxnWa5TYicWGz36icuLdwkC36Q/0?wx_fmt=jpeg)

# Cloudflare 公开摊牌，五个月拦下 4160 亿次 AI 抓取，互联网靠流量吃饭的时代要结束了？

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYQNIyABHZrCWcZT6asQr23iaO5wvXibL4CtruQ1E2AY6iaaH3X4LxMnSrBXvjhQND7Y4ibRahz9FhPVBw/640?wx_fmt=gif)

> 公众号：网络技术联盟站

过去十几年，互联网的商业逻辑其实异常稳定。

网站生产内容 → 吸引真人访问 → 通过广告、订阅、电商或服务变现。

不管是媒体、博客、论坛，还是企业官网，本质上都是围绕“人类注意力”这个核心资产运转。

但现在，这个逻辑正在被一种新型“访客”彻底打乱。

不是人，而是 AI 机器人。

在2025年下半年，AI大模型的训练饥渴症彻底暴露：它们像饥不择食的掠食者，在互联网上疯狂抓取人类创作的内容。Cloudflare，这个占据全球近八成CDN市场的网络基础设施巨头，站了出来。自今年7月推出“AI Bot Blocker”默认开启功能以来，Cloudflare在短短五个月内，已经为旗下客户阻挡了超过**4160亿次**来自AI爬虫的请求。这一数字之庞大，相当于全球每人平均被“偷”了50次内容。

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQkoaSybGI2FbAvxOzfIypfdE4WpNZGfN9EAgrICUMG8RUsKK60ATeXvWqRUJFU11NxVqpGC7Gl6g/640?wx_fmt=png&from=appmsg)

Cloudflare联合创始人兼CEO Matthew Prince在接受《Wired》专访时直言：“互联网的商业模式即将发生剧烈变革。我不知道它会变成什么样子，但这是我几乎每时每刻都在思考的问题。”他同时发出警告：如果不尽快建立新的付费机制，内容创作者的生存基础将被AI公司无偿掠夺，互联网将从“流量经济”转向某种未知的新范式。

## 4160亿次

4160亿这个数字并非夸张，而是Cloudflare实时统计的真实数据。今年7月，Cloudflare宣布“内容独立日”（Content Independence Day）倡议，并将“阻挡已知AI爬虫”设为默认选项。网站主无需任何额外配置，即可自动屏蔽包括OpenAI的GPTBot、Anthropic的ClaudeBot、Google的Google-Extended、Common Crawl的CCBot等主流AI爬虫。

结果令人震惊：仅五个月，累计拦截请求就达到4160亿次。平均到每天，就是约27亿次——相当于每秒钟有3万多次AI爬虫被拒之门外。

Matthew Prince解释道：“传统互联网商业模式的核心是：创作者生产内容→吸引人类流量→通过广告、电商或订阅变现。现在AI公司直接跳过了‘人类流量’这一环，把内容拿去训练模型、生成摘要、卖给终端用户，却不给原创网站任何回报。这相当于有人在你家餐厅里偷菜谱，开了一家竞品店，还不付钱。”

Cloudflare的举措本质上是在帮网站主说“不”。除非AI公司与网站主达成付费许可协议，否则爬虫将被直接拒绝对内容的访问。

## Google的“捆绑”难题

在所有AI爬虫中，有一个Cloudflare无法彻底阻挡的例外——Google。

Google在2023年就将传统搜索爬虫（Googlebot）和AI专用爬虫（Google-Extended）合并为同一个User-Agent。这意味着，如果你选择屏蔽Google-Extended以保护内容不被Gemini等模型训练，同时也会被Google搜索彻底抛弃，不再被索引、不出现在搜索结果中。

Prince对此毫不客气：“这太疯狂了。你不能用昨天的垄断地位，去撬动明天的垄断地位。”他认为Google此举是在利用搜索霸权，强迫网站主在“被AI免费抓取”和“失去搜索流量”之间二选一。

这一做法也引发了行业广泛批评。许多独立媒体和内容创作者表示，他们宁愿失去部分搜索流量，也不愿内容被无偿用于训练竞争性AI产品。但现实是，大多数网站仍不敢彻底拉黑Google——搜索流量仍是许多网站的生命线。

过去一年，多项独立研究已证实：AI生成的摘要（Search Generative Experience、AI Overviews、ChatGPT搜索等）正在显著减少原创网站的点击量。

Perplexity、Gemini、ChatGPT等产品在回答用户问题时，往往直接给出总结性答案，并附上来源链接。但用户看到答案后，往往不再点击进入原网站。Gartner今年一份报告显示，新闻媒体网站来自搜索的流量平均下降15%-30%，一些重度依赖Google流量的站点甚至下降超过50%。

更严重的问题在于“模型崩坏”（model collapse）。多篇学术论文（包括Nature今年发表的研究）指出，当AI模型大量使用AI自己生成的数据进行训练时，模型会迅速退化，输出越来越同质化、错误率上升、创造力下降。人类原创内容仍是AI模型进化的唯一优质燃料。

这形成了一个悖论：AI公司越强大，越需要人类内容；但它们越直接给用户答案，原创网站流量越少，创作者收入越低，优质内容生产动力就越弱。长此以往，整个互联网内容生态将陷入恶性循环。

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQkoaSybGI2FbAvxOzfIypfQZlskRLc6gL5v2nbKFZYK5qnQ2B9nGDlPRcRMONoGb75tvH4mqq9VQ/640?wx_fmt=png&from=appmsg)

## 付费许可

解决办法正在浮现：付费内容许可协议。

2024年以来，已有多家媒体集团与AI公司达成协议：

* 2024年10月，Anthropic宣布与Amazon达成高达300亿美元的合作，将Claude模型深度部署在AWS上，同时承诺为训练数据支付许可费用。
* OpenAI与News Corp、Axel Springer、Reddit、Stack Overflow等签订了数亿美元级别的授权协议。
* Perplexity、Google、Apple等也在积极与出版商谈判。

Prince认为，这只是开始。未来可能出现三种主流模式：

1. **直接许可**：AI公司向单个网站或媒体集团支付固定费用或按使用量付费。
2. **行业联盟**：类似音乐领域的ASCAP/BMI，内容创作者组成联盟统一谈判分成。
3. **技术中介**：像Cloudflare这样的基础设施公司提供“付费白名单”机制——AI公司向Cloudflare支付费用，即可进入其客户网站的白名单。

Cloudflare显然更倾向于第三种。它不仅能保护客户，还能从中抽取一定比例的服务费，形成新的收入增长点。

Cloudflare目前在全球CDN市场份额高达79.9%（2022年数据，2025年预计更高），是无数网站抵御DDoS攻击、加速内容分发的幕后基础设施。其客户涵盖从小型博客到全球顶级媒体、电商平台。

当互联网内容生态更健康、网站数量更多、创作者更有动力时，自然需要更多CDN和安全服务——这直接利好Cloudflare的生意。

Prince毫不讳言：“我们希望看到一个由真实人类内容驱动的、多元化互联网。这对创作者好，对用户好，也对我们好。”

但这也引发质疑：Cloudflare是否在借保护内容之名，巩固自身在基础设施层的霸权？毕竟，它已经多次因单一配置错误导致全球大范围网站宕机（最近一次是2025年11月那场影响数千万网站的故障，其CTO不得不公开道歉）。

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQkoaSybGI2FbAvxOzfIypf9nvQyztiaicQdXiaQM4MINBlmIcHOY2OZ32ThibH1V338tSPbFVDz9uMGw/640?wx_fmt=png&from=appmsg)

Cloudflare的AI爬虫阻挡行动，实际上也暴露了当前全球互联网基础设施的高度集中化风险。

2024年7月的CrowdStrike全球蓝屏事件导致航空、医疗、金融系统大面积瘫痪；Cloudflare的多次配置失误也曾让半个互联网短暂“消失”。

这种集中化在带来效率的同时，也制造了单点故障风险。当AI时代到来，内容分发、模型训练、推理服务更加依赖这些基础设施时，系统性风险将被进一步放大。

Matthew Prince说：“AI是一次平台级变迁（platform shift），堪比从桌面互联网到移动互联网的转变。”

这一次，变迁的核心问题是：谁拥有内容，谁为内容付费，谁从内容中获利。

Cloudflare用4160亿次拦截宣告：免费掠夺内容的时代即将结束。创作者、出版商、基础设施公司、AI公司，必须在新的规则下重新坐到谈判桌前。

未来的互联网可能是：

* 更多付费墙与会员制
* 更多许可协议与分成机制
* 更分散的基础设施与去中心化内容分发尝试
* 或者，一个我们尚未想象的全新商业范式

无论结果如何，2025年都将成为分水岭。AI爬虫与人类内容的“围猎与反围猎”大战，才刚刚拉开帷幕。

**喜欢就****分享**

**认同就****点赞**

**支持就****在看**

**一键四连，你的技术也四连**

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYRJ20XxicqZhK1qicQFqicZN3BDMEIvovHPnsWicnRgkibCNOtcZf7icVkErP0b18JZia29GVKLkhR5IJ1ibQ/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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