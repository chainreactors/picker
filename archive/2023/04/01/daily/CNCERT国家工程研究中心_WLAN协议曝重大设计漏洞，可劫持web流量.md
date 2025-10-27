---
title: WLAN协议曝重大设计漏洞，可劫持web流量
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535857&idx=2&sn=7401706bdf553ed90faa559a63525b15&chksm=fa93fa30cde4732660061de45a0a635075eae6285fffe32986cd22d01da897fbc7f0658afda4&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-04-01
fetch_date: 2025-10-04T11:24:36.853261
---

# WLAN协议曝重大设计漏洞，可劫持web流量

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lKa7J8hhicfibgDneGggvibfgs3jguRA6icjgibrCOE91r1wPpWhVFns2k8eFnnxr1mhJfoMr3qvmBTlA/0?wx_fmt=jpeg)

# WLAN协议曝重大设计漏洞，可劫持web流量

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176lKa7J8hhicfibgDneGggvibfgbErDU4FShOg3ygZofDDI7WwyGZpfyxl8vSUe1KVziaXTvrHUO8ic99hA/640?wx_fmt=png)

东北大学的网络安全研究人员在IEEE 802.11无线局域网协议标准中发现了一个设计漏洞，攻击者可欺骗接入点以明文形式泄漏网络帧。

WLAN帧是由标头、数据有效负载和尾部组成的数据容器，其中包括源和目标MAC地址、控制和管理数据等信息。这些帧按队列排序受控传输，以避免碰撞冲突，并通过监视接收点的忙/闲状态来最大化数据交换性能。

研究人员发现，排队/缓冲的帧缺乏安全保护机制，攻击者可以操纵数据传输、客户端欺骗、帧重定向和捕获。

“该缺陷可以用来劫持TCP连接或拦截客户端Web流量，影响范围极大，包括各种设备和操作系统（Linux，FreeBSD，iOS和Android）”东北大学的Domien Schepers和Aanjhan Ranganathan以及imec-DistriNet的Mathy Vanhoef在昨天发表的技术论文中写道。

# **省电不省心**

IEEE 802.11标准包括节能机制，允许WiFi设备将发往休眠设备的帧进行缓冲或排队，以此来节省电力。

当客户端站（接收设备）进入休眠模式时，它会向接入点发送一个带有包含节能标头的帧，此后所有发往它的帧都将排队。客户端站唤醒后，接入点会取消缓冲帧的排队，对其加密后传输到目标。

但是，该标准没有提供有关管理这些排队帧的明确安全规范，也没有设置限制，例如缓冲帧可以在此状态下停留多长时间。

攻击者可以假冒联网设备的MAC地址，并将节能帧发送到接入点，将发往目标的帧排入队列。然后，攻击者发送唤醒帧以获取排队帧堆栈。

传输的帧通常使用组寻址加密密钥（在WiFi网络中的所有设备之间共享）或成对加密密钥进行加密，该密钥对于每个设备是唯一的，用于加密两个设备之间交换的帧。

但是，攻击者可以通过向接入点发送身份验证和关联帧来更改帧的安全上下文，从而强制其以明文形式传输帧或使用攻击者提供的密钥对其进行加密。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZ9g7dusvalVibNdA8jf0HfLnh7oEU3KiaibO7bvutetnqSI7h17JUAvZ3gxRFL235agVazRiaxjpw3Bw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

实施该攻击需要使用研究人员开发的名为MacStealer的自定义工具，该工具可以测试WiFi网络的客户端隔离绕过，并在MAC层拦截发往其他客户端的流量。

研究人员报告说，Lancom、Aruba、思科、华硕和D-Link的以下网络设备产品受到这些攻击的影响，完整列表如下：

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZ9g7dusvalVibNdA8jf0HfL7Mp2R79m8WVrotuacgaqx0XuwHYNIL8yQnUialKHboIYZfRaFo2lkrA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

研究人员警告说，该攻击可被用来将JavaScript等恶意内容注入TCP数据包。

“攻击者可以使用自己的互联网连接服务器，通过假冒发件人IP地址的路径外TCP数据包将数据注入TCP连接，”研究人员警告说：“这可以被滥用，以明文HTTP连接向受害者发送恶意JavaScript代码，目的是利用客户端浏览器中的漏洞。”

虽然这种攻击也可以用来窥探流量，但由于大多数网络流量都是使用TLS加密的，因此影响有限。

该攻击的技术细节可在USENIX Security 2023论文中找到（链接在文末），该论文将在今年五月份的BlackHat Asia大会上发表。

# **思科承认中招**

首个承认受WLAN协议漏洞影响的厂商是思科，它承认论文中的攻击可能适用于思科无线接入点产品和具有无线功能的Meraki产品。

但思科认为，检索到的帧不太可能危及安全防护得当的网络的整体安全性。

“这种攻击被视为机会主义攻击，攻击者获得的信息在安全配置的网络中价值不是很高。”

话虽如此，但思科仍建议采取缓解措施，例如通过思科身份服务引擎（ISE）等系统使用策略执行机制，该系统可以通过实施思科TrustSec或软件定义访问（SDA）技术来限制网络访问。

思科还建议“实施传输层安全性，以尽可能加密传输中的数据，因为这会使攻击者无法使用获取的数据。”思科安全公告中写道。

**参考链接：**

https://papers.mathyvanhoef.com/usenix2023-wifi.pdf

原文来源：GoUpSec

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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