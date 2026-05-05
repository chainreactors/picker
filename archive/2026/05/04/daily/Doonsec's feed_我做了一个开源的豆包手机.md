---
title: 我做了一个开源的豆包手机
url: https://mp.weixin.qq.com/s/WqscKGhQ2-0tFd-pzeygJg
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:57:14.297506
---

# 我做了一个开源的豆包手机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fib1FQSshPPibEDpz6S9LZuu0Arg75GqWpD1RHwKzREnBg3gNib0Bu9p8THCfxg5qMiaMRDUQxdhRSz0NEB19km3PUn1hkD3qicbzMIcNQMPmHIU/0?wx_fmt=jpeg)

# 我做了一个开源的豆包手机

原创

Flanker
Flanker

Flanker论AI

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> OpenCyvis 是一个开源的 AI 手机方案。用户可以自由选择 LLM 后端（云端或本地），AI 在后台虚拟显示器上操作，不占用前台屏幕。Apache 2.0 协议，代码完全公开。

## 背景

过去一年，不少厂商推出了「AI 手机」的概念——豆包、三星 Galaxy AI、Google 的 Gemini 集成等等。核心思路大同小异：AI 理解屏幕内容，代替用户完成操作。

但这些方案有一个共性：它们都是封闭的。模型由厂商指定，数据通过厂商的服务器处理，用户没有办法审计中间发生了什么，也没有办法换一个自己信任的模型。

开源社区也有一些尝试，比如基于 ADB 的各种PhoneUse项目。它们可以让用户自定模型，但需要连接电脑，且 AI 操作时会直接占用用户的屏幕。

于是我做了OpenCyvis ，试图同时解决这两个问题。

---

## 核心设计

### 开源 + 模型可选

这是整个项目最重要的一点。

一个能看到你屏幕、操作你 App 的 AI，本质上是手机里权限最高的软件。它运行什么模型、截图发给了谁、数据经过哪些环节，用户应该有能力去验证，而不是只能相信厂商的承诺。

OpenCyvis 的做法是：代码全部开源，LLM 后端由用户自己配置。目前支持三类：

| 后端类型 | 示例 | 说明 |
| --- | --- | --- |
| OpenAI 兼容 API | Qwen、GPT、 Mimo | 默认方式，接入任意 OpenAI 兼容的 endpoint |
| Anthropic API | Claude Sonnet | 原生 Anthropic 协议 |
| Ollama（本地或自建） | Gemma 4、Llama、Qwen | 模型运行在本地，截图不离开设备 |

选择本地模型时，整个流程——截图、推理、执行——全部在设备端完成，没有任何网络请求。

**能力演示：一句话串联多个操作**

