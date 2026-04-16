---
title: 【AI安全】Burp接入MCP协议！AI秒变黑客
url: https://mp.weixin.qq.com/s/zqn35U4P393H2rG5jaV_Iw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:46:32.088410
---

# 【AI安全】Burp接入MCP协议！AI秒变黑客

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y05UtykogHSNoEoGVuV21UWhgPJMibgN3L10rRicaX2h8ymqAB4npEKbakPoibkJXeTIztKAKUGxGsuedicpPWDo2tQaWZSFK2t632salb3nfBs/0?wx_fmt=jpeg)

# 【AI安全】Burp接入MCP协议！AI秒变黑客

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、打破次元壁：Burp Suite 拥抱 MCP 协议的史诗级进化 🚀🔥

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！🚀

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

各位安全研究员、白帽子黑客以及对 AI 技术充满狂热的极客们，准备好迎接一场工具链的彻底革命了吗？！💥 今天我们要探讨的，是一个真正意义上打破“次元壁”的超强黑客科技——Web 渗透测试神器 Burp Suite，与当前拥有极强推理能力的 AI 大模型客户端（比如强到没朋友的 Claude）进行深度融合！🧠💻

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHQLoa7PmX5y3CCWiacHSq8XFSNVEHJqj4VBhPZrnew4LQmesccNmk2KicWZ88Q7gwher6LV6tFQhLuNFiaIE0jJ3S91c8oaIfoDjI/640?wx_fmt=png&from=appmsg)

到底什么是 MCP（Model Context Protocol）协议？🤔 简单来说，AI 大模型虽然极其聪明，但它们通常被“关在笼子里”，无法直接触及你电脑上的本地文件、无法读取你正在抓包的流量、更无法操控你的渗透测试软件。这就好比一个绝顶聪明的军事家被蒙住了双眼，空有一身谋略却无法指挥前线。🛑

但是！MCP 协议的出现，彻底撕裂了这道屏障！🌟 MCP 协议全称是 Model Context Protocol（模型上下文协议），它的核心使命就是为 AI 大模型提供一条标准化、安全且高效的“数据总线”。通过这个协议，AI 客户端可以直接读取外部应用程序的数据源！详细协议内容大家甚至可以去 `modelcontextprotocol.io` 膜拜一下官方文档。📚

现在，PortSwigger 官方生态终于迎来了重磅插件——**Burp Suite MCP Server Extension**！🛠️ 这意味着什么？这意味着你可以在 Claude Desktop 等 AI 客户端中，直接通过自然语言与 Burp Suite 进行无缝对话！🤖💬 你可以直接对 AI 说：“帮我分析一下刚才抓到的登录接口流量，看看有没有越权漏洞的可能性”，或者“提取出 Proxy 历史记录中所有带 JWT Token 的请求”。AI 将通过 MCP 协议，瞬间调取 Burp Suite 内部的真实数据进行分析！🔍⚡ 这绝对是网络安全测试领域的“降维打击”！

为了让大家更直观地理解这个插件的超强特性，我们整理了它的三大核心功能矩阵：👇

| 🌟 核心特性 | 💡 详细解读 |
| --- | --- |
| **无缝桥接 AI 与 Burp** 🌉 | 通过标准的 MCP 协议，将 Burp Suite 的底层数据接口完全暴露给 AI 大模型，实现真正的跨应用联动。 |
| **Claude Desktop 自动安装** 🤖 | 专为当前最强桌面级 AI 客户端 Claude Desktop 打造，提供极其友好的自动化安装与配置流程，小白也能一键起飞！ |
| **内置 Stdio 代理服务器** 🔌 | 针对桌面端 AI 无法直接支持 HTTP SSE 的“物理缺陷”，插件自带底层数据流代理，完美解决通信兼容性问题！ |

---

# 二、手把手带你起飞：Burp 扩展的保姆级构建与安装指南 🛠️💻

废话不多说，我们直接进入实战环节！想要让你的 AI 化身为最强黑客助手，第一步就是要把这个神仙扩展（Extension）给完美地编译并安装到你的 Burp Suite 当中。别担心，哪怕你是纯新手，跟着下面这份保姆级指南，也绝对能一次成功！✅🎉

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHTp0Sgk6QL3HPAesYa5JSOsWt8jOvQsDSYtwLR1QpmRmhlzWibA1zmFbTd4HarwGy9PqBknZicJQf2H3uzb15Npo2rbYVvfglYOQ/640?wx_fmt=png&from=appmsg)

