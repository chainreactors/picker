---
title: 有手就行的JADX MCP环境配置
url: https://mp.weixin.qq.com/s/xds5Nw8705zQdjxPYmtZVA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:47:30.798692
---

# 有手就行的JADX MCP环境配置

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpK1KHpiaPvmYNl5iad7E2KicFLMQHynTNUcVhXaBUibvyib6dsGKONdueicXw/0?wx_fmt=jpeg)

# 有手就行的JADX MCP环境配置

哈拉少安全小队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于魔影安全实验室
，作者菜鸡Y4ph3tS

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7dyIT2lXGuWueGibaThjHuybc1ZnibEO7GjWUvhW74ZgoQ/0)

**魔影安全实验室**
.

魔影安全团队官方公众号，给做安全的朋友们提供一个技术分享的渠道。技术内容涉及网络安全各个方向。

前言

最近几天放假没出去玩，刚好在研究MCP，发现这个JADX的MCP已经相对成熟完善，刚好又有APP分析的需求，就顺手写了这个文章，其实是一篇笔记性质的文章，有需要的可以看看。后续会考虑写和其他MCP联动，工作流编排实现自动化分析任务的相关文章。

本文示例里用的是deepseek，但是根据大佬们的实测效果cc、gemini的效果其实都比ds要更好，感兴趣的可以自己探索一下。

本文使用的环境为：Ubuntu22.04+JADX1.5.3+JADX MCP Server6.0和Windows11+JADX1.5.3+JADX MCP Server6.0

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqp3rKGJaRlia1I11hic6RVZHNQZ4VLcNZAKfaolhRbBCibdjuXe5hzWNFNQ/640?wx_fmt=png&from=appmsg)

JADX MCP Server简介

JADX MCP Server 是一个独立的 Python 服务器，通过 MCP（模型上下文协议）与修改版 jadx-gui（参见：jadx-ai-mcp）进行交互。它允许 LLMs 实时与反编译的 Android 应用上下文进行通信。JADX MCP Server的高层级序列图如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpGfYkm9vmXzZw6licS7FpuxE1lImljY6r5jKuKUZHexZPiamicK9uBLX6A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

JADX-mcp插件安装与配置

首先下载最新版本的jadx（此处使用1.5.3）

https://github.com/skylot/jadx

然后去github找到zinja-coder大佬开发的JADX MCP组件

https://github.com/zinja-coder/jadx-ai-mcp/

下载release中的最新版本，包含一个jar文件和一个zip文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpiczH9lm8egVN7vvw5JyQm35zBCnQSMppRKQ6ibm4PLUY8jZkYB2EzOPA/640?wx_fmt=png&from=appmsg)

启动jadx，可以使用命令行安装插件

```
 jadx plugins --install"github:zinja-coder:jadx-ai-mcp"
```

也可以在jadx中选择插件-Manage Plugins-安装插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpcxrWkwCktS6bcAJ7845z1RMEMRElx1Fz8WrpM09HaicibL9QZZnwAdjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

不建议在windows下部署，因为windows问题比较多，可以考虑用Linux，linux也可以直接下载jadx的包，然后将包解压到opt目录下，在环境变量中添加jadx的路径，即可成功执行

```
 unzip -d /opt/jadx jadx-1.5.3.zip
```

完成后直接执行./jadx-gui即可运行图形化的jadx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpiaITqiafysI6oC7D4dU4V0aX0thuWlMQtuic6qzk7s17wN2Ub3YP2Ev9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

在命令行下使用以下命令安装插件

```
 jadx plugins --install"github:zinja-coder:jadx-ai-mcp"
```

uv环境配置

安装完成后需要配置其他必须项，根据项目文档首先安装uv和uvx，执行命令，该步骤需要科学上网

```
 curl-LsSf https://astral.sh/uv/install.sh | sh
```

安装完成后按照提示添加到环境变量，然后直接执行uv可以出现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpOlNhRUgtQ04PKTcCa0dWpmoBsoYWgQiatF2RkkowKcUSscgqRKWzdNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

但是现在发现了一个很离谱的问题，添加到环境变量后，很多命令直接用不了了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpb8fjjDc8DCaFZCHCVDIEUz5Wxl7jvAibkmbEaPkibv8mzhDlcDCqPnGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpbTYCgr8HQEoFlcNrzichnK11NxhFLrST5aDzD6VOed3OtupNRJ8JMOg/640?wx_fmt=png&from=appmsg)

解决方案是把uv通过cp命令放到opt的目录下，然后把新的目录加入环境变量，此时即可正常使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpiaWa0XgIQCehVED3jjq9BeCZ7GwRcRZykbeica8fJICp0QTgqB4BEVUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

建立uv的虚拟环境，和python类似，然后需要更换国内源，否则速度感人，依次执行以下命令

```
 echo'export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple' >> ~/.bashrc source ~/.bashrc uv venv source .venv/bin/activate uv pip install httpx fastmcp
```

启动MCPserver

然后就可以使用uv运行mcp server了

```
 uv run jadx_mcp_server.py --http
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpjY9xJicw2XAgdibcBBMk0GNS34LngZQBjUtJdISKQDOIxaf8z7IxxLicw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

启动jadx，并加载一个apk程序，控制台输出可以看到已经调用了MCP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpibmwZM7pZR1p57Z3f7ajP1icpdK7MagrY3jicxAI1KNVV7Wib2RW3qwa7w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

AI交互式应用配置

然后使用cherrystudio配置一下大模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpicPw24OX8bKO72O1DpbQ4J18dm0RHnyx59nvsQeOeCIXU2hfIYHpkww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

配置MCP服务器，配置按照之前命令行的输出，选择流式HTTP，路径和terminal中展示的一样

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpMbRLPvLOqvibBYNWicZyiaJh5qxM9ak32uTonMOKG13m3W69LKtojN3iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

配置一个助手，即沟通时的Assistant，提示词可以设置为“你是一个专业的安全逆向工程师”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpgiacgv8Lp8Dg5AnsYX6FbTpTb0Xj4gfkPk7Esyiayv3Ql3yyZOluzAaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

会话页启用MCP服务器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpsHvIBNiag00icGaTJxXRuBcbXPz1SlicqT2EaiccMibIcq3n3B8C4GsRn5w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58MxM8T5GmvYZRRzuDMhmibNrP9KbfcmI4KOpnRj3zj7VNRSwkvQMGuNUib0QygGg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/An8y3z8LAJRoYIOLq6oTNrsHMOleZu4sauEkatbPnvgECNKByySI4Q8u7iaQXuryHk6kew61J2KoKgCsynkqnCg/640?from=appmsg)

提交结果即可通过MCP调用对APK文件进行分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2sFaYicrjxop6J3QicqPVhz9vNRKm4uOqpcVbbZ3fjZweZiaPqAdFLCbALtz7231ThR799iaf63MgRBSzv3ArOibdlQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NS4fw7xEs2Pp1G46RcaicvGI58M...