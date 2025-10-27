---
title: Midjourney 也得「站着敬酒」，AI 图片生成新王 Flux 怎么这么强？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653051355&idx=1&sn=e906ea357b32440d2e31ccde835fc93d&chksm=7e57246d4920ad7bbf8e104e98ec4135646c221602663c9e043fd3f57147c83203286f6b4b8c&scene=58&subscene=0#rd
source: 极客公园
date: 2024-08-14
fetch_date: 2025-10-06T18:03:58.284933
---

# Midjourney 也得「站着敬酒」，AI 图片生成新王 Flux 怎么这么强？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxRiaicb8xRIbu4HNFKx7ORInWzVbaXibcVAwDssciacaJPSicOJx789UuRlw/0?wx_fmt=jpeg)

# Midjourney 也得「站着敬酒」，AI 图片生成新王 Flux 怎么这么强？

原创

芯芯

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxf4FBoVVfhcOYculvguvC2Zazjmia7JcV51iayQfWkgk4ZHJPcaHT4yOw/640?wx_fmt=jpeg&from=appmsg)

表情、手指、细节，堪比真人照片。

**作者 | 芯芯****编辑**| 靖宇****

江山代有模型出，一代更比一代强。

就当人们以为 AI 图片生成领域战争已经基本结束时，又有一个新的模型团队出现，用自家产品将 Midjourney、DALL-E 挑落马下。

8 月初，初创公司 Black Forest Labs 横空出世，发布了拥有 120 亿参数的文本生成图像模型 Flux，随后迅速走红，被誉为 Stable Diffusion 的继承者，并与 Midjourney 直接对打。

从网上曝光的图片能看出，Flux 在生成人物、尤其是真实人物的场景中，图像已经非常接近真人实拍的效果。无论是人物的表情、皮肤光泽、发型、人物配饰等细节方面，都做到了接近完美。

更重要的是，**Flux 开源其系列的一些模型，可以在一台配置不错的笔记本电脑上运行**，这也意味着它会像 Stable Diffusion 一样，可以在多模型平台上找到并使用。

Black Forest Labs 宣称，其模型在图像质量和对文本提示的遵循度等方面，超过了现有的主流选择，如 Midjourney 和 DALL-E。

过去两年中，在 AI 图像生成市场，Midjourney、DALL-E 和 Stable Diffusion 和 Adobe Firefly 等一直在激烈竞争，Flux 凭什么一出来就能抢走风头，甚至被认为可能击败现有的其他模型？

**01**

****Flux，横空出世即走红****

Flux 来自 AI 初创公司 Black Forest Labs，这家新公司由一些开发了 Stable Diffusion 背后技术并发明了潜在扩散技术的研究人员创立，总部位于德国。

今年 8 月 1 日，Black Forest Labs 才对外正式宣布成立，就迅速打响名声。「我们深深植根于生成式 AI 研究社区，致力于开发和推进用于图像和视频等媒体的最先进的生成式深度学习模型。」

Black Forest Labs 称，其公司「决心建立生成式媒体行业的标准」，作为实现这一目标的第一步，他们发布了 Flux.1 文本生成图像模型套件，称在图像细节、提示响应、风格多样性和场景复杂性方面定义了文本生成图像的新前沿。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxJdB4S8DeW0f3SX8FKc3GN8t8FKmmYYRrFdRXmKZOTWDP96JO5Lice3A/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxzGHkzv02mfpfuvTxPiaiamxKtbOZibDMr5g7wzarTYHXtkrvZWse7WuvQ/640?wx_fmt=png&from=appmsg)网友用 Flux 模型生成的图像｜图片来源：reddit

为了在可及性和模型能力之间取得平衡，Flux.1 目前提供了三个版本：Pro、Dev 和 Schnell，都是文本生成图像模型，大小依次递减。

其中，Flux.1 Pro 版是通过 API 提供的闭源版本，也是最强大的版本，提供最先进的图像生成性能。可以通过 API 注册访问，适用于商业应用，为订阅用户提供生成式 AI 图像技术的访问权限。

