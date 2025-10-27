---
title: Claroty利用RCE在西门子PLC中发现硬编码的加密密钥
url: https://www.anquanke.com/post/id/281720
source: 安全客-有思想的安全新媒体
date: 2022-10-15
fetch_date: 2025-10-03T19:54:50.305576
---

# Claroty利用RCE在西门子PLC中发现硬编码的加密密钥

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

# Claroty利用RCE在西门子PLC中发现硬编码的加密密钥

阅读量**168326**

发布时间 : 2022-10-14 10:00:06

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第383期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、Cymru发布恶意软件IcedID近期攻击活动的分析报告

[![]()](https://p1.ssl.qhimg.com/t0144f22a7ac45f2c4a.jpg)

Cymru表示，IcedID在近期的攻击活动中使用了不同的感染途径。报告指出，在9月13日至21日，IcedID的主要分发方式包括：ZIP->ISO->LNK->JS->[CMD或BAT]->DLL、ZIP->ISO->CHM->DLL、ZIP->ISO->LNK->BAT->DLL、带有宏的恶意Word或Excel文档以及通过PrivateLoader按安装付费服务直接分发。其中，使用ISO->LNK感染链的活动最成功，其次是使用游戏破解诱饵的PrivateLoader活动。[[阅读原文]](https://www.bleepingcomputer.com/news/security/hackers-behind-icedid-malware-attacks-diversify-delivery-tactics/)

## 2、澳大利亚加速推动关键基础设施改革的风险管理计划

[![]()](https://p3.ssl.qhimg.com/t0102bed4e4e00a3ce3.jpg)

近日，澳大利亚政府宣布，已开始根据《2018年关键基础设施安全法》第2A部分的要求，就风险管理计划规则的制定进行公开意见征求。该行动致力于建立强有力和有效的政府与产业界伙伴关系，这是实现政府关键基础设施安全和弹性愿景的关键。风险管理计划(RMP)将要求某些关键基础设施资产的所有者和运营商识别其业务面临的风险，并由董事会或其他管理机构每年签署一份风险计划。意见征求期限从2022年10月5日到11月18日。[[阅读原文]](http://www.anquan419.com/knews/24/3415.html)

## 3、白宫公布消费者设备网络安全标签计划：参考能源之星

[![]()](https://p3.ssl.qhimg.com/t0161b827b5bb1687e8.jpg)

CyberScoop报道称，一位要求匿名的白宫高级官员告诉该媒体，白宫国家安全委员会周二（10月11日）宣布一项消费品网络安全标签计划的计划，该计划旨在改善对互联网连接设备的数字保护。 来自消费品协会、制造公司和技术智囊团的大约50名代表将于10月19日在白宫召开会议专题讨论，预计2023年春季推出该计划。[[阅读原文]](https://www.cyberscoop.com/white-house-to-unveil-internet-of-things-labeling/)

## 4、NIST 牵头推进混合卫星网络安全指南研制

[![]()](https://p5.ssl.qhimg.com/t01490f274d30c0081f.jpg)

近期，美国国家标准与技术研究院（NIST）国家网络安全卓越中心（NCCoE）牵头组织商用卫星利益共同体，征集行业专家，共同开展卫星互联网商用价值、技术发展、挑战与愿景等研究。商用卫星利益共同体未来将定期召开会议，推动持续完善混合卫星网络安全指南（Hybrid Satellite Networks Cybersecurity Framework Profile Draft Annotated Outline，以下简称《指南》）。

《指南》于2022年7月12日发布初稿，由NCCoE牵头，联合MITRE公司共同发布，旨在指导相关单位建设、应对卫星互联网网络安全威胁，管理混合卫星网络（Hybrid Satellite Networks，HSN）架构、程序、资产等。并于2022年8月11日召开线上会议，讨论各方专家对《指南》的反馈意见，给出HSN的网络安全框架概览，规划下一步工作内容。[[阅读原文]](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.27.ipd.pdf)

## 5、Claroty利用RCE在西门子PLC中发现硬编码的加密密钥

[![]()](https://p5.ssl.qhimg.com/t010e1107dbed5cd610.jpg)

位于纽约的工业网络安全公司 Claroty 的研究部门 Team82 透露，他们成功提取了嵌入西门子可编程逻辑计算机（PLC）系列 SIMATIC S7-1200/1500s 和西门子自动化工程软件平台 TIA Portal 中的严密防护、硬编码的密码密钥。

据悉，该团队针对SIMATIC S7-1200和S7-1500 PLC的CPU部署了一种新的远程代码执行 (RCE) 技术，为此他们使用了之前对 Siemens PLC 的研究中发现的漏洞 ( CVE-2020-15782 )这使他们能够绕过 PLC 上的本机内存保护并获得读/写权限。

经测试，他们不仅能够提取西门子产品线中使用的内部严密保护的私钥，还能够实施完整的协议栈，加密和解密受保护的通信和配置。[[阅读原文]](https://www.infosecurity-magazine.com/news/claroty-found-cryptographic-keys/)

## 6、韩政府提交加入《网络犯罪公约》意向书

[![]()](https://p1.ssl.qhimg.com/t01a606d2b21d7d1558.jpg)

韩国外交部11日表示，政府向欧洲理事会提交有关加入《网络犯罪公约》（又称《布达佩斯公约》）的意向书。

欧洲理事会将在对这份意向书进行审议后正式邀请韩国加入，之后韩方办理国内相关程序，并向欧洲理事会交存加入书，加入该公约的程序由此完毕。

《布达佩斯公约》于2004年7月生效，目前有美国、日本、澳大利亚等共67个国家加入。《公约》规定网络犯罪处罚对象、公约缔结国之间的合作程序等内容。外交部表示，推进加入该《公约》旨在与国际社会一道打造安全和平的网络空间。[[阅读原文]](https://cn.yna.co.kr/view/ACK20221011005700881)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/281720](/post/id/281720)

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

![](https://p3.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* [1、Cymru发布恶意软件IcedID近期攻击活动的分析报告](#h2-1)
* [2、澳大利亚加速推动关键基础设施改革的风险管理计划](#h2-2)
* [3、白宫公布消费者设备网络安全标签计划：参考能源之星](#h2-3)
* [4、NIST 牵头推进混合卫星网络安全指南研制](#h2-4)
* [5、Claroty利用RCE在西门子PLC中发现硬编码的加密密钥](#h2-5)
* [6、韩政府提交加入《网络犯罪公约》意向书](#h2-6)

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