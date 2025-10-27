---
title: AI Waifu RAT：新型恶意软件伪装AI助手劫持用户电脑
url: https://www.anquanke.com/post/id/311788
source: 安全客-有思想的安全新媒体
date: 2025-09-03
fetch_date: 2025-10-02T19:32:35.354300
---

# AI Waifu RAT：新型恶意软件伪装AI助手劫持用户电脑

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

# AI Waifu RAT：新型恶意软件伪装AI助手劫持用户电脑

阅读量**51117**

发布时间 : 2025-09-02 15:47:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/ai-waifu-rat-a-new-malware-masquerades-as-an-ai-assistant-to-hijack-your-pc/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员Ryingo近日发布针对新型恶意软件”**AI Waifu RAT**“的详细分析，该后门程序通过伪装成创新技术渗透大型语言模型（LLM）角色扮演社区。这份被称作”利用社区对’元交互’和新颖AI能力兴趣的社会工程学大师课”的报告，揭示了威胁分子如何利用用户好奇心和信任分发恶意软件。

该远程访问木马（RAT）最初出现在LLM角色扮演论坛，作者将其营销为允许AI角色”打破第四面墙”的研究项目。报告指出：”作者推介的工具让用户的AI角色’Win11虚拟伴侣’能够’与现实世界电脑交互’——被包装成令人兴奋的沉浸式功能。”宣传的”功能”包括读取本地文件以”了解用户”和支持任意代码执行（ACE）。分析明确表示：”这是经典的社会工程攻击……恶意文件被伪装成令人期待的软件增强功能。”

静态和动态分析显示，这个所谓的”代理”二进制文件实则是直接的远程访问木马。其架构包含在受害者机器上运行的本地代理，监听固定端口并通过明文HTTP请求接受命令。暴露的三个关键端点包括：

1. **/execute\_trusted**：未经用户同意直接在PowerShell执行命令，”使所有安全防护失效”；
2. **/execute**：包含面向用户的同意检查，但因信任端点存在而可被绕过；
3. **/readfile**：从磁盘读取任意文件并外泄至C&C服务器。

报告警告：”该框架是可扩展的高风险RAT。攻击者可随时通过**LLM C&C**推送静默更新或下达命令，部署更高级的恶意软件如勒索软件、信息窃取器或键盘记录器。”Ryingo强调了该设计实现的多种攻击场景：

1. 作者直接滥用：对受感染系统的完全远程控制；
2. 第三方劫持：明文C&C允许中间人（MITM）攻击；
3. 路过式攻击：恶意网站可向固定本地端口发送特制请求；
4. 供应链污染：通过提供恶意API作为免费”服务”，诱使用户授予后门访问权限。

虽然技术层面不算复杂，但该木马的真实有效性在于心理操纵。作者将杀毒软件/端点检测（AV/EDR）的检测结果称为误报，并明确告诉用户禁用防护：”如果您的防病毒软件报警，请将其加入白名单或暂时关闭。”Ryingo解释称，该策略之所以有效，是因为利用了：小众社区内部的信任、用户对”高级功能”的渴望、以及将安全警告视为误报的文化。

研究人员还检查了作者早期项目，包括所谓的”CTF挑战”二进制文件。这远非教育性谜题，而是包含持久化机制、反调试技巧和破坏性行为（如在多次错误输入后强制关闭用户电脑）。Ryingo结论明确：”这不是’挑战’，而是纯粹的破坏行为。”作者反复使用eval()和系统调用等不安全模式，强化了其项目更像是伪装恶意软件而非研究的观点。

本文翻译自securityonline [原文链接](https://securityonline.info/ai-waifu-rat-a-new-malware-masquerades-as-an-ai-assistant-to-hijack-your-pc/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311788](/post/id/311788)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ai-waifu-rat-a-new-malware-masquerades-as-an-ai-assistant-to-hijack-your-pc/)

如若转载,请注明出处： <https://securityonline.info/ai-waifu-rat-a-new-malware-masquerades-as-an-ai-assistant-to-hijack-your-pc/>

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