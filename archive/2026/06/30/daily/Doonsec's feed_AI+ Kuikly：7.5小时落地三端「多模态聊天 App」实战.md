---
title: AI+ Kuikly：7.5小时落地三端「多模态聊天 App」实战
url: https://mp.weixin.qq.com/s/xVSkRLIYP0Y9Q9ia-Co2Xw
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:22:42.691980
---

# AI+ Kuikly：7.5小时落地三端「多模态聊天 App」实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz907VkBvjUSiazedaEa0CQH9eTB0qALAKR5ffWGU5TKqOygHIw9n0IOD8hF1NNCYiaUgBMIh6zDHz9xIliaVUfj8sm0N01CPjmJvaJQ/0?wx_fmt=jpeg)

# AI+ Kuikly：7.5小时落地三端「多模态聊天 App」实战

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

> Kuikly 是腾讯开源的高性能跨端框架，基于 Kotlin Multiplatform 技术，覆盖 Android、iOS、HarmonyOS、H5、微信小程序、Mac 六大平台，支撑业务日活用户超5亿。当 Kuikly 搭配真正懂它的 AI，开发会怎样——零手写代码，仅凭自然语言，7.5 小时交付一套支持 Android、iOS、鸿蒙三端的 AI 聊天 App。看 AI 如何调研组件、扩展原生模块、自行定位 Bug，感受为什么「AI + Kuikly」是当下客户端开发效率最高的组合之一。

用 28 轮对话、740 字自然语言，生成约 3500 行代码，完成一套三端可运行的多模态 AI 聊天 App。全程零手写，不看代码，1 天交付。

放在传统开发里，同样的功能 iOS、Android、鸿蒙各写一遍，要 30 人天；就算用 Kuikly 手写，也得 7.5 人天。这次用 AI 辅助，实际只花了 7.5 小时。最终交付的 App 支持流式 Markdown、拍照识图、相册选取、SSE 长连接、本地会话管理，一套代码即可覆盖 Android、iOS、鸿蒙三端。

