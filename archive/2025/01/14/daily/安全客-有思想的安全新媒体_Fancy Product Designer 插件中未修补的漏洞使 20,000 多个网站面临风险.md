---
title: Fancy Product Designer 插件中未修补的漏洞使 20,000 多个网站面临风险
url: https://www.anquanke.com/post/id/303456
source: 安全客-有思想的安全新媒体
date: 2025-01-14
fetch_date: 2025-10-06T20:04:34.908620
---

# Fancy Product Designer 插件中未修补的漏洞使 20,000 多个网站面临风险

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

# Fancy Product Designer 插件中未修补的漏洞使 20,000 多个网站面临风险

阅读量**54268**

发布时间 : 2025-01-13 14:24:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/unpatched-vulnerabilities-in-fancy-product-designer-plugin-put-20000-websites-at-risk/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-51919 & CVE-2024-51918]()

Patchstack 的安全研究员拉菲-穆罕默德（Rafie Muhammad）在最近的一份安全公告中发现了 Fancy Product Designer 插件中的关键漏洞。该插件由 Radykal 开发，销量已超过 20,000 件，以允许用户自由设计和个性化产品而闻名。然而，由于发现了严重的安全漏洞，数千个 WordPress 网站面临风险。

Fancy Product Designer 插件受两个重大漏洞的影响：

1. **未经验证的任意文件上传 (CVE-2024-51919)：** 该漏洞的 CVSS 得分为 9.0，允许未经身份验证的用户向服务器上传任意文件，包括恶意 PHP 文件。漏洞存在于 save\_remote\_file 和 fpd\_admin\_copy\_file 函数中。由于输入验证不足，攻击者可利用这些函数实现远程代码执行（RCE）。正如 Rafie Muhammad 解释的那样：”由于这两个函数没有适当的检查，如果有任何代码在没有额外文件检查的情况下利用这些函数，那么我们就可以实现任意文件上传。”
2. **未经验证的 SQL 注入（CVE-2024-51818）：** 该漏洞的 CVSS 得分为 9.3，允许未经身份验证的用户在数据库上执行任意 SQL 查询。根本原因在于 get\_products\_sql\_attrs 函数未能正确处理用户输入。Muhammad 强调指出：”在这种情况下，strip\_tags 函数本身并不足以防止 SQL 注入，因为该函数实际上只能清除 HTML、XML 和 PHP 标记。这一问题可能导致重大数据泄露或未经授权的数据库修改。

截至报告发布时，这些漏洞在最新插件版本 6.4.3 中仍未得到修补。强烈建议使用 Fancy Product Designer 插件的网站管理员采取以下措施：

* 立即禁用该插件。
* 监控供应商的网站和官方渠道，以获取有关修补程序的更新。
* 使用网络应用程序防火墙 (WAF) 检测和阻止利用企图。

本文翻译自securityonline [原文链接](https://securityonline.info/unpatched-vulnerabilities-in-fancy-product-designer-plugin-put-20000-websites-at-risk/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303456](/post/id/303456)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/unpatched-vulnerabilities-in-fancy-product-designer-plugin-put-20000-websites-at-risk/)

如若转载,请注明出处： <https://securityonline.info/unpatched-vulnerabilities-in-fancy-product-designer-plugin-put-20000-websites-at-risk/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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