---
title: 研究人员发现两个未被披露的Linux后门
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492429&idx=1&sn=403e8e1d786edf29b4cc66d8d6f40d97&chksm=e90dc967de7a4071d76126dbd73a9fd99d881f00aca19723fe6f9e1617970d48bc78ab176dfc&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-24
fetch_date: 2025-10-06T19:16:02.457980
---

# 研究人员发现两个未被披露的Linux后门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 研究人员发现两个未被披露的Linux后门

BaizeSec

白泽安全实验室

网络安全厂商ESET研究人员近期发现了两个以前未知的Linux后门样本：WolfsBane和FireWood。这些样本被用于网络攻击活动，目标是窃取敏感数据，如系统信息、用户凭证以及特定文件和目录。这些工具旨在保持持久访问权限，并秘密执行命令，以便于在逃避检测的同时进行长期的敏感数据收集。

**WolfsBane分析：**

研究人员发现WolfsBane是Windows后门Gelsevirine的Linux对应版本，WolfsBane样本最初在VirusTotal上被发现，上传地点包括台湾、菲律宾和新加坡，很可能源自对被入侵服务器的事件响应。研究人员高度确信这些样本与Gelsemium组织有关，这是一个高级持续性威胁（APT）组织。Gelsemium组织此前曾针对东亚和中东地区的实体进行攻击，其已知历史可追溯至2014年。此前，尚未有公开报告称Gelsemium组织使用过Linux恶意软件。

WolfsBane是一个简单的加载链的一部分，包括投递者（dropper）、启动器（launcher）和后门（backdoor）。WolfsBane投递者模仿了合法的命令调度工具cron，而其启动器和后门则分别伪装成KDE桌面组件和udevd系统服务。在WolfsBane攻击链中，还包含了一个修改过的开源用户空间Rootkit。这意味着攻击者利用了开源的Rootkit代码，对其进行了修改，以适应他们的攻击需求。这种Rootkit存在于操作系统的用户空间，并能够隐藏其活动，使得防御者难以检测到攻击者的行为。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOQiclJw3euPakzuxImr2msOFQamUuicoa0JyFPNLe1ruicwDfWiarrUsWQNXqCXghnZ54JO0LPoG6LtA/640?wx_fmt=png&from=appmsg)

图 1 WolfsBane感染链

**FireWood分析：**

研究人员还发现了另一个Linux后门FireWood。然而，研究人员无法确定FireWood与Gelsemium组织工具之间的联系，其在分析的报告中的出现可能是巧合。因此，研究人员对FireWood归因于Gelsemium组织的信心较低，但与一个被研究人员追踪的名为Project Wood的后门有关。研究人员追溯分析到2005年，并观察到它演变成更复杂的版本。该后门曾在Operation TooHash事件中被使用过，在事件分析的报告中还包含几个额外的工具——主要是webshells，这些工具一旦安装在被入侵的服务器上，就允许攻击者远程控制。

研究人员通过对比WolfsBane和FireWood与Gelsemium之前使用的Windows恶意软件的相似性，确定了这些Linux后门的归属。分析发现，这些后门在网络通信、命令执行机制、配置结构和域名使用上与Gelsemium的历史活动有显著相似之处。研究人员指出，APT组织越来越多地关注Linux恶意软件，这一趋势可能与Windows电子邮件和端点安全性的改进有关。随着端点检测和响应（EDR）工具的广泛使用，以及微软默认禁用Visual Basic for Applications（VBA）宏，攻击者正在寻找新的攻击途径，特别是针对互联网面向系统的漏洞，其中大多数系统运行在Linux上。

参考链接：

https://www.helpnetsecurity.com/2024/11/21/linux-backdoors-wolfsbane-firewood/

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