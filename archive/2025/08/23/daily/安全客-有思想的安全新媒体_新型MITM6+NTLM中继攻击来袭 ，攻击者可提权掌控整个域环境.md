---
title: 新型MITM6+NTLM中继攻击来袭 ，攻击者可提权掌控整个域环境
url: https://www.anquanke.com/post/id/311414
source: 安全客-有思想的安全新媒体
date: 2025-08-23
fetch_date: 2025-10-07T00:17:54.854596
---

# 新型MITM6+NTLM中继攻击来袭 ，攻击者可提权掌控整个域环境

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

# 新型MITM6+NTLM中继攻击来袭 ，攻击者可提权掌控整个域环境

阅读量**74716**

发布时间 : 2025-08-22 17:16:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Florence Nightingale，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-mitm6-ntlm-relay-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种结合MITM6与NTLM中继技术的精密攻击链近日被披露，可导致**Active Directory域环境全面沦陷**。该攻击利用Windows默认的IPv6自动配置行为，使攻击者能在数分钟内从网络访问权限提升至域管理员权限。

**核心攻击机理**

1. 滥用Windows IPv6自动配置功能及AD域默认的10个计算机账户配额
2. 使用mitm6+ntlmrelayx工具组合创建配置RBCD权限的恶意账户，快速获取域管理员权限
3. 修复方案：禁用IPv6、设置ms-DS-MachineAccountQuota=0、启用签名验证、部署DHCPv6防护

这种攻击技术对运行标准Windows环境的企业构成重大威胁，因其利用的是内置协议漏洞，无需依赖恶意软件或零日漏洞。

### **IPv6自动配置攻击**

Resecurity报告指出，MITM6攻击瞄准了Windows的基础行为：系统启动或连接网络时自动发送DHCPv6请求。即使企业未主动使用IPv6，Windows机器仍会优先进行IPv6配置，从而形成可被利用的攻击面。

攻击者部署mitm6工具充当恶意DHCPv6服务器，响应这些请求并向受害机器分配恶意DNS服务器地址。通过执行`sudo mitm6 -d target.local –no-ra`命令，攻击者即可成为目标域的权威DNS服务器。

（翻译说明：采用”全面沦陷”强化域环境被攻破的严重性；通过加粗突出**技术术语**和**关键风险**；使用代码块标注命令行操作；保留所有英文专业术语原称；采用分项列举方式清晰呈现攻击机理和修复方案，符合技术公报的排版规范）

![]()

攻击链随后通过Impacket工具包中的**ntlmrelayx**工具延续，该工具通过欺骗WPAD（Web代理自动发现协议）截获NTLM认证尝试。攻击者执行：`sudo impacket-ntlmrelayx -ts -6 -t ldaps://target.local -wh fakewpad –add-computer –delegate-access`，创建恶意计算机账户并配置基于资源的约束委派（RBCD）。

报告指出，**Active Directory默认的ms-DS-MachineAccountQuota设置允许任何认证用户添加最多10个计算机账户**，这使得攻击者能够创建受其控制的计算机对象。这些账户随后可修改其msDS-AllowedToActOnBehalfOfOtherIdentity属性，从而获得包括域管理员在内的高权限账户模拟能力。

### **防御建议**

该攻击的影响远不止初始网络入侵。一旦成功，攻击者可使用`secretsdump.py "target.local/User:Password@target.local"`提取NTLM哈希，并通过CrackMapExec等工具进行横向移动：`crackmapexec smb 10.0.0.1/8 -u administrator -H 1f937b21e2e0ada0d3d3f7cf58c8aade –share`。

![]()

企业可能面临严重后果，包括：**全域沦陷**、**凭据窃取**、**服务中断**及**潜在数据泄露**。由于攻击滥用合法的Windows协议，其隐蔽性使得检测变得异常困难。

关键缓解策略包括：禁用非必需的IPv6协议、设置**ms-DS-MachineAccountQuota=0**防止未授权计算机账户创建、强制实施SMB和LDAP签名防止中继攻击。在网络层面，应在交换机和路由器上部署**DHCPv6防护**以阻止未授权的IPv6通告。

此攻击事件表明，默认配置可能造成重大安全漏洞，凸显出主动强化Active Directory安全配置和持续监控异常网络服务的重要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-mitm6-ntlm-relay-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311414](/post/id/311414)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-mitm6-ntlm-relay-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-mitm6-ntlm-relay-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

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