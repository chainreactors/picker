---
title: 光速4小时解封！Anthropic与OpenClaw的博弈真相
url: https://mp.weixin.qq.com/s/OqQOC_MzIbek_qyspeKEvg
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:41:28.330146
---

# 光速4小时解封！Anthropic与OpenClaw的博弈真相

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKjMjhok69QXphLPJfczWESxrHxemMqKt56HaMQI0vibvNQkZjc7dMXV9iaOoVnFibyJhvAnibLRd8wZRp3zN3TicUTRPmxibs6DwANo/0?wx_fmt=jpeg)

# 光速4小时解封！Anthropic与OpenClaw的博弈真相

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

4月10日晚，AI圈直接炸了。

OpenClaw（江湖人称“龙虾”）创始人Peter Steinberger，在X上晒出了Anthropic的封号邮件：

经内部调查，你的账户存在可疑信号，违反使用政策，我们已撤销你对Claude的访问权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJQl7DLhsuia4sXROMQzwic7prfoRgX92ekv7ibZyibVWgs1WjCQJAvolniaV9XMQq5vicDPaCLVyxKO2S3HSjLJziaibibYYKJL3p37JVs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJO3OH9eJDDlH2uTAcPJn3IjGTd3GonibCtanc4yfFh6XdwVwzph92KUH0nFlngoguDDpE6cNJHBcvyKWuLaYrOzWDe73ibdKdfc/640?wx_fmt=jpeg)

紧接着他补了一句扎心的话：

各位，未来要让OpenClaw继续兼容Anthropic的模型，会变得更难了。

消息一出，开发者社区瞬间沸腾。有人骂Anthropic“卸磨杀驴”，有人感慨“开源生态终究干不过巨头围墙”。

结果谁也没想到——仅仅4个小时后，Peter就发了第二条推文：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIWsmVibRnVEGSqe0rRD3OuRgwyXN3ugvuPsiaQx7RSx6th3lrkiburM0EaMZvQwKghFQemdickayFfzRnRib1z74nDKXK7NibpnzGeo/640?wx_fmt=jpeg)

我的账号恢复了。谢谢大家！

从“全网封杀”到“光速解封”，这波极限反转，把Anthropic的焦虑、开源生态的挣扎，全摊在了阳光下。

01 OpenClaw是什么？为什么Anthropic非要“敲打”它？

OpenClaw不是简单的第三方Claude客户端，它是完全由Claude自己写出来的开源AI Agent框架。

Peter用自然语言给Claude提需求，让AI一行行写出了这个能自主执行任务的工具——帮你管邮件、理日历、处理文件、订机票，相当于给Claude装了一双“能干活的手”。

这款工具爆火后，成了Claude订阅用户的“神器”：

花20美元/月的Pro订阅，就能用OpenClaw无限调用Claude模型，相当于用“包月自助餐”的钱，吃了“无限量自助火锅”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJyJ5lADBXS56l3c2bDMaGLj8wPByGyHzyX5IvWG3Qo7q0icWbeJYbHbBh0ay410icthdHCdcJt1wVNCyjP8ibny89yXE9iczDZRibA/640?wx_fmt=jpeg)

而这，恰恰踩中了Anthropic的红线。早在今年1月，Anthropic就明确规定：

Claude的OAuth Token仅限官方产品使用，第三方工具、Agent SDK一律禁止。4月4日，Anthropic直接下了死手：Claude订阅额度不再支持OpenClaw等第三方工具，想继续用？要么单独买API按量付费，要么开通额外用量包，彻底终结了“薅羊毛”的可能。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKS5bw0GaxbRqkpOc57Ea76Wxg2IegE55ibQwrHxF8o4WrZCFFGXVI4NxYSy1JbrZpl3qdS7OAbcYmXge0XEdtzqxUqohicLv3zE/640?wx_fmt=jpeg)

说白了，Anthropic的核心矛盾很简单：

用户用低价包月疯狂调用模型，带来了远超预期的算力成本；OpenClaw分流了官方产品用户，还威胁到自家Claude Code产品；更关键的是，第三方工具让Anthropic无法精准控制模型使用场景，给安全合规带来巨大风险。这次封号，根本不是针对个人，而是对第三方开源生态的“杀鸡儆猴”。

