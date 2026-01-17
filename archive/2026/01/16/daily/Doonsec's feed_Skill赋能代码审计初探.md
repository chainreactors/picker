---
title: Skill赋能代码审计初探
url: https://mp.weixin.qq.com/s/auJiEOJyD4iKFvW0YdMOSg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:25:20.516086
---

# Skill赋能代码审计初探

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DvxV6yFV5brGMU5cia15YhajsY46r6iciaIJTC1l9eQHaBdib2Zn9icsBmpmgeBXn0ATVn24JWDekPyiad9c28voiaHDw/0?wx_fmt=jpeg)

# Skill赋能代码审计初探

原创

俗说君
俗说君

鹿鸣安全团队

![]()

在小说阅读器中沉浸阅读

# 前言

最近在学Skill，就想尝试找个场景将其进行应用。也算是填一下之前Codeql+LLM应用的坑了。

**总体的思路**：利用CodeQL先实现静态代码扫描输出扫描的json数据，而后基于Skill文档的步骤送入到Claude中加载运行进行验证及修复方案和参考攻击payload生成。

# 前置配置

## CodeQL

CodeQL实现静态代码分析效率还是可以的，但是它对查询语法的编写要求很高，导致难度就比较大，且对于编译性语言和非编译性语言的项目审计难度也不一样。

对于java，C，C# 等需要指定构建方式

对于python等项目则可以直接进行扫描审计

具体的搭建流程可以看《CodeQL代码审计初探》一文中的过程，主要就是保证执行codeql指令的时候可以正常运行即可，并且针对python、java等语言包的查询扩展库也要指定好。

## Claude Skill

### 简单介绍

Skill执行需先在本地搭建Claude，我是利用的中转站（https://api.code-relay.com/register?aff=3V9T），依据其教程完成安装即可。出现如下界面就说明安装成功了

![](https://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5brGMU5cia15YhajsY46r6iciaIcDF3ZkUiafPib8mwrUFtmQiafvrOEGibulS5ribiaDUOppKPqanJF2PAIdTw/640?wx_fmt=png&from=appmsg)

Skill本质上来说是一种“提示词扩展”，而非具体的“代码执行”，与传统的提示词相比，只是加载方式不同。

Agent Skills 是一种轻量级、开放的格式，用于通过专业知识和工作流扩展AI智能体的能力。

Skill 的核心是一份 Markdown 文件（SKILL.md）。当 Skill 被调用时，系统并不会去“运行”这个 Skill，而是读取这个文件，将其中的大量指令、工作流和知识“展开”并“注入”到当前的对话历史中。

#### Skill运作流程

整个过程可以看作是一个 “动态加载特定领域大脑” 的过程：

1. 用户请求： 例如：用户输入“帮我分析这个 PDF。”
2. LLM 决策： 看到 Skill 工具里有 pdf 技能的描述，决定调用 command: "pdf"。
3. 系统介入：

* 读取 pdf/SKILL.md。
* 生成一条给用户的“正在加载...”消息。
* 生成一条给 AI 的“你现在是 PDF 专家，你的工作流是 1,2,3...”的隐藏消息。
* 修改当前 Session 的权限，允许使用 Bash 中的 PDF 工具。

4. LLM 执行： 带着新注入的记忆（Prompt）和新获得的权限（Tools），Claude 仿佛变了一个人（Agent），开始执行具体的 Bash 命令来处理 PDF。

**小结：**Claude Agent Skills 的原理是通过“元工具”动态地将“静态的知识文件（Markdown）”转化为“动态的对话上下文（Prompt）”。

它并没有创造新的“程序执行”方式，而是极其聪明地利用了 LLM In-Context Learning（上下文学习） 的能力，实现了功能的无限扩展和按需加载。

#### SKill编写格式

一个 Skill = 任务说明书 + 工具代码 + 专业知识 + 素材资源。

本质上就是一种代码和资源的组织方式。

skill.md包含以下字段：

```
name:必填(是)  【最多64个字符。仅允许小写字母、数字和连字符。不能以连字符开头或结尾。】
description:必填(是)  【最多1024个字符。非空。描述该 Skill 的功能及适用场景。】
license:必填(否)  【许可证名称或引用的捆绑许可证文件。】
compatibility:必填(否)  【最多500个字符。说明环境要求（目标产品、系统包、网络访问权限等）。】
metadata:必填(否)  【用于附加元数据的任意键值映射。】
allowed-tools:必填(否)  【Skill 可使用的预批准工具列表（空格分隔）。（实验性功能）】
```

# 落地实现

这里只是先做了一个简单的demo，主要就是为了能跑通skill的运行流程，因此整体项目的结构不是很大（仅仅以python为例，因为不用编译，可以直接检测）。 目录结构如下：

```
codeql-sast/
├── SKILL.md          # 主指令文件（必须有）
├── queries/          # 一些查询相关的文件
└── scripts/
    └── codeql_scan.py  # 工具脚本
```

## 效果展示

直接跟claude对话，帮我审计一下这个python项目，项目路径是“C:\Users\xxxx\codeql\_vlun.py”

![](https://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5brGMU5cia15YhajsY46r6iciaIGic19djVXQoxhcrZM9BsJXdFzlSiamZhdtDXiaLcG14rqE21EdQXmeTxw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5brGMU5cia15YhajsY46r6iciaIrOP522mHF44Hlia4q6ic2MfemQsQ8ebIYibeVoz7rQkm63SwAC7BvYjoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5brGMU5cia15YhajsY46r6iciaIPbrufksdLUBwSiau5REqgkPvgPUqgekcMMmJEyQAtQoFIjDC7FJRGVw/640?wx_fmt=png&from=appmsg)

依据给出的payload参考进行漏洞利用验证

![](https://mmbiz.qpic.cn/mmbiz_jpg/DvxV6yFV5brGMU5cia15YhajsY46r6iciaIByZnNZL6k0NJoVXD7F1O0YP7920CRtYYT0VvAVl4SGRQd8SfIdHWag/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5bqJnK3nmY4cGVb4XPibKDwHtw0pd0mKuiaKqHgibIg5GIwpGbv7Da46jBVgM3ZHEyvp8mcPeU5DMLK2Q/0?wx_fmt=png)

鹿鸣安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DvxV6yFV5bqJnK3nmY4cGVb4XPibKDwHtw0pd0mKuiaKqHgibIg5GIwpGbv7Da46jBVgM3ZHEyvp8mcPeU5DMLK2Q/0?wx_fmt=png)

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