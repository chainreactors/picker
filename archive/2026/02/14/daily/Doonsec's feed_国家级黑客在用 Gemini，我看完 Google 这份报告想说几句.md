---
title: 国家级黑客在用 Gemini，我看完 Google 这份报告想说几句
url: https://mp.weixin.qq.com/s/zBYk8FKTSBCJb72wOb6seQ
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:22:24.679501
---

# 国家级黑客在用 Gemini，我看完 Google 这份报告想说几句

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFBoia4xTNmgc2cEwZRK9S5DjdJPFHAR6sGyKibl8ickma8XhibLvJf9JrdFjId9JrYzGZFw0kvyDoRIBDIdiaibgrs9sOkAiaI6USWND8/0?wx_fmt=jpeg)

# 国家级黑客在用 Gemini，我看完 Google 这份报告想说几句

原创

丘驰
丘驰

极客零零七

![]()

在小说阅读器中沉浸阅读

# 上周，Google 发了一份报告，内容很有意思。

报告说，中国、俄罗斯、伊朗、朝鲜的国家级黑客组织，正在用 Google 自家的 AI 产品 Gemini 来策划网络攻击。

其中中国的APT31（也叫 Judgment Panda，被 Google 追踪多年的老牌 APT 组织）的做法最有代表性——他们用 Gemini 扮演"网络安全专家"角色，让 AI 自动分析漏洞、生成针对特定美国目标的渗透测试方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L7VicJKsiaibFCmISKXVXZZEvsBERcjfrjoAxaSBtdiawrPOltnn2gQ7cEl0ESbgkZ9oVicsawVicicgKczo1tCKud4717umEkNqqM8iapByQhkOXsI/640?wx_fmt=png&from=appmsg)

配合他们使用的工具叫HexStrike，一个基于MCP协议的开源红队框架。

报告出来之后，各大媒体的标题基本都是「AI 被武器化！」「黑客用 Gemini 攻击！」，一片惊呼。

我也看了很久。但我想说的，跟大多数标题不太一样。

## 第一：这根本不是新鲜事

AI 辅助攻击，不是从 APT31 开始的。

我学安全这几年，AI 工具渗入渗透测试工作流这件事，早就在发生了。自动化漏洞分析、辅助 Payload 生成、加速代码审计——这些事情我自己也在做，相信很多读这篇文章的人也在做。

APT31 做的事情，说白了就是：用 Gemini 当「AI 助手」，像我们平时问「这个 CVE 怎么用」「帮我写个绕 WAF 的 Payload」一样。

区别只是，他们是有任务目标的国家队，我们是在靶机上练手的学生。

所以「国家级黑客用上了 AI」这件事，并不是新的技术突破。而是一个早已在民间发生的事情，现在有了国家队下场的确认。

## 第二：真正值得关注的不是 AI，是速度

Google 的报告里有一句话，我觉得才是核心：

> "APT 组织正在实验用 AI 来支持'半自动化'的攻击行动。"

**半自动化**。这才是关键词。

以前一个 APT 组织策划一次定向攻击，从情报收集、目标分析、漏洞选型、Payload 开发，可能需要几周甚至几个月。这些工作需要经验丰富的专家一步步来。

有了 AI 之后，这个流程可以被大幅压缩。

不是说 AI 能替代人，而是 AI 能让一个「够用的」攻击者，快速干完「需要专家才能做的」部分工作。这意味着：

* 攻击的**迭代速度更快**
* 能发起高质量攻击的**人门槛更低**
* 同样规模的攻击团队，能**同时覆盖的目标更多**

从防守方的角度看，这件事才是真正值得警惕的地方，不是「AI 在攻击」，而是「攻击者的节奏变快了」。

## 第三：一个有点荒诞的细节

Google 的报告里，有一个细节：APT31 用来辅助攻击的 AI，是Google 自己做的 Gemini。

而 Google 最终干了什么？把那些账号封了。

自家的 AI 产品被对手用来攻击自家盟友，然后自己发一份报告揭露此事，顺手把账号封掉。

这个故事放在科幻小说里，可能还不够写实。

当然，这其实说明了另一件事：大模型厂商对「谁在用我的 AI 干什么」，掌握着极强的可观察性。Google 知道 APT31 在做什么，然后选择了公开——这本身也是一种战略。

## 第四：我们普通学安全的人，该怎么看这件事

我问了我自己一个问题：

**看完这份报告，我明天打靶的方式会改变吗？**

答案是不会，但思维方式会变一点。

AI 是工具，和 Burp、sqlmap、Nmap 一样。工具本身没有立场，用的人有立场。APT31 用 Gemini 做攻击规划，我用 Gemini 做学习辅助，性质不同，逻辑是一样的——谁能用好工具，谁就效率更高。

但有一点，我觉得对我们这些学安全的人是提醒：

**如果攻击者借助 AI 在提速，防守方也必须借助 AI 在提速。**

不管是 IOC 分析、日志异常检测、漏洞响应，AI 辅助防守已经不是选修课了。这不是在宣传什么产品，而是一个客观的现实——靠人肉分析跑不过半自动化的攻击节奏。

## 最后说一句

这份报告让我印象最深的，不是 APT31 有多厉害，而是 Google 在最后写的那句话：

> **"目前没有迹象显示这些攻击取得了成功。"**

国家队用了 AI，结果还是没打进去。

这说明 AI 不是银弹，攻防对抗归根结底还是人的对抗。AI 是加速器，不是决定因素。

技术没有捷径，打磨能力才是正事。

**你在日常学习里有没有用 AI 辅助安全研究？效果怎么样？留言聊聊。**

下篇预告：APT28 利用微软 Office 零日漏洞（CVE-2026-21509）的完整攻击链拆解。

> 关注「极客零零七」，每周实战攻防干货。
>
> 回复「工具」获取渗透测试工具清单 · 回复「AD攻击」获取 AD 域攻击速查手册

**参考资料**

* Google: China's APT31 used Gemini to plan US cyberattacks — TheRegister[https://www.theregister.com/2026/02/12/google\_china\_apt31\_gemini/]
* Google Reports State-Backed Hackers Using Gemini AI — The Hacker News[https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html]
* Google says hackers are abusing Gemini AI for all attack stages — BleepingComputer[https://www.bleepingcomputer.com/news/security/google-says-hackers-are-abusing-gemini-ai-for-all-attacks-stages/]

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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