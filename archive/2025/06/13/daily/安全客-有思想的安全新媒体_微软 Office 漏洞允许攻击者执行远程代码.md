---
title: 微软 Office 漏洞允许攻击者执行远程代码
url: https://www.anquanke.com/post/id/308412
source: 安全客-有思想的安全新媒体
date: 2025-06-13
fetch_date: 2025-10-06T22:50:57.487354
---

# 微软 Office 漏洞允许攻击者执行远程代码

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

# 微软 Office 漏洞允许攻击者执行远程代码

阅读量**1353889**

发布时间 : 2025-06-12 15:43:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/microsoft-office-vulnerabilities/#google_vignette>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft Office 中的多个关键漏洞可能允许攻击者在受影响的系统上执行任意代码。

这些漏洞被跟踪为CVE-2025-47162,CVE-2025-47953,CVE-2025-47164和CVE-2025-47167,所有漏洞的CVSS得分为8.4分(满分10分),并影响Windows,Mac和Android平台的众多Office版本。

安全研究员0x140ce发现了这些缺陷,这些缺陷利用了基本的内存管理弱点,包括基于堆的缓冲区溢出,无使用条件和类型混淆错误。

此漏洞(CWE-122)源于在 Office 文件解析例程中内存分配期间的不当边界检查。

### **[CVE-2025-47162:](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47162)基于堆的缓冲溢出**

攻击者可以制作包含超大数据有效载荷的恶意文档,在处理时触发基于堆的缓冲区溢出。

通过覆盖相邻的内存区域,攻击者获得了对指令指针的控制权,从而启用了与登录用户相同的权限任意执行。

CVSS 向量字符串 CVSS:3.1/AV:L/AC/AC:L/PR:N/UI:N/S:U/C:H/I/A:H:H 突出显示本地攻击向量 (AV:L) 和低攻击复杂度 (AC:L ) , 无需用户交互 (UI:N)。尽管标题中有“远程”名称,但在下载或预览恶意文件后,漏洞在本地进行利用。

只需在预览窗格中查看武器化文档即可触发溢出,而无需用户交互。恶意宏可以在文件打开时自动利用。

### **[CVE-2025-47953:](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47953)通过不当使用后资源名称验证**

此漏洞(CWE-641)源于文件和资源名称的缺陷验证,导致无使用条件。

当 Office 在过早释放内存区域后尝试访问内存区域时,攻击者可以将恶意代码注入悬空指针的位置。缺陷在CVSS量表上得分为8.4,反映了CVE-2025-47162的严重程度。

特别设计的文件名会触发不适当的资源分配。微软将其评为“不太可能的开发”,因为操纵内存布局所需的精度。

该漏洞影响Windows,macOS(Office LTSC 2021/2024)和Android版本,需要统一修补。

### **[CVE-2025-47164:](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47164)内存管理中的经典使用后免费**

在 CWE-416 下进行分类,此漏洞源于 Office 在释放内存后未能使指针无效。

攻击者通过将释放的内存与恶意数据重新定位,从而执行代码。

CVSS 可利用性评估将此“开发更可能”标记为可预测的内存重用模式。

自2016年以来,所有Office版本都容易受到攻击,强调需要全面修补。

### **[CVE-2025-47167:](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47167)对象处理中的类型混淆**

当 Office 错误处理对象类型,将资源误认为不兼容类型时,会出现此漏洞(CWE-843 ) 。

攻击者制作包含畸形对象的文档,导致类型混乱,从而破坏内存并实现代码执行。

CVSS指标反映了其他缺陷,在保密性,完整性和可用性方面得分很高。开发技术包括在文档中嵌入矛盾类型元数据。

**跨所有平台发布的安全更新**

[微软于2025年6月10日发布了安全更新](https://cybersecuritynews.com/microsoft-patch-tuesday-june-2025/),涵盖所有主要Office版本,包括Office 2016、Office 2019、Office LTSC 2021、Office LTSC 2024、Microsoft 365 Apps for Enterprise和Office for Android。

更新通过各种机制提供,包括适用于企业版本的Click-to-Run部署和用于独立安装的传统安全更新包。

值得注意的是,Microsoft 365基于云的更新没有立即可用,该公司表示更新“将尽快发布”,客户将通过CVE信息修订收到通知。

受影响的版本跨越32位和64位版本,特定更新包由构建号标识,例如Office 2016的16.0.5504.1000和Mac版本的16.98.25060824。

组织应该优先考虑立即应用这些补丁,因为严重程度等级和高可利用性评估。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/microsoft-office-vulnerabilities/#google_vignette)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308412](/post/id/308412)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/microsoft-office-vulnerabilities/#google_vignette)

如若转载,请注明出处： <https://cybersecuritynews.com/microsoft-office-vulnerabilities/#google_vignette>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**8赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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