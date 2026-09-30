---
title: 解密对话式AI背后的广告追踪风险
url: https://mp.weixin.qq.com/s/L1K1HuKGQZUqTbb-Czt6Zw
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:40:40.231997
---

# 解密对话式AI背后的广告追踪风险

# 解密对话式AI背后的广告追踪风险

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最近几年，ChatGPT、Gemini、Claude 这类大模型对话助手已经走进无数人的日常生活。不管是查询健康问题、规划理财方案，还是处理工作文案，大家都习惯把各类私人、敏感的信息交给 AI。很多人默认，我和 AI 的对话，只有我和 AI 服务商能够看到。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpsGoMoS6Yv3j9jGYKvnkBtJVzJghO219XL9jOyskO85b2AKQcZEiax8OrjlEjiawfZE3yBgYLRhndicy5T5tlR6yoMvVBlG0GRCI/640?wx_fmt=png&from=appmsg)

但一份针对 9 款主流对话式 AI 的学术研究却敲响警钟：传统互联网广告追踪体系，已经大规模渗透进对话式 AI 产品，你的对话标题、提问内容、聊天链接，甚至聊天截图，都有可能泄露给第三方广告追踪服务商（ATS，Advertising and Tracking Services）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDolwYyH7TMfphTt4S5pYmEV2IvDYTUUHPgVn32yGeIyibv2iaLhSZEa8Tf3LQV5folpyddzo7n1nYGcXyxZGnL5YlqibpUwX5wczY/640?wx_fmt=png&from=appmsg)

# 对话式 AI，全新的隐私攻击面

很多人对网络追踪的认知停留在浏览器 Cookie、APP 读取设备 ID。但对话式 AI 和普通网页、手机 APP 有着本质区别，用户会在这里输入大量高度敏感的信息，包含身体健康状况、收入财务、职场机密、个人隐私心事。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr8emr2N9SpxYwxibVyWRrpJ2KwypbfibqIDFUeeaA09lZBwhmLYnKIUpehMdYdFc6m4WxCGRIadLa5SAm2oVSicfvLaK1klWpqEQ/640?wx_fmt=png&from=appmsg)

如图 1 所示，整个流程分为用户、对话 AI 服务商（第一方）、第三方广告追踪服务器（ATS Server）三方。 对话 AI 分为客户端（Web 网页、Android 移动端）和服务端。

网页或者 APP 内部嵌入的第三方 SDK，可以直接收集数据向外传输；服务商服务端也会主动把部分数据转发给第三方。 泄露出去的不只是设备编号、用户账号这类标识符，还有对话衍生产物（Conversational Artifacts），这是对话 AI 独有的风险数据，包括聊天唯一 ID、聊天链接（Permalink 永久链接）、AI 自动生成的对话标题、用户原始提问 Prompt、聊天截图。 一旦这些对话内容相关的数据，搭配用户持久化识别标识一起发送给第三方，广告追踪方就可以把你的真实聊天内容，绑定到你的个人用户画像里。更危险的是部分聊天公开链接没有访问权限校验，拿到链接的外部主体就可以读取完整对话记录。

# 研究者怎么测出这些隐私漏洞

这项研究一共测评 9 款市面上主流对话 AI 产品：ChatGPT、Claude、Grok、DeepSeek、Perplexity、Gemini、MS Copilot、Mistral (Le Chat)、Meta AI。覆盖全部 9 个产品网页端，以及 8 款拥有安卓 APP 的移动端应用。

实验全部在 2026 年 5 月于西班牙开展，结合静态代码反编译和动态流量抓包，模拟普通用户真实使用场景。会切换不同实验条件：是否接受 Cookie 授权、访客账号 / 免费账号 / 付费会员账号、无痕模式，还模拟普通人向 AI 咨询医疗问题，生成带有敏感信息的聊天会话。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoVrcbWL48FhNqZZULIGlTDTlHu2WXZhzaoAuhwSqpTTbsfIiaE1x9HbhZfzCFAggKjlu9VCia1ZBQsecVQXGL6ZrKIcyHFvQM6Q/640?wx_fmt=png&from=appmsg)

