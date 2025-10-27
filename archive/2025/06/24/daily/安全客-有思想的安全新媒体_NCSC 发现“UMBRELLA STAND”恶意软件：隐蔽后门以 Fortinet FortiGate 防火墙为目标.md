---
title: NCSC 发现“UMBRELLA STAND”恶意软件：隐蔽后门以 Fortinet FortiGate 防火墙为目标
url: https://www.anquanke.com/post/id/308777
source: 安全客-有思想的安全新媒体
date: 2025-06-24
fetch_date: 2025-10-06T22:52:18.425085
---

# NCSC 发现“UMBRELLA STAND”恶意软件：隐蔽后门以 Fortinet FortiGate 防火墙为目标

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

# NCSC 发现“UMBRELLA STAND”恶意软件：隐蔽后门以 Fortinet FortiGate 防火墙为目标

阅读量**50645**

发布时间 : 2025-06-23 15:55:07

**x**

##### 译文声明

本文是翻译文章，文章来源：https://securityonline.info/ncsc-uncovers-umbrella-stand-malware-stealthy-backdoor-targets-fortinet-fortigate-firewalls/

译文仅供参考，具体内容表达以及含义原文为准。

![]()

英国国家网络安全中心 （NCSC） 发现了一个名为 UMBRELLA STAND 的新恶意软件活动，揭示了一个通过隐蔽后门访问和加密通信针对 Fortinet FortiGate 100D 防火墙的复杂框架。这一发现引发了人们对针对关键网络基础设施的持续网络间谍活动的严重担忧。

根据[该报告](https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/umbrella-stand/ncsc-mar-umbrella_stand.pdf)，“*UMBRELLA STAND 是一组参与者二进制文件，可能通过利用目标设备中的安全漏洞来部署……旨在促进对给定目标网络的长期访问*。该恶意软件旨在在嵌入式设备中运行，使攻击者能够执行 shell 命令、配置命令和控制 （C2） 服务器并纵系统行为——同时在很大程度上未被发现。

该恶意软件由几个相互关联的组件组成，包括：

* blghtd – 主网络和任务二进制文件
* jvnlpe – 确保 blghtd 持久性的看门狗进程
* cisz – 初始设置和加载器模块
* libguic.so – LD\_PRELOAD共享对象以加载其他组件
* reboot\_hooker – 挂接到重启进程以实现持久性
* a – 基于 AES 的文件加密器/解密器
* BusyBox、nbtscan、tcpdump – 帮助网络侦查和数据泄露的公共设施

NCSC 指出，“*已观察到 UMBRELLA STAND 与一组公开可用的工具一起部署，包括：BusyBox、nbtscan、tcpdump 和 openLDAP。*

该恶意软件的突出特点之一是它在端口 443 上使用虚假的 TLS 信标来掩盖与其 C2 基础设施的通信。尽管模仿了合法的 TLS 1.0 标头 （17 03 01），但没有发生真正的握手。这种策略被归类为 MITRE ATT&CK T1001.003（协议模拟）。

“*观察使用 TLS 数据响应而不执行握手的服务器可能表明存在可疑活动*，”NCSC 报告警告说。

该恶意软件使用 AES-CBC 加密和固定的 IV 来存储其消息，并通过主机名的翻转 CRC32 哈希来识别受感染的主机，从而允许 C2 保持会话持久性。

UMBRELLA STAND 支持广泛的命令和数据泄露功能：

* Shell 命令执行（通过 BusyBox/ash）
* 以 6000 字节的块读取文件
* 使用 .ini 文件的命令分块和异步执行跟踪
* 信标间隔重新配置和 C2 地址覆盖

UMBRELLA STAND 经过精心设计，可在重启后继续运行并通过以下方式逃避管理检测：

* Reboot hooking — 在系统重启时执行加载程序二进制文件
* ld.so.preload 劫持 — 利用动态链接器注入
* 隐藏目录 — 例如 /data2/.ztls/
* 进程伪装 — 将进程名称替换为 /bin/httpsd

“*UMBRELLA STAND 修改了其进程名称……可执行文件名称和假字符串之间的任何长度差异都用空字节填充*，”报告详细说明。

此外，FortiOS 的原生安全功能被重新利用，通过在 sysctl 二进制文件中滥用字符串替换来隐藏恶意软件的存在。

关键入侵指标 （IOC） 包括：

* C2 IP：`89.44.194.32`
* 隐藏路径：`/data2/.ztls/`
* AES 加密堆栈字符串
* 伪装的进程名称：`/bin/httpsd`
* 注入工具：到 PID 1 中（init 进程）`SYSV664564856`

NCSC 还发布了几条强大的 YARA 规则来检测恶意软件的加密和纯文本变体，确保防御者即使应用了混淆也可以捕捉到威胁的迹象。

有趣的是，NCSC 指出“*在 UMBRELLA STAND 和 COATHANGER 中观察到的加载组件之间具有相当大的相似性*。”两种菌株都利用了持久的钩子机制和模块化的二进制加载器，表明了共享的工具链或开发谱系。

本文翻译自https://securityonline.info/ncsc-uncovers-umbrella-stand-malware-stealthy-backdoor-targets-fortinet-fortigate-firewalls/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308777](/post/id/308777)

安全KER - 有思想的安全新媒体

本文转载自: https://securityonline.info/ncsc-uncovers-umbrella-stand-malware-stealthy-backdoor-targets-fortinet-fortigate-firewalls/

如若转载,请注明出处：

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