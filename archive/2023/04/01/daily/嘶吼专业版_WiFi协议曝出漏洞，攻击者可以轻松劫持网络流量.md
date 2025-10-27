---
title: WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247559413&idx=1&sn=6ef1e8bfc555f0bad13f9da67ca6ad71&chksm=e91438cfde63b1d978cad62067f34df4e8270a6dd8542a85213ec057919253235a8b7bd26323&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-04-01
fetch_date: 2025-10-04T11:24:30.153307
---

# WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPpKwHc3PgDSRTvfibQrypqKDjj8LNWvPMCMn4xzkX1GWhV9lm2iabv1Hw/0?wx_fmt=jpeg)

# WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPibPOj8KVDpvUEiaAiamDvlzZwqjX5qlK7icSiapROoib41VlEf0ATPomrsAA/640?wx_fmt=png)

网络安全研究人员近日在IEEE 802.11 WiFi协议标准的设计中发现了一个基本的安全漏洞，这个漏洞让攻击者可以诱骗接入点泄露明文格式的网络帧。

WiFi网络帧如同数据容器，由报头、数据载荷和报尾组成，含有源和目的地MAC地址、控制和管理数据之类的信息。

这些帧在队列中排序，在受控制的材料中传输以免碰撞，并通过密切关注接收端的繁忙/空闲状态来最大限度地提升数据交换性能。

研究人员发现，队列/缓冲帧并没有得到充分的保护，攻击者可以采取多种手段：操控数据传输、客户端欺骗、帧重定向和捕获。

美国东北大学的Domien Schepers和Aanjhan Ranganathan以及比利时鲁汶大学imec-DistriNet的Mathy Vanhoef在昨天发表了一篇技术论文《对帧做手脚：通过操控传输队列绕过WiFi加密机制》，他们在论文中写道：“我们的攻击有其广泛的影响，因为它们可以影响各种不同的设备和操作系统（Linux、FreeBSD、iOS和安卓），还因为它们可以用来劫持TCP连接或拦截客户端和互联网流量。”

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)节电漏洞

IEEE 802.11标准包括节电机制，允许WiFi设备通过缓冲或队列发给睡眠模式设备的帧来达到节电效果。

当客户端站（接收设备）进入睡眠模式时，它向接入点发送一个帧，该帧的报头含有节电位，因此发给该接入点的所有帧都进入队列。

然而，该标准并没有为管理这些队列帧的安全性提供明确的指导，也没有设置限制，比如帧可以在这种状态下逗留多长时间。

一旦客户端站由睡眠模式进入工作模式，接入点将缓存的帧从队列中取出，采用加密，并将它们传输到目的地。

攻击者可以欺骗网络上设备的MAC地址，并向接入点发送节电帧，从而迫使它们开始将发送给目标的帧列入队列。然后，攻击者发送唤醒帧来检索帧堆栈。

传输的帧通常使用在WiFi网络中所有设备之间共享的组地址加密密钥或成对加密密钥进行加密，这个加密密钥对每个设备而言都具有唯一性，用于加密两个设备之间交换的帧。

然而，攻击者可以通过向接入点发送验证帧和关联帧来改变帧的安全上下文，从而迫使接入点以明文形式传输帧或使用攻击者提供的密钥对其进行加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPCYuOLzK0iclO0Riaa0AD1LgoZPkIViaL5x2DtM2T4RFMEfqcEongKSFpQ/640?wx_fmt=png)

图1. 攻击图（图片来源：papers.mathyvanhoef.com）

这种攻击可以使用研究人员创建的名为MacStealer的自定义工具来实现，该工具可以测试WiFi网络的客户端隔离旁路，并在MAC层拦截发给其他客户端的流量。

研究人员报告，来自Lancom、Aruba、思科、华硕和友讯的网络设备型号已知受到这些攻击的影响，完整的设备列表如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPuMhM5791icdRScw11GFWs92MdlL6tRc3x9XwuHdVia67tiaonITB4xwxQ/640?wx_fmt=png)

图2. 测试后发现易受攻击的设备（图片来源：papers.mathyvanhoef.com）

研究人员警告，这些攻击可能被用来将JavaScript等恶意内容注入到TCP数据包中。

研究人员警告：“攻击者可以使用他们自己的与互联网连接的服务器，通过注入带有受欺骗的发送者IP地址的路径外TCP数据包，将数据注入到这个TCP连接中。”

“比如说，这可能被用来通过明文HTTP连接向受害者发送恶意JavaScript代码，目的是利用客户端浏览器中的漏洞。”

虽然这种攻击也可以用来窥视流量，但由于大多数互联网流量都是使用TLS加密的，因此造成的影响有限。

技术细节和研究内容可在USENIX Security 2023论文中获得（https://papers.mathyvanhoef.com/usenix2023-wifi.pdf），该论文将于2023年5月12日在即将召开的黑帽亚洲大会上发表。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)思科承认漏洞

第一家承认WiFi协议漏洞影响的供应商是思科，它承认论文中概述的攻击可能会成功攻陷思科无线接入点产品和具有无线功能的思科Meraki产品。

然而思科认为，检索到的帧不太可能危及适当安全的网络具有的整体安全性。

思科声称：“这种攻击被视为伺机作案的攻击，攻击者获得的信息在安全配置的网络中几乎没有多少价值。”

不过，该公司还是建议用户采取缓解措施，比如通过思科身份服务引擎（ISE）等系统使用策略执行机制，该系统可以通过实施思科TrustSec或软件定义访问（SDA）技术来限制网络访问。

思科的安全公告写道：“思科还建议尽可能实施传输层安全，以便对传输中的数据进行加密，因为这将使攻击者无法使用获取的数据。”

目前，还没有有人恶意利用研究人员发现的漏洞的已知案例。

参考及来源：https://www.bleepingcomputer.com/news/security/wifi-protocol-flaw-allows-attackers-to-hijack-network-traffic/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPnU2MhrhCF0mrypTJPLNYMSZBreJa6rEU1wFAh2pxrFl23L1B7AiaR4A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPZjibEQkItGhIjkhwkiabRqwfSFLibfdJOKloneXgJ4NBUEFnRicoSruxXg/640?wx_fmt=png)

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