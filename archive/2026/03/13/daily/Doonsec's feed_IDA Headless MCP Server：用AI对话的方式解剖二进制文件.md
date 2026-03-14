---
title: IDA Headless MCP Server：用AI对话的方式解剖二进制文件
url: https://mp.weixin.qq.com/s/6GvxFzkvO-XpTOfqVVe6XA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:05:32.297278
---

# IDA Headless MCP Server：用AI对话的方式解剖二进制文件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfCsyytQpt0ia1DhUqxwggrCrvy6WMjsE39lnfXibee9CicT3lwicJX3NDNSbYNHJI4Sua1dCiankaEnvdAPZo40oSiaOKG1OoBJ7Ficw/0?wx_fmt=jpeg)

# IDA Headless MCP Server：用AI对话的方式解剖二进制文件

原创

工具党
工具党

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 想在Claude里直接调用IDA Pro反汇编代码？IDA Headless MCP Server做到了。它通过MCP协议暴露了52个二进制分析工具，利用Go管理多会话并发，用Python驱动真正的IDA，让你在聊天窗口里就能完成复杂的逆向工程。

## 01 痛点：为什么需要这个工具？

逆向工程师每天有一多半时间在IDA里点点点，翻函数列表，看伪代码，做交叉引用分析。这些操作重复、繁琐。

有没有一种可能，你只需要对Claude说：“打开那个libapp.so，找找里面的加密函数，看看它在哪儿被调用，把伪代码给我。”然后AI助手就能替你操作IDA，直接返回你要的结果？

IDA Headless MCP Server就是为了实现这个目标。它不是另一个独立的分析工具，而是把强大的IDA Pro变成一个可以通过模型上下文协议（MCP）调用的“云服务”。

它的架构很清晰：你用Claude Desktop或者Claude Code作为前端交互，一个Go语言写的服务器负责协调，背后的脏活累活——真正的IDA分析——交给隔离的Python工作进程去干。

## 02 核心功能：52个工具，能干点啥？

这个服务器通过MCP暴露了52个工具，基本覆盖了日常逆向的刚需操作。

* 核心分析：打开二进制文件、运行自动分析、找入口点、获取函数列表。
* 代码查看：获取指定地址的伪代码、反汇编指令、交叉引用。
* 高级支持：特别集成了对Unity游戏（通过Il2CppDumper）和Flutter/Dart应用（通过unflutter）的元数据导入，能极大地提升这类二进制文件的分析效率。
* 会话管理：支持多个分析会话并行，每个会话有独立的工作进程和4小时（可配置）的自动超时释放机制。

功能听起来不少，但它有个很实在的设计：分页返回结果。默认一次最多给你1000条数据，防止一次请求把内存撑爆或者网络卡死。

## 03 配置与安装：能跑起来吗？

想用这个工具，门槛其实不低。你需要先把家里的“重型装备”准备好。

首先，你得有正版IDA。IDA Pro 9.0以上，或者IDA Essential 9.2以上都行。这是核心，没得商量。

然后，要配置idalib。这就是让Python脚本能够无头（headless）运行IDA的关键。项目里提供了一个脚本帮你设置：

./scripts/setup\_idalib.sh

接着是环境。Go需要1.21以上，并且装好protoc工具。Python要3.10以上，用pip安装项目里的依赖。

如果你想分析Unity游戏或者Flutter应用，还得额外去GitHub上把Il2CppDumper和unflutter这两个工具弄下来。

这些都搞定后，安装就一句话的事：

git clone https://github.com/你的仓库/ida-headless-mcp.git cd ida-headless-mcp make setup

这个命令会自动把前面提到的idalib设置、Python依赖安装、Go服务器编译都搞定。

## 04 基础工作流：怎么用起来？

装好了，启动服务器：

./bin/ida-mcp-server

它默认在17300端口监听。然后你需要告诉Claude它的位置。编辑Claude Desktop的配置文件：

{   "mcpServers": {     "ida-headless": {       "url": "http://127.0.0.1:17300/",       "type": "http"     }   } }

重启Claude Desktop，理论上你就能跟AI聊着天分析二进制了。

一个典型的分析对话可能是这样的，背后的工具调用流程是：

1. `open_binary(path="/path/to/binary.so")`

   打开文件，获得一个会话ID。
2. `run_auto_analysis(session_id="...")`

   让IDA跑一遍自动分析。
3. `get_functions(session_id="...")`

   列出所有函数。
4. `get_decompiled_func(session_id="...", address=某个地址)`

   查看特定函数的伪代码。
5. 最后用`close_binary(session_id="...")`关闭会话，释放资源。

对于Flutter应用，流程更高效。先用unflutter提取元数据，然后用`import_flutter`工具一键导入。官方数据说，一次导入能创建近万个函数定义、两千多个结构体，并设置三万多个注释，效率远超手动分析。

## 05 优缺点分析：它真的那么好吗？

说实话，这个项目想法很酷，但现阶段更适合喜欢折腾的极客，或者有明确自动化分析需求的团队。

**优点很明显：**

* **解放双手：**

  把重复的IDA操作交给AI和自动化脚本，工程师可以更专注于逻辑推理和策略制定。
* **知识沉淀：**

  分析过程可以被记录、复现，甚至可以做成标准化的分析流水线。
* **并发能力强：**

  Go服务器管理多会话，可以同时分析多个样本，适合批量任务。
* **生态整合好：**

  直接集成Il2CppDumper和unflutter，解决了移动端和游戏逆向的两大痛点。

**缺点和挑战也很现实：**

* **依赖太重：**

  正版IDA是硬门槛，idalib的配置对新手也不友好。整个工具链搭建起来有点复杂。
* **学习成本：**

  你需要熟悉MCP的概念、知道52个工具各自是干什么的，以及如何通过自然语言让AI准确调用它们。这本身就需要学习。
* **调试困难：**

  当分析出错时，你需要排查是Go服务器问题、Python工作进程问题，还是IDA本身的分析问题。日志分散在不同的地方。
* **性能开销：**

  每个会话一个独立的IDA进程，非常吃内存。分析大型二进制文件时，资源消耗不容忽视。

## 06 结语：谁该试试它？

IDA Headless MCP Server展示了一个未来工作流的样子：人类负责提需求和判断，AI和自动化工具负责执行繁琐的具体操作。

如果你是以下几类人，可以考虑深入试试：

* 逆向工程团队，希望将部分分析工作标准化、自动化。
* 安全研究人员，经常需要批量分析同类型样本（比如一批Flutter恶意软件）。
* 技术极客，单纯对“用AI操作专业软件”这个想法感到兴奋，并愿意花时间折腾。

对于只是偶尔用IDA看看单个样本的爱好者来说，现在直接打开IDA图形界面可能还是更直接的选择。

这个项目在GitHub上是MIT协议开源。同类的工具还有GhidraMCP等，说明用MCP桥接专业分析工具正在成为一个趋势。也许用不了多久，跟AI助手协作进行深度技术分析，会成为安全人员的日常。

回复“ida-headless-mcp”获取项目

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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