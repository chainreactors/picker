---
title: G.O.S.S.I.P 阅读推荐 SHARK
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499308&idx=1&sn=a0f71ad0178efa08f392030314dd475f&chksm=c063d0f5f71459e3932b6f80c0a952c521a41c353db38ae6b30324240e5d138565b1ce966f87&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-12-05
fetch_date: 2025-10-06T19:39:11.757001
---

# G.O.S.S.I.P 阅读推荐 SHARK

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiaefWia3177QYI3sKr7CiatHox8AcamibKrAiciaZTU6hx2PxYnhaGSzQlWpA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 SHARK

原创

王绍江@SYSU

安全研究GoSSIP

12月第一次给大家送上“G.O.S.S.I.P和朋友”系列，这次的论文推荐介绍的是中山大学南雨宏老师研究团队和来自印第安纳大学（IUB）、阿里巴巴和复旦大学的多位研究人员合作完成的论文Leaking the Privacy of Groups and More: Understanding Privacy Risks of Cross-App Content Sharing in Mobile Ecosystem，论文发表于2024年的NDSS会议上，主要聚焦于移动端生态中**跨应用内容分享**的隐私泄露问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiafQR9gicaLp9KnGVnGr8kRZmEyHnhZIAIOkBayJujnBNX6DG26icoPc9g/640?wx_fmt=png&from=appmsg)

跨应用内容分享是指在移动应用中将内容（如抖音的短视频、知乎的推文）分享转发至其它社交应用或平台（如微信、钉钉）的功能。随着智能手机的广泛普及，在当前移动互联网生态中，跨应用内容分享已经成为各类应用中必不可少的基础功能之一，下面的图片展示了一个典型的跨应用内容分享过程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeia0nAzZn2Gich2icficDM53xYibHIxDuaS8bHwZGtFLNQnGz0XgtPT3ZuXtw/640?wx_fmt=png&from=appmsg)

相信大家都在日常生活中使用过应用的内容分享功能吧，内容分享怎么会和隐私泄露扯上关系呢？实际上，有些应用的分享功能可能在我们分享给好朋友一些内容的时候还会分享一些额外的信息，这些信息在应用后台暗潮汹涌地流动，可能在不知不觉中就被有意或无意间泄露了出去。可能看到现在你还是一头雾水，那就让我接着看看这篇论文所披露的问题，你可能就会对内容分享过程的隐私泄露有一个更加清晰的理解，下面让我们进入正题。

这篇论文首次从用户隐私角度，探索了移动端分享功能技术实现的背后是否存在潜在的隐私泄露隐患，以及如何检测对应这样的隐私泄露行为。论文围绕跨应用内容分享提出以下四个研究问题：

（1）内容分享过程中是否存在隐私泄露问题？

（2）若存在隐私泄露，那么受害者和获益者分别是谁？以及对应的泄露模式是怎样的。

（3）若发生隐私泄露，获益者可以获得受害者的哪些敏感信息？

（4）如何设计通用的工具/方法对目前移动端内容分享的隐私泄露模式进行检测？

**隐私泄露模式**

针对上述四点问题，作者在论文中提炼出三种在跨应用内容分享过程中可能存在的隐私泄露模式：

模式1. 应用自身窃取用户社交关系（SBT，Sharing Behavior Tracking）：分享内容的本质是分享链接，应用通过往链接中嵌入用户的唯一id标识符来追踪用户的分享链。例如用户A分享抖音视频链接到微信/钉钉，抖音会往视频链接中插入用户A的唯一id。当链接被用户B在微信中打开时，抖音可以根据链接中的id将用户A和用户B进行关联，从而获取用户A和用户B为社交好友这个信息，下图展示了此隐私泄露模式的大致流程。已有工作已经证明了社交好友关系信息的隐私性和重要性，因此，这个隐私泄露模式是对社交好友关系的一个补全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiaxBdp52I3la7dYenxKX0bIiaj0yMtuZyQxWx30GibIcQc6ORWDOLnKpZw/640?wx_fmt=png&from=appmsg)

