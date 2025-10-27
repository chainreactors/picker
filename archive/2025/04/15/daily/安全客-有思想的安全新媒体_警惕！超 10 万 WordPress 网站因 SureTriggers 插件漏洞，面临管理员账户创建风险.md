---
title: 警惕！超 10 万 WordPress 网站因 SureTriggers 插件漏洞，面临管理员账户创建风险
url: https://www.anquanke.com/post/id/306504
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:11.743327
---

# 警惕！超 10 万 WordPress 网站因 SureTriggers 插件漏洞，面临管理员账户创建风险

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

# 警惕！超 10 万 WordPress 网站因 SureTriggers 插件漏洞，面临管理员账户创建风险

阅读量**51119**

发布时间 : 2025-04-14 14:54:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/100000-wordpress-sites-vulnerable/>

译文仅供参考，具体内容表达以及含义原文为准。

在 SureTriggers WordPress 插件中发现了一个严重漏洞，该漏洞影响超过 10 万个 WordPress 网站，攻击者有可能利用此漏洞创建未经授权的管理员账户。

这个漏洞被认定为 CVE-2025-3102，其通用漏洞评分系统（CVSS）评分为 8.1（高危），影响该插件直至 1.0.78 版本（包括 1.0.78 版本）的所有版本。

该漏洞专门针对那些安装并激活了此插件，但未正确配置 API 密钥的网站。

这一安全问题源于该插件在处理 REST API 端点时存在身份验证绕过的情况，它未能正确验证空的密钥值。

当该漏洞被利用时，攻击者可以利用这一疏忽在无需身份验证的情况下创建管理员账户，从而完全控制该网站。

一旦获得管理员权限，恶意行为者就可以上传后门程序、注入恶意软件、将用户重定向到钓鱼网站，或者在受影响的网站上插入垃圾内容。

Wordfence 的研究人员在 2025 年 3 月 13 日通过他们的漏洞赏金计划发现了这个漏洞。

安全研究人员 mikemyers 发现并负责任地报告了这个问题，因其发现获得了 1024 美元的赏金。发现该漏洞后，Wordfence 迅速通知了该插件的开发者 Brainstorm Force，后者于 2025 年 4 月 3 日发布了一个修复版本。

从技术层面来看，这个漏洞暴露出该插件在安全架构方面存在令人担忧的疏忽。

问题存在于处理该插件 REST API 端点权限检查的函数中。这个函数将请求头中的密钥与配置的密钥进行比较，但没有检查密钥是否为空。函数名为 autheticate\_user() 。

#### ****漏洞分析****

对存在漏洞的代码进行检查可以揭示身份验证绕过是如何发生的：

public function autheticate\_user($request) {

$secret\_key = $request->get\_header(‘st\_authorization’);

list($secret\_key) = sscanf($secret\_key, ‘Bearer %s’);

if ($this->secret\_key!== $secret\_key) {

return false;

}

return true;

}

关键缺陷在条件语句中很明显，该语句仅比较密钥是否不相等，而没有验证其中任何一个是否为空。

因此，当插件配置的密钥和攻击者提供的密钥都为空时，条件判断结果为真，攻击者就获得了对 REST API 端点的访问权限。

通过这个端点，攻击者可以执行 run\_action() 函数，在无需任何身份验证的情况下创建管理员账户。

强烈敦促 WordPress 网站管理员立即将插件更新到 1.0.79 版本。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/100000-wordpress-sites-vulnerable/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306504](/post/id/306504)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/100000-wordpress-sites-vulnerable/)

如若转载,请注明出处： <https://cybersecuritynews.com/100000-wordpress-sites-vulnerable/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

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