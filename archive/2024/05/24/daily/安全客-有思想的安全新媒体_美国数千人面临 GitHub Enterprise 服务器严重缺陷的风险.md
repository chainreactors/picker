---
title: 美国数千人面临 GitHub Enterprise 服务器严重缺陷的风险
url: https://www.anquanke.com/post/id/296715
source: 安全客-有思想的安全新媒体
date: 2024-05-24
fetch_date: 2025-10-06T16:48:56.901575
---

# 美国数千人面临 GitHub Enterprise 服务器严重缺陷的风险

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

# 美国数千人面临 GitHub Enterprise 服务器严重缺陷的风险

阅读量**71870**

发布时间 : 2024-05-23 10:38:37

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/critical-github-enterprise-server-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

美国数千个使用 SAML 单点登录 (SSO) 身份验证的 GitHub Enterprise Server (GHES) 实例面临着因严重漏洞而引发的高风险，目前该漏洞已在开放互联网上出现概念验证漏洞。

GitHub Enterprise Server 是一个自托管的软件开发平台，可充当独立的虚拟设备。它使用 Git 版本控制、强大的 API、生产力和协作工具以及集成来帮助构建和交付软件。建议在受监管合规性约束的企业中使用GHES，这有助于避免公共云中的软件开发平台出现的问题。

GitHub 周一推出了修复程序，以解决 GitHub Enterprise Server 中的一个最严重漏洞，该漏洞可能允许攻击者绕过身份验证保护。

该严重缺陷被追踪为 CVE-2024-4985，在 CVSS 等级上具有最高的严重等级，因为它允许攻击者未经授权访问目标实例，而无需事先进行身份验证。

GitHub解释说：“在使用 SAML 单点登录 (SSO) 身份验证和可选加密断言功能的实例中，攻击者可以伪造 SAML 响应来配置和/或获得对具有管理员权限的用户的访问权限。”

GitHub 表示，默认情况下不启用加密断言。它进一步补充道：“不使用 SAML SSO 或使用没有加密断言的 SAML SSO 身份验证的实例不受影响。”

加密断言通过加密 SAML 身份提供商 (IdP) 发送的消息来提高 GHES 实例与 SAML SSO 的安全性。

GitHub 指出，该严重漏洞影响 3.13.0 之前的所有 GHES 版本。它已在版本 3.9.15、3.10.12、3.11.10 和 3.12.4 中修复。

然而，升级到最新补丁的用户可能会面临一些问题。此更新版本的已知问题有：

* 升级过程中将删除自定义防火墙规则。
* 在配置运行的验证阶段，Notebook 和 Viewscreen 服务可能会出现“无此对象”错误。此错误可以忽略，因为服务仍应正确启动。
* 如果根站点管理员在登录尝试失败后被锁定在管理控制台之外，则该帐户不会在定义的锁定时间后自动解锁。具有实例管理 SSH 访问权限的人员必须使用管理 shell 解锁该帐户。
* 如果实例配置为将日志转发到启用了 TLS 的目标服务器，则站点管理员使用 ghe-ssl-ca-certificate-install上传的证书颁发机构 (CA) 捆绑包 将不受尊重，并且与服务器的连接会失败。
* /var/log/mysql/mysql.err文件中的mbind ：不允许操作错误 可以忽略。当 不需要CAP\_SYS\_NICE功能时， MySQL 8 无法正常处理 ，而是输出错误而不是警告。
* 在 AWS 中托管的实例上，管理员重新启动实例后，系统时间可能会与 Amazon 的服务器失去同步。
* 在配置了 HTTP X-Forwarded-For 标头以在负载均衡器后面使用的实例上，该实例的审核日志中的所有客户端 IP 地址都错误地显示为 127.0.0.1。
* 在某些情况下，存储在存储库中的大型 .adoc 文件无法在 Web UI 中正确呈现。原始内容仍然可以以纯文本形式查看。
* 在集群配置中的实例上，如果 Redis 尚未正确重启，使用ghe-restore恢复备份 将过早退出。
* 在启用了 GitHub Actions 的实例上，部署 GitHub Pages 站点的 Actions 工作流可能会失败。
* 最初使用ghe-migrator导入的存储库将无法正确跟踪高级安全贡献。

**PoC 上市，数千人面临风险**
ODIN 是 Cyble 推出的一款用于攻击面管理和威胁情报的互联网搜索引擎，它发现，暴露在互联网上的近3,000 个Github Enterprise Server 实例容易受到 CVE-2024-4985 的攻击。

其中，目前未打补丁且面临被利用风险的实例数量最多 (209k)来自美国，其次是爱尔兰，有 331 个易受攻击的实例。

ODIN 的客户可以使用查询：services.modules.http.title：“Github Enterprise”来跟踪易受攻击的实例。

![GitHub 企业服务器]()
受 CVE-2024-4985 攻击的 GitHub Enterprise Server 的国家/地区分布（来源：Cyble 的 ODIN）
这个最严重的错误需要紧急修补，因为GitHub 本身现已提供概念验证。 GitHub 用户已经给出了有关 PoC 漏洞利用的分步指南，因此预计很快就会出现广泛的利用（如果尚未发生的话）。

本文翻译自 [原文链接](https://thecyberexpress.com/critical-github-enterprise-server-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296715](/post/id/296715)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/critical-github-enterprise-server-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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