模式2. 应用或内嵌第三方SDK服务收集用户分享内容（SDI，Sharing Data Interception）：跨应用分享功能的实现应遵循最小数据原则，即收集的数据应只用于满足功能需求。但在研究中发现，第三方SDK服务在实现跨应用分享功能的同时将用户的分享内容进行了收集，比如下图中截取自实际应用的代码片段中，一个用来分享内容的接口除了实现将内容分享到微信的功能之外，实际上还包括将分享内容发送到应用自己的服务器。而此类数据收集并非用户实现分享功能，因此存在隐私泄露行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiaKEX7CS0hlLic0RLyIxTHJB9S48pDjSWHSgDZDON2UJnxUtaUbFBoZdg/640?wx_fmt=png&from=appmsg)

模式3. 内容接收者获取发送者隐私（SDE，Sharer Data Exposure）：有些分享链接中可能不仅仅只有用户希望分享的内容，还包括用户的其他隐私信息。比如下面所展示的例子中，当用户A从抖音分享视频链接给微信/钉钉的用户B，用户B可以通过这个链接中的id信息定位到用户A的抖音号。有了抖音号之后，用户B只需要简单的修改一下访问链接就能轻松访问到用户A的个人主页，从而对用户A进行监控或画像等行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiaIRLzK6ajJYNv3HUDr6icumlFPWQnwMoXzicwB4xgyhENjwS7O7dd8EXQ/640?wx_fmt=png&from=appmsg)

**隐私泄露检测工具：Shark**

上面所提到的三种隐私泄露模式确实存在于一些软件中，不利于我们的软件生态发展，那有什么好的办法可以验证应用是否存在这些隐私泄露模式呢？这篇论文的研究人员给我们带来了一款检测工具——Shark。这个工具利用动静态结合的方式来检测应用是否存在上述的隐私泄露模式，下面是这个工具的工作流程和设计上的简单介绍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiagGRx1MYk6M5T7iaGsQAQRTzNd0rsnEhcaiaezBQsAAeegkuTHb3szPYA/640?wx_fmt=png&from=appmsg)

观察Shark的工作流程图，我们不难发现Shark包含三个模块分别完成三个目标：应用分享功能识别与定位（Static Information Extraction）、触发分享功能完成跨应用分享（Dynamic Sharing Activity Triggering）、实时监控流量进行隐私泄露确认（Leakage Detection）。只需要将待测试的应用输入到这个工具中，Shark就会根据这三大模块对这个应用进行检测，然后输出结果，那么这三大模块是怎么实现的呢？

首先、Shark会利用静态分析技术来提取应用在运行时触发内容分享所需的关键信息。更具体地说，Shark 会解析应用的反编译程序代码和用户界面资源文件，以定位共享按钮和这个按钮所在的用户页面。然后，Shark 构建界面转换图，其中包含一组可行的候选路径，以触发和完成内容分享的可行路径候选集。界面转换图会记录在一个内容分享的过程中，内容源应用和目标应用之间所经历的各个页面的信息来作为内容分享的候选路径。以下图展示的分享过程为例，这个分享过程从触发分享过程的界面开始，到完成内容分享一共经历了四个不同的界面，只需要知道这4个界面的信息我们就能知道分享应用的全过程。因此下面所展示的界面转换图为：Sharing Activity -> SelectPlatform Activity -> SelectFriend Activity-> Finish Activity

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiaZvXr8dQA7wb4NibibCwDGNBNAVNswiaGVupdV1D8hF35VyS8CyjZseHvQ/640?wx_fmt=png&from=appmsg)

此外，Shark采用后向数据流分析来跟踪与共享内容相关的变量。这样，它就能准确地在源应用程序和目标应用程序的共享按钮之间建立源应用程序和目标应用程序的分享按钮之间的联系（即哪个按钮指向微信，哪个按钮指向 Facebook）。

