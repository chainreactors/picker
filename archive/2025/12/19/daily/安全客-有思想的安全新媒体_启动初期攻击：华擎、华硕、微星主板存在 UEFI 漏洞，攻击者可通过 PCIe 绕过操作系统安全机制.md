---
title: 启动初期攻击：华擎、华硕、微星主板存在 UEFI 漏洞，攻击者可通过 PCIe 绕过操作系统安全机制
url: https://www.anquanke.com/post/id/313882
source: 安全客-有思想的安全新媒体
date: 2025-12-19
fetch_date: 2025-12-20T03:13:39.281985
---

# 启动初期攻击：华擎、华硕、微星主板存在 UEFI 漏洞，攻击者可通过 PCIe 绕过操作系统安全机制

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

# 启动初期攻击：华擎、华硕、微星主板存在 UEFI 漏洞，攻击者可通过 PCIe 绕过操作系统安全机制

阅读量**14615**

发布时间 : 2025-12-19 17:21:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/early-boot-attack-uefi-flaw-in-asrock-asus-msi-boards-lets-hackers-bypass-os-security-via-pcie/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

现代计算机启动过程中的核心安全机制被发现存在重大缺陷，导致系统极易遭受物理攻击，攻击者可彻底绕过操作系统的防御措施。美国计算机应急响应协调中心（CERT/CC）发布的一份新漏洞公告显示，部分**UEFI 固件**的实现方式未正确初始化关键硬件防护机制，这使得攻击者能够在操作系统加载前，就读取和写入系统内存。

该漏洞影响多家厂商的设备，其中华擎（ASRock）硬件对应的漏洞编号为**CVE-2025-14304**—— 它将原本用于提升速度的特性：**直接内存访问（DMA）**，变成了任何可物理接触设备的攻击者手中的强力武器。

现代计算机依赖一个名为 \*\* 输入输出内存管理单元（IOMMU）\*\* 的组件作为 “守门人”，阻止外围设备在未经授权的情况下访问系统内存的敏感区域。但这个新漏洞暴露了一个危险的问题：系统报告的状态与实际运行状态不一致。

报告指出：“尽管固件显示 DMA 保护已激活，但它并未正确初始化 IOMMU”。

这就在 “启动初期（early-boot）” 阶段制造了一个可被利用的窗口期。由于 “守门人” 未正常工作，插入 PCIe 接口的恶意设备（比如被攻陷的网卡，或是专门的攻击工具），可以在操作系统启动自身防护机制之前，肆意读取系统内存中的数据。

对于无法保证物理安全的环境来说，这种 “防护机制失效” 的影响极为严重。

“拥有物理访问权限的恶意 PCIe 设备，可在操作系统防御机制加载前，读取或修改系统内存”。

攻击者可在启动前的阶段注入代码，或是提取机密信息，这种攻击对杀毒软件或操作系统级别的安全控制来说完全不可见。报告警告称，该漏洞 “会泄露敏感数据，还会让使用未打补丁固件的受影响系统，遭遇启动前代码注入攻击”。

尽管漏洞公告显示 “多家厂商受影响”，但重点点名了华擎及其子品牌 ASRockRack、ASRockInd。

华擎主板的具体漏洞编号为 CVE-2025-14304，CVSS 评分为 7.0，这意味着 “未经过身份验证的物理攻击者，可借助支持 DMA 的 PCIe 设备，在操作系统内核及其安全功能加载前，读取和写入任意物理内存”。此外，华硕（CVE-2025-11901）、技嘉（CVE-2025-14302）和微星（CVE-2025-14303）的主板也受该漏洞影响。

安全管理员被要求以对待操作系统补丁的优先级，处理固件更新。

CERT/CC 建议：“由于受影响的厂商众多，且补丁发布时间不同，用户应定期查看厂商信息板块，获取最新的安全公告和固件更新包”。

对于安全要求较高的机构，建议更为严格：“难以控制物理访问权限的环境，应优先完成补丁更新，以降低启动前 DMA 攻击的风险”。

本文翻译自securityonline [原文链接](https://securityonline.info/early-boot-attack-uefi-flaw-in-asrock-asus-msi-boards-lets-hackers-bypass-os-security-via-pcie/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313882](/post/id/313882)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/early-boot-attack-uefi-flaw-in-asrock-asus-msi-boards-lets-hackers-bypass-os-security-via-pcie/)

如若转载,请注明出处： <https://securityonline.info/early-boot-attack-uefi-flaw-in-asrock-asus-msi-boards-lets-hackers-bypass-os-security-via-pcie/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **830**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2025-37164（CVSS 评分 10.0）：未验证身份即可远程执行代码，HPE OneView 漏洞或致数据中心遭完全控制](/post/id/313860)

  2025-12-19 17:27:54
* ##### [零日漏洞预警：黑客利用 SonicWall SMA1000 系列漏洞链，实现未验证身份的最高权限远程代码执行](/post/id/313863)

  2025-12-19 17:27:02
* ##### [RTO challan 诈骗事件解析：虚假交通罚单 + 恶意 VPN 组合攻击的盗刷原理](/post/id/313869)

  2025-12-19 17:26:53
* ##### [百亿美元转向：OpenAI 洽谈亚马逊巨额融资 —— 但暗藏硅谷式附加条件](/post/id/313874)

  2025-12-19 17:25:55
* ##### [开发者的胜利：社区强烈反对后，GitHub 推迟自托管运行器收费计划](/post/id/313856)

  2025-12-19 17:25:31

### 相关文章

* ##### [CVE-2025-37164（CVSS 评分 10.0）：未验证身份即可远程执行代码，HPE OneView 漏洞或致数据中心遭完全控制](/post/id/313860)

  2025-12-19 17:27:54
* ##### [零日漏洞预警：黑客利用 SonicWall SMA1000 系列漏洞链，实现未验证身份的最高权限远程代码执行](/post/id/313863)

  2025-12-19 17:27:02
* ##### [RTO challan 诈骗事件解析：虚假交通罚单 + 恶意 VPN 组合攻击的盗刷原理](/post/id/313869)

  2025-12-19 17:26:53
* ##### [百亿美元转向：OpenAI 洽谈亚马逊巨额融资 —— 但暗藏硅谷式附加条件](/post/id/313874)

  2025-12-19 17:25:55
* ##### [开发者的胜利：社区强烈反对后，GitHub 推迟自托管运行器收费计划](/post/id/313856)

  2025-12-19 17:25:31
* ##### [2025 年 Chrome 零日漏洞遭在野利用：全面深度分析](/post/id/313877)

  2025-12-19 17:23:30
* ##### [Kubernetes 安全预警：Headlamp 漏洞（CVE-2025-14269）致未授权用户可劫持 Helm 集群](/post/id/313879)

  2025-12-19 17:21:53

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