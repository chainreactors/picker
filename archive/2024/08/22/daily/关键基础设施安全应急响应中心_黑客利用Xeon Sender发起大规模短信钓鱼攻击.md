---
title: 黑客利用Xeon Sender发起大规模短信钓鱼攻击
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545438&idx=2&sn=9d7420d08e3df05479f476da0aecb3e0&chksm=c1e9be0ff69e371997bc1dec48756dc44f3e3921fddf5c85f80f4b24d3955733f620fbf7222a&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-22
fetch_date: 2025-10-06T18:04:29.273875
---

# 黑客利用Xeon Sender发起大规模短信钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguqETZ6dLwNO7tLehI2iaTBP1thWpzo86tPJibPQbEPnR9JrJc7YvUIEQAEuacTYTSxJ8p7a7W8YwFw/0?wx_fmt=jpeg)

# 黑客利用Xeon Sender发起大规模短信钓鱼攻击

关键基础设施安全应急响应中心

恶意行为者正在使用一种名为 Xeon Sender 的云攻击工具，通过滥用合法服务大规模开展短信钓鱼和垃圾邮件活动。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39jIMgwZ8qzxKQplH6ymZO1RjMSmpK721tP0tRttMDibrGKRpXibicXySjjmtOfpHMzicaFEmlWZcAudw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

SentinelOne安全研究员Alex Delamotte在与《黑客新闻》分享的一份报告中提到：攻击者可以利用Xeon通过多个软件即服务（SaaS）提供商，使用服务提供商的有效凭证发送信息。

据悉，用于大规模分发短信的服务包括亚马逊通知服务（SNS）、Nexmo、Plivo、Proovl、Send99、Telesign、Telnyx、TextBelt 和 Twilio。

值得注意的是，该活动并没有利用这些提供商的任何固有弱点，而是使用合法的 API 进行垃圾短信群发攻击。还引用了 SNS Sender 等工具，这些工具越来越多地成为批量发送钓鱼信息并最终获取目标敏感信息的途径。

其主要是通过 Telegram 和黑客论坛传播，其中一个旧版本归功于一个专门宣传破解黑客工具的 Telegram 频道。最新版本以 ZIP 文件形式提供下载，归功于一个名为 Orion Toolxhub的 Telegram 频道，该频道有 200 名成员。

Orion Toolxhub 创建于 2023 年 2 月 1 日，免费为成员提供可用于暴力破解攻击、IP 地址反向查询的软件，如 WordPress 网站扫描器、PHP web shell、比特币剪切器，以及一个名为 YonixSMS 的程序，该程序声称可提供无限短信发送功能。

Xeon Sender 也被称为 XeonV5 和 SVG Sender，这个基于 Python 的程序的早期版本最早在 2022 年被检测到。

Delamotte 表示，该工具的另一个化身是托管在带有图形用户界面的网络服务器上。这种托管方式消除了潜在的访问障碍，使那些可能不擅长运行 Python 工具并对其依赖关系进行故障排除的技术水平较低的攻击者也能使用。

无论使用哪种变体，Xeon Sender 都为用户提供了一个命令行界面，可用于与所选服务提供商的后台 API 通信，并协调垃圾短信群发攻击。

这也意味着威胁分子已经掌握了访问端点所需的 API 密钥。精心制作的 API 请求还包括发件人 ID、信息内容以及从文本文件中的预定义列表中选择的电话号码之一。

除了短信发送方法外，Xeon Sender还具有验证Nexmo和Twilio账户凭证、为给定的国家代码和地区代码生成电话号码以及检查所提供的电话号码是否有效等功能。

SentinelOne 表示，尽管该工具缺乏精细度，但源代码中充满了单个字母或字母加数字等模棱两可的变量，使调试工作更具挑战性。

Xeon Sender 主要使用供应商特定的 Python 库来制作 API 请求，这给检测带来了更大的挑战。因为每个库都是独一无二的，提供商的日志也是如此，团队可能很难检测到对特定服务的滥用行为。

因此，为了抵御 Xeon Sender 这样的威胁，企业应该监控与评估或修改短信发送权限相关的活动，或对分发列表的异常更改，如大量上传新的收件人电话号码。

**参考资料：**

https://thehackernews.com/2024/08/xeon-sender-tool-exploits-cloud-apis.html

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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