如图 2，整套实验流程分为 4 个环节，第一步筛选市场主流 AI 服务，第二步对网页端使用 Chrome 开发者工具抓网络流量，安卓端使用插桩改造的 Pixel3a 手机监控全部网络流量与 SDK 加载行为；第三步控制实验变量，调整 Cookie 许可、账号类型，输入包含敏感信息的提示词；第四步分析流量，梳理第三方接收的数据、识别泄露的对话资源，完成隐私风险评估。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqcFsvGOFzKo5GGhia0L1C3T5iaxb1VNFicYtd8l2Zj01HM3Pl048scWTzafibyy3XmesvqAhKKiaAGplzI2RpHD6G1zTictVQtKxGOM/640?wx_fmt=png&from=appmsg)

研究团队区分第一方和第三方服务，就算是谷歌、微软、Meta 自家的广告统计组件，也归类为第三方广告追踪服务 ATS，保证各个产品之间评判标准统一。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqznX3z95O4Q7524sI2kzmv6s64PEO5dmKniazW8qeFm45nW5HoOdbbibEkFZktIzgia8vMRUMe80Ck1IyTB4MSVHiaxo4HB5wAlRM/640?wx_fmt=png&from=appmsg)

# 实测：几乎所有 AI 产品都接入第三方追踪服务

研究结果显示，所有被测对话 AI 产品，都至少接入一个第三方广告追踪服务。实验一共抓到 124 个不同第三方域名，归属 44 家机构，其中 34 家属于广告追踪服务商。网页端和移动端追踪行为差异很大，11 个追踪机构同时出现在网页和 APP，15 个仅存在网页端，8 个仅出现在安卓客户端，Braze 就是仅移动端会见到的追踪 SDK。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrXQ4S61fmqfMYdxWVZnc4lMvJib3OZ5ooxVVhs1lqNZnCTpoAa8yUxEic9YEBEC47tXZqQ2uE5hvA4JuDdXqIHD5gEqn9kMxw70/640?wx_fmt=png&from=appmsg)

谷歌系组件覆盖面最广，覆盖绝大多数被测产品，包含 Google Ads、Google Tag Manager、Firebase 等；Sentry、Datadog、Intercom、Meta 相关追踪组件也高频出现。DeepSeek 还被检测到国内风控指纹服务 FengkongCloud（风控云）、ShuMei（数美），这类设备指纹工具很少出现在传统追踪数据库记录当中。

安卓 APP 里 71% 的外部网络请求，并不是 APP 原生代码发起，而是来自 WebView 内嵌网页组件。Grok 的 WebView 流量占比高达 98%，Perplexity 达到 91%，ChatGPT 为 71%。WebView 相当于在 APP 内部嵌套浏览器，网页端全套广告追踪技术可以直接搬到手机 APP 内部运行。

# Cookie 同意、会员付费，防护效果远没有想象中好

网页端弹出 Cookie 授权弹窗是大家很熟悉的场景，很多人以为只要拒绝非必要 Cookie，就可以阻断广告追踪。 但实测情况并不乐观：就算用户选择拒绝非必要 Cookie，很多产品依旧会和第三方追踪域名建立网络连接。只有勾选全部同意 Cookie 之后，才会额外激活 Meta、TikTok、Twitter Ads 更多广告组件。 忽略弹窗不做任何选择，流量行为等价于拒绝 Cookie，不会触发额外第三方连接。

付费订阅也不能作为隐私保护伞。绝大多数产品免费账号和高级会员账号，接入的第三方追踪服务商几乎一模一样。仅有 Claude 安卓端出现小幅度差异，免费版加载 Intercom、Sentry，付费版没有加载，研究人员推测这来自代码动态触发，不一定是刻意针对会员关闭追踪。

> 小知识：CSP（Content‑Security‑Policy 内容安全策略）是网页的安全头，它会预先声明页面允许访问的外部域名。哪怕抓包没抓到实际网络请求，CSP 名单里面的域名代表网页具备加载对应第三方资源的权限，在特定条件下就会激活。被测产品 CSP 配置大量包含 Google Tag Manager、Google Analytics、TikTok、Meta 广告域名，代表存在潜在追踪通路。

# 真正可怕的风险：对话内容直接泄露给广告商

传统追踪最多收集你点击了什么页面，而对话 AI 的追踪，可以拿到对话本身的元信息。统计数据显示，9 款产品中 6 个网页客户端、8 款里 3 个安卓客户端，会在正常聊天过程向第三方输出对话衍生数据。

