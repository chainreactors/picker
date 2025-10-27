---
title: 工业物联网蜜罐、蜜网：一种重要的IIoT安全手段
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533693&idx=2&sn=8c103ab08bd4eef9f97c97ec82c5fefe&chksm=fa93f2bccde47baac47f6c068f8c42c869cacb50b1bd76eedf3be5218166b252e4d268a482ff&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-01-06
fetch_date: 2025-10-04T03:10:37.832232
---

# 工业物联网蜜罐、蜜网：一种重要的IIoT安全手段

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176ljBQiaZRCRkh03X2GkY1hIoniadZV6pFPWuBicAFvCVyKakYt1RYQv3vtqYOFRZ4Cls4P6QSnHx0KAQ/0?wx_fmt=jpeg)

# 工业物联网蜜罐、蜜网：一种重要的IIoT安全手段

网络安全应急技术国家工程中心

以下文章来源于中国保密协会科学技术分会
，作者熊思齐

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Jv1XiaqM8A25kZDJyDiaGNBs4WtH5KDf3q1td1IxdYfVg/0)

**中国保密协会科学技术分会**
.

及时发布官方科学技术前沿文章或观点、中国保密协会实时动态资讯、科学技术分会日常会议或活动信息，为中国保密协会科学技术委员及委员单位搭建便利的沟通平台。

**摘要：**工业物联网定义为利用工业通信技术将物联网技术应用到自动化领域。IIoT环境已经深入我们的城市、交通、制造业、基础设施等各个领域，同时IIoT也逐渐成为当今黑客发起攻击的热门目标。事实证明，蜜罐和蜜网对于了解和抵御对IIoT的攻击至关重要，它们可以吸引攻击者并欺骗其认为自己已获得了对真实系统的访问。蜜罐和蜜网可以与其他主流安全解决方案（防火墙、入侵检测系统IDS）形成互补，很好地对恶意行为进行防御。本文对面向IIoT的蜜罐和蜜网的研究进行介绍。

1、工业物联网及相似定义

工业物联网（IIoT, Industrial Internet of Things）的定义是利用工业通信技术将物联网技术应用到自动化领域【1】。与之相似的有两个概念：物联网和信息物理系统。

**1.1 工业物联网与物联网**

物联网（IoT, Internet of Things）是一个由互联网连接的设备组成的网络，如传感器、执行器和其他能够收集数据和进行通信的嵌入式设备。

根据定义，IIoT是IoT利用工业通信技术在自动化领域的应用，而物联网IoT作为工业物联网IIoT的基础，其应用深入我们生活的每个角落。传感器、执行器、可穿戴设备、嵌入式设备和许多其他IoT设备随处可见，建筑、城市、交通、汽车、制造业、关键(核反应堆、发电厂、炼油厂等)和非关键基础设施以及农业等各种环境中都有IoT的应用。

**1.2 信息物理系统**

信息物理系统（CPS, Cyber-Physical System）是由传感器、执行器、可编程逻辑控制器PLC、远程终端单元RTU、智能电子设备IED和其他嵌入式设备组成的网络，用于监测和控制关键和非关键应用领域中的物理过程。

CPS的应用场景包括但不限于工业控制系统ICS、智能电网、其他智能基础设施（如水、煤气、建筑自动化）、医疗设备和智能汽车【2】, 【3】。总的来说，IIoT因其工作环境的特殊性（封闭系统）而与CPS密不可分。

从定义上看，IoT、CPS和IIoT三个概念其实十分相似，并无太大区别。NIST的一份特别报告中指出，IoT和CPS的不同之处在于，IoT更强调物理世界中的信息与网络相关技术，而CPS更贴近于一种封闭系统实现，更侧重于感知和信息交换控制【4】。在上述基础上，IIoT因同时具有两者的特征而进一步连接了IoT和CPS的定义。

2、工业物联网蜜罐、蜜网

**2.1 常见的工业物联网安全机制**

为了保护IIoT环境下的工业设备，在工业网络中常采用多种网络防御手段，如密码学加密、使用防火墙、搭载入侵检测系统IDS和入侵防御系统IPS、采用防病毒和反恶意软件解决方案等。我国现行的工业无线网络规范国家标准定义的工业网络协议包含3层：物理层、链路层和应用层，它在安全管理上也采用了多种安全机制，如CCM\*加密模式（广泛应用于IEEE 802.x协议和BLE协议），配置基于时间戳和nonce的防重放攻击手段等安全机制【5】。

**2.2 传统工业物联网安全机制面临的挑战**

