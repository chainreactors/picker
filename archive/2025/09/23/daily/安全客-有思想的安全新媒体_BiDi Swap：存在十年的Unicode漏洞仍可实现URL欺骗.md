---
title: BiDi Swap：存在十年的Unicode漏洞仍可实现URL欺骗
url: https://www.anquanke.com/post/id/312297
source: 安全客-有思想的安全新媒体
date: 2025-09-23
fetch_date: 2025-10-02T20:30:59.024416
---

# BiDi Swap：存在十年的Unicode漏洞仍可实现URL欺骗

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

# BiDi Swap：存在十年的Unicode漏洞仍可实现URL欺骗

阅读量**62620**

发布时间 : 2025-09-22 18:10:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/bidi-swap-a-decade-old-unicode-flaw-still-enables-url-spoofing/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Varonis威胁实验室团队发布了一份令人警醒的报告，揭示了现代浏览器在处理混合文本方向时存在的一个**持续十年以上的漏洞**。该漏洞名为“BiDi Swap”，允许攻击者构造看似合法的欺骗性URL，暗中将受害者重定向至其他网站。

核心问题在于浏览器对左到右（LTR，如英语）和右到左（RTL，如阿拉伯语）脚本的解析机制。Varonis指出：“通过利用浏览器处理RTL和LTR脚本的方式，攻击者可构造看似可信但实际指向恶意网站的URL。这种被称为BiDi Swap的方法常被用于钓鱼攻击。”

### **Unicode欺骗技术的历史与演变**

该漏洞源于Unicode的双向（Bidi）算法——一项旨在正确渲染混合语言文本的标准。但Varonis解释：“尽管双向算法通常能较好地处理域名，但在子域名和URL参数上存在缺陷。这一漏洞导致LTR-RTL混合URL可能无法按预期显示，为恶意行为打开了方便之门。”

此类问题并非首次出现，历史上已有多种Unicode欺骗技术：

1. **Punycode同形异义字攻击**：用近 identical 的西里尔字母或希腊字母替换拉丁字母（如“аpple.com ”冒充“apple.com ”）；
2. **RTL覆盖漏洞**：利用Unicode控制字符伪装恶意文件扩展名（如将“blafdp.exe ”显示为看似无害的“blaexe.pdf ”）。

这些案例均表明，文本处理的微小缺陷可能引发重大安全风险。

### **攻击示例：混合脚本伪造可信域名**

攻击者可通过混合脚本模仿可信域名：

```
https://varonis.com.ו.קום/parameter
https://ורוניס.קום.ו.קום/
```

乍看之下，这些伪造链接可能欺骗用户，使其误以为正在与合法网站交互。

### **浏览器厂商的修复现状**

尽管该问题已存在十余年，浏览器厂商仍未提供全面修复方案：

1. **Chrome**：“相似URL导航建议”功能提供部分保护，但测试显示仅标记特定域名（如“google.com ”），大量其他恶意URL仍可绕过检测；
2. **Firefox**：通过在地址栏高亮显示域名关键部分，帮助用户识别可疑链接；
3. **Edge**：微软团队虽将该问题标记为“已解决”，但URL显示逻辑未发生实质变化。

### **建议：用户警惕与厂商行动**

Varonis强调，**用户意识仍是关键**：“务必验证可疑URL，尤其是混合脚本或显示异常模式的链接。”团队同时呼吁浏览器开发者加强域名高亮和相似URL检测功能，组织应持续开展链接安全意识培训。

本文翻译自securityonline [原文链接](https://securityonline.info/bidi-swap-a-decade-old-unicode-flaw-still-enables-url-spoofing/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312297](/post/id/312297)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/bidi-swap-a-decade-old-unicode-flaw-still-enables-url-spoofing/)

如若转载,请注明出处： <https://securityonline.info/bidi-swap-a-decade-old-unicode-flaw-still-enables-url-spoofing/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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