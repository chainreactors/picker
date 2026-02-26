---
title: Android恶意软件运行时调用Google Gemini
url: https://www.anquanke.com/post/id/314819
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:48.629102
---

# Android恶意软件运行时调用Google Gemini

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

# Android恶意软件运行时调用Google Gemini

阅读量**24173**

发布时间 : 2026-02-25 14:19:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pooja Tikekar，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/android-malware-taps-google-gemini-at-runtime-a-30819>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员新发现一款 Android 恶意软件家族，该恶意软件在运行过程中**调用 Google Gemini 大模型**，以实现部分持久化机制的自动化。据研究人员描述，这是已知的**第二起由 AI 驱动的移动恶意软件案例**。

相关阅读：医疗行业 CISO 医疗物联网安全指南

安全厂商 Eset 将该恶意软件命名为 **PromptSpy**，并指出它是**生成式 AI 直接嵌入 Android 恶意软件**的早期实例，可让恶意程序适配设备环境并提升抗清除能力。

研究人员在上传至 VirusTotal 的安卓安装包中发现了该恶意软件。Eset 表示，其产品遥测数据中**暂未监测到 PromptSpy**，也未证实该恶意软件已在野外大规模部署。但其技术设计充分表明，黑产攻击者正尝试借助 AI 模型，突破传统移动恶意软件在自动化能力上的局限。

此次发现之前，Eset 曾在 2025 年 8 月披露过 **PromptLock**—— 一款由生成式 AI 驱动的勒索软件。该勒索软件内置本地运行的大语言模型，可在运行时动态生成加密逻辑并支撑恶意代码执行，而非完全依赖预编译的二进制文件。

**PromptSpy 的核心创新点在于其与 Android 用户界面的交互方式**。

与传统依赖硬编码坐标或静态自动化脚本（极易失效）的恶意软件不同，PromptSpy 会抓取用户当前界面的 **XML 结构信息**，包括文本标签、控件类型与屏幕坐标，并将这些结构化数据发送给 Gemini。

Gemini 会返回 **JSON 格式指令**，明确指出需要点击或操作的界面元素。PromptSpy 在本地执行对应动作，获取更新后的界面状态，重复执行上述流程，直至实现持久化驻留。

安装完成后，该恶意软件会尝试获取 **无障碍服务（AccessibilityService）权限**。这是一项高风险安卓功能，几乎所有安卓木马都会试图诱骗用户授予该权限。

研究人员指出，该恶意软件具备**防卸载功能**：

它会在包含 “stop”“end”“clear”“Uninstall” 等关键词的按钮上覆盖一层**不可见界面**，拦截用户操作，阻止常规卸载。

目前唯一可靠的清除方式是**重启进入安全模式**，此时第三方应用无法干扰系统。

该恶意软件其他已观测到的行为还包括：

采集设备信息、上传已安装应用列表、窃取锁屏 PIN 码、视频录制解锁图案、上报前台应用状态以及屏幕截图。

Eset 将部分 PromptSpy 样本追溯至一个仿冒摩根大通的独立网站 **MorganArg**，表明该攻击活动**主要针对阿根廷用户**。

研究人员还在代码中发现**中文语言字符串**，暗示其开发环境可能与中文地区相关，但目前尚未将该活动归属于任何已知黑客组织。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/android-malware-taps-google-gemini-at-runtime-a-30819)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314819](/post/id/314819)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/android-malware-taps-google-gemini-at-runtime-a-30819)

如若转载,请注明出处： <https://www.govinfosecurity.com/android-malware-taps-google-gemini-at-runtime-a-30819>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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