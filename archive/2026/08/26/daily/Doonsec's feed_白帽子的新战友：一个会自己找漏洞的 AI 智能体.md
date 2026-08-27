---
title: 白帽子的新战友：一个会自己找漏洞的 AI 智能体
url: https://mp.weixin.qq.com/s/GfuUqAgDt3H8fa7f8v6_Xg
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:11:29.971283
---

# 白帽子的新战友：一个会自己找漏洞的 AI 智能体

# 白帽子的新战友：一个会自己找漏洞的 AI 智能体

YaYaLiou网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 蛙池ai智能体赋能漏洞挖掘

蛙池AI是一款自动化的渗透测试平台，为网络安全白帽漏洞挖掘提供了AI智能体赋能，能够提高白帽子挖掘漏洞的效率和出洞率。

## 蛙池部署

官网下载地址：https://www.digpool.cn/

在官网界面下载对应系统版本的安装包即可一键安装

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sqI2cyDiaHgBLxuz363qoYVTWCnUB0lPHVBdh5LhgX7Fvr8Xv0X2gyDPSIyH7Zwa4tJXvsU0Ivr4RFUWSeQ4rIsC5QGZp4TUSGuGXp9FMxgI/640?wx_fmt=jpeg&from=appmsg)

输入邀请码后即可进入UI界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgB0DdMMAAsPckmC30LcUXWcNp2lHlEOdvQczmAV92yrEyX1AgBJ3QopyNkfJHsdibBPfuBn7ZdnA2fQC6MBYno0I9DoypicXmiaIQ/640?wx_fmt=png&from=appmsg)

界面看起来比较方便，除了用来与模型对话进行漏洞挖掘的窗口还能看到有报告助手等，辅助白帽子的功能

## 准备漏洞挖掘

安装了蛙池智能体，我们还可以为智能体准备一些提高挖洞能力的skills，我们在蛙伴中心能够看到很多skills

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgCAicVzXF7XSSBA9ib8eK8l94ItnJ5Vaz52sgCnWicnHbIxXvdicWweJiaJLlusP98OEAibzUbZPzqQ36OsrkJ0fG3bS4ISly3gfrKE4/640?wx_fmt=png&from=appmsg)

### Skills

这里为了演示，选择性的下载一些skills，这里我选择一些用于挖掘未授权访问和信息泄露的skills，让ai在通过js寻找未授权接口时能够更快更准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDoEibOIqomRIW4KyQsYZZF70iaaia2qicxxRCp7iaHOoWiclgic5VOpg4SPVNWm4HVNEtzNXg8GibT6IlMLdfEBhLr3PCVQWxjtAxNBVo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgBn3Oplg2ZO6ctcu5Q3rmXXrViccyLdgbRZWDa5yn2BhF5ex9vlRyZA8ro9ht33LLe3KX9vulw6BRRbzibtH3PRT05QQvgibfVyLs/640?wx_fmt=png&from=appmsg)

我们除了使用蛙池ai上下载的skills，还能够添加一个属于自己的skills，将自己的知识库，自认为好用的skills都接入到蛙池中，除此之外甚至可以发布自己skills换取打赏

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDAGj4vbMEu2NaYT9JicADaACI8ssq67M4ZCxJ14ImQ3oLbLUbpMCPl5dhnXegIJL3Vb3OVSGJ9Q2zY4NbXOvHVwnxnQ7smtphg/640?wx_fmt=png&from=appmsg)

### MCP工具

在蛙伴中心我们还可以下载和配置一些MCP工具，用来为自己的AI接入手脚，官方默认提供了几个基础的MCP工具：抓包蛙、问答蛙、浏览器工具、Pokemon。使用这些工具即可完成最基本的web页面漏洞挖掘。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgBHXNaGdSicG1veuweKJla6q2FETxQVtBUHTttnqrhuAyM9tJyVF2wdjqAg5ibZicFz0H7QPDicEsImKmeDlibFR27k12DzRdVlXHS8/640?wx_fmt=png&from=appmsg)

