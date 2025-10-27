---
title: 黑客使用假VPN和浏览器NSIS安装程序来传输Winos 4.0恶意软件
url: https://www.anquanke.com/post/id/307743
source: 安全客-有思想的安全新媒体
date: 2025-05-27
fetch_date: 2025-10-06T22:23:29.611808
---

# 黑客使用假VPN和浏览器NSIS安装程序来传输Winos 4.0恶意软件

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

# 黑客使用假VPN和浏览器NSIS安装程序来传输Winos 4.0恶意软件

阅读量**134640**

发布时间 : 2025-05-26 13:06:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 拉维·拉克什马南，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/05/hackers-use-fake-vpn-and-browser-nsis.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员披露了一项恶意软件活动,**该活动使用假软件安装程序伪装成LetsVPN和QQ浏览器等流行工具来提供Winos** 4.0框架。

该活动于2025年2月由Rapid7首次发现,涉及使用名为Catena的多阶段内存驻留装载机。

“Catena使用嵌入式shellcode和配置交换逻辑来完全在内存中放置像Winos 4.0这样的有效载荷,从而避开传统的防病毒工具,”安全研究人员Anna Širokova和Ivan saidFeigl说。“一旦安装,它悄悄地连接到攻击者控制的服务器 – 主要托管在香港 – 以接收后续指令或额外的恶意软件。

这些攻击,就像过去部署Winos 4.0的攻击一样,似乎特别关注说中文的环境,网络安全公司称这是一个非常有能力的威胁行为者的“谨慎,长期规划”。

Winos 4.0(又名ValleyRAT)于2024年6月首次被Trend Micro公开记录,用于通过VPN应用程序的恶意Windows Installer(MSI)文件针对讲中文用户的攻击。该活动归因于它跟踪的威胁集群Void Arachne,也称为Silver F

随后分发恶意软件的活动利用了与游戏相关的应用程序,如安装工具,速度增强器和优化实用程序,作为诱骗用户安装它的诱因。另一波攻击浪潮于2025年2月通过据称来自国家税务局的网络钓鱼电子邮件针对台湾的实体。

Winos 4.0 构建在已知远程访问木马 Gh0st RAT 的基础之上,是用 C++ 编写的高级恶意框架,它利用基于插件的系统来收集数据、提供远程 shell 访问以及启动分布式拒绝服务 (DDoS) 攻击。

|  |
| --- |
|  |
|  |

Rapid7表示,2025年2月标记的所有工件都依赖于NSIS安装程序,捆绑了签名的诱饵应用程序,嵌入“.ini”文件中的shellcode以及反光DLL注入,以秘密保持对受感染主机的持久性并避免检测。整个感染链都被命名为Catena。

“到目前为止,该活动在整个2025年一直很活跃,显示出一致的感染链,并进行了一些战术调整 – 指向一个有能力和适应性的威胁行为者,”研究人员说。

NSIS起点是一个木偶联安装程序,冒充QQ浏览器的安装程序,这是腾讯开发的基于Chromium的Web浏览器,旨在使用Catena提供Winos 4.0。恶意软件通过TCP端口18856和HTTPS端口443与硬编码的命令和控制(C2)基础设施通信。

|  |
| --- |
| [![Winos 4.0 Malware](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRdModoOxpSz6qoEHjwuXEQHmXZtaKMQEOIGvnBCJkiDLRSg6ufT1pRQFS-4NfsYk6cY_Ywdd6tztrNxQVmLKsMEwchOOI6lqNqdqTIRgAtNiQD0VsIWOWBITy4TvFhoAWCzCyfAljxFOoV3-e-SLOho3D65rEKM-wKuI7jIkcBm8CQdPox16WLm51ZfsN/s728-rw-e365/eee.jpg "维诺斯 4.0 恶意软件")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRdModoOxpSz6qoEHjwuXEQHmXZtaKMQEOIGvnBCJkiDLRSg6ufT1pRQFS-4NfsYk6cY_Ywdd6tztrNxQVmLKsMEwchOOI6lqNqdqTIRgAtNiQD0VsIWOWBITy4TvFhoAWCzCyfAljxFOoV3-e-SLOho3D65rEKM-wKuI7jIkcBm8CQdPox16WLm51ZfsN/s728-rw-e365/eee.jpg) |
|  |

对主机的持久性是通过在初始妥协后几周执行的计划任务来实现的。虽然恶意软件具有显式检查以查找系统上的中文设置,但即使情况并非如此,它仍然会继续执行。

这表明它是一个未完成的功能,并且有望在恶意软件的后续迭代中实现。也就是说,Rapid7表示,它在2025年4月发现了一个“战术转变”,不仅改变了Catena执行链的一些元素,而且还整合了逃避防病毒检测的功能。

在改进的攻击序列中,NSIS安装程序将自己伪装成LetsVPN的设置文件,并运行PowerShell命令,该命令为所有驱动器(C:\到Z:\)添加Microsoft Defender排除。然后,它会删除其他有效载荷,包括一个可执行文件,该可快照运行进程并检查与中国供应商奇虎360开发的防病毒产品360 Total Security相关的进程。

二进制文件与VeriSign颁发的过期证书签署,据称属于腾讯科技(深圳)。有效期为2018-10-11至2020-02-02。可执行文件的主要责任是反射加载DLL文件,该文件反过来连接到C2服务器(“134.122.204[.]11:18852”或“103.46.185[.]44:443”),以便下载和执行Winos 4.0。

“这项活动展示了一个组织良好,以区域为重点的恶意软件操作,使用木马化的NSIS安装程序,悄悄地放弃Winos 4.0舞台,”研究人员说。

“它严重依赖内存驻留有效载荷,反射式DLL加载和带有合法证书签名的诱饵软件,以避免发出警报。基础设施重叠和基于语言的定位暗示与Silver Fox APT有联系,活动可能针对中文环境。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/05/hackers-use-fake-vpn-and-browser-nsis.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307743](/post/id/307743)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/05/hackers-use-fake-vpn-and-browser-nsis.html)

如若转载,请注明出处： <https://thehackernews.com/2025/05/hackers-use-fake-vpn-and-browser-nsis.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25

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