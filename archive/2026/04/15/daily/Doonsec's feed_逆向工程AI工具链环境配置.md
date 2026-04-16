---
title: 逆向工程AI工具链环境配置
url: https://mp.weixin.qq.com/s/-VBc5UZ_uOtgt91GMkIYfQ
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:52:08.777306
---

# 逆向工程AI工具链环境配置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fpMwbItribG79NYNicHhmVqAECJxEWOImK4YoxKDtaXqT7ORSvRwxA00VBpCMsMtNnNhEK5fia9Y7DHc26v3nNODZa8R6fdJYskYTlqgo0TYLg/0?wx_fmt=jpeg)

# 逆向工程AI工具链环境配置

原创

非白即黑
非白即黑

攻有道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、前言

在 AI 的辅助下，陆续完成了多项加解密相关的逆向分析工作，分析效率和整体效果均得到较大提升，已基本具备落地使用价值。期间成功完成某软件的 gRPC Hook 篡改代码开发，以及某 Q 聊天记录数据库的加解密分析与导出（这部分分析完全由AI自主进行分析，期间我只提供了几篇文章和相应的hook日志「工具使用的codex、GPT5.4、ida-pro-mcp」）。
现对AI工具的环境配置与使用，进行一个总结。

本文主要工具及环境如下：

* • 操作系统：MacOS
* • Python管理器：pyenv、uv（远程主机）
* • Python版本：3.11.12
* • IDA-Pro 9.0
* • jadx-gui 1.5.5
* • codex-cli 0.114.0

# 二、环境配置

## 2.1、前置问题

> 在安装过程中碰到的如下这些问题，如你的环境没有这些问题可以忽略此节。

### 2.1.1、IDA默认Python环境配置问题

在此之前你可能会碰到这几个问题，IDA的Python环境管理问题

```
# Mac配置IDA默认Python环境
'/Applications/IDA Professional 9.0.app/Contents/MacOS/idapyswitch' \
  --force-path /Users/user/.pyenv/versions/3.11.12/lib/libpython3.11.dylib, 其中 /Users/user/.pyenv/versions/3.11.12 替换为你的python安装目录
# Windows配置IDA默认Python环境
idapyswitch.exe --force-path PATH\TO\YOUR\PYTHON3.11.12\python3.dll, 其中 PATH\TO\YOUR\PYTHON3.11.12 替换为你的python安装目录
```

## 2.2、逆向分析常用MCP环境配置

### 2.2.1、ida-pro-mcp

#### 安装最新ida-pro-mcp

> 项目提示Python版本不低于**3.11**，由于不想破坏我本机的Python环境我选择使用pyenv进行python环境管理，你也可以选择其他的python环境管理器进行操作。（所以以下配置我均在虚拟环境的前提下进行配置，配置过程中也使用虚拟环境的绝对路径进行配置，如有IDA默认环境问题可以看本文2.1.1。）

```
# 找到自己对于的虚拟环境目录，进入虚拟目录（我这里使用的是/Users/user/.pyenv/versions/3.11.12/bin）
cd /Users/user/.pyenv/versions/3.11.12/bin
# 先卸载旧的ida-pro-mcp
./pip uninstall ida-pro-mcp
# 安装官方最新ida-pro-mcp
./pip install https://github.com/mrexodia/ida-pro-mcp/archive/refs/heads/main.zip
```

#### 配置你的配置文件

```
# 进入虚拟目录
cd /Users/user/.pyenv/versions/3.11.12/bin
# 进入安装向导
./ida-pro-mcp --install
```

![](https://mmbiz.qpic.cn/mmbiz_png/fpMwbItribG4zkKQBMuibCzSAUcdb8PuuUdPBxNbAITHKmQZRCJ7MwuK5gKBgQibkyyxK9VaGVJ2e9H4XoS75C4crIhv2khNK8334kM3WEwY0o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fpMwbItribG7DdMoEdI33icDG6rWzHo6icCk43S2x4tgCosbq6gicrhcWMsrR94oE0zp62PFycbudvbIZqwQ0rXvZh3j0iaMBsJAOgh9icRx2EJtE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fpMwbItribG7fOJ1d54Umlz2uLVB6rtHibCXMr7BZb03wGITic1zgEG5ibIk6Uy8iaV4xUehwKohBYQZyeA5JWoZyicdKrOp7nGDHLKcPIWCVuH2Q/640?wx_fmt=png&from=appmsg)

会自动修改你相应工具的配置文件，后期也可以手动修改这些配置文件

```
Select global targets to install: Cursor, Claude Code, Codex, Zed
Installed Cursor MCP server (restart required)
  Config: /Users/user/.cursor/mcp.json
Installed Claude Code MCP server (restart required)
  Config: /Users/user/.claude.json
Installed Codex MCP server (restart required)
  Config: /Users/user/.codex/config.toml
Installed Zed MCP server (restart required)
  Config: /Users/user/Library/Application Support/Zed/settings.json
```

例：.codex/config.toml，如下他会添加俩个mcp\_server我把第一个默认关闭了

```
[mcp_servers.ida_pro_mcp]
command = "/Users/admin/.pyenv/versions/3.11.12/bin/python3"
args = ["/Users/admin/.pyenv/versions/3.11.12/lib/python3.11/site-packages/ida_pro_mcp/server.py"]
enabled = false
startup_timeout_sec = 1800.0

或

[mcp_servers.ida-pro-mcp]
url = "http://127.0.0.1:13337/mcp"
```

启动ida开启mcp，并在codex中尝试连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fpMwbItribG4kj4TTianQ8LSY4klpHs0SsyjB7bpUWupDBibY0qUoSrWXlIrcqFViarXqXfewknm01xoMgdXnZOGyHBAOpezElyLtuDvQX9rOo4/640?wx_fmt=png&from=appmsg)

