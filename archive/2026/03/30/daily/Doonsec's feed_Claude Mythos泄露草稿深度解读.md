---
title: Claude Mythos泄露草稿深度解读
url: https://mp.weixin.qq.com/s/jphweWCIfEnwGlcCOARPDg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:32:43.834401
---

# Claude Mythos泄露草稿深度解读

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OSrUp93dKEnvu7icaryPWkhAInFVgcVOpGl6A54lZRe1NjVaeNQcFbOCx8APOGpvCHQGYbq8ib5pweX2oqA7VfQR622kE0jJJKVJ4Q4T2YcO8/0?wx_fmt=jpeg)

# Claude Mythos泄露草稿深度解读

原创

rayh4c
rayh4c

先进攻防

![]()

在小说阅读器中沉浸阅读

2026年3月26日到27日，Anthropic自家内容管理系统出了大问题。数据缓存意外公开，近三千份未发布的内部文件瞬间就能被搜索引擎找到。Fortune杂志记者Bea Nolan第一个发现并做了独家报道，安全研究人员也立刻跟进验证。Anthropic很快修复了漏洞，并承认这是人为配置错误。他们同时确认，新模型真实存在，正在小范围早期测试中。

最引爆全网的，就是那两版从未发布的博客草稿。一版叫Claude Mythos，另一版内部代号Capybara。内容基本一致，只换了名字。这份草稿直接把下一代旗舰模型的底牌亮了出来：能力实现阶跃式突破，网络安全风险前所未有，推理成本高到必须谨慎发布。

以下就是泄露的原始草稿全文，来自公开存档并经过多方验证：

**Claude Mythos**

We have finished training a new AI model: Claude Mythos. It's by far the most powerful AI model we've ever developed.

03 | 2026

Mythos is a new name for a new tier of model: larger and more intelligent than our Opus models which were until now our most powerful. We chose the name to evoke the deep connective tissue that links together knowledge and ideas.

Compared to our previous best model Claude Opus 4.6 Mythos gets dramatically higher scores on tests of software coding academic reasoning and cybersecurity among others.

In preparing to release Claude Mythos we want to act with extra caution and understand the risks it poses even beyond what we learn in our own testing. In particular we want to understand the model’s potential near-term risks in the realm of cybersecurity and share the results to help cyber defenders prepare.

Mythos is also a large compute-intensive model. It’s very expensive for us to serve and will be very expensive for our customers to use. We’re working to make the model much more efficient before any general release.

For those reasons we’re taking a slower more gradual approach to releasing Mythos than we have with our other models. We’re beginning with a small number of early-access customers who will explore the model’s cybersecurity applications and report back what they find.

**A head start for cybersecurity**

We have written several times in recent months about the rapid progress in AI models’ cybersecurity skills skills that can be used for good or for ill. We’ve documented the ways in which models can be used to rapidly discover vulnerabilities in codebases we’ve also shown how they’re already being used to commit large-scale cyberattacks.

Although Mythos is currently far ahead of any other AI model in cyber capabilities it presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders.

That’s why our release plan for Mythos focuses on cyber defenders: we’re releasing it in early access to organizations giving them a head start in improving the robustness of their codebases against the impending wave of AI-driven exploits.

**Pre-release safety testing**

As with all of our models we have tested Claude Mythos on a very wide variety of safety and capability evaluations.

**Expanding the release**

We’ll be slowly expanding access to Claude Mythos to more customers using the Claude API over the coming weeks. Since we’re particularly interested in cybersecurity uses that’s where we aim to expand the EAP initially.

这份草稿把Anthropic的真实意图写得清清楚楚。他们没有急着把最强模型推向市场，而是选择先把重点放在网络安全防御上。

**为什么Anthropic要坚持防御优先**

草稿里专门用一整节解释了原因。他们最近几个月已经多次公开讨论过AI在网络安全上的快速进步。这些能力既能用来保护系统，也能用来发动攻击。他们自己做过实验，证明现有模型已经能快速扫描代码找出漏洞，甚至被用来发起大规模真实攻击。

Mythos把这种能力推到了新高度。它目前在网络攻防上领先其他模型一大截。更重要的是，它预示着接下来的一波模型会让攻击速度远远超过防御方的反应能力。攻击可以几秒钟完成整个漏洞利用链，而防御方还在手动打补丁。

