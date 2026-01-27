---
title: G.O.S.S.I.P 阅读推荐 2026-01-26 以“包”之名
url: https://mp.weixin.qq.com/s/JmPGL14s6F7vS_aVgDRv3A
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:35:18.333897
---

# G.O.S.S.I.P 阅读推荐 2026-01-26 以“包”之名

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5SnrEW8A5c3yia51iciayGCiaaJloicsQCfxaHWpSvsW6q045bJgSURNjByQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-01-26 以“包”之名

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

在2025年IEEE S&P会议上的论文 *Born with a Silver Spoon: On the (In)Security of Native Granted App Privileges in Custom Android ROMs* 中，作者介绍了一种新的安全问题：在厂商定制的ROM中，一些并非system level的第三方APP也拥有了特殊的“地位”，同时攻击者可能滥用这种特权来实施伪造APP身份的关联攻击：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5y83AficDKzysVicfrjYcYXIJyCtVu1bUmpQHaV7bJAH9jrBpCrDriazjA/640?wx_fmt=png&from=appmsg)

在很长一段时间内，大家研究厂商定制的ROM，基本上都聚焦在那些system APP的安全问题上，很少有人关注那些第三方的APP，不过最近几年随着超级APP的垄断逐渐形成（你手机上连微信、支付宝、抖音、小红书这种APP都一个没有吗？）厂商也不得不“屈服”于给它们“开后门”，这就是本文作者提出的新概念——**I**mplicit **T**rust **A**pp vulnerability（ITA vulnerability），那么这种ITA漏洞的本质是什么呢？

先来看下面这个对比实验，作者先开发了一个叫做`com.tencent.application`的APP，安装测试了一下，发现“在其他APP上方显示”这个功能是关闭的；然后作者把这个包名改成了微信的包名`com.tencent.mm`，在某个特定的手机上安装，咦？怎么自动就获得了“在其他APP上方显示”的权限（没有手工去申请，也没有用户授权）？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5ZvxagAB7KiaAfNZeHvVMLEsoKZCX4YeD7bEg2XKuDwHzkCMf9n7KKhg/640?wx_fmt=png&from=appmsg)

看到这里，聪明的读者大概明白了，ITA漏洞是针对一些定制化的Android系统在某些针对APP的认证过程中，仅使用了包名（package name）来作为过滤器，给特定的APP预制了特定的权限的问题。这种问题的成因可以从系统的代码里面看到，嗯，下图这个例子（政治不正确，还在使用Whitelist这种词）就是一个典型的只检查APP的包名而不去检查开发者的签名的情况（当然，检查签名这个代码就太复杂了）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5hHIff0zibM5lyLd3YDR1meOxCjEtpO8rMbGqN0wqWfFDf5TGOx8tZMA/640?wx_fmt=png&from=appmsg)

在另一个定制的Android系统中（在网上随手一搜应该是三星的定制系统），直接为`com.alipay.security.mobile.authenticator`这个APP开了绿色通道，允许它在任何情况下都不用经过反病毒检查（下图）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5JIWfIy3hZahLRPhRx20zG86iaW61oBmuWnk7Oqiar0c1FkseEbYz1aqQ/640?wx_fmt=png&from=appmsg)

好，理解ITA漏洞并不难，可是怎么在整个Android系统这么复杂的代码中去寻找这一类特定的问题呢？作者首先假设这种“走后门”的行为一般只针对热门的APP（哼哼当然懂的都懂，还有某些APP是不允许讨论的也会在此列），所以分析的时候作者就只关注了应用市场上的Top 100 APP（Google和国内），分析ROM里面的关键代码有没有对这些APP的包名做特殊处理：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5LDTDbH2LUnbNjfesHEwvibtgNrIk3iastLGwA3OQ2rNJiaUTxYu8qicVgQ/640?wx_fmt=png&from=appmsg)

具体到分析步骤上，整个工作的基础还是用了很标准的Soot + FlowDroid的静态分析，在系统的代码中去寻找和关键的包名对应的string变量，然后做相关的数据流分析。当然这篇2025年的研究论文只是粗粗地使用了一些LLM，不像今年的各种论文（包括投稿）里面LLM满天飞。作者用了一个70亿参数的Mistral-7B-Instruct-v0.2模型，在数据流分析发现了可能的ITA漏洞之后，把相关的代码上下文发给模型去进行root cause分类（如下表，分为六类）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5GOUcObkCvicVNhVRT9tO9ocyers3bgicChkGrcyFJo0RJboT93sw4cWg/640?wx_fmt=png&from=appmsg)

在实际的实验环节，作者针对46家Android OEM厂商的686个定制的ROM进行了分析，找到了3078个潜在的ITA漏洞，作者表示这个太多了，只能手工抽取5%（也就是154个）来验证，结果作者表示没有任何的FP！当然这个分析并没有直接给出PoC去验证，只是检查了整个针对包名的判断流程里面有没有其他的验证，如果没有，就认为这是一个ITA漏洞。

我们先可以看看针对所有发现的问题，哪些厂商最坑（不能多说，又要引发口水战了）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia54udvE8ZYjmB8Jxd3jExcza2XicmgibmykFr8YqJichazicpHHqfo0VdHhg/640?wx_fmt=png&from=appmsg)

不用看也能知道哪个APP是后门之王，那就是~~老登必备的~~微信APP！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia5PaX73Rjc0X24yFOaMwjuKmP9equdM6nJlbFlDNDU3pBMGfBUrftoVg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia50XOMsqiaYAQ1KicT8jBLQoh4YOL6m2untgQ4VYARKiczkMzmK4gSf2GuA/640?wx_fmt=png&from=appmsg)

比较有意思的是作者也比较了同一个OEM厂商在不同机型上引入的ITA漏洞的数量的差别：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia54y4gKVq5YMN5AtRd1TchdwWIVVAxWia5FG0TNws4CYB5Y4sVRr98jrg/640?wx_fmt=png&from=appmsg)

实际上在case study环节的内容更有意思，不过涉及到的厂商都比较敏感啊，我们考虑了一下算了还是不说了，大家去看论文原文吧！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GAZrYcfoZPlfP3hHC2vBia55hJegaGexREialQNvu11n2YBIib1O2bIWhluU5cj6ZUlZguQJ8Agtavg/640?wx_fmt=png&from=appmsg)

---

> 论文：https://ieeexplore.ieee.org/document/11023417 （鄙视IEEE，人家ACM都免费了）

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