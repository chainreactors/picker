---
title: 持续进化：雾帜智能推出轻量级终端神器SOAR-CLI
url: https://mp.weixin.qq.com/s/juBdpS57Sg6HWa-Rp2xkoA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:35:12.834143
---

# 持续进化：雾帜智能推出轻量级终端神器SOAR-CLI

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wrqYILmh0cn2gIf9yYXRuwcTeJlassW78EZIFhF9vQaotHpgtEhzOIakqWDia9BvgBvyHKMyYZynkS3ExTk2s2DyFAOdGyPD07heib3mbL6DE/0?wx_fmt=jpeg)

# 持续进化：雾帜智能推出轻量级终端神器SOAR-CLI

原创

雾宝宝
雾宝宝

雾帜智能

![]()

在小说阅读器中沉浸阅读

# 打通 AI Agent 与安全编排的最后一公里！

在现代企业安全运营的发展浪潮中，自动化与人工智能的深度融合正成为不可阻挡的趋势。作为安全行业创新的驱动者，**上海雾帜智能科技有限公司（flagify.com）** 在这片前沿阵地上不断落子，形成了端到端、立体化的编排与 AI 基础设施生态体系。

今天，我们正式向安全社区开源了一款全新的轻量级终端神器——**SOAR-CLI**！

---

## 🎯 我们的演进之路：从核心引擎到全面 AI 化

众所周知，我们长期耕耘的核心驱动力来源于强大的底层建设：

* • **AI SOC 产品序列** 为企业构筑了智能化的高级安全运营中心；
* • **OctoMation / HoneyGuide SOAR（编排自动化产品）** 作为能力基座，封装了海量的安全动作（Actions）与剧本（Playbooks），横向调度数百种企业内部应用与防火墙设备。

但在生成式 AI（AIGC）爆发的当下，“大模型如何直接、安全、有效地操作这些沉淀好的专业系统”成了摆在所有企业面前的新课题。为此，我们早前已经连续推出了两大重磅组件：

* • **UniMCPServer**：一款高度定制的 MCP Server 模拟器与调试利器，大幅简化并加速了大模型工具链的测试门槛；
* • **SOAR-MCP**：专门将我们的 SOAR 底座能力开放给符合 MCP 协议的各类流行大模型 IDE 及客户端（如 Claude Desktop）。

**然而，这就足够了吗？**

在实际的一线攻防、脚本运维自动化以及 AutoGPT 类野生自主 Agent 体系的开发中，我们发现很多开发者、运维人员以及轻量级的 LLM 脚手架更加依赖于传统的、通用的 **命令行终端（Command Line Interface）**。

为此，**SOAR-CLI** 应运而生。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wrqYILmh0ckL3sEWBlW8ejpOBqVnCGO5y006cOHxW0icsFic6OW0dT0CtVFkZl1K5wmvuJ0BQro8h20cuRPvnAKRI9rD58iaobiaM6seAvjNiaNs/640?wx_fmt=jpeg&from=appmsg)

---

## 💻 SOAR-CLI：是运维极客的大满贯，也是大模型最佳的“双手”

SOAR-CLI 本质上是一个使用 Python Typers 及 Rich 框架全新打造的纯终端调用工具，它极其轻量、跨平台，不仅大幅提升了人类运维人员的体验，更在底层设计上彻底倒向了“机器原生”。

### 亮点一：极致体验的人类模式 (Human-First UI)

当我们以安全运维工程师的身份登录终端：

* • **直观查询**：一键查询并以精美的终端 ASCII 数据表格（Rich Table）罗列所有的自动化剧本列表。
* • **动态寻参**：智能拉取任意剧本的入参 Schema，一目了然得知需要输入什么网段、IP 或者溯源类型格式。
* • **自动净化**：我们专门内置了富文本/DraftJS 解析器，在终端上剔除了一切恶心的底层源码残留，把清晰、友好的纯中文说明带给用户。
* • **人类语言级的容错**：如果你手滑敲错了一个 ID，或传错了参数？你不会面对冰冷的 400 Bad Request 代码，CLI 会立刻捕捉远端服务器状态并给出“剧本不存在”或“参数验证错误”等温暖的中文提示。

![](https://mmbiz.qpic.cn/mmbiz_png/wrqYILmh0clTZBjUELnKPh7H0zjbr55ZNsS9icGaYSibjWwenANqj1t19bH6yUHGCIsJolr4TN6FgttqJYuQnkCIVjIZ8fg0HMUS8ZPssoHWA/640?wx_fmt=png&from=appmsg)

### 亮点二：专为 AI Agent 定制的强制 JSON 机器模式 (Agent-Native Mode)

我们没有忘记“将业务变为给大模型的工具”。在任何命令的极简调度下，只需要加上一个全局参数 `--json` / `-j`：

* • **一键切换**：终端所有华丽的表格展示、富文本渲染被瞬间全部屏蔽。
* • **全格式解析**：输出变为绝对严格的、强字段对应的纯正 JSON 对象块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wrqYILmh0cmdp7fuGUbvib5FLIwj9rTu5riaXPo8yfpLXXaDfGBDA0Bpvg86PDxRmSv6BLwV0TN2KdSXxJPPZe8FnNfMcV7dhzScyCYLCVJFw/640?wx_fmt=png&from=appmsg)

从此，Claude Code、Codex、OpenClaw、AutoGPT、LangChain 或你们自己编写的各种野生 AI 调度脚手架、客户端龙虾，能极其精准地解析 SOAR 所有的剧本清单、出入参数甚至运行节点细节日志。

---

## 🚀 立即体验：开源社区见！

> **"工具本应好用，编排理应自由。"**

SOAR-CLI 虽然非常轻快，但它代表了我们产品拼图里关键的“最后一公里”。通过这一步，不管是人，还是活跃在各大服务器后台的智能 Agent，都能以最低的心智负担通过几个字符串命令，瞬间调动背后如同汪洋大海般的 OctoMation 能力池（隔离、阻断、封禁、通报、富化）。

**SOAR-CLI 目前已遵循 MIT 协议全面开源！** 完全允许任何人自由集成与调用。

👉 **项目地址**：https://github.com/flagify-com/soar-cli

同时别忘了我们的兄弟矩阵，构建您的全方位智能运营体系：

* • SOAR-MCP 端
* • OctoMation 核心引擎

**拥抱命令行，拥抱极客，拥抱真正可用的大模型操作能力！即刻去 GitHub 挂个 Star 吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w4F8nwSdIlA5KCGhJonnyYFW4uFib8m8733JRhucxB2RFAnUYYlF9IOA1xD3AnwTiadCeJlugF6K4H9eaWDhlOYA/0?wx_fmt=png)

雾帜智能

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w4F8nwSdIlA5KCGhJonnyYFW4uFib8m8733JRhucxB2RFAnUYYlF9IOA1xD3AnwTiadCeJlugF6K4H9eaWDhlOYA/0?wx_fmt=png)

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