![三合一任务：设闹钟 → 开勿扰 → 切暗色主题](https://mmbiz.qpic.cn/mmbiz_gif/fib1FQSshPP9wxic2ibAhgNtibIsD4zSEsuuKHUricQOJ4UE7od45ckjuljszaUSibh3CXfh2ZoGq8Ywnc7PibmdIBpPTMvkyEpkeAwUaJAlY4l2h0/640?wx_fmt=gif)![跨应用比价：Amazon vs Walmart](https://mmbiz.qpic.cn/mmbiz_gif/fib1FQSshPP8A3GRc2YyMUX5Q4kvdkoDkgke9CiavWjAypq5rcW6pYVHcjnDW0zMSgVwXBUPvlwJVQRribiaBuXY55QGarZVQ2IHgsNaJ1ScAhY/640?wx_fmt=gif)

### Agent 如何理解和操作

OpenCyvis 的核心是一个 observe → think → act 循环。每一步，模型同时接收两种输入：

![Observe → Think → Act 循环](https://mmbiz.qpic.cn/mmbiz_png/fib1FQSshPPib7kMoVsN7iaDdouDy8BGWIoWicNqv6mpoBrSKicBTnDkibw9FoNvNeWW9PET3jAmCUz7yDhJ6JLe310GuCSuLa91jUiabLOqtpxIuc/640?wx_fmt=png)

Observe → Think → Act 循环

**截图 + UI 元素树（双通道感知）**

目前大多数开源 phone agent 只依赖截图——让模型"看"屏幕然后猜测点击坐标。这种纯视觉方案在复杂界面上经常点错位置。

OpenCyvis 同时提供两种输入：截图让模型理解当前界面的语义和布局，UI 元素树（Accessibility Tree）提供每个控件的精确坐标、类型和层级关系。两者互补——视觉信息解决"这是什么"，结构信息解决"它在哪里"。此外，当模型陷入死循环时，本地快速哈希相似性检测也可以为模型作出有效提示。

**原生 Tool Calling（14 种动作）**

很多开源方案让模型输出自由文本（如"请点击屏幕中间的按钮"），再用正则表达式解析出坐标和动作——这种方式脆弱且容易出错。OpenCyvis 使用 LLM 原生的 function calling 协议，模型直接返回结构化的 JSON 动作指令。支持的动作包括：

* • **操作类**：tap、long\_press、swipe、type\_text、key\_event（返回/主页/回车等）、open\_app
* • **流程控制**：wait（等待页面加载）、finish（任务完成）、fail（无法完成）
* • **交互类**：ask\_user（向用户提问）、handoff\_user（交还控制权）
* • **记忆类**：note（工作记忆）、remember（跨任务长期记忆）

这种设计使得模型的输出始终是可解析、可验证的。不存在"模型说了一句话但系统没理解"的情况。

**工作记忆（Note）**

在多步操作中，模型可能需要记住中间信息——比如在 A 应用里查到了一个价格，切到 B 应用后需要对比。OpenCyvis 提供了 note 机制：模型可以在任何一步的动作中附带一条 note，记录关键信息。这些 note 会在后续每一步的 prompt 中作为上下文回传给模型，相当于给 AI 一个"便签本"。最多保留 10 条，FIFO 淘汰。

另外还有 remember 机制用于跨任务的长期记忆——比如用户说过"我的外卖默认地址是 XX"，模型可以记下来，下次再接到类似任务时直接使用。

### 虚拟显示器：后台操作

目前开源社区的 AI 手机 / 手机自动化方案主要有两种技术路线：

**ADB 方案**：通过 USB 或网络连接，用 `adb shell input` 和 `screencap` 从外部控制手机。优点是不需要修改系统，缺点是必须连接电脑，且操作直接发生在用户正在使用的屏幕上——AI 工作时用户无法正常使用手机。

**Accessibility Service 方案**：通过 Android 无障碍服务获取 UI 树和执行操作。不需要连接电脑，但同样在前台屏幕上操作，且无障碍服务的权限模型存在局限——部分系统操作和受保护界面无法触达。

这两种方案的共同问题是：AI 和用户共享同一块屏幕。AI 在操作时，用户要么等着，要么看着自己的手机被"别人"操控。

#### VirtualDisplay 是什么

VirtualDisplay 是 Android 系统原生提供的一个 API，允许在系统内部创建额外的逻辑显示器。它本来的用途包括 Chromecast 投屏、分屏模式、以及 Android Automotive 的多屏显示等。每个 VirtualDisplay 拥有独立的显示 ID，应用可以被迁移到任意一个 Display 上独立运行。

OpenCyvis 利用这个机制，在系统内创建一个用户不可见的后台 Display。AI 需要操作的应用被迁移到这个后台 Display 上运行，AI 的截图和触摸注入都针对这个 Display 执行。用户的前台屏幕（Display 0）完全不受影响，这种方案也被部分商业AI手机所使用。

具体实现上：

* • 通过 `DisplayManager.createVirtualDisplay()` 创建后台显示器
* • 通过反射调用 `IActivityTaskManager.moveTaskToDisplay()` 将目标应用迁移过去
* • 截图使用 `SurfaceControl.screenshot(displayId)`（API 36+）或 ImageReader 回退
* • 触摸注入通过 `InputManager.injectInputEvent()` 指定目标 displayId
* • 用户查看时，通过 SurfaceView 渲染 VirtualDisplay 的内容；接管时，触摸事件转发到后台 Display

这些操作需要平台签名才能获得 `INJECT_EVENTS` 等权限，所以 OpenCyvis 需要用平台密钥签名后集成到系统镜像中。

![Watch 模式：实时查看 AI 在虚拟显示器上的操作](https://mmbiz.qpic.cn/sz_mmbiz_gif/fib1FQSshPP8CrlWSEaIDLYyMJLlPqluKL538HefzRkzwzJFBsSWxpbk1lCuic59SpsRSbLTnObtvXcuu1ULnNveia42OCXicZE9Ks5l21kFvbE/640?wx_fmt=gif)

Watch 模式：实时查看 AI 在虚拟显示器上的操作

**后台运行时的悬浮球 + 完成通知**

当 AI 在后台工作时，桌面上会显示一个悬浮球，表示 AI 正在运行。任务完成后，系统会弹出通知提醒用户查看结果。

![悬浮球 + 完成通知](https://mmbiz.qpic.cn/sz_mmbiz_gif/fib1FQSshPP8tsqWoYiaibIJFUhNyP5J5Cax9DSv1WmyfDc21ZokGM3wcvnmXGLjjkVmVFiaic3dhOgq0bZ8iceHZAWIHcfTduCQq9cNcTgewdXnU/640?wx_fmt=gif)

悬浮球 + 完成通知

---

## 和现有方案的对比

（向右滑动查看更多）

| 特性 | 商业 AI 手机 | 云手机 | ADB 类方案 | OpenCyvis |
| --- | --- | --- | --- | --- |
| 代码开源 | ❌ | ❌ | ⚠️ | ✅ |
| 用户可选模型 | ❌ | ❌ | ⚠️ | ✅ |
| 支持本地模型 | ❌ | ❌ | ⚠️ | ✅ |
| AI 工作时不占屏幕 | ⚠️ | ✅ | ❌ | ✅ |
| 无需 ADB / 电脑 | ✅ | ⚠️ | ❌ | ✅ |

---

## 本地模型实测

我测试了 6 个本地模型在 4 个真实场景（打开系统设置、拨打电话号码、识别不可能完成的任务、查找联系人）上的表现：

| 模型 | 架构 | 体积 | 推理速度 | 通过率 |
| --- | --- | --- | --- | --- |
| **Gemma 4 26B-A4B** Q4 | MoE (26B/4B) | 17 GB | 63 tok/s | 4/4 |
| **Gemma 4 E2B** Q4 | Dense (2B) | 1.8 GB | 41 tok/s | 4/4 |
| **Qwen 3.5 35B-A3B** Q4 | MoE (35B/3B) | 22 GB | 47 tok/s | 3/4 |
| **Gemma 4 E4B** Q4 | Dense (4B) | 3 GB | 61 tok/s | 3/4 |
| **GUI-Owl 1.5 8B** Q4 | Dense (8B) | 5.4 GB | 75 tok/s | 2/4 |
| **GUI-Owl 1.5 32B** Q4 | Dense (32B) | 20.5 GB | 23 tok/s | 2/4 |

几个值得注意的结论：

* • Gemma 4 E2B 只有 1.8GB，但通过了全部 4 个测试。对于日常任务，小模型的能力已经够用。
* • GUI-Owl 是专门为 GUI 操作训练的模型，但在我们的场景里反而不如通用模型。原因是它不会在不确定时主动询问用户——通用模型的 tool calling 和推理能力在实际使用中更重要。
* • MoE 架构（Gemma 4 26B-A4B）在速度和质量之间取得了比较好的平衡，是目前推荐的本地默认模型。

基座模型的能力进步非常快。可能就在去年，能本地部署的开源模型还没有办法支撑这样的应用场景——理解复杂的手机界面、规划多步操作、在不确定时做出合理判断。但到了今年，以 Gemma 4 为代表的新一代模型，已经能够很好地在本地完成这些任务。一个 1.8GB 的模型通过全部测试，在一两年前是不可想象的。

我也观察到，一些商业 AI 手机产品在模型之上构建了大量的工程约束——比如独立的意图识别系统、预定义的任务模板、分步骤的流程编排等。这些设计在模型能力不足时是必要的补偿手段。但随着基座模型本身的推理和工具调用能力不断增强，其中很多约束正在变得不再必要。模型自己就能理解意图、规划步骤、调用工具，不需要在外面再套一层硬编码的逻辑。

这也是 OpenCyvis 的设计选择：尽量少做工程约束，把核心能力交给模型本身。模型会继续进步，而硬编码的规则只会变成负担。

---

## 关于名字

OpenCyvis = Open Cyber Jarvis。

Jarvis 是《钢铁侠》里 Tony Stark 的 AI 管家——理解主人的意图，操控各种系统完成任务。我觉得这个意象很贴切：AI 手机本质上就是一个能理解你的指令、帮你操控手机完成事情的数字助手。加上 Cyber 强调它运行在数字世界，Open 表明一切公开透明。

---

## 接下来要做的事

目前 OpenCyvis 需要刷入 AOSP 系统镜像才能使用，因为它依赖平台签名权限。这是当前最大的使用门槛。

接下来的方向：

* • **更轻量的安装方式**——探索不需要刷机的方案，降低使用门槛
* • **跨设备协同**——手机和桌面之间的联动

### 愿景

AI 手机应该是公共基础设施，而不是某家公司的私有产品。我们的目标是建立一个开放的移动 AI 标准——让每个人都能拥有、审计和掌控自己的 AI 助手。

---

Website: https://opencyvis.ai

GitHub: opencyvis/opencyvis-phone | Apache 2.0
欢迎提 Issue、贡献代码。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/otTC1bvhCaw9icfEeqfhQnvFUWgvofjYRFUvsdEKQKnD4WrBr28cicN9XNxg6wb82HJKE1blr82ThK1NM9LkoHsQ/0?wx_fmt=png)

Flanker论AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/otTC1bvhCaw9icfEeqfhQnvFUWgvofjYRFUvsdEKQKnD4WrBr28cicN9XNxg6wb82HJKE1blr82ThK1NM9LkoHsQ/0?wx_fmt=png)

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