Flux.1 Dev 版是开源版本，具有非商业许可，供社区开发，直接从 Pro 版本「蒸馏」而来，据称有类似的质量和提示响应能力，同时比同尺寸的标准模型更高效，可在 HuggingFace 上获取，并可直接在 Replicate 或 Fal.ai 上试用。

最后一个 Flux.1 Schnell 版，是速度最快的版本（schnell 在德语中意为快速），也是精简版本，据称运行速度最高可提高十倍，开放源代码，采用 Apache 2 许可，适用于本地开发和个人使用，与 Dev 版本类似，也可以在 Hugging Face 上获取。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxWQxjGyx1W3js4gsRdpHbZmGlmiaHdD75OCiapMufLyygwIXNofK8pvBQ/640?wx_fmt=png&from=appmsg)Flux 部分模型可在 AI 开源社区获取｜图片来源：Hugging Face

有科技博主测评后认为，**两个高端 Flux.1 模型的输出在提示忠实度上与 OpenAI 的 DALL-E 3 相当，且在真实感上接近 Midjourney 6**。

他们还发现，Flux.1 在生成手部图像方面似乎表现相当出色，这在早期的图像合成模型（如 Stable Diffusion 1.5）中是一个薄弱点。尽管自那时起，像 Midjourney 这样的 AI 图像生成器也掌握了手部生成，但 Flux.1 的公开权重模型在各种姿势下能够相对准确地渲染手部图像，仍然值得注意。

理论上说，Flux.1 两个较小的版本可以在性能较好的硬件上运行，例如高性能笔记本电脑，这使得它更容易被更广泛的用户使用，包括业余爱好者、开发人员和小型企业，这也意味着不必依赖互联网或云来运行 Flux.1。

不过，硬件性能较弱的用户可能会遇到困难。**Flux.1 的开源模型大小约为 23GB，这意味着它可能需要接近 24GB 的 VRAM 才能运行**，直到出现可能更轻量化的版本。

已经有科技网站在测评中称，在配有 RTX 4090 的笔记本电脑上运行——它们在对提示的遵从度、图像质量和图像中文字渲染方面都优于 Midjourney、DALL-E 甚至 Ideogram。

据 Black Forest Labs 称，Flux.1 模型采用了 Black Forest Labs 称之为「多模态和平行扩散 Transformer 块的混合架构」，参数规模达 120 亿，比之前的扩散模型更进一步，融合了流匹配和其他优化技术。

在基准测试中，Flux 表示其模型在图像合成方面设立了新标准，称在视觉质量、提示跟随度、大小/长宽比多样性、排版和输出多样性方面表现出色，超越了 Midjourney v6.0、Dall-E 3（HD）和 SD3 Ultra 等模型。

Black Forest Labs 的图表显示，其 Pro 和 Dev 模型是迄今为止最好的图像生成器，而其相对较弱的 Schnell 版本虽然未超越 SD3-Ultra 和 Ideogram，但也超越了 Midjourney v6.0 和 DALL·E 3（HD）。Black Forest Labs 称，「Flux.1 [schnell] 是迄今为止最先进的少步模型，不仅在其类别中表现出色，还超越了强大的非蒸馏模型。」

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxwodsPMvICx8lD4Cr6QQ3503ntH2NchJkeylnSicQthNKcYt5VqdKF7w/640?wx_fmt=png&from=appmsg)Flux 模型与其他模型对比｜图片来源：Black Forest Labs

所有 Flux.1 模型版本都支持 0.1 和 2.0 百万像素的各种纵横比和分辨率。强调这个亮点，是因为市面上不少 AI 工具仅支持生成「方形」图像。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxYDtg6dAf3Mx8ZHu6jtqKlu4eZGhoibsZWoUUESL27GbicBaWNyicc2jPg/640?wx_fmt=png&from=appmsg)Flux 模型支持各种纵横比｜图片来源：Black Forest Labs

对于那些有兴趣探索 Flux 的人来说，有几种方法可以访问和使用该模型。如果计算机足够好，可以下载并在本地运行 Flux.1。此外，目前已经有几个网站提供了 Flux.1 的访问权限。

