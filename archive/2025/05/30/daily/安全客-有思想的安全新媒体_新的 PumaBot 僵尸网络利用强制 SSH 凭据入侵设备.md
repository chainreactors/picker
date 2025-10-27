---
title: 新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备
url: https://www.anquanke.com/post/id/307967
source: 安全客-有思想的安全新媒体
date: 2025-05-30
fetch_date: 2025-10-06T22:23:28.496895
---

# 新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备

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

# 新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备

阅读量**155180**

发布时间 : 2025-05-29 14:59:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-pumabot-botnet-brute-forces-ssh-credentials-to-breach-devices/>

译文仅供参考，具体内容表达以及含义原文为准。

![僵尸]()

一种名为PumaBot的新发现的基于Go的Linux僵尸网络恶意软件正在嵌入式物联网设备上强制SSH凭据以部署恶意有效载荷。

PumaBot的目标性质也很明显,它基于从命令和控制(C2)服务器中提取的列表而不是更广泛的互联网扫描来定位特定的IP。

### 瞄准监控摄像头

Darktrace在一份报告中记录了PumaBota report,提供了僵尸网络攻击流,妥协指标(IoC)和检测规则的概述。

[![]()](https://www.akamai.com/lp/api-security-power-of-n?utm_source=pubdirect&utm_medium=video&utm_campaign=f-mc-62146&utm_id=global_api_security&utm_content=video_pofn&utm_placement=bleeping_computer)

恶意软件从其C2(ssh.ddos-cc.org)接收目标IP列表,并尝试在端口22上执行暴力登录尝试以进行开放SSH访问。

在此过程中,它检查是否存在“Pumatronix”字符串,Darktrace认为该字符串可以与供应商针对监视和交通摄像头系统相对应。

一旦目标建立,恶意软件就会收到凭据来测试它们。

如果成功,它运行“名称 -a”来获取环境信息并验证目标设备不是蜜罐。

接下来,它将其主要二进制(jierui)写入/lib/redis并安装systemd服务(redis.service),以确保跨设备重新启动的持久性。

最后,它将自己的SSH注入到“authorized\_keys”文件中以维持访问,即使在清除原发感染的清理情况下也是如此。

在感染保持活动状态时,PumaBot 可以接收命令以尝试数据泄漏、引入新的有效载荷或窃取在横向移动中有用的数据。

Darktrace 看到的示例有效载荷包括自更新脚本、替换合法 ‘pam\_unix.so’ 的 PAM rootkit 和守护程序(二进制文件 ” ) 。

恶意 PAM 模块收集本地和远程 SSH 登录详细信息,并将其存储在文本文件 (con.txt) 中。“观察者”二进制(1)不断查找该文本文件,然后将其泄漏到C2。

![在文本文件上写凭据]()

被清除后,从受感染的主机上擦除文本文件,以删除恶意活动的任何痕迹。

PumaBot的规模和成功目前未知,Darktrace没有提及目标IP列表的广泛程度。

这种新的僵尸网络恶意软件在发起有针对性的攻击方面脱颖而出,这些攻击可能为更深层次的企业网络渗透开辟道路,而不是直接使用受感染的物联网进行低级网络犯罪,例如分布式拒绝服务(DoS)攻击或代理网络。

为了抵御僵尸网络威胁,将物联网升级到最新的可用固件版本,更改默认凭据,将它们放在防火墙后面,并将其保存在与有价值系统隔离的单独网络中。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-pumabot-botnet-brute-forces-ssh-credentials-to-breach-devices/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307967](/post/id/307967)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-pumabot-botnet-brute-forces-ssh-credentials-to-breach-devices/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-pumabot-botnet-brute-forces-ssh-credentials-to-breach-devices/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24

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