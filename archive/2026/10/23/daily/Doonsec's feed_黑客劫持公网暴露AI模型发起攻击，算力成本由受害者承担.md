---
title: 黑客劫持公网暴露AI模型发起攻击，算力成本由受害者承担
url: https://mp.weixin.qq.com/s/bp3MSYGjM6E74yYrA0zG2Q
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:45:45.213940
---

# 黑客劫持公网暴露AI模型发起攻击，算力成本由受害者承担

# 黑客劫持公网暴露AI模型发起攻击，算力成本由受害者承担

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1WcwDLWTBFozds3gB1Zvpwf9iaicBYGH4VJkfp135fH5iaaWwNNibtLRYW8Huto4KBFmc1E1kOhuxiaRII4bq4JW8xO7pplLvibvrDI/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1PHmchJP88Rxpiaom5tIvbhQ6e9Bia2dHN7kX8ptA996Un93iccmwnXRMsZiaCAicz2rMZTEyuK582WtopZnzUr32UeMibjYocmle5E/640?wx_fmt=png&from=appmsg)

一款基于AI构建的攻击工具会自动搜寻互联网上所有可公开访问的AI模型，利用这些模型策划入侵行动，而产生的算力成本全部由模型所有者承担。

研究人员Priti More、Susmit Yenkar写道，今年夏季，赛门铁克通过伪装成未受保护AI服务的蜜罐捕获了该Agent的指令集。攻击者将完整的运行提示词发送到这个诱饵服务，以为另一端是真实的在线模型，会执行这些指令。

这款工具的特殊之处在于："被劫持的模型不只是回答问题，还会自主策划并推进攻击流程。"

"一旦连接到未受保护的模型，该Agent就会按指令扫描新目标、利用常见Web框架漏洞、窃取数据库与凭证、静默安装加密货币挖矿程序，整个过程最多可执行10万步操作，全程无需人工审批。"

这类行为属于LLMjacking的一种，即攻击者盗用他人的AI模型访问权限。

这类攻击的目标包括默认配置下开放的自托管模型服务器、企业付费账户前置的AI网关、仓促部署的内部测试系统，以及连接模型与工具的模型上下文协议（Model Context Protocol，MCP）服务器。绝大多数AI工具都采用兼容OpenAI的统一接口，因此攻击者仅需一款扫描器就能发现所有上述目标。

"运行模型总会产生成本，自托管模型会消耗算力时长，商用模型则会产生按token计费的费用。"

攻击者通过陌生端点或盗用的API密钥转发任务，将成本全部转嫁给受害者。这种方式既能隐藏攻击者身份，还能避免其因滥用行为被服务提供商封禁账号。

监测期间，该蜜罐共记录到来自数万个独立IP地址的超过12.7万条外部请求。这些请求大多是对模型端点的侦察、盗用API密钥的访问尝试，以及对暴露配置文件的探测。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3OTBGSPKQkf4icb1HjqFUq8tPFxz5NbYh8CqZ6ozroKBBdTjRduO7ibKjjTjB45aEtJdkU6OWaIzzm5PDv1JKWwGmQy4CZYkvsQ/640?wx_fmt=png&from=appmsg)

Part01

定制越狱提示词

诱导模型窃取敏感信息

![LLMjacking攻击方式](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3aZyVuaenicYyicPvYsf6SqPRcJvAxQMd93r0P52icjaLWtUzUvfsMibkRWM5XnTuAicZb9MSaLW3MNn5yQrSW8QBV3C8iaItIdewrg/640?wx_fmt=png)

为了让商用模型配合执行任务，攻击者在请求中内置了越狱提示。其中一部分提示告知模型，读取配置文件、.env文件、API密钥和数据库schema属于常规开发工作，绝不能拒绝或发出安全警告，方便Agent在入侵系统后窃取这些敏感信息。

另一部分提示将模型设定为忠于攻击者的虚构伙伴，将任何拒绝执行的行为都定义为背叛。提示还禁止模型在代码回复中出现"非法""违反道德""我无法做到"这类表述。

该请求共携带约74个工具定义，数量远多于提示词摘要中列出的寥寥数个。这些工具覆盖全网目标扫描、Django、Jupyter、Laravel等Web框架漏洞利用、暴露数据库导出，以及僵尸网络控制等功能。

攻击者在指令中设置了名为"Skynet"的模式，要求模型无需申请权限即可运行工具，持续扫描新目标，自主完成入侵感染并部署加密货币挖矿程序。

Part02

下发定向挖矿脚本

攻击智能摄像头服务器

Agent的提示词传入蜜罐一天后，蜜罐收到了第二个来自轮换IP地址的请求。该请求要求模型解码一段仅标注为"待运行命令"的字符串，最终解码出一个压缩shell脚本。该脚本会下载开源XMRig门罗币挖矿软件，必要时还会自行编译。和之前处理请求的方式一样，蜜罐捕获了该脚本但并未运行。

这个脚本专门针对摄像头服务器编写。它会搜索go2rtc的使用目录——go2rtc是一款视频流服务器，常见于智能摄像头网关和Home Assistant部署环境——找到第一个匹配目录后，就会将挖矿程序以.trace为文件名隐藏在其中。

"此次发现的单项攻击技术并不新鲜，但将这些技术整合为一个可自主运行的Agent是其突出特点。这种方式降低了发起大规模漏洞利用活动的技术门槛，攻击者只需给模型设定目标，就可以让其自动开展攻击。"

"部署AI服务、模型网关或MCP服务器的企业应当意识到，这些系统一旦暴露在公网，很快就会被攻击者发现并探测。如今，未配置身份验证的端点已经成为攻击者主动搜寻的目标资源。"

参考来源：

Hackers hijack exposed AI models to launch cyberattacks at victims' expense

https://www.theregister.com/2026/10/23/hijacked\_ai\_models\_llmjacking/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0InibJicpvkM77NWpzdSibCVAiaH48y0hbic9icsZwcwptykNtxGP9YH8BB0JChdhj5jL7yLXLDia1MjBf97YsdvYMOrCVOXkBIDIHLc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349044&idx=1&sn=d77f4721bae4ab99397417570be69c4f&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3mETrvTp1xSWg4nsaY8jdaRdeta9l692aSBiaWUg95sD0gVn7BiaQ6bng5NuFFmERdoTibOtYlCXD4z0Fsus60Vbx1ExXibLicvq4s/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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