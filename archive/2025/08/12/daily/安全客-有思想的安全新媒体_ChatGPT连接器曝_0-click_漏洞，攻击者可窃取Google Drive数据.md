---
title: ChatGPT连接器曝"0-click"漏洞，攻击者可窃取Google Drive数据
url: https://www.anquanke.com/post/id/311088
source: 安全客-有思想的安全新媒体
date: 2025-08-12
fetch_date: 2025-10-07T00:16:44.725099
---

# ChatGPT连接器曝"0-click"漏洞，攻击者可窃取Google Drive数据

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

# ChatGPT连接器曝"0-click"漏洞，攻击者可窃取Google Drive数据

阅读量**75254**

发布时间 : 2025-08-11 17:18:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/chatgpt-0-click-connectors-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

OpenAI **ChatGPT Connectors** 功能中被发现存在严重漏洞，攻击者可在用户最初完成文件共享后，无需任何额外操作，就从已连接的 Google Drive 账户中窃取敏感数据。

这项攻击被命名为 **“AgentFlayer”**，代表了一类全新的、针对 AI 企业工具的零点击漏洞。该漏洞由 Zenity 的网络安全研究员 Michael Bargury 和 Tamir Ishay Sharbat 在拉斯维加斯 Black Hat 黑客大会上披露，他们现场演示了如何通过单个恶意文档，就能自动盗取受害者云端存储账户中的数据。

**ChatGPT Connectors** 于 2025 年初上线，可让 AI 助手与 Google Drive、SharePoint、GitHub、Microsoft 365 等第三方应用集成，支持用户搜索文件、获取实时数据，并基于个人业务数据提供上下文相关的回答。

![]()

### **“零点击”漏洞原理**

研究人员利用 **间接提示注入（Indirect Prompt Injection）** 技术实施攻击：在看似无害的文档中嵌入不可见的恶意指令（如将 1 像素的白色文字隐藏在白色背景中）。当 ChatGPT 处理该文档时，这些隐藏指令会操纵其行为。

“用户只需将来自不受信任来源的一个看似普通的文件上传到 ChatGPT——这几乎是日常操作。一旦上传，攻击就已经完成，不需要再点击任何东西。”Bargury 解释道。

攻击的过程是：受害者将“投毒”文档上传到 ChatGPT，或将其保存到自己的 Google Drive 中。即使只是发出“总结一下这份文件”这样的无害请求，也可能触发隐藏的恶意指令，让 ChatGPT 在受害者的 Google Drive 中搜索 API 密钥、凭证或机密文件等敏感信息。

![]()

研究人员利用 ChatGPT **渲染图片** 的能力作为主要数据外传方式。当隐藏指令发出时，ChatGPT 会将窃取的数据嵌入到图片 URL 的参数中，并在渲染图片时向攻击者控制的服务器自动发送 HTTP 请求。

### **绕过防护**

OpenAI 最初通过内部 “url\_safe” 接口对图片 URL 进行安全检查，但研究人员发现，可以使用 **Azure Blob Storage** URL 绕过这一防护，因为 ChatGPT 默认信任此类链接。

![]()

攻击者可将图片托管在 Azure Blob Storage 上，并利用 Azure Log Analytics 监控访问请求，从图片 URL 参数中获取外泄数据，同时伪装成使用合法的微软基础设施。

### **风险与影响**

这一漏洞对大量部署 ChatGPT Connectors 的企业环境构成严重威胁。若企业将该功能与 SharePoint 等关键业务系统集成（存放人力资源手册、财务文件或战略规划等），可能会引发大规模数据泄露。

研究人员指出，这一攻击并不限于 Google Drive——任何 ChatGPT 可连接的资源（如 GitHub、SharePoint、OneDrive 等）都可能成为数据外泄目标。

更令人担忧的是，该攻击绕过了传统的安全意识培训：即便员工已熟知防范钓鱼邮件或可疑链接，也可能中招，因为文档看似正常，而数据窃取过程完全隐蔽。

### **OpenAI 反应与挑战**

OpenAI 在接到漏洞通报后，迅速针对研究人员演示的具体攻击场景实施了缓解措施。但研究人员警告，底层架构性问题依然存在：

> “即便是看起来安全的 URL 也可能被滥用。如果某个 URL 被视为安全，攻击者就一定会找到利用它的办法。”

这一漏洞体现了 AI 企业工具面临的更广泛安全挑战。类似问题在业内并不罕见，例如微软 Copilot 的 “EchoLeak” 漏洞，以及其他 AI 助手遭遇的多种提示注入攻击。

开放式 Web 应用安全项目（OWASP）已将 **提示注入** 列为《2025 年 LLM 应用十大安全风险》之首，显示出此类威胁在 AI 系统中的普遍性。

### **防护建议**

安全专家建议采取以下措施来降低类似攻击的风险：

1. 对 AI 连接器的权限实施严格访问控制，遵循**最小权限原则；**

2. 部署专门用于监控 AI 智能体活动的安全解决方案；

3. 教育用户不要向 AI 系统上传来自不受信任来源的文档；

4. 在网络层面监控异常的数据访问模式；

5. 定期审计已连接的服务及其权限设置。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/chatgpt-0-click-connectors-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311088](/post/id/311088)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/chatgpt-0-click-connectors-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/chatgpt-0-click-connectors-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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