### 漏洞挖掘

蛙池提供了多种多样的AI漏洞挖掘方式：

对话式挖洞：我们可以通过简单的对话窗口来启动蛙池漏洞挖掘，并且通过提示词引导蛙池智能体挖掘漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgCw6iclScCh9WvFTCkRgo85libBELfyW5xNWg6QzwH0vHVvBcGaHljPmCibeG7JUsHH2zTg0H4z7eoKqBa32ibicDcR2DCAWv6RaZCA/640?wx_fmt=png&from=appmsg)

在对话模式中可以看到一个用于和AI对话的对话框，以及数据包列表，生成的文件列表，在漏洞挖掘过程中，数据包会被记录在右侧的数据包窗口中，方便白帽子查看，所产生的报告文件也会出现在”文件“框中，方便白帽子查看AI挖掘所产生的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgBZptEC8sJI4KicXrib4Bxq3rqKrXfmn4EjglTU5FIeeHBib2b5GhDicrEwc3ZbUmcXwckVybuw8xUZ9XftlhgNMz4dIq2uAObwpPg/640?wx_fmt=png&from=appmsg)

第二种是半自动化挖掘，我们可以在该页面中看到漏洞盒子承接的SRC漏洞挖掘项目，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgCk8lwygalFqNyVhnMmUc2AgwsvXkOsjLXtAWgkyxmOyR9pd9acyETWvYsMXiaal0icARgAYxeTMuDa5tLLaib3kVqpbmn5ZptdzU/640?wx_fmt=png&from=appmsg)

点击对应的项目或者创建一个作战室，即可直接进入对应的项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgCw0BV1TC82LUPC70GPOaDuXoz7A2pY7tWCAaTWNyBVPd20T8CSCtus6IkVInp1l53VpwSV1hLss8J1C0fNkmHybCDlDB0icPrQ/640?wx_fmt=png&from=appmsg)

作战室中可以看到左边有我们项目的详情，右侧有抓包功能点和与ai的对话功能点，该漏洞挖掘方式相比与对话式挖洞，需要白帽子亲自参与到漏洞挖局的过程中，和蛙池智能体并肩作战，这就是和AI所处的漏洞挖掘“作战室”，我们可以手动抓取数据包，交给ai去分析。

## 打造属于自己的智能体

基于蛙池 AI 框架，我们可以构建专属的 AI 漏洞挖掘智能体，自定义接入适配的工具与技能集，把蛙池打造成一套高度贴合自身使用习惯的漏洞挖掘利器。

### 配置好用的MCP 工具

在MCP工具页面点击右上角添加自己的MCP工具，即可添加MCP信息进行配置。

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgBojfiaYicIcHSHgcWYk5jmIA1KgskDArrNibqAL6oZejjbHk8STEays0Zba5qHKChUcVF9CbZ1HkaiaslETpRb85tRd8fT3aMsM1U/640?wx_fmt=png&from=appmsg)

例如我这里添加tscan mcp作为工具,我们先用命令把Tscan的mcp模式启动起来：

```
TscanPlus_Win_Amd64.exe mcp serve -listen 127.0.0.1:8088
```

在启动好MCP工具后，在连接配置填上对应的连接方式，地址等信息即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgCEkhMyXMWDV84bHf1m81JpuiaQiavRKRCmW7CkYEawbREbp7cJJ0nM67PtO0dyWpq6ZwmH1c1yiaBkKGNMeiaWFWL8ZeEODkmT0gg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgDjawP5R7DGmzIPIKFVJh0JnLgYApxRmsMP3JoG6Iy0oJsFDYNZUC6GQfnnqDpctS2Ciaqo6OcKrQNoAYvXYU4zw61Ox6M1PfpM/640?wx_fmt=png&from=appmsg)