正因为这样，Anthropic决定把早期访问权先给网络安全组织。这些组织可以用Mythos扫描自家代码库，自动生成补丁，把系统加固好，抢在AI驱动的攻击浪潮到来之前做好准备。这不是一句空洞的口号，而是基于真实威胁做出的战略选择。模型越强，释放节奏就必须越谨慎。

社区里很多人立刻注意到了其中的讽刺。X平台和Reddit上到处有人说，最擅长网络安全的模型却因为自家配置错误把三千份文件全敞开了。但更多声音认为，这正是Anthropic负责任的地方。他们没有像其他公司那样快速广发测试，而是先武装防御方再慢慢放开。这种做法和OpenAI、Google的激进路线形成了鲜明对比，也给整个行业立了一个新标杆。

**AI从人人可用走向少数人专享**

草稿里最直白的一句是Mythos是算力密集型模型，对他们来说服务成本很高，对客户来说使用成本也会很高。他们正在努力优化效率，但短期内不会大规模开放。

这句话的背后是整个AI成本曲线的转折。过去大家觉得模型越大越便宜，推理成本会随着技术进步持续下降。可Mythos打破了这个幻觉。参数量和架构复杂度远超上一代，每次复杂查询需要的GPU算力、显存和电力都可能是之前的几倍。Anthropic不会自己补贴，而是直接把成本转嫁给客户。

这意味着前沿模型正在从日常生产力工具变成真正的战略级奢侈品。大企业和政府有预算买早期访问权，能用最强模型做战略决策、代码审计和产品研发。创业公司和中小企业就惨了。过去一年人人用AI创业的红利窗口正在快速关闭。用低阶模型的人和用Mythos的人，效率差距可能从一点点拉大到好几倍。Creator Buddy创始人等分析师早就预言，智力差将成为新的降维打击。

普通开发者、内容创作者和自由职业者只能继续用免费或低阶版本。最顶尖的能力永远藏在高价付费墙后面。泄露后X平台和YouTube上大量AI创业博主开始焦虑，他们的自动化工具和创意流程很可能瞬间落后两个世代。

产业链也随之重塑。NVIDIA和硬件巨头成为最大赢家，对高端GPU的需求会再次暴增。能源、电网和数据中心变成战略资源。云厂商必须重新定价高阶实例，否则就要亏本。传统网络安全公司短期内股价大跌，但长远可能被迫和AI深度绑定。

社区讨论里这个话题热度最高。分析师在X上估算Mythos定价可能达到每百万token上百美元。开发者感慨说，智能本身不再稀缺，稀缺的是获取最强智能的通道。Reddit创业板块的帖子直言，所有AI创业idea都得重新算预算，小公司很可能直接出局。乐观的人觉得很快会有蒸馏版降价，但主流观点是2026到2027年这段时间，普通人要抓紧现在还能低成本使用的窗口。

**AI军备竞赛进入新阶段**

Mythos不是一次孤立的泄露，而是2026年AI发展转折的缩影。行业从单纯堆算力进入后Scaling时代，安全、成本和发布节奏成为新的博弈焦点。Anthropic这次展示的负责任形象，也可能是为他们即将到来的IPO铺路。

整个事件证明，AI已经强大到连创造者都已经感到恐惧，已深陷AI失控的担忧中。Mythos正式发布可能预计在4月以后，早期访问的结果将最终决定这个神话到底是网络安全防御的神器，还是只属于少数人的潘多拉魔盒。

对普通人来说，可能现在已经是最后的机会。趁还能低成本用上最强模型，尽快把自己的AI技能用于生产价值。未来，最强模型的窗口也许正在关闭，它们很可能只属于那些付得起钱的富人。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aff8CeTWGibA5zAI16OFZEHI5c51EBAElrFjYskP0ecgvlYSJqIs1gTpBpvQfXOXicpEefcQxeu3icgfruknxYCAQ/0?wx_fmt=png)

先进攻防

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aff8CeTWGibA5zAI16OFZEHI5c51EBAElrFjYskP0ecgvlYSJqIs1gTpBpvQfXOXicpEefcQxeu3icgfruknxYCAQ/0?wx_fmt=png)

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