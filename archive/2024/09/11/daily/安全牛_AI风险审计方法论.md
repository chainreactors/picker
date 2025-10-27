---
title: AI风险审计方法论
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651132091&idx=2&sn=083aa66090c43d26950bddfa589d5142&chksm=bd15a0688a62297ee00e26b0c0466cdfb327112a503a8c8b60b71fecce1b8a47a1b70c4cf4a9&scene=58&subscene=0#rd
source: 安全牛
date: 2024-09-11
fetch_date: 2025-10-06T18:28:39.633666
---

# AI风险审计方法论

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCGK0cL6LhMDoCdZfKwiaPLogdPRkKNibUDX5FD9gOyUjCGic0Gtfpd6Lm9o4CR9N2Ycu5HLkP5HAHIQ/0?wx_fmt=jpeg)

# AI风险审计方法论

安全牛

以下文章来源于ISACA
，作者Denis Piazzi

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5pbwgfbqEFG6KjnytNoyNTNkTibmib1F4VetdD7KtV0ong/0)

**ISACA**
.

享誉全球的专业技术组织ISACA，致力于推动全球技术领域的人才、专业知识和学习的持续进步，构建全球化专业社区，助力个人的职业进步和企业的数字化转型。其颁发的CISA等认证受到安全、治理、审计、鉴证、风险、数据和隐私等领域从业者的高度认可。

从医疗保健、金融到虚拟助理和自动驾驶汽车，人工智能（AI）在日常生活中无处不在。AI可能彻底改变人类的生活和工作方式，并加速人类生产信息和技术互动方式的转变。但AI也暴露出重大的伦理、法律和社会挑战。其中，最紧迫的问题之一是AI决策过程缺乏问责制和透明度，可能导致偏见、歧视，以及对个人和社会的伤害。

企业在采用AI时通常会面临一些共同的挑战，比如对AI工作原理了解不足，难以分析和解释模型的输出，以及责任和所有权分配不当。

因此，通过技术、监管、数据和流程的角度来审计AI模型，对于确保负责任和合乎伦理道德的使用AI至关重要。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iclpC61N24PkiaG0G0Tpb14TnQfLuue0gDFOU0TCe1VMDYMCCWkdR1lmrJkNYffodicsksZqghtbrSV4yPR6IrFJw/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

