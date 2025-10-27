---
title: 新型“Plague” PAM 后门曝光：关键 Linux 系统面临静默凭证窃取风险
url: https://www.anquanke.com/post/id/310859
source: 安全客-有思想的安全新媒体
date: 2025-08-05
fetch_date: 2025-10-07T00:17:40.953011
---

# 新型“Plague” PAM 后门曝光：关键 Linux 系统面临静默凭证窃取风险

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

# 新型“Plague” PAM 后门曝光：关键 Linux 系统面临静默凭证窃取风险

阅读量**96352**

发布时间 : 2025-08-04 17:17:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员近日披露了一种此前未被发现的 Linux 后门程序，被命名为 **Plague（瘟疫）**，它已经在未被察觉的情况下潜伏了一年之久。

据 Nextron Systems 的研究员 Pierre-Henri Pezier 表示：“该后门被构建为一个恶意的 PAM（可插拔认证模块），允许攻击者悄无声息地绕过系统认证，并持续获取 SSH 访问权限。”

PAM（Pluggable Authentication Modules）是一组用于管理 Linux 和类 UNIX 系统中用户认证的共享库。由于 PAM 模块会被加载到具有高权限的认证进程中，一旦被植入恶意模块，就可能被用于**窃取用户凭证、绕过认证检查，并规避安全工具的检测**。

该安全公司表示，自 2024 年 7 月 29 日起，他们在 VirusTotal 上发现了多个与 Plague 有关的样本，但无一被杀毒引擎识别为恶意文件。这一发现不仅说明该后门具备极强的隐蔽性，也表明背后不明攻击者仍在持续开发这一恶意工具。

Plague 拥有四项关键功能：

**1. 内置静态凭证，实现秘密访问；**

**2. 通过反调试机制和字符串混淆来抵御分析与逆向工程；**

**3. 利用环境变量清除机制增强隐匿性；**

**4. 擦除 SSH 会话痕迹，避免被审计追踪。**

为了不留下操作痕迹，Plague 会通过 `unsetenv` 删除诸如 `SSH_CONNECTION` 和 `SSH_CLIENT` 等环境变量，并将 `HISTFILE` 重定向至 `/dev/null`，防止 shell 命令被记录。

Pezier 指出：“Plague **深度集成于认证流程中**，能在系统升级后依旧存活，并几乎不会留下可供取证的痕迹。配合其多层次的代码混淆和环境变量篡改行为，使得传统检测工具极难发现其存在。”

这类隐蔽性极高的后门对 Linux 系统构成了严重威胁，提醒各方务必加强 PAM 模块的完整性检测和访问控制。

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310859](/post/id/310859)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html)

如若转载,请注明出处： <https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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