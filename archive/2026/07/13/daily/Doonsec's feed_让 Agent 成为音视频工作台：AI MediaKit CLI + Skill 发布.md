---
title: 让 Agent 成为音视频工作台：AI MediaKit CLI + Skill 发布
url: https://mp.weixin.qq.com/s/Kfrcbw91WY71XKD50vVEmg
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:15.451074
---

# 让 Agent 成为音视频工作台：AI MediaKit CLI + Skill 发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9FeewTPP1T8iautmznSUY7oUGsEhuJcNqIPFc34SERWAWkEiboydYSKibKNQ48ibYoY0f8IEB0T491o7EpFeWo8c5Wnia5YPibUSVKicsFk/0?wx_fmt=jpeg)

# 让 Agent 成为音视频工作台：AI MediaKit CLI + Skill 发布

火山引擎视频云
火山引擎视频云

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeycNX5LfXT9JHUHaRqws1MjxW92qxdUndlghT52JfmsZlxgN6SUFoFWg73MnfIua3JfEjAQkUe3y9Jj6Kmqw5FNPyO5RxaBGQ/640?wx_fmt=png&from=appmsg)

在刚刚结束的 2026 Force 源动力大会上，火山引擎智能视频云正式发布了 AI MediaKit CLI 与 Skill。火山引擎 AI Media Platform 产品负责人杭梦钰指出：AI 视频生产的下一阶段，不只是生成一段画面，而是交付一条真正能上线的视频。

模型让内容生成变得越来越容易。用户可以用一句话、一张图或一段参考视频生成画面。但在真实生产中，一条视频从“生成出来”到“可以发布”，中间仍然需要大量音视频处理工作：理解素材、裁剪片段、拼接成片、添加字幕、擦除原字幕、增强画质、调整帧率和分辨率、适配不同平台规格，需要覆盖理解 — 处理 ——交付的全链路工作。

这些工作过去属于剪辑软件、后期系统和云端 API。到了 Agent 时代，我们希望它们也可以被 Agent 直接理解、调用和编排。

这也是 **AI MediaKit CLI + Skill** 发布的背景：让 Agent 不只是会写 prompt、调用模型，而是拥有一座可调用、可编排、可交付的音视频工作台。

**Agent 需要的不只是模型，还有工作台**

对大多数文本任务来说，Agent 的工作方式已经很自然：读文档、写代码、调接口、看日志。输入和输出大多是文本，Agent 可以直接判断结果是否正确。

但音视频任务不一样。

视频是画面，音频是声波。成片好不好、字幕对不对、节奏顺不顺、画质有没有提升，这些都不是纯文本问题。Agent 活在符号世界里，而音视频活在感官世界里。

因此，音视频工具如果只是把一个 API 包成命令，并不足够 Agent 可靠使用。Agent 需要知道：

* 有哪些音视频能力可以调用；
* 每个能力需要什么输入；
* 长耗时任务是否提交成功；
* 任务执行到哪一步；
* 最终产物在哪里；
* 结果能不能继续交给下一步处理。

这就是“音视频工作台”的意义。

它是一组面向 Agent 的能力层：把理解、处理、交付等音视频处理流程，封装成 Agent 可以调用和编排的工具。

**AI MediaKit：面向 Agent 的音视频能力底座**

AI MediaKit 是火山引擎面向 Agent 时代提供的音视频开发套件，沉淀了**100+ 音视频原子能力**，覆盖视频理解、剪辑、字幕、画质增强、字幕擦除、转码、音频处理、图像处理等生产环节。

这些能力过去往往分散在不同软件、不同 API、不同后期系统里。AI MediaKit 要做的，是把它们重新组织成一套面向 Agent 和开发者的能力底座。

此次发布的**CLI + Skill**，就是 Agent 进入这座工作台的第一层入口。

它让开发者可以用命令行调用音视频能力，也让 Claude Code、Trae、Cursor、Codex、OpenClaw 等 Agent runtime 可以通过自然语言触发对应工具。

换句话说，AI MediaKit 提供的是 100+ 音视频能力池；CLI + Skill 则是这些能力面向 Agent 生态的标准化入口，并会随着底层能力开放持续跟进。

**AI MediaKit CLI + Skill 发布了什么**

AI MediaKit CLI + Skill 主要由三部分组成。

**第一部分是 AI Mediakit Cli。**

它是面向 Agent 的原生命令行工具。开发者和Agent都可以直接用命令完成视频裁剪、拼接、加字幕、画质增强、字幕擦除等任务，也可以把它接入自动化处理流程。

**第二部分是 AI MediaKit Skills。**

Skill 面向 Agent runtime。安装后，用户可以在 Agent 对话窗口里直接描述需求，由 Agent 理解意图、编排能力、拼接命令、提交任务并交付结果。

当前 Skill 按四大能力域拆分，并会随着 AI MediaKit 底层能力开放持续跟进：

* byted-mediakit-editing：剪辑类能力，包括裁剪、拼接、变速、加字幕、加水印、音视频合成等；
* byted-mediakit-video：视频处理类能力，包括画质增强、字幕擦除、视频处理等高阶视频 AI 能力；
* byted-mediakit-image：图像处理类能力，包括图像增强、智能抠图、擦除修复、OCR、智能裁剪等；
* byted-mediakit-audio：音频处理类能力，包括人声背景音分离、音频处理及后续扩展能力。

