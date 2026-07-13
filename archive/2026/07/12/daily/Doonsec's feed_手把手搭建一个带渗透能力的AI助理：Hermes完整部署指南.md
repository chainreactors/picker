---
title: 手把手搭建一个带渗透能力的AI助理：Hermes完整部署指南
url: https://mp.weixin.qq.com/s/ffJ7HXQctFTrnq7PB3676A
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:28:37.687803
---

# 手把手搭建一个带渗透能力的AI助理：Hermes完整部署指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GEVYW8ofHic382kGiaXGDYQGeNkgDsEQVL0UT0t5icLVsIADW3FMn6lvcE6EVibs3asVkRZVdicicAEAmVlAII2ibcUjeKEymuT4qZ1KrqJEicS7l9U/0?wx_fmt=jpeg)

# 手把手搭建一个带渗透能力的AI助理：Hermes完整部署指南

原创

老鑫安全
老鑫安全

老鑫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 为什么要自己搭一个？

市面上的AI助手不少，但真正能让你自由控制、随时调用、还能干点“脏活累活”的，其实没几个。

我之前折腾Hermes有一阵子了。这玩意儿说白了就是一个Agent框架，但它厉害的地方在于——你给它配上合适的模型和工具，它就能自己规划任务、调用工具、一步步把事情干完。

我主模型用deepseek-v4-flash，图的就是便宜、快。但DeepSeek本身不支持看图、听语音，所以得另外接模型来补这些能力。

这套方案搭完之后，效果大概是这么个情况：

* 云服务器跑着，不用关机
* 主力推理靠deepseek-v4-flash
* Telegram上发消息就能指挥它干活
* 图片识别和语音用别的模型顶上
* 顺带还能做点逆向分析和安全测试的活儿

不废话，直接开整。

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic3biaB2QVWcGYic3Pib1NicT2icr2icVwT0Iszx8c6gWvSWY9TGvzflCibRnRbKWherFIzwF3vz1Dkf18VHHadnpiaN1y3aVBOgq0xLktY/640?wx_fmt=png&from=appmsg)

---

## 第一步：搞一台机器

云服务器随便哪家都行，Hermes本身不挑配置，真正花钱的是API调用，不是服务器租金。

我个人用的是AWS香港节点，系统Debian。

硬件要求真的不高：

| 项目 | 最低 | 建议 |
| --- | --- | --- |
| CPU | 1核 | 2核 |
| 内存 | 1GB | 2-4GB |
| 硬盘 | 10GB | 20GB+ |
| 系统 | Debian 11+ | Debian 12 |

网络这块儿，能正常访问GitHub就行。如果用国内的大模型（像智谱、通义），连代理都省了。

---

## 第二步：登进服务器

服务商会给IP、用户名、密码（或者密钥）。SSH工具我用Termius，界面干净，多台机器切换也顺手。

连接过程没啥好说的：

* 打开Termius，点New Host
* 填IP、用户名、端口（默认22）
* 密码登录直接填密码；密钥登录的话，先在Keychain里导入私钥，然后选SSH Key

连上之后，第一件事是切root更新环境：

```
sudosu
apt update && apt upgrade -y
```

然后装一堆基础工具，后面都会用到：

```
apt install -ycurlwgetgitvim nano unzip tar tmux htop build-essential ca-certificates sudo
```

装完之后建议切回普通用户操作，别一直挂着root：

```
su 你的用户名
```

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic187KZic9u1BvD4DAzMqmlia7DrC0K6sGMIKRvn1cib2WiaiasiarXg3EOZKRrxRAvvAdvXicBQsg93E88BCWaPKUbuVEiacvcbqBIWCTQ/640?wx_fmt=png&from=appmsg)

## 第三步：装Hermes本体

官方给了一键脚本，省事儿：

