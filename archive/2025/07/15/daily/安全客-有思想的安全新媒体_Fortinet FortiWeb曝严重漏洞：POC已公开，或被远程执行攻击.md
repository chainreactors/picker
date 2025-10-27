---
title: Fortinet FortiWeb曝严重漏洞：POC已公开，或被远程执行攻击
url: https://www.anquanke.com/post/id/309976
source: 安全客-有思想的安全新媒体
date: 2025-07-15
fetch_date: 2025-10-06T23:16:40.401538
---

# Fortinet FortiWeb曝严重漏洞：POC已公开，或被远程执行攻击

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

# Fortinet FortiWeb曝严重漏洞：POC已公开，或被远程执行攻击

阅读量**73302**

发布时间 : 2025-07-14 17:25:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源： securityaffairs 2

原文地址：<https://securityaffairs.com/179874/security/patch-immediately-cve-2025-25257-poc-enables-remote-code-execution-on-fortinet-fortiweb.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Fortinet FortiWeb 产品中编号为 CVE-2025-25257 的高危漏洞（CVSS 评分 9.8）目前已公开可被利用的概念验证（PoC）代码，攻击者可借此在未认证状态下远程执行命令，对尚未修复的服务器构成严重威胁。

该漏洞属于典型的 SQL 注入（CWE-89），允许未认证的远程攻击者通过特制的 HTTP 或 HTTPS 请求执行未授权的 SQL 指令，从而进一步实现对系统的控制。Fortinet 在安全公告中指出：**“FortiWeb 中存在 SQL 注入漏洞（CWE-89），未经身份验证的攻击者可通过构造特定的 HTTP 或 HTTPS 请求执行未授权的 SQL 指令或命令。”**

Fortinet 已在以下版本中发布补丁修复该问题：7.6.4、7.4.8、7.2.11 和 7.0.11。该漏洞由 GMO Cybersecurity 的 Kentaro Kawane 通过负责任披露渠道提交。

安全公司 watchTowr 在最新分析中，通过对比 Fortinet httpsd 服务的 7.6.3 和 7.6.4 两个版本，识别出官方修复引入的关键变更，并确认了补丁内容。研究人员在发现 SQL 注入漏洞后，进一步探索如何将其升级为远程代码执行（RCE）攻击。

他们首先尝试利用 MySQL 的 `INTO OUTFILE` 语句将任意文件写入服务器。通常这类操作会受限于数据库用户权限，但由于配置不当，攻击者在此次案例中竟可以 root 权限写入文件，显著提升了利用的可行性与破坏性。

虽然最初尝试向启用 CGI 的目录写入 Web Shell 失败（因文件无法执行），研究团队巧妙转向了另一种攻击路径。他们发现 CGI 目录中存在一个由 Apache 通过 /bin/python 执行的脚本 `ml-draw.py`，并利用 Python `.pth` 文件的隐蔽机制，在 Python 的 site-packages 目录中植入恶意代码。一旦被导入，`.pth` 文件即可执行如 `import os` 之类的命令，触发任意代码执行。

在绕过 `INTO OUTFILE` 的文件大小和路径限制后，研究人员最终成功利用该漏洞，实现了通过触发 CGI 脚本执行任意 Python 代码的攻击链。

值得注意的是，watchTowr 还发布了一个 **检测工件生成器（Detection Artifact Generator）**，用于协助安全团队检测 FortiWeb 中该漏洞的潜在利用行为。

尽管目前尚无 CVE-2025-25257 被实际利用的公开案例，但由于概念验证代码已经流传，安全专家强烈建议管理员尽快部署官方补丁，以防漏洞被大规模武器化利用。

本文翻译自 securityaffairs 2 [原文链接](https://securityaffairs.com/179874/security/patch-immediately-cve-2025-25257-poc-enables-remote-code-execution-on-fortinet-fortiweb.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309976](/post/id/309976)

安全KER - 有思想的安全新媒体

本文转载自:  [securityaffairs 2](https://securityaffairs.com/179874/security/patch-immediately-cve-2025-25257-poc-enables-remote-code-execution-on-fortinet-fortiweb.html)

如若转载,请注明出处： <https://securityaffairs.com/179874/security/patch-immediately-cve-2025-25257-poc-enables-remote-code-execution-on-fortinet-fortiweb.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**7赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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