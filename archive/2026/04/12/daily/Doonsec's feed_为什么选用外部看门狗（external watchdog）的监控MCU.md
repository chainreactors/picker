---
title: 为什么选用外部看门狗（external watchdog）的监控MCU
url: https://mp.weixin.qq.com/s/I1-5clCFrc1SpaviRivXzQ
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:55:09.393943
---

# 为什么选用外部看门狗（external watchdog）的监控MCU

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCFyYKvokMkXe3XQgj57iaSn1IL4OsgzK9ibOBDoHojloyWpyKweMSQfCibMMRNNfdMQeJF7LpMANrsmTw6IrWp14Yvz7K0RdtTbs/0?wx_fmt=jpeg)

# 为什么选用外部看门狗（external watchdog）的监控MCU

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于开心果 Need Car
，作者开心果 Need Car

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7xmZWjMxkpzia4Ft2qUbKVib3waicn3vUKRjoL8iaKrC191A/0)

**开心果 Need Car**
.

号主：开心果 Need Car，主要从事汽车Autosar开发，公众号主要分享 通信、诊断、存储、网络管理、标定、Bootloader等工程开发问题。致力于将学到的知识，分享给更多的Autosar从业者，努力解答一线开发工程师的困顿！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

在MCU的嵌入式开发中，不同的控制器有着不同的功能安全目标要求。但是 ，当讨论看门狗（watchdog）的时候，我们常常会感到困惑，比如：对于MCU的监控（monitor），为什么需要使用外部看门狗呢？使用内部看门狗不行吗？

讨论这个话题，我们先从功能安全目标说起，示意如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB0JwmEEm0YsUE9mvoBibvicg8iclib23uQSBibqJhNBiafSvZQ4TyC88T5wm5O1iaN2WDJuZ1KF9agVgxynMhKR2P4w3e3V4no9a6U8c/640?wx_fmt=png&from=appmsg)

**首先**，设定的安全目标（SG，Safety Goal）是：**MCU失控不等导致危险行为**。

**其次**，根据SG设计功能安全要求（FSR，Functional Safety Requment）：系统必须监控MCU时钟和程序执行异常。

**再次**，针对FSR设计技术安全要求（TRS，Technical Safety Requment）:**必须使用一套独立于MCU的监控机制**。

**最后**，落实TRS，即：选用外部窗口看门狗进行MCU的时钟和程序执行监控。

这里延伸一下，MCU内部也有看门狗（internal watchdog），使用MCU内部的看门狗监控MCU时钟和程序执行异常不可以吗？回答这个问题，我们就得从两者功能的区别谈起。

**01**

**内部看门狗和外部看门狗的功能区别**

内部看门狗和外部看门狗的功能区别如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC1abQL8SmyaaoL0Y6xPxfHkicWuzDU6BWpgP6WwXNaUHhuZEPic8fokjLpNribKf8qzIhZ5DqOLZvl7pcicKicgW38VyialgA8TmQCM/640?wx_fmt=png&from=appmsg)

**Note**：RC(Resistor‑Capacitor Oscillator，电阻‑电容振荡器)

如上表，由于内部看门狗不能监控MCU主要时钟的停振/频偏等异常，所以，这无法满足功能安全目标。所以，从这个角度，使用内部看门狗是不合适的。

那么，内部看门狗就真的不能用吗？不是，如果内部看门狗使用独立时钟，可以对MCU主时钟进行监控，进而满足MCU的SG要求，如此，可以使用内部看门狗监控MCU。但是，目前，**多数MCU芯片的MCU时钟和内部看门狗使用共源时钟，所以，内部看门狗也就无法监控MCU的时钟失效**。

**02**

**对看门狗理解**

首先，看门狗（watchdog）是一种安全机制（Safety Mechanism）。项目中，是否使用watchdog，以及使用哪种watchdog（external /internal watchdog）需要看产品设计的安全目标。

**(一)系统架构设计中的功能安全要求**

在做系统架构、功能安全概念设计时，对系统的安全等级通常要求如下：

* **ASIL A / ASIL B**

可使用MCU内部watchdog，视需求决定是否加外部watchdog

* **ASIL C / ASIL D**

强烈建议（几乎默认）**使用外部看门狗**作为**独立安全机制提升DC（diagnostic coverage）**，以**满足硬件架构指标**SPFM（Single‑Point Fault Metric）/LFM（Latent‑Fault Metric）。

所以，watchdog和系统要达到的安全目标关系应该这样理解：系统的安全要求来源自系统目标ASIL（Automotive Safety Integrity Level）。即：如果系统是ASIL D，那么**看门狗必须能满足ASIL D所需的性能**，比如：及时诊断程序执行顺序错误（program sequence failure）、时钟失效（clocking failure）等。**高ASIL系统**通常需要**独立监控，很多ASIL C/D 系统会使用外部看门狗以满足SG**。

ISO 26262-10（2018版）中，在系统级设计（system level design）中提到了这样一个假设：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAgd5oyRVw84DU5pT98Fus7A4OApiaF9ziczrxAroiaDE0Xbm1nUfJ1GTTicIm4iboQibic38kFA8PK7ZWfBh1QYc4GGibpOlk65G2TiaNs/640?wx_fmt=png&from=appmsg)

简而言之：系统层需要提供MCU外部的独立看门狗，**用于监控MCU运行时序是否正常**。也就是说，**这个假设的成立才能够在真实系统中满足对应的ASIL要求**。

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

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

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb362959dbcb159324b2593d70bce78d82a9&scene=21#wechat_red...