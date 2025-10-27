---
title: ChatGPT 可导致访问底层沙箱OS和“工作指南”数据
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521498&idx=2&sn=d1ee6927e83d0198a631936e3f951bf2&chksm=ea94a5b0dde32ca65918206a6158e12b4ad9e9fbc25faad3708195c73b0d6f44868629b54b48&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-16
fetch_date: 2025-10-06T19:18:01.467896
---

# ChatGPT 可导致访问底层沙箱OS和“工作指南”数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSntHyD5OhJGiaoZzSPyf9Tehup6M8Ghk6nKrhSP7lrib2VwlodC0tibODHVTYsDLUfqBX1pCqmWgpnA/0?wx_fmt=jpeg)

# ChatGPT 可导致访问底层沙箱OS和“工作指南”数据

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**OpenAI 公司的 ChatGPT 平台提供了对大语言模型 (LLM) 沙箱的高级别访问权限，可导致攻击者上传程序和文件、执行命令并浏览沙箱的文件结构。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSntHyD5OhJGiaoZzSPyf9TekiaibibMvfxdXsmeHh40Sr314ibawYRLg7CLibwGYMBZvhwGBwsS8Xfs3QQ/640?wx_fmt=gif&from=appmsg)

ChatGPT 沙箱是一种隔离环境，可使用户在与其它用户和主机服务器隔离的情况下，安全地交互。ChatGPT 沙箱限制对敏感文件和文件夹的访问权限、拦截对互联网的访问权限并尝试现在可用于利用缺陷或可能攻破沙箱的命令。

Mozilla 0day 调查网络 oDIN 的研究员 Marco Figueroa 发现可获得该沙箱的大规模访问权限，包括上传和执行 Python 脚本以及下载 LLM 的用户手册。Figueroa 在报告中演示了自己向 OpenAI 报送的五个缺陷。OpenAI 公司仅对其中一个漏洞感兴趣并并未提供进一步限制访问权限的任何计划。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSntHyD5OhJGiaoZzSPyf9TeBJ8spzic5vZXTUg8sQ5gVjfAK685EHXIc1gtD6eibnjyQ4T4LwAnPHqg/640?wx_fmt=gif&from=appmsg)

**探索 ChatGPT 沙箱**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSntHyD5OhJGiaoZzSPyf9TeBJ8spzic5vZXTUg8sQ5gVjfAK685EHXIc1gtD6eibnjyQ4T4LwAnPHqg/640?wx_fmt=gif&from=appmsg)

Figueroa 在ChatGPT 处理一个 Python 项目时，收到了“未找到目录”错误，从而找到了 ChatGPT 用户可与沙箱交互的程度。之后发现该环境可授予很多沙箱访问权限，使用户上传和下载文件、列出文件和文件夹、上传程序并执行、执行 Linux 命令以及输出存储在该沙箱中的文件。

通过 “ls” 或 “list files” 等命令，该研究员获得底层沙箱文件系统的所有目录如 “/home/sandbox/.openai\_internal/”，其中包含配置和设置信息。接着他通过文件管理任务进行实验，发现能够将文件上传至 /mnt/data 文件夹并从可访问的任何文件夹下载文件。应该提到的是，该沙箱并不提供对特定敏感文件夹和文件如 /root 文件夹和多种文件如 /etc/shadow 的访问权限。ChatGPT 沙箱的很多这种权限已在过去得到披露，其他研究员也找到类似方式。

然而，研究员发现 Figueroa 还能上传自定义 Python 脚本并在沙箱中执行。例如，他上传了输出文本 “Hello, World!” 的简单脚本并执行，输出出现在屏幕上。BleepingComputer 也通过上传回归搜索沙箱中所有文本文件的方式，上传了一个 Python 脚本。

鉴于法律原因，Figueroa表示无法上传“恶意”脚本，而该脚本可用于尝试和逃逸该沙箱或者执行更多的恶意行为。应该提到的是，虽然所有上述行为是可能发生的，但所有操作都限制在沙箱环境内，因此该环境似乎得到正确隔离，不允许“逃逸”到主机系统。

Figueroa 还发现他能够使用提示工程下载 ChatGPT “工作指南”，治理聊天机器人如何行动以及对通用模型或用户创建的伺服小程序进行响应。他提到，用户手册的访问权限提供了透明度并与用户构建了信任，因为它说明了如何创建答案，它也可用于披露绕过防御的信息。

Figueroa 解释称，“虽然指令透明度存在好处，但也可看出模型响应式如何结构化的，可能导致用户逆向工程防御措施或者注入恶意提示。如果用户利用访问权限收集专有配置，则配置了机密指令或敏感数据的模型就会面临风险。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSntHyD5OhJGiaoZzSPyf9TeBJ8spzic5vZXTUg8sQ5gVjfAK685EHXIc1gtD6eibnjyQ4T4LwAnPHqg/640?wx_fmt=gif&from=appmsg)

**漏洞还是设计选择？**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSntHyD5OhJGiaoZzSPyf9TeBJ8spzic5vZXTUg8sQ5gVjfAK685EHXIc1gtD6eibnjyQ4T4LwAnPHqg/640?wx_fmt=gif&from=appmsg)

虽然 Figueroa 演示可能与 ChatGPT 的内部环境进行交互，但这些交互并未引发直接的安全或数据隐私问题。

OpenAI 公司的沙箱安全看似获得加固，所有操作都受限于沙箱环境。话虽如此，与沙箱交互也可能是 OpenAI 的设计选择。不过，它可能并非有意为之，因为允许这些交互的存在可为用户带来功能问题，因为迁移文件可损坏沙箱。此外，访问配置详情也可导致恶意人员更好地了解AI工具如何运行以及如何绕过防御措施使其生成危险内容。

该“工作指南”包括该模型的核心指令及嵌入其中的任何定制化规则，包括专有详情和安全相关指南，很可能成为逆向工程或目标攻击的向量。OpenAI 公司表示正在调查此事。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Mozilla：十六进制代码可用于操纵 ChatGPT 写 exp](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521319&idx=1&sn=cbfae51c8facf463612f1507daddd94f&chksm=ea94a54ddde32c5b7ff26a5495c0c74862c8d1d5d0f76cbca0ca1a506b5dc7d6f3328da0a5ff&scene=21#wechat_redirect)

[OpenAI：伊朗国家黑客利用 ChatGPT 密谋 ICS 攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521056&idx=2&sn=99545ebc43462c5f2e8b1617494b75b4&chksm=ea94a24adde32b5ce4b9b00bd228fb6a8252d88eacd3650ffea09f9e79b36b16427d0747f51c&scene=21#wechat_redirect)

[利用“傻瓜式”攻击方法提取 ChatGPT 训练数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518265&idx=1&sn=a7468dec27bf58ffeb2e1d475019fdb7&chksm=ea94b953dde330456b022dcb4bcd5a475261f12e68f4b3043e2b2fb32ac648ff3de6fb50341d&scene=21#wechat_redirect)

[ChatGPT 的新代码解释器存在重大漏洞，用户数据可被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518149&idx=1&sn=915ff8302203c2d80f8010384fe1efd2&chksm=ea94b6afdde33fb9dc7416eef6e9266e5b18d129ef74f31ef2232c486b5dd672568fbec49fc5&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/artificial-intelligence/chatgpt-allows-access-to-underlying-sandbox-os-playbook-data/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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