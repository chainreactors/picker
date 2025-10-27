---
title: NVIDIA NeMo 框架三大高危漏洞危及 AI 开发，数据篡改与远程代码执行风险剧增
url: https://www.anquanke.com/post/id/306833
source: 安全客-有思想的安全新媒体
date: 2025-04-25
fetch_date: 2025-10-06T22:04:31.778995
---

# NVIDIA NeMo 框架三大高危漏洞危及 AI 开发，数据篡改与远程代码执行风险剧增

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

# NVIDIA NeMo 框架三大高危漏洞危及 AI 开发，数据篡改与远程代码执行风险剧增

阅读量**50364**

发布时间 : 2025-04-24 10:01:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/nvidia-nemo-framework-high-risk-vulnerabilities-allow-remote-code-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

![NVIDIA NeMo Remote Code Execution]()

NVIDIA 发布了一份安全公告，披露其 NeMo 框架中存在三个严重级别的漏洞。NeMo 框架是一个可扩展的、云原生的生成式人工智能平台，专为使用大语言模型（LLMs）、多模态模型（MMs）、语音识别（ASR）、文本转语音（TTS）和计算机视觉（CV）的开发人员而设计。

每个漏洞的通用漏洞评分系统（CVSS）基础评分均为 7.6，这表明如果被成功利用，这些漏洞会带来严重风险，可能导致远程代码执行和数据篡改。

第一个漏洞（CVE-2025-23249）涉及不安全的反序列化。据 NVIDIA 称，NeMo 框架 “存在一个漏洞，用户可通过远程代码执行导致对不可信数据进行反序列化。成功利用这个漏洞可能会导致代码执行和数据篡改”。

反序列化攻击能让攻击者操纵序列化对象，并在数据恢复过程中执行恶意代码，这使得该漏洞在协作式或分布式人工智能开发环境中尤其危险。

第二个漏洞（CVE-2025-23250）是由于对文件路径名的限制不足而产生的：“攻击者可通过任意文件写入操作，导致对受限目录的路径名出现不当限制。成功利用该漏洞，可能会导致代码执行和数据篡改。”

这一弱点可让对手覆盖敏感文件或引入恶意配置，有可能劫持人工智能工作流程中的训练管道或污染数据集。

第三个漏洞（CVE-2025-23251）影响代码生成过程本身：“用户可通过远程代码执行导致对代码生成的控制不当。成功利用这个漏洞可能会导致代码执行和数据篡改。”

在生成式人工智能环境中，可信代码与不可信代码之间的界限可能很模糊，因此这个漏洞尤其令人担忧。

NVIDIA 已发布了 NeMo 框架的更新版本，以解决这些安全问题。更新后的版本为 25.02。强烈建议使用 NVIDIA NeMo 框架的用户尽快更新到 25.02 版本，以降低与这些漏洞相关的风险。

本文翻译自securityonline [原文链接](https://securityonline.info/nvidia-nemo-framework-high-risk-vulnerabilities-allow-remote-code-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306833](/post/id/306833)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/nvidia-nemo-framework-high-risk-vulnerabilities-allow-remote-code-execution/)

如若转载,请注明出处： <https://securityonline.info/nvidia-nemo-framework-high-risk-vulnerabilities-allow-remote-code-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**10赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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