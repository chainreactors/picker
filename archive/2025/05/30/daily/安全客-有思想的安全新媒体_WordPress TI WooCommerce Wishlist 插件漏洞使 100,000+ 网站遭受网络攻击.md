---
title: WordPress TI WooCommerce Wishlist 插件漏洞使 100,000+ 网站遭受网络攻击
url: https://www.anquanke.com/post/id/307980
source: 安全客-有思想的安全新媒体
date: 2025-05-30
fetch_date: 2025-10-06T22:23:23.956205
---

# WordPress TI WooCommerce Wishlist 插件漏洞使 100,000+ 网站遭受网络攻击

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

# WordPress TI WooCommerce Wishlist 插件漏洞使 100,000+ 网站遭受网络攻击

阅读量**89934**

发布时间 : 2025-05-29 15:27:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/wordpress-ti-woocommerce-wishlist-plugin-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

流行的 TI WooCommerce Wishlist 插件中的一个严重安全漏洞已使超过 100,000 个 WordPress 网站面临潜在的网络攻击，安全研究人员警告即将面临利用风险。

该漏洞被指定为 CVE-2025-47577，并被分配了最高 CVSS 分数 10.0，它使未经身份验证的攻击者能够将任意文件上传到受影响的网站，从而可能导致服务器完全受损。
TI WooCommerce Wishlist 插件为 WooCommerce 商店添加了愿望清单功能，已成为全球电子商务网站的重大安全责任。

该漏洞特别影响版本 2.9.2 和所有以前的版本，插件开发人员目前没有提供补丁版本。

鉴于其广泛部署和潜在攻击的严重性，该安全漏洞是最近几个月发现的最严重的 WordPress 插件漏洞之一。

Patchstack 分析师在例行安全评估中发现了这个关键漏洞，并立即尝试在 2025 年 3 月 26 日联系插件供应商。

然而，在近两个月没有收到开发人员的回应后，该安全公司于 2025 年 5 月 16 日将漏洞详细信息发布到他们的数据库中，随后于 2025 年 5 月 27 日发布了公开公告。

缺乏供应商响应使网站管理员除了从他们的安装中完全删除插件之外，别无选择。

## 技术感染机制

该漏洞源于插件的文件上传处理机制中的一个根本缺陷，特别是在函数中。`tinvwl_upload_file_wc_fields_factory`

此功能通过 WordPress 的原生功能处理文件上传，但故意禁用通常会防止恶意文件上传的关键安全验证。`wp_handle_upload`

有问题的代码展示了绕过 WordPress 内置安全措施的危险配置：-

```
function tinvwl_upload_file_wc_fields_factory( $file ) {
    if (!function_exists( 'wp_handle_upload' ) ) {
        require_once( ABSPATH . 'wp-admin/includes/file.php' );
    }
    $upload = wp_handle_upload(
        $file,
        [
            'test_form' => false,
            'test_type' => false,
        ]
    );
    return $upload;
}
```

严重安全故障通过 parameter 发生，该参数显式禁用通常会将上传限制为安全文件类型的文件类型验证。`'test_type' => false`

此配置允许攻击者将可执行的 PHP 文件直接上传到服务器，然后可以远程访问和执行这些文件以实现完全的系统入侵。

只有当 WC Fields Factory 插件同时处于活动状态时，才能利用该漏洞，从而创建一个影响插件用户群子集的特定攻击媒介。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/wordpress-ti-woocommerce-wishlist-plugin-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307980](/post/id/307980)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/wordpress-ti-woocommerce-wishlist-plugin-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/wordpress-ti-woocommerce-wishlist-plugin-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* [技术感染机制](#h2-0)

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