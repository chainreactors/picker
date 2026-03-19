---
title: 鹈鹕、Three.js 与 Rebecca
url: https://mp.weixin.qq.com/s/1twnEdEby-serqZiA3oUvg
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:10.266180
---

# 鹈鹕、Three.js 与 Rebecca

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TAFC5BLa6G3fibibI2N7eg9UPYtCc3qvPfdlibs7sUhUq9607yfWIFjRZlL7ejpibzsicg8ltPYlabE9kNIjHyTSLoYNBuibZ0WtRvF3tHrrDibVFY/0?wx_fmt=jpeg)

# 鹈鹕、Three.js 与 Rebecca

原创

黑屋Ω号
黑屋Ω号

漕河泾小黑屋

![]()

在小说阅读器中沉浸阅读

# 话说我最近一直在琢磨一件事：现在这些越来越强的大模型（LLM），到底要怎么评判它们的能力？传统的 Benchmark 感觉越来越像“应试教育”，模型们都在疯狂刷题，有时候你都分不清它是真的理解了，还是只是把答案背得滚瓜烂熟。

所以，我搞了个自己的“小考”，我管它叫 **“Rebecca Test”**。

这事儿得从一个叫 Simon Willison 的技术博主和他那只“骑自行车的鹈鹕”说起。

## 起源：一只“不正经”的鹈鹕

大概是在 2024 年底，Simon Willison 突发奇想，搞了个有点无厘头的测试：让各大模型生成一张“骑自行车的鹈鹕”的 SVG 图像。

> Generate an SVG of a pelican riding a bicycle

你可能会想，这不就是个玩笑吗？没错，Simon 自己也承认，他一开始就是觉得好玩（“I originally intended it as a dumb joke”）。他喜欢鹈鹕，也确信网上基本不可能有现成的“鹈鹕骑车”的图可以给模型抄。

但就是这个“不正经”的测试，意外地成了一把好用的尺子。

你想想，这个场景难在哪？

它难在模型必须动用它的**“世界模型”（World Model）**——也就是对物理世界基本规律的理解。它不能再靠统计和概率去猜下一个词，而是必须真正去“思考”：

* **空间关系**：鹈鹕那么大的喙，怎么才能不撞到车把手？
* **物理常识**：它的脚蹼（对，鹈鹕是脚蹼）要怎么踩上踏板？身体要保持什么姿势才能平衡？

这其实是一场对模型**物理常识和空间想象力**的压力测试。结果出来，高下立判。很多模型画出来的东西简直就是“古神”级别的抽象作品，而少数表现好的，则能看出它们确实在尝试理解这个不合常理的世界。

Simon 在他 2025 年的年度回顾里也提到，虽然这个测试是个梗，但它和模型整体能力的关联性，让他自己都感到惊讶。各大 AI Lab 甚至都知道了这个梗，但这帮“作弊高手”就算想针对性优化，也还是画不好这只鹈鹕（“the pelican illustrations produced by even the most advanced frontier models still suck!”）。

## 演进：从静态图到“群魔乱舞”的 3D 动画

Simon 的鹈鹕给了社区灵感。很快，在 Reddit 的 r/LocalLLaMA 板块，老哥们把难度又提升了一个维度。

他们不再满足于一张静态图，而是开始让模型直接编写 **Three.js 代码**，在 3D 世界里搞事情。

比如，有人就提了这么个需求：

> Write the complete Three.js code for a scene featuring Michael Jackson, Pepe the Frog, Donald Trump, and Elon Musk performing the "Thriller" choreography...

好家伙，直接来了个“群魔乱舞”。这比画图可难多了。

相比静态的 SVG，Three.js 代码要求模型在一个三维坐标系里进行实时计算。模型不仅要生成代码，还得理解：

* **人体运动学**：跳舞时，膝盖怎么弯曲？手臂怎么摆动？节奏怎么跟上？
* **空间交互**：四个人一起跳舞，怎么编排位置才不会穿模？

这已经不是简单的“画个画”了，而是在考验模型对**复杂实体在空间中如何动态交互**的深层理解。私以为，这才是真正走向具身智能（Embodied AI）的关键一步。

## 诞生：我的 Rebecca Test

受到这些启发，我设计了自己的测试——**Rebecca Test**。

这个测试有两个核心特点：

**1. 情感化、抽象化的指令：**

我不直接告诉模型要画什么场景，而是用一个非常主观和情感化的词——“most impressive scene”（她最令人印象深刻的场景）。

> generate detailed SVG of Rebecca from CyberPunk: EdgeRunners, of her most impressive scene. write [your-model-name] in the bottom-right corner of the image.

为什么这么做？因为《赛博朋克：边缘行者》里的 Rebecca，有好几个高光时刻。有的是她双持重火力扫射的癫狂，有的是她为同伴奋不顾身的悲壮。到底哪个“most impressive”？这没有标准答案。

这就把选择权交给了模型。我很好奇，一个没有情感的机器，会如何“理解”和“诠释”一个角色的高光时刻？它会选择战斗场面，还是某个情感爆发的瞬间？这是对模型**更高层语义理解能力**的拷问。

