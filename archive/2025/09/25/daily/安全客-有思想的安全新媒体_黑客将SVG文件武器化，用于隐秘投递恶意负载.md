---
title: 黑客将SVG文件武器化，用于隐秘投递恶意负载
url: https://www.anquanke.com/post/id/312351
source: 安全客-有思想的安全新媒体
date: 2025-09-25
fetch_date: 2025-10-02T20:37:55.427252
---

# 黑客将SVG文件武器化，用于隐秘投递恶意负载

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

# 黑客将SVG文件武器化，用于隐秘投递恶意负载

阅读量**115134**

发布时间 : 2025-09-24 16:44:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-weaponizing-svg-files/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期针对拉丁美洲的一场攻击活动显示，攻击者正利用**包含嵌入式恶意载荷的超大SVG文件**分发AsyncRAT——一种能够全面攻陷系统的强大远程访问木马。

该活动通过精心构造的钓鱼邮件启动，邮件**冒充司法系统等合法机构**，以虚构的法律程序或法院传票制造紧迫感。受害者收到声称涉及诉讼或官方文件需立即处理的消息，被迫在未充分检查的情况下打开附件中的SVG文件。

与需要外部命令控制基础设施的传统恶意软件活动不同，这些**武器化SVG文件自身包含完整的恶意包**。这种被称为“**SVG走私**”的技术，利用可缩放矢量图形（SVG）基于XML的特性，将脚本、交互元素和编码载荷直接嵌入看似无害的图像文件中。

![]()

Welivesecurity分析师指出，这些文件通常超过**10 MB**（远大于普通图形文件），在网页浏览器中打开时会立即渲染出**伪造的政府门户网站**。攻击者似乎利用人工智能工具为单个目标生成定制文件，每个受害者收到的SVG文件均填充随机数据，以规避基于特征的检测系统。

### **感染机制与载荷投递：多阶段欺骗与动态组装**

感染过程通过精心设计的**多阶段工作流**展开，在维持受害者注意力的同时下载恶意组件。

当用户点击SVG附件时，默认网页浏览器会渲染一个模仿哥伦比亚司法系统的**精致伪造门户**，包含官方徽标、政府风格设计和动态进度指示器。

恶意SVG文件中嵌入的JavaScript模拟文件验证过程，显示逼真的进度条和状态消息（如“Verificando documentos oficiales”和“30% completado”）以增强真实性。

在这一“表演”期间，脚本会悄悄组装并部署包含最终AsyncRAT载荷的**密码保护ZIP压缩包**。嵌入的代码包含base64编码的二进制数据，这些数据会被实时解码和组装：

```
const payloadData = "UESDBBQACQgIAGxD+VpRqIWSufYYACn8GAAxAAAAMDFfREVNQU5EQSBQRU5BTCBQT1IgRUwgSlVaR0FETyAwMS...";
const binaryString = atob(payloadData);
const bytes = new Uint8Array(binaryString.length);
```

该活动还采用**DLL侧载技术**，让合法应用程序加载恶意库，使最终的AsyncRAT载荷能与正常系统进程融合，从而逃避检测。

检测遥测数据显示，攻击呈现系统性部署模式，2025年8月的**每周中段出现攻击高峰**，主要针对哥伦比亚用户。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-weaponizing-svg-files/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312351](/post/id/312351)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-weaponizing-svg-files/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-weaponizing-svg-files/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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