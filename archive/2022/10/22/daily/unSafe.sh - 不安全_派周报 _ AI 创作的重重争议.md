---
title: 派周报 | AI 创作的重重争议
url: https://buaq.net/go-132048.html
source: unSafe.sh - 不安全
date: 2022-10-22
fetch_date: 2025-10-03T20:34:50.328586
---

# 派周报 | AI 创作的重重争议

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/29f6b3ae8887049f3d2e8efb1fcdfcd8.jpg)

派周报 | AI 创作的重重争议

我们根据近几个月 AI 创作相关的新闻事件，总结一些该领域目前争议较大的问题，并厘清一些名词和概念的对应关系，以便感兴趣的读者进一步研究和思考，希望能促进以一种审慎但开放的心态看待 AI 创作。AI
*2022-10-21 22:10:42
Author: [sspai.com(查看原文)](/jump-132048.htm)
阅读量:28
收藏*

---

我们根据近几个月 AI 创作相关的新闻事件，总结一些该领域目前争议较大的问题，并厘清一些名词和概念的对应关系，以便感兴趣的读者进一步研究和思考，希望能促进以一种审慎但开放的心态看待 AI 创作。

## AI 创作的重重争议

说今年是 AI 技术实际应用的爆发之年，应该是恰如其分的。前几个月，人们已经轮番被 GPT 生成的文章，Copilot 生成的代码，Stable Diffusion、DALL-E 和 Midjourney 生成的图片刷屏。热潮之下，巨头也纷纷赶场，前有 Google 的图像生成模型 Imagen，后有 Meta 的文本转视频模型的 Make-A-Video，微软则另辟蹊径，将 DALL-E 2 内置在新服务 Microsoft Designer 中，满足普通用户的邀请函、明信片等日常设计需求。

