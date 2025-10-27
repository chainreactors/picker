---
title: 新型PerfektBlue攻击曝光：数百万辆汽车面临远程黑客攻击风险
url: https://www.anquanke.com/post/id/309920
source: 安全客-有思想的安全新媒体
date: 2025-07-12
fetch_date: 2025-10-06T23:16:51.234331
---

# 新型PerfektBlue攻击曝光：数百万辆汽车面临远程黑客攻击风险

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 新型PerfektBlue攻击曝光：数百万辆汽车面临远程黑客攻击风险

阅读量**64442**

发布时间 : 2025-07-11 16:11:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/bluetooth-protocol-stack-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为**PerfektBlue**的新型严重安全威胁已出现，其针对OpenSynergy公司的BlueSDK蓝牙框架，给汽车行业带来了前所未有的风险。

这种复杂的攻击向量通过一系列**内存损坏和逻辑漏洞**，可对汽车及其他行业的数百万台设备实施**远程代码执行（RCE）**。

#### ****核心要点****

1. BlueSDK中存在4个可被链式利用的漏洞，借助蓝牙可实现一键式远程代码执行。
2. 梅赛德斯-奔驰、大众和斯柯达等品牌的数百万辆汽车因信息娱乐系统存在漏洞而受到影响。
3. 攻击者可获取全球定位系统（GPS）追踪数据、进行音频录制、访问个人数据，甚至可能控制车辆电子控制单元（ECU）。
4. 尽管OpenSynergy已于2024年9月发布修复程序，但受汽车供应链延迟影响，部分制造商直至2025年6月才完成漏洞修补。

该漏洞利用链**仅需极少的用户交互，就会对车载信息娱乐（IVI）系统构成严重威胁**，攻击者可能借此获取GPS坐标、音频记录、个人数据，并横向渗透至关键的车辆电子控制单元。

OpenSynergy公司BlueSDK蓝牙框架存在严重漏洞

PCA网络安全公司向《网络安全新闻》透露，此次攻击采用了**复杂的漏洞利用链，融合了4个不同的漏洞**，且最多仅需目标用户点击一次即可实施攻击。这种攻击方法利用了**BlueSDK的框架特性**，不同厂商在该框架上采用的安全配置和配对机制各不相同。攻击流程始于与目标设备建立**蓝牙连接**，通常需要通过配对来达到相应的安全通信级别。

然而，由于BlueSDK的框架架构，不同设备的具体配对要求存在显著差异。部分设备可能允许无限次配对请求，有些则需要用户交互，还有些配置可能完全禁用配对功能。这种差异性形成了**复杂的攻击面**，不同制造商和设备类型的漏洞利用条件也各不相同。

![]()

此次攻击的危害在于，它能通过**蓝牙通信协议**实现远程代码执行，具体针对**音频/视频远程控制规范（AVRCP）、逻辑链路控制与适配协议（L2CAP）以及射频通信（RFCOMM）层**。攻击成功后，攻击者可在目标系统中获得**用户级权限**，进而实施进一步的漏洞利用和横向渗透。

PerfektBlue攻击链包含**4个**严重漏洞，每个漏洞都有对应的CVE编号。

* **CVE-2024-45434**是其中**最严重**的漏洞，为AVRCP服务中存在的**“释放后使用（UAF）”**漏洞，CVSS评分为**8.0**。这种内存损坏漏洞源于系统在执行操作前未验证对象是否存在，使得攻击者能够操控已释放的内存区域并执行任意代码。
* **CVE-2024-45431**涉及对L2CAP通道远程通道标识符（CID）的验证不当，CVSS评分为**3.5**。该漏洞允许攻击者创建以空标识符作为远程CID的L2CAP通道，可能绕过安全机制。
* **CVE-2024-45433**和**CVE-2024-45432**均针对RFCOMM协议实现，CVSS评分均为**5.7**。前者因函数终止不正确，在检测到异常情况后未正确控制返回流程；后者则是由于函数调用时使用错误变量作为参数，导致参数传递错误。

从**技术层面**来看，实施这种攻击需要深入了解**蓝牙协议栈、内存管理和嵌入式系统架构**。

攻击者必须**按顺序链式利用**这些漏洞，在通过其他漏洞**建立受compromise的L2CAP和RFCOMM连接**后，利用**AVRCP中的“释放后使用”漏洞**实施攻击。

|  |  |  |  |
| --- | --- | --- | --- |
| ****CVE编号**** | ****描述**** | ****CVSS3.1评分**** | ****严重程度**** |
| CVE-2024-45434 | AVRCP服务中存在释放后使用漏洞 | 8.0 | 严重 |
| CVE-2024-45431 | L2CAP通道远程CID验证不当 | 3.5 | 低 |
| CVE-2024-45433 | RFCOMM中函数终止不正确 | 5.7 | 中等 |
| CVE-2024-45432 | RFCOMM中函数调用参数错误 | 5.7 | 中等 |

**缓解措施**

PerfektBlue攻击的影响范围**覆盖多家主要汽车制造商**，已确认**梅赛德斯-奔驰、大众和斯柯达**的车辆存在相关漏洞。

研究人员已在梅赛德斯-奔驰NTG6/NTG7主机、大众MEBICAS3信息娱乐系统（ID.4车型系列）以及斯柯达MIB3主机（速派车型系列）上成功演示了概念验证漏洞利用。

每次漏洞利用都能使攻击者在车载信息娱乐系统中获得用户级权限，如“phone”或“sint\_sec\_btapp”权限。

汽车行业复杂的供应链给补丁部署带来了困难。尽管OpenSynergy于2024年9月发布了修复程序，但部分制造商直到2025年6月才完成修补，这凸显了汽车网络安全供应链管理中存在的严重漏洞。

缓解策略包括**立即为受影响设备更新固件、在不使用时禁用蓝牙功能**，以及**实施网络分段**以防止从车载信息娱乐系统横向渗透至车辆关键部件。

制造商应优先**对蓝牙协议栈实现进行安全验证**，并建立健全的漏洞披露流程。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/bluetooth-protocol-stack-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309920](/post/id/309920)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/bluetooth-protocol-stack-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/bluetooth-protocol-stack-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)