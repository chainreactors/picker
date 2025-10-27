---
title: 来了，Frida源码情景分析
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484681&idx=1&sn=d483b2bd75fa9273c787c28c89f30cc3&chksm=fcdd0504cbaa8c12e35f0efd013230e933029c0b467692c35b903f9a89bfc80266d037f41f41&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2024-10-22
fetch_date: 2025-10-06T18:51:59.261430
---

# 来了，Frida源码情景分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8Pxqz0ScUFaSVEX25qQqkAn6MKMJURVEggILVDkibPGVHVBiaHicC9Gcxg/0?wx_fmt=jpeg)

# 来了，Frida源码情景分析

非虫

软件安全与逆向分析

Frida工具自从作者创建以来，已经走过了15个年头，始终受到软件安全领域工作者的热爱与追捧。近年来，Frida在安全对抗方面的应用可谓是移动安全领域最热门的话题之一。个人在2021年尝试开发了一个名为strong-frida的项目，随着安全对抗技术的不断升级，我决定深入研究Frida的整体框架及其内部实现细节，以便向那些前辈学习他们的思路与实现方法。

这个研究过程将是一个庞大的工程，我深知许多朋友也曾有过类似的计划，但由于种种原因，目前市场上并没有一份完整的、系统化的资料可供参考。因此，我愿意主动尝试，勇敢地踏上探索Frida这条大河的旅程。学习与探索的过程往往是枯燥且充满挑战的，需要一步一步扎实地推进。我希望能成为朋友们学习路上的一只小舟，在尽可能节省大家宝贵时间的同时，分享Frida这条小河上那些未知的故事与经验。

在这个过程中，我将记录下我的学习心得、遇到的困难以及解决方案，将整个学习计划分成三季的视频内容来展开。希望能够为其他有志于探索Frida的朋友提供一些参考和帮助。让我们一起在这条充满未知与挑战的道路上，携手前行，共同成长。

课程大纲设计如下：‍‍

* 设定第一季：构建系统与语言基础篇 讲vala语言基础，Frida构建系统以及项目里面的python、nodejs、c、vala等项目的动态调试。
* 设定第二季：Linux系统篇，讲frida-core、firda-gum、devkits、frida-tools等工具的组件接口实现。
* 设定第三季：安卓系统篇，讲各组件工作流程以及在安卓上特定实现的细节，讲hook内幕，frida js调试等。

  ‍

下面是Frida整体项目图，框中的三个部分就是将要探索的领域。‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8zZkgGQDKp3cbw8XuZ1EoajlhefiaBIqDaJV13uPBogIcib3QunTickwjQ/640?wx_fmt=png&from=appmsg)

Frida安全对抗肯定是很多朋友最想关注的内容。有老学员建议将检测点的讲解放到视频内容中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8REZib7ctIcMjF1oLqWib1iblnJzmLKwBI2oFfgDGlEBlpINMukTbSAOxw/640?wx_fmt=png&from=appmsg)

这个是必须要安排进去的！

课程里面涉及到Python、Bash、JavaScript、C、Vala等多种编程语言的开发与调试。整个开发环境采用目前最流行的devcontainers实现课程讲解与学员使用的环境的统一。对于学员关心的问题，只要是能够实现的内容，都会优先安排。有老学员问是否会涉及Linux上的C开发。‍‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v895ZiaVKPRLVibflV9bc096JtoEkkGyknmJ1ibzRF6PM6YosmibicxFUsjUQ/640?wx_fmt=png&from=appmsg)

这个是肯定的，各种语言的开发调试与代码讲解，是整个系列内容的核心所在。‍

课程内容不是简单的代码讲解，为了能够理解整个项目的框架，需要绘制各种组织架构图、时序图与活动图。‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8k5zBKIKCb7rDEYLNWgWdibEVZ1VoaqiaRedqSKHf4oOn6kS2b55W4wnQ/640?wx_fmt=png&from=appmsg)

还有一些代码，使用活动图方便实现的，就会使用活动图来绘制，比如编译流程。‍‍‍‍‍‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8adEicicGZjgM3fC44U4jwkMcD2EotdX9s3096x6FH4WF64lYzhSXf4SA/640?wx_fmt=png&from=appmsg)

还有很多在流程上方便使用时间线展示的，使用时序图来绘制。‍‍‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8zW0y4vh0V3trS4qDkoyWJemias3MJE2UpumthHhDa6hOAr6QQuxpwCg/640?wx_fmt=png&from=appmsg)

课程中的一些学习参考资料都是英文的，为了保证大家能够学会看懂，这里也专门花时间翻译了文档，一起提供给大家。‍‍‍‍

**根据大家的阅读习惯，提供了中文翻译版本与中英对照版本！**‍‍‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8N5zmIvnBqkib8Jk3dTvFGkHZO7G4R2ibdXrb04sbQcNRHn5F5OPJXGqQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnbSoMJr69sfUcSTWMGiae6v8ibpSOGhibmQbtnB2NSoxIRibeBpyGcibHntRbI3kvuWAysYt7VmznkoGtA/640?wx_fmt=png&from=appmsg)

课程计划双11当天开更。价格计划每季600元，全三季1800元。**目前早鸟报名活动价格全三季800元。联系微信feicongcn购买。**双11开更涨价。‍‍‍

点赞、转发、在看、评论本条内容的朋友，购买课程再送软件安全知识星球一年。‍‍‍‍

课程目录更新动态见：

https://github.com/feicong/ebpf-course

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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