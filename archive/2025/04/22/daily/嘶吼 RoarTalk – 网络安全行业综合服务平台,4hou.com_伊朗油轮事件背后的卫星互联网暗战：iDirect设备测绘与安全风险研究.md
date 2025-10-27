---
title: 伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究
url: https://www.4hou.com/posts/7M21
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-22
fetch_date: 2025-10-06T22:03:39.497477
---

# 伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究

伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究

盛邦安全
[资讯](https://www.4hou.com/category/info)
2025-04-21 11:06:52

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)45168

收藏

导语：伊朗油轮事件背后的卫星互联网暗战：iDirect设备测绘与安全风险研究

**一、前言**

本文主要分享一些我们最近对iDirect设备的研究，篇幅较长，我们公开了部分研究成果，也希望更多对卫星网络安全研究感兴趣的读者能加入这个新赛道。

**二、事件回顾**

**2.1 事件概况**

2025年3月18日，黑客组织Lab Dookhtegan（又称“Read My Lips”）宣称对伊朗两大国有航运公司—伊朗国家油轮公司（NITC）和伊斯兰共和国航运公司（IRISL）的116艘船只发动大规模网络攻击，导致油轮的卫星通信系统全面瘫痪。此次攻击正值美国对也门胡塞武装发动军事打击之际，被外界视为针对伊朗地区代理人的“数字报复”。

此次攻击主要针对船舶的卫星通信系统，导致船上和陆地间的通信中断，该组织利用Shodan等互联网搜索工具扫描并锁定了暴露在互联网上的iDirect卫星通信终端，通过默认口令获取终端root权限。攻击者随后部署自动攻击脚本，利用终端自带的dd指令擦除存储器，导致终端系统无法正常工作。

本次攻击事件的技术复杂度表明，这绝非普通黑客组织所能独立完成，背后可能存在国家行为体的间接支持。Lab Dookhtegan 在Telegram上表示，发起这项行动是为了配合美国对也门胡塞武装的袭击，这两家公司负责向胡塞武装供应弹药。根据技术分析，此次攻击手法与2022年2月针对Viasat卫星网络的攻击高度相似，同样利用了设备弱口令和系统版本陈旧(2020年版本)的安全缺陷，反映了卫星通信设备面临的普遍安全挑战。

**2.2 冲突焦点**

在此次事件中，美国ST Engineering iDirect公司的iDirect卫星调制解调器成为攻击者的核心目标。作为船舶与外界通信的关键桥梁，iDirect卫星调制解调器在船只远离陆地时提供可靠的高带宽通信链路。这些设备采用"星状网"拓扑结构，通过Ka或Ku波段与地球同步轨道卫星相连，形成覆盖全球海域的通信网络，在伊朗海事领域有大量部署。iDirect卫星调制解调器存在默认口令（root,P@55w0rd!），一般用户不会主动修改该密码导致默认口令的风险存在。另一方面，系统版本的陈旧也增加了较大风险，通过此次事件获取到的信息，该设备系统为2020年版本，OpenSSH等关键服务版本老旧，主要由于设备厂商较少提供系统更新服务导致，这些脆弱性与设备厂商缺乏持续更新支持直接相关，造成"技术债务"不断积累。

从功能角度看，这些卫星终端负责船舶的互联网接入、远程监控、船员通信及数据传输等关键业务。虽然目前多数船只的总线系统与通信系统相对隔离，限制了攻击影响范围，但随着船舶自动化程度提高和系统互联深化，这种隔离正逐渐弱化。攻击者通过破坏这些终端，不仅造成通信中断，还展示了针对关键基础设施的精准打击能力。美国企业生产的卫星通信设备在伊朗油轮上的广泛应用，形成了一种特殊的技术依赖关系，使伊朗关键海运基础设施在国际政治博弈中处于脆弱位置。

**三、海事卫星通信骨干单元iDirect设备**

**3.1 iDirect设备简介**

iDirect设备指的是美国ST Engineering iDirect公司（其母公司为新加坡ST Engineering）的卫星通信产品。ST Engineering iDirect产品类型包括调制解调器、集线器和卫星通信解决方案，主要服务于服务商、网络运营商、政府机构、大型企业、军队等客户，其全资子公司iDirect Government是美国国防部领先的卫星通信产品供应商。其产品线涵盖iQ系列、Evolution系列、Evolution Defense 系列、Velocity 系列、MDM系列及9系列等多个方向，其中Evolution系列主要用于星状组网架构的VSAT场景，在海事通信领域具有广泛应用。消息表明，我国目前仍有Evolution系列的设备正在服役。

![QQ20250418-174211.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744971998919749.png "1744971998919749.png")

iDirect相关设备并不依赖于特定的卫星系统，而是通过与不同的卫星服务提供商合作，使用多种卫星来提供通信服务。伊朗的油轮具体使用哪颗卫星来提供通信服务取决于服务提供商的选择和船舶的航行区域。此次攻击的核心目标是船载iDirect VSAT（甚小孔径终端）卫星通信设备中的调制解调器。

iDirect VSAT设备的工作原理基于卫星通信的基本架构，实现了地面站点与卫星之间的双向数据传输。其通信链路包括从中心站点（Hub）到远程站点的前向链路和从远程站点回传到中心站点的返回链路。

其技术特点是采用基于TDMA（时分多址）和SCPC（单载波每信道）的混合访问方式：支持DVB-S2/S2X标准，实现高效的带宽利用；实现动态带宽分配(DBWA)，根据流量需求自动调整带宽资源；集成QoS(服务质量)功能，确保关键业务流量优先处理。采用IP封装技术，将用户数据封装成适合卫星传输的格式，实现加密和压缩功能，保障数据安全和传输效率，支持TCP加速和Web缓存，优化卫星链路的数据传输性能。