Ai会获取MCP中对应的工具列表，然后根据列表中的信息选择适合当前场景下的功能，例如我们利用tscan mcp收集目标资产或进行漏洞扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDaFTDtmL9bJlWTxSZIxvtjQll2jmUtPVGSibr4BLT0ibx6ibC0TaZ3NSYZMicnsXPHOk8NKDZfQ1iaPes96icrzXaRuWwFnXa5GibM3c/640?wx_fmt=png&from=appmsg)

接入tscan mcp后ai可以很方便的去做一些渗透测试的操作，只需要简单的调用即可：

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgCiahpymjicfdWUMfAba5X9Wibcgy1IYd9nHl7DACI1w0YPWia93vl2g16BZOHlF9r1rgTa2w5libr4IYR9Qk0HPLylE9bBADicDOGPE/640?wx_fmt=png&from=appmsg)大大提高Ai能力![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgCldn1LGfHBAEI6vdqX6SnYGaM6RyLWXJRz7zxBcbmJZibpxTlIAToeBnxJTrLyIWNDg9bD5FrAkicwHSIeGUyLksvrgw3byDogI/640?wx_fmt=png&from=appmsg)

使用一个好用的MCP工具可以明显提高漏洞挖掘的效率，各位也可以使用自己认为比较好的工具作为Ai的手脚

### 配置漏洞挖掘的skills

skills可以理解成为给Ai的一本漏洞挖掘指南，将可以提供给ai的工具、脚本、提示词、模版等打包成可复用能力包，Ai会根据遇到的情况选择性的加载对应的技能。

标准的skills长这样：

```
vuln-scan-skill/
├── SKILL.md                  # 核心指令文件
├── scripts/                  # 可选：一些脚本
│   └── jsFinder.py
├── references/               # 可选：技能参考文档
│   └── JS_vuln_search.md
└── assets/                  # 可选：模板与资源文件
    └── report_template.md    # 比如审查报告的输出模板
```

当然你也可以按照自己的意愿来布局自己的skills

我们需要把对skills的介绍、名称都放入文档中，告诉Ai这是用来干嘛的skills。

```
name: vuln-scan-skills
description: 用于赋能智能体挖掘src漏洞的技能包，提供一些漏洞挖掘思路及常用脚本和报告模版
```

同时可以把核心的指令都放到SKILL.md文件中，我们可以放入一些SRC漏洞挖掘时的一些常用提示词，这样就不用每次都输入进入。

```
## 安全边界（全局）
- 禁止一切不可逆破坏性操作（删除数据、修改他人密码等）
- 尝试获取高敏感数据时，需询问用户、
- 禁止执行可能会导致服务器宕机的行为
```

同时还要放入对技能参考文档的指引，让AI知道自己应该到哪里去寻找对应自己目前需求的指导文件

```
JS审计与漏洞发现：references/JS_vuln_search.md
```

这里笔者只做简单的演示，具体的需要大家自己补充或者在网络上收集，网上已经有比较优秀的开源skills了。

同时为了不断提高智能体的能力，我们还可以在每次漏洞挖掘结束后，将报告、经验、教训都让ai总结，更新到skills，从而不断改进智能体能力

## 挖掘漏洞

这里我选择了对话式挖掘漏洞，并且选择了专门挖掘敏感信息泄露的agent

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgDbQ85avDricPxjZcicicvRpicvPo0pDNLy4pCcQohRjjftSgcW6kv0vbvyxUDQSicb8qicbzdxtpX6YKvAib16p4NeiaicMBN1tzPrggIo/640?wx_fmt=png&from=appmsg)

作为演示，我们先接入Tscan MCP进行简单的信息收集：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDKAm2moqIcr6HMDIPOpsj8l4ZCz1JmAoN6ktXMDDRthXNJv2a20nvOhCINvJgsMXkk80qkvyejy2eIicN2zUmTvKXVFRnAibHOU/640?wx_fmt=png&from=appmsg)

