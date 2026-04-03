---
title: MCP也过时了？CLI 才是 AI Agent 的终极进化方向？
url: https://mp.weixin.qq.com/s/ML94qzZYRhTdwK9IHRiAqw
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:24:09.881505
---

# MCP也过时了？CLI 才是 AI Agent 的终极进化方向？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BowImrBK4tLrX8Wsw8tkmoTSIQbJTIoEGOK3e9bMxR0bEv9wCibNicoetpN2t2e4nLLupeydOYKDzbHNIW05bJaOLzcrib3BPC27Ey7NicbOeUQ/0?wx_fmt=jpeg)

# MCP也过时了？CLI 才是 AI Agent 的终极进化方向？

原创

YangYang
YangYang

YY的黑板报

![]()

在小说阅读器中沉浸阅读

> **摘要：** 2024年我们还在讨论 Model Context Protocol (MCP) 如何统一接口，2026年，大厂和开发者们却纷纷转身拥抱“古老”的 CLI。从 Claude Code 到飞书，一场“降维打击”正在发生。

---

## 一、 曾经的明星 MCP，为什么“降落”了？

一年前，Anthropic 推出的 **MCP (Model Context Protocol)** 被视为 AI 插件的标准。它试图建立一套通用的 JSON-RPC 协议，让 AI 能够像插拔 U 盘一样接入搜索、数据库和各种 SaaS 软件。

但随着 AI Agent 走进深水区，MCP 的弊端开始显现：

1. **Token 吞噬者**：MCP 需要向模型注入大量的 Schema 描述。据测算，同样的任务，MCP 的 Token 消耗有时是纯指令的 **10-30 倍**。
2. **黑盒困境**：MCP 封装了逻辑，AI 只能看到结果。这种“隔靴搔痒”的交互，限制了高阶模型（如 Claude 3.5/4）的推理发挥。
3. **重复造轮子**：为了让 AI 查个 Git 状态，你得专门写个 MCP Server，而系统里明明已经躺着一个用了几十年的 `git status`。

## 二、 2026 的新共识：CLI 才是 Agent 的“母语”

当下的技术趋势正在发生剧烈转折：**与其教 AI 怎么用插件，不如让 AI 像程序员一样直接敲命令。**

**CLI (命令行界面)** 正在经历一场文艺复兴：

* **极致的透明度**：AI 可以看到每一条命令的报错（stderr）并自主纠错。
* **无限的组合力**：AI 能够利用管道符 `|` 将 `grep`, `awk`, `jq` 组合起来，这种灵活性是预设好的 MCP 工具无法比拟的。
* **存量市场的降维打击**：世界上 90% 的生产力工具都有 CLI 接口。AI 只需阅读 `--help`就能自学成才，无需开发者重新封装。

## 三、 巨头转身：从 Claude Code 到飞书

这场变革不是推测，而是正在发生的现实。

### **1. Anthropic 的野心：**

最新的 **Claude Code** 几乎完全抛弃了繁琐的 MCP 封装，直接在终端里“裸奔”。它直接调用系统的 `npm`, `pytest`, `gh`，效率提升了不止一个量级。

### **2. 飞书的“全量 CLI 化”：**

就在上个月，飞书正式发布了 **Lark CLI v1.0.0**。这标志着办公巨头不再执着于复杂的插件系统，而是把 2500 多个 API 全部“指令化”。
现在的 AI 助手，只需一行 `lark msg send --text "开会"` 就能接管你的办公室，这种\*\*“执行层”的效率\*\*让传统的 UI 点击显得极其笨重。

## 四、 开发者该如何选择？

这是否意味着 MCP 彻底过时了？并非如此。目前的行业分工已逐渐清晰：

* **MCP 负责“连接”**：适合跨系统、需要严格权限隔离、涉及非结构化数据（如 Notion, Slack）的场景。它是 AI 的“外挂接口”。
* **CLI 负责“执行”**：适合重度工程、高频调用、自动化办公。它是 Agent 的“核心肌肉”。

如果你在构建一个需要深度操作环境的 Agent，**请优先考虑 CLI**。在 2026 年，能熟练操控 Shell 的 AI，才是真正具备生产力的 Agent。

---

### 💡 实操手册：如何配置飞书 CLI 开启 Agent 办公？

如果你想让你的 AI 助理接入飞书，只需三步：

1. **安装**：`npm install -g @lark-opdev/cli`
2. **授权**：在飞书开放平台创建自建应用，获取 `App ID`。
3. **注入**：将应用凭证设为环境变量，AI 即可通过 `opdev` 指令直接操作你的文档、日历和群聊。

---

**今日互动：**
你认为 AI 应该像人一样点图标，还是像黑客一样敲命令？欢迎在评论区分享你的看法。

---

如果你觉得这篇分析对你有启发，欢迎**点赞、在看、转发**，我们一起见证 AI Agent 的进化。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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