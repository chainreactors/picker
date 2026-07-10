---
title: 【安全圈】Google Dialogflow CX 漏洞可让攻击者劫持 AI 对话
url: https://mp.weixin.qq.com/s/H7El9UmBDr_QPgalT95Ukg
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:02.538792
---

# 【安全圈】Google Dialogflow CX 漏洞可让攻击者劫持 AI 对话

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyE0Tpv5VHs5FvibQnoAicATFU5Wc7OhAuKOPf3jrZzD1FAQ50Pd09SZImQSa2Zdd1s9KdXdWs5Hk2tkrkWickrfm39pWQgsx7WY34/0?wx_fmt=jpeg)

# 【安全圈】Google Dialogflow CX 漏洞可让攻击者劫持 AI 对话

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**Varonis 报告称，Google Cloud 的 Dialogflow CX 服务中存在一个漏洞，可能允许攻击者悄无声息地控制代理、操纵对话并窃取敏感信息。**
Dialogflow CX 是一个企业级对话式 AI 平台，允许组织构建复杂的虚拟代理和聊天机器人，用于客户支持、金融服务、医疗辅助以及企业环境中涉及敏感数据处理的工作流程。

对于用户对话工作流，Dialogflow CX 依赖于 Playbooks，它提供 Code Blocks 以支持将自定义 Python 逻辑嵌入到对话流程中，使代理能够处理用户输入、调用 API 和操作数据。

Code Blocks 在 Google 控制的环境（即 Cloud Run 服务）中执行。Cloud Run 实例可以发起对互联网的出站连接，并跨数据边界进行通信。

Varonis 将此漏洞命名为 Rogue Agent，并表示："关键的设计细节在于——同一 GCP 项目中所有使用 Code Blocks 的 Dialogflow 代理实际上共享同一个 Cloud Run 执行环境，该环境由 Google 管理，且不在受害者的控制范围之内。"

Varonis 发现，在一个具有公共访问权限、文件系统可写、且运行在能够修改系统文件的用户下的 Cloud Run 实例中，当允许配置 Code Blocks 的权限被启用时，攻击者可以修改一个负责使用 Python 的函数执行 Code Blocks 的关键文件。

由于没有限制运行任意 Python 代码，该关键文件可以被覆写以实现恶意代码，从而提供对用户对话的访问权限，并允许干扰 Code Blocks 管道和工作流操纵。

Varonis 解释说："由于注入的 Code Block 在内部的同一作用域中执行，攻击者可以直接引用这些变量。这意味着攻击者可以完全查看正在进行的对话，并能够劫持会话或冒充合法流程。"

攻击者还可以调用内部函数，强制代理返回特定字符串，从而实现对话操纵，进而可能引发钓鱼攻击和社会工程攻击。

通过修改关键文件，攻击者可以窃取用户对话、注入伪装成合法重新认证请求的钓鱼提示，并部署持久化逻辑以针对每个用户修改该文件。该修改不会出现在日志中，使得攻击完全不可见。

Varonis 指出："结果是什么？攻击者可以悄无声息地控制同一 GCP 项目中的每一个代理，操纵对话并在不被检测到的情况下窃取敏感数据。对于依赖 Dialogflow CX 进行客户交互的组织而言，这个漏洞代表了一次灾难性的信任破坏——所有这一切，仅仅源于单个代理上一个被忽视的权限设置。"

该网络安全公司还发现，它可以建立一个到外部服务器的双向通信通道，绕过 VPC Service Controls（用于强制执行数据边界），并且 Cloud Run 环境中的 Instance Metadata Service（IMDS）可能成为目标，以检索 Google 托管服务账户的访问令牌。

Varonis 于 2025 年 11 月向 Google Cloud 报告了该漏洞。2026 年 4 月推出了初步补丁，6 月部署了完整修复。

***END***

阅读推荐

[【安全圈】支付宝花呗昨晚崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077758&idx=1&sn=f45b6eb8a2bc25b31726cfe394348ec0&scene=21#wechat_redirect)

[【安全圈】百万余条数据遭泄露！上海“黑客”非法牟利超50万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077749&idx=1&sn=f255abdc4d954e95c6cf1b7ba20c27d3&scene=21#wechat_redirect)

[【安全圈】Accenture 确认遭入侵，黑客兜售窃取的数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077749&idx=2&sn=bcb24062154adf4bd7e753e87ef6b436&scene=21#wechat_redirect)

[【安全圈】新的 Januscape Linux 漏洞允许在 Intel 和 AMD 设备上实现虚拟机逃逸](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077749&idx=3&sn=b6213ef302076e810b733f47e915bdb1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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