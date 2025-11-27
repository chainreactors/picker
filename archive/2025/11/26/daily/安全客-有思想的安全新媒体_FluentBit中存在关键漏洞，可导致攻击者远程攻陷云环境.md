---
title: FluentBit中存在关键漏洞，可导致攻击者远程攻陷云环境
url: https://www.anquanke.com/post/id/313397
source: 安全客-有思想的安全新媒体
date: 2025-11-26
fetch_date: 2025-11-27T03:11:07.314609
---

# FluentBit中存在关键漏洞，可导致攻击者远程攻陷云环境

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

# FluentBit中存在关键漏洞，可导致攻击者远程攻陷云环境

阅读量**16660**

发布时间 : 2025-11-26 14:43:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/critical-fluentbit-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Fluent Bit 中发现的 **五个新的严重漏洞链** 已使数十亿容器化环境面临远程入侵风险。

Fluent Bit 是一款全球部署量超 **150 亿次** 的开源日志与遥测代理，是现代云基础设施的核心组件。该工具在银行系统、AWS 和微软 Azure 等云平台以及 Kubernetes 环境中收集、处理和转发日志。这种规模的组件一旦出现安全故障，不仅影响单个系统，还会 **波及整个云生态系统**。

这些新披露的漏洞允许攻击者通过未净化的标签操作实现 **身份验证绕过、未授权文件操作、远程代码执行和拒绝服务攻击**。攻击面覆盖多个关键功能：利用漏洞的攻击者可中断云服务、篡改数据、执行恶意代码并隐藏踪迹。通过控制日志服务行为，攻击者还能注入虚假遥测数据、将日志重定向至未授权目标，并篡改事件记录内容。

部分漏洞 **已超过八年未修复**，使云环境长期暴露在针对性攻击之下。Oligo Security 的安全研究人员与 AWS 合作，通过协调漏洞披露机制发现了这些缺陷。研究表明，基础设施核心组件的弱点可能引发复杂攻击链，影响全球数百万部署实例。

Oligo Security 分析师在对 Fluent Bit 的输入和输出插件进行全面安全评估后发现了这些漏洞，其研究团队指出 **身份验证机制、输入验证和缓冲区处理存在严重安全缺口**。发现后，他们立即与 AWS 及 Fluent Bit 维护者协作，最终在 4.1.1 版本中发布修复补丁。

### 路径遍历与文件写入漏洞技术分析

**CVE-2025-12972** 是漏洞链中最危险的缺陷之一。Fluent Bit 的 File 输出插件通过 `Path` 和 `File` 两个配置参数将日志直接写入文件系统。许多常见配置仅使用 `Path` 选项，并从记录标签派生文件名，但该插件在构建文件路径前 **未对标签进行净化**。攻击者可在标签值中注入 `../` 等路径遍历序列，突破预期目录限制并向系统任意位置写入文件。

![]()

由于攻击者可通过操纵日志内容部分控制写入文件的数据，他们能在关键系统位置创建恶意配置文件、脚本或可执行程序。当 Fluent Bit 以高权限运行时，此漏洞可直接导致远程代码执行。若 HTTP 输入配置了 `Tag_Key` 设置，且 File 输出未指定 `File` 参数，漏洞将极易被利用；使用 forward 输入结合文件输出的配置同样脆弱，允许未认证攻击者注入恶意标签并写入任意文件。

### 缓解措施与建议

![]()

所有运行 Fluent Bit 的组织 **必须立即更新至 4.1.1 或 4.0.12 版本**，并优先升级生产环境部署，同时调整配置以减少攻击面：

1. 使用静态预定义标签，消除不可信输入对路由和文件操作的影响
2. 在输出配置中显式设置 `Path` 和 `File` 参数，避免基于动态标签的路径构造
3. 以非 root 权限运行 Fluent Bit，并将配置文件挂载为只读，大幅降低漏洞利用危害

AWS 已完成内部系统加固，并建议所有客户立即升级。安全社区认为，这些漏洞暴露了开源安全报告中的系统性挑战——关键基础设施组件往往依赖资源有限的志愿维护者来应对协调式安全披露。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/critical-fluentbit-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313397](/post/id/313397)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/critical-fluentbit-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/critical-fluentbit-vulnerabilities/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **740**

* 粉丝
* **6**

### TA的文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44

### 相关文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44
* ##### [高级威胁组织ToddyCat升级攻击工具库，新型工具专门窃取Outlook邮件并劫持Microsoft 365访问令牌](/post/id/313434)

  2025-11-26 18:27:40
* ##### [威胁行为体利用Blender基金会官方文件作为载体，传播臭名昭著的StealC V2信息窃取木马](/post/id/313427)

  2025-11-26 18:26:53

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