这不是“Vibe Coding”的玄学叙事，而是一次“AI + Kuikly 跨端框架”的实弹演习。Skills 和 Rules 让 AI 始终保持在正确的技术上下文中，组件库开箱即用、三端模板一键生成，这套基础设施支撑起了“AI + Kuikly”的协同效率。之前[搜狗输入法用 Spec Coding 把新页面开发从 3 天压到 1 天](https://mp.weixin.qq.com/s?__biz=MzA3NTYzODYzMg==&mid=2653581729&idx=1&sn=01305c91e3322a576ad858a6fed6609c&scene=21#wechat_redirect)，[QQ 音乐用 AI 智能转码实现 90%+ 代码采用率](https://mp.weixin.qq.com/s?__biz=MzA3NTYzODYzMg==&mid=2653581858&idx=1&sn=0ef8ee7a3ae6c85bc83909811678cc48&scene=21#wechat_redirect) ，效率红利正在被验证。

说到底，这次实验就想回答一个问题：纯靠对话，能把事情做到什么程度？一天之后，我有了答案。

![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUAgugukbvA9CsdhWADAR9LGlQslD0AeQ1YaZHpJAnLLyDeHDCAUaywxKublehJzotFibXTIa3KxlPiavty9IcKukzzWsy8tBxaYc/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=0)

![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUBXlRF8KTic6Dpib6YY0TSP72icefbDTSxrdgZNmX239hBNcQBnktlSL3PjZeBdH7voIsCt3kXIGic91D9UVZoNq0I7EDOSo8XlUyo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=1)

![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUCVk81ibSLZmB7VeY2mTickwkWQRS8N5GpvYic6pJDbUnQ98I51F34tUgHCyMIExkpPoBkhCP3JKFr6JRC5kWPGv56e2FcIRnchfY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=2)

下面是这一天的真实日记。

AI Coding 全过程

先把这一天的节奏拉成一条时间线：

![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUCJeOeN1jfYaCJ59cibzFgqNcc8HGbd7Uu840n4wfkjZiaBCtyzBTwBOzWxGe5j5JXamEd97ARlbV3MluPGIvmgLb9c3wbDSeM3k/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=3)

## 09:00 - 09:10｜环境准备：先把 AI 开发环境搭起来

动手写代码前，得先把 AI 的“工作环境”备齐。

先跟着[KuiklyUI GitHub 仓库](https://github.com/Tencent-TDS/KuiklyUI)的指引装好 IDE 和 Kuikly 插件。我本地早就配好了，直接跳过这一步，开始创建模板工程。按向导填写信息、一路点下一步，Android、iOS、鸿蒙三端的工程文件就准备好了。

> 觉得 Kuikly 有意思的话，欢迎给 [KuiklyUI GitHub 仓库](https://github.com/Tencent-TDS/KuiklyUI)点个 ⭐️ 关注，以后好找。

接着，按照官网[AI编程](https://kuikly.tds.qq.com/AI/)的指引在工程里安装 Kuikly AI 的 Skills 和 Rules。

```
npx skills add Tencent-TDS/KuiklyUI-AI/skills
```

这一步很关键。Kuikly DSL 相对专有，通用大模型的训练语料覆盖并不充分，而 Skills 和 Rules 能把框架知识喂给模型，让 AI 像一个熟悉 Kuikly 的开发者一样工作。

到这里，Kuikly 的 AI 开发环境就算准备好了，然后我切到 AI Coding 的主场：CodeBuddy。

## 09:10 - 10:20｜需求分析与方案设计：先确定能复用什么，再决定自己写什么

这是一个完整 App 而非单个页面，所以我没让它直接开写，而是先用 CodeBuddy superpowers 插件里的 `brainstorming`技能把需求拆清楚。

**给它的第一条指令：**

> /brainstorming 使用 Kuikly 实现一个多模态 AI 聊天 App，一码三端，支持 Android、iOS、鸿蒙。核心能力包括：发送文本/图片消息、拍照发图、相册选图、AI 流式回复、Markdown 渲染、打开消息中的网址、本地会话管理、历史会话恢复。优先使用 Kuikly 官方和社区已有组件。

这条 Prompt 写得比较完整，关键是两点：明确“一码三端”，不是只跑 Android 的 Demo；强调“优先使用已有组件”，避免它上来就造轮子。

**组件查询**

AI 随即调用查询第三方组件的技能，筛出一份匹配清单（`KuiklyChatUI`、`KuiklyMarkdown`、`KuiklyAlbum`、`KuiklyCamera`、`KuiklySQLite`、`KuiklyWebview`、`KuiklyToast`），接着并行访问它们的 GitHub 信息调研用法与平台支持。

有个细节挺有意思：AI 本来在清单里选了`KuiklyMarkdown`来做 Markdown 渲染，但调研后发现 `KuiklyChatUI`里的`AiMessageText`已覆盖 AI 消息的 Markdown 渲染场景，于是不再单独引入`KuiklyMarkdown`，最终落地 6 个组件。这就是 Skills 和 Rules 的第一个收益——AI 开始知道什么时候**不该写**。

确定组件清单后，AI 还标出两个需要用 Kuikly 的 Module 机制扩展的能力缺口：

1. 现有`Network`不支持 SSE 长连接，需补一个`SSEModule`
2. 图片发给多模态模型前需统一压缩和 base64 编码，需补一个`ImageModule`

过去用 AI 写代码，最怕它把所有问题都包装成"没问题，我来实现"，然后一路写到编译报错。这次 AI 则表现得像一个资深的 Kuikly 开发者，我知道这是 Kuikly AI 的 Skills 和 Rules 的功劳。它们很好地充当了 AI 的缰绳，哪些用组件、哪些自研、用何种方式组织代码，都被框得很清楚。

**方案基本确定**

* 聊天主体用 KuiklyChatUI
* Markdown 能力复用 AiMessageText
* 拍照和相册分别用 KuiklyCamera、KuiklyAlbum
* 会话历史用 KuiklySQLite
* 外链打开用 KuiklyWebview
* 轻提示用 KuiklyToast
* SSE 和图片压缩编码用自研 Module 补齐

AI 接着推演了架构、数据结构和交互设计，整体合理，我基本没打断，很快就拿到了第一版开发  plan。

## ![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUDXxwQEqosWD0basrBbfo3icseHQI4BARZ5ibWh9eoodKW5jk6lfibSBkAPWkBOFuqyZvCv7ythiafYVAHpoytokVkEB6Km07TP5Tw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=4)

## 10:20 - 11:10｜编码实现：AI 是怎么把代码写出来的

plan 确认后，我基本就让 AI 自己往下跑了，中途没有太多打断。

值得说一下的是它在不同环节调用的技能，这也是这次"AI 真的懂 Kuikly"的关键。

补两个框架没覆盖的能力时，它用的是`[skill:kuikly-expand-api]`——也就是 Kuikly 官方提供的"扩展原生 API / 自定义 Module"技能。`SSEModule`和 `ImageModule`这两个跨端 Module 都是靠它生成的：从 commonMain 的接口定义，到三端 native 侧的桥接实现，技能里都有明确的规范可循，AI 不用凭记忆去猜 Kuikly 的 Module 写法。

![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUCWhgTyDbSdGEyYTQN0GDkoB5hYBdgEJXUm0d6IGhWkhib9x23nCCzMF8yEy3aEYmHrr2gKfNdCbRSxRviapYGuZUucLanDBLaBk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=5)

实现聊天主页面和历史会话列表页面时，它用的是`[skill:kuikly-ui-framework]`和`[skill:kuikly-reactive-observer]`。前者负责 Kuikly DSL 的页面结构和组件用法，后者负责响应式状态——消息列表、流式回复这些需要随状态变化自动重渲染的地方，都是靠`observable`把数据和 UI 绑起来的。

![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUC8qjq5DSlj60l83wuw80Hnm55t3ZibEzyrnNBx9IDDvq22qelDhgLiarvHGkKx2l5EiaeRBNiaAZBqe9HwZ8NHT28WdWaboor6tUw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=6)

整个过程给我的感觉是：AI 不是在"硬写一种它半懂的 DSL"，而是每到一个环节先加载对应的 Kuikly 技能，再按规范动手。该用哪个组件、该扩展哪个 API、状态怎么绑，基本没走偏。

## 11:10 - 12:30｜集成自测：上真机测试，发现一个图片加载缺陷

plan 执行完，我先在 Android 真机上跑。

**一次编译就成功了。**

App 起来，界面干净，输入框、消息列表、发送按钮都在。我发出了第一条文字消息，AI 流式回复正常滚了出来，Markdown 也渲染对了。

![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUCAHbkfMeLvVfjj2eOSTHPRBDIxM00grzyia0Sh2NQB2S2TY7dk6hYia3oEfXKibticmsxicHnFA7wZwvrjxWrfBCMoARkZb6J5vj0Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=7)

对于一个一码三端、还自带 SSE 长连接和多模态结构的工程来说，第一次真机运行就直接跑通文字链路，这个结果比我预期要好。

文字链路没问题，我接着试图片消息。

**图片链路出问题：让 AI 自己定位**

点开相册，选图页面正常打开了——缩略图宫格布局也铺出来了，**但每一格的缩略图都加载不出来**，整片宫格只有一个个空白格子，看不到图，自然也没法选。

![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUDQGESYj3rKkuoOs6Ba4ianf3fXDVfCpQHpibuParMcwFC10Z67RdhjyJIoYtSLYFw5GdfMle8ibZ1bH3zz5UPaXfQ5jfzffaxWmk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=8)

我没有自己去翻代码，直接把现象和文件甩给 CodeBuddy，让它自己查：

> `@ImagePickerPage.kt` 的图片加载不出来，请添加日志，用adb自行分析原因

AI 按我说的先加日志、再用`logcat`抓日志，用`adb`注入操作复现，顺着日志一步步缩小范围。

很快它就定位到了根因：

> 相册组件给每张缩略图的图片地址是 **content provider 格式**（`content://...`），而模板工程默认实现的 `ImageAdapter` 只处理了 base64、http、assets、file 几种来源，没有认 `content://`这种 URI，所以每张缩略图都解码失败、显示空白。

定位清楚后，它在`ImageAdapter`加上了对 content URI 的识别，重新运行，相册缩略图全部正常显示，选图、发送也都通了。模型能正确识别画面主体并给出对应回答，说明多模态理解链路也跑通了。

![图片](http://mmecoa.qpic.cn/mmecoa_png/2YTOibpx9RUDblFgoBMOhEuqPtQve0rRgW9H7W9oJiccClmNbXiaJ6B6ujgsicsMCicCUmtzO6YluPbjsNZOFytQnjpeRaA10KaAdgApOFiaRwuVw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=9)

这个问题的链路其实很长：从 `KuiklyAlbum`组件取出缩略图信息，到跨端的 UI 组织，再到原生图片控件上屏，每一步都可能是原因。但因为有 Kuikly AI 的知识库托底，AI 省去了研究框架源码，**我只给出问题现象、相关文件和分析要求，它就能自己加日志、用 logcat + adb 把根因一路查到`ImageAdapter`这一层**，就这样轻描淡写地把问题解决了。它再一次扮演了一个资深 Kuikly 开发的角色。

## 14:00 - 17:30｜迭代优化：把"能用"磨成"好用"

文字和图片链路都通了，剩下的就是细节打磨。产品体验的反复推敲，在原生开发里最磨人，也最容易出现平台不一致。而跨端框架的优势正在于此：一次修改，三端同步改好；配合 Kuikly AI，很多修改进一步简化成了一句 Prompt。

我基本是一条一条把问题丢给 AI，它改完我真机验证，再提下一个。

**1）键盘遮挡输入框**

最先碰到的是老问题：键盘弹起来，把输入框挡住了。

我让 AI 监听 `keyboardHeight`，用外层容器的`paddingBottom`把输入区顶上去。它顺手还处理了一个细节——Kuikly 的键盘事件要挂在`Input` / `TextArea`上，而`ChatSession`内部的输入框不暴露这个事件，于是它在页面内挂一个代理 Input 承接 Kuikly 的键盘事件回调。这个绕法挺地道，不是我提示的。

**![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUAl86c0xSibYQFNfR5c9icRLAtQ2av79YWvsAUovqNVicbVNc6rNfiafZ4CCaibJ6o8JFAYcV58F3Eic57WV1UnB8NUBBsMIk87YPjAs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=10)**

**2）鸿蒙上新建会话不生效**

在鸿蒙端验证时发现一个偏功能性的 bug：新建会话后，历史列表里始终只有那一条旧会话。

把现象交给 AI，它顺着路由链路定位到根因落在鸿蒙的`RouterAdapter`，这是 Kuikly 处理页面...