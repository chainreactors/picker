---
title: ModeLeak漏洞：研究人员在Google Vertex AI中发现权限提升和模型泄露威胁
url: https://www.anquanke.com/post/id/301816
source: 安全客-有思想的安全新媒体
date: 2024-11-15
fetch_date: 2025-10-06T19:13:46.332295
---

# ModeLeak漏洞：研究人员在Google Vertex AI中发现权限提升和模型泄露威胁

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

# ModeLeak漏洞：研究人员在Google Vertex AI中发现权限提升和模型泄露威胁

阅读量**58332**

发布时间 : 2024-11-14 14:28:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/modeleak-flaw-researcher-uncovers-privilege-escalation-model-exfiltration-threats-in-google-vertex-ai/>

译文仅供参考，具体内容表达以及含义原文为准。

![ModeLeak - Google Vertex AI]()

在最近的一份报告中，Palo Alto Networks 的研究人员披露了谷歌 Vertex AI 平台中的两个关键漏洞，这些漏洞可能使组织面临严重的安全风险。这些漏洞被称为 “ModeLeak”，可实现权限升级和模型外渗，可能允许攻击者访问 Vertex AI 环境中的敏感机器学习（ML）和大型语言模型（LLM）数据。

第一个漏洞是通过 Vertex AI 中的自定义作业进行权限升级。通过利用 Vertex AI Pipelines 中的自定义作业权限，攻击者可以访问整个项目的数据。报告指出：“通过操纵自定义作业管道，我们发现了一个权限升级路径，它允许我们访问远远超出预期范围的资源。这种访问权限包括从 Google 云存储和 BigQuery 数据集中列出、读取和导出数据的能力–这些操作通常需要更高级别的授权。”

通过自定义代码注入，研究人员演示了攻击者如何注入命令以打开反向 shell，从而在环境中创建后门。这一漏洞源于授予服务代理的默认权限，研究人员发现该权限过于宽泛。“凭借服务代理的身份，我们可以列出、读取甚至导出我们本不应该访问的数据桶和数据集中的数据。”

第二个漏洞带来了更为隐蔽的威胁：通过恶意模型进行模型外渗。恶意行为者可以将中毒模型上传到公共存储库，一旦部署，就会渗透到环境中的其他敏感模型。“想象一下恶意行为者将中毒模型上传到公共模型库的情景，”报告解释道。“一旦部署，恶意模型就会渗透到项目中的所有其他 ML 和 LLM 模型，包括敏感的微调模型。”这种情况创建了一个模型到模型的感染途径，嵌入在微调适配器中的专有信息可被攻击者复制和外渗。

Palo Alto Networks 此后与谷歌分享了这些发现，谷歌已部署了修复程序，以确保谷歌云平台（GCP）上 Vertex AI 的安全。为了抵御类似威胁，Palo Alto Networks 建议企业实施严格的访问控制，并密切监控模型部署流程。报告警告说，如果这些漏洞被威胁行为者利用，特别是在敏感数据驱动模型训练和调整的环境中，可能会造成广泛的后果。

本文翻译自securityonline [原文链接](https://securityonline.info/modeleak-flaw-researcher-uncovers-privilege-escalation-model-exfiltration-threats-in-google-vertex-ai/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301816](/post/id/301816)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/modeleak-flaw-researcher-uncovers-privilege-escalation-model-exfiltration-threats-in-google-vertex-ai/)

如若转载,请注明出处： <https://securityonline.info/modeleak-flaw-researcher-uncovers-privilege-escalation-model-exfiltration-threats-in-google-vertex-ai/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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