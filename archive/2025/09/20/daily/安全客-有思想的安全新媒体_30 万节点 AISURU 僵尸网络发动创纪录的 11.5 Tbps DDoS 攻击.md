---
title: 30 万节点 AISURU 僵尸网络发动创纪录的 11.5 Tbps DDoS 攻击
url: https://www.anquanke.com/post/id/312272
source: 安全客-有思想的安全新媒体
date: 2025-09-20
fetch_date: 2025-10-02T20:24:32.630788
---

# 30 万节点 AISURU 僵尸网络发动创纪录的 11.5 Tbps DDoS 攻击

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

# 30 万节点 AISURU 僵尸网络发动创纪录的 11.5 Tbps DDoS 攻击

阅读量**66254**

发布时间 : 2025-09-19 18:33:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Mann，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/300k-node-aisuru-botnet-drives-record-breaking-11-5-tbps-ddos-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员揭露了名为 **“AISURU”** 的分布式拒绝服务（DDoS）与代理僵尸网络，它曾在全球范围内制造出 **创纪录的 11.5 Tbps 攻击流量**。

AISURU 至少自 **2024 年**起就已活跃，并在 **2025 年**快速扩张，规模与能力大幅提升。目前估计已控制超过 **30 万台受感染设备**，这些设备主要通过路由器漏洞被攻陷。

该发现由 **XLab 研究人员**发布，报告基于内部遥测数据及一位熟悉 AISURU 威胁行为者的匿名线人提供的信息。

AISURU 最早于 **2024 年 8 月**被 XLab 识别，当时它曾攻击游戏《黑神话：悟空》的分发平台。自那以来，XLab 的网络威胁洞察与分析系统（CTIA）已捕获数千个 AISURU 样本。

关键的扩张发生在 **2025 年 4 月**：该组织一名成员入侵了 **Totolink 路由器固件更新服务器**，将固件请求重定向至恶意脚本（托管在 **updatetoto[.]tw**）。在 DNS 遥测中，这次感染活动清晰可见，该域名在一个月内飙升至 **Tranco 排名 672,588**，并导致新增超过 **10 万台僵尸节点**。

AISURU 由三名核心成员操控：

* **Snow**：僵尸网络开发者
* **Tom**：漏洞研究员与利用代码开发者
* **Forky**：负责变现与销售

他们因内部冲突和在载荷中夹带的“嘲讽”而臭名昭著，甚至在其他僵尸网络操作者中也颇受争议。其攻击包括多次创纪录的事件，例如 **2025 年 5 月**对记者 Brian Krebs 个人网站的 DDoS 攻击，以及 **2025 年 9 月**针对 **IP 185.211.78.117** 发动的 **11.5 Tbps** 超大规模攻击。

AISURU 主要瞄准 **未打补丁的路由器与嵌入式系统**，并持续利用 **已知漏洞（N-day）和新发现的 0-day 漏洞**。受影响厂商包括：

* **Totolink**（固件更新服务器被攻陷）
* **Cambium Networks**（cnPilot 路由器 0-day）
* **Zyxel、D-Link、Linksys、T-Mobile、Realtek** 等

受害者遍布多个行业和地区，据 XLab 报告，该僵尸网络**每天攻击目标多达数百个**，不分行业与地域。

### 技术细节

AISURU 使用 **改良版 RC4 算法**进行字符串解密和通信加密，硬编码密钥为 **PJbiNbbeasddDfsc**。技术分析显示其具备多层反分析机制，包括：

* **环境检测**：规避虚拟化与分析环境；
* **OOM Killer 规避**：操纵 `/proc/self/oom_score_adj`；
* **进程伪装**：伪装为系统进程，如 *telnetd* 或 *klogd*；
* **持久化与隐匿**：通过保留 `.so` 库、重命名二进制文件等非常规方式实现；
* **C2 通信**：采用定制协议，支持 DDoS 攻击、命令执行、反弹 shell 与代理控制，基础设施使用混淆的 TXT 记录、XOR 编码及基于特定 IP 范围的 GRE 隧道。

### DDoS、代理与新的盈利模式

AISURU 已从单纯的 DDoS 工具转型为**多用途平台**。最新版本增加了 **代理模块**，C2 指令显示其愈发重视住宅代理功能。通过调用 **Speedtest 公共端点**进行网速测试，僵尸网络可识别高带宽节点并优先用于代理业务。

这种转型符合地下市场的趋势：僵尸网络运营者不再仅依赖高调的 DDoS，而是多元化发展，代理节点被出租给需要低调基础设施的威胁行为者，用于欺诈、爬虫或命令执行。

### 防御措施

要防御类似 **AISURU** 的僵尸网络攻击，建议：

* **及时更新路由器固件**至最新版本；
* **限制 WAN 访问**；
* **修改默认管理员凭证**；
* **关闭未使用的服务**。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/300k-node-aisuru-botnet-drives-record-breaking-11-5-tbps-ddos-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312272](/post/id/312272)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/300k-node-aisuru-botnet-drives-record-breaking-11-5-tbps-ddos-attack/)

如若转载,请注明出处： <https://cyberinsider.com/300k-node-aisuru-botnet-drives-record-breaking-11-5-tbps-ddos-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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