**第三部分是 Agent 友好的任务机制。**

音视频任务经常是异步的，不适合只靠一次命令返回判断成功。AI MediaKit CLI + Skill 将 task\_id、任务查询、轮询等待、终态结果回收等流程下沉到工具层，让 Agent 不必靠“记忆”判断什么时候回来查任务。

开发者可以通过一行命令快速完成mediakit-cli 和 mediakit skills：

```
npx @volcengine/mediakit-cli install -y
```

其中，mediakit-cli 负责执行音视频任务；这条命令也会把 AI MediaKit Skills 分发到本机支持的 Agent runtime 中。装好之后，Agent 就可以通过自然语言调用这些能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9Fed5uCHLDduFtkbxLQ7LFZYLCAvRW3gGhHicIyNbRNA1icUPPxsbnFK7NTT0UUMlwic3c34YKFvXiajxwFRG2qpOZK9bk3RJia5UcH2M/640?wx_fmt=jpeg&from=appmsg)

**从一句话，到一条可交付视频**

比如用户说：

“帮我把这个视频前 10 秒剪出来，再加上字幕。”

接入 AI MediaKit CLI + Skill 后，Agent 可以自动识别这是一个剪辑任务，调用 editing Skill，生成对应的裁剪和加字幕命令，执行任务并返回最终视频。

再比如：

“把这条短剧素材做一下画质增强，输出 1080p 版本。”

Agent 可以调用 video Skill，将任务提交到云端画质增强能力，并通过 shared Skill 轮询任务状态，直到拿到最终产物。

在更复杂的场景中，Agent 还可以把多个能力编排成工作流：先擦除原字幕，再重压新字幕；先裁剪多个片段，再拼接成片；先生成素材，再做画质增强和平台规格适配。

模型擅长生成，AI MediaKit 负责把生成后的素材处理成真正可上线、可分发、可消费的成片。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FefJkibYzuianSYuIHZCDJyCFfziaicCm4Zw5tx8MN4GB8DfPwO8A7jHD3wI2vxH3iby4O3wwF0n5nibia4mMm0R7zSQ4GqO86uDHrPC10/640?wx_fmt=jpeg&from=appmsg)

**不是 API Wrapper，而是 Agent 的工作台入口**

AI MediaKit CLI + Skill 并不是把 API 简单包一层命令。

它面向 Agent 使用场景做了几件关键设计。

**能力结构化**

Agent 不需要凭经验猜命令和参数，而是可以通过 Skill 描述理解每个能力的用途、输入和调用方式。

**长任务可回收**

音视频任务往往耗时更长。CLI + Skill 将任务提交、状态查询、终态判断和结果回收沉到工具层，让 Agent 可以稳定完成长链路任务。

**端云协同**

基础剪辑类任务适合在本地完成，成本低、确定性强；画质增强、字幕擦除等重算力任务适合交给云端。Agent 不需要理解底层算力细节，只需要围绕目标编排任务。

**多入口统一底座**

企业后端可以走 API，开发者和 CI 可以走 CLI，Agent 用户可以走 Skill。不同入口面向不同使用场景，但连接的是同一套 AI MediaKit 能力体系。

这让 AI MediaKit 不只是一个能力集合，而是逐步成为面向 Agent 的音视频工作台。

**面向更大的音视频 Agent 生态**

从内容创作到企业生产，音视频任务天然是长链路任务。一次成片往往涉及理解、剪辑、字幕、音频、增强、导出等多个环节。过去，这些环节需要人操作多个软件，或者开发者手动接入多个 API。

Agent 带来的变化，是这些工作可以被重新组织成自然语言驱动的工作流。

对开发者来说，AI MediaKit CLI + Skill 降低了接入门槛；对 Agent 来说，它提供了一组可调用、可组合、可回收结果的音视频工具；对内容生产场景来说，它让从生成到交付的链路更自动化、更稳定。

未来，随着 AI MediaKit 100+ 音视频能力持续开放，CLI 和 Skill 也会持续跟进，让更多音视频处理能力进入 Agent 工作流。

模型让 Agent 拥有生成内容的大脑。AI MediaKit CLI + Skill，则让 Agent 拥有处理和交付音视频的工作台。

**让 Agent 成为音视频工作台，这只是第一步。**

**了解更多**

* 访问 **AI MediaKit 产品官网**（https://www.volcengine.com/product/imp）
* 访问 **mediakit-cli GitHub 开源仓库**（https://github.com/volcengine/mediakit-cli）

快速开始：

安装 CLI 与 Skil

```
npx @volcengine/mediakit-cli install -y
```

或给你常用的 Agent 说：

```
帮我安装一下mediakit cli和skill：https://github.com/volcengine/mediakit-cli
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecQgbYqptTtKSZcjcEBsswoqAPqg4L1vGXRj9uBZfuuHnXaFmULRdZ78ZZYg5fsAJr3gKs9HWPn09RC3V5tct2Mow2B1q3Yokg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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