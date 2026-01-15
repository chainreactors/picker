---
title: 高危警报：Moxa交换机存在OpenSSH远程代码执行漏洞（CVSS 9.8）
url: https://www.anquanke.com/post/id/314327
source: 安全客-有思想的安全新媒体
date: 2026-01-14
fetch_date: 2026-01-15T03:28:06.192270
---

# 高危警报：Moxa交换机存在OpenSSH远程代码执行漏洞（CVSS 9.8）

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

# 高危警报：Moxa交换机存在OpenSSH远程代码执行漏洞（CVSS 9.8）

阅读量**18779**

发布时间 : 2026-01-14 12:59:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/critical-alert-moxa-switches-exposed-to-openssh-remote-code-execution-cvss-9-8/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Moxa 的工业以太网交换机中被发现存在一个**严重安全漏洞**，可能威胁工业控制系统（OT）网络的完整性。该漏洞编号为 **CVE-2023-38408**，CVSS 评分高达 **9.8（高危）**，意味着需要**立即修复**。

问题出在设备所使用的 **OpenSSH 组件** 中，具体影响 **OpenSSH ssh-agent 在 9.3p2 之前版本中的 PKCS#11 功能**。

该漏洞源于一个 “**不可靠的搜索路径**”。如果 ssh-agent 被转发到攻击者控制的系统，就可能导致**远程代码执行（RCE）**。像 `/usr/lib` 这样的目录中的代码并不一定安全，而该漏洞的出现是因为之前的问题 **CVE-2016-10009** 的修复并不彻底。

由于漏洞严重性极高，官方强烈建议用户**立即采取修复措施**以降低风险。

### 受影响的产品系列

Moxa 已确认两个主要产品系列受到影响：

### 1. EDS 系列

型号包括：EDS-G4000、EDS-4008、EDS-4009、EDS-4012、EDS-4014、EDS-G4008、EDS-G4012、EDS-G4014

受影响固件：**4.1 及更早版本**

### 2. RKS 系列

型号包括：RKS-G4000、RKS-G4028、RKS-G4028-L3

受影响固件：**5.0 及更早版本**

### 修复措施

Moxa 已发布安全补丁，但**暂未提供公开下载**。用户必须联系 Moxa 技术支持以获取补丁文件。

* **EDS 系列：** 请求安全补丁 **v4.1.58**
* **RKS 系列：** 请求安全补丁 **v5.0.4**

### 临时缓解方案

对于无法马上进行固件更新的组织，Moxa 建议采用**纵深防御策略**降低风险：

* **限制访问：** 使用防火墙或访问控制列表（ACL）仅允许可信 IP 通信；通过 VLAN 隔离工业网络。
* **减少暴露面：** 确保设备不直接暴露在互联网上，并关闭未使用的端口。
* **加强认证：** 启用多因素认证（MFA）和基于角色的访问控制（RBAC）。
* **安全通信：** 使用 VPN 或 SSH 等加密协议进行远程访问，并仅限授权人员使用。
* **监控：** 部署异常检测以发现未授权活动，并定期审查审计日志。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-alert-moxa-switches-exposed-to-openssh-remote-code-execution-cvss-9-8/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314327](/post/id/314327)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-alert-moxa-switches-exposed-to-openssh-remote-code-execution-cvss-9-8/)

如若转载,请注明出处： <https://securityonline.info/critical-alert-moxa-switches-exposed-to-openssh-remote-code-execution-cvss-9-8/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **920**

* 粉丝
* **6**

### TA的文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22

### 相关文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22
* ##### [ValleyRAT\_S2病毒攻击组织：投放隐匿恶意软件，窃取金融敏感信息](/post/id/314334)

  2026-01-14 12:59:44
* ##### [苹果确认谷歌 Gemini 将为 Siri 提供技术支持，强调隐私仍是核心优先级](/post/id/314310)

  2026-01-14 12:58:29

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