因IIoT环境的特殊性，对各设备在资源限制、网络寿命和QoS等方面有着独特要求，这也对IIoT环境的安全防御能力发出了巨大的挑战。IoT是IIoT的基础，IoT设备通常具有有限的电源、存储、计算和通信资源，这尤其在IIoT利用工业通信设备在自动化领域部署这一工作环境下，对其能采用的安全机制有着相当的限制。而另一方面，IIoT环境中使用的设备设计之初并没有考虑安全性。举例来说，在工业生产中，工业网络通常需要满足低时延、低功耗、高可靠性和高稳定性等要求，在这样的前提下，IIoT/CPS的应用环境都被认为是默认安全且孤立的。这种模糊的安全假设在2010年被广为人知的“震网”病毒打破。这个例子说明传统静态的“隐式信任”模型亟需重构革新，“零信任”在网络实施中的核心思想——去除隐式信任也同样是为解决这类问题而生。考虑到零信任相关技术、规范并未发展成熟，且本文主要对IIoT蜜罐和蜜网进行介绍，这里不对零信任原则过多赘述。随着越来越多的工业环境被连接到互联网，数十年不会更换的工业设备其安全机制的更新也已成为严重问题。

**2.3 蜜罐、蜜网及其在工业物联网的应用**

传统的IIoT安全机制对安全研究人员发现并分析攻击者攻击方式（以及防御应对）并不透明。蜜罐用以吸引攻击者并欺骗其认为自己已获得了对真实系统的访问，是一种以被攻击和可能被破坏为目的而使用的工具，而在一个系统上实现的两个或多个蜜罐组成一个蜜网【6】, 【7】。蜜罐可以与防火墙和IDS集成为IPS，以捕获攻击者的有关信息，研究他们的所有行为，并开发可以防止未来可能的攻击的安全方案。

实际使用时，蜜罐和蜜网可以部署在不同的位置，例如云计算环境、企业网络的隔离区 （DMZ区）、实际应用程序/生产环境（在IoT、IIoT或CPS网络中）以及具有公共 IP 地址的私有部署环境中，其基础蜜网架构如图1所示【8】。不同环境的选项有其自身的优点和缺点；此外，部署环境不同，最适合该环境的蜜罐或蜜网类型也不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtH5v9FiaLxFJ70hKKGJPGDSbYHQHlibrGrdHicL5xCBBhXI7BX10cj3plo0orDibnpQniaWvTZN8YWHXw/640?wx_fmt=jpeg)

图1 基础蜜网架构

IIoT的部署环境十分广泛，Javier等的研究将蜜网在IIoT的应用环境分为了6个大部分，分别为工业控制系统ICS、智能电网、水系统、燃气线路、楼宇自动化系统和综合IIoT蜜网，并从技术发展上对其进行了分类，图2是适用IIoT的蜜罐、蜜网分类，图3则描绘了IIoT蜜罐、蜜网的发展历史[8]。作为现有蜜罐的主要目标应用领域之一，一半以上的IIoT蜜罐都是针对ICS环境而设计。虽然针对特定IIoT应用的饵较少（大多数研究是针对ICS的），但类似的工业设备（如PLC）仍被ICS和智能基础设施（如电网、水、天然气）所使用。

