---
title: “LameHug” 恶意软件利用 AI 大模型实时生成 Windows 数据窃取指令
url: https://www.anquanke.com/post/id/310220
source: 安全客-有思想的安全新媒体
date: 2025-07-19
fetch_date: 2025-10-06T23:38:54.806287
---

# “LameHug” 恶意软件利用 AI 大模型实时生成 Windows 数据窃取指令

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

# “LameHug” 恶意软件利用 AI 大模型实时生成 Windows 数据窃取指令

阅读量**101723**

发布时间 : 2025-07-18 17:38:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/lamehug-malware-uses-ai-llm-to-craft-windows-data-theft-commands-in-real-time/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

乌克兰国家网络安全应急响应中心（CERT-UA）近日发现一类**新型恶意软件“LameHug”**，该恶意软件利用大型语言模型（LLM）在受感染的**Windows系统**中**实时生成并执行命令，实施数据窃取等活动**。

据CERT-UA通报，“LameHug”由**Python**编写，通过调用**Hugging Face**平台的接口，与名为**Qwen 2.5-Coder-32B-Instruct**的大模型进行交互。该模型由**阿里云开发，开源发布**，专用于**生成代码、进行逻辑推理并响应编程类指令请求**，可将自然语言描述转换为可执行的多种语言代码或终端命令。

CERT-UA在7月10日接到报告称，有攻击者从被入侵邮箱发送仿冒政府官员名义的恶意邮件，目标为**乌克兰行政管理机构**。邮件中包含一个压缩包附件，携带“LameHug”加载器，已发现的三个变种名称分别为**“Attachment.pif”、“AI\_generator\_uncensored\_Canvas\_PRO\_v0.9.exe”和“image.py”**。

![]()

*试图植入 LameHug 恶意软件的钓鱼邮件*

*来源：乌克兰国家网络事件响应团队（CERT-UA）*

CERT-UA初步分析认为，该攻击活动与俄罗斯国家支持的APT28组织有关，评估置信度为**“中等”**。

在此次攻击中，“LameHug”被用于**执行系统探测和数据窃取任务**，相关命令由大语言模型根据攻击者预设提示动态生成。具体包括：**收集系统信息并保存至info.txt文件；递归搜索Windows系统中的关键目录（如Documents、Desktop和Downloads）下的文档；并通过SFTP或HTTP POST方式将数据外传**。

![]()

*发送至大语言模型用于生成命令的提示词*

*来源：乌克兰国家网络事件响应团队（CERT-UA）*

据悉，“LameHug”是**首个**被公开披露的**集成大模型功能、用于实际攻击操作**的恶意软件。这一做法标志着**网络攻击方式可能进入新的阶段**，攻击者能够在入侵过程中**动态调整策略**，无需更新恶意载荷。

此外，该恶意软件利用**Hugging Face平台**进行命令交互，也可能用于**建立通信隐蔽的指令控制（C2）通道**，从而延长攻击潜伏期，**逃避检测**。

CERT-UA未透露LameHug所执行的大模型生成指令是否在攻击中取得成功。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/lamehug-malware-uses-ai-llm-to-craft-windows-data-theft-commands-in-real-time/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310220](/post/id/310220)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/lamehug-malware-uses-ai-llm-to-craft-windows-data-theft-commands-in-real-time/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/lamehug-malware-uses-ai-llm-to-craft-windows-data-theft-commands-in-real-time/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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