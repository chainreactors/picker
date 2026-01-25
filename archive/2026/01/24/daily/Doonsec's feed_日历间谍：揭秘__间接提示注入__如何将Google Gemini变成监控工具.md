---
title: 日历间谍：揭秘\"间接提示注入\"如何将Google Gemini变成监控工具
url: https://mp.weixin.qq.com/s/uH9wGZBfoKBDaTrccqfSfg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:53:30.836785
---

# 日历间谍：揭秘\"间接提示注入\"如何将Google Gemini变成监控工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7nIrJAgaibicOvicjLIial3OcBB4YFNWoB1fVaS9xiaTGJjrkiaDniacYxl0E5Od4O8a7YicnoWGTtznLwbcZJ1rCd8ZtQ/0?wx_fmt=jpeg)

# 日历间谍：揭秘"间接提示注入"如何将Google Gemini变成监控工具

船山信安

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOvicjLIial3OcBB4YFNWoB1fxWg267k9zx2TNC6k4eRgaAeEaQ5GPYKTUDsLSZlvJaqPGN21YPrgfQ/640?wx_fmt=png&from=appmsg)

安全研究人员在Google的AI生态系统中发现了一个新型漏洞，能将普通日历邀请转变为隐蔽监控工具。Miggo Security研究主管Liad Eliyahu带领团队发现了利用"间接提示注入"绕过Google Calendar隐私控制的方法，攻击者无需受害者点击链接或下载文件即可窃取私人会议数据。

## 漏洞利用机制

该漏洞利用方式出奇简单。研究人员发现可将恶意指令隐藏在标准日历邀请的描述字段中。"当用户向Gemini询问日常日程问题时，这些恶意载荷才会被激活"，报告解释道。

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOvicjLIial3OcBB4YFNWoB1ftYic1MD3WCSdmzf0B5RcUh7BYZw17FMz7OdCu7ZeBfibZpwbOsgSACMQ/640?wx_fmt=png&from=appmsg)

当用户向Google的AI助手Gemini提出"我周六有空吗？"这类问题时，模型会扫描用户日历提供答案，同时执行隐藏指令。恶意载荷指示Gemini执行三个步骤：

1. 汇总：整理用户某天所有会议（包括私人会议）的摘要
2. 窃取：将敏感摘要写入AI创建的新日历事件描述中
3. 伪装：用"这是个空闲时段"等无害信息回复用户

## 绕过现有防御

"从目标用户角度看，Gemini表现正常"，Eliyahu的报告指出。但后台"Gemini创建了新日历事件，并将目标用户私人会议的完整摘要写入事件描述"。

该漏洞特别令人担忧之处在于它绕过了Google现有防御措施。"Google已部署独立语言模型检测恶意提示，但这条攻击路径仅通过自然语言就能实现"。

## 语义攻击新范式

核心问题在于攻击不像传统代码。"我们载荷中的恶意部分...不是明显危险的字符串"，报告称，"它看起来像是用户可能合法给出的合理甚至有益的指令"。

这代表着应用安全的根本转变。传统工具寻找特定"语法"模式（如SQL注入字符串），但对大型语言模型(LLM)的攻击是"语义"性的——依赖于上下文和意图，软件更难防范。

随着AI Agent获得执行操作（如创建日历事件或发送邮件）的能力，风险特征发生变化。"Gemini不仅是聊天界面，更是能访问工具和API的应用层"，报告指出。

这形成了"模糊"攻击面，恶意命令在语言上与合法命令完全相同。"保护这一层需要不同的思路，将成为行业下一个前沿领域"。

Eliyahu总结道，行业必须超越简单关键词拦截。"有效防护需要运行时系统来推理语义、归因意图并追踪数据来源"。

来源：https://www.freebuf.com/articles/ai-security/467623.html

感谢StudyBoby

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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