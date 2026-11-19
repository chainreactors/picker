---
title: 平台一旦停摆，两万终端就是两万个孤岛：某区级政数局终端安全高可用建设实践
url: https://mp.weixin.qq.com/s/sFoL-Jx7hrGC32HF3uKTxw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:34.371811
---

# 平台一旦停摆，两万终端就是两万个孤岛：某区级政数局终端安全高可用建设实践

# 平台一旦停摆，两万终端就是两万个孤岛：某区级政数局终端安全高可用建设实践

安恒信息

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icVz8RbowK3zzWCaicK1LPbSTJDDcicxleNaqXXSxYPFppNTsB1z02AlkKRMHgtzdCselqbaOWGGfYJPqibodouxRQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

案例实践 · 终端安全高可用

某区政务服务和数据管理局约有两万台终端承担核心政务服务，统一接入一个 EDR 管理平台。这些终端承载着便民服务、不动产登记、社保医保、市场监管等业务。

政务终端不能停，

平台是整张网“看得见、管得住”的中枢

从职能看，这个单位统筹区域政务大厅服务、审批便民改革、数字政府建设与政务数据共享，还牵头 12345 热线的督办工作，面向企业和群众提供线上线下政务服务支撑。与企业办公终端不同，这里的终端白天持续办理业务、覆盖民生事项，数量大、点位散——这类场景的安全产品，管理中枢能不能持续在线，是一条硬指标。

两万台终端能统一管理，靠的是平台的集中管控。终端上的 EDR 客户端在本机执行防护，平台中断时仍照常生效——但它守的是自己那一台。资产盘点、日志汇总、关联分析、告警通知、处置下发，这些事都需要平台来调度；平台一断，这几件事同时停摆，全网退回各自独立防护的状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QsTClNuIiapF1J7Iicw5MRNHOotI1uasRt2FMXHKMYrTuzibpbe5bvbDUrVPbYx53KH4n6oJNicXYq4TYAiaHn9I8bTKCN2Bk4O3LnBYUYF7SAjA/640?wx_fmt=png&from=appmsg)

图 1｜两万台终端分散接入，统一汇入同一个 EDR 管理平台。

建设这套系统时，端侧要挡住勒索、病毒扩散和非授权外联，平台要能盘点资产、下发策略和闭环处置。检修和发版期间，集中管理同样不能断档。

安恒EDR搭载鸾鸟高可用底座

保障安全运营不断档

高可用需要在上线前确定，不能等到故障发生后再补。它保的是整套安全运营持续运转——看得见全局，研判、下发、处置也能照常推进：业务窗口未必立即察觉，终端规模越大，这段空窗的代价越重。

安恒自研鸾鸟底座，让平台集中管控更稳。EDR 管理端部署在鸾鸟底座上，集群、编排、存储、升级这些最考验工程能力的环节都由底座承担——这是长期迭代出来的成熟平台，部署时就自带高可用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QsTClNuIiapFug6J5OgicibzHbictmX1iaBRdQksibtus7hDbbcHQneOYAAvz9BK8dOcnHbrBTpDI7JYUFbCXlttt9IvYIZ09fBW3FNblic8xRcCA4/640?wx_fmt=png&from=appmsg)

图 2｜鸾鸟底座支撑的 EDR 高可用能力

高可用落地的五个常见顾虑

*惑*终端散在镇街和延伸办公点，切换一次是不是要逐台调整配置？

**解**不用。终端只认一个地址，要提前确认的只有一件事：管理节点在同一网段内，这个地址才能漂移。

*惑*上高可用，是不是得单独配一套机器、专门派人盯着？

**解**不需要。集群由底座提供，不另购组件、不另做集成；日常也不用专人值守，扩缩、切换都由底座处理。

*惑*数据多存几份，是不是很占空间、维护起来也麻烦？

**解**冗余由底座统一维护，扩容、重建不额外增加人工；占用按数据类型分配，避免全量镜像成倍增加。

*惑*升级难道只能挑半夜停机做？白天发版会不会出事？

**解**不用挑半夜。升级在业务运行中完成——要排的是变更窗口，不是停机窗口。

*惑*这套平台能否应对机房级故障？

**解**同城范围内，集群可以跨机房部署，一个机房出问题由另一个机房承接，数据和管理都不中断；异地容灾则按灾难恢复的要求单独设计。

两万台终端，管理始终在线

平台建成后，区级政务服务和数据管理局的两万台终端都在同一个平台上管理。资产状态、在线情况、策略执行情况，在一处就能看到；日志和告警实时汇总，需要追溯时随时能查；检修和升级按计划推进。安全运营这层，不再因为平台状态留出空窗——日常值守和应急处置都能照常接上。

