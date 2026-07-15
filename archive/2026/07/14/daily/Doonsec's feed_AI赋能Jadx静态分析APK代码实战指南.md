---
title: AI赋能Jadx静态分析APK代码实战指南
url: https://mp.weixin.qq.com/s/IpecR0YXm7C7T3JD0KSLXw
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:46:10.769241
---

# AI赋能Jadx静态分析APK代码实战指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dBEVa0kEoRAib8fPmoe77lLdHhhw4QXgsERAfpmibQmske7aJxw3RVIw9QibicvMakgIQLLMiaUK8ic86aHwNUibhEBsUCOeOTSk9K9IGBsKByKQaU/0?wx_fmt=jpeg)

# AI赋能Jadx静态分析APK代码实战指南

王全洲
王全洲

国家网络空间安全云社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

当AI遇上Jadx ，Android逆向从未如此简单。本文手把手教你用Trae和Claude Code两种方式 ，通过MCP协议和命令行让AI帮你读懂APK代码。

***写在前面***

Jadx是Android逆向中最经典的反编译工具之一 ，能将DEX/APK反编译为可读的Java源码。过去我们用它时 ，流程通常是：反编译 → 在成千上万个类中翻找 → 肉眼定位关键逻辑 → 手动分析。

现在 ，AI来了。

通过**MCP（Model Context Protocol）**协议 ，AI可以直接"看懂"反编译后的代码 ，你只需要用自然语言提问 ，它就能帮你搜索类、分析逻辑、提取协议 ，甚至生成Frida Hook脚本。

本文将围绕**两种使用方式×两款AI**工具 展开：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDUopxhDEARhLic03ibchGhp8GHDVQCY8wzxKUGPavO5qg4tkJljFibkXjOvPJ7QGS0YibhNYfR9mkvwP6Vd6AqX4jh0ibWHv4vJeRo/640?wx_fmt=png&from=appmsg)

两款AI工具分别是**Trae**（字节跳动出品的AI原生IDE）和**Claude Code**（Anthropic出品的命令行AI编程助手）。

**0****1**

***通过MCP方式使用Jadx***

MCP（ Model Context Protocol）是Anthropic推出的模型上下文协议 ，它为AI模型提供了一套标准化的工具调用接口 。对于Jadx来说 ，MCP意味着AI 可以直接调用Jadx内部API，实现类搜索、源码查看、资源读取等操作。

**架构原理**

在开始配置之前 ，先了解MCP方式的工作原理：

AI客户端（Trae /Claude Code）

               │  MCP 协议（JSON-RPC over stdio）

               ▼

JADX MCP Server（Python服务，负责转发请求）

               │  HTTP请求（默认 127.0.0.1 :8650）

               ▼

JADX-AI-MCP插件（运行在 Jadx-GUI 进程内）

               │  调用Jadx API

               ▼

Jadx-GUI（当前打开的APK工程）

MCP Server是一个Python中间层 ，它接收AI客户端的工具调用请求 ，再转发给Jadx-GUI中运行的插件去执行。所以整个链路中 ，**Jadx-GUI必须保持打开状态。**

**核心工具一览**

配置完成后，AI将拥有以下能⼒（以jadx-ai-mcp/ jadx-mcp-server为例，共约27个⼯具）：

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAUEYTj0dXo21oa9UQ3Voytd9nELemmyBHyicY33BmAasiaLraGdAXbsRFB0TVMMQpmsa5DJpw8fsZCViaHvAV9ybb75SCMFMQELc/640?wx_fmt=png&from=appmsg)

**1.1 在Trae中通过MCP使用Jadx**

Trae是字节跳动推出的AI原⽣IDE，内置了强⼤的智能体（Agent）系统，天然⽀持MCP协议。下⾯⼀步步配置。

**第一步：环境准备**

# 1. 确保已安装Java 17+

java -version

# 2. 下载jadx最新版（如 jadx-1.5.5）

# 从 https://github.com/skylot/jadx/releases 下载

# 3. 安装 jadx-ai-mcp 插件（二选一）

# 方式 A：命令行安装（推荐）

jadx plugins --install "github:zinja-coder:jadx-ai-mcp"

# 方式 B：GUI手动安装

打开 jadx-gui → 插件 → 管理插件 → 安装插件 → 选择 jadx-ai-mcp-xxx.jar

# 4. 下载 jadx-mcp-server

# 从 https://github.com/zinja-coder/jadx-ai-mcp/releases 下载 v6.3.0 版本

wget https://github.com/zinja-coder/jadx-ai-mcp/releases/download/v6.3.0/jadx-mcp-server-6.3.0.zip

