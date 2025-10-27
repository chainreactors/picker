---
title: Palo Alto 修复了 PAN OS 和 Cortex XDR 中的漏洞
url: https://www.anquanke.com/post/id/297951
source: 安全客-有思想的安全新媒体
date: 2024-07-17
fetch_date: 2025-10-06T17:41:06.894464
---

# Palo Alto 修复了 PAN OS 和 Cortex XDR 中的漏洞

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

# Palo Alto 修复了 PAN OS 和 Cortex XDR 中的漏洞

阅读量**66404**

发布时间 : 2024-07-16 12:08:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Casi Cincuenta Monos，文章来源：Medium

原文地址：<https://casi-cincuenta-monos.medium.com/palo-alto-soluciona-vulnerabilidades-en-pan-os-y-cortex-xdr-ccb009e1b4ac>

译文仅供参考，具体内容表达以及含义原文为准。

检测到的第一个也是最严重的问题会影响 *Expedition 工具，该工具*有助于将配置从其他提供商迁移到 Palo Alto PAN-OS 平台。

如果组件的关键功能中缺少身份验证，攻击者将允许攻击者获得对管理员帐户的控制权，并访问系统导入的机密、凭据和其他数据。

CVE-2024–5910 和 CVSS 量表的严重性评分为 9.3。该错误会影响 1.2.92 之前的版本，并在其中进行了修复。

CVE-2024–5911 标记了一个 bug，该漏洞允许具有读/写管理员权限的攻击者将任意文件上传到系统，从而导致 Panorama 组件拒绝服务，该组件以分层方式管理一组*防火墙*。

在这种情况下，关键性评估为 7.0 分。反复利用此漏洞可能导致工具进入维护模式，需要手动干预才能将其恢复到正常操作模式。该错误已在 PAN-OS 版本 10.1.9、10.2.4 及更高版本中修复。

CVE-2024–5912 的 CVSS 等级严重程度为 6.8 分，会影响 8.2.2 和 7.9.102-CE 之前版本中的 XDR Cortex 代理。该错误是由错误的文件签名检查引起的，允许攻击者逃避未经授权的文件类型的执行块。

利用 CVE-2024–5913 需要对文件系统进行物理访问，这将允许攻击者在 11.2.1、11.1.4、11.0.5、10.2.10 和 10.1.14-h2 之前的 PAN-OS 版本中提升权限。该漏洞在 CVSS 量表上的严重程度为 5.4 分。

更臭名昭著的是 CVE-2024–3596，它被称为 *BlastRADIUS。*PAN-OS 中的此漏洞允许 Palo Alto 防火墙和 RADIUS 服务器之间进行中间*干预*者攻击，该服务器管理网络和 IT 资源访问中的身份验证、授权和可审计性。

利用此漏洞，需要使用 CHAP 或 PAP 协议配置服务器，攻击者能够逃避身份验证过程并将权限提升为超级用户。

失败是由于缺乏对这些协议对传输层安全性 （TLS） 的支持所致。不建议使用 CHAP 或 PAP，除非它们封装在加密连接中使用。

Palo Alto Networks 表示，在发布时，这些漏洞均未在攻击中检测到。

本文翻译自Medium [原文链接](https://casi-cincuenta-monos.medium.com/palo-alto-soluciona-vulnerabilidades-en-pan-os-y-cortex-xdr-ccb009e1b4ac)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297951](/post/id/297951)

安全KER - 有思想的安全新媒体

本文转载自: [Medium](https://casi-cincuenta-monos.medium.com/palo-alto-soluciona-vulnerabilidades-en-pan-os-y-cortex-xdr-ccb009e1b4ac)

如若转载,请注明出处： <https://casi-cincuenta-monos.medium.com/palo-alto-soluciona-vulnerabilidades-en-pan-os-y-cortex-xdr-ccb009e1b4ac>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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