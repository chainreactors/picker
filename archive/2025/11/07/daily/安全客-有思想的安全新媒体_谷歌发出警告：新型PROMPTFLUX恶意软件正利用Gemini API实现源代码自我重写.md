---
title: 谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写
url: https://www.anquanke.com/post/id/313072
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:00:48.771631
---

# 谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写

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

# 谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写

阅读量**28391**

发布时间 : 2025-11-07 10:27:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/promptflux-malware-using-gemini-api/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌威胁情报小组（GTIG）近日披露了名为**PROMPTFLUX的实验性恶意软件家族详情，该恶意软件能利用Gemini AI API动态重写自身代码。**

根据GTIG于2025年11月4日发布的最新AI威胁追踪报告，这一进展表明攻击者正从单纯利用生产力工具转向将大语言模型直接嵌入恶意软件，以实现实时适应与规避检测。

尽管仍处于测试阶段且尚未具备大规模入侵能力，PROMPTFLUX已成为首个被观测到实现”即时”AI集成的恶意软件，可能为更自主化的攻击铺平道路。

PROMPTFLUX以VBScript释放程序形式运作，初始伪装成”crypted\_ScreenRec\_webinstall”等无害安装程序，针对不同行业和地区的用户实施欺骗。

其核心创新在于”思维机器人”模块，该模块通过硬编码的Gemini API密钥调用”gemini-1.5-flash-latest”模型，生成用于规避杀毒软件检测的混淆VBScript代码。

该恶意软件会引导大语言模型生成自包含的规避脚本，仅输出代码而不含冗余文本，并将响应记录在临时文件中持续优化。在高级变种中，它每小时会重写全部源代码，嵌入原始负载、API密钥与再生逻辑，形成确保通过Windows启动文件夹实现持久化的递归变异循环。

GTIG指出，**虽然自我更新功能仍处于注释状态**（表明其处于早期开发阶段），但该恶意软件已尝试向可移动驱动器和网络共享驱动器横向传播。

这种手法不仅利用AI的生成能力进行创建，更着眼于持续生存，与依赖固定特征码、易被防御方检测的静态恶意软件有本质区别。

PROMPTFLUX的出现正值网络犯罪市场日趋成熟之际——AI工具正涌入地下论坛，以订阅制价格提供从深度伪造到漏洞利用的各项能力。

![]()

**攻击者还在提示词中采用社会工程学手段，冒充CTF参赛者或学生以规避AI安全限制，获取漏洞利用代码。**

随着这些工具降低新手攻击者的门槛，GTIG警告风险正在加剧，包括像**PROMPTLOCK**这类能动态生成Lua加密脚本的自适应勒索软件。

作为响应，谷歌已迅速禁用相关API密钥与项目，同时DeepMind正增强Gemini的分类器与模型防护机制以阻断滥用提示。公司通过优先构建强健防护原则、借助SAIF等框架分享洞见，以及提供红队测试漏洞工具，强调对负责任AI的承诺。

诸如用于**漏洞狩猎的Big Sleep与自动修补的CodeMender**等创新，凸显了主动对抗AI威胁的努力。

尽管PROMPTFLUX目前尚未构成直接入侵威胁，但GTIG预测其将快速蔓延，敦促各组织监控API滥用行为并采用行为检测替代特征码方案。随着AI更深度融入运营，这份报告预示着构建全域生态系统防御以领先持续进化对手的迫切需求。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/promptflux-malware-using-gemini-api/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313072](/post/id/313072)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/promptflux-malware-using-gemini-api/)

如若转载,请注明出处： <https://cybersecuritynews.com/promptflux-malware-using-gemini-api/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **663**

* 粉丝
* **6**

### TA的文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13

### 相关文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13
* ##### [恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载](/post/id/313076)

  2025-11-07 10:27:01
* ##### [远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测](/post/id/313056)

  2025-11-07 10:26:52
* ##### [二进制供应链安全平台Binarly Transparency Platform 3.5发布，新增对Java归档文件与JVM字节码的深度支持](/post/id/313053)

  2025-11-07 10:26:40

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