---
title: 严重的思科 ISE 云漏洞（CVSS 9.9）与 PoC 漏洞利用威胁 AWS、Azure 和 OCI
url: https://www.anquanke.com/post/id/308136
source: 安全客-有思想的安全新媒体
date: 2025-06-06
fetch_date: 2025-10-06T22:47:56.715072
---

# 严重的思科 ISE 云漏洞（CVSS 9.9）与 PoC 漏洞利用威胁 AWS、Azure 和 OCI

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

# 严重的思科 ISE 云漏洞（CVSS 9.9）与 PoC 漏洞利用威胁 AWS、Azure 和 OCI

阅读量**88511**

发布时间 : 2025-06-05 12:39:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-cisco-ise-cloud-vulnerability-cvss-9-9-with-poc-exploit-threatens-aws-azure-oci/>

译文仅供参考，具体内容表达以及含义原文为准。

![思科 ISE, CVE-2025-20286]()

思科已经修补了一个关键漏洞(CVE-2025-20286,CVSS 9.9),该漏洞影响了其身份服务引擎(ISE)在AWS,Microsoft Azure和Oracle云基础设施(OCI)中的基于云的部署。该漏洞可能允许未经身份验证的远程攻击者访问敏感数据并执行管理操作。

*“此漏洞之所以存在,是因为当Cisco ISE部署在云平台上时生成凭据不正确……导致不同的Cisco* ISE部署共享相同的凭据。

CVE-2025-20286 允许攻击者从 Cisco ISE 的一个实例中提取静态凭据,并重用它们以访问同一云平台和发布版本上的其他部署。这种大规模的配置监督在云中部署时会影响主管理节点。

*“攻击者可以通过从云中部署的Cisco [ISE中提取用户凭据来利用此漏洞](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/),然后使用它们访问通过不安全端口部署在其他云环境中的Cisco ISE。*

成功的漏洞利用可能导致:

* ①未经授权的数据访问
* ②配置更改
* ③执行有限的管理操作
* ④服务中断

漏洞影响以下 Cisco ISE 云部署:

![]()

值得注意的是,凭据是每个平台共享的,例如,AWS 上的所有 3.1 个实例都具有相同的静态凭据。

虽然没有变通办法,但思科提出了缓解策略,例如:

* ①使用云安全组限制源 IP
* ②通过 ISE UI 限制对已知管理员 IP 的访问
* *③对于新的安装:“运行`application reset-config ise`命令将用户密码重置为新值。**这将重置 Cisco ISE 到工厂默认值。*

*思科警告说:“恢复备份将恢复原始凭据。*

[思科建议应用修补程序](https://software.cisco.com/download/home/283801620/type/283802505/release/HP-CLOUD-CSCwn63400)`ise-apply-CSCwn63400_3.1.x_patchall-SPA.tar.gz`到受影响的版本(3.1–3.4)并迁移到以下固定版本:

①3.3 → 3.3P8(2025年11月可用

②3.4→ 3.4P3(2025年10月可用)

③3.5 将默认发货(预计2025年8月)

Cisco PSIRT 证实:

> *“概念验证漏洞利用代码可用……Cisco PSIRT不知道该漏洞有任何恶意使用。*

尽管如此,随着公共漏洞利用代码的存在,云管理员被敦促将其视为关键风险并立即修补。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-cisco-ise-cloud-vulnerability-cvss-9-9-with-poc-exploit-threatens-aws-azure-oci/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308136](/post/id/308136)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-cisco-ise-cloud-vulnerability-cvss-9-9-with-poc-exploit-threatens-aws-azure-oci/)

如若转载,请注明出处： <https://securityonline.info/critical-cisco-ise-cloud-vulnerability-cvss-9-9-with-poc-exploit-threatens-aws-azure-oci/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52

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