unzip jadx-mcp-server-6.3.0.zip -d jadx-mcp-server

cd jadx-mcp-server

# 5. 安装Python依赖（推荐使用uv）

pip install -r requirements.txt

或

uv sync

**第⼆步：在Trae中添加MCP配置**

打开Trae，进⼊**设置→MCP服务器**，点击「⼿动添加」，填写以下JSON配置：

{

    "mcpServers" : {

        "jadx-mcp-server" :  {

            "command" : " uv" ,

            "args" : [

                "--directory" ,

                "D:\\tools\\jadx-mcp-server-v6 .3 .0\\jadx-mcp-server" ,

                "run" ,

                "jadx\_mcp\_server.py"

            ]

        }

    }

}

**提⽰：** 如果环境中没有uv，也可以直接用 Python解释器：

    {

        "mcpServers" : {

            "jadx-mcp-server" :  {

                "command" :

"C:\\Users\\xxx\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",

       "args":["D:\\tools\\jadx-mcp-server\\jadx\_mcp\_server.py"]

        }

    }

}

**第三步：启动与使用**

1. **打开Jadx-GUI**，加载你要分析的APK
2. **在Trae中创建智能体**：AI对话⾯板右上⻆设置图标 → 选择MCP，勾选jadx-mcp-server
3. **开始对话**，⽤⾃然语⾔下达分析指令

**实战示例对话：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRApX7iaU1Y43In3luRD3MLtrWFjxvaHaJs3ojNaXfZOrzo5kBJHmUiaC6QXQicOqHNdibiciauYoPPVBjdLoKGvXmlbzsqsDBsJUCF1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dBEVa0kEoRCLVLc9AqzsBkzP6XoQzibDodu5UMx5AqyN5O9x2InodpZRNnwA4D1m4xIXcMZRdRZ8wta4c2TDZJf3EE8mc1VoibuYueFONG1LQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRCbwujdurtlyDkUArNn6pjSN3g8kJicicPU5gOCRbQYzI7KX8bJnaJh9YQGFzhPkOnTdibJIfhIzoAaPLuMMC8p41ggrw2FzA3kcQ/640?wx_fmt=png&from=appmsg)

**关键配置技巧**

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDN6hgpicibD1icrEmwAtrXssy23Nkav4nnJtaicLISVsNpianSsHc3Yoesy1mkxianWjwIicLb9CVnezDg0XV1G8L7gGBiaK2NmOVqNWU/640?wx_fmt=png&from=appmsg)

**1.2 在Claude Code中通过MCP使用Jadx**

Claude Code是Anthropic官方推出的命令行AI编程助手 ，同样支持MCP协议。可以在两种环境中配置：

* **Claude Desktop**（桌面应用）：配置  claude\_desktop\_config .json
* **Claude Code CLI**（命令行）：通过 claude  mcp  add命令或项目级配置

下面我们介绍命令行模式配置 MCP。**通过****Claude Code CLI**配置，在项目目录中直接添加MCP服务：

# 使用claude mcp add 命令

claude mcp add jadx-mcp-server -- uv --directory /path/to/jadx-mcp-server run jadx\_mcp\_server.py

**在****Claude Code****中使用**

1. 先启动**Jadx-GUI**并打开APK

2. 启动**Jadx MCP Server**

3. 在Claude Code中直接提问

**实战****⽰****例对话：**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dBEVa0kEoRC8tSxeVbmGiagIsPUDU0Tars6TMaJ0AL4WziatQW3dauuyMibORicficibF7dF5sKRh7icS2jriajDEM3lfyp8hHib6zdZzhclDjyxE2Mc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dBEVa0kEoRCOfP7BmNsmcpaHZNPlGtMGGQ1vh1dCicXhr5X9oibRLStkbEvMKv3MNZ6swsVicFnIictnJnybic2icgu2KGBribBXezHfU3y0VPAgW4/640?wx_fmt=jpeg&from=appmsg)

**使用 Android-pentest-mcp（进阶方案）**

如果你需要更完整的 APK 安全测试能力 ，可以试试社区中更成熟的**Android-pentest-mcp**项⽬ ：

# GitHub: https://github.com/imcfyulong/Android-pentest-mcp

# 包含27个MCP工具，覆盖 APK  解包、反编译、代码扫描、动态 Hook

claude mcp add android-pentest-mcp -- npx /path/to/android-pentest-mcp

接入后只需一句话："帮我测试这个 APK 的安全问题" ，AI 就会自动执行 5 个阶段的渗透测试工作流：

