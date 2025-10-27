---
title: 新发现！卡巴斯基称ChatGPT可用于恶意代码识别
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247534906&idx=3&sn=346e886b77ec7c153ce30cea5eb32b4b&chksm=fa93fffbcde476ed01bc621a53c7c679d22bdc086d70021d33b9981e637ef1e1e37cc39fe2ca&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-02-25
fetch_date: 2025-10-04T08:04:55.736661
---

# 新发现！卡巴斯基称ChatGPT可用于恶意代码识别

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176moltN6pDACpaVffQkr6gEBUJMkafHMt5SiaFMQoZZUP3yBIBOGVNy7roKveCo5xSjPqxTNOTG7jsg/0?wx_fmt=jpeg)

# 新发现！卡巴斯基称ChatGPT可用于恶意代码识别

网络安全应急技术国家工程中心

随着近日大型语言模型 (LLM) ChatGPT的流行，许多网络安全工作者也开始实验它在抵御安全威胁方面的能力。目前已有多项实验表明，ChatGPT不仅能够对潜在的安全事件进行分类，还能从中发现代码的安全漏洞，即便它没有专门针对此类活动进行训练。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR395GXpyw1LICt3AIRPxnpjlD3GBTvZ3wcC6fAo55jghqewRtJVrwfdJ0WImfRMXI6QnYtv2aV2HxA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

2月15日，卡巴斯基在一项实验中，将ChatGPT 作为事件响应工具的实用程序进行分析。他们模仿一般攻击者使用 Meterpreter 和 PowerShell Empire 代理感染了一个系统，用 ChatGPT 对受感染的进程进行识别。结果显示，ChatGPT在没有误报的情况下正确排除了137 个良性进程，识别出了2个恶意进程，并且还提供了该服务应被归类为陷落标识（indicator of compromise）的原因结论。

最终，卡巴斯基分析师使用 ChatGPT 分析了测试系统上 3500 多个事件的元数据，发现了 74 个潜在的危害指标，其中 17 个是误报。该实验表明，ChatGPT 可用于为未运行端点检测和响应 (EDR) 系统、检测代码混淆或逆向工程代码二进制文件的公司收集取证信息。

这项实验是从向 ChatGPT 询问 Mimikatz 和 Fast Reverse Proxy 等几种黑客工具开始的。人工智能模型成功地描述了这些工具，但当被要求识别众所周知的哈希值和域时却失败了，例如， ChatGPT无法识别恶意软件WannaCry众所周知的哈希值。

但显而易见，卡巴斯基在识别主机上的恶意代码方面则较为成功，他们要求 ChatGPT 创建一个 PowerShell 脚本，以从系统中收集元数据和危害指标并提交。在手动改进代码后，安全人员在受感染的测试系统上使用了该脚本。

在此之前，其他安全公司也在研究如何通过此类模型来执行特定的防御相关任务。去年12月，数字取证公司Cado Security使用ChatGPT创建了一个事件中的JSON数据的妥协时间表，生成了一份“不完全准确但总体良好”的报告。

# **结果是否可用？**

由此看出，ChatGPT得出的结果到底是否可用？安全咨询公司NCC集团尝试用ChatGPT作为寻找代码中的漏洞的方法，得到了“不总是准确”的结果。NCC集团首席科学家 Chris Anley 表示，安全分析师、开发人员和逆向工程师在使用如ChatGPT的大型语言模型时要小心行事，尤其是对于超出其能力范围的任务。

“我赞同专业开发人员和其他使用代码的人去探索 ChatGPT 和类似模型，但更多的是为了获得灵感，而不是为了获得绝对正确、真实的结果，“Chris Anley说道。”用ChatGPT进行安全代码审查不是我们的最佳选择，所以期望它第一次就做到完美是有点不公平。"

卡巴斯基事件响应团队负责人 Victor Sergeev也警告称，结果不准确是一个非常现实的问题，要注意这些这可能产生的误报和漏报，并称目前的ChatGPT”也只是另一个容易产生意外结果的统计神经网络“。

# **有待完善的隐私规则**

目前，已经有公司开始对使用互联网上的信息创建数据集提出异议，NCC Group 的 Anley 表示，安全专家必须确定提交的入侵指标是否暴露了敏感数据，或者提交软件代码进行分析是否侵犯了公司的知识产权。“向ChatGPT提交代码是否是个好主意，很大程度上取决于具体情况。"很多代码是专有的，受到各种法律保护，所以我不建议人们提交代码给第三方，除非他们得到许可。” Anley说道。

Sergeev也发出了类似的警告。使用ChatGPT检测漏洞，必然会向系统发送敏感数据，这可能违反了公司政策，并可能带来商业风险。

**参考来源：**

https://www.darkreading.com/analytics/chatgpt-subs-security-analyst-hallucinates-occasionally

原文来源：网信北京

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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