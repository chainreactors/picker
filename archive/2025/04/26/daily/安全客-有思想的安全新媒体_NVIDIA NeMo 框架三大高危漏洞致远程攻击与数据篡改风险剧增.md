---
title: NVIDIA NeMo 框架三大高危漏洞致远程攻击与数据篡改风险剧增
url: https://www.anquanke.com/post/id/306867
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:04:05.433095
---

# NVIDIA NeMo 框架三大高危漏洞致远程攻击与数据篡改风险剧增

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

# NVIDIA NeMo 框架三大高危漏洞致远程攻击与数据篡改风险剧增

阅读量**78363**

发布时间 : 2025-04-25 10:02:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/nvidia-nemo-framework-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

NVIDIA NeMo 框架存在三个高危漏洞，攻击者可利用这些漏洞执行远程代码，这有可能危及人工智能（AI）系统的安全，并导致数据被篡改。

这些安全漏洞分别被认定为 CVE-2025-23249、CVE-2025-23250 和 CVE-2025-23251，每个漏洞的通用漏洞评分系统（CVSS）基础得分均为 7.6 分，这表明对于这个广受欢迎的生成式人工智能框架的用户来说，存在着重大风险。

NVIDIA 于 2025 年 4 月 22 日发布了安全补丁，敦促用户立即进行更新，以防范在 Windows、Linux 和 macOS 平台上可能出现的漏洞被利用的情况。

****NVIDIA********NeMo 框架中的高危漏洞****

第一个漏洞（CVE-2025-23249）涉及对不可信数据的不安全反序列化，这可能使攻击者能够远程执行任意代码。

这个被归类为 CWE-502 的漏洞，使得攻击者能够在数据处理周期中操纵序列化对象并注入恶意代码。

官方安全公告指出：“NVIDIA NeMo 框架存在一个漏洞，用户可能会因远程代码执行而导致对不可信数据进行反序列化。成功利用这个漏洞可能会导致代码执行和数据篡改。”

第二个漏洞（CVE-2025-23250）源于不正确的路径验证（CWE-22），攻击者有可能通过利用路径遍历技术来执行任意文件写入操作。

安全研究人员指出，这一弱点可能会让攻击者覆盖敏感文件或引入恶意配置，从而有可能劫持训练流程或在人工智能工作流程中污染数据集。

第三个漏洞（CVE-2025-23251）与对代码生成的控制不当（CWE-94）有关，攻击者可利用该漏洞进行远程代码执行。

对于一个为生成式人工智能应用设计的框架来说，这一点尤其令人担忧，因为它直接影响到可信和不可信代码执行环境之间的界限。

NVIDIA 对来自上海大学的安全研究员 Peng Zhou 表示感谢，因为他报告了 4 月份发现的这三个漏洞。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****漏洞编号（CVE）**** | ****受影响产品**** | ****影响**** | ****利用前提条件**** | ****CVSS 3.1 评分**** |
| CVE-2025-23249、CVE-2025-23250、CVE-2025-23251 | NVIDIA NeMo 框架（Windows、Linux、macOS；25.02 版本之前的所有版本） | 代码执行，数据篡改 | 远程攻击者，需要用户交互 | 7.6（高危） |

这三个漏洞具有相同的攻击向量规格（AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:H/A:L），这表明它们可以在攻击复杂度较低且无需特权的情况下被远程利用，不过需要用户进行交互操作。

NeMo 框架是一个可扩展的云原生生成式人工智能平台，被从事大型语言模型（LLM）、多模态模型以及包括语音识别和计算机视觉等各种人工智能应用研究的研究人员和开发人员广泛使用。

该公司已发布 25.02 版本以修复这些问题，并强烈建议所有受影响的系统立即进行更新。

安全专家建议使用 NeMo Framework 的机构采取以下措施：

1.立即更新到 25.02 版本。

2.检查任何可能已受到损害的人工智能系统。

3.在人工智能开发流程周围实施额外的安全控制措施。

4.监控系统，留意可能表明存在漏洞被利用情况的异常活动。

这些漏洞凸显了在人工智能开发框架中安全的重要性日益增加，因为它们在全球的商业运营和研究计划中变得越来越关键。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/nvidia-nemo-framework-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306867](/post/id/306867)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/nvidia-nemo-framework-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/nvidia-nemo-framework-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**9赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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