![](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapHiaYKkE31Rc2RwKWWWMYoicBJUm3VsNxBxzicA1wKcjeeT2ib8wp5JflbEdqYp19f6gqsD8ftlm7I0rm3g8EDX6wibyZX29V4sdYJY/640?wx_fmt=png&from=appmsg)

图 3｜XX区级政务服务和数据管理局风险评估视图。

平台不断档，这张网才始终看得见。

![](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapH770UDVz4icATpq15ibQbEcLQtWTcUbLLicBkopQmjBz3I3VsOurcxzic0UVzyibOia3pl558jSicPYpaXwsKnDFt1LyTV9BtNrBZUzg/640?wx_fmt=png&from=appmsg)

扫码获取限时免费试用

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Ppczr1X4OOTmbg4rENrqwqbYqRtgl3icicic9an9TicNrOnKOT4t2icSyx7w/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

**点点赞**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6P0OFJt7aruYwYjIWic5WCu7iaE9ZYWmW6TKPcvrib6Itmpc0dnMqlANmow/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

**点分享**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PwKHSiaCHQrj4D3mJJZ7QGPX1zbt3rJEKjhdBkX12A8r5L47fI28upaA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

**点喜欢**

点击下方名片立即关注

不走丢哦！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PzUETDErlviazPRtpVtc98iasfL8RCCib8yzmeGJ9HrBlJASFn5qz95QwQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Pb2aOfdTZnZZbozL1mvicIWsdWicdDcibz2SAuHblLHicWQc8CmX6WT6OMA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PBQVNtt5ynIG7UjUHbRJFvFXgKjZW6mzjjhlxfjwtXfrdJyPgroKWQA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

**往期****精彩****回顾**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

[博物馆里玩密室？CCF计算机博物馆即将开馆，安恒牵头的“计算+安全”展区抢先看！](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653916&idx=1&sn=27b2e720bf6315fba3e951a519c37120&scene=21#wechat_redirect)

2026-11-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QsTClNuIiapFmQfqSDrf5kwBibFBGrK4F2bOcWeEMq2KH5qGtuQE2LcQapJXYbkIu43JNZ7nX1kkK41zPxrHM9ZiavMOzDDia6ahGya3DjVtiaHU/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653916&idx=1&sn=27b2e720bf6315fba3e951a519c37120&scene=21#wechat_redirect)

[全国数据职业教育教学指导委员会成立，苗春雨当选委员](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653891&idx=1&sn=22b648e58280272f471c0191860a40b6&scene=21#wechat_redirect)

2026-11-16

[![](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapHeNmn2l9TmPFSicKDhX3kzrDwuP9L5v9nMjYM4f8X11etuUNDTSYmTBvjWqk7aEn0vwFribNZMtKD2V8Yy5f4xzbzQ873wtsSkI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653891&idx=1&sn=22b648e58280272f471c0191860a40b6&scene=21#wechat_redirect)

[“十五五”规划专设AI安全保障章：企业要准备的三件事](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653864&idx=1&sn=cfad7ec8017c3b46cbca8d534fe0025a&scene=21#wechat_redirect)

2026-11-13

[![](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapGziaSibxlqJEb6ouLBUeQGZZ6icbQd0YB9k17td4zQpuBKHNmT21GEyMfic4q3CuOibjgKTRQRnOIQu5Ysww7AT9I6HzRaAr9D8kEc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653864&idx=1&sn=cfad7ec8017c3b46cbca8d534fe0025a&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3wm5VicXg2ibVyMsjPZ3OJSzTwdeSU207GIcBicQDzkDVgFNvXD0npWKhFtBb2VtiaczibVqM8HE0vRoNw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/cbge2dLXia4bbQyBibIkuZz7hZVFlib5Oib5VZCiacheOLBHzKc88VEQYkXdC7BfdzLSVml0HWO6RjrP7FHL8oL0ONw/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=43)

法律声明

本文数据均来自内部统计、媒体报道、公开信息整理等，仅供信息分享，可能存在统计口径差异或误差，敬请理性看待，我们不对其准确性承担责任。股市有风险，投资需谨慎。阅读者在作出任何投资决定之前，应当咨询各自的顾问。本公众号发布内容仅代表内容创作视角，不构成任何投资建议或投资依据。在任何情况下，本公众号及运营主体不对任何人的投资结果承担法律责任。本公众号原创内容，欢迎合法合规复制、转载，转载时请务必注明出处，不得断章取义、以偏概全或进行有悖原意的引用。

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3yb7qoZWcKSwhTB3uxkfjDibSNP8lzqckKw2hXiarlP61qbUia2RUibZ15gV3hiabWypl17tkwrW7SaWOg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过