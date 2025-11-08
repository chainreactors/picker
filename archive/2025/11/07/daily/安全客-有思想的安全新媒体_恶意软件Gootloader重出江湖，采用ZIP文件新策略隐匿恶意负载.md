---
title: 恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载
url: https://www.anquanke.com/post/id/313076
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:00:58.116177
---

# 恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载

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

# 恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载

阅读量**21380**

发布时间 : 2025-11-07 10:27:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/zip-file-tactic/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现，**Gootloader**恶意软件活动再度活跃，其采用精妙的新型规避技术，通过操纵ZIP压缩包来规避检测与分析。

此次威胁的发现归功于安全研究员RussianPanda与Hackress团队，他们确认该活动正通过遭入侵的网站积极攻击受害者。

尽管今年早些时候曾遭到打击，但Gootloader背后的威胁行为体已携强化战术卷土重来，显示出其维持这一长期运营活动的决心。

**该恶意软件继续利用以法律术语为中心的社会工程学诱饵，诱骗毫无戒心的用户下载恶意负载，这些负载作为后续攻击的初始接入向量，往往最终导致勒索软件部署。**

五年多来，Gootloader运营者始终围绕法律主题关键词（包括”合同”、”表格”和”协议”）构建其攻击方法，这些词汇天然吸引商务人士和法律研究者。

当前活动显著扩展了此方法，通过超过100个被入侵网站分发数千个独特搜索关键词，以撒下更大的网捕捉潜在受害者。

**攻击链始于受害者搜索合法法律文件时接触到这些被入侵网站。**

威胁行为体采用精密的门控系统，根据地理位置、操作系统、来源网站和访问时间等多种条件决定向不同访客显示的内容。

**未满足特定条件（例如在工作时间通过搜索引擎从英语国家使用Windows系统访问）的用户，会看到看似无害的博客内容——这些内容通常由人工智能工具生成。**

然而，符合目标画像的受害者则会目睹页面剧变。原本无害的网页会重新绘制自身，模仿合法的法律资源网站，有时甚至冒充知名机构。

一个显著案例是创建虚假的”耶鲁法律期刊”页面，攻击者在此运用Unicode字符替换技术，用视觉上相同的西里尔字母替代拉丁字母，从而规避基础检测机制。

**这些欺诈页面显示多种可下载资源，包括PDF、文档、视频和图像，这些内容在语境上与受害者原始搜索查询高度相关。此Gootloader变种最重大的进化在于新型ZIP文件操纵技术，该技术会根据使用的解压工具产生不同结果。**

当通过大多数受害者使用的默认文件管理器Windows资源管理器处理时，压缩包会正确提取带.JS扩展名的恶意JScript文件——即预期负载。

这种具有双重人格的ZIP文件构成了有效的时间拖延机制，使得恶意文件能够规避依赖非Windows解压工具的自动化安全扫描器和沙箱分析环境。

待安全团队识别出实际负载行为时，恶意软件可能已在受害者系统建立持久化并开启下一阶段操作。

然而，使用行业标准工具（包括VirusTotal、Python的zipfile库或7-Zip）分析同一压缩包的安全研究人员，则会遇到完全不同的内容：看似无害的文本文件，从而掩盖了压缩包的真实恶意性质。Gootloader的持久化方法也经历了显著改进。先前变种依赖计划任务确保负载在系统重启后仍能执行——这种技术已被终端检测方案广泛识别。

**当前版本实施了更为复杂的多阶段方法，旨在增加取证分析和修复工作的难度。**

**感染过程现在会投放两个功能互补的独立LNK快捷方式文件。第一个快捷方式嵌入用户的启动文件夹，确保用户登录Windows账户时自动执行。**

该主快捷方式并非直接启动恶意负载，而是引用战略性放置在AppData目录结构中的第二个LNK文件，使其在常规检查中更不易被发现。

**此二级快捷方式作为实际负载启动器，执行初始感染过程中投放的另一个JavaScript文件。**

**更复杂的是，Gootloader会创建使用Ctrl+Alt组合随机字母的自定义键盘快捷键，用于手动触发二级LNK文件。**

在初始感染序列中，恶意软件通过程序模拟这些击键组合以无需用户交互即启动执行，为操作增添了又一重隐蔽层。Gootloader携增强能力回归印证了网络安全领域的一个基本挑战：成功的打击行动很少能永久消除顽固的威胁行为体，反而会迫使其进行战术进化。

该活动运营者持续展现其在绕过安全控制、维持操作安全以及通过高度情境化社会工程学欺骗用户方面的技术创造力。

调查潜在Gootloader感染的组织和安全专业人员应优先检查在不同工具中呈现不一致解压行为的ZIP压缩包——这是该活动独特规避技术的明确指标。

此外，监控启动文件夹和AppData目录中异常的LNK文件放置，结合对意外计划任务或自定义热键配置的警惕，有助于在攻击者推进至后续目标（包括勒索软件部署）前识别已失陷系统。

本文翻译自gbhackers [原文链接](https://gbhackers.com/zip-file-tactic/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313076](/post/id/313076)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/zip-file-tactic/)

如若转载,请注明出处： <https://gbhackers.com/zip-file-tactic/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13
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