至此，ida-pro-mcp的环境配置已完成。

**补充远程主机MCP方式**

```
# 在本机上运行，用ssh将远程端口映射到本地
ssh -L 13337:127.0.0.1:13337 user@远程机器IP
```

～/.codex/config.toml

```
[mcp_servers.ida-pro-mcp]
url = "http://127.0.0.1:13337/mcp"
```

在此记录几个有用的目录

```
# pyenv环境目录
~/.pyenv/versions/3.11.12/lib/python3.11/site-packages/ida_pro_mcp
# idapro插件目录
~/.idapro/plugins
```

### 2.22、jadx-ai-mcp

> 可自行选择最新的版本进行下载

* • jadx-ai-mcp-6.2.0.jar
* • jadx-mcp-server-v6.2.0.zip

#### jadx-ai-mcp.jar

导入方式安装（你也可以直接在设置中的插件管理进行安装）：jadx-mcp-server.jar包

![](https://mmbiz.qpic.cn/mmbiz_png/fpMwbItribG5v7p0qokqT9rO4fbFZHq5oaUEOp5FMsPnMgBNaibU5dNI329ibBeBh6XMGVLU3vYeFE7y9UxGaRjJlcJbvQWOXhVaTxvSRabYuQ/640?wx_fmt=png&from=appmsg)

#### jadx-mcp-server

> 我这里采用pyenv的虚拟环境，其他环境可自行选择

配置并安装依赖

```
# 进入你的插件解压目录
cd ~/tools/tool/04tools/0400-操作系统/0001-安卓/jadx/exp/jadx-mcp-server/
# 安装pip包
/Users/user/.pyenv/versions/3.11.12/bin/pip install -r requirements.txt
```

#### 配置你的配置文件

**本机MCP方式**
～/.codex/config.toml

```
[mcp_servers.jadx-ai-mcp]
command = "/Users/user/.pyenv/versions/3.11.12/bin/python3"
args = [
  "jadx_mcp_server.py",
]
cwd = "/Users/user/tools/tool/04tools/0400-操作系统/0001-安卓/jadx/exp/jadx-mcp-server"
enabled = true
```

**补充远程主机MCP方式**

```
# 在本机上运行，用ssh将远程端口映射到本地
ssh -L 8651:127.0.0.1:8651 user@远程机器IP
# 远程主机运行，如何根据自己的环境选择一个命令执行
uv run jadx_mcp_server.py --http --port 8651 --jadx-port 8650 # 使用uv管理的虚拟环境
python jadx_mcp_server.py --http --port 8651 --jadx-port 8650 # 使用python
```

～/.codex/config.toml

```
[mcp_servers.jadx-ai-mcp]
url = "http://127.0.0.1:8651/mcp"
```

如图所示，正常使用

![](https://mmbiz.qpic.cn/mmbiz_png/fpMwbItribG5yo0qbCqLElEAOvp2hSfxd6JPX6BLxDh3tAcDz3SpEHcQ8E36rjpBuvq4hNtynwWCov6dewUdLVdmAuLOwAWhrEk1icJdJKe78/640?wx_fmt=png&from=appmsg)

随后即可在codex或者其他agent中使用该mcp

### 2.2.3、chrome-devtools-mcp

#### codex添加chrome-devtools-mcp

> 直接按照官方配置进行添加：https://github.com/ChromeDevTools/chrome-devtools-mcp

```
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

只需要输入如上命令，即可将mcp添加至codex`～/.codex/config.toml`

```
[mcp_servers.chrome-devtools]
command = "npx"
args = ["chrome-devtools-mcp@latest"]
```

---

如有疑问请微信公众号留言，术业有专攻，闻道有先后，获取更多内容点击左下角`阅读原文`

![](https://mmbiz.qpic.cn/mmbiz_png/ic5ERMY2ib5RvnBeKhsMA56BVWW2ibdXTgJbLzVUsCqLqtLQVzRuFDZr7kVcpGg9GrSvfIHWaNLyQImiaUbHDI3TAg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ic5ERMY2ib5RsRBWoPyRGJOgxU6hdKHkJldxcl9hTLeoCVQEzGoKj86GkwNYIuQTCEQVVmtaZYrmpdPjBCQyicHicg/0?wx_fmt=png)

攻有道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ic5ERMY2ib5RsRBWoPyRGJOgxU6hdKHkJldxcl9hTLeoCVQEzGoKj86GkwNYIuQTCEQVVmtaZYrmpdPjBCQyicHicg/0?wx_fmt=png)

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