![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRCv8Bn4GOQUWzjcicQnjXzy8qIiacBw4M2WMzBjXsX9lpROdGn8bryzeEd4EkqdH0HZ8xdQhEibLokW7l39tkB37ZVBSMtic4wx5ec/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/dBEVa0kEoRBv5VMO8dLo9qMtXj16v7CuapVSf83hiaficnESK9zJJrVVoic3iak1aDN59f70F72VWJGCabeDQ32H3ZyVlKPequnVkmv5OkmjA0o/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***通过命令行方式使用Jadx***

MCP 方式虽然强大 ，但它要求 Jadx-GUI 保持打开状态 ，且需要完整的 Python 中间件。对于**批量反编译**或**自动化流水线**场景 ，直接在终端中调用 Jadx CLI 往往更高效。

在 AI 时代 ，我们仍然可以让 AI 帮我们生成和执行命令行——AI 充当"指挥官" ，Jadx CLI 充当"执行者"。

**Jadx CLI 常用命令速查**

# 基本反编译

jadx -d output\_dir target .apk

# 生产环境 APK 推荐：启用反混淆

jadx --deobf -d output\_dir target .apk

# 只反编译代码，不处理资源（省时省内存）

jadx --no-res -d output\_dir target .apk

# 限制线程数（大 APK 防 OOM）

jadx -j 2 -d output\_dir target .apk

# 导出为 Gradle 项目

jadx --export-gradle -d output\_dir target .apk

# 显示反编译失败的代码

jadx --show-bad-code -d output\_dir target .apk

# 调整 JVM   内存处理超大 APK

JAVA\_OPTS="-Xmx8G" jadx  -j  1  -d  output\_dir  huge .apk

# Windows环境下为

set  JAVA\_OPTS=-Xmx8G

jadx -j 1 -d output\_dir huge .apk

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRARIyy60cCwlzsAxNamo2hbPY8M5kyanpHmPBFq6tyYK8TNOOxJNhdpelAqywlT0WxEHpGw71qvBZExoWksbS6hgSIjfGL0Krc/640?wx_fmt=png&from=appmsg)

**2.1 在Trae中通过命令行使用Jadx**

Trae的智能体不仅能通过MCP调用工具 ，还能直接在终端中执行命令。这意味着你只需要描述需求 ，AI就会自动拼装并执行 Jadx 命令。

**使用方式一：自然语言驱动**

直接在Trae的AI对话中输入：

你：帮我用jadx反编译当前目录下的 test .apk，输出到 decompile 目录，不要资源文件，启用反混淆。

Trae：好的，我来执行以下命令：

jadx --deobf --no-res -d decompile test .apk

Trae的智能体会自动在终端中执行该命令，并将输出结果返回给你。

**使用方式二： 结合 Python脚本批量反编译**

让Trae帮你编写批量反编译脚本 ，然后一键执行：

你：帮我写一个 Python  脚本，批量反编译当前目录下所有的 APK  文件，每个 APK 输出到对应名称的目录中。

Trae：好的，创建 jadx\_batch\_decompile.py：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRCvhZiaTek183PFjAnwmVAAdvlpSAQiaRIu81ia7oyZXuiaRb8Qmn0AxjbmDGqngE0q0oL9jZ3qLB2dkwRRKDfbRw14N9ibjI8icxQYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRABNWR56dsA3uXCMk1869aiae9avxbqBk3O49rk6zRPX6r0vcL8kcAZTLtXPhUScY7TuOXsT83lkO0XNa7lySCdibffF1TMwo2Vs/640?wx_fmt=png&from=appmsg)

然后让Trae在终端中执行它：

Trae：脚本已创建。现在运行它：

python  jadx\_batch\_decompile .py

**实战技巧**

你：jadx 反编译完了，帮我在 decompile 目录中搜索所有包含 " password " 或 " secret " 的文件

Trae：好的，在反编译结果中搜索敏感信息：

grep -r -l --include= " \* .java "  -E  " (password|secret|apiKey|token) "  decompile/

decompile/sources/com/example/util/CryptoHelper.java decompile/sources/com/example/network/ApiService.java

**2.2 在Claude Code中通过命令行使用Jadx**

Claude Code作为原生命令行AI助手 ，执行终端命令是它的核心能力 。它不仅可以运行Jadx CLI，还支持通过Skill插件自动编排反编译工作流。

**使用方式一： 直接执行命令**

$  claude

>反编译当前目录的 app .apk，启用反混淆和 4  线程，输出到 decompiled   目录

Claude Code:  好的，我来执行反编译命令。

$  jadx --deobf -j 4 -d decompiled app .apk

INFO  -  Processing . . .

INFO  -  Decompiling with 4 threads

INFO ...