例如，AI 图像平台社区 NightCafe 已经可以访问 Flux.1 模型，用户可以快速将其与 Ideogram 和 Stable Diffusion 3 等其他工具生成的图像进行比较。AI 模型平台 Poe，也可以访问 Flux.1，允许用户以聊天的形式生成图像。

用户还可以通过更多面向开发者的平台获取访问权限，包括 Based Labs、Hugging Face 和 Fal.ai 等。市场上最大的 AI 图像平台之一 FreePik 表示，它也正在努力将 Flux 引入其网站。

网上已经有不少实验者，较火的是一些真实感很强的图像，乍一看就像普通照片，甚至引起 AI 图像被用于实施诈骗或制造假新闻的担忧。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxvvRibxfUzra9vlibIcc8APOt98azMcwNc7cnebfqKZCVjZbMPMtyibBag/640?wx_fmt=png&from=appmsg)Flux 模型生成的 AI 人像｜图片来源：reddit

「如果我不知道第一张照片发布在哪里，我 100% 会相信这是一张真实的照片。这种疯狂的真实感。我实际上还以为我正在浏览一些关于 Ted 演讲之类的 Reddit 广告。」有 reddit 用户如此评论。还有用户认为，「Flux 确实超越了 midjourney」。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxU2YOiafwpqQFyWP3QnEyXDK3gibkxhibTxJAqoibKWvlGjCsHo8BlQo4Kg/640?wx_fmt=png&from=appmsg)用户利用 Flux 模型生成的 AI 人像｜图片来源：reddit

不过，也有观察者指出，仔细看的话，仍然可以识别出这些图像是 AI 生成的，比如「文字是最大的亮点，尤其是图中挂绳和麦克风等物品上的小文字。」

**02**

****AI 图片江湖：****

****开源 vs 闭源****

Black Forest Labs 由 Robin Rombach、Andreas Blattmann 和 Dominik Lorenz 领导，他们都是 Stability AI 的前工程师，此外还有其他在扩散式 AI 模型开发中起重要作用的人物。

Flux.1 的发布时机对开源 AI 来说具有一定意义。

Stable Diffusion 背后的公司——Stability AI 在几个月前经历了一些动荡，该公司的产品因在人体解剖生成方面表现不佳而遭到广泛批评，用户在社交媒体上分享了扭曲的四肢和身体的示例图像。

Flux.1 的发布距 Stability AI 在 6 月中旬发布的 Stable Diffusion 3 Medium 版本仅七周，该问题版本的发布伴随着 Stability AI 三位关键工程师的离职，他们随后与潜在扩散的共同开发者等人一起创立了 Black Forest Labs。

Black Forest Labs 在成立声明中，强调了其团队在推动媒体生成 AI 方面的出色记录，称他们的创新包括「创建 VQGAN 和潜在扩散模型、用于图像和视频生成的 Stable Diffusion 模型（如 Stable Diffusion XL、Stable Video Diffusion、Rectified Flow Transformers），以及用于超快实时图像生成的对抗性扩散蒸馏技术。」

**在对外发布 Flux 之前，Black Forest Labs 已经完成了 3100 万美元的种子轮融资**，由 a16z 创始人 Andreessen Horowitz 领投，天使投资者包括前迪士尼总裁 Michael Ovitz 等，以及其他在 AI 研究和公司建设方面的专家，General Catalyst 和 MätchVC 进行了追加投资。

有 AI 社区的创业者认为，在 Stability 崩溃后，开源 AI 领域一直缺少一家优秀的图像生成公司，而 Black Forest Labs 发布的 Flux.1 质量看起来可以媲美 DALL-E，这对于多模态 AI 来说是一个好消息，向开源 AGI 进军的步伐仍在继续。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxBRGxwLbS2GBxNr6aLvJQhNRPGp5mPGy8r8WFVapYXas0ibNNabfebdQ/640?wx_fmt=png&from=appmsg)AI 社区人士支持图像生成模型开源｜图片来源：X

目前，通过简单的文本提示生成图像是生成式 AI 领域最成熟的应用之一，市场上至少已经有几十款 AI 图像生成器，提供各种选项、功能和风格，各有千秋。

