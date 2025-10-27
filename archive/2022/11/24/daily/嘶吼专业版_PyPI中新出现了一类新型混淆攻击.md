---
title: PyPI中新出现了一类新型混淆攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247554118&idx=2&sn=34b05fbe5e21d7c0b5db62a30956a32d&chksm=e915c47cde624d6ae8567e1d148330edddc5b223650b76968b1964aa12e8fd54493e283412a0&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-24
fetch_date: 2025-10-03T23:39:43.274438
---

# PyPI中新出现了一类新型混淆攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATevdIxeLzGn3pqFS7bATKCHTba2vDB5F2XBeBvkAobGaKJCojReEbCaQ/0?wx_fmt=jpeg)

# PyPI中新出现了一类新型混淆攻击

xiaohui

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

针对恶意包的新型混淆技术可以在图像中隐藏代码。

Check Point 研究团队最近在PyPI上检测到一个新的、从未见过的恶意包，PyPI是Python编程语言的软件库。恶意包被设计用来隐藏图像中的代码(基于图像的代码混淆——隐写术)，并通过Github上的开源项目感染PyPI用户。这些发现反映了攻击者严密的攻击计划，证明了PyPi上的混淆技术已经进化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATewibEMgZJAMeubGD0Q6vHSyibNbSQjY5aqiauYmAaLXQcOL8ricsblKxOYA/640?wx_fmt=png)
   常见恶意软件包结构

开源域上的恶意软件包通常包括3个主要组件：

恶意代码：负责下载和运行病毒可执行文件，向攻击者打开远程shell，或者只是收集并发布它能找到的所有PII。

运营商代码：负责注入恶意代码。通常，它将是一个合法的包，其中包含作为安装代码一部分的恶意代码段（如PyPI中的setup.py或NPM中的安装后脚本）。运营商代码通过混淆处理被隐藏，或者可以在安装过程中从诸如pastebin.com之类的源动态下载。

感染软件包：首先吸引受害者安装恶意软件包，一种常见的技巧是与普通合法名称相似的包名。

攻击者通常会仔细命名包名称。选择过于普通的包名可能会导致恶意应用程序被快速检测到(对PyPI用户具有很高的可见性)。选择一个小众名称可导致包的下载量较少，这将降低成功感染的潜在数量，需要开发商通过积极与潜在用户接触，让他们安装受感染的包来填补这一空白。在大多数情况下，攻击者似乎喜欢规模化攻击，即模仿常见的包名，假设高下载量将保证至少发生一些感染，即使潜在的软件包寿命更短。有些情况包括更独特和更重要的恶意代码设计选择。Apicolor似乎使用的就是该方法，它有一个小众且不受欢迎的软件包，但会积极尝试让GitHub用户安装该应用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATewibEMgZJAMeubGD0Q6vHSyibNbSQjY5aqiauYmAaLXQcOL8ricsblKxOYA/640?wx_fmt=png)
   Apicolor

Check Point 研究团队检测到的恶意包名为“apicolor”。乍一看，它似乎是PyPI上许多开发包中的一个。它是相当新的，最初发布于今年10月31号，有一个大致的描述和一个混淆的标题，说明这是一个“REST API的核心库”。普通恶意包的观察者几乎不会注意到这些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATe8djDKqEvpiaRZQtm9gu5XurDauWv9pAJjhhg1382jn0AcmIwvpL2eicQ/640?wx_fmt=png)

在深入研究了包安装脚本之后，研究人员注意到开头有一个奇怪的、重要的代码部分。它首先手动安装额外的需求(不是通过更常见的需求部分)，然后从web下载一张图片，使用新安装的包处理图片，并使用exec命令触发处理生成的输出。代码片段与我们通常在一般setup.py安装脚本中看到的代码片段有很大不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeNiadnt6vZtW6DUicVz1YicibgYJmxOC7Iuj3YrJSHy1DW3icIOXT0daRiajA/640?wx_fmt=jpeg)

手动安装的两个包是request(API使用中非常流行的帮助包)和judyb。judib包的细节最初看起来像一个“正在进行中”的包，有一个空的描述和一个混淆的标头，说明这是“一个纯Python judyb模块”。深入研究发现，judyb与apicolor首次发布的时间大致相同。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeDCLiatyIN7gxFeJ6LUicvicmNImWuhOuiacupadxZR8xS9LhpNwnxHInhA/640?wx_fmt=jpeg)

judyb代码原来是一个隐写术模块，负责隐藏和揭示隐藏在图片中的信息。研究人员怀疑在apicolor安装过程中下载的图像可能包含其内部的隐藏部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeDprHKMYeaUSX3WyVUjska6iaRqLzI0B0RQMkgO4lmvCaBLpb64eBriaQ/640?wx_fmt=jpeg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeOxkeCv6iakUiaibLIURlgD47XpWfnmR9fRuWDfBhQ2vsLc440Lpa8uEqQ/640?wx_fmt=jpeg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATe45RQic6kQ1xr9ia1tBzhfEeIu4EFzxLVsZqlibyavXUTWz5NyI9b4t6icw/640?wx_fmt=jpeg)