02 封号又解封：Anthropic的“进退两难”，太真实了

为什么Anthropic刚封完号，又光速给Peter解封了？

答案只有一个：Anthropic不敢彻底把开源生态逼死。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicITlIicslWkpEYiav5O0oM0PyRy2cz73fPxdtABApoP758obV3T5NoN8YNSRfMic4yaXrYMcbciaFYLkA3stDvNXUTm3cTgGUia3VYo/640?wx_fmt=jpeg)

一方面，Anthropic极度依赖开发者生态。Claude能在GPT-4的围剿中杀出重围，很大程度上靠的是开发者社区的支持。

OpenClaw作为最火的第三方Agent工具，本身就是Claude生态的“活广告”——无数用户因为OpenClaw才订阅了Claude Pro。如果彻底封杀，等于直接把大量核心用户推给OpenAI、Gemini，这是Anthropic绝对承受不起的。

另一方面，Anthropic的政策本身就充满矛盾。它既想限制第三方工具的无节制调用，又不想彻底关上开源的大门；

既想保护商业利益，又要维持“AI安全、开放协作”的人设。这次封号，更像是一次“试探性敲打”：

警告Peter别再挑战政策底线，同时给社区明确信号——我们的规则不容侵犯。

奥特曼在X上公开称Peter是「一个有无数好点子的天才」。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicITiac17sy1CnMk7WUQIK4EIetkW74OzfeMY4zdyphFmfRcwQeIT1EliamjiaHlz7C4A9CMbPZhW66qRHgrzrrpvhzvbq7jWNHUTU/640?wx_fmt=jpeg)

而Peter的操作也堪称教科书级别：

先晒封号邮件引发社区共鸣，把自己塑造成“开源生态的受害者”；

不激化矛盾，只说“未来兼容会更难”，留足台阶；账号解封后第一时间感谢社区，既给了Anthropic面子，又巩固了自己的人设。

这是一场双方心知肚明的“表演”：Anthropic立了规矩，Peter赚了流量，社区看了热闹，最后各退一步，皆大欢喜。

03 这场战争，才刚刚开始

这次封号事件，本质上是AI巨头与开源生态终极博弈的缩影。

从OpenAI封杀第三方ChatGPT客户端，到Anthropic封杀OpenClaw，再到各大模型厂商收紧API权限，一个清晰的趋势正在发生：AI行业正在从“开放协作”，彻底转向“巨头割据”。

巨头们的逻辑很简单：

模型训练、算力投入都是天文数字，必须靠付费订阅、API收费回本；第三方工具的无节制调用，本质上是在消耗巨头算力，却不产生对应收益；只有筑起围墙，把用户锁在自己的生态里，才能实现商业闭环。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKNVw5CeeSyJq8AghVHkfqj643jeYAqAFr45GKoPUgeicENlbETcBjAcjLtdjbEwf349xy6hhauNdSxI2j24iauZKJcdHnMZUibNo/640?wx_fmt=jpeg)

而开源生态的反抗从未停止：OpenClaw用户开始转向OpenAI、Gemini；

开发者们开发不依赖单一巨头的开源Agent框架；

社区用脚投票，支持真正开放的工具。

Peter在账号解封后，没有选择妥协，而是继续推进OpenClaw开发，用行动证明：哪怕巨头筑起高墙，开源的火种也不会熄灭。

网友评论：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJWJ8micR2iccYsYA2ErRPkbnLBGJNvPG1azjyNtXswh6cpetxDia7b1v33TdxLiaxHfxuPUgjiaiarPoTicRibVTPg0ofFmAE4J5mO25k/640?wx_fmt=jpeg)

最后

这次封号又解封的闹剧，给所有AI从业者、普通用户都提了个醒：

没有永远的免费午餐，也没有永远的开放生态。Anthropic的焦虑，是所有AI巨头的焦虑；

OpenClaw的挣扎，是所有开源工具的挣扎。未来的AI世界，注定是巨头围墙与开源生态的长期博弈。

而我们能做的，就是保持清醒：

既不迷信巨头的“开放承诺”，也不盲目追捧开源的“绝对自由”，在两者之间，找到属于自己的生存空间。毕竟，在AI的浪潮里，唯一不变的，就是变化本身。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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