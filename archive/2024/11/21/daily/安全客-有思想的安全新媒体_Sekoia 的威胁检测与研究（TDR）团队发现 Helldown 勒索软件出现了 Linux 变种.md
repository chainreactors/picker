---
title: Sekoia 的威胁检测与研究（TDR）团队发现 Helldown 勒索软件出现了 Linux 变种
url: https://www.anquanke.com/post/id/302006
source: 安全客-有思想的安全新媒体
date: 2024-11-21
fetch_date: 2025-10-06T19:14:03.586228
---

# Sekoia 的威胁检测与研究（TDR）团队发现 Helldown 勒索软件出现了 Linux 变种

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

# Sekoia 的威胁检测与研究（TDR）团队发现 Helldown 勒索软件出现了 Linux 变种

阅读量**45388**

发布时间 : 2024-11-20 10:36:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/cve-2024-42057-exploited-by-helldown-ransomware-to-target-linux/>

译文仅供参考，具体内容表达以及含义原文为准。

![Helldown ransomware Linux]()

**Sekoia的威胁检测与研究（TDR）团队发现了Helldown勒索软件的Linux变种，扩大了威胁范围。**

Helldown 勒索软件组织以前以针对 Windows 系统而闻名，现在已将其活动范围扩大到 Linux 机器。Sekoia的威胁检测与研究（TDR）团队发现了这一新情况，他们在一条推特上提到了针对Linux系统的Helldown勒索软件的Linux变种。

Helldown 是勒索软件领域的一个相对较新的成员，于 2024 年 8 月首次出现，目前已在美国和欧洲造成 31 名受害者，其中包括 Zyxel 的欧洲子公司。该组织采用双重勒索策略，在加密文件之前先渗出敏感数据，并威胁说如果不支付赎金，就会公布窃取的信息。

Sekoia 已将几起 Helldown 攻击与 Zyxel 防火墙的漏洞联系起来。一个名为 CVE-2024-42057 的关键漏洞允许未经身份验证的代码执行，已被确定为该组织的一个可能入口点。值得注意的是

* 受攻击的防火墙被发现带有恶意用户账户和有效载荷，如从俄罗斯 IP 上传的 zzz1.conf 文件。
* 利用漏洞，攻击者可以进一步进入网络，使用高级端口扫描器等工具和命令来瘫痪防御系统

Helldown 的勒索软件以 Windows 和 Linux 系统为目标，具有独特的有效载荷：

* **Windows 勒索软件**： 采用阴影副本删除、进程终止和加密。被攻击的系统上会留下一份赎金说明 ReadMe.[encrypt\_extension].txt。
* **Linux 勒索软件**： 主要针对 VMware ESX 服务器。它会杀死虚拟机，用 RSA 加密密钥加密文件，并将密钥附加到加密文件中，只能用攻击者的私人密钥解密。

Helldown 通过渗出大量数据进行双重勒索–每个受害者的数据量从 22GB 到 431GB。被盗数据通常包括 PDF 和扫描文档，可能来自网络文件共享驱动器或 NAS 系统。

Helldown 的行为和工具与 Darkrace 和 Donex 有相似之处，两者都源自泄露的 LockBit 3 代码库。不过，这些组织之间尚未建立明确的联系。

本文翻译自securityonline [原文链接](https://securityonline.info/cve-2024-42057-exploited-by-helldown-ransomware-to-target-linux/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302006](/post/id/302006)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cve-2024-42057-exploited-by-helldown-ransomware-to-target-linux/)

如若转载,请注明出处： <https://securityonline.info/cve-2024-42057-exploited-by-helldown-ransomware-to-target-linux/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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