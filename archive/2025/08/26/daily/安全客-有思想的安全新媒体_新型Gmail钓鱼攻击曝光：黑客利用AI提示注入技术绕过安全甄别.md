---
title: 新型Gmail钓鱼攻击曝光：黑客利用AI提示注入技术绕过安全甄别
url: https://www.anquanke.com/post/id/311451
source: 安全客-有思想的安全新媒体
date: 2025-08-26
fetch_date: 2025-10-07T00:17:58.254577
---

# 新型Gmail钓鱼攻击曝光：黑客利用AI提示注入技术绕过安全甄别

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

# 新型Gmail钓鱼攻击曝光：黑客利用AI提示注入技术绕过安全甄别

阅读量**79181**

发布时间 : 2025-08-25 17:50:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/gmail-phishing-with-prompt-injection/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

钓鱼攻击的本质始终是欺骗，但在此次攻击活动中，攻击者不仅针对用户进行欺诈，**更试图操纵基于AI的防御系统**。

该攻击是Anurag上周披露的Gmail钓鱼攻击链的升级版本。先前攻击依赖紧迫性诱导和页面跳转，而本次**引入了专门设计用于混淆自动化分析系统的隐藏AI指令**。

根据Anurag的分析，钓鱼邮件主题为：
**“Login Expiry Notice 2025年8月20日下午4:56:21”**
邮件正文警告收件人其密码即将失效，敦促其立即验证账户凭证。

对用户而言，这是典型的**社交工程攻击**：通过制造紧迫感、伪装Gmail官方品牌标识，**诱使用户不假思索地点击操作**。

### 针对AI的指令注入攻击

攻击的真正创新点对用户不可见。**隐藏在邮件源代码中的文本**，刻意模仿ChatGPT/Gemini等大语言模型的指令风格编写。

这种 **“提示注入”（prompt injection）攻击**旨在劫持安全运营中心（SOC）日益依赖的AI安全工具——这些工具通常用于威胁分类和分级处置。

Anurag指出：攻击通过**双轨并行策略同时针对人类心理与机器智能**。AI模型可能因注入的指令陷入冗长推理循环或生成无关结论，而非识别恶意链接并标记邮件。若攻击成功，将导致：

1. 自动化系统错误分类威胁
2. 关键警报延迟
3. 钓鱼邮件完全突破防御体系

### 攻击链技术解析

1. **邮件投递**
   邮件源自**SendGrid服务**：通过 **SPF/DKIM验证，****DMARC验证失败** → 仍进入收件箱
2. **可信跳板**
   初始链接使用**Microsoft Dynamics域名**构建可信首跳：
   `hxxps://assets-eur.mkt.dynamics.com/.../0cecd167-e07d...`
3. **反爬虫防护**
   跳转至含**CAPTCHA验证码**的页面：
   `hxxps://bwdpp.horkyrown.com/M6TJL@V6oUn07/`
4. **钓鱼页面**
   导向**Gmail主题登录页**含混淆JavaScript：
   `hxxps://bwdpp.horkyrown.com/yj3xbcqasiwzh2?id=[ 长ID]`
5. **环境检测**
   发起GeoIP请求收集数据：
   `hxxps://get.geojs.io/v1/ip/geo.json`
6. **信标验证**
   通过会话跟踪信标区分用户：
   `GET hxxps://6fwwke.glatrcisfx.ru/tamatar@1068ey`

此攻击标志着钓鱼策略的进化：攻击者构建**AI感知型威胁**毒化防御工具，迫使防御策略转向——组织需同时防护用户免受社交工程攻击及AI工具免受指令操纵。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/gmail-phishing-with-prompt-injection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311451](/post/id/311451)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/gmail-phishing-with-prompt-injection/)

如若转载,请注明出处： <https://cybersecuritynews.com/gmail-phishing-with-prompt-injection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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