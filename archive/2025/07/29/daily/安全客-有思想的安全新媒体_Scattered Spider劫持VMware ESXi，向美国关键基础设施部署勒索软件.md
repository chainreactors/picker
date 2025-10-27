---
title: Scattered Spider劫持VMware ESXi，向美国关键基础设施部署勒索软件
url: https://www.anquanke.com/post/id/310652
source: 安全客-有思想的安全新媒体
date: 2025-07-29
fetch_date: 2025-10-06T23:50:20.837727
---

# Scattered Spider劫持VMware ESXi，向美国关键基础设施部署勒索软件

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

# Scattered Spider劫持VMware ESXi，向美国关键基础设施部署勒索软件

阅读量**65083**

发布时间 : 2025-07-28 16:39:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/07/scattered-spider-hijacks-vmware-esxi-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

臭名昭著的网络犯罪集团**Scattered Spider正针对VMware ESXi虚拟化主机发动攻击**，目标主要集中在**北美的零售、航空和运输行业**。

谷歌的Mandiant团队在一份详细分析报告中指出：“该组织的核心战术一直保持一致，且不依赖于软件漏洞。相反，他们使用一种经过验证的战术，主要通过拨打IT帮助台电话进行社会工程攻击。”

“攻击者非常具有攻击性、创造性，并且特别擅长使用社会工程技术绕过成熟的安全防护程序。他们的攻击不是偶发的，而是精确的、有针对性的行动，旨在破坏一个组织最关键的系统和数据。”

这些攻击者还被称为**0ktapus、Muddled Libra、Octo Tempest和UNC3944**，他们曾通过先进的社会工程攻击获取受害环境的初始访问权限，然后采用“生活在土地上”（LotL）的方法，操纵受信任的管理系统，并利用他们对Active Directory的控制，进一步向VMware vSphere环境推进。

谷歌表示，这种方法通过**绕过安全工具并留下极少的妥协痕迹，提供了一条直接从虚拟化主机（hypervisor）进行数据外泄和勒索病毒部署的路径**，”极为有效”。

![]()

该攻击链分为五个阶段：

1. **初始入侵、侦察和权限提升**：攻击者通过获取与IT文档、支持指南、组织架构图和vSphere管理员相关的信息，进行侦察，并枚举像HashiCorp Vault等密码管理器中的凭证，或其他特权访问管理（PAM）解决方案。攻击者还会拨打公司的IT帮助台电话，冒充高价值管理员请求密码重置，以便获取账户控制权限。
2. **利用映射的Active Directory凭证切换到虚拟环境**：攻击者使用从Active Directory获取的vSphere凭证访问VMware vCenter Server Appliance（vCSA），然后执行远程命令创建持久的加密反向Shell，绕过防火墙规则。
3. **在ESXi主机上启用SSH连接并重置root密码**：执行所谓的“磁盘交换”攻击，提取NTDS.dit的Active Directory数据库。该攻击方法是通过关闭一个域控制器（DC）虚拟机（VM），脱离其虚拟磁盘，然后将磁盘连接到攻击者控制的其他未监控虚拟机中。攻击者复制NTDS.dit文件后，会恢复虚拟机并重新启动DC。
4. **利用访问权限删除备份任务、快照和存储库，阻碍恢复过程**。
5. **通过SSH访问ESXi主机，使用SCP/SFTP上传定制勒索病毒二进制文件**。

谷歌表示：“UNC3944的攻击战术要求防御策略的根本转变，从基于EDR的威胁狩猎转向以基础设施为中心的主动防御。” “与传统的Windows勒索病毒不同，这种威胁在速度和隐匿性上有明显区别。”

该科技巨头还特别提到攻击者的“极端速度”，指出从初始入侵到数据外泄和最终勒索病毒部署，整个感染过程可能在短短几个小时内完成。

![]()

根据Palo Alto Networks Unit 42的报告，Scattered Spider组织不仅在社交工程方面表现出色，还与DragonForce（又名Slippery Scorpius）勒索病毒程序合作，曾在两天内外泄超过100 GB的数据。

为了应对这些威胁，建议组织采取三层防护措施：

1. 启用vSphere锁定模式，强制执行execInstalledOnly，使用vSphere虚拟机加密，淘汰旧的虚拟机，强化帮助台的安全措施。
2. 实施抗钓鱼的多因素身份验证（MFA），隔离关键身份基础设施，避免身份验证循环。
3. 集中并监控关键日志，隔离备份与生产环境的Active Directory，确保它们对被攻陷的管理员不可访问。

谷歌还建议，随着VMware vSphere 7的生命周期接近结束（预计2025年10月），组织在进行系统迁移时应考虑重新架构系统，增强安全性。

![]()

谷歌指出：“针对vSphere基础设施的勒索病毒攻击，包括ESXi主机和vCenter Server，因其能立即并广泛地瘫痪基础设施，构成独特而严重的风险。”

“如果不主动采取这些推荐的缓解措施来应对这些相互关联的风险，组织将暴露于针对性攻击之下，这些攻击能迅速摧毁整个虚拟化基础设施，导致运营中断和财务损失。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/07/scattered-spider-hijacks-vmware-esxi-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310652](/post/id/310652)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/07/scattered-spider-hijacks-vmware-esxi-to.html)

如若转载,请注明出处： <https://thehackernews.com/2025/07/scattered-spider-hijacks-vmware-esxi-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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