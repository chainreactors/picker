---
title: 大多数网络攻击的成功只因1%的漏洞导致
url: https://mp.weixin.qq.com/s/KrZvN9_VA4s5ifA8BmJkMg
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:05:44.595571
---

# 大多数网络攻击的成功只因1%的漏洞导致

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NfTcBxVIDrFeIInsqraEaqu1LR5TQII0jkV2ria6zy3yXCibrt5Iq6PsXibXlyorvl9krChfV4zH34GTxk2NXmq7wzPyUl4EWTFU/0?wx_fmt=jpeg)

# 大多数网络攻击的成功只因1%的漏洞导致

黑白之道

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

**本文关键看点：**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

**#****01**

2025年48,000个CVE，实际用于真实攻击的只有1%；

**#****02**

AI导致的虚假漏洞泛滥；

**#****03**

漏洞修复无法跟上漏洞利用；

********▍********本文内容由AI工具翻译生成，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

尽管每年披露的安全漏洞数量高达数万项，一项最新研究发现，绝大多数漏洞从未在实际攻击中被利用。真正造成破坏的，是一小部分被“持续定向攻击”的高价值漏洞。

![图片](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mzkSc0YHYPEGMmnmZBXNnmADoRBZYiaAWGHw2ckwPibia5nclljkSCkccIDkR4aiclNQPBqFXFFF7sycI7mQSWAaG2wTQT1iay0UNhk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

研究机构 VulnCheck 今日发布《2026 Exploit Intelligence Report（2026 年漏洞利用情报报告）》，对过去一年攻击者行为进行了系统性分析。报告指出，在 2025 年披露的 48,000 个 CVE 漏洞中，仅约 1% 被用于现实世界攻击。然而，这极少数漏洞却遭到极高频率、极短时间窗口的集中打击。

**0****1**

**重点攻击 CVE：被持续定向的高危漏洞**

该研究独家分享给 Hackread.com，并列出了黑客重点利用的具体漏洞。

排名首位的是 React2Shell（CVE-2025-55182），该漏洞可帮助攻击者绕过主流 Web 平台的安全机制。部分攻击组织在漏洞披露后数小时内即尝试利用。

企业级软件同样成为攻击焦点。Microsoft SharePoint（CVE-2025-53770）和 SAP NetWeaver（CVE-2025-31324）漏洞位列滥用榜前列。值得注意的是，针对 SAP 漏洞的攻击活动早在 2025 年 1 月即已出现，而官方披露时间则晚了三个月，显示出攻击者可能提前掌握漏洞信息。

大量攻击属于零日漏洞（zero-day）利用，即受害组织在尚无补丁可用时即遭攻击。报告指出，与勒索软件相关的漏洞中，有 56.4% 首次被发现时即处于攻击利用状态。

VulnCheck 首席技术官 Jacob Baines 表示，尽管被重点攻击的漏洞数量不多，“但这些漏洞正以更快的速度、更大规模被武器化。”

**02**

**国家行为体与勒索软件团伙活跃度变化**

报告还揭示了威胁行为体格局的变化。

与中国有关的威胁组织活动量在过去一年增长了 52%，而已命名国家级组织的整体活动量则下降 13%。与此同时，与伊朗有关的组织活动有所下降。

除国家行为体外，多个知名勒索软件家族依然高度活跃，包括 Cl0p、DragonForce、Earth Lamia 以及 RomCom。这些团伙正越来越多地专注于“初始访问点”（initial access points），以更高效地窃取数据并实施勒索。

**03**

**“AI 垃圾代码”泛滥：信号被淹没**

2025 年，VulnCheck 共跟踪到超过 14,400 个漏洞利用样本，涉及约 10,480 个独立漏洞，较上一年增长 16.5%。

这一增长部分源于所谓的“AI 生成垃圾代码”（AI-generated slop）。该术语指由 AI 自动生成的虚假或不可运行代码。这类代码虽然通常无法真正利用漏洞，但会在互联网上制造大量噪音信号，使防御人员更难识别真实威胁。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mzr3kdVBenjS3elrTCLSpwG57wdPpkib9ppeFvpd3KTOIHedEIeibtyjyorD66XpQz2h6Uu6uaO1y5gSS8eNiazUggpVSQmMAbSw8/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

风险态势依然严峻。去年共有 884 个漏洞被新增至 VulnCheck 的“已知被利用漏洞”数据集中，其中近一半为 2025 年新披露漏洞。值得注意的是，截至 2026 年初，约三分之一与勒索软件相关的漏洞仍未发布公开补丁。

总体而言，报告指出一个清晰趋势：漏洞发现数量创历史新高，但漏洞修复与风险控制能力，并未跟上攻击者武器化与利用漏洞的速度。对安全团队而言，关键不在于应对“所有漏洞”，而在于识别并优先防御那 1% 真正驱动攻击的高风险漏洞。

\* 本文为泽钧编译，原文地址：https://hackread.com/1-security-flaws-drive-cyberattacks-2025-report/
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

> **文章来源：数世咨询**

黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！

如侵权请私聊我们删文

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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