网页端泄露现象更加突出：5 个网页产品向外发送对话永久链接 Conversation URL，3 个网页产品会泄露 AI 自动生成的对话标题 Conversation Title，还有产品会向外发送用户提示词 Prompt、聊天截图 Screenshot。安卓端较少泄露完整链接，但是会泄露对话唯一 IDConversation ID。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpT1W8yKpsKYeZGSohJkyRtcfuaFJHz5ibmQOJBRIROfSyxTGHKicw9ZDgvmH4cfm36ViaqkKnlEsDWtuLHstFQbLZsWvd8gdYYsY/640?wx_fmt=png&from=appmsg)

AI 自动生成的对话标题信息量很高，举个研究里的真实示例： 用户提问 “早期帕金森病有哪些症状”，AI 生成标题 Early‑stage Parkinson’s Symptoms；用户询问薪资 85000 美元如何负担纽约房贷，AI 直接生成标题把薪资数字写进去。仅仅一个标题，第三方就可以推断你的疾病顾虑、收入水平、财务压力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr4tyDAjZCYPt8He7bI8bToJrnQypOo3SLuzNYeFoCL6paRu9zGBSeIm2IFmesZKcbGicMjmRoibTHibMXLu2wiaYsyib5C5dsK97m0/640?wx_fmt=png&from=appmsg)

最极端案例来自 Grok 网页端，当用户开启聊天分享功能之后，TikTok 不仅拿到对话链接、标题、用户提问，还会收到聊天界面截图。截图完整保留用户输入的医疗活检咨询内容，就像图 12 展示的样例，用户的问诊文本直接出现在发送给广告服务商的数据载荷里。

# 聊天数据还会绑定你的身份标识，完成用户画像串联

如果只是拿到匿名对话文本风险尚且有限，但现实中对话衍生数据经常和各类用户识别 ID 一起发送第三方。 网页端常见追踪标识： 1. 第三方 Cookie：比如 Meta 的\_fbp、TikTok 的\_ttp，伴随聊天元数据一同上报； 2. 哈希邮箱 HEMs：把你的邮箱做哈希运算，第三方可以反向做身份匹配，FTC（美国联邦贸易委员会）明确提示哈希不等于匿名化； 3. 账号 ID、会话伪随机 ID，用于跨会话识别同一个账号。

部分服务商还使用服务端转发（Server‑Side Forwarding）技术，流量绕过浏览器，广告拦截插件完全无法阻挡。Claude 通过第一方域名代理，服务端直接把事件转发给 Meta、LinkedIn、TikTok；Grok 借助服务端版 Google Tag Manager，把对话标题、聊天链接直接 POST 请求发送广告 API。

安卓移动端除账号 ID 之外，还会泄露 AAID 安卓广告 ID、设备硬件标识。Grok 会同时向 AppsFlyer 上传 AAID 和用户账号 ID，就算用户重置广告 ID，持久化账号 ID 依旧可以把新老广告 ID 绑定，消解重置 ID 带来的隐私保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqoDlgZ7xeHp2EwCZQtv5SiaKmDzVWLuONhBAfEsEDXS7jCILP0RbInEDaP5vK0CeIWQkvvZsicyu8S7RIFq7VywJh9CsSJ0tvns/640?wx_fmt=png&from=appmsg)

# 公开聊天永久链接，权限管控漏洞重重

很多对话 AI 支持生成分享链接 Permalink，发给其他人查看聊天记录。研究团队重点测试：在不登录账号的无痕浏览器打开这些链接，看是否可以直接读取全部会话。

结果发现部分产品默认权限设置十分宽松。Grok 免费、付费账号生成的聊天链接默认公开可读，需要用户手动关闭公开访问；Perplexity 访客模式下所有聊天链接默认对外公开。 当第三方追踪器拿到这类无权限校验的公开链接，它可以主动访问链接地址，读取完整全部聊天问答内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpQl81MbtJSMaeShCzRSk0FwgbvKic1WdXH1NNV2wxCrwElog6ticdJD078fah3jYasYK5EX20XrYaL93icVx7HTLpibgyX86Bc9gU/640?wx_fmt=png&from=appmsg)

