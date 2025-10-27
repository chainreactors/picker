---
title: NSA敦促组织使用内存安全的编程语言
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247553904&idx=2&sn=8070bc03eae00daee7c21f0eb4de0abb&chksm=e915c34ade624a5cb7050678a005ae25d45e857167cadc8faf0fe1a3cd0d0cf52549e4a5e47d&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-17
fetch_date: 2025-10-03T23:01:26.679731
---

# NSA敦促组织使用内存安全的编程语言

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29mKMo6B5eb3MFYEClXcLqXqibHLybu3nLljV9CNlEe6PFp3ICnYmoQddssY9bUyosfbJRZuMh0Pyw/0?wx_fmt=jpeg)

# NSA敦促组织使用内存安全的编程语言

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

美国国家安全局（NSA）近日发布了指导方针，鼓励众多组织将编程语言从C和C++之类的语言转向内存安全的替代语言，即C#、Rust、Go、Java、Ruby或Swift。

这家政府机构发公告称：“NSA建议各组织尽可能使用内存安全的语言，并通过诸多代码强化防御措施来加强保护，比如编译器选项、工具选项和操作系统配置。”

这家政府机构主要担心的是，不法分子可能会利用内存管理不善的代码中的漏洞，内存管理不善的情况在为程序员提供更多选项和灵活性的语言中较为常见。

NSA举了这样的例子：威胁分子通过缓冲区溢出或利用软件内存分配缺陷来潜入系统。

与此同时，内存安全语言结合使用编译时检查和运行时检查，自动阻止由程序员犯错误引起的漏洞。注意，不是所有的错误，但每一点都有所帮助。比如说，涉及不安全使用内存指针或并发线程之间竞态的错误可以被这些语言发现。

NSA表示，恶意网络威胁分子可以利用这些漏洞实现远程代码执行或造成其他不利影响，这常常会危及设备，成为大规模网络入侵的第一步。

很明显，最好避免遇到这种情况。

NSA网络安全技术总监Neal Ziring表示，在开发软件时，一致地使用内存安全语言及其他保护机制很有必要，以消除此类漏洞。

然而NSA确实认识到，“内存安全”这个名称有点不当，这个概念比较宽泛。

内存安全也有其自身的难题。比如说，额外的内存保护级别可能一开始会减慢开发速度，因为内存不安全的代码不会由特定的工具链构建，不过漏洞数量较少、将来代码的可维护性更强，其回报可以说是值得的。从一种语言转换到另一种语言可能是ASCII的老问题，即使有时可以转换。比如说，虽然Rust功能强大，但学用起来难度相当大。

据调研公司SlashData声称，从2020年第一季度到2022年第一季度，Rust用户的数量增长了两倍。Go也非常受追捧，据统计它拥有330万名开发者组成的社区。JavaScript十年来一直是最受欢迎的语言，拥有1750万名开发者。

虽然这两种语言无处不在，但NSA坚称C和C++特别成问题，这是一种流行的观点。微软的Azure首席技术官Mark Russinovich在9月份亮明了其观点，是时候停止使用这两种经受时间考验的语言编写的任何新项目了。

这位首席技术官确实承认，尽管他会偏向于用Rust编写新工具，但仍然存在“大量的C/ C++，将被维护和完善几十年（更长时间）。”就在他发推文的前一天晚上，Russinovich已经往其85000行Sysinternals添加了C/ C++代码。

网络安全公司Acronis的首席信息安全官（CISO）Kevin Reed在接受IT外媒The Register采访时表示：“我认为NSA的做法是正确的。”

“像地址空间布局随机化（ASLR）和堆栈保护这样的缓解措施是一种权宜之计，而不是全面的解决方案；改用内存安全语言要好得多”，Reed在呼应Russinovich的观点前补充道。

Reed表示，他对立马会看到效果持怀疑态度，因为多年来编写的C和C++代码数量很庞大，即使明天都开始使用Rust和Go，也需要几十年的时间才能收拾好这副烂摊子。

参考及来源：https://www.theregister.com/2022/11/11/nsa\_urges\_orgs\_to\_use/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29mKMo6B5eb3MFYEClXcLqX8xkj6elnCxDoBQYpGGf7Ue0fZuzRD4BqQtcb0Xvoc1x78JOfY6KUHg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29mKMo6B5eb3MFYEClXcLqXW3wxnj3QgztXtEDBqaHaPJOicEqUdpP59v7VQ2D1ewvDGq1x2W9Mgrw/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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