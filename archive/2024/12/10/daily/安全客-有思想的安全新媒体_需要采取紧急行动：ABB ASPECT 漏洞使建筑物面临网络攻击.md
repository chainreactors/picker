---
title: 需要采取紧急行动：ABB ASPECT 漏洞使建筑物面临网络攻击
url: https://www.anquanke.com/post/id/302544
source: 安全客-有思想的安全新媒体
date: 2024-12-10
fetch_date: 2025-10-06T19:33:08.149063
---

# 需要采取紧急行动：ABB ASPECT 漏洞使建筑物面临网络攻击

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

# 需要采取紧急行动：ABB ASPECT 漏洞使建筑物面临网络攻击

阅读量**54098**

发布时间 : 2024-12-09 14:47:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/urgent-action-needed-abb-aspect-vulnerabilities-expose-buildings-to-cyberattacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![ASPECT Vulnerabilities]()

ABB 针对其楼宇能源管理平台 ASPECT 系统发布了重要网络安全公告。该公告于2024年12月5日发布，详细描述了多个漏洞，这些漏洞可能允许攻击者远程控制该系统并执行恶意代码。

这些漏洞影响到 ASPECT 的不同版本，包括未经授权的访问和远程代码执行，以及跨站脚本和拒绝服务攻击。ABB 已将 CVSS v3.1 基本分高达 10.0，表明了这些漏洞的严重性。

该公告强调了许多漏洞，包括：

* **CVE-2024-6298 (CVSS 10)： 远程代码执行 (RCE)**
  输入验证不当可允许攻击者远程执行任意代码。ABB 指出，“攻击者可以成功利用这些漏洞，远程控制产品，并可能插入和运行任意代码”。
* **CVE-2024-6515 (CVSS 9.6)： 明文密码**
  密码可能以明文或 Base64 编码处理，增加了意外暴露凭证的风险。
* **CVE-2024-51551 (CVSS 10)： 默认凭据**
  使用公开默认凭据的设备容易受到未经授权的访问，因此需要立即更新凭据。
* **CVE-2024-51549 (CVSS 10)：绝对路径遍历**
  该漏洞可访问和修改非预期资源，带来重大安全风险。

该公告强调，ASPECT 设备的设计并非面向互联网。ABB 重申了之前向客户发出的警告，指出：“ASPECT 设备并非面向互联网。2023 年 6 月发布的产品公告向客户告知了这一参数。”

尽管如此，只有当攻击者能够访问安装了 ASPECT 并直接暴露于互联网的网段时，才能利用本公告中报告的漏洞。

ABB 感谢 Zero Science Lab 的 Gjoko Krstikj 负责任地报告了这些漏洞。公司已发布固件更新来解决这些问题，并敦促客户立即应用这些更新。

为降低风险，ABB 概述了以下即时步骤：

1. **断开暴露于互联网的设备的连接**
   移除任何直接连接到互联网或配置了不安全网络设置的 ASPECT 系统。
2. **升级固件**
   确保所有 ASPECT 产品更新到 3.08.03 或更新版本，以解决这些漏洞。
3. **实施安全访问控制**
   使用安全的虚拟专用网络（VPN）进行远程访问，并确保防火墙保护 ASPECT 安装。
4. **更改默认凭据**
   ABB强调，安装后立即更改默认密码至关重要。

更多信息，请访问ABB网络安全页面。

本文翻译自securityonline [原文链接](https://securityonline.info/urgent-action-needed-abb-aspect-vulnerabilities-expose-buildings-to-cyberattacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302544](/post/id/302544)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/urgent-action-needed-abb-aspect-vulnerabilities-expose-buildings-to-cyberattacks/)

如若转载,请注明出处： <https://securityonline.info/urgent-action-needed-abb-aspect-vulnerabilities-expose-buildings-to-cyberattacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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