在开始动手之前，我们必须先检查一下你的系统环境是否已经准备就绪。磨刀不误砍柴工，基础环境的搭建是重中之重！⚠️

**环境准备与前置条件（Prerequisites）** 📝

你需要确保电脑上已经安装了以下两大核心组件，并且它们都已经被正确配置到了系统的环境变量（PATH）当中：

| ⚙️ 必备组件 | 🔍 验证方法 | 💡 组件说明 |
| --- | --- | --- |
| **Java 运行环境** ☕ | 在终端输入 `java --version` | 这是运行和编译 Burp 插件的灵魂！必须确保系统能正常输出 Java 版本号。 |
| **JAR 打包工具** 📦 | 在终端输入 `jar --version` | `jar` 命令是构建和安装扩展的绝对必需品。如果没有它，后续的打包将直接报错瘫痪！ |

**第一步：克隆绝密源码仓库 📂**

首先，我们需要把位于 GitHub 上的项目源码全部“扒”到本地。打开你的终端（Terminal）或者命令行工具，找一个风水宝地，输入以下命令：

```
git clone https://github.com/PortSwigger/mcp-server.git
```

按下回车后，稍等片刻，所有的源码就会如同天女散花般下载到你的电脑中。下载完成后，务必使用 `cd mcp-server` 命令，将当前工作目录切换到该项目的根目录中。这就像是进入了打造神兵利器的铁匠铺！🔨

**第二步：使用 Gradle 锻造 JAR 核心文件 ⚙️**

进入目录后，我们需要借助 Gradle 这个强大的构建工具来编译源码。你完全不需要提前安装 Gradle，因为项目里已经贴心地为你准备好了 Wrapper！直接在终端中敲下这行魔法指令：

```
./gradlew embedProxyJar
```

🚀 此时屏幕上会疯狂滚动编译日志，代码正在被极速编译并打包。当看到 `BUILD SUCCESSFUL` 字样时，恭喜你！核心插件已经被成功打包成了一个 JAR 文件，它静静地躺在 `build/libs/burp-mcp-all.jar` 这个路径下，等待着被唤醒！✨

**第三步：将扩展注入 Burp Suite 的心脏 💉**

拿到 JAR 包后，接下来就是见证奇迹的时刻了。请严格按照以下步骤操作：

1. 1. 🎯 **启动 Burp Suite**：像往常一样打开你吃饭的家伙。
2. 2. 🧩 **进入扩展中心**：在顶部导航栏找到极其重要的 **Extensions（扩展）** 选项卡。
3. 3. ➕ **添加新扩展**：点击左上角的 **Add（添加）** 按钮。
4. 4. ☕ **选择扩展类型**：在弹出的窗口中，将 Extension Type（扩展类型）坚定地选择为 **Java**。
5. 5. 📁 **定位文件**：点击 **Select file …（选择文件）**，然后一路寻找到你刚才编译出来的 `build/libs/burp-mcp-all.jar` 文件并选中它。
6. 6. 🚀 **一键加载**：最后，点击 **Next（下一步）** 开始加载。

只要你没有乱动配置，几秒钟后，这个 MCP Server Extension 就会在 Burp Suite 内部被成功激活！你的 Burp 已经具备了与 AI 沟通的超能力！💪

---

# 三、核心机密：无缝对接 Claude 与花式配置玩法全解析 🧠⚡

🎯 **【AI 测试环境工程化落地】**

桌面级 AI 客户端由于底层架构限制无法直接与 Burp HTTP 服务器握手，硬核极客究竟是如何通过隐藏的“代理降临”机制完美破局的？又是如何仅靠几行神秘的 JSON 代码，让 Claude 的灵魂瞬间注入并接管 Burp 的数据海洋？

👉 **本章节核心的高阶配置实战、底层协议突破指南已独家发布于「Oxo AI Security 知识星球」。** 立即加入星球解锁该部分的完整内容，打通大模型与安全工具链的“任督二脉”！不仅如此，星球内部更有海量前沿干货

---

* • 📚 **AI 文献解读**：最前沿的 LLM 安全论文深度剖析。
* • 🐛 **AI 漏洞情报**：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。
* • 🛡 **AI 安全体系**：从红队攻击到蓝队防御的全方位知识图谱。
* • 🛠 **AI 攻防工具**：红队专属的自动化测试与扫描工具箱。

🚀 立即加入 **Oxo AI Security 知识星球**，掌握AI安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

Oxo Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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