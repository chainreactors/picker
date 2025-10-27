---
title: Veeam 备份与复制漏洞曝光： 高严重性漏洞使数据面临风险
url: https://www.anquanke.com/post/id/302459
source: 安全客-有思想的安全新媒体
date: 2024-12-07
fetch_date: 2025-10-06T19:33:13.902832
---

# Veeam 备份与复制漏洞曝光： 高严重性漏洞使数据面临风险

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

# Veeam 备份与复制漏洞曝光： 高严重性漏洞使数据面临风险

阅读量**79179**

发布时间 : 2024-12-06 15:16:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/veeam-backup-replication-vulnerabilities-exposed-high-severity-flaws-put-data-at-risk/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-42448 & CVE-2024-42449]()

备份、恢复和数据管理解决方案的著名提供商 Veeam Software 发布了一个安全更新，以解决其 Veeam Backup & Replication 软件中的多个漏洞。这些漏洞有可能使经过验证的攻击者执行恶意代码，未经授权访问敏感信息，并破坏连接系统的完整性。

其中最严重的漏洞 CVE-2024-40717 的 CVSS v3.1 得分为 8.8，表示严重程度较高。该漏洞可使攻击者以提升的权限执行任意代码，从而可能导致整个系统被入侵。此更新解决的其他漏洞包括：

* **CVE-2024-42451：** 允許存取以人類可讀格式儲存的憑證。
* **CVE-2024-42452：**允許以提升的權限遠端上載檔案至連接的 ESXi 主機。
* **CVE-2024-42453:** 允許控制和修改連接的虛擬基礎結構主機。
* **CVE-2024-42455:** 助長不安全的反序列化，可能導致檔案刪除。
* **CVE-2024-42456：** 授予访问特权方法和控制关键服务的权限。
* **CVE-2024-42457：**通过远程管理界面暴露已保存的凭证。
* **CVE-2024-45204：** 利用凭证处理权限不足，可能导致 NTLM 哈希值泄漏。

另一个漏洞 CVE-2024-45207 影响 Microsoft Windows 的 Veeam Agent。当未受信任用户可写的目录被添加到 PATH 环境变量时，利用该漏洞可实现 DLL 注入。虽然默认的 Windows PATH 不包括此类目录，但在错误配置的环境中，风险仍然很大。

Veeam 已在 Veeam Backup & Replication 12.3（构建 12.3.0.310）和 Veeam Agent for Microsoft Windows 6.3（构建 6.3.0.177）中修复了这些漏洞，并敦促所有用户立即升级到该版本。作为临时缓解措施，Veeam 建议从备份服务器上的 “用户和角色 ”设置中删除任何不受信任或不必要的用户。

强烈建议依赖 Veeam Backup & Replication 的组织立即采取行动，保护其关键数据和基础设施。

本文翻译自securityonline [原文链接](https://securityonline.info/veeam-backup-replication-vulnerabilities-exposed-high-severity-flaws-put-data-at-risk/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302459](/post/id/302459)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/veeam-backup-replication-vulnerabilities-exposed-high-severity-flaws-put-data-at-risk/)

如若转载,请注明出处： <https://securityonline.info/veeam-backup-replication-vulnerabilities-exposed-high-severity-flaws-put-data-at-risk/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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