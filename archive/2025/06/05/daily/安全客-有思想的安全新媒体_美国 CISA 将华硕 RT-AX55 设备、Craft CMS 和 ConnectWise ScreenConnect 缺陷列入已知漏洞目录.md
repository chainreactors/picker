---
title: 美国 CISA 将华硕 RT-AX55 设备、Craft CMS 和 ConnectWise ScreenConnect 缺陷列入已知漏洞目录
url: https://www.anquanke.com/post/id/308112
source: 安全客-有思想的安全新媒体
date: 2025-06-05
fetch_date: 2025-10-06T22:49:26.131531
---

# 美国 CISA 将华硕 RT-AX55 设备、Craft CMS 和 ConnectWise ScreenConnect 缺陷列入已知漏洞目录

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

# 美国 CISA 将华硕 RT-AX55 设备、Craft CMS 和 ConnectWise ScreenConnect 缺陷列入已知漏洞目录

阅读量**183476**

发布时间 : 2025-06-04 16:06:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs 2

原文地址：<https://securityaffairs.com/178591/hacking/u-s-cisa-adds-asus-rt-ax55-devices-craft-cms-and-connectwise-screenconnect-flaws-to-its-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全和基础设施安全局(CISA)[added](https://www.cisa.gov/news-events/alerts/2025/06/02/cisa-adds-five-known-exploited-vulnerabilities-catalog)[在其已知的利用漏洞(KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)目录中添加了华硕RT-AX55设备,Craft CMS和ConnectWise ScreenConnect漏洞。

以下是这些缺陷的描述:

* [CVE-2021-32030](https://www.cve.org/CVERecord?id=CVE-2021-32030) 华硕路由器不当身份验证漏洞
* [CVE-2023-39780](https://www.cve.org/CVERecord?id=CVE-2023-39780) 华硕 RT-AX55 路由器操作系统命令注入漏洞
* [CVE-2024-56145](https://www.cve.org/CVERecord?id=CVE-2024-56145) 精加工 CMS 代码注入漏洞
* [CVE-2025-3935](https://www.cve.org/CVERecord?id=CVE-2025-3935) ConnectWise ScreenConnect 不当身份验证漏洞
* [CVE-2025-3539](https://www.cve.org/CVERecord?id=CVE-2025-35939) Craft CMS 外部控制假定的不可变Web参数漏洞

上周,[ConnectWise透露](https://securityaffairs.com/178442/hacking/connectwise-cyberattack-sophisticated-nation-state-actor.html),它已经发现了与高级民族国家演员有关的可疑活动。该公司证实,此次攻击影响了少数ScreenConnect客户。[CVE-2025-3935](http://www.connectwise.com/company/trust/security-bulletins/screenconnect-security-patch-2025.4)[may have led](https://www.reddit.com/r/msp/comments/1kxpwrn/connectwise_confirms_screenconnect_cyberattack/)跟踪为CVE-2025-3935的ScreenConnect漏洞可能导致ConnectWise漏洞,允许通过被盗的机器密钥执行远程代码。虽然ConnectWise尚未确认是否被利用了此漏洞,但它在披露之前修补了云托管实例的问题。

[另一个有趣的问题是CVE-2023-39780](https://nvd.nist.gov/vuln/detail/CVE-2023-39780),它影响了华硕RT-AX55。上周,[GreyNoise研究人员警告说](https://securityaffairs.com/178413/malware/new-ayysshush-botnet-compromised-over-9000-asus-routers-adding-a-persistent-ssh-backdoor.html),一个新的AyySSHush僵尸网络破坏了9000多个华硕路由器,增加了一个持久的SSH后门。

GreyNoise在华硕RT-AX55 v3.0.0.4.386.51598中发现了利用经过身份验证的命令注入漏洞CVE-2023-39780来执行任意系统命令的有效载荷。

攻击者利用命令注入漏洞添加其 SSH 密钥并启用端口 53282 上的访问,确保跨重新启动和更新的持续后门访问。

根据绑定操作指令(BOD)22-01： 减少已知漏洞被利用的重大风险，欧洲安全与合作机构必须在规定日期前解决已发现的漏洞，以保护其网络免受利用目录中漏洞的攻击。专家还建议私营机构审查目录并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2025 年 6 月 23 日前修复漏洞。

本文翻译自securityaffairs 2 [原文链接](https://securityaffairs.com/178591/hacking/u-s-cisa-adds-asus-rt-ax55-devices-craft-cms-and-connectwise-screenconnect-flaws-to-its-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308112](/post/id/308112)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs 2](https://securityaffairs.com/178591/hacking/u-s-cisa-adds-asus-rt-ax55-devices-craft-cms-and-connectwise-screenconnect-flaws-to-its-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/178591/hacking/u-s-cisa-adds-asus-rt-ax55-devices-craft-cms-and-connectwise-screenconnect-flaws-to-its-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [漏洞预警](/tag/%E6%BC%8F%E6%B4%9E%E9%A2%84%E8%AD%A6)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27

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