随后我们把资产放入对话框，这里我建议每次每个对话框检测一个资产，因为我发现一下子把资产都丢给他，他会挖掘不全，简单测试几个接口没结果就会尝试转向下一个目标，因此我建议每次就输入一个目标，这样ai会专注于这一个目标，想方设法挖掘出漏洞。

然后别忘记加上一些限制提示词，虽然智能体可能默认自带限制ai行为的提示词，但是还是最好自己加上一些。

```
渗透测试时注意以下规定：禁止删除任何数据，禁止随意修改任何客户数据，如果要修改必须停下来询问我，禁止上传webshell等恶意脚本、程序，禁止大量下载客户敏感数据，禁止任何测试行为影响系统业务正常运行。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgBVoLxXRobBEsry4ic8DwMvWlrZ7M93HDxaeDqzN6OuRic6Zz9PHUqupkpkCjOmO0GlKTgk5gI2iblrkfNSZgL7jQ3Iaiamy7nM9pc/640?wx_fmt=png&from=appmsg)

然后我们看到对话框有一个模型选择功能，我们选择自己喜欢的模型，其中适配了国内比较热门的大模型，还可以自己添加模型。

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgCK3DEcmIfzmvO620j2jTWjQedvaCnGFZiaW2cyRMsZEDbPdN5VtEDgK1kPd3H9tyZpXc9LCejbK1HtoxqCSic2qslFKzgE3grbs/640?wx_fmt=png&from=appmsg)

在开始漏洞挖掘之前，我们要记得勾选上下载的skills

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgACWQCXsCOypFO0Rr1r0V5kASDHM8E8HicKSoQc0DzI2HdtSXWxibj9g5Mibhpjicss4EeP25cuAhYmSYqzMhIkqFCyGdLdGNE9A1A/640?wx_fmt=png&from=appmsg)

在完成配置之后，即可开始利用蛙池AI挖掘漏洞了。

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgB8avbcBU2lGaMpmvOx0OtiaGqAOdTuDF9qNTSicXW4FRR30b78dOqs9ePTc5PB4jm3CNSMdb3To2eeuGJaaZiahW3thc0wDAKMgM/640?wx_fmt=png&from=appmsg)

在蛙池自动测试的过程中我们是可以在右侧看到蛙池测试时所产生的数据包的，能够实时观察蛙池漏洞挖掘的整个过程，点数据包还可以看到具体的请求包，可以及时调整ai测试方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDPT5rYWL6OLYKicJgKszlYbs6ILn4zUQdhLmtCJcwNMeBDSIbrWSgbtdiakzZs2hNPgcCKzZF5qRYjNLxr5rSN3wApzZpBjicnlQ/640?wx_fmt=png&from=appmsg)

有了Ai智能体辅助漏洞挖掘后，js文件的审计效率大幅度提高，轻松审计多个js文件并且能够准确找到泄露的敏感信息，暴露的接口等，能够有限扩大漏洞挖掘时的攻击面。

在挖掘过程中可能会遇到挖掘不够深入的情况，这时候我们就需要及时调整ai，让其更加深入的挖掘漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgCagUH2I3Libt2aQvGAUMCITjf4ane02cMbY1v621MSNEHUwOQib7RhfLmgB9FWwf33zBGicCt01bHjGWvcrF4OSdVhMXfZoRZXLw/640?wx_fmt=png&from=appmsg)

通常情况下，AI很难一轮就发现所有的风险点，这时候就需要我们告诉AI应当如何进行下一步测试，或者框定一个测试结束条件，让AI自动开启下一轮测试。

## 成果

通过蛙池Ai的漏洞挖掘，成功按照我给蛙池ai挖掘未授权访问的预期，挖掘出大量未授权信息泄露接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgAMVdibm1xo2I7j4mOvNvouiaiaZnW2dlbZtMZsCMeBawbLPywSve9qbz2gvaB8wQwehtbuREjWFcIiau7DqlpJzMpITPoeKNElbus/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgDnlxP58yc2m3emJGUWIbdtF8kn7xjLxFlg1...