现在回到apicolor安装代码，第一步是观察从网上下载的图片。这似乎是合法的，没有什么异常。

将judyb的“揭示”方法应用于这张图片，显示了一条隐藏的信息，从该图像中发现。该消息似乎包含一个base64混淆的Python代码，这是恶意软件包隐藏其恶意代码的常用做法。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATekrf8icWyktPsyWN7NBdcdO44UQ1GYt7yWqxCxXO0IhtWiaicWuiaymJZ5g/640?wx_fmt=jpeg)

使用base64对该代码段进行去混淆处理揭示了我们非常熟悉的常见恶意代码模式；从web下载恶意exe并在本地运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeicfd8sLEwOnLmBEn25pn198PUMljUPpgbqb1icNEoVrZJjCJjUzvqcbA/640?wx_fmt=jpeg)

在发现apicolor软件包的恶意和载体部分后，接下来就应该介绍如何安装这些软件包以及这些感染是如何被引发的？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATewibEMgZJAMeubGD0Q6vHSyibNbSQjY5aqiauYmAaLXQcOL8ricsblKxOYA/640?wx_fmt=png)
   主动感染

研究人员搜索使用这些包的代码项目，使团队能够进一步了解它们的感染技术及进程。通过这一搜索，很明显apicolor和judib非常小众，在GitHub项目上有少量使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATer6LP5Y7Kx68ibt6WpIW8oPF3ERQuhChKDcT7f6CWBeXibTY3oewiamibDw/640?wx_fmt=jpeg)

只有三个GitHub用户似乎在他们的代码中包含了这些包。将它们作为(超级冗余的)需求添加到其公开可访问的GitHub项目中。不出所料，这三个用户都是GitHub的新用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATe1oXWrKuI0jJc3L5ZTURGDdMWO6KyibnPTq3bnEYewkb94q9bYAXe1XQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATebG40wczbCpp5KeVdr9umZAzAjDLROULwZxymy9YorlvBFJ4lF8fc9w/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeyVRFD3g4jDHg0ULaZdhRJDmeAtibqL0NPm4sLa4KIaX69f8Y4AKZIAA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATewibEMgZJAMeubGD0Q6vHSyibNbSQjY5aqiauYmAaLXQcOL8ricsblKxOYA/640?wx_fmt=png)
   隐性感染

感染过程如下：

当用户在网上搜索合法的项目时，会遇到这些GitHub开源项目，并在本地安装它们，他们并不知道其中含有恶意的包。需要注意的是，代码似乎有效。在某些情况下，存在空的恶意包。从安装程序的角度来看，他们正在尝试一个来自GitHub的开源项目，并不知道其中隐藏了恶意木马程序部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeicL9mzs3dAdblGLURZEld3mzNalyyQw1jfAgxGicarAiaSRG5JACZL4zw/640?wx_fmt=jpeg)

细心的用户只会考虑热门的开源项目，而上述项目似乎符合这一标准。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeyOfukSr5FFXMEZdwjuug0g5I1nJ323mIpjqhcTK01tG1MDzFhWD5hQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeenQxwU8JAibOBcakRHtLj7A5wFBbHgJXVg8rLWibZtK2fbltgse1IUrQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATewibEMgZJAMeubGD0Q6vHSyibNbSQjY5aqiauYmAaLXQcOL8ricsblKxOYA/640?wx_fmt=png)
   向PyPI披露

一旦这些包被识别出来，Check Point Research就会提醒PyPI它们的存在，之后PyPI就会进行删除。

供应链攻击 旨在利用组织和外部方之间的信任关系。这些关系可能包括合作伙伴关系、供应商关系或使用第三方软件。攻击者会破坏一个组织，然后向供应链的上游移动，利用这些受信任的关系来访问其他组织的环境。近年来，这类攻击越来越频繁，影响也越来越大，因此开发人员必须确保自己的操作安全，反复检查正在使用的每个软件成分，特别是从不同存储库下载的软件，尤其是那些不是自己创建的软件。

研究人员发现了一种新型的有组织的攻击，他们不仅会模仿一个常见的包，隐藏其恶意代码，还会直接针对特定类型的用户组织发起攻击，将感染阶段从高度关注的PyPI平台转移到GitHub，这使得检测此类恶意包变得更加困难。

参考及来源：https://research.checkpoint.com/2022/check-point-cloudguard-spectral-exposes-new-obfuscation-techniques-for-malicious-packages-on-pypi/

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29IPtCG50icBxktc5rzaIhdSc0JhHibksQzb1ibmicTa6v6FZwFfAeqmJzpTIuKqzbLGWPjtRn4rwUEXg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeYeIEa4OiaFXguSm9haklicCrTSLR9c0vZDHpvSzBib5K2juybJoK9Jl5w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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