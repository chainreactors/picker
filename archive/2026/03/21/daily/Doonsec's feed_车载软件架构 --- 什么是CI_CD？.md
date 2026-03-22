---
title: 车载软件架构 --- 什么是CI/CD？
url: https://mp.weixin.qq.com/s/2aT2Xn-w_YXOXYJqjKy4cw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:15:52.884829
---

# 车载软件架构 --- 什么是CI/CD？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaC2mp9ibvw5k7uYHfWpb50vDdrUaVUQZAic7Epcbb8CxlAfOvKwN3ZCkgU5c51ibjNQlZsFvGFHGrqjCwAcfAfxVI46DnqYpcgbBI/0?wx_fmt=jpeg)

# 车载软件架构 --- 什么是CI/CD？

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于车载诊断技术
，作者穿拖鞋的汉子

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5zwxkqqC7HV2iauDhVtTha8cxdRypibjiae5GworkpzSkaw/0)

**车载诊断技术**
.

分享车载汽车电子技术WeChat：gongkenan2013

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**背景信息**

随着软件将车辆的安全性、舒适性和便利性提升到新的水平，开发人员现在需要比传统系统更现代、更强大的软件开发环境。这样的环境需要能够经常更新软件并在车辆上市后将这些更新部署到车辆上。这种方法叫做持续集成（CI）和持续部署（CD），简称CI/CD。

过去，软件开发遵循僵化、迟钝的瀑布法，并使用高度离散的工具链。开发过程被分割为不同的阶段，只有前一个阶段结束，后一个阶段才会开始。许多开发过程都需要手动完成。从工具链的一个部分切换到下一个部分也是如此。采用这种方法，推出新的软件版本需要耗时六到八个月。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwiclK22MRxrdibYAwykFdic8JJ3vQPajM2eK4dp0mkWjruRqrulUBjXED0icM5FIwtNX6dFIez2M7qM6A/640?wx_fmt=png&from=appmsg)

如今汽车行业力推的软硬分离架构为开发人员带来新的机会。他们可以使用现代化的敏捷方法及DevOps方法按照自己的时间计划来更新软件，速度更快且不受硬件更迭或其它物理更新的影响。这种方法可实现前所未有的在速度、可扩展性、质量和安全性方面水平的提升。

**02**

**什么是CI/CD?**

CI/CD是持续集成（Continuous Integration, CI）、持续交付（Continuous Delivery, CD）与持续部署（Continuous Deployment, CD，注意这里的CD对应了两个不同的概念）的简称。它是实现敏捷开发和DevOps理念的一种方法，通过持续自动化和持续监控贯穿于应用的整个生命周期（从集成和测试，到交付和部署）。

**1. 持续集成（Continuous Integration, CI）**

持续集成是一种软件开发实践，即团队开发成员经常集成他们的工作，通常每个成员每天至少集成一次，也就意味着每天可能会发生多次集成。每次集成都通过自动化的构建（包括编译、发布、自动化测试）来验证，从而尽快地发现集成错误。持续集成的主要流程包括：

-> 代码编译：将源代码编译成可执行文件或库。

->代码打包：将编译后的文件打包成可部署的单元。

->单元测试：对代码中的各个单元进行测试，确保每个单元按预期工作。

->代码静态扫描分析：对代码进行静态分析，检查潜在的错误、漏洞或不良编程实践。

->UI、接口自动化测试：对应用的用户界面和接口进行自动化测试，确保它们按预期工作。

持续集成的好处包括快速发现错误、防止分支大幅偏离主干、降低总体构建成本，并在开发周期的早期发现缺陷。

**2. 持续交付（Continuous Delivery, CD）**

持续交付是持续集成流程的扩展，它强调软件在持续集成的基础上，始终处于可部署的状态。持续交付的目标是拥有一个可随时部署到生产环境的代码库。在持续交付中，每个阶段（从代码更改的合并，到生产就绪型构建版本的交付）都涉及测试自动化和代码发布自动化。在流程结束时，运维团队可以快速、轻松地将应用部署到生产环境中。但需要注意的是，持续交付在自动化测试和集成结束后，具备部署的能力，但不会自动部署，而是手动部署。

**3. 持续部署（Continuous Deployment, CD）**

持续部署是持续交付的进一步延伸，它自动将应用发布到生产环境。由于在生产之前的管道阶段没有手动门控，因此持续部署在很大程度上都依赖精心设计的自动化测试。实际上，持续部署意味着开发人员对应用的更改在编写后的几分钟内就能生效（假设它通过了自动化测试）。这更加便于持续接收和整合用户反馈。

CI/CD集成于CI/CD工具及代码托管服务中，它让持续自动化和持续监控贯穿于应用的整个生命周期。这些关联的事务通常被统称为CI/CD管道（Pipeline），由开发、测试、运维团队以敏捷方式协同支持。CI/CD有助于降低应用的部署风险，提高开发效率，并加速软件交付周期。在现代软件开发中，CI/CD已成为不可或缺的一部分。

在持续集成（CI）方法中，软件将实现自动化编译，软件开发的各个步骤都将包含在 “CI链” 中，因为一个环节的输出将成为下一个环节的输入。持续部署（CD）指在车辆上市后自动部署新的软件版本。CI/CD以及持续测试（CT），现在都可以在汽车上实现，但在汽车行业，测试新的高级应用程序会造成独特的难题，原因是测试需要在实体车辆上或者在测试台上的复杂模拟环境中进行。例如，想象一下对特定软件进行测试有多复杂，该软件需要分析来自多个雷达和摄像头的输入信息，以便自主执行操控，如超过公路上慢速行驶的汽车，或者在车辆、行人及其它障碍物遍布的复杂城市环境中进行导航。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwiclK22MRxrdibYAwykFdic8JJJgGUap4KMoompwJyn3q5QWfm20O0sQAHm17xT06nn3libctGoA2wbNg/640?wx_fmt=png&from=appmsg)

理想的方法是通过基于云的集中化平台，使开发人员能够在位于世界任何测试中心的相关测试台上执行任何测试，从而消除开发和测试过程中的瓶颈。这些测试可以安排软件在环（SIL）、硬件在环（HIL）甚至车辆在环（VIL），以便进行更真实的测试。此方法可以利用全球资源，达到处理当今艰巨挑战所需的规模。

使用基于云的CI意味着，开发团队创建的新代码自动集成到更大的代码库中，基于云的CD使用无线（OTA）更新确保成功构建的代码自动部署到所在的测试或生产环境中。应用得当的话，基于云的方法还可以在整个过程中进行安全性编译，包括灾难恢复。托管在云中的集中式基础架构允许通过单一管理视图查看所有这些高度安全且有弹性的CI链。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwiclK22MRxrdibYAwykFdic8JJlDhib97x9bMFSnmemicMLDJjhCDQJ6wzlyobERUszlGOgDr2HCKA6Izg/640?wx_fmt=png&from=appmsg)

CI/CD 可自动执行以前将新代码从提交到生产所需的人工干预，因此可最大限度地减少停机时间，并加快代码的发布速度。而且，由于能够更快地将更新和更改集成到代码中，因此，可以更加频繁、高效地采纳用户的反馈意见，从而为用户带来积极的效果，客户的整体满意度也会有所提高。

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

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087...