有些主流的 AI 图像生成工具完全独立，比如 Midjourney。在不到两年的时间里，Midjourney 从只能创建低分辨率、几乎无法辨认的人物图像，已经发展到现在可以生成高分辨率的、几乎与相机拍摄的照片无法区分的图像。

不过，Midjourney 因拒绝讨论其训练数据来源而备受争议。许多人怀疑其数据大部分来自抓取任何可以找到的公开图像，而不考虑是否获得了图像创作者的许可。

Leonardo 生成的图像几乎可以与 Midjourney 相媲美，今年 7 月被在线设计独角兽 Canva 宣布收购。

有些图像生成器内置于其他产品中。比如，OpenAI 将 DALL-E 3 集成在 ChatGPT 的付费版本中，可以通过对话方式生成和编辑图像。微软也将 DALL-E 3 集成到 Microsoft 的 Copilot 聊天机器人中，推出了 Copilot Designer。

其他巨头方面，谷歌方面基于 Imagen 系列模型，推出了 ImageFX，但目前仅支持生成方形图像，限制了应用场景，Meta 的 Imagine 也存在同样的问题。

还有前谷歌工程师出来创立了 Ideogram，擅长在图像上添加文本，适合生成带有文字的图像，比如电影海报、传单、贺卡等。

Adobe 推出了 AI 图像生成工具 Firefly，最大优势之一是它与 Photoshop 的深度整合，以及据称合规的训练数据集，主要来自 Adobe Stock。

此外还有支持多模型工具的 AI 图像生成社区，比如 NightCafe，支持多种模型选择，包括 Stable Diffusion、DALL-E 3、CLIP-Guided Diffusion 等。像 Stability AI 的图像工具，已经被像 NightCafe 这样的社区平台公司广泛使用。

**Black Forest Labs 的 Flux 与市面上的 AI 图像生成工具的主要不同，可能还是在于开源**。

该公司称，「我们相信生成式 AI 将成为所有未来技术的基础构建块。通过向广泛的受众提供我们的模型，我们希望将其好处带给每个人，教育公众，并增强对这些模型安全性的信任。」

Black Forest Labs 在成立声明中强调「透明度是建立信任和广泛采用的关键」，希望将技术尽可能广泛地为大众所用，将最先进的 AI 带给「全球每个人」，据称这是其核心信念。

不过，谈到「信任和安全」时，公司没有提到 Flux.1 模型的训练数据来源。有科技网站测评发现，根据 Flux.1 模型生成的图像，包括版权角色的描绘，Black Forest Labs 可能使用了大量未经授权的抓取的互联网图像，主要可能由 LAION 收集。

LAION 是收集了训练 Stable Diffusion 数据集的组织。但目前这也只是猜测。尽管 Flux.1 的技术成就值得注意，但如果团队的做法像 Stability AI 一样对「公平使用」图像抓取的伦理问题有所松懈，这种做法可能会最终引发类似 Stability AI 所面临的诉讼。

此外，文本生成图像模型只是第一步，Flux 这些模型据称是为 Black Forest Labs 即将推出的文本生成视频系统套件奠定基础。他们已经在开发一个文本生成视频模型，承诺将提供高质量输出并以开源形式发布，称将是「适用于所有人的最先进文本生成视频技术。」

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b2hSfeg8BkPiaFhHOgIsYAxcWIgMuP6KoTHIlLGevvrm7d63Xfib0U04TCxImJXwZXmcBricqMESuCg/640?wx_fmt=png&from=appmsg)文本生成视频模型预告｜图片来源：Black Forest Labs

「我们的视频模型将以高清晰度和前所未有的速度解锁精确的创建和编辑功能。我们致力于继续引领生成式媒体的未来。」Black Forest Labs 称。

这意味着，他们未来可能将与 OpenAI 的 Sora、Runway 的 Gen-3 Alpha 等产生竞争。Midjourney 也有类似的计划，其开发人员正在开发 3D 和视频模式，想将 AI 图像、视频、3D 和实时生成模型结合在一起，通过文本提示创建完全沉浸式的虚拟环境。

\*头图来源：reddit

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**在 AI 图像生成领域，**

**开源与闭源模型各有哪些优势和劣势？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP...