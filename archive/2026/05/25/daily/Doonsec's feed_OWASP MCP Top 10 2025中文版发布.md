---
title: OWASP MCP Top 10 2025中文版发布
url: https://mp.weixin.qq.com/s/1Nf6Nz_tOGpp1agpBWWy9A
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:58:55.938043
---

# OWASP MCP Top 10 2025中文版发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DLytMdWfrF6x3Znz27GibOGvziadK8UP3DBGeib7hqic5p5KhMJLxlKAleAJymNBxV0n8U5ceksbloeoEQe9glfQwJoCn7guaYUdsort83omiblo/0?wx_fmt=jpeg)

# OWASP MCP Top 10 2025中文版发布

一起聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhaTeG2u7bEwF1HJNXbF7yj3Kwvv5Hmf5422j2twUIGnTnbgic2WaEKJl1vYVRfCFibY5Ueh3bj1Mgg/640?wx_fmt=gif)

相关内容：

[OWASP Agentic Skills Top 10](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247523632&idx=1&sn=72409870e060a382aeb439a4b28d7727&scene=21#wechat_redirect)

[OWASP发布2026智能体应用十大安全风险！](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247522814&idx=1&sn=3992d24f506ee88e03ee40fe17dd95f8&scene=21#wechat_redirect)

[OWASP发布的2025年风险项有哪些？](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247521416&idx=1&sn=6e390c01730e180a07fd724ae2e54b3a&scene=21#wechat_redirect)

[最新版 | OWASP TOP10 安全漏洞（web方向）](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247521916&idx=1&sn=d4a844a85c4b7c0c55fb9803f3f04b8a&scene=21#wechat_redirect)

[OWASP Top 10 基础设施安全风险2024](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247517513&idx=1&sn=86c6977c4e0f49a4cdaa10a2ee4fe638&scene=21#wechat_redirect)

[2025 OWASP 大语言模型应用程序10大风险](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247516929&idx=1&sn=a715db45df94a45c7c28e803faee7416&scene=21#wechat_redirect)

[OWASP发布《AI大模型应用网络安全治理检查清单》](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247506852&idx=2&sn=a686522d2485dc56d756c99b294371a6&scene=21#wechat_redirect)

[OWASP大模型安全Top 10分析与实践](https://mp.weixin.qq.com/s?__biz=MzI3NjUzOTQ0NQ==&mid=2247521665&idx=1&sn=7c0b950ba31460e1bb59731caabe41a2&scene=21#wechat_redirect)

...

**OWASP\_MCP\_Top\_10\_2025中文版**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn4UQsuSPibycgVNox22LQBnDD0NdumaMoicrNPKGwwtFSl9sNEHkmkYibOymTOVNSWLjzicQXiaXITbQzA/640?wx_fmt=gif&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn4UQsuSPibycgVNox22LQBnDD0NdumaMoicrNPKGwwtFSl9sNEHkmkYibOymTOVNSWLjzicQXiaXITbQzA/640?wx_fmt=gif&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=3)

建随着人工智能系统日益融入软件供应链、企业应用和安全基础设施，构建结构化、安全且可解释的模型交互层变得至关重要。模型上下文协议（MCP）正在兴起，成为定义人工智能模型操作、上下文和行为边界的框架。然而，MCP的强大功能和灵活性也带来了一类新的漏洞和攻击面，而这些漏洞和攻击面仍有待深入研究。

    OWASP Top 10针对MCP的安全漏洞概述了MCP系统生命周期中最关键的安全问题，涵盖模型错误绑定、上下文欺骗、提示状态操纵、不安全的内存引用以及隐蔽信道滥用等。在涉及智能体AI、模型链、多模态编排和动态角色分配的场景中，这些风险会更加显著。

    通过梳理十大与MCP相关的漏洞，并为安全设计、实施和审计实践提供具体建议，本项目旨在帮助人工智能开发人员、机器学习工程师和安全从业人员掌握构建情境感知型和攻击抵御型人工智能系统所需的洞察力。OWASP MCP Top10将作为一份动态文档，随着人工智能模型能力和协议创新的步伐而不断更新，并以现实世界的威胁、研究成果和行业反馈为基础。

**1**

**介绍**

![图片](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUDKx7Re03yMQsfP8UpzKZbOE7CBe7RwoZYE2UWTqgh1MMDgZnoWxPJxTkIDYl5IDB4wwCe1AOLWRA/640?wx_fmt=png&wx_&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=4)

本白皮书基于 OWASP www-project-mcp-top-10 仓库 2025 目录全部 10 项风险条目完成全量翻译、统一校订与白皮书式编排，面向从事 AI 安全、智能体治理、研发安全、架构设计与安全运营的专业读者。全文在保留 OWASP 风险框架核心内涵的基础上，对术语、结构、文风和控制建议进行了系统统一，以便直接用于培训宣贯、内部评审、治理设计与正式汇报。

![](https://mmecoa.qpic.cn/mmecoa_png/AA7xLoo4FKarSd33DVVibKa8w5GKB1krEZkUln930DYuzJk4PARibIfktVdSF9pFxR0gz7URseyGkjbfJphKfKTiaTfLNLWxB1KZ9yicjjic52ug/640?wx_fmt=png&from=appmsg)

**2**

**团队成员**

![图片](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUDKx7Re03yMQsfP8UpzKZbOE7CBe7RwoZYE2UWTqgh1MMDgZnoWxPJxTkIDYl5IDB4wwCe1AOLWRA/640?wx_fmt=png&wx_&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=7)

项目组组长：张坤

翻译人员：张坤、卜宋博

审核人员：王颉、张坤

由于成员知识与翻译水平有限，存在的错误敬请指正。

邮箱：wangj@owasp.org.cn

**报告节选**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DLytMdWfrF4ApgWdgHYq09xxOsvCRpXzcMtWlnJpQ0XblgeFDTtKsgM9ickUrMnwKOPn30HUmC4g1kEibsfELXxEEyfdBlyVqtNb7zmMk43rM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DLytMdWfrF7fdR0iard8MjnvQEGRNsslPYXyxyWuNm00iasBfEaypTZxvWUMPZf2N0Fsc2CSAUJHoMbfe8rDYsrUILPFQ2Kic7lOjv6cmmoTNI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DLytMdWfrF7icwVRLwGia0Kj3HcRuRZKyUbcfcCZIGxjOXz6L7s6zEWxianKuRf4TTnNuB83DiaPo3DiaGFnclhFnqU1aJyUribUeCrpdcImGIHw8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DLytMdWfrF68bwr8XaOUX8YdfYEsYNGmtAUBL1D0qvNmyyicoMTUcicsZIQdrmZESChkGvCuKv7h7JZfyQ4R8cQLe5PicHBXbhM4vxkqAibW3os/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DLytMdWfrF7UYVeFicra1qTXiaq2jMLpuVUda0cqdF5ibOGyURlibn5bhNzfM4zqfoNDjQRuia5j7SibIy3I2ECSn0Kf4GpdA3JXYFnTCv6ysBvOo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DLytMdWfrF6pH0lHMgic4AzmIFQibwphE6bRpUYxLqdGibnGyYoO2exIm59TdbrBSfIqvib81obqdEvxFZJdO7c6Fj5m5m4UnENtjUt10EpLSlg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DLytMdWfrF6sxrhY0JIaLAeOh6YTZxUKsaw7EUIZ1tpZXaQLnvgFC25Y82jq9HWAER6aQnEfum6gdRj3MkGf5xxLNvvib21zPaQfR2tbecMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DLytMdWfrF7GeQUZJheDx20dR8blrYDOq5JgDT236tsqznia3VI6aFic2LphQFb9ZrWZzmIl1ZKsAJ2ZoiagcoldcFTsxCoViajI30QWT4dUx70/640?wx_fmt=png&from=appmsg)

**全部内容请到帮会中下载，感谢支持！！**

END

来源：OWASP

**freebuf 帮会简介**

![](https://mmbiz.qpic.cn/mmbiz_gif/GVddVRW7oDEVbUCJAMic9gZNHQKMIDs4q4XgJFzav6HztpaianNrNvDDB8E7eawnRSbzEy55S0g6lSXghg2vkzUg/640?wx_fmt=gif)

**「一起聊安全」**公众号及帮会致力于网络安全材料汇总与分享，围绕**网络****安全标准**、**安全政策法规**、**安全报告及白皮书**、**安全会议、安全方案、新技术**等方向，与FREEBUF知识大陆共建**【一起聊安全】帮会**，目前相关内容已有**8200+**，安全标准涵盖国标、行标、团标等，包括等保、关基、商密、数据安全、云计算、物联网、工业互联网、移动安全、风险评估、安全攻防等30+方向内容，覆盖最新安全政策法规、安全报告及白皮书等，为网安人提供最新最全资料。

![](https://mmbiz.qpic.cn/mmbiz_png/m7P2WNG81X6oLJEDDLlYXmCMLMlpBOIH2ZDHCjm0nNUVJrdWJzuptfr3DHRKwSHEfDPUlO1Fz4eHLs3iaHDyN1A/640?wx_fmt=png&from=appmsg)

****加入方式：**网页端和APP**

****网页端：******https://wiki.freebuf.com/societyDetail?society\_id=69**

****APP端：****

![](https://mmbiz.qpic.cn/mmbiz_png/m7P2WNG81X5tEVZrRY6pZFxM4kO5ReXZ9M0eAr2aUTpy17dK2heeG0qrktJ6kxBzEYBm7RdDf4PpTuXCYN07uQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

加入帮会是所有材料均可下载！

![](https://mmbiz.qpic.cn/mmbiz_gif/GVddVRW7oDEVbUCJAMic9gZNHQKMIDs4qfcR51jSJUB2CA1ATfdwPXX8ib1SoFsJQLbbVMTAQYdyVoettMpMTaIg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaHpokNh4uWxia9Vv2eYjfzjK9Euejia8GQQAicPWkJI7HfpDplIlc3tPr73ZYKHIdg9kIHpWaJia2tGA/640?wx_fmt=gif)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaHpokNh4uWxia9Vv2eYjfzjXjW9bUCoUia7g4iaVGGGm5AKWRMoDMQoFDdJuiceofhPJ8SJpKSGToZcw/640?wx_fmt=gif)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaHpokNh4uWxia9Vv2eYjfzjAEe2Bq3UgWlgxribzfYtnQ6EVkxkao5qmK0xpaoycfHyGVl7zFicPGibw/640?wx_fmt=gif)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaHpokNh4uWxia9Vv2eYjfzjDia9eCL6sIvuL17F5uKHsjx0GNc6estct1jOfWh4EtOcVsvzynOar1Q/640?wx_fmt=gif)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/m7P2WNG81X6gszEIGb6olEVA7J5PFeibFIFISSKHOd9udpmQBpFq8spz8ftpDfwOjPO7xSkTuQSpEKzryyTdoibg/0?wx_fmt=png)

一起聊安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/m7P2WNG81X6gszEIGb6olEVA7J5PFeibFIFISSKHOd9udpmQBpFq8spz8ftpDfwOjPO7xSkTuQSpEKzryyTdoibg/0?wx_fmt=png)

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