![](https://mmbiz.qpic.cn/mmbiz_png/ZDvkiapJxbMKkzEyD06pxn9Pr5cFUxvMh3FyB6W1wMQHu8gZxPhDr2BQx698ddqk5B4Vptz5PtmibygQZHjbribfA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

AI风险审计的重要性

AI风险审计是审查AI系统、算法和数据，从而识别和减轻潜在的风险、威胁和影响。AI风险审计涉及评估AI系统的性能、可靠性、安全性以及道德影响，并评估AI系统是否符合法律和监管要求。AI风险审计可用于识别和解决数据质量、算法偏差、公平性、隐私和安全等问题。这些问题在急于开发和部署AI的过程中往往经常会被忽视。可以在AI生命周期从设计和开发到部署和运营的不同阶段执行审计。

AI风险审计还可以通过提供可靠性、公平性和问责制的证据，帮助建立对AI系统的信任和信心。AI风险审计可以增强开发人员、用户和监管机构之间的透明度和沟通，并培养一种负责任和道德的AI开发文化。

![](https://mmbiz.qpic.cn/mmbiz_png/ZDvkiapJxbMKkzEyD06pxn9Pr5cFUxvMh3FyB6W1wMQHu8gZxPhDr2BQx698ddqk5B4Vptz5PtmibygQZHjbribfA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

实现有道德的AI

然而，AI风险审计并非没有自身的挑战和局限。主要挑战之一是，对于什么是良好的AI治理和道德规范缺乏标准化和共识。执行AI风险审计没有通用的框架或方法，一个审计师可能与另一个审计师有不同的准则和标准，从而可能会造成混乱和不一致，破坏AI风险审计的可信度和有效性。

然而，最近一些政府已经发布或开始起草法规，促进AI模型的安全和道德发展:

* 欧盟提出了“欧洲人工智能法案”，制定AI使用的共同规则，并应对道德和安全挑战。
* 英国正在探索关于AI的道德法规，并可能通过AI办公室制定进一步的指导方针。
* 中国已经发布了AI发展的道德准则，并正在探索应对道德和安全挑战的法规。
* 美国没有关于AI的具体联邦法律，但正在讨论制定国家法规的必要性。
* 新加坡通过“人工智能治理框架模式”发布了AI指导方针，以促进合乎道德和负责任的使用AI。

AI具有让生活变得更好的潜力，但前提是以负责任和合乎道德的方式开发和使用。

AI系统通常使用基于大型数据集的复杂且精密的算法，这些算法可能难以理解和解释。此外，AI系统可以随着时间的推移逐步学习和适应，可能使得预测其行为或其产生的影响变得困难。计划利用AI的力量并不是一个简单的购买和安装新兴技术解决方案的问题，因为AI的本质会影响许多业务领域。如果组织想要配备AI这种颠覆性工具，就必须准备一个充分且结构化的方法，加以监督和控制以便有效遵守快速发展的法规。

全球或各地的每一个监管机构都在努力确保AI系统的问责制和透明度，这是建立对这些系统的信任和信心的关键一步，并将有助于确保以负责任和合乎道德的方式开发和使用AI系统。实现这一目标的路线图包括以下几个步骤:

* **建立明确的道德和法律框架** **-** 应包括制定数据收集、使用和共享的指导方针，以及确保AI决策过程的透明度、公平性和问责制的指导方针。
* **在设计和开发AI系统时考虑道德规范** **-** 应从一开始就考虑到。这意味着开发人员应该在AI算法和系统设计和开发时优先考虑公平性、透明度和问责。
* **解决算法偏见** **-** 算法偏见是AI系统中一个重要的道德问题，因为它可能导致对弱势群体的歧视和伤害。这些偏见在模型中以不同的方式发展，通常反映了训练数据中存在的趋势和偏差。常见的偏见包括时间偏见、抽样偏见、文化偏见和社会偏见。开发人员和审计人员在识别和解决AI系统中的算法偏见时应保持警惕。
* **确保数据隐私和安全** **-** 数据隐私和安全是AI系统中的关键问题，因为它们会影响个人隐私和数据保护。AI系统的设计和开发应具有强大的数据隐私和安全保护，并应定期审计以确保符合相关法规。
* **促进透明度和沟通** **-** 开发人员、用户和监管机构之间的透明度和沟通对于在AI系统中建立信任和问责制至关重要。开发人员应该对AI系统使用的算法和决策过程保持透明，并且应该清楚的沟通AI系统的使用方式和用途。
* **促进协作和创新** **-** 促进协作和创新对于确保以负责任和道德的方式开发和使用AI系统至关重要。这意味着来自不同部门的利益相关者，包括学术界、工业界、政府和民间社会，应该共同努力，分享最佳实践，识别新的挑战，促进有道德和负责任的AI发展。

![](https://mmbiz.qpic.cn/mmbiz_png/ZDvkiapJxbMKkzEyD06pxn9Pr5cFUxvMh3FyB6W1wMQHu8gZxPhDr2BQx698ddqk5B4Vptz5PtmibygQZHjbribfA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

建议的AI风险审计方法

图1描述了一种建议的审计AI模型的方法，以确定其是否符合可解释、透明性和道德标准，尽管该方法不一定详尽无遗，但可以作为参考：

![](https://mmbiz.qpic.cn/mmbiz_png/iclpC61N24PkiaG0G0Tpb14TnQfLuue0gDGepuXyZwLqiaq2JfmPhKWo3Cs8tLicNjL5bkQf9RvBwqS6ZuX6UicTeTA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

1. **审计规划 -** 识别出所有的AI模型，并根据内外部法规进行风险评估以确定哪些AI模型属于审计范围。随后，必须确定主要利益相关者（如总法律顾问、监管专家、数据科学家和数据所有者）以获取必要的资源。在规划的最后阶段，必要确定拥有被审计模型运行领域所需特定技能的审计团队。
2. **数据管理审计 -** AI模型严格依赖其训练和正常运行所使用的数据。因此，有必要验证影响AI数据管理过程以及设计和实现的控制措施。
3. **算法审计 -** AI模型的开发必须遵循结构化的方法，即从分析要解决的业务问题开始，然后是开发阶段、后续的生产和持续管理。

   为了确保企业维护声誉、品牌信任、风险缓解和AI能力的有效货币化，有必要直接管理与采用AI信任原则相关的所有审计和测试:

* **公平** - 减少算法中的偏见，避免对某些群体的不公平歧视。
* **透明性/可解释性** - AI系统内部运作的清晰性和开放性，以及以可理解的方式解释AI模型如何做出特定决策或预测的能力。
* **可靠性** - AI系统在不同情况下随时间提供准确、一致和可靠结果的能力。一个值得信赖的AI系统，必须能够保持高标准的性能和一致性，表现出足够的鲁棒性和稳定性。
* **安全** - 实施强有力的安全措施，保护AI系统、数据和相关用户。AI的安全对于避免威胁、恶意操纵、侵犯隐私，以及与部署AI技术相关的其他风险至关重要。
* **隐私** – 对与AI模型相关的信息和数据进行保护和保密处理。在处理和操纵敏感数据或个人数据时，AI中的隐私保护尤为重要。

4. **审计关闭 -** 在审计的最后阶段，有必要记录审计结果，包括风险来源、差距和整改计划，并为已确定的差距提供补救和缓解措施建议。

![](https://mmbiz.qpic.cn/mmbiz_png/ZDvkiapJxbMKkzEyD06pxn9Pr5cFUxvMh3FyB6W1wMQHu8gZxPhDr2BQx698ddqk5B4Vptz5PtmibygQZHjbribfA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

结语

AI风险审计是确保AI问责制和透明度的关键活动，可以帮助识别和减轻潜在的风险和危害，建立对AI系统的信任和信心，促进负责任和合乎道德的AI发展。然而，AI风险审计面临着挑战和局限，例如，缺乏标准化、AI系统的复杂性。这些挑战必须通过监管机构和审计人员之间的合作以及使用技术创新（例如，自动数据分析软件或AI模型的可解释性方法）解决，确保以负责任和合乎道德的方式使用AI，造福企业和社会。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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