![](https://mmbiz.qpic.cn/mmbiz_png/EWgMcLZQ4bQfFKdNicq1WdWfsu4bAiaWqsbwNgdf1ooOgORc7M92rqm6M8jJpGQ2uNlNKXepPtCibicrHPFtXQ4xibg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2 适用IIoT的蜜罐、蜜网分类

![](https://mmbiz.qpic.cn/mmbiz_png/EWgMcLZQ4bQfFKdNicq1WdWfsu4bAiaWqsNJ4qmB5iaIRAH1jW8jd9Jn22bYBS6qdKxiaXD6xjcibNpPYr1jQT2JjLQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3 IIoT蜜罐、蜜网的发展

IIoT蜜网始于2004年思科的SCADA HoneyNet项目。SCADA HoneyNet是基于Honeyd的开源蜜罐框架，是一个低交互蜜网，支持模拟在PLC上运行的Modbus/TCP、FTP、Telnet和HTTP服务。Berman在美国空军技术研究所发布的2012年的论文是在文献中针对IIoT蜜罐、蜜网进行的第一个研究，次年第二篇该领域论文同样是在美国空军技术研究所发布，而这两篇论文的发布时间正好对应于震网病毒的时代。2013年，史上最受欢迎的ICS蜜罐Conpot开源项目完成，Trend Micro Research的Wilhoit发布了他们的低交互ICS蜜罐白皮书，这也为后来大量的IIoT/CPS方向的蜜罐、蜜网研究实践注入了新的动力。

IIoT低交互蜜罐可以提供扫描、目标协议、攻击源和暴力尝试有关的有价值信息。另一方面，只有通过中/高交互蜜罐，才有可能发现并分析其他更高级的攻击、对具体工业协议及流程的攻击。IIoT高交互蜜罐允许攻击者对系统进行破坏，或利用蜜罐进行一些其他攻击行为，所以部署高交互蜜罐是一个很危险的行为，尤其是在IIoT这种具有特殊要求的环境，更不用说工业设备的高成本是IIoT蜜罐使用虚拟资源而非物理设备的最大驱动因素之一。

IIoT环境因其独特的要求和功能，使得包括蜜罐在内的安全工具，即使有着很先进前沿的研究，却始终难以在这些领域积极部署应用。就蜜罐的用途而言，大多数蜜罐和蜜网都只有着研究目的而没有生产目的。SCADA设备需要连续工作，能够中断和停机的情况少之又少。除此之外，工业设备一般有高度的时效限制，需要严格保证响应时间。因此，在未部署蜜罐的ICS生产环境中插入蜜罐，或对已被淘汰或版本落后的蜜罐进行更新是非常困难的，这些行为极大可能影响ICS通信，并对系统有破坏风险（高交互蜜罐）。

最常被用于在IIoT蜜罐、蜜网中检测/测试的攻击是扫描（scanning）攻击。大多数研究都对扫描攻击进行了不同时间周期的测试，这些蜜罐能统计扫描次数、进行流量分析、借助现有库判断扫描源合法性等。除了DoS和DDoS，SSH、暴力尝试和中间人攻击也是特定的蜜罐和蜜网环境中的重点检测对象。一些虽然没有上述攻击那么常见的，像勒索软件、挖矿后台等恶意软件和一些针对ICS的特定攻击，例如HAVEX RAT、PLC Blaster和tank overflow攻击也是防护重点。

Linux是蜜罐和蜜网主流的操作系统环境，除此之外还有FreeBSD。编程语言上，Python最为流行，C/C++和Java也有使用。这应该与这些语言有支持工业协议的库有关，例如Python有Modbustk、pymodbus和cpppo EtherNet/IP库；C/C++有libiec61850和OpenDNP3库；Java有JAMOD Modbus库[8]。Conpot蜜罐作为最流行的IIoT/CPS开源蜜罐，也是用Python编写的。

**2.4 总结与启发**

IIoT环境十分特殊，任何蜜罐/蜜网在开发之初，应考虑其目标应用领域、目的、成本、部署环境、所提供/模拟的服务、与攻击者预期交互程度、所消耗资源、所需工具、指纹识别性以及可能出现的实际责任问题等。此外，IIoT的蜜罐/蜜网从应用到部署，也需要事先进行多方面考量：例如对哪些具体应用、具体工业协议、部署在网络的位置、资源分配（如何保证工业生产通信、控制资源）等。

IIoT蜜罐/蜜网是一种重要的安全手段，该领域一直以来也是非常活跃的研究领域，如何将现有的前沿研究实际应用至生产环境，与其他安全手段配合，起到更好保护IIoT环境的作用，则是我们未来更需关注的部分。

（本文部分内容翻译修改自A Survey of Honeypots and Honeynets for Internet of Things, Industrial Internet of Things, and Cyber-Physical Systems (J. Franco et al. 2021)）

**参考文献：**

[1]  E. Sisinni, A. Saifullah, S. Han, U. Jennehag, M. Gidlund[C]. Industrial Internet of Things: Challenges, opportunities, and directions. IEEE Trans. Ind. Informat.. 2018(4), vol. 14, no. 11, pp. 4724-4734.

[2]  B. Bordel, R. Alcarria, T. Robles, D. Martín[C]. Cyber–physical systems: Extending pervasive sensing from control theory to the Internet of Things. Pervasive Mobile Comput. 2017, vol. 40, pp. 156-184.

[3]   A. Humayed, J. Lin, F. Li, B. Luo[C]. Cyber-physical systems security—A survey. IEEE Internet Things J. 2017, vol. 4, no. 6, pp. 1802-1831.

[4]  C. Greer, M. Burns, D. Wollman, E. Griffor[DB/OL]. Cyberphysical systems and Internet of Things. NIST, Gaithersburg, MD, USA. 2019, Rep. 1900-202.

[5]  GB/T 26790, 工业无线网络WIA规范[S].

[6]  L. Spitzner[DB/OL]. The Value of Honeypots, Part One:Definitions and Values of Honeypots. http://www.symantec.com/connect/articles/value-honeypotspart-onedefinitions-and-values-honeypots/, Apr. 14, 2020.

[7]  P. Kumar, R. Verma[J]. A review on recent advances & future trends of security in honeypot.  Int. J. Adv. Res. Comput. Sci.. 2017, vol. 8, no. 3, pp. 1108-1113.

[8]  J. Franco, A. Aris, B. Canberk, A. S. Uluagac[C]. A Survey of Honeypots and Honeynets for Internet of Things, Industrial Internet of Things, and Cyber-Physical Systems. IEEE Communications Surveys & Tutorials. 2021, vol. 23, no. 4, pp. 2351-2383.

原文来源：中国保密协会科学技术分会

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg)

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