---
title: CISA 警告：Citrix NetScaler 零日远程代码执行漏洞正遭广泛利用
url: https://www.anquanke.com/post/id/311702
source: 安全客-有思想的安全新媒体
date: 2025-08-30
fetch_date: 2025-10-07T00:17:49.601613
---

# CISA 警告：Citrix NetScaler 零日远程代码执行漏洞正遭广泛利用

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

# CISA 警告：Citrix NetScaler 零日远程代码执行漏洞正遭广泛利用

阅读量**100030**

发布时间 : 2025-08-29 16:14:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Florence Nightingale，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cisa-warns-citrix-netscaler-0-day/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）近日紧急发布警告，指出 Citrix NetScaler 系统中存在一个严重的零日漏洞（编号 **CVE-2025-7775**），该漏洞已被攻击者积极利用。由于风险极高，该漏洞已于 2025 年 8 月 26 日被立即纳入 **CISA“已知被利用漏洞”（KEV）目录**。

## 关键信息

1. **Citrix NetScaler 零日漏洞被积极利用**，已加入 CISA KEV 目录。
2. 漏洞可实现 **未经身份验证的远程代码执行（RCE）**。
3. **必须立即更新 Citrix 固件**，以防系统被攻破。

## 漏洞详情：内存溢出（CVE-2025-7775）

该漏洞属于 **内存溢出缺陷**，影响 Citrix NetScaler 应用交付控制器（ADC）、Gateway 以及部分 SD-WAN 产品。

**内存溢出漏洞**发生在应用程序写入超出分配边界的数据时，攻击者可利用这一缺陷在受影响系统上执行任意代码。对于在企业网络架构中处于核心位置的 NetScaler 系统而言，这类漏洞尤为危险。

根据 **CVSS 3.1** 评分体系，该漏洞评分高达 **9.8（严重级别）**。技术细节表明，这是一个可远程触发、无需身份验证的 **缓冲区溢出漏洞**。

攻击方式通常为：攻击者构造恶意 HTTP 请求，并在其中注入超大数据载荷，从而导致内存损坏并实现提权代码执行。由于漏洞位于 **数据包处理引擎**，攻击者可借此绕过安全控制，直接获取设备的管理权限。

## 受影响范围

* **受影响产品**：
  + Citrix NetScaler ADC
  + Citrix NetScaler Gateway
  + Citrix NetScaler SD-WAN WANOP
  + 所有未打补丁的固件版本
* **影响**：远程代码执行（RCE）
* **利用条件**：
  + 攻击者可访问 NetScaler 管理接口
  + 无需认证
  + 能发送特制 HTTP 请求
  + 目标运行存在漏洞的固件版本

## 修复与缓解措施

CISA 已依据 **BOD 22-01（强制性运营指令）** 要求所有联邦机构立即修复该漏洞。

* **临时防护措施**：
  + 实施网络分段
  + 配置访问控制列表（ACL）限制外部访问
* **官方补丁**：
  Citrix 已发布安全公告，提供修复补丁。该补丁通过 **改进边界检查和输入验证** 来消除内存溢出问题。管理员应立即升级至最新固件版本，可通过 **nsconfig 命令行工具**完成配置更新。
* **额外建议**：
  + 部署 Web 应用防火墙（WAF）规则，检测并阻断针对漏洞的利用尝试
  + 检查系统日志与异常流量，防范潜在入侵

## 总结

CVE-2025-7775 被列入 CISA KEV 目录，意味着该漏洞已在真实攻击中被广泛利用。由于 NetScaler 在企业网络基础设施中的关键地位，任何延迟修复都可能导致严重后果。各组织必须 **立即响应、及时打补丁并强化监控**，以降低被攻陷风险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cisa-warns-citrix-netscaler-0-day/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311702](/post/id/311702)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cisa-warns-citrix-netscaler-0-day/)

如若转载,请注明出处： <https://cybersecuritynews.com/cisa-warns-citrix-netscaler-0-day/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [关键信息](#h2-0)
* [漏洞详情：内存溢出（CVE-2025-7775）](#h2-1)
* [受影响范围](#h2-2)
* [修复与缓解措施](#h2-3)
* [总结](#h2-4)

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