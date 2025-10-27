---
title: Encrypthub入侵了618个组织以部署InfoStealer勒索软件
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581351&idx=1&sn=66b7a795dc151391e050e2982bcbc22c&chksm=e9146e9dde63e78bf1ef7bed6f56bf43a79bb93e2f2794436da0150813b503cad177b22f48b1&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-03-01
fetch_date: 2025-10-06T21:59:30.232931
---

# Encrypthub入侵了618个组织以部署InfoStealer勒索软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJ4X6DbLpggj9tyCianerwJjWDBQb5ibTnxThrn1oS1xWZznQtibDkWIMXw/0?wx_fmt=jpeg)

# Encrypthub入侵了618个组织以部署InfoStealer勒索软件

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一个名为“EncryptHub”的威胁者（又名“Larva-208”），一直以世界各地的组织为目标，通过鱼叉式网络钓鱼和社会工程攻击来访问企业网络。

根据Prodaft上周在内部发布的一份报告称，自2024年6月Encrypthub启动运营以来，它已经攻击了至少618个组织。

在获得访问权限后，威胁者安装远程监控和管理（RMM）软件，然后部署像Stealc和Rhadamanthys这样的信息窃取程序。在许多观察到的案例中，EncryptHub也会在受损的系统上部署勒索软件。

据悉，该威胁组织隶属于RansomHub和BlackSuit，过去曾部署过这两家勒索软件加密器，可能是它们的初始访问代理或直接附属机构。

然而，在研究人员观察到的许多攻击中，攻击者部署了自定义的PowerShell数据加密器，因此他们也保留了自己的变体。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJV48KWl3nlM8bLKfY1QJcQyqAFCvEjdpGIGkYhF4j91iay2McuFHoT0g/640?wx_fmt=png&from=appmsg)获得初始访问权限

Larva-208的攻击包括短信网络钓鱼、语音网络钓鱼，以及模仿企业VPN产品（如Cisco AnyConnect、Palo Alto GlobalProtect、Fortinet和Microsoft 365）的虚假登录页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJ1I67RYDAmWt7Ye93VZEX2dkM8IMv2RxyVeTQo7mloFlHZ38brmYBpA/640?wx_fmt=png&from=appmsg)

假冒思科登录页面

攻击者通常在给目标的消息中冒充IT支持人员，声称VPN访问有问题或他们的帐户存在安全问题，指示他们登录到一个网络钓鱼网站。

受害者收到链接，这些链接将他们重定向到网络钓鱼登录页面，在那里他们的凭据和多因素身份验证（MFA）令牌（会话cookie）被实时捕获。

一旦网络钓鱼过程结束，受害者将被重定向到服务的真实域，以避免引起怀疑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJnJicUD7yqfy2OxejPQwsRZEZcAhQwiagSNfqQzxs3cTwu6l2JD2lcghw/640?wx_fmt=png&from=appmsg)

网络钓鱼过程概述

EncryptHub已经购买了70多个模仿上述产品的域名，如“linkwebcisco.com”和“weblinkteams.com”，以增加人们对钓鱼网页的合法性认知。

这些钓鱼网站托管在像Yalishanda这样的可靠托管提供商上，ProDaft说，这些提供商通常不会对合理的删除请求做出回应。

Prodaft还发现了另一个名为larava -148的子组织，他们帮助购买用于网络钓鱼活动的域名，管理主机，并建立基础设施。

Larva-148有可能向EncryptHub出售域名和网络钓鱼工具包，尽管它们之间的确切关系尚未被破译。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJV48KWl3nlM8bLKfY1QJcQyqAFCvEjdpGIGkYhF4j91iay2McuFHoT0g/640?wx_fmt=png&from=appmsg)恶意软件部署

一旦EncryptHub入侵目标系统，它就会部署各种PowerShell脚本和恶意软件来获得持久性、远程访问、窃取数据和加密文件。

首先，他们会欺骗受害者安装RMM软件，如AnyDesk、TeamViewer、ScreenConnect、Atera和Splashtop。这使得他们能够远程控制受损的系统，保持长期访问，并使横向移动成为可能。

接下来，他们使用不同的PowerShell脚本来部署信息窃取程序，如Stealc、Rhadamanthys和变幻无常的Stealer，以窃取存储在web浏览器中的数据。这些数据包括保存的凭据、会话cookie和加密货币钱包密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJeI7ib8Sw9QPHYs3fvZoTxEsCIWLGf5IQGXK5NwTGNKJsx0kib4rVPYBA/640?wx_fmt=png&from=appmsg)

攻击中使用的自定义PowerShell脚本

在Linux和Mac设备上执行类似行为的Python脚本中，威胁者试图从被破坏的系统中窃取大量数据，包括：

**·**来自各种加密货币钱包的数据，包括MetaMask，以太坊钱包，Coinbase钱包，Trust钱包，Opera钱包，Brave钱包，TronLink， Trezor钱包等。

**·**各种VPN客户端的配置数据，包括Cisco VPN Client、forticclient、Palto Alto Networks GlobalProtect、OpenVPN、WireGuard等。

**·**来自流行密码管理器的数据，包括Authenticator、1Password、 NordPass、DashLane、Bitwarden,RoboForm、Keeper、 MultiPassword、 KeePassXC和LastPass。

**·**匹配特定扩展名或文件名包含特定关键字的文件，包括图片、RDP连接文件、Word文档、Excel电子表格、CSV文件、证书等。目标文件名中的一些关键字包括“pass”，“account”，“auth”，“2fa”，“wallet”，“seedphrase”，“recovery”，“keepass”，“secret”等等。

Larva-208的最后一个威胁是以基于powershell的自定义加密器的形式出现的勒索软件，该加密器使用AES加密文件并附加“。加密”扩展名，删除原始文件。

受害者收到一封勒索信，要求用USDT通过电报支付赎金。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJAaC9kj36wyYmicvncOmeNEDqfG5bX5ujz1AZo9eMMcxKCxzV53icLeibQ/640?wx_fmt=png&from=appmsg)

Larva-208的勒索信

Prodaft表示，EncryptHub是一个老练的恶意分子，它会为提高攻击效率而量身定制攻击计划，对大型组织进行高价值的攻击。

本报告中研究的LARVA-208鱼叉式网络钓鱼行为表明，有针对性的网络攻击越来越复杂。通过采用高度定制的策略，先进的混淆方法和精心制作的诱饵，威胁者已经展示了逃避检测和破坏高价值目标的重要能力。

参考及来源：https://www.bleepingcomputer.com/news/security/encrypthub-breaches-618-orgs-to-deploy-infostealers-ransomware/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJB1fPiaXqgc1MwZVbKf7YsgfuUlkYnYlyOUKwJ5WTHR94lOCElWJh1pA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29fOTqJSIRDx7s6OnnW6ArJ9gFOX2icaL2kf5c86hFFaujAsiaqhndWrPI4LVUHFfCUsYKPe9ib5Kmug/640?wx_fmt=png&from=appmsg)

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