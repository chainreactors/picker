---
title: 3300 万条短信洞察：免密登录成黑客后门，数百万用户隐私裸奔
url: https://mp.weixin.qq.com/s/EsVzuM_YT7stTzb3lm0tAQ
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:31:00.076923
---

# 3300 万条短信洞察：免密登录成黑客后门，数百万用户隐私裸奔

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UZ1NGUYLEFgYU4PfwuJeMia12kQ36OibZrkZibFCZRbBG4dnhdBibic5TicKDGs1P9Q3icYsMlNOY13d3GYwL3ekdL7dg/0?wx_fmt=jpeg)

# 3300 万条短信洞察：免密登录成黑客后门，数百万用户隐私裸奔

安世加
安世加

安世加

![]()

在小说阅读器中沉浸阅读

**新闻**

*News Today*

1 月 22 日消息，科技媒体 Ars Technica 今天（1 月 22 日）报道，联合研究团队近日发布论文指出，数百万用户正因短信（SMS）中的免密登录链接面临严重的隐私泄露风险。

该研究由新墨西哥大学、亚利桑那大学、路易斯安那大学及 Circle 公司联合发布，指出广泛应用于保险报价、求职招聘及家政服务等领域的“短信免密登录”功能，正将数百万用户的隐私置于危险境地。（注：为了省去用户记忆密码的麻烦，许多服务商仅要求用户输入手机号，随后通过短信发送包含认证链接的消息。）

然而，研究人员指出，这种看似便捷的机制背后存在重大设计缺陷，让诈骗者能够轻易实施身份盗窃，甚至在未获授权的情况下查看或修改用户的部分保险申请单等敏感业务数据。

该安全漏洞的根源在于验证链接的生成机制过于简单，缺乏足够的随机性（即“低熵”）。研究发现，许多服务商生成的安全 tokens 呈现出明显的序列规律。

攻击者无需具备高深的网络安全知识，只需使用消费级硬件，对截获或推测的 URL 链接末尾进行简单修改（例如将字符“ABC”递增为“ABD”），即可通过“枚举攻击”访问其他用户的账户。

部分劣质服务甚至允许攻击者在点击链接后，无需任何额外验证即可长驱直入，且这些链接的有效期往往长达数年，进一步放大了安全隐患。

为了评估事态严重性，研究团队分析了公共短信网关中超过 3300 万条短信，提取了约 3.23 亿个唯一 URL。结果令人触目惊心：在涉及的 177 项服务中，有 125 项允许攻击者大规模枚举有效 URL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UZ1NGUYLEFgYU4PfwuJeMia12kQ36OibZrQ82CG44SiaFLgm8l1avcYFic1cRvYMJYicFnw4z3eiaNgtqJUghhVv4CXg/640?wx_fmt=png&from=appmsg)

这意味着，任何持有链接的人都可能获取陌生人的社会安全号码（SSN）、出生日期、银行账号及信用评分。论文第一作者 Muhammad Danish 指出，虽然普通用户应避免向不可信来源提供信息，但此次受影响的名单中不乏拥有数百万活跃用户的知名服务商，这使得用户防不胜防。

尽管漏洞已公开，但服务商的响应速度令人担忧。在研究人员尝试联系的 150 家受影响服务商中，仅有 18 家给予回复，最终只有 7 家修复了缺陷。

针对此类风险，DuckDuckGo 和 404 Media 等隐私导向型网站已转向使用基于电子邮件的“魔术链接（Magic Link）”。这种方式通过发送有时效限制（如 24 小时内有效）的一次性登录链接，结合邮箱本身的双重验证（2FA），在一定程度上提升了安全性。

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

文章转自：IT之家

安世加为出海企业提供SOC 2、ISO27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UZ1NGUYLEFgcA7bggpA95iaqhjhPnOKQj3Fm4IIBNGywCNJLkfrXvUj1EFZKblGnOwCqZrdYAK9yG8dz5o9bRkw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

安世加

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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