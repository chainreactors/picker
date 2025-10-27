---
title: SystemBC僵尸网络每日入侵1500台VPS服务器用于DDoS攻击
url: https://www.anquanke.com/post/id/312317
source: 安全客-有思想的安全新媒体
date: 2025-09-23
fetch_date: 2025-10-02T20:30:57.581755
---

# SystemBC僵尸网络每日入侵1500台VPS服务器用于DDoS攻击

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

# SystemBC僵尸网络每日入侵1500台VPS服务器用于DDoS攻击

阅读量**73756**

|评论**1**

发布时间 : 2025-09-22 18:13:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/systembc-botnet-hacking-1500-vps-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

SystemBC僵尸网络的出现标志着基于代理的犯罪基础设施发生了**重大演变**。

该僵尸网络的运营者不再劫持家用设备作为代理，而是转向攻陷**大型商业虚拟专用服务器（VPS）**，从而提供高容量代理服务，同时将对终端用户的干扰降至最低。

近几个月，Lumen Technologies观察到平均**每日新增1500台被攻陷的VPS系统**，每台服务器均被用于为犯罪威胁团伙转发恶意流量。这些受感染服务器作为**高带宽代理节点**，能提供传统家用设备僵尸网络无法维持的**前所未有的吞吐量**。

### **技术特性：加密通信与持久化机制**

SystemBC最早由Proofpoint于2019年记录，如今其功能已从简单代理扩展到更多领域。成功入侵后，加载器会解密硬编码配置，并连接至**80余个命令控制（C2）服务器**中的一个。

恶意载荷通过**XOR与RC4加密组合**保护通信信道，极大增加了防御者的检测与分析难度。Lumen分析师在对Linux变体样本的动态分析中发现，其出站心跳和C2响应均采用**三阶段加密流程**。这种在规避与检测之间的持续博弈，凸显了SystemBC多年来的**强大生存能力**。

### **犯罪生态影响：商业化代理服务整合**

该僵尸网络的影响已渗透整个网络犯罪生态。除提供可出租的代理资源外，SystemBC网络还被整合进更大规模的犯罪服务中，例如**REM Proxy**——这是一种分层商业服务，为多个犯罪集团提供支持。

![]()

Proxy的高端“Mix-Speed”层级包含大量**SystemBC感染的服务器**，因其流量规模和稳定性而被犯罪者青睐。

与此同时，低质量代理被用于**暴力破解攻击和凭证窃取**。这种受感染VPS资产的双重利用，凸显了威胁行为者如何在统一架构下优化不同的感染与利用阶段。

### **感染机制与解密流程**

感染机制通常始于对互联网暴露服务的**443端口 opportunistic扫描**。一旦识别出易受攻击的VPS，恶意软件便通过**80端口HTTP协议**启动下载。

![]()

获取的shell脚本带有俄语注释，可自动并行下载并执行**180余个SystemBC样本**。每个样本的二进制文件中均嵌入**40字节XOR密钥**。执行时，加载器通过以下伪代码重构C2配置：

```
# Pseudocode for SystemBC configuration decryption
key = read_bytes(offset=0x100, length=40)
encrypted_config = read_bytes(offset=0x200, length=config_length)
config = xor(rc4(xor(encrypted_config, key), key), key)
```

![]()

解密后，配置文件会生成**C2端点列表和操作参数**。加载器随后构造初始心跳包（包含密钥、填充字节和0xFFFF头部），通过相同加密流程加密后传输。

![]()

C2服务器的响应包含**四字节命令头**，指示新建代理、注入代理数据或终止连接。

Lumen研究人员指出，这种**对称加密方案**能有效规避基于特征的检测，同时在受感染服务器上保持**极低计算开销**。

### **现代恶意软件即服务（MaaS）典范**

通过结合**可扩展感染策略、强加密机制**以及与商业代理服务的整合，SystemBC成为现代**恶意软件即服务（MaaS）** 模式的典型代表。持续监控和快速共享威胁指标，仍是缓解其广泛威胁的关键。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/systembc-botnet-hacking-1500-vps-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312317](/post/id/312317)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/systembc-botnet-hacking-1500-vps-servers/)

如若转载,请注明出处： <https://cybersecuritynews.com/systembc-botnet-hacking-1500-vps-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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