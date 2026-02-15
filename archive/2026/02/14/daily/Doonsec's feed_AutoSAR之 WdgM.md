---
title: AutoSAR之 WdgM
url: https://mp.weixin.qq.com/s/TBnacNLxuGsizzDvTG95Rw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:16:52.237088
---

# AutoSAR之 WdgM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDbnhEiajDiar51554gk6XBfG4MuSP6lXobibFPRbpWfgP4frZ8n6Gv8K9enFHPgqYm4faNAgUiaXjdX6T74B7sMQM3c6lVqGKAGxE/0?wx_fmt=jpeg)

# AutoSAR之 WdgM

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于车端软件开发
，作者初光

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4VlsQ4u7vnErC5WEVVGiceORT8gngeOqE93LlXXguhz7Q/0)

**车端软件开发**
.

『车端』智能汽车架构和软件开发平台，用心服务每一个读者

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

**01**

**介绍**

现代 ECU 包含高度模块化的嵌入式软件，该软件可以由非可信和可信软件组件组成，这些组件执行不同 ASIL 级别的功能。在这种情况下，我们有两种不同的方法

* 整个软件必须按照最高的ASIL进行开发。
* 保持具有不同 ASIL 级别的软件组件，并确保具有较高 ASIL 级别的组件不受具有较低 ASIL 级别的元件的干扰 FFI。（常用方法） 一个系统往往需要同时实现多条ASIL等级不同的功能安全需求，当这些需求分配到软件模块上，不同的模块需要满足不同的ASIL等级，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAib7kTwae4cK5icia0e87ts8iaF7R83nxZtznfLWp1YbjWbD0q6t9qibeGE8bEGZatqEmt31p33HwsnfxbFcdRJpoam6sGtEicsQ1sc/640?wx_fmt=png&from=appmsg)

**02**

**时间监控**

时序是嵌入式系统的一个重要属性。安全行为要求系统的动作和反应在正确的时间内执行。正确的时间可以用一组必须满足的时序约束来描述。然而，AUTOSAR 软件组件本身无法确保正确的计时。应该以某种方式确保它，但另一个独立组件是AUTOSAR WdgM。看门狗管理器 (WDGM) 位于 AUTOSAR 堆栈的服务层，如图所示，看门狗服务分布在 AUTOSAR 层中。它基本上包括：

看门狗管理器（服务层） 看门狗接口（ECU抽象层） 看门狗驱动程序（MCAL层）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA7RLYqPNXj917Piae19nyibiaYAM7uF9ib6sPn2MQwQ6GQg5lzGIPcy7laWgQzpUA722lFh3U3NLuLlj4ibkia14xml1zGTofIzfDZw/640?wx_fmt=png&from=appmsg)

看门狗管理器的任务是监督软件的执行，如果发现软件执行中的错误或缺陷，WDGM 将采取行动。SWC 使用 WDGM 提供的服务，使用客户端服务器接口。SWC 是客户端，WDGM 是服务器

定时保护和监控可以描述为监控以下属性：

1、监控任务在指定时间调度。

2、消耗他们的执行时间预算。

3、不要独占操作系统资源。（例如CPU负载重、中断请求多） 以下与时序和执行相关的故障可被视为软件组件之间干扰的原因：

* 执行的阻塞
* 死锁
* 活锁
* 执行时间分配不正确
* 软件元素之间的同步不正确。
* 执行流程不正确。ISO 26262 引入了一些用于错误检测的软件安全机制。它将活跃度和期限监督确定为临时保护的安全机制。并且还控制流监控作为错误执行流的机制。AUTOSAR 提供了一个方便的解决方案来实现这些机制/服务，它就是看门狗管理器 WdgM。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDbs9mtzlYBWbWlkCzicIyvHsWnSGE79qt17CjXGTfaUdW3aK6Bj2iaEcibfJflttJo7yJ3Ovxb89Lo4y44oeIT2SUIElVOGqg7UU/640?wx_fmt=png&from=appmsg)

WdgM 的主要目的是提供一种机制来验证 SWC 的执行和时序约束。它的目的是考虑周期性和周期性的最大时序约束来监督应用程序执行的可靠性。

为了构建可以提供所有这些服务的通用且可扩展的模块，AUTOSAR 引入了一种新模式来概括 WdgM 的功能。它将您想要监控的任何指定的感兴趣的软件实体声明为“受监管实体 SE”。SE 的监控是通过在 SE 内部放置一些点“API / RTE 调用”来验证目标事件（调度、完成等）是否已经发生，这些点称为检查点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCbT57SibVSpLsBRca1MUqTrHc94nicHtdm2RwWaCdlGP3clgMxMhvTUSlg5dXQa1lzY2OTN01biaOssCvAs3m38keOFEpqKSKiaWc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAp56C11Y6xoD1YyUefSwyHIZaY74Sbicz0nFTuzibGibaWVdHGMbwliavt1pqdsPlyex0iaAF37vicq7gbLicyguQ5oP0MkjtdPwDtyE/640?wx_fmt=png&from=appmsg)

WdgM 提供三种类型的监督来涵盖上述服务，如图所示。每个SE都有自己独特的标识符和本地状态。整个WdgM有一个整体状态，称为全局状态，根据监管类型、SE的配置，那些局部状态会影响全局状态，这将在后面描述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAa1Igx1aYEewibUOBzFiaedGf7rcyJeK4Il44MRPZNseictJR4byyFdE2IbpTTY0O497ia4WfDwZycI597FWOk4TmtCQCJVFWbOQE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBjFQwxHTDKsbjtB7EE3Aoe8DNMH1nv1psd0w0sSgdGaYO3iaKusN4pvNAxDa0gxhibQbYiaC5u4hdvAkiaNBiaM9eVNKAoIH8SQbyE/640?wx_fmt=png&from=appmsg)

WdgM 将获取包含所有 SE 及其配置的结构数组，并根据这些配置执行所需的监控，并且 WdgM 将相应地更新其本地状态。

在 WdgM 决定更新其全局状态以停止之前，本地状态不会导致重置，这将根据监督类型建立单独的状态机。下图包含监控和评估实时监督 SE 的流程图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBz6O8eQZu1Ugibpk3XJAsBCXmRzice3Syyico9EmxcWmibdBUiakrnyC9tKOhhmf3sQdIM3ibqvrvRQAcdoz2SNx08oPjexVhZUvqqA/640?wx_fmt=png&from=appmsg)

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=app...