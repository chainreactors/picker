---
title: ZynorRAT攻击Windows和Linux系统以获取远程访问权限
url: https://www.anquanke.com/post/id/312104
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:24.126000
---

# ZynorRAT攻击Windows和Linux系统以获取远程访问权限

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

# ZynorRAT攻击Windows和Linux系统以获取远程访问权限

阅读量**56870**

发布时间 : 2025-09-12 17:33:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/zynorrat-attacking-windows-and-linux/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为ZynorRAT的新型复杂远程访问木马（RAT）已成为跨平台威胁，通过创新的Telegram命令与控制（C2）基础设施，针对Windows和Linux系统发起攻击。

该恶意软件于2025年7月首次被发现，采用Go语言编译，代表了远程访问能力的显著进化——融合传统RAT功能与现代通信渠道，以逃避检测并持久控制受感染系统。

ZynorRAT的攻击方法展现出极强的灵活性，将**Telegram机器人**作为受感染设备与威胁行为者之间的主要通信载体。攻击者可通过加密消息渠道下发命令、窃取数据、监控目标系统，其流量与合法通信高度融合，难以区分。利用主流消息平台实施恶意活动，反映了网络威胁的演变趋势——传统网络监控可能无法识别此类可疑通信。

ZynorRAT的**跨平台设计**使威胁行为者能够攻陷多样化计算环境，从企业Linux服务器到Windows工作站，在异构网络中构建统一攻击面。

![]()

Sysdig研究人员在常规威胁狩猎中发现了该恶意软件，并指出其独特的实现模式和跨平台兼容性，使其有别于现有RAT家族。

恶意软件的发现时间线显示其开发工作持续进行，上传至VirusTotal的多个样本检测率不断下降，表明开发者在积极改进逃避技术。

从监控的Telegram频道收集的情报显示，该恶意软件可能由讲土耳其语的行为者开发，证据指向一名代号为“halil”的开发者，其可能正准备将该工具在地下市场商用分发。

### **高级持久化与命令执行机制**

ZynorRAT针对不同目标平台实施复杂的持久化技术，体现开发者对不同操作系统管理实践的深入了解。

在Linux系统上，恶意软件通过在`~/.config/systemd/user/system-audio-manager[.]service`放置精心构造的服务定义文件，利用systemd用户服务实现持久化。这种方法借助用户特定的服务管理功能，往往能避开传统安全监控工具的检测。

```
[Unit]
Description=System Audio Core Service
After=network.target
[Service]
ExecStart=/home/user/.local/bin/audio
Restart=always
RestartSec=10
[Install]
WantedBy=default.target
```

该持久化机制会在恶意软件进程终止后每10秒自动重启，确保对受感染系统的持续控制。

命令执行能力不仅限于简单的shell访问，还包括通过`/fs_list`命令枚举文件系统、通过`/proc_list`和`/proc_kill`函数管理进程，以及通过`/metrics`命令收集全面系统信息——包括主机名、用户信息和通过查询`api.ipify.org` 获取的外部IP地址。

这些功能将受感染设备转变为全面的情报收集平台，为攻击者提供横向移动和数据窃取所需的详细环境感知能力。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/zynorrat-attacking-windows-and-linux/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312104](/post/id/312104)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/zynorrat-attacking-windows-and-linux/)

如若转载,请注明出处： <https://cybersecuritynews.com/zynorrat-attacking-windows-and-linux/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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