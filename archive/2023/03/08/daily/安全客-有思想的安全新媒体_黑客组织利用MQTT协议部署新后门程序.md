---
title: 黑客组织利用MQTT协议部署新后门程序
url: https://www.anquanke.com/post/id/287049
source: 安全客-有思想的安全新媒体
date: 2023-03-08
fetch_date: 2025-10-04T08:52:39.999955
---

# 黑客组织利用MQTT协议部署新后门程序

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

# 黑客组织利用MQTT协议部署新后门程序

阅读量**130871**

发布时间 : 2023-03-07 10:00:17

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第470期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、国产APP利用Android漏洞提权使其难以卸载

[![]()](https://p1.ssl.qhimg.com/t0193d96bdf1fcc1d6b.png)

国内的一个独立安全研究机构DarkNavy发表文章披露，国内一家互联网巨头的APP利用了Android系统漏洞提权使其难以卸载。

报道没有公开相关公司的名字，但称得上巨头也就那四五家公司。报道称，该APP首先利用了多个厂商OEM代码中的反序列化漏洞提权，提权控制手机系统之后，该App即开启了一系列的违规操作，绕过隐私合规监管，大肆收集用户的隐私信息（包括社交媒体账户资料、位置信息、Wi-Fi信息、基站信息甚至路由器信息等）。之后，该 App利用手机厂商OEM代码中导出的root-path FileContentProvider，进行System App和敏感系统应用文件读写；进而突破沙箱机制、绕开权限系统改写系统关键配置文件为自身保活，修改用户桌面(Launcher)配置隐藏自身或欺骗用户实现防卸载；随后，还进一步通过覆盖动态代码文件的方式劫持其他应用注入后门执行代码，进行更加隐蔽的长期驻留；甚至还实现了和间谍软件一样的遥控机制，通过远端“云控开关”控制非法行为的启动与暂停，来躲避检测。[[阅读原文]](https://www.solidot.org/story?sid=74293)

## 2、黑客组织利用MQTT协议部署新后门程序

[![]()](https://p0.ssl.qhimg.com/t018684d9770b1238de.png)

安全公司ESET报告，黑客组织Mustang Panda aka TA416和Bronze President部署了一种新的后门程序MQsTTang。恶意程序主要通过钓鱼邮件传播，通过一个GitHub软件库下载负荷，它会在注册表增加一个启动时运行的注册表项去实现持久存在。为了躲避监测它利用了MQTT协议去进行指令通信。MQsTTang还会检查主机上是否存在调试器或监控工具，如果有发现，它会相应的改变行为。[[阅读原文]](https://www.welivesecurity.com/2023/03/02/mqsttang-mustang-panda-latest-backdoor-treads-new-ground-qt-mqtt/)

## 3、电动汽车充电设施正成为网络攻击的新目标

[![]()](https://p0.ssl.qhimg.com/t01097789e2cf11468c.png)

随着电动汽车 (EV) 充电基础设施急于跟上美国电动汽车销量的急剧增长，网络攻击者和安全研究人员等已经开始关注基础设施中的安全弱点。能源网络网络安全公司 Saiflow 的研究人员在开放式充电点协议 (OCPP) 中发现了两个漏洞，可用于分布式拒绝服务 (DDoS) 攻击和窃取敏感信息。

2月，能源网络网络安全公司 Saiflow 的研究人员在开放式充电点协议 (OCPP) 中发现了两个漏洞，可用于分布式拒绝服务 (DDoS) 攻击和窃取敏感信息。爱达荷国家实验室最近发现，它检查的每个充电器——更正式地称为电动汽车供电设备 (EVSE)——运行的是过时版本的 Linux，有不必要的服务，并允许许多服务以 root 身份运行，根据一项调查《能源》杂志上的电动汽车充电漏洞研究。该论文称，其他潜在的攻击包括中间人攻击 (AitM) 和暴露在公共互联网上的服务。[[阅读原文]](https://www.darkreading.com/ics-ot/ev-charging-infrastructure-electric-cyberattack-opportunity)

## 4、新型TPM 2.0漏洞可能让黑客窃取加密密钥

[![]()](https://p2.ssl.qhimg.com/t014cf9d5bdb5a0764a.png)

可信平台模块 (TPM) 2.0规范受到两个缓冲区溢出漏洞的影响，这些漏洞可能允许攻击者访问或覆盖敏感数据，例如加密密钥。

TPM 是一种基于硬件的技术，可为操作系统提供防篡改安全加密功能。它可用于存储加密密钥、密码和其他关键数据，这使得其实施中的任何漏洞都值得关注。虽然某些 Windows 安全功能需要 TPM，例如测量启动、设备加密、Windows Defender System Guard (DRTM)、设备健康证明，但其他更常用的功能不需要 TPM。

但是，当可信平台模块可用时，Windows 安全功能在保护敏感信息和加密数据方面获得增强的安全性。由于需要启动安全措施并确保 Windows Hello 人脸识别提供可靠的身份验证，微软将 TPM 2.0规作为运行Windows 11的要求时，TPM2.0规范受到了欢迎（和争议）。

Linux 也支持 TPM，但没有要求在操作系统中使用该模块。此外，有可用的 Linux 工具允许应用程序和用户保护 TPM 中的数据。[[阅读原文]](https://www.bleepingcomputer.com/news/security/new-tpm-20-flaws-could-let-hackers-steal-cryptographic-keys/)

## 5、Play勒索软件团伙泄露奥克兰市相关数据

[![]()](https://p5.ssl.qhimg.com/t01ca68b26bfa6e670b.png)

Play 勒索软件组织开始泄露一个10 GB的档案，其中包含敏感数据，例如员工信息、护照和 ID。

在最近的一次攻击中，Play 勒索软件团伙终于开始泄露从奥克兰市窃取的数据。Play 勒索软件团伙在最近的一次网络攻击中开始泄露他们从奥克兰市（加利福尼亚州）窃取的数据。

奥克兰是旧金山湾区东湾区最大的城市，湾区第三大城市，加州人口第八大城市。奥克兰市于2023年2月10日披露了一次勒索软件攻击，安全漏洞始于2023年2月8日。出于谨慎考虑，奥克兰市将受影响的系统下线，同时他们努力保护受影响的基础设施。信息技术部通知地方当局并对事件展开调查，以确定问题的范围和严重程度。[[阅读原文]](https://securityaffairs.com/143037/cyber-crime/play-ransomware-leaks-city-of-oakland.html)

## 6、FBI和CISA联合警告Royal勒索软件攻击风险增加

[![]()](https://p2.ssl.qhimg.com/t01f1162ad30e5356c7.png)

日前，CISA和FBI发布了一份联合咨询报告，强调针对许多美国关键基础设施部门（包括医疗保健、通信和教育）对受到Royal勒索软件攻击的风险越来越大。

此前，美国卫生与公众服务部 (HHS) 发布了一份咨询报告，其安全团队于2022年12月透露，勒索软件行动与针对美国医疗保健组织的多次攻击有关。

作为回应，  FBI 和 CISA 共享了妥协指标和一系列相关的战术、技术和程序 (TTP)，这将帮助防御者检测并阻止在其网络上部署 Royal 勒索软件有效载荷的企图。[[阅读原文]](https://www.bleepingcomputer.com/news/security/fbi-and-cisa-warn-of-increasing-royal-ransomware-attack-risks/)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287049](/post/id/287049)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t01a1ab830955b940ce.png)

[![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)](/member.html?memberId=2)

[安全客](/member.html?memberId=2)

有思想的安全新媒体

* 文章
* **3687**

* 粉丝
* **225**

### TA的文章

* ##### [ISC.AI2024热点资讯](/post/id/297785)

  2024-07-10 17:00:28
* ##### [ISC2023热点资讯](/post/id/289102)

  2023-06-06 17:21:40
* ##### [数说安全《攻击面管理产品》报告发布 360以第一顺位入选国内代表性安全厂商](/post/id/288540)

  2023-05-05 12:03:24
* ##### [伪装成ChatGPT的 恶意软件被用来引诱受害者](/post/id/288531)

  2023-05-05 12:01:24
* ##### [研究人员发现Microsoft Azure API管理服务中的3个漏洞](/post/id/288526)

  2023-05-05 11:59:52

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

* [1、国产APP利用Android漏洞提权使其难以卸载](#h2-1)
* [2、黑客组织利用MQTT协议部署新后门程序](#h2-2)
* [3、电动汽车充电设施正成为网络攻击的新目标](#h2-3)
* [4、新型TPM 2.0漏洞可能让黑客窃取加密密钥](#h2-4)
* [5、Play勒索软件团伙泄露奥克兰市相关数据](#h2-5)
* [6、FBI和CISA联合警告Royal勒索软件攻击风险增加](#h2-6)

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