在动态运行时，Shark会打开应用程序，并根据静态分析所收集到的信息触发内容分享活动。同时截取具体的与内容分享相关数据及其暴露上下文（如发送目的地、参数等），并将它们传递到泄漏检测模块，以确认在内容分享的过程中是否存在之前提及的三种隐私泄露模式。

在泄露检测模块中，为了检测应用是否存在上述三种隐私泄露模式，Shark的研发人员巧妙的制定了三种不同的规则，确认应用程序是否确实存在隐私泄漏。例如，针对模式1所展示的隐私泄露模式，Shark采用了差分分析来识别共享链接是否确实包含用户可识别信息。当不同用户共享相同内容时共享相同内容时，无论用户身份如何，携带共享内容的链接都应保持一致。换句话说，如果在测试过程中，不同的用户共享的相同内容共享但是产生的分享链接不同，那这可能就存在隐私泄露风险。其他两种隐私泄露模式的介绍在论文也有详细的提及，感兴趣的小伙伴可以点击文末的链接进行研究。

**实验设置与检测结果**

为了验证上述三种隐私泄露模式的流行程度，这篇论文的研究人员还进行了一个实验：从中国和美国的应用市场上各收集了150个最受欢迎的应用作为测试对象，将其作为Shark的输入。最终实验结果显示，中国150个应用中有120个应用存在分享功能，其中有67/120 (55.82%)至少存在一种隐私泄露模式，美国150个应用中有66个应用存在分享功能，其中有8/66 (12.12%)至少存在一种隐私泄露模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoicAZJIJxaYibYYVdw4hdeiaOD4YfFkXb2ib3lyR7ynD0TianY1HfU0hSAhD5DuWRdKbicicInSYBqCc6g/640?wx_fmt=png&from=appmsg)

通过比较两个不同国家应用程序的隐私泄露实例数量，我们不难发现在中国的应用程序中，比例相对较高。作者进一步调查显示，其中一个原因是因为美国的应用程序没有集成两个第三方内容分享相关的SDK。

作者指出，上述的隐私泄露模式不仅仅是安卓软件所独有的特性，在iOS系统上的应用程序也可能面临着上述的隐私泄露风险。对于至少有一种上述隐私泄漏模式的 Android 应用程序，作者也获得了其相应的 iOS 版本（如果有的话），在所有 74 个有问题的安卓应用程序中，有 71 个应用程序具有相应的 iOS 版本。通过手动拦截和检查收集到的网络流量，作者发现至少 58/71 个应用程序（81.69%）的应用程序的iOS版本也有这些隐私泄漏模式。在 iOS 应用程序中如此普遍的在 iOS 应用程序中如此普遍的隐私泄漏现象并不奇怪，这是因为平台在实现跨应用分享内容方面的基本技术相似。

**对抗方法**

这些隐私泄露模式对抗起来还是挺难的，不过作者也针对不同的群体给出了不同的意见和建议来对抗这些隐私泄露模式。

对于应用程序用户来说，尤其是对隐私敏感的用户可以截图并直接分享内容图片。这样，分享的内容就不用通过分享链接的方式来实现，因此内容分享将变得不再可追踪。不过，鱼和熊掌不能兼得，这种方式也难免会因为额外的操作而降低用户体验；

对于系统供应商来说，内容分享机制依赖于系统框架的支持（如安卓系统中的 Intent）来提供跨应用程序的共享链接，系统供应商有可能拦截共享链接并过滤掉暴露用户身份的参数。然而，这种机制并不是万能的因为对手可以采取额外措施，在自己创建的 URL 中隐藏用户身份。

对于监管机构和应用市场来说，可以采取更多切实可行的对策。具体来说，监管机构和应用市场都可以明确规定应用开发商应如何遵守有关用户共享数据的隐私设计惯例。此外，应用市场还可以采用额外的审查机制来识别此类数据分享机制，这样可以降低隐私泄露的风险。

对于这些隐私泄露模式，你有什么看法？感兴趣的小伙伴可以去研究论文原文来发现更多的细节~

---

论文：https://www.ndss-symposium.org/wp-content/uploads/2024-138-paper.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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