---
title: 一条短信即可完全控制设备！工业物联网设备中广泛使用的调制解调器容易受到短信攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247544530&idx=1&sn=b47001ef41824f465b4319f26f93d9e9&chksm=fa939813cde41105e167c4bc55fcd44949d612fdac0ace8f68db2315b7445573376146fea89a&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-05-12
fetch_date: 2025-10-06T17:17:10.948721
---

# 一条短信即可完全控制设备！工业物联网设备中广泛使用的调制解调器容易受到短信攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kH5VDsO3Zq3zpxnXedcdjsdBGFibfy95kmlXprmcYm266R5yxTUJNQbzIhhM9uZzhuo2hvYEghc3g/0?wx_fmt=jpeg)

# 一条短信即可完全控制设备！工业物联网设备中广泛使用的调制解调器容易受到短信攻击

网络安全应急技术国家工程中心

2023年11月，卡巴斯基ICS CERT部门的安全研究人员披露了有关elit Cinterion蜂窝调制解调器的一组8个独立的漏洞，其中7个的标识符为CVE-2023-47610或CVE-2023-47616，另一个尚未注册。Telit Cinterion蜂窝调制解调器广泛应用于工业、医疗保健和电信等行业，其安全缺陷可能允许远程攻击者通过短信执行任意代码。在公布安全问题之前，安全公司已于2023年2月向供应商报告了这些问题。本周六（5月11日），在柏林举行的OffensiveCon会议上，亚历山大·科兹洛夫(Alexander Kozlov)和谢尔盖·阿努弗里科(Sergey Anufrienko)将提供有关安全问题的低级技术细节，以及威胁参与者如何利用这些技术来控制易受攻击的Telit Cinterion设备。为了演示远程危害调制解调器的可能性，研究人员开发了自己的基于短信的文件系统，他们通过SUPL消息处理程序中发现的漏洞将其安装到调制解调器中。基于此，研究人员可以远程激活Over The Air Provisioning，在调制解调器上安装任意MIDlet，使用制造商提供的标准机制可以保护MIDlet不被移除，但需要调制解调器固件的完全反射来擦除它。根据这项研究的发现，研究人员计划于2024年5月发表一份关于调制解调器安全的白皮书。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icVBUeiaqKOwRgdFdZv3C3dibd6jJ8LkicWtlHEU3RETFE8IezaknleYjzEftYxd1QZDW6liaph1nYYBibg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

调制解调器漏洞简介

卡巴CERT在漏洞通告中称，Telit Cinterion BGS5、Telit Cinterion EHS5/6/8、Telit Cinterion PDS5/6/8、Telit Cinterion ELS61/81、Telit Cinterion PLS62中存在CWE-526：通过环境变量暴露敏感信息漏洞，该漏洞可能允许本地、低特权攻击者可以访问目标系统上的敏感数据。简要漏洞描述如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVBUeiaqKOwRgdFdZv3C3dibdficxpCQYYZU9f8LQX4k6dvVIAWAut7FAxkUibQIpeQzLQnbnduSicpvRg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVBUeiaqKOwRgdFdZv3C3dibdnPicZhxfs2CcPdVnE9d2QvkgOibf3xstm8OKAYlyHGsgekr0VAbq4kvw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

例如， CVE-2023-47611允许通过绕过数字签名验证以提升的权限执行代码，这对数据机密性和设备完整性构成威胁。CVE-2023-47610威胁最大，攻击者可以使用特制的短信激活该漏洞，并在未经身份验证的情况下在调制解调器上远程执行代码。

一条短信即可实现设备接管

在这八个漏洞中，最严重的一个漏洞是CVE-2023-47610，这是一个影响调制解调器的用户平面位置(SUPL)消息处理程序的堆溢出问题。

卡巴斯基与Telit合作，基于对技术细节的全面分析，给它打了8.8分(满分10分)。然而，NIST的评估是，该问题具有关键影响，并获得了9.8分的严重分数。

通过特别制作的短信利用该漏洞的攻击者可以触发该漏洞，并在调制解调器上远程执行任意代码，而不需要身份验证。

在与BleepingComputer分享的一份报告中，研究人员表示，短信界面存在于所有调制解调器上，如果知道手机运营商网络中的目标调制解调器的用户数量，就有可能访问它。

他们解释说，运营商的限制有时可能会阻止发送二进制短信，但假基站应该绕过这一限制。

通过利用CVE-2023-47610通过短信执行任意代码，攻击者可以获得对调制解调器操作系统的深度访问。

“这种访问还促进了RAM和闪存的操作，增加了完全控制调制解调器功能的潜力——所有这些都不需要身份验证或需要对设备的物理访问”——卡巴斯基。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVBUeiaqKOwRgdFdZv3C3dibdmejjKTTIql65upkicibV2ANGpU2h2H97Sc2ByfA3B0xvFGlk9g1DcQ1A/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

两位研究者即将进行的公开演讲《One SMS to Root Them All: Exposing Critical Threats in Millions of Connected Devices》-一条短信搞定所有：暴露数百万连接设备的严重威胁。

影响评估

尽管卡巴斯基研究人员发现的其他漏洞的严重性得分较低，但它们可以被用来损害具有各种功能的基于midlet的Java应用程序的完整性。

根据卡巴斯基的说法，攻击者可以通过绕过数字签名检查(CVE-2023-47611)以更高的特权(制造商级别)实现代码执行。这不仅会对数据机密性和完整性构成威胁，还会对更广泛的网络安全和设备完整性构成威胁。

虽然研究的目标是Cinterion EHS5-E系列调制解调器，但由于该供应商的其他产品具有类似的软件和硬件架构，其他型号设备也受到影响:

Cinterion BGS5

Cinterion EHS5/6/7

Cinterion PDS5/6/8

Cinterion ELS61/81

Cinterion PLS62

卡巴斯基告诉BleepingComputer, Telit修复了一些已发现的漏洞，但有些仍未打补丁。

卡巴斯基ICS CERT负责人叶夫根尼•冈恰洛夫(Evgeny Goncharov)表示:“我们发现的漏洞，加上这些设备在各个行业的广泛部署，突显了全球大规模破坏的可能性。”

卡巴的安全措施及建议

Goncharov指出，由于调制解调器嵌入到其他解决方案中，因此确定哪些产品受到影响是一个挑战。

这家安全公司有一些建议来减轻威胁，这些建议通常是通过与电信运营商合作来实现的。一种策略是禁止向受影响的设备发送短信，并使用安全配置的私有APN。

卡巴斯基还建议强制应用程序签名验证，以防止在调制解调器上安装不受信任的MIDIets，并采取措施防止未经授权的物理访问设备。

**参考资源：**

1.https://www.securitylab.ru/news/548123.php

2.https://www.bleepingcomputer.com/news/security/widely-used-modems-in-industrial-iot-devices-open-to-sms-attack/

3.https://www.offensivecon.org/speakers/2024/alexander-kozlov-and-sergey-anufrienko.html

4.https://ics-cert.kaspersky.com/vulnerabilities/

原文来源：网空闲话plus

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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