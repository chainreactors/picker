---
title: 美国CISA将Windows和高通漏洞添加到其已知利用漏洞目录中
url: https://www.anquanke.com/post/id/300813
source: 安全客-有思想的安全新媒体
date: 2024-10-13
fetch_date: 2025-10-06T18:46:49.031188
---

# 美国CISA将Windows和高通漏洞添加到其已知利用漏洞目录中

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

# 美国CISA将Windows和高通漏洞添加到其已知利用漏洞目录中

阅读量**80290**

发布时间 : 2024-10-12 11:19:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/169557/security/u-s-cisa-adds-windows-and-qualcomm-bugs-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

美国网络安全和基础设施安全局 (CISA) 在其已知漏洞目录中增加了 Windows 和高通漏洞。
美国网络安全和基础设施安全局 (CISA) 在其已知漏洞目录 (KEV) 中增加了以下漏洞：

CVE-2024-43047 高通多个芯片组使用后免费漏洞
CVE-2024-43572 Microsoft Windows 管理控制台远程代码执行漏洞
CVE-2024-43573 Microsoft Windows MSHTML 平台欺骗漏洞
高通公司本周解决了其产品中的 20 个漏洞，其中包括一个潜在的零日问题，该问题被追踪为 CVE-2024-43047（CVSS 得分 7.8）。该漏洞源于一个可导致内存损坏的 “使用后免费”（use-after-free）错误。

该零日漏洞存在于数字信号处理器（DSP）服务中，影响数十种芯片组。

“目前，DSP 使用未使用的 DMA 句柄 fds 更新头缓冲区。在 put\_args 部分，如果头缓冲区中存在任何 DMA 句柄 FD，就会释放相应的映射。不过，由于头缓冲区是以无符号 PD 的形式暴露给用户的，因此用户可以更新无效的 FD。如果该无效 FD 与任何已在使用的 FD 相匹配，则可能导致免费使用（UAF）漏洞。“作为解决方案，为 DMA FD 添加 DMA 句柄引用，只有在找到引用时才释放 FD 的映射。

谷歌零项目的网络安全研究人员塞斯-詹金斯（Seth Jenkins）和国际特赦组织安全实验室的王聪慧（Conghui Wang）报告了这一漏洞。詹金斯希望建议尽快解决安卓设备上的这一问题。

谷歌威胁分析小组称，CVE-2024-43047 可能正受到有限的、有针对性的利用，Wang 也证实了野外活动。

研究人员还没有公布利用 CVE-2024-43047 的攻击细节，但报告机构以调查与商业间谍软件供应商有关的网络攻击而闻名。

关于CISA添加到KEV目录中的微软漏洞，IT巨头在2024年10月的补丁星期二安全更新中已经解决了这两个问题。

微软证实，这两个问题正在被恶意利用。

CVE-2024-43572 (CVSS score: 7.8) – 微軟管理控制台遠端執行程式碼漏洞： 如果用户加载恶意的 MMC snap-in，Microsoft 管理控制台漏洞可能允许远程攻击者执行代码。虽然攻击需要社会工程学且可能有限，但管理员应立即应用更新以减轻潜在危害。
CVE-2024-43573（CVSS 得分：6.5）- Windows MSHTML 平台欺骗漏洞： 尽管该漏洞被评为中度，但它与 APT 组织 Void Banshee 以前使用的漏洞补丁相似。这种相似性表明原来的修补程序可能不够完善，因此建议及时测试和部署此更新。
根据约束性操作指令 (BOD) 22-01： 减少已知漏洞被利用的重大风险》，FCEB 机构必须在规定日期前处理已发现的漏洞，以保护其网络免受利用目录中漏洞的攻击。

专家还建议私营机构审查目录并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2024 年 10 月 29 日前修复该漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/169557/security/u-s-cisa-adds-windows-and-qualcomm-bugs-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300813](/post/id/300813)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/169557/security/u-s-cisa-adds-windows-and-qualcomm-bugs-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/169557/security/u-s-cisa-adds-windows-and-qualcomm-bugs-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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