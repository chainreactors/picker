---
title: 黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷
url: https://www.anquanke.com/post/id/314748
source: 安全客-有思想的安全新媒体
date: 2026-02-06
fetch_date: 2026-02-07T04:07:33.738259
---

# 黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷

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

# 黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷

阅读量**29572**

发布时间 : 2026-02-06 11:12:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/react-server-vulnerability-exploited/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

CVE-2025-55182 漏洞披露两个月后，针对 React 服务端组件的攻击行为已从大范围扫描，演变为**协同化、高流量的规模化攻击活动**。

据格雷诺伊斯（GreyNoise）2026 年 1 月 26 日至 2 月 2 日的监测数据显示，威胁行为者正积极利用这一**高危漏洞**部署加密挖矿程序，并建立**持久化远程访问权限**。

尽管尝试发起漏洞利用的独立攻击源达 1083 个，但攻击流量高度集中。两个特定 IP 地址发起的恶意会话占所有监测数据的 56%，这一特征表明攻击来自**自动化的大型攻击基础设施**，而非人工测试行为。

## 威胁态势与主要攻击方

已监测到的攻击均使用针对 CVE-2025-55182 漏洞的公开 Metasploit 模块，攻击者可通过**单个恶意 HTTP POST 请求**，在未完成身份验证的情况下实现远程代码执行（RCE）。主要威胁行为者的攻击目标呈现明显分化：

* **加密挖矿攻击团伙（87.121.84 [.] 24）**：发起的攻击流量占比 22%，涉及 311484 次恶意会话。该团伙会执行检索脚本，从跳板服务器下载门罗币挖矿程序（XMRig）的二进制文件，其攻击依赖外部基础设施托管恶意载荷。
* **交互式访问攻击团伙（193.142.147 [.] 209）**：发起的攻击流量占比 34%，涉及 488342 次恶意会话。该团伙完全绕过跳板服务器，通过恶意载荷直接向扫描源 IP 的 12323 端口开启反向 Shell，其攻击意图并非自动化窃取资源，而是**实现交互式的网络横向渗透**。

对该加密挖矿攻击基础设施的深度分析发现，其存在长期恶意活动记录。核心跳板服务器 205.185.127 [.] 97 自 2020 年起，就一直托管着 mased [.] top、mercarios [.] buzz 等受攻击者控制的域名。

此外，该服务器同一子网内的相邻 IP（87.121.84 [.] 25、87.121.84 [.] 45）目前仍在传播 Mirai 和 Gafgyt 僵尸网络变种，可见该子网已成**僵尸网络运营者的聚集地**，其攻击目标同时涵盖企业服务器与民用物联网设备。

## 漏洞详细信息

CVE-2025-55182 是 React 服务端组件中存在的**反序列化漏洞**，其通用漏洞评分系统（CVSS）评分为**10.0 分**，属于最高级别的高危漏洞。未授权攻击者可通过操纵服务器处理的序列化数据，实现**任意代码执行**。

漏洞编号：CVE-2025-55182

通用漏洞评分：10.0（高危）

受影响软件：React 服务端组件

漏洞类型：不安全的反序列化

**受影响版本**：

* React 19.0.0
* React 19.1.0 至 19.1.1
* React 19.2.0

**已修复版本**：

* React 19.0.1、19.1.2、19.2.1

攻击者将攻击目标精准指向**开发端口**，推测其意在寻找配置不当的服务实例 —— 开发人员若使用`--host 0.0.0.0`启动参数，会导致服务器意外暴露至公网。被攻击最多的端口包括 443、80、3000、3001 和 3002。

安全团队被敦促**立即将 React 组件升级至最新修复版本**。若暂时无法完成补丁部署，需严格限制开发端口的网络访问权限，并阻断下述攻击特征指标。

## 入侵特征指标（IOCs）

### 网络指标（IPv4 地址）

IP 地址 193.142.147[.]209  类型是攻击源 IP 关联攻击行为 反向 Shell / 交互式远程访问

IP 地址 87.121.84[.]24 类型是攻击源 IP 关联攻击行为  门罗币挖矿程序投放

IP 地址 205.185.127[.]97 类型是跳板服务器  关联攻击行为  恶意载荷托管

IP 地址176.65.132[.]224 类型是跳板服务器  关联攻击行为  恶意载荷托管

### 网络攻击特征

* 反向 Shell 端口：TCP/12323
* 流量特征：包含异常 Next-Action 请求头的 HTTP POST 请求

### 文件哈希值（SHA-256）

[哈希值待进一步分析]—— 从 205.185.127 [.] 97 获取的门罗币挖矿程序（XMRig）二进制文件（ELF 格式）。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/react-server-vulnerability-exploited/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314748](/post/id/314748)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/react-server-vulnerability-exploited/)

如若转载,请注明出处： <https://cybersecuritynews.com/react-server-vulnerability-exploited/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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
* **1010**

* 粉丝
* **6**

### TA的文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11

### 相关文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11
* ##### [Xcode 26.3落地macOS苹果正式引入智能体式AI编码功能](/post/id/314784)

  2026-02-06 11:10:45
* ##### [RapidFort完成4200万美元A轮融资 深耕自动化漏洞修复领域](/post/id/314788)

  2026-02-06 11:10:18
* ##### [CVE-2026-24735Apache Answer漏洞致私密帖子历史记录泄露](/post/id/314754)

  2026-02-06 11:09:38

### 热门推荐

文章目录

* [威胁态势与主要攻击方](#h2-0)
* [漏洞详细信息](#h2-1)
* [入侵特征指标（IOCs）](#h2-2)
  + [网络指标（IPv4 地址）](#h3-3)
  + [网络攻击特征](#h3-4)
  + [文件哈希值（SHA-256）](#h3-5)

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