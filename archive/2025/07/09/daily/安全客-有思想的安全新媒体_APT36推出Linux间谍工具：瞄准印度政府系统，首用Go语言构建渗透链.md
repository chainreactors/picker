---
title: APT36推出Linux间谍工具：瞄准印度政府系统，首用Go语言构建渗透链
url: https://www.anquanke.com/post/id/309551
source: 安全客-有思想的安全新媒体
date: 2025-07-09
fetch_date: 2025-10-06T23:16:27.451705
---

# APT36推出Linux间谍工具：瞄准印度政府系统，首用Go语言构建渗透链

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

# APT36推出Linux间谍工具：瞄准印度政府系统，首用Go语言构建渗透链

阅读量**54676**

发布时间 : 2025-07-08 16:45:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/apt36-unleashes-linux-malware-transparent-tribe-targets-indian-government-with-go-based-espionage-tools/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近日，**网络安全公司 CYFIRMA** 披露了一项新的网络攻击活动，显示出**巴基斯坦背景的APT组织APT36（又名Transparent Tribe）在攻击手法上的重大升级——首次将攻击目标转向基于Linux的系统。此次攻击明确针对印度政府内部广泛部署的BOSS Linux操作系统**，揭示出该组织不断进化的网络间谍策略。

“APT36对Linux平台投放专属恶意代码，标志着其攻击能力迈入新阶段，**同时也反映出政府及关键基础设施所面临的**网络间谍风险正不断上升。”报告指出。

攻击以一封**伪装成网络安全通告的钓鱼邮件**开始，邮件附带的**压缩包文件名为**“**Cyber-Security-Advisory.zip**”，内部包含一个看似无害的“.desktop”快捷方式文件。
但点击执行后，这个文件实际上会：

* **打开一个伪装的PowerPoint诱饵文件（slide.pptx）**，通过LibreOffice Impress展示，增强可信度；
* **同时在后台静默下载并运行一个名为BOSS.elf的恶意ELF二进制程序**。

> **“这一双重策略操作流程设计缜密，既迷惑受害者保持信任感**，又可在无察觉的情况下完成**恶意代码投放和执行**。”CYFIRMA强调。

该恶意程序由Go语言编写，**本地落地为client.elf文件**，使用`nohup`命令执行，确保**在用户退出后依旧持续运行**，并将所有执行输出重定向至`/dev/null`以实现**完全静默运行**。

**BOSS.elf主要具备以下核心功能：**

* **信息收集（Reconnaissance）**：获取系统主机名、CPU信息、内存配置、运行级别、启动脚本等；
* **持久化与规避检测**：借助`main.junkcalc2`模块记录日志，**避免被杀软发现**；
* **数据探测与外传**：利用`os.readDir`遍历文件系统，并通过`main.sendResponse`上传敏感数据；
* **屏幕监控**：调用Go语言库`github.com/kbinani/screenshot`，**截取用户桌面图像**。

恶意程序会连接至C2服务器：`101.99.92[.]182:12520`，**每隔30秒自动重连，确保通信稳定性与长期驻留**。

本次行动还使用了已知APT36基础设施域名`sorlastore.com`，**该域名此前被用于向Windows系统投放带有恶意宏的PowerPoint插件文件（PPAM）**。

**“这些攻击延续了APT36以钓鱼邮件为载体的战术，常通过冒充网络安全或国防通告**，投递伪装文件诱导受害者执行。”CYFIRMA补充道。

这项最新行动释放出明确信号：**以Linux为核心环境的政府机构和国防单位**，正面临来自APT组织**更具针对性与持续性的高危威胁**。建议所有使用Linux系统的公共部门单位，立即将该威胁提升为优先处理事项，强化检测与防御机制。”报告最后警告道。

本文翻译自securityonline [原文链接](https://securityonline.info/apt36-unleashes-linux-malware-transparent-tribe-targets-indian-government-with-go-based-espionage-tools/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309551](/post/id/309551)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/apt36-unleashes-linux-malware-transparent-tribe-targets-indian-government-with-go-based-espionage-tools/)

如若转载,请注明出处： <https://securityonline.info/apt36-unleashes-linux-malware-transparent-tribe-targets-indian-government-with-go-based-espionage-tools/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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