```
curl-fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

跑完之后，如果系统不认`hermes`命令，刷新一下环境变量：

```
source ~/.bashrc
```

然后进配置向导：

```
hermes setup
```

界面里会有三个选项：

* Quick Setup（快速，但自由度低）
* Full setup（完整，推荐）
* Blank State（从头自己配）

选**Full setup**，一步步走。

---

## 第四步：配模型和API

配置过程中最核心的一步就是选模型。DeepSeek在这里是性价比之王，我选的是deepseek-v4-flash。

具体步骤：

1. 在Provider列表里找到DeepSeek（或者OpenCode这类聚合平台）
2. 填上你的API Key（去DeepSeek官网申请，记得充值）
3. Base URL用默认的就行，直接回车
4. 模型选deepseek-v4-flash
5. Backend选local

其他选项按需勾选，不确定的就先跳过。

配完之后，跑几个命令验证一下：

```
hermes --help
hermes doctor
```

能正常回显就说明装好了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic0ibeX14l5olkP9oTl954snOPypA6aRTxDOW7K2oMyJ2XtODbtKgicYdCL1pXD16Hpu8CTwia7zA6rtY58lECKfU8F4pNnopbKg8A/640?wx_fmt=png&from=appmsg)

---

## 第五步：接上Telegram，手机也能指挥它

有了Telegram Bot，就不用每次都SSH进服务器敲命令了，手机上发消息就行。

配置命令：

```
hermes gateway setup
```

选Telegram之后，终端会跳出一个链接。

**创建Bot的流程：**

1. 在Telegram里搜`@BotFather`
2. 发`/newbot`，按提示起名字
3. 拿到BotFather给的HTTP API Token
4. 把Token粘回终端

**获取你的用户ID：**

搜`@userinfobot`，发任意消息，它会返回你的数字ID。把这个ID也填回终端。

完成后启动Gateway：

```
hermes restart
```

去Telegram给你的Bot发条消息，能回复就说明通了。

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic2n32iblDvPkJbOxr4kFibzofcM13FaNkEX7hxpQVkesnCu2ic7LMdxybF7I6WOB6QznQ1SLE7jegf2rICQmK7tdhSacBRGQjL2Zg/640?wx_fmt=png&from=appmsg)

---

## 第六步：补上图像和语音能力

deepseek-v4-flash虽然好，但不支持多模态，所以得另找模型来干视觉和语音的活儿。

**图像识别和音频解析**

指定一个支持多模态的辅助模型来处理这类请求。比如用opencode里的mimo-v2.5-flash，专门负责看图、听音频。

配置方式是在Hermes的设置里指定`vision_model`和`auxiliary_model`参数。

**语音输出（TTS）**

免费方案可以用Edge TTS或者小米的接口，配置好provider和voice参数就行。具体细节我之前的推文里写过，这里不展开。

配完之后，Hermes遇到图片或语音请求，会自动切换到对应的辅助模型处理，对用户来说是无感的。

---

## 第七步：让Hermes学会逆向

这个环节其实不复杂，核心就两步：

1. 把包含逆向技能配置的仓库丢给Hermes去拉
2. 让它完整阅读项目里的说明文档（比如readme\_ai.md），然后按规范执行

Hermes能做的逆向相关事情包括：

* 辅助反编译分析，比如解JAR包看代码结构
* 配合Frida做动态调试，检测反调试和Hook逻辑
* 接入BurpSuite辅助分析HTTP流量

说白了，Hermes在这里充当一个懂逆向的助手角色，能理解上下文、记指令、执行多步操作。比起你自己翻文档翻半天，它要快得多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic2InubLh1BhaicjZiawzKS5iaCEuDF63sicC5M1QrjziaA7GYvTHndhXHep0HTdX9Licj4B1zgtIrHzUicu4yKM7ibcbCw0JukqfuzKYYE/640?wx_fmt=png&from=appmsg)

---

## 第八步：Agent钱包——让机器自己花钱

这块算是进阶玩法了。给Agent配上钱包，它就能自己调用付费服务，不用你手动介入。

安装Agent Passport：

```
curl -fsSL https://agentpassport.ai/install.sh | bash
```

配置过程很简单，跟着提示走就行。装完之后，Agent可以支付小额费用调用各种外部API：

| 服务 | 单价 | 用途 |
| --- | --- | --- |
| Firecrawl | $0.002/次 | 网页抓取 |
| AgentMail | $0.01/次 | 发邮件 |
| Exa | $0.005/次 | AI搜索 |
| Cloud Vision | 按量 | 图片识别 |

用USDC结算，到账速度很快。未来Agent自己调用服务完成任务会越来越普遍，提前折腾一下不吃亏。

---

## 第九步：实际用一下

日常遇到可疑链接（特别是链上交易那种钓鱼网站），直接发给Telegram上的Hermes，让它帮你分析。

它会自己去打开页面、抓取内容、检查域名信誉，然后给你一个判断结论。对于防诈骗来说，这玩意儿还挺实用的。

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic0BcibAfU9EhVk7LQ7wDgjKKrgcy5oryicHrC7riaR0uCmzc4p9wJSN4ibUq5ibXlqy78Ljnv7y89CV2XdZWaNONibSl39K6n9DmqAQA/640?wx_fmt=png&from=appmsg)

---

## 总结一下

从零到一搭完这套系统，你手里就有一个：

* 云上7×24小时在线的AI助理
* Telegram随时遥控
* deepseek-v4-flash负责主力推理，便宜又快
* 辅助模型补齐了看图和听语音的能力
* 还带逆向分析和安全检测的工作流

这已经是个挺完整的“全能Hermes”了。至于Agent钱包、自主支付、自动化渗透这些更骚的操作，后面可以慢慢折腾，能玩的东西还多得很。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

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