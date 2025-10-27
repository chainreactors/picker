---
title: 全球首例AI驱动勒索软件“PromptLock”已在野利用
url: https://www.anquanke.com/post/id/311538
source: 安全客-有思想的安全新媒体
date: 2025-08-28
fetch_date: 2025-10-07T00:18:26.197993
---

# 全球首例AI驱动勒索软件“PromptLock”已在野利用

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

# 全球首例AI驱动勒索软件“PromptLock”已在野利用

阅读量**71819**

发布时间 : 2025-08-27 17:49:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Amar Ćemanović，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/first-ai-powered-ransomware-promptlock-discovered-in-the-wild/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

ESET研究人员日前发现全球首例集成AI语言模型的勒索软件，该恶意软件能够**实时生成恶意代码**。被命名为”PromptLock”的勒索软件通过Ollama API本地调用OpenAI的gpt-oss:20b模型，实现跨平台动态脚本生成，显著提升攻击灵活性并增强规避检测能力。

该发现由ESET研究团队在分析VirusTotal上传的恶意样本后通过X平台公开。针对Windows和Linux环境的样本均采用Golang编写，被归类为Filecoder.PromptLock.A。ESET强调，PromptLock似乎是**尚在开发中的概念验证**，也可能是非恶意部署的实验性项目。但它的出现标志着勒索软件演进过程中的重大技术飞跃。

值得注意的是，PromptLock可通过向本地gpt-oss:20b模型输入硬编码提示词，按需生成Lua脚本。这些脚本用于文件系统枚举、选择性数据渗出和加密操作。该设计使PromptLock能跨Windows、macOS和Linux环境运行，无需单独编译版本，实现了勒索软件中罕见的**跨平台便携性**。

![]()

值得注意的是，该勒索软件并未嵌入整个大语言模型（否则会使二进制文件增加数GB容量），而是通过建立通往攻击者控制服务器的内部代理（运行Ollama API及模型）来规避此问题。这种隧道技术通常用于绕过网络限制，同时保持对外部资源的访问。

**PromptLock**与**LAMEHUG**存在战略相似性，当时攻击者利用HuggingFace的Qwen 2.5-Coder-32B-Instruct模型动态生成系统命令，使恶意软件获得跨环境自适应能力。但PromptLock通过本地集成模型实现了技术突破，支持离线生成恶意代码，彻底摆脱对外部API的依赖。

与传统依赖静态逻辑的恶意软件不同，集成AI的恶意软件能根据上下文、环境或系统数据实时调整行为，这对防御者应对新型威胁提出严峻挑战。

ESET建议防御者监测异常的Lua脚本执行行为（特别是涉及系统枚举或加密流程的脚本），并关注共享文件哈希值。网络管理员应检查出站连接中是否存在向LLM服务基础设施（尤其是通过Ollama API）进行代理隧道的迹象。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/first-ai-powered-ransomware-promptlock-discovered-in-the-wild/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311538](/post/id/311538)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/first-ai-powered-ransomware-promptlock-discovered-in-the-wild/)

如若转载,请注明出处： <https://cyberinsider.com/first-ai-powered-ransomware-promptlock-discovered-in-the-wild/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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