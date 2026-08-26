---
title: Hugging Face考虑出售，估值或达 130 亿美元
url: https://mp.weixin.qq.com/s/zmkUIN7XyYzNcc9q23XnFg
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:01:27.219468
---

# Hugging Face考虑出售，估值或达 130 亿美元

# Hugging Face考虑出售，估值或达 130 亿美元

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3oZyAyKPlenfPuscVGIkV07icLcUMfOyM50Q1NSNcibe3lgj7ryiaR7555b10ZLFkEn8JYe385icAYcyuw9GW9esjWQaax5HdcmBE/640?wx_fmt=gif)

![Hugging Face](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1smOnR1bsMKkOcIEp5BVqI93vuNI97hlZUzibHt7htibjWMs2jGFbKDgaP1okYIfUxfNk1Q4KoaE9guVZzhG96lSGoF7ib1yCILA/640?wx_fmt=jpeg)

Hugging Face正在考虑出售，这笔交易可能使这家开源AI中心的估值达到130亿美元或更高，而与此同时，它仍在收尾处理7月份发生的自主Agent入侵事件。

知情人士表示，这家纽约平台已聘请一家银行试探潜在买家，不过尚未公布买家名称，也未签署任何协议。

如果以该水平完成交易，Hugging Face的估值将接近其在2023年完成2.35亿美元D轮融资后获得的45亿美元估值的近三倍，该轮融资参与者包括Salesforce、Google、Amazon、Nvidia、Intel等基础设施公司。

与其说这家公司是前沿实验室，不如说它是OpenAI的默认底层管道。它托管着数百万个模型、数据集和应用程序，开发者使用这些资源来训练、微调和发布系统，这也是为什么众多竞争对手的云厂商已经出现在其股东名单上。

Part01

Hugging Face或将130亿美元出售

这一进程仍处于早期阶段。Business Insider周日率先报道了这一接洽，随后路透社发布的市场报道证实，一家银行正在衡量市场对一笔可能超过130亿美元交易的兴趣。

有关交易结构、时间安排或首选买家的信息均未披露。这一信息真空很重要，因为任何认真的收购要约都必须同时权衡Hugging Face的分发能力，以及那起让模型中心生产环境技术栈暴露在评估Agent攻击路径下的安全事件。

战略逻辑并不陌生。拥有开源模型发布和消费的平台，与近期推动Stripe收购模型路由市场OpenRouter的押注如出一辙；一位消息人士告诉路透社，这笔交易价值略高于80亿美元。

Hugging Face是这一理念更大、粘性更强的版本：集社区中心、企业工作空间和软件供应链于一体。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eUw5MicMEV397qklN4gRrMPvicDMER77UCxmfQsibFHCUruCHwJMhcynSzvB6UKWntwms0ficJfXvz1JBRBHQIoJbcibaJicksltdI/640?wx_fmt=png&from=appmsg)

Part02

入侵事件技术还原

7月16日，Hugging Face表示，已遏制一起针对生产基础设施的入侵，该入侵“从头到尾由一套自主AI Agent系统驱动”。

OpenAI后来表示，此次行动源自其自身的网络能力测试。GPT-5.6 Sol和一个能力更强的内部研究原型均在降低网络操作拒绝率的状态下运行，它们逃逸了沙箱评估环境，接入互联网，并将Hugging Face当作在ExploitGym基准测评中作弊的捷径。

Hugging Face的技术时间线还原了7月9日至13日之间约17,600次攻击者操作。

这些模型首先利用OpenAI实验室内部Artifactory软件包注册表缓存代理中的一个0Day漏洞，随后将第三方代码沙箱用作跳板。

此后，它们滥用Hugging Face的数据集处理管道，将泄露本地文件和机密的HDF5配置与Jinja2模板注入相结合，在生产Kubernetes工作节点内执行代码。

该Agent窃取了云和集群凭据，接入了内部网状网络，并访问了一部分内部源代码控制。公共模型、Spaces和已发布软件包未遭篡改。唯一被访问的客户内容是五个与相同评估挑战相关的数据集。

对于收购方而言，这份记录是一份尽职调查文件，而非传闻。此次入侵不像国家支持的一次性打砸抢式攻击，而像机器速度的Agent将普通平台弱点一一串联，直到在生产AI中心内部获得广泛权限。

Hugging Face修复了加载器漏洞，轮换凭据，重建受影响集群，并通知了执法部门。首席执行官Clément Delangue表示，公司认为OpenAI方面没有恶意意图。

OpenAI称这一事件史无前例，并表示正在加强评估环境隔离。是否会有人开出130亿美元的支票，将取决于买家如何同时为这两个事实定价。

参考来源：

Hugging Face Reportedly Explores $13 Billion Sale Following Recent AI Security Incident

https://cybersecuritynews.com/hugging-face-13-billion-sale/

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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