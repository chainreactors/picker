---
title: 思科发布警告：黑客正积极在野利用其ASA与FTD防火墙中的零日远程代码执行漏洞
url: https://www.anquanke.com/post/id/313049
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:01:03.583921
---

# 思科发布警告：黑客正积极在野利用其ASA与FTD防火墙中的零日远程代码执行漏洞

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

# 思科发布警告：黑客正积极在野利用其ASA与FTD防火墙中的零日远程代码执行漏洞

阅读量**22070**

发布时间 : 2025-11-07 10:26:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cisco-asa-and-ftd-0-day-rce-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

思科（Cisco）已确认，威胁行为者正在**主动利用**其**Secure Firewall自适应安全设备（ASA）** 和**威胁防御（FTD）软件**中的一个**严重远程代码执行（RCE）漏洞**。

该漏洞编号为**CVE-2025-20333**，于2025年9月25日首次披露，对依赖这些防火墙进行VPN访问的组织构成**严重风险**。其CVSS评分为**9.9**，允许**已认证攻击者**以**root权限执行任意代码**，可能导致设备完全被接管。

漏洞根源在于VPN Web服务器处理HTTP(S)请求时对**用户提供的输入验证不足**。拥有有效VPN凭证的攻击者可构造恶意请求触发漏洞，绕过正常安全防护，执行代码以窃取数据、安装恶意软件或进一步渗透网络。

思科在2025年11月5日更新的安全公告中披露，一种**针对未打补丁系统的新型攻击变体**已出现，导致设备意外重启并引发**拒绝服务（DoS）中断**。

思科事件响应团队表示，现实世界中已出现利用该漏洞的攻击案例，凸显了问题的紧迫性。

### **Cisco ASA和FTD零日RCE漏洞细节**

CVE-2025-20333的核心是**webvpn组件中存在缓冲区溢出（CWE-120）**，当某些远程访问功能启用时触发。

#### **受影响的配置场景**：

1. **ASA软件**：易受攻击的设置包括启用AnyConnect IKEv2客户端服务、移动用户安全（MUS），或通过“webvpn enable ”等命令配置的基础SSL VPN。
2. **FTD设备**：通过IKEv2远程访问或在Cisco Secure Firewall Management Center等管理界面中启用SSL VPN时面临类似风险。

**仅启用了这些功能的SSL监听套接字的设备会暴露风险**；Cisco Secure FMC软件不受影响。

### **紧急建议与应对措施**

目前**无临时缓解方案**，升级是唯一防御手段。思科强烈建议立即修补至公告中列出的修复版本，例如ASA 9.18.4.19或FTD 7.4.2。

![]()

客户应使用“**show running-config**”审计配置以识别暴露点，并监控异常VPN流量。公司将此漏洞与针对防火墙平台的广泛攻击关联，建议采取**多因素认证和入侵检测**等分层防御措施。

随着网络威胁不断演变，此次事件凸显了边界安全中**延迟更新的危险**。在持续遭受攻击的时代，延迟采取行动的组织面临连锁性 breach 的风险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cisco-asa-and-ftd-0-day-rce-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313049](/post/id/313049)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cisco-asa-and-ftd-0-day-rce-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/cisco-asa-and-ftd-0-day-rce-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **663**

* 粉丝
* **6**

### TA的文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13

### 相关文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13
* ##### [恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载](/post/id/313076)

  2025-11-07 10:27:01
* ##### [远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测](/post/id/313056)

  2025-11-07 10:26:52

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