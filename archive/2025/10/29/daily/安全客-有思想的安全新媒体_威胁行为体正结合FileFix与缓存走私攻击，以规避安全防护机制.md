---
title: 威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制
url: https://www.anquanke.com/post/id/312867
source: 安全客-有思想的安全新媒体
date: 2025-10-29
fetch_date: 2025-10-30T03:10:28.301456
---

# 威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制

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

# 威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制

阅读量**24098**

发布时间 : 2025-10-29 17:29:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta ，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/filefix-and-cache-smuggling-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现了一场复杂的钓鱼攻击活动，该活动结合了两种新兴攻击技术以绕过传统安全防御。

这种混合攻击方法将**FileFix社会工程战术**与**缓存走私（cache smuggling）** 相结合，在不触发基于网络的检测系统的情况下投放恶意软件 payload。

这一演变标志着威胁行为者规避端点检测与响应（EDR）解决方案的**重大策略转变**——通过消除恶意代码执行期间建立互联网连接的需求，实现隐蔽攻击。

攻击始于一个伪装成**合法FortiClient合规检查器界面**的欺骗性钓鱼页面。

![]()

受害者被社会工程诱导，将剪贴板内容粘贴到Windows资源管理器地址栏中执行恶意命令。

该技术利用FileFix方法学，通过资源管理器地址栏的**2048字符限制**传递远大于传统ClickFix攻击（受限于Windows“运行”对话框的260字符）的payload。

![]()

攻击者通过在命令中填充空格进一步隐藏恶意内容：用户只能看到看似无害的文本，而恶意PowerShell脚本则隐藏在不可见部分。

此攻击活动与传统恶意软件分发方法的核心区别在于，它创新性地利用**缓存走私**在受害者系统上预放置payload。

不同于安全工具通常监控的常规Web请求下载恶意文件，该攻击利用浏览器缓存机制，将伪装成合法图像文件的嵌入式可执行文件存储在本地。

MalwareTech分析师在Expel Security的威胁情报调查中发现了这一技术：第一阶段加载器直接从浏览器缓存中提取第二阶段payload，**不产生任何可疑网络流量**。

技术实现细节如下：JavaScript代码使用fetch()函数检索伪造的JPG文件（实为包含恶意payload的ZIP归档）。

通过将HTTP Content-Type标头设置为image/jpeg，攻击者诱骗浏览器将可执行文件缓存为标准静态资源。

随后，嵌入式PowerShell脚本搜索浏览器缓存目录定位走私的ZIP文件，提取内容并执行恶意软件，**全程不建立任何会触发网络监控系统的外部连接**。

### **高级Exif走私技术**

在基础缓存走私原理之上，安全研究人员开发了更复杂的变体——利用**Exif元数据隐藏**在合法图像文件中。

该技术利用可交换图像文件格式（Exif）规范，允许在JPG图像中存储高达64 KB的元数据。

通过将恶意payload嵌入超大Exif字段同时保持图像结构有效，攻击者可创建完全正常的照片，其中隐藏的可执行代码**无法通过常规检查发现**。

实现过程利用了Exif解析器处理ASCII字符串字段的特性：大多数软件将空字节视为字符串终止符，但Exif规范通过单独的长度字段定义实际数据大小。

研究人员演示了如何构造图像描述字段：先放置良性文本，后跟空字节，再用分隔符标记包裹payload数据。

当通过Windows资源管理器属性查看时，仅显示无害描述；而完整恶意payload仍嵌入文件结构中，可通过PowerShell正则表达式匹配特定字节模式**程序化提取**。

这种Exif走私方法解决了早期缓存走私实现的多个缺陷：

传统方法仅将可执行文件重命名为图像文件，会生成损坏的图像图标，并面临防火墙内容类型验证的检测风险。

新技术生成**完全有效的JPG文件**，可正常显示图像，同时包含无需专用Exif解析器即可提取的隐藏payload。

测试表明，此方法可通过多种攻击向量生效，包括Microsoft Outlook电子邮件附件——即使禁用预览功能，图像仍会被预先缓存，可能在用户打开邮件前**提前投放payload**。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/filefix-and-cache-smuggling-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312867](/post/id/312867)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/filefix-and-cache-smuggling-attacks/)

如若转载,请注明出处： <https://cybersecuritynews.com/filefix-and-cache-smuggling-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **630**

* 粉丝
* **6**

### TA的文章

* ##### [重磅！网络安全法迎来重大修改，人工智能治理迈出关键一步](/post/id/312934)

  2025-10-29 17:30:44
* ##### [OpenAI宣布启动重组，非营利基金会将重新掌握公司核心控制权](/post/id/312864)

  2025-10-29 17:29:30
* ##### [威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制](/post/id/312867)

  2025-10-29 17:29:15
* ##### [TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效](/post/id/312872)

  2025-10-29 17:28:56
* ##### [新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码](/post/id/312878)

  2025-10-29 17:27:44

### 相关文章

* ##### [重磅！网络安全法迎来重大修改，人工智能治理迈出关键一步](/post/id/312934)

  2025-10-29 17:30:44
* ##### [OpenAI宣布启动重组，非营利基金会将重新掌握公司核心控制权](/post/id/312864)

  2025-10-29 17:29:30
* ##### [TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效](/post/id/312872)

  2025-10-29 17:28:56
* ##### [新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码](/post/id/312878)

  2025-10-29 17:27:44
* ##### [Docker Compose 中存在路径遍历漏洞（CVE-2025-62725），通过OCI制品可导致任意文件被覆盖](/post/id/312882)

  2025-10-29 17:27:07
* ##### [Wear OS 信息应用存在权限漏洞 (CVE-2025-12080)，可导致无权限应用在未经用户授权的情况下发送短信/RCS消息，且POC已公开](/post/id/312885)

  2025-10-29 17:26:40
* ##### [Magento 中存在严重漏洞（CVE-2025-54236），可导致会话劫持与RCE，且已被活跃利用](/post/id/312888)

  2025-10-29 17:26:05

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