其网络架构由中心主站、卫星转发器和远程终端组成，主站连接互联网骨干网，负责管理整个网络，远程终端通过天线和调制解调器与卫星通信。

![QQ20250418-174320.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972011149855.png "1744972011149855.png")

**3.2 主要部署场景与应用生态**

iDirect在全球范围内实现了可靠的卫星通信，特别是在传统通信基础设施不可用或不可靠的地区发挥着重要作用,如在海事通信、能源行业、政府和军事应用、偏远地区连接等场景下应用。

在海事领域，iDirect设备广泛应用于海上通信。可用于商业船队，为船员提供互联网访问和通信服务，支持船舶远程监控和诊断系统，提供航线优化和天气导航信息服务；也可用于邮轮和客运船，为乘客提供高速互联网服务，支持船上娱乐系统和支付系统，实现船舶安全监控和紧急通信；还可用于海上石油平台，提供远程操作和监控能力，支持视频会议和专家远程协助，确保关键业务数据的实时传输。

在石油和天然气行业，iDirect设备可应用于偏远油气田的通信和管道监控等场景。可连接偏远油气田现场与总部的通信，支持SCADA系统和远程监控，提供员工福利通信服务；可用于管道监控，实现长距离管道的实时监控，支持泄漏检测系统数据传输，提供安全监控和紧急响应通信。

在政府和军事领域也有广泛应用。iDirect的军用级产品线可应用于战术通信，提供易于部署的机动通信系统，支持加密和抗干扰通信，实现指挥控制系统的网络化；还可应用于边境监控，连接偏远监控站点，支持视频监控和传感器数据回传，提供紧急情况下的通信保障。

在缺乏传统通信基础设施的偏远地区通信方面也有着应用。可在缺乏传统通信基础设施的地区提供互联网接入，支持远程教育和医疗服务，实现政府公共服务的数字化；在灾难响应场景下，可以提供快速部署的应急通信系统，支持救灾指挥和协调以及在传统通信中断时提供备份连接。

**3.3 互联网设备分布情况**

从DayDayMap的测绘结果显示，共有12922个设备暴露在互联网上。

![QQ20250418-174359.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972023388972.png "1744972023388972.png")

其中印尼、德国、沙特、美国和英国使用的该设备最多，这些国家也都对应有大量的海上通信业务。

![QQ20250418-174419.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972037121915.png "1744972037121915.png")

**四、iDirect设备相关协议分析**

**4.1 分析思路**

iDirect设备提供的协议从多个方面进行分析，一个是根据伊朗反政府黑客组织“Lab Dookhtegan”公布的信息；另一个是设备的官方文档；三是根据设备的应用场景入手；最后通过未知协议带有特定信息入手。

**4.1.1 根据伊朗反政府黑客组织“Lab Dookhtegan”公布信息**

根据伊朗反政府黑客组织“Lab Dookhtegan”公布的iDirect设备内部监听端口信息可知，目前TCP端口443，80，22，2494，以及UDP端口36057，53471，9000，60989，67，1492均有机会对其进行尝试。

![QQ20250418-174449.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972054151482.png "1744972054151482.png")

A、80，443webserver

在daydaymap上根据如下指纹搜索到相关设备，其中title=="iDirect Terminal"可以确认是该产品，而另一个无法对其进行确认。

body="<input type=\"hidden\" name=\"fail\" value=\"/login.html\"/>"||title=="iDirect Terminal"

![QQ20250418-174549.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972077772232.png "1744972077772232.png")

![QQ20250418-174612.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972085485585.png "1744972085485585.png")

B、22端口的ssh信息

![QQ20250418-174647.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972100712262.png "1744972100712262.png")

C、Falcon主要是用于运行所有的satellite functions。

![QQ20250418-174710.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972117112003.png "1744972117112003.png")

在2494端口探测数据时发现有iDirect证书的数据，用于佐证2494端口对iDirect设备的识别。

![QQ20250418-174736.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972129155135.png "1744972129155135.png")

**4.1.2 iDirect Velocity的说明书发现其支持snmp功能**

**![QQ20250418-174759.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972143165151.png "1744972143165151.png")**

****4.2 设备的应用场景****

i. Mikrotik

从《俄罗斯Dozor-Teleport卫星通信运营商遭黑中断情况分析》一文中发现了iDirect与Mikrotik混合的应用场景，同时在其Mikrotik官网论坛里发现用户关于iDirect和Mikrotik混合场景的讨论。再根据Mikrotik提供的协议，进行涉及协议的分析。如下图，可以获取到这个设备的hostname,当将TIRTASARI在海事网站**MarineTraffic: Global Ship Tracking Intelligence | AIS Marine Traffic**进行搜索时，可以发现这是一艘货轮的名称。

![QQ20250418-174823.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972171530388.png "1744972171530388.png")

![QQ20250418-174833.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972186502648.png "1744972186502648.png")

![QQ20250418-174839.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972195349270.png "1744972195349270.png")

Mikrotik一般在外部的协议主要是PPTP,L2TP,IPsec以及bandwidth-test。其中pptp和l2tp协议能获取更多有效信息供指纹进行识别。

![QQ20250418-175048.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972210564363.png "1744972210564363.png")

![QQ20250418-175054.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972218130826.png "1744972218130826.png")

ii. Cisco

iDirect X7-EC Satellite Router内嵌了Cisco 5921 Embeded services Router，也就是说可以通过Cisco端口进行iDirect设备的识别。

![QQ20250418-175200.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250418/1744972229879259.png "1744972229879259.png")

**未知协议**

**banner="iDIRECT"&&service="junoscript"**

![QQ20250418-175228.p...