但丰收之秋的另一面也是多事之秋。本周初，*Bloomberg* [报道](https://www.bloomberg.com/news/articles/2022-10-17/digital-media-firm-stability-ai-raises-funds-at-1-billion-value) Stable Diffusion 的开发商 Stability AI 以 10 亿美元的估值，融到了 1 亿多美元的种子轮。但如果观察舆论，其中不乏对其「吸血」「寻租」的批判。同样是在本周，设计师、程序员兼律师 Matthew Butterick（因其[字体排印教程](https://practicaltypography.com/)颇有名气）宣布与律所合作[调查 GitHub Copilot 的侵权情况](https://githubcopilotinvestigation.com/)，再次抛出了与该服务相生相随的版权争议，表示将根据收集证据情况决定是否起诉。

![](https://cdn.sspai.com/2022/10/21/629101e4d5dbc3651a86eb08ac494051.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

就此，本文根据近几个月 AI 创作相关的新闻事件，总结了一些该领域目前争议较大的问题，以便感兴趣的读者进一步研究和思考，希望能促进以一种审慎但开放的心态看待 AI 创作。

**在具体列举问题和事件之前，还有必要先厘清一些名词和概念。** 我们知道，AI 创作虽然涉及复杂的算法和技术，但其基本模式是一致的：研究者用大量的数据训练模型，使其能按设想的方式将输入（如文本或图片）转化为输出（如符合描述的文字、图片、视频等），以满足特定的应用场景。

这一过程涉及了 AI 模型、模型的开发者、用于训练模型的数据集，以及部署模型所得的应用等不同概念。尽管这些概念在很多日常表述中容易被混淆或误用，但正确区分这些环节，对于准确讨论和分配权利、义务和责任是重要的。这里，我们以近期受关注比较多的 AI 技术为例，列举其相关概念的对应关系供参考：

| **模型** | **开发者** | **数据集** | **应用/界面** |
| --- | --- | --- | --- |
| GPT-3 | OpenAI | [CommonCrawl](https://commoncrawl.org/) 的经过滤版本 | [OpenAI API](https://openai.com/blog/openai-api/) |
| Codex (基于 GPT-3) | OpenAI | 公开的自然语言文本 公开源代码，尤其是 GitHub 上公共仓库中的代码 | GitHub Copilot |
| DALL-E, DALL-E 2 (基于 GPT-3) | OpenAI | 公开的文本—图片配对（部分来自基于网络图片及其图注的 [Conceptual Captions](https://ai.google.com/research/ConceptualCaptions/)和基于 Flicker 上照片和视频的 [YFCC100M](http://www.multimediacommons.org/)） | OpenAI 提供的网页界面 |
| Midjourney | Midjourney | 公开艺术作品（未具体披露范围） | Midjourney Discord 机器人 |
| Stable Diffusion | Stability AI | LAION-5B | 第三方制作的 GUI 应用或网页界面，如 [DiffusionBee](https://diffusionbee.com/)、[NMKD Stable Diffusion GUI](https://github.com/n00mkrad/text2image-gui)等 |
| Imagen | Google Brain | LAION-400M 私有内部数据集 | 暂无计划发布 |
| Make-A-Video | Meta AI | 经过滤的 LAION-5B 子集 [HD-VILA-100M](https://github.com/microsoft/XPretrain/tree/main/hd-vila-100m) [WebVid-10M](https://m-bain.github.io/webvid-dataset/) | 尚未公开发布 |

在此基础上，下面是从新闻事件中总结的一些常见问题及相关讨论。

**使用他人的版权作品训练模型，是否构成侵权？** 这是目前几乎所有 AI 模型都无法回避的质疑。首先复习一个基本原则：即使是公开免费提供的代码和作品，只要不是宣布进入公有领域，都受到版权保护；如果用这些代码或作品进行 AI 训练，一般仍然构成法律意义上的「使用」行为，需要获得权利人许可。这也就意味着使用者需要同时遵守许可条款的各项要求：常见的要求包括注明来源、标注原始许可信息等；有的许可证还限制使用方法和目的（例如不能商业化使用）。

而如果要绕过许可条件，就只能主张自己的使用行为构成「合理使用」，但现有的法规和案例都无法明确为此提供支撑。例如，Butterick 在发难 GitHub Copilot 的网页中就写道，GitHub 在用平台上的开源代码投喂 Copilot 时，既没有遵循相关代码的许可证要求，标注原始的许可信息，又没有拿出构成合理使用的充分证据，因此有侵权嫌疑。

不过，也存在一些可能利好 AI 开发商的先例，例如早年颇受关注的 Google Books 一案（将受版权保护的图书扫描并数字化不构成侵权，[*Authors Guild v. Google*](https://law.justia.com/cases/federal/appellate-courts/ca2/13-4829/13-4829-2015-10-16.html), 721 F.3d 132 (2d Cir. 2015)）；以及年初刚刚判决的 LinkedIn 一案（第三方抓取 LinkedIn 上的职业资料等可在互联网上公开访问的数据，不构成侵权访问计算机系统，[*hiQ Labs, Inc. v. LinkedIn Corp.*](https://casetext.com/case/hiq-labs-inc-v-linkedin-corp-5), 31 F.4th 1180 (9th Cir. 2022)）。

但即使如此，这类关于文本和数据挖掘（TDM）的案例还是太少，不足以形成一般经验；而且那些传统技术领域的判决，能多大程度推广到 AI 场景下，也是未知数。

**即使暂时抛开版权问题，AI 训练行为还可能侵犯他人的肖像、隐私，或违反伦理道德。** 早在 2019 年，CC 许可证的维护组织就[发文认为](https://creativecommons.org/2021/03/04/should-cc-licensed-content-be-used-to-train-ai-it-depends/)，使用 CC 授权的作品来训练 AI 在默认情况下应该是合法的，但也鼓励研究者考虑人格、隐私、公德等版权之外的因素。

而随着 AI 应用的门槛降低，这种矛盾也开始集中出现。例如，根据 *Motherboard* 的[报道](https://www.vice.com/en/article/3ad58k/ai-is-probably-using-your-images-and-its-not-easy-to-opt-out)，人们在 Stable Diffusion 和 Imagen 的训练素材 LAION 数据集中，发现了患者诊疗图片、非自愿拍下的裸露照片和恐怖活动的血腥场景等素材。这不仅事前难以发现（有人后来开发了专用搜索工具 [*Have I Been Trained?*](https://haveibeentrained.com/)），而且发现后的补救措施也只有通过 Stability AI 提供的表单逐一要求删除。

因此，目前就有人认为，对于这类涉及他人权利的训练素材，应当采用自愿加入（opt-in）而不是自愿退出（opt-out）的机制；而反对者自然以无法实施和阻碍技术进步为由回应。

**AI 生成作品的权利如何归属？** 从浅层看，这可能是 AI 创作领域少数争议比较小的问题：至少从美国实践看，AI 作品是可以申请版权保护的，唯一的要求是作者必须登记成人类而不是机器。就在九月底，一位名叫 Kris Kashtanova 的纽约艺术家借助 Midjourney 创作了一本漫画，为其申请了著作权登记，并且[获得通过](https://www.instagram.com/p/CivS3iiPigt/)。

![](https://cdn.sspai.com/2022/10/21/1187b7283e6dddbfd3475d9a1d9f0e55.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

但困难的问题在于，AI 训练素材的作者对于 AI 生成的类似作品，能否主张权利？换个问法，如果 AI 作品与他人作品的内容或风格高度一致，是否属于剽窃？例如，*MIT Tech Review* 最近[报道](https://www.technologyreview.com/2022/09/16/1059598/this-artist-is-dominating-ai-generated-art-and-hes-not-happy-about-it/)了一位波兰数字艺术家 Rutkowski 的烦恼。Rutkowski 擅长将古典绘画风格与魔幻场景结合起来，曾经为《龙与地下城》《万智牌》等作品创作插画。但在 Stable Diffusion 火爆后，Rutkowski 发现如果在该模型的输入中加上自己的名字，就能得到仿佛出自己手的作品。还有很多作品被 Stable Diffusion「研究学习」的艺术家描述过类似的情况。

![](https://cdn.sspai.com/2022/10/21/2290c24e32cc6f3b2f32cca4b29fd655.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

当然，艺术史不是没有见证过类似的问题；马塞尔·杜尚的[小便池](https://zh.wikipedia.org/wiki/%E5%99%B4%E6%B3%89_%28%E6%9D%9C%E8%B1%A1%29)和安迪·沃霍尔的[罐头](https://zh.wikipedia.org/wiki/%E9%87%91%E5%AF%B6%E6%B9%AF%E7%BD%90%E9%A0%AD_%28%E8%97%9D%E8%A1%93%E4%BD%9C%E5%93%81%29)在问世时也是充满争议，但最终没有像时人担心的那样摧毁艺术，而是扩展了艺术的定义。但对于 AI 这种规模、效率都远超人类的无机物，又要如何评价它们的「致敬」行为呢？

对此，一种可能的回应是，AI 使用者在编写文本提示词方面做出了创作性努力，从而为其享有作者权利提供了正当性。例如在九月，科罗拉多州博览会的美术比赛中，一名参赛者通过 Midjourney 创作的 AI 作品被评为第一名。

![](https://cdn.sspai.com/2022/10/21/a08da33b033005a5fe156e5dff8fd6c3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

不出意料地，艺术爱好者对此表示谴责。但获奖者则辩解称，生成画作的提示词是自己花了几个星期才想出来的，自己进而用它生成了一百幅作品，然后从中优中选优，才有了获奖作品。

既然 AI 创作产生权利的摩擦是难以避免的，那下一个自然的问题就是，**AI 创作侵权的责任应由谁承担？** 这方面虽然目前的关注焦点主要在于训练模型的研究者和应用提供者，但也有不少观点认为，模型的使用者也需要承担义务和责任。例如，如果使用 Stable Diffusion 创作图片，就有义务不去试图创作内容侵权或违反道德规范的作品；如果使用 Copilot 辅助开发，就有义务检查足定生成的代码是否直接反刍的他人原作（正如很多商业团队在[净室设计](https://zh.wikipedia.org/wiki/%E5%87%80%E5%AE%A4%E8%AE%BE%E8%AE%A1)中所做的那样）；否则，就应承担相应的风险和责任。

一种比较有新意的提法来自《[新物种](https://us.macmillan.com/books/9781250296115/thenewbreed)》（*The New Breed*）一书，该书主张在处理人和人工智能的关系时，参考人和动物的关系，例如像动物饲养人对动物的「肇事行为」承担责任那样，要求使用者对 AI 创作的侵权后果承担责任。

总之，在法律和社会共识付之阙如的情况下，**目前 AI 创作的行为规范主要还是靠行业自律。** 例如，在模型层面，很多研究者都采纳了 Google 旗下 TensorFlow 首倡的「[模型卡](https://arxiv.org/pdf/1810.03993.pdf)」（model card）做法，即以文档形式对模型的预期用途、数据来源、限制与权衡、使用时的道德考量和缓解措施等信息进行充分披露。开源的 Stable Diffusion 还在其许可证（[CreativeML Open RAIL-M](https://github.com/runwayml/stable-diffusion/blob/main/LICENSE)）中将「负责任使用」作为许可条件。

![](https://cdn.sspai.com/2022/10/21/b96ce4e3007aec722e40cc8383848969.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Stable Diffusion 披露的模型卡

在应用层面，DALL-E 等部署为服务的模型普遍加入了自动审核机制，禁止输入一些敏感词句，并自动屏蔽偶尔出现的不妥结果。比较特别的仍然是 Midjourney：除了在[服务条款](https://midjourney.gitbook.io/docs/terms-of-service#10.-limitation-of-liability-and-indemnity)中禁止侵犯性内容，排除自身责任外；由于免费用户可以相互看到在 Discord 房间里发出的机器人指令，本身就自带一种社区监督的效果。

此外，也正是因为这些 AI 创作生死攸关的问题基本都是空白，**市场参与者也普遍表现出一些谨慎的倾向。** *Waxy* 博客在评论 Meta 的视频生成模型时就[指出](https://waxy.org/2022/09/ai-data-laundering-how-academic-and-nonprofit-researchers-shield-tech-companies-from-accountability/)，如今这些大型科技公司在试水 AI 创作时，越来越倾向于走外包路线。通过将繁重的数据收集和模型培训工作委托给科研机构和非营利组织，提高被认定为合理使用的几率，并避免被直接问责或起诉。Getty Images、Shutterstock 等图库也选择[停止收录或限制展示](https://www.theverge.com/2022/9/21/23364696/getty-images-ai-ban-generated-artwork-illustration-copyright?scrolla=5eb6d68b7fedc32c19ef33b4)AI 作品，理由都是这类作品权属不明，可能使客户面临法律风险。

**最后，除了权利归属，AI 作品的使用场合和动机也频繁成为争议问题。** 八月，《大西洋月刊》旗下的邮件通讯 Galaxy Brain 因为在一篇访谈中使用了 AI 图片[备受争议](https://newsletters.theatlantic.com/galaxy-brain/62fc502abcbd490021afea1e/twitter-viral-o...