---
title: 黑客利用嵌入恶意 JavaScript 的 SVG 文件在 Windows 系统执行恶意软件
url: https://www.anquanke.com/post/id/310952
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:42.018373
---

# 黑客利用嵌入恶意 JavaScript 的 SVG 文件在 Windows 系统执行恶意软件

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

# 黑客利用嵌入恶意 JavaScript 的 SVG 文件在 Windows 系统执行恶意软件

阅读量**56113**

发布时间 : 2025-08-08 16:57:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-weaponizing-svg-files-with-malicious-embedded-javascript/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子开始**将可缩放矢量图形（SVG）文件武器化**，把看似无害的图片文件变成能够在 Windows 系统上**执行恶意 JavaScript 的复杂钓鱼工具**。

这种新兴威胁利用了 **SVG 文件基于 XML 的结构**，在文件中嵌入并执行恶意脚本。当用户在默认浏览器中打开这些文件时，脚本会被自动触发，从而绕过传统主要针对可执行文件的安全防护。

与存储像素数据的标准图像格式（如 JPEG、PNG）不同，SVG 文件使用 **XML 代码**来定义矢量路径、形状和文字。这一根本差异给攻击者提供了可乘之机——他们可以将 JavaScript 代码嵌入文件结构中，并在用户用浏览器打开文件时自动执行。

这种攻击主要针对 **Windows 系统**，因为在该环境中，SVG 文件通常会默认在**浏览器**中打开，从而实现**无需额外操作即可运行脚本**的效果。

Seqrite 安全研究人员发现了一起采用该技术的精密攻击行动。攻击者**通过鱼叉式钓鱼邮件投递恶意 SVG 文件**，邮件主题具有迷惑性，例如“您预定活动的提醒”，附件文件名则为“Upcoming Meeting.svg”（即将召开的会议）或“Your-to-do-List.svg”（您的待办事项清单）等。

![]()

*SVG攻击链全解析（数据来源：Seqrite安全团队）*

为了绕过邮件安全过滤，这一行动还利用 **Dropbox、Google Drive、OneDrive** 等云存储平台分发恶意文件。

此次攻击展现了极高的技术复杂度。威胁行为者运用了多种规避手段，以维持**持久性**并避免被传统安全方案检测到。

## 技术感染机制与代码混淆

恶意 SVG 文件在 CDATA 段中嵌入 `<script>` 标签，以隐藏恶意逻辑，防止被基础内容扫描器发现。安全研究人员发现，**攻击者使用一个十六进制编码的字符串变量（Y）与一个简短的异或（XOR）密钥（q）进行载荷混淆**。

在处理时，这段编码数据会被解密为可执行的 JavaScript，并利用以下语句重定向受害者：

```
window.location = 'javascript:' + v;
```

成功解密后，载荷会**将用户重定向至命令与控制（C2）基础设施**——具体为 `hxxps://hju[.]yxfbynit[.]es/koRfAEHVFeQZ!bM9`，该地址先通过 Cloudflare 的 CAPTCHA 网关，再展示高度逼真的 Office 365 登录页面，用于窃取用户凭据。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-weaponizing-svg-files-with-malicious-embedded-javascript/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310952](/post/id/310952)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-weaponizing-svg-files-with-malicious-embedded-javascript/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-weaponizing-svg-files-with-malicious-embedded-javascript/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [技术感染机制与代码混淆](#h2-0)

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