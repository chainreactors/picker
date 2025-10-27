---
title: LibreOffice 指责微软借复杂文件格式蓄意 “锁定” 用户
url: https://www.anquanke.com/post/id/310370
source: 安全客-有思想的安全新媒体
date: 2025-07-22
fetch_date: 2025-10-06T23:16:58.319060
---

# LibreOffice 指责微软借复杂文件格式蓄意 “锁定” 用户

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

# LibreOffice 指责微软借复杂文件格式蓄意 “锁定” 用户

阅读量**47248**

发布时间 : 2025-07-21 17:23:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/libreoffice-accuses-microsoft-of-deliberate-lock-in-through-complex-file-formats/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

知名开源办公套件 LibreOffice 近日发表声明，指控微软蓄意采用**不必要的复杂文件格式**，将用户 **“锁定” 在其 Microsoft 365 生态系统中**，以此阻碍文档向其他平台的无缝迁移，**破坏工作流的连续性**。

双方争议的复杂性聚焦于 **XML 标记语言** ——Microsoft 365 与 LibreOffice 均使用 XML 构建和定义文档。LibreOffice 解释道：

“XML 模式包含 XML 文档的**结构、数据类型和规则**，由 XML 模式定义（XSD）文件描述。它告知计算机预期内容，并检查数据是否符合规则。理论上，XML 与 XSD 共同构成了互操作性概念的基础。”

然而，在互操作性方面，LibreOffice 与 Microsoft 365 采取了**截然不同**的路径。LibreOffice 遵循**开放文档格式（ODF）**—— 这是一种不受企业控制的行业标准开放格式。ODF 标准支撑着人们熟悉的文件类型，如文本文档的 ODT 格式和电子表格的 ODS 格式。

相比之下，微软打造了**自有专有格式 “Office Open XML（OOXML）”**，以涵盖其软件套件的所有功能，由此产生了 DOCX（文本文档）、XLSX（电子表格）等广泛使用的格式。本质上，这些格式是 ZIP 压缩包 —— 只需将 DOCX 文件重命名为 ZIP 扩展名，即可查看 Microsoft 365 文档的内部结构。

LibreOffice 认为，**XML 本应成为兼容性的桥梁，但微软却将其 OOXML 标准 “武器化”**，使其过于复杂，刻意设置准入障碍。该办公套件指出，深层嵌套结构、非直观命名规则以及大量可选元素，是这种复杂性的显著特征。

对于开源办公软件开发者而言，在没有微软工程师直接协助的情况下，实现与微软格式的兼容几乎是一项**不可能完成的任务**。即便是最简单的句子，也会被转化为错综复杂的嵌套标签。尽管在屏幕上显示的内容可能完全相同，但底层的文件结构极为复杂，令其他办公套件难以解析。

LibreOffice 还指出，类似的 “锁定” 机制还体现在其他方面，尤其是这些**复杂格式与推广 Windows 11 的举措相互关联**。该公司认为，微软坚持此类转换缺乏合理的技术依据，仅是为了**加深用户依赖**。

最后，LibreOffice 呼吁用户考虑从**专有 Windows NT 操作系统**迁移至**开放的、社区驱动的 Linux 平台**，并以开源的 LibreOffice 替代封闭的 Microsoft 365 套件。

本文翻译自securityonline [原文链接](https://securityonline.info/libreoffice-accuses-microsoft-of-deliberate-lock-in-through-complex-file-formats/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310370](/post/id/310370)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/libreoffice-accuses-microsoft-of-deliberate-lock-in-through-complex-file-formats/)

如若转载,请注明出处： <https://securityonline.info/libreoffice-accuses-microsoft-of-deliberate-lock-in-through-complex-file-formats/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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