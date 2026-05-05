---
title: AutoSAR PNC和ComM
url: https://mp.weixin.qq.com/s/DO4g_9HUZN308kC6VK5WGg
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:04.513066
---

# AutoSAR PNC和ComM

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaC0icEczibOTujrYrl9uibryQyDm3qfFyR1mDySg51ePLy4auZbB9DHKP1AgaKksyp0RKIfhW40lbBCu56CcgHYr2Vg6Z5icCYouRs/0?wx_fmt=jpeg)

# AutoSAR PNC和ComM

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**01**

**PNC和ComM**

PNC 和 ComM层的Channel不是一个概念，ComM的Channel对应具体的物理总线数。

在ComM模块中，一个Channel可以对应一个PNC，也可以对应多个PNC。

**02**

**PNC管理**

PNC（Partial Network Cluster） 即“局部网络集群”， 通过一些规则（通常按照功能类） 将车辆网络进一步划分为不同的“局域网”， 通过 PNC 管理其各种状态。

如下图：OBC和BMS组成一个PNC1,而MCU和BMS又组成了一个PNC2。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDsIrIbvqp8IYuZwHNuvHRTZCOq7VBxXqNEuj8qOf9K154txyiclMXziarrZuWyAmbJGPtOR3AultuhtZBMoialHfc4z4mprTVn7s/640?wx_fmt=png&from=appmsg)

**NM PDU结构及PNC信息位置**

PNC,是一种将网络通信进行分组和控制的方法，属于AUTOSAR COM层，是从Autosar 4.0.3开始增加的，主要目的是为了省电；PNC是PDU中的一部分；

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCSmtRMm5EicPvoTSgp0gcD59MjtzKgW7cj6c8QXw26VWKdpSKfHgkQhicc3CtWfMFuvlsuJTuz8ianVufwMBorUOFwFfUN8FbEjg/640?wx_fmt=png&from=appmsg)

NID：Source Node  Identifier，即对应节点CAN报文的CanID，比如节点 NM Msg CanID 为 0x509，则 NID = 0X09(配置工具配置)，5表示网络管理报文类型。

CBV：Control Bit Vector，控制位向量。

User Data：使能PN功能时，存储PNC信息。假设某网段内有48个PNC，User Data中的每一个Bit代表一个PNC，可以用PNC 0 ~ PNC 47标识这48个PNC。注意：节点具体需要处理多少个PNC，根据需求配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBnia4c5PibbUbicdw81JJFxppibAge5UKBKKQwWnOt4NB7pibmhBptGrlHlXibLvwLnDDuYOq4ACUO3L0UYzMpjhnicH8IlcljzgUfQg/640?wx_fmt=png&from=appmsg)

**如何理解节点关联PNC**

一个网段内有多个节点，多个节点之间可以形成多个PNC，也就意味着：具体到某个节点，并不是所有的PNC 都对该节点有效。

比如：ECU1有两个节点Node1和Node2，Node1收到的网络管理报文中，只关注PNC20、PNC22、PNC30是否置位（ = 1），因为Node1只参与PNC 20、PNC22、PNC30三个网络簇，并不关心PNC16或者其他的PNC #n状态，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD8LpOIdCgjRXialvP64ib9KgenCOw7ubMsRiafOxfgibibzOfqEETonRMaGKtc157BFLz9681LGf3MDQN2ZGekibv1ItFan8NtKiaDvc/640?wx_fmt=png&from=appmsg)

**PNC状态管理**

PNC有两种模式，其中COMM\_PNC\_FULL\_COMMUNICATION包含三种子状态：

COMM\_PNC\_FULL\_COMMUNICATION

* COMM\_PNC\_REQUESTED
* COMM\_PNC\_READY\_SLEEP
* COMM\_PNC\_PREPARE\_SLEEP

COMM\_PNC\_NO\_COMMUNICATION

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCszhhrAQNicSAjY167SW1VWiaMVlLd9icSZ2YKEpmibbURge2ctmpkRDCkQMNpUiawdWZOHyJibRRfjEnIR02QfQXANwGV8OVd509YA/640?wx_fmt=png&from=appmsg)

系统上电后整个PNC的状态在COMM\_PNC\_NO\_COMMUNICATION。在PNC状态切换过程中如果是主动唤醒节点直接请求FULL通信，或者是网关节点控制的节点在收到网关下的ERA（External Request Array，表示的是外部的唤醒状态设置相关的数组）数组的相关状态位，直接从COMM\_PNC\_NO\_COMMUNICATION进入到COMM\_PNC\_REQUESTED阶段。

如果是被动唤醒的节点，则根据接收到唤醒报文中的PNC位状态切换到COMM\_PNC\_READY\_SLEEP或者COMM\_PNC\_PREPARE\_SLEEP。其中PNC位设置一般在NM的报文中体现，而开发者只需根据相应的NM报文的UserData中对应的PNC位操作即可。

而COMM\_PNC\_FULL\_COMMUNICATION内部的三个子状态的切换也是根据该节点的是否能被动唤醒功能进行内部的状态切换，主要体现是主动唤醒下需要Request Full相关的操作以及NM报文中对应的UserData中相关的PNC位进行转换的。

**03**

**ComM 通道 状态管理**

ComM 通道有三种模式，其中除 COMM\_SILENT\_COMMUNICATION 之外每种模式有两种子状态：

COMM\_NO\_COMMUNICATION（无通信模式，不接收也不发送。）

* COMM\_NO\_COM\_NO\_PENDING\_REQUEST（无网络请求状态。）
* COMM\_NO\_COM\_REQUEST\_PENDING（有通信请求 ，但未使允许通信 标志ComMAllowed。）

COMM\_FULL\_COMMUNICATION（全通信模式， 既可接收也可发送。）

* COMM\_FULL\_COM\_NETWORK\_REQUESTED（网络请求状态。）
* COMM\_FULL\_COM\_READY\_SLEEP（准备睡眠状态。）

COMM\_SILENT\_COMMUNICATION（静默模式， 接收但不发送。）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaArvF7ia49wazQBNTGRfdq4Mj3rTZ8jN6lYB00CK5iaqGKI8DHqfiaRlT2WAefiazuibxgYiauJ6yagdZAslZZlOga7JibJabsU05Cdn8/640?wx_fmt=png&from=appmsg)

来源：CSDN博主「up up day」

https://blog.csdn.net/m0\_56208280/article/details/130580453

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255...