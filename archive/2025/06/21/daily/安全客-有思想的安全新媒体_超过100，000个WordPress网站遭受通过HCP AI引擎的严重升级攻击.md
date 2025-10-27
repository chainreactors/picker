---
title: 超过100，000个WordPress网站遭受通过HCP AI引擎的严重升级攻击
url: https://www.anquanke.com/post/id/308696
source: 安全客-有思想的安全新媒体
date: 2025-06-21
fetch_date: 2025-10-06T22:53:07.041924
---

# 超过100，000个WordPress网站遭受通过HCP AI引擎的严重升级攻击

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

# 超过100，000个WordPress网站遭受通过HCP AI引擎的严重升级攻击

阅读量**104046**

发布时间 : 2025-06-20 16:57:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/100000-wordpress-sites-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

WordPress 生态系统中出现了一个严重的安全漏洞，通过 AI Engine 插件的模型上下文协议 （MCP） 实施，使超过 100,000 个网站面临权限提升攻击。

该漏洞被指定为 CVE-2025-5071，CVSS 评级高达 8.8，影响 AI 引擎插件版本 2.8.0 至 2.8.3，允许具有最低订阅者级别访问权限的经过身份验证的攻击者获得对目标 WordPress 网站的完全管理控制权。

该安全漏洞集中在插件的 MCP 功能中的授权机制不足上，它使 Claude 或 ChatGPT 等 AI 代理能够通过执行各种命令来控制和管理 WordPress 网站。

![]()![]()

该漏洞专门针对类中的函数，其中权限检查不充分会授予对强大 WordPress 管理功能的未经授权的访问。`can_access_mcp()``Meow_MWAI_Labs_MCP`

Wordfence 分析师于 2025 年 5 月 21 日在例行威胁情报作中发现了这一关键的安全漏洞，促使立即采取负责任的披露程序。

该漏洞的影响不仅限于简单的未经授权的访问，因为成功利用该漏洞后，攻击者能够执行 、 和 等命令，从而有效地通过权限提升实现整个站点入侵。`wp_update_user``wp_create_user``wp_update_option`

但是，该漏洞仅严重影响专门启用了 Dev Tools 并随后在其插件设置中激活了 MCP 模块的用户，该模块默认处于禁用状态。

攻击媒介利用插件的身份验证框架，攻击者可以在其中绕过安全控制并获得管理权限，随后使他们能够上传恶意插件、修改内容并在受感染的网站上建立持久的后门。

发现后，Wordfence Premium、Care 和 Response 用户于 2025 年 5 月 22 日收到了保护性防火墙规则，而免费用户于 2025 年 6 月 21 日收到了相同的保护。

## 技术身份验证绕过机制

该漏洞的核心在于函数中有缺陷的身份验证实现。`auth_via_bearer_token()`

原始易受攻击的代码包含一个严重的疏忽，即该函数无法正确验证空令牌值：-

```
public function auth_via_bearer_token( $allow, $request ) {
  if ( empty( $this->bearer_token ) ) {
    return false;
  }
  $hdr = $request->get_header( 'authorization' );
  if ( $hdr && preg_match( '/Bearer\s+(.+)/i', $hdr, $m ) &&
      hash_equals( $this->bearer_token, trim( $m[1] ) ) ) {
    return true;
  }
  return $allow;
}
```

此实现允许攻击者通过简单地省略 Bearer 令牌来绕过身份验证，从而导致函数返回默认值，对于已登录的用户，该值默认为 true。`$allow`

该补丁通过实施严格的管理员功能检查和全面的空值验证来解决此问题。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/100000-wordpress-sites-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308696](/post/id/308696)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/100000-wordpress-sites-exposed/)

如若转载,请注明出处： <https://cybersecuritynews.com/100000-wordpress-sites-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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

* [技术身份验证绕过机制](#h2-0)

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