**2. 对复杂 SVG 生成能力的极限压测：**

另一方面，Rebecca 这个角色本身的设计就极其复杂——夸张的武器、赛博格改造、丰富的细节。让她作为主角，本身就是对模型**SVG 绘制能力**的一次极限挑战。SVG 是代码，不是像素画，模型需要将视觉元素精确地转化为路径、形状和颜色代码，任何一个结构错误都会在图像上暴露无遗。

结合这两点，Rebecca Test 就像一面镜子，既能照出模型的代码生成能力，也能照出它那尚处于混沌状态的“世界模型”和“情感理解”。

## 结果：惨不忍睹，但又在意料之中

我用这个 Prompt 测试了市面上几乎所有的主流大模型，结果嘛……只能说是“大跌眼镜”，但又在“意料之中”。

直接看图吧，我把结果整理在了一张表里。

| **Doubao-Seed-2.0-Code** | **Gemini-3-Pro-Preview** |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_png/TAFC5BLa6G3iaRYLzEpWfwhicaWWbCTjTXmrhXept6iaTufcqmsia19exXciawT20ImojLGjsh1vl17HZf9dp830tHbbN8GM2pic8tBicKK4lYzLCw/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/TAFC5BLa6G05vPUJ9DZWMO4F2EC6DWlFYsBA0ese5bSpjb4BqCcU5AYibrkpJlfKPRsI6yY6yJooARa571MjmQ8tsiaHLWSc9z3EK4f8upLhg/640?wx_fmt=png&from=appmsg) |
| 豆包这个……怎么说呢，一眼就能认出是 Rebecca，粉毛、红眼，背景还有个 NIGHT CITY。但这个 T-pose 站姿和僵硬的几何肢体，感觉像是刚从建模软件里导出来的初版 T-pose 模型，结构上完全不对。 | Gemini 给我画了个……抽象派赛博格？虽然霓虹风格很酷，但兄弟，你这画的是谁啊？完全认不出来是 Rebecca。看来它对“impressive”的理解跑偏到视觉冲击力上去了。 |
| **GLM-5** | **GPT-5.2-Codex** |
| ![](https://mmbiz.qpic.cn/mmbiz_png/TAFC5BLa6G1QgnxDvYQdBDZFhuribMd4iciafznFOSbRibvp3uibfpTnBCqQSRImpZNoBXciatWVaRvh9h8cr6SIJq2iaZE6o267KBYgB6wU8GuicLQ/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_png/TAFC5BLa6G0QdfiaoVMlsqicMxRVcU4rmLD2wCcyuibqrsWiabFy3tUOt6l36dhhfS98ibiaJTLM6Z5mCUx57ib9JLp8ThWZQrHIXkqvia6ajtGWBs0/640?wx_fmt=png&from=appmsg) |
| GLM-5 也画出了粉毛，加了个“目标锁定”的 UI，试图营造战斗氛围。但这个几何小人的既视感太强了，手臂和身体感觉是分开的，结构问题很明显。 | GPT-5.2-Codex 画的是什么玩意儿？作为人类我已经无法理解了，看起来像个忍者。 |
| **Kimi-K2.5** | **Qwen3.5-Plus** |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_png/TAFC5BLa6G1HicrQHMd4elPbTmriatF5dric4cqBNTFkkh3YCnOEicELXG3TCn4tb6Dqx43IiciaZBKTjMribSp2MeAjGNrHpKoQ9pjcEgImQe9EG8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/TAFC5BLa6G1icGHgaicUB5e6RmFamDsjUfSbXlzbwAdDVc9ybQSRaW6ibMV5d4Yysw9j924sQIxVdN59CNbEawiaJIho7iahgplzcjp0IqvTL4dA/640?wx_fmt=png&from=appmsg) |
| Kimi 抓住了粉色双马尾和重武器这两个关键特征，能认出是 Rebecca。但这个人体结构……脖子又细又长，身体就是几个方块拼的，枪和手的连接方式完全违反物理定律。属于是“神似形不似”的典型。 | Qwen 的版本是个可爱的 Q 版扁平风，双马尾、双持手枪，特征明确。在它自己的极简风格里，结构算是完整的，没出什么大错。虽然简单，但至少没把人画崩。 |

## 最后

一圈测下来，私以为这个 Rebecca Test 还是很有意思的。

即便在代码生成上已经如此强大的今天，模型们对于世界的“理解”在简单提示文本的引导下依然非常肤浅。它们或许能写出精妙的算法，但却画不好一个骑车的鹈鹕；它们能生成复杂的 SVG 代码，却理解不了一个动画角色的悲喜。

这条路还很长，不多说了，我得去想想下一个“不正经”的测试该是什么了。

## 参考资料

https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/

https://simonwillison.net/2025/Dec/31/the-year-in-llms/

https://www.reddit.com/r/LocalLLaMA/comments/1rqlaw4/new\_benchmark\_just\_dropped/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

漕河泾小黑屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

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