研究人员使用 CanaryToken（蜜罐 URL）做实验，在对话文本、上传文档里埋入探测链接，观测有没有外部服务访问这个链接。Grok 出现大量访问记录，短短几天收到来自 14 个国家 48 个自治系统合计 70 次访问，虽然实验对话在欧盟生成，65.7% 访问 IP 来自美国服务器。

> 重点：就算没有观测到外部访问行为，也不代表风险不存在。欧盟法院 FashionID 判例说明，服务商把可被第三方读取的资源对外暴露这件行为本身，就已经属于个人数据处理，需要承担合规义务，不一定要等第三方真的读取数据才算违规。

# 法律视角：和欧盟 GDPR、ePrivacy 指令存在合规冲突

这项研究从欧盟现行法规角度审视这些行为。 依据 ePrivacy 指令第 5.3 条，用于广告画像的 Cookie、像素追踪、ID 收集，必须拿到用户事先明确同意。EDPB（欧洲数据保护委员会）明确这条规则不止约束 Cookie，URL 追踪、像素、脚本驱动的数据上报全部受该条款管控，禁止暗模式诱导用户点击同意。

而 GDPR 通用数据保护条例提出更高要求：服务商向 Meta、TikTok 这类第三方披露聊天相关信息，必须做到两点。 第一，清晰告知用户哪些数据、出于什么目的、基于哪条法律依据交给第三方。但调研发现 OpenAI、Anthropic、xAI 等平台隐私政策描述十分笼统，只用 “用户内容” 这类模糊词汇，没有明确告知对话标题、聊天链接会转发广告商。 第二，处理行为必须具备合法基础。把聊天元数据发送给广告服务商，不属于正常提供 AI 服务的合同必要条件。服务商不能拿 “服务运行必需” 作为理由，只能依靠用户明确许可或者正当利益抗辩。但正当利益抗辩也需要向用户提供便捷的拒绝途径，而很多产品没有做到。

特别值得警惕，用户经常向 AI 输入健康、心理这类特殊类别敏感个人数据。聊天记录哪怕没有直接保存原始问诊文本，通过标题、摘要也能够推断出用户健康状态，触发 GDPR 对于特殊类别个人数据的严格保护规则。

有观点会提出，数据经过伪匿名化处理就可以放开限制，但欧盟法院 SRB/Scania 判例指出，如果接收方（例如 Meta、谷歌）手握海量用户数据库，有能力把伪匿名标识还原定位自然人，伪匿名不能免除告知用户的法律义务。

西班牙数据保护局 AEPD 参考这份研究，推动欧洲数据保护委员会 EDPB 针对 AI 对话服务第三方数据泄露开展集体调查。

# 用户能做什么？现有防护手段的局限

## 用户侧可以执行的操作

1. 网页端如果提供选项，选择拒绝非必要 Cookie。但要知道拒绝之后依旧会残留一部分追踪通路，不能完全消除风险；

2. 不要随意生成分享聊天链接，用完及时关闭公开分享权限；

3. 尽量不要在对话 AI 输入极度敏感的医疗、财务、家庭隐私内容；

4. 使用广告拦截扩展程序，但要注意服务端转发类追踪，浏览器插件拦截不到；

5. 移动端关闭系统广告 ID 个性化开关，但 APP 内嵌 WebView 带来网页追踪不受系统广告开关管控。

过去我们总以为对话 AI 是属于自己和大模型之间私密对话，但是广告变现浪潮正在把对话式 AI 拉入传统互联网追踪生态。泄露出去的不止设备编号，而是我们的思考、疑问、烦恼，这些由文字组成的内心信息。

风险不是来自传统网页浏览，而是 AI 服务本身产出的对话衍生产物，这些全新数据泄露通道，是监管、厂商、普通用户过去没有充分预估到的。这项研究也留下很多待探索方向，企业版 AI 产品、桌面客户端、语音对话模式，它们的隐私现状还需要后续更多审计。

//项目中涉及到的测试数据：github/guinucool/pbst2027

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrACY340QI653J3BTObEurqJdng8elWsSoZGUvnPDvYRRIXB0ZfZDhBPwzkf290kAsasYibmTBCHI8XWcYZE14Gapg321Q66PrU/640?wx_fmt=png&from=appmsg)

更多Ai相关资料👇

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mm...