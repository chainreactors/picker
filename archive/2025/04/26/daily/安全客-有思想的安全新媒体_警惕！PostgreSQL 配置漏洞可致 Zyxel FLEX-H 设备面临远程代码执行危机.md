---
title: 警惕！PostgreSQL 配置漏洞可致 Zyxel FLEX-H 设备面临远程代码执行危机
url: https://www.anquanke.com/post/id/306874
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:04:03.338747
---

# 警惕！PostgreSQL 配置漏洞可致 Zyxel FLEX-H 设备面临远程代码执行危机

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

# 警惕！PostgreSQL 配置漏洞可致 Zyxel FLEX-H 设备面临远程代码执行危机

阅读量**77699**

发布时间 : 2025-04-25 10:32:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/zyxel-rce-vulnerability-authentication/>

译文仅供参考，具体内容表达以及含义原文为准。

Zyxel 的 FLEX-H 系列设备存在一个严重漏洞，攻击者可利用该漏洞执行任意数据库查询，并且无需进行身份验证就能获得远程代码执行的能力。

该漏洞由研究人员 rainpwn 发现，并于 2025 年 4 月 22 日被官方披露，这使得这些企业级安全设备面临潜在的毁灭性攻击风险。

该漏洞源于受影响设备上运行的 PostgreSQL 数据库服务的架构配置错误。通常情况下，PostgreSQL 仅限制在本地主机的 5432 端口进行访问，但攻击者可以通过 SSH 隧道绕过这一限制。

研究人员解释道：“通过端口转发的 SSH 隧道会将数据库服务暴露给外部访问，从而在远程系统与数据库之间创建一个直接的通信通道。”

这个漏洞尤其危险，因为访问数据库无需进行身份验证。一旦攻击者建立了 SSH 隧道，他们就可以对 PostgreSQL 实例自由执行任意 SQL 查询。

****Zyxel**** ****设备的远程代码执行漏洞****

攻击者利用了 PostgreSQL 强大但危险的 COPY FROM PROGRAM 函数，该函数允许执行系统命令。安全研究人员用以下代码展示了这一能力：

这个简单的查询可以获取敏感的系统信息，但攻击者可以轻松修改它，以生成反向 Shell 或执行其他恶意命令。

PostgreSQL 实例运行时具有足够的权限来实现系统级别的访问。

该漏洞是一个更广泛的攻击链的一部分，可能会导致系统被完全攻破。在以 postgres 用户身份获得初始访问权限后，攻击者可以：

1.利用竞态条件，即使拥有用户级别的权限也能建立 SSH 隧道。

2.从已登录的管理员那里窃取身份验证令牌。

3.通过系统的恢复管理功能上传恶意文件。

4.使用特制的 SetUID 二进制文件获取根级别访问权限。

研究人员表示：“通过利用这一能力，能够实现远程代码执行（RCE），成功执行系统命令以获取敏感的系统信息。”

****缓解措施****

Zyxel 已将 CVE-2025-1731 和 CVE-2025-1732 分配给这些漏洞，并于 2025 年 4 月 14 日发布了安全补丁。

受影响的企业机构应立即采取以下措施：

1.将所有Zyxel FLEX-H 系列设备的固件更新到最新版本。

2.实施网络分段，以限制管理访问。

3.监控 SSH 端口上的可疑连接尝试。

4.检查日志中是否存在异常的 PostgreSQL 活动。

该漏洞凸显了正确设置数据库访问控制和身份验证机制的至关重要性，即使对于那些原本只应在本地访问的服务也是如此。

使用 Zyxel FLEX-H 设备的企业机构应将此次更新视为一项紧急安全措施，因为在公开披露该漏洞后，很可能会迅速出现利用该漏洞的工具。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/zyxel-rce-vulnerability-authentication/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306874](/post/id/306874)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/zyxel-rce-vulnerability-authentication/)

如若转载,请注明出处： <https://cybersecuritynews.com/zyxel-rce-vulnerability-authentication/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**9赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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