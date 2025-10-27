---
title: 当心！新型Android银行恶意木马软件--Brokewell的新进化及其对用户的威胁
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492195&idx=1&sn=305cf0d4dd5d0caa1b1cfee7e7869b07&chksm=e90dc849de7a415fd43cb727f8ddca9242961638fb6d546b556eb3562efc17987091b5e3c807&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-05-16
fetch_date: 2025-10-06T17:17:39.783353
---

# 当心！新型Android银行恶意木马软件--Brokewell的新进化及其对用户的威胁

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 当心！新型Android银行恶意木马软件--Brokewell的新进化及其对用户的威胁

BaizeSec

白泽安全实验室

**一、事件摘要**

随着移动银行业务的普及，针对移动设备的恶意软件也在不断进化。最近，ThreatFabric的研究人员发现了一种名为“Brokewell”的新型Android恶意软件，该软件具备数据窃取和远程控制功能，能够绕过Android 13+的安全限制，并通过各种手段进行传播。研究人员还发现该木马似乎正在积极开发更新，几乎每天都会添加新命令。在分析研究的过程中，他们发现了另一个可以绕过Android13+ 限制的下载器。该下载器由同一行为者开发，并已公开发布。攻击者并不是试图隐藏其源代码存储库，其中一台用于命令和控制的服务器还托管了一个名为“Brokewell Cyber Labs”的存储库，由“Baron Samedi”创建。它包含旨在绕过Android 13+限制的Android加载器的源代码。研究人员指出，该款木马会对银行业用户构成了重大威胁，因为它允许攻击者远程访问通过银行应用程序提供的所有资产。

**二、攻击技术分析**

最初，研究人员发现了伪装成浏览器更新的一个页面，该页面旨在安装一个Android应用程序。乍一看，这并没有什么不寻常——伪装成浏览器更新是网络攻击者用来诱使受害者下载和安装恶意软件的常见方法，对于毫无戒心的受害者来说，这种方法看起来是无害的（有一个精心制作的页面，推广软件新版本的更新），并且看起来也很自然（因为它发生在正常的浏览器使用过程中）。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOhDJRWiadfYshywbfJ5TMjiaT7GD75TibU9OiaCsZk3h8mVreCmhbfgSCF53tfWmlWcgBLiamibJo5HdYA/640?wx_fmt=png&from=appmsg)

图 1 伪装浏览器更新示意图

然而，分析表明下载的应用程序是一个以前未见过的恶意软件家族，具有广泛的功能。 此外，回顾性分析显示，该恶意软件家族之前针对流行的“立即购买，稍后付款”金融服务和奥地利数字身份验证应用程序发起了攻击活动。

Brokewell使用了覆盖攻击，这是Android银行恶意软件的常见技术，它在目标应用上叠加一个伪造的屏幕以捕获用户的凭据。此外，Brokewell还可以窃取cookies，这是现代移动银行恶意软件的另一个常见特性。它通过启动自己的WebView，覆盖onPageFinished方法，并加载合法的网站来实现这一点。一旦受害者完成登录过程，Brokewell就会转储会话cookies，并将它们发送到命令和控制（C2）服务器。

此外，Brokewell配备了“可访问性日志”，可以捕捉设备上发生的每一个事件：触摸、滑动、显示信息、文本输入和打开的应用程序。所有操作都会被记录下来，并发送到命令和控制服务器，有效地窃取了在受控设备上显示或输入的任何机密数据。需要强调的是，在这种情况下，任何应用程序都有数据泄露的风险：Brokewell会记录每一个事件，对设备上安装的所有应用程序构成威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOhDJRWiadfYshywbfJ5TMjiaOQZovtwYJkxQG8wyWzb2McNFC53MmB3xgCg2C26MicpE6ibicQVRIS9Dw/640?wx_fmt=png&from=appmsg)

图 2  攻击代码示意图

这种恶意软件还支持各种“间谍软件”功能：它可以收集有关设备的信息、呼叫历史记录、地理位置和录制音频。在窃取凭据后，攻击者可以使用远程控制功能发起设备接管攻击。为了实现这一点，恶意软件执行屏幕流，并为攻击者提供一系列可以在受控设备上执行的动作，如触摸、滑动和点击指定元素等。

研究人员调查发现，这些攻击者并没有试图隐瞒他们的身份：在其中一台用作Brokewell的命令和控制（C2）点的服务器也被用来托管一个名为“Brokewell Cyber Labs”的存储库，该存储库由“Baron Samedit”创建。此存储库包含“Brokewell Android Loader”的源代码，这是同一开发人员的另一个工具，旨在绕过Android 13+对旁加载应用程序的辅助功能服务的限制。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOhDJRWiadfYshywbfJ5TMjiaia5NFaWZfQMxQ3InrPjMFeiarW8nHdR1pqlFlK7iaf8h1UIkJRNbicXDFA/640?wx_fmt=png&from=appmsg)

图 3 代码存储库示意图

这种情况将对威胁形势产生重大影响。首先，更多的攻击者将会轻松获得绕过Android 13+限制的能力，这表明可能成为大多数移动恶意软件家族的一个常规功能，类似于读取短信消息。其次，目前提供此功能作为独特功能的现有“Dropper-as-a-Service”产品可能会关闭其服务或尝试重组。这将进一步降低了希望在现代设备上分发移动恶意软件的网络攻击者的进入门槛，使更多的网络攻击者更容易进入该领域。

最后，对“Baron Samedit”档案的进一步调研分析显示，他们至少活跃了两年。然而，该攻击者此前曾向其他网络攻击者提供过工具，以检查来自多个服务的被盗账户。随着“Brokewell Android Loader”的推出及其公开可用性，“Baron Samedit”已经转向移动恶意软件，这表明网络犯罪分子对这一领域的兴趣日益增加。

**三、总结**

新发现的恶意软件家族Brokewell，它从零开始实现了设备接管功能，这突显了网络攻击者对此类功能持续的需求。这些攻击者需要这一功能才能直接在受害者的设备上进行欺诈，对于严重依赖设备识别或设备指纹识别的欺诈检测工具来说，这构成了一个重大挑战。预计这个恶意软件家族将会进一步演变，因为研究人员已经观察到恶意软件几乎每天都在更新。另外，Brokewell恶意软件很可能会作为租赁服务在地下渠道推广，吸引其他网络犯罪分子的兴趣，并引发针对不同地区目标的新活动。还有，像Brokewell这样的恶意软件家族对金融机构的客户会构成了重大风险，导致难以在没有适当欺诈防护措施的情况下被成功欺诈。

参考链接：

https://cybernews.com/security/android-banking-malware-remote-control/

https://www.threatfabric.com/blogs/brokewell-do-not-go-broke-by-new-banking-malware

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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