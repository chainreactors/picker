---
title: Zerobotv9僵尸网络开始劫持企业自动化系统
url: https://www.anquanke.com/post/id/314979
source: 安全客-有思想的安全新媒体
date: 2026-03-04
fetch_date: 2026-03-05T04:05:34.861961
---

# Zerobotv9僵尸网络开始劫持企业自动化系统

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

# Zerobotv9僵尸网络开始劫持企业自动化系统

阅读量**22081**

发布时间 : 2026-03-04 10:35:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/beyond-the-router-how-the-zerobotv9-botnet-is-hijacking-enterprise-automation/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

据阿卡迈（Akamai）安全情报与响应团队（SIRT）近期调查显示，臭名昭著的恶意软件家族 **Zerobot** 携全新手段卷土重来。

这个最新版本被命名为 **Zerobotv9**，它不再只瞄准普通家庭网络设备，而是**主动攻击企业级工作流自动化系统**。

阿卡迈 SIRT 于 **2026 年 1 月中旬**发现这一轮新型攻击。

攻击者不仅针对常规硬件 —— 具体为 **Tenda AC1206 家用路由器**，还在利用一款主流企业软件平台 **n8n** 中的漏洞。

n8n 平台本质上是一个**数字中间件**，企业使用它无缝对接内部数据库、云服务与日常应用系统。

正如阿卡迈报告所指出的，这一攻击目标的转变对企业安全团队是**重大警示信号**：

“对 n8n 漏洞的攻击尤为值得警惕：僵尸网络通常利用物联网（IoT）设备，如安防摄像头、DVR 和路由器，但 n8n 属于完全不同的攻击范畴。”

黑客拿下家用路由器后，可能仅用其发送垃圾流量。

但**一旦控制 n8n 平台**，攻击者就有可能**横向渗透进入企业最核心的内部网络**，窃取 **API 密钥** 并篡改关键数据。

该恶意软件正在利用两个已公开补丁的已知漏洞：

* **Tenda 路由器漏洞（CVE-2025-7544）**

  这是一个**远程栈溢出漏洞**，影响 Tenda AC1206 设备 15.03.06.23 版本的 `/goform/setMacFilterCfg` 接口，漏洞评级为**严重**，可通过 `deviceList` 参数利用。
* **n8n 平台漏洞（CVE-2025-68613）**

  该漏洞源于**缺少沙箱隔离机制**。

  正常情况下，软件会在沙箱中运行，无法触及系统其他部分；

  而该漏洞可让攻击者**突破沙箱限制**，**直接在主服务器上执行命令**。

攻击者利用这些漏洞入侵后，会运行一个简易脚本（名为 `tol.sh`），以此安装 **Zerobot** 主要攻击载荷。

报告指出：

“威胁行为人 opportunistically 利用近期披露的漏洞**在当下十分普遍。即便管理规范、及时补丁的机构，在漏洞公开后也往往存在一段**可被攻击的窗口期，而部分企业甚至完全忽略这类设备的补丁更新。”

Zerobot 核心基于 **Mirai** 恶意代码构建，后者是多年前引发大规模网络瘫痪的著名僵尸网络。

尽管原始作者已落网，但 Mirai 源码在网上**完全公开**，无论是新手还是资深黑客都能据此开发变种。

阿卡迈研究人员对这类攻击持续泛滥的原因给出结论：

“尽管近期执法部门打掉多个高影响力僵尸网络，但基于 Mirai 的恶意程序仍在不断扩散。因为**搭建一套基于 Mirai 的僵尸网络，门槛相当低**。”

本文翻译自securityonline [原文链接](https://securityonline.info/beyond-the-router-how-the-zerobotv9-botnet-is-hijacking-enterprise-automation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314979](/post/id/314979)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/beyond-the-router-how-the-zerobotv9-botnet-is-hijacking-enterprise-automation/)

如若转载,请注明出处： <https://securityonline.info/beyond-the-router-how-the-zerobotv9-botnet-is-hijacking-enterprise-automation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28
* ##### [AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户](/post/id/314998)

  2026-03-04 10:33:55

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