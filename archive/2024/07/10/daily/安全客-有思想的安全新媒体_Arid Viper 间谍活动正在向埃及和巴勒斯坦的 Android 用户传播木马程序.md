---
title: Arid Viper 间谍活动正在向埃及和巴勒斯坦的 Android 用户传播木马程序
url: https://www.anquanke.com/post/id/297726
source: 安全客-有思想的安全新媒体
date: 2024-07-10
fetch_date: 2025-10-06T17:40:03.057094
---

# Arid Viper 间谍活动正在向埃及和巴勒斯坦的 Android 用户传播木马程序

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

# Arid Viper 间谍活动正在向埃及和巴勒斯坦的 Android 用户传播木马程序

阅读量**180356**

发布时间 : 2024-07-09 19:37:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 卢卡斯·斯特凡科，文章来源：welivesecurity

原文地址：[https://www.welivesecurity.com/en/eset-research/arid-viper-poisons-android-apps-with-aridspy/](https://www.welivesecurity.com/en/eset-research/arid-viper-poisons-android-apps-with-aridspy/%20)

译文仅供参考，具体内容表达以及含义原文为准。

# **Arid Viper 使用 AridSpy 毒害 Android 应用程序**

ESET 研究人员发现 Arid Viper 间谍活动正在向埃及和巴勒斯坦的 Android 用户传播木马应用程序

![]()

ESET 研究人员已确定了五项针对 Android 用户的活动，这些活动都带有木马病毒应用程序。这些活动很可能是由 Arid Viper APT 组织发起的，始于 2022 年，其中三项在本文发布时仍在进行中。他们部署了多阶段 Android 间谍软件（我们将其命名为 AridSpy），该软件从其 C&C 服务器下载第一阶段和第二阶段的有效负载，以帮助其避免被发现。该恶意软件通过专门的网站进行传播，这些网站冒充各种消息应用程序、工作机会应用程序和巴勒斯坦民事登记处应用程序。通常，这些是现有的应用程序，通过添加 AridSpy 的恶意代码而被木马病毒感染。

**博文的要点：**

* ESET 研究发现了三阶段 Android 恶意软件（我们将其命名为 AridSpy），通过五个专用网站进行传播。
* 在某些情况下，AridSpy 的代码被捆绑到提供合法功能的应用程序中。
* 虽然 AridSpy 的第一阶段之前已经记录过，但我们在这里还对其以前未知的后期阶段进行了全面分析。
* AridSpy 是一种远程控制木马，专注于窃取用户数据。
* 我们在巴勒斯坦和埃及发现了六次 AridSpy 现象。
* 我们中等程度确信 AridSpy 是 Arid Viper APT 组织所为。

Arid Viper 又名 APT-C-23、Desert Falcons 或 Two-tailed Scorpion，是一个自 2013 年以来一直活跃的网络间谍组织。该组织以针对中东国家而闻名，多年来因其针对Android、iOS和Windows平台的大量恶意软件而备受关注。我们在之前的博客文章中报道过该组织及其当时最新的间谍软件。

## 概述

ESET Research 发现了五个针对 Android 用户的 Arid Viper 活动。这些活动通过专门的网站传播恶意软件，受害者可以从这些网站上下载并手动安装 Android 应用程序。这些网站上提供的三个应用程序是被恶意代码木马化的合法应用程序，我们将其命名为 AridSpy，其目的是进行间谍活动。您可以在图 1 中看到概览方案。

![]()

*图 1. 渗透概览*

AridSpy 于 2021 年首次由Zimperium分析；当时，该恶意软件仅包含一个阶段，所有恶意代码都在木马应用程序中实现。

ESET Research 发现的第二次 AridSpy 攻击发生在2022 年（ 360 Beacon Labs随后于 2022 年 12 月对其进行了分析），恶意软件运营商将目标锁定在卡塔尔世界杯。该攻击活动冒充了众多 Kora 应用程序之一，部署了与 AridSpy 捆绑在一起的 Kora442 应用程序。与 Zimperium 分析的样本一样，该恶意软件此时仍只有一个阶段。

2023 年 3 月，360 Beacon Labs 分析了 Arid Viper 运营的另一个 Android 活动，并根据图 1 中提到的myScript.js文件的使用情况，发现 Kora442 活动与 Arid Viper 组织之间存在联系。我们在本博文讨论的活动中也发现了相同的联系（如*归因*部分所述）。事实证明，它是识别其他 Arid Viper 分发网站的有用指标。

2023 年 8 月，我们在遥测中记录了对 AridSpy 的检测，并进行了进一步调查。我们确定了巴勒斯坦和埃及的目标。在这些活动中，AridSpy 变成了一个多阶段木马，最初的木马化应用程序从 C&C 服务器下载了额外的有效载荷。

截至本文发布时，发现的五个活动中有三个仍在活动；这些活动使用专门的网站来分发冒充 NortirChat、LapizaChat 和 ReblyChat 以及 تطبيق المشغل（机器翻译：运营商应用程序；我们将其称为工作机会应用程序）和 السجل المدني الفلسطيني（机器翻译：巴勒斯坦民事登记处）应用程序的恶意应用程序。我们通过遥测、VirusTotal 以及使用[FOFA 网络搜索引擎](https://en.fofa.info/)（Shodan 和 Censys 的替代品）对共享 myScript.js 脚本进行分析发现了以下分发网站：

* lapizachat[.]com
* reblychat[.]com
* nortirchats[.]com
* pariberychat[.]com (不活跃)
* renatchat[.]com (不活跃)

在我们调查的同时，FOFA 研究团队发布了一篇[博文](https://medium.com/%40fofabot/practical-fofa-asset-expansion-apt-c-23-android-malware-7964b6625c6d)，讨论了发现七个带有myScript.js JavaScript 文件的分发网站，这些文件负责检索 Arid Viper 有效载荷的下载路径。其中四个网站分发了各种版本的 AridSpy。以下两个我们以前不知道：

* clemochat[.]com
* voevanil[.]com

在这篇博文中，我们重点关注可以从上面列出的所有已确认的活跃分发网站获取的 AridSpy 有效载荷。

请注意，这些恶意应用程序从未通过 Google Play 提供，而是从第三方网站下载的。要安装这些应用程序，潜在受害者需要启用非默认 Android 选项来安装来自未知来源的应用程序。

### **受害者学**

我们在遥测中总共检测到了六次 AridSpy 攻击，分别来自巴勒斯坦和埃及。在巴勒斯坦注册的大多数间谍软件实例都针对恶意的巴勒斯坦民事登记应用程序，还有一次检测结果不属于本博文中提到的任何活动。然后，我们在埃及发现了相同的第一阶段有效载荷，但包名称不同。在埃及还检测到了另一个第一阶段有效载荷，它使用与 LapizaChat 和工作机会活动中的样本相同的 C&C 服务器。

### **归因**

根据以下指标，我们以中等可信度将 AridSpy 归咎于 Arid Viper：

* AridSpy 针对的是巴勒斯坦和埃及的组织，这符合 Arid Viper 典型目标的子集。
* 多个 AridSpy 分发网站使用一个名为myScript.js的独特恶意 JavaScript 文件，该文件之前已被[360 Beacon Labs](https://www.ctfiot.com/106664.html)和[FOFA](https://medium.com/%40fofabot/practical-fofa-asset-expansion-apt-c-23-android-malware-7964b6625c6d)链接到 Arid Viper 。

myScript.js首次被发现，并被链接到 Arid Viper，是在[360 Beacon Labs](https://www.ctfiot.com/106664.html)于2023 年3 月 30 日对Arid Viper 运营的另一个 Android 活动的[分析中](https://www.ctfiot.com/106664.html)。该活动中使用的 (未命名) 恶意 Android 代码[之前归因](https://research.checkpoint.com/2020/hamas-android-malware-on-idf-soldiers-this-is-how-it-happened/)于 Arid Viper 组织。myScript.js在该活动中使用的分发网站之一上被发现。此 JavaScript 代码的目的是下载托管在分发服务器上的恶意 Android 应用程序。

图 2 显示了注册网站下载按钮点击处理程序的代码部分，图 3 显示了生成用于下载恶意应用程序的文件路径的 JavaScript 代码。

![]()

*图 2. 注册下载按钮的单击事件处理程序*

![]()

*图 3. 负责下载恶意应用程序的 JavaScript 代码*

[正如 360 Beacon Labs 指出的那样，我们在 2022 年报道过的](https://twitter.com/ESETresearch/status/1596222496121925633)针对卡塔尔 FIFA 世界杯的攻击活动中也使用了相同的 JavaScript 代码，该攻击活动使用了早期版本的 AridSpy。在两次攻击活动中，分发网站都使用了这个特定的myScript.js脚本从服务器中检索恶意应用程序，尽管最终的有效载荷有所不同。

最后，我们在本文讨论的活动的分发网站上发现了一段非常相似的 JavaScript，分发 NortirChat、LapizaChat 和 ReblyChat。在我们的调查过程中，FOFA 搜索引擎的研究团队独立证实了这种联系，他们发现了七个相同的分发网站，其中包含负责下载 Android AridSpy 的myScript.js ，并将[此恶意软件归因](https://medium.com/%40fofabot/practical-fofa-asset-expansion-apt-c-23-android-malware-7964b6625c6d)于 Arid Viper。

我们无法将这些活动中使用的 JavaScript 代码链接到任何合法或开源项目，这使我们相信该脚本很可能特定于各种传播 Android 恶意软件的 Arid Viper 活动。

Arid Viper 有可能重复使用了这种传播方法，但在新的攻击活动中改用了新工具 AridSpy，因为该组织之前使用的（未命名）恶意软件家族已被各种研究人员和安全公司[披露和分析。](https://www.ctfiot.com/106664.html)

有趣的是，我们还在 AridSpy 分发网站上发现了不同版本的myScript.js，伪装成巴勒斯坦民事登记应用程序。在这种情况下，该脚本具有相同的用途，但 JavaScript 代码不同：该脚本没有下载 AridSpy，而是返回了指向 AridSpy 的硬编码链接。

此版本的脚本基于[网上提供的](https://netparadis.com/javascript-tutorial-44-ajax/)脚本，与使用自定义开发的myScript.js文件的早期版本相反。当早期版本的myScript.js被披露并归因于 Arid Viper 时，威胁行为者很可能更改了其代码，以避免他们的新代码与该组织联系起来。

## 技术分析

### **初始访问**

本节中提到的所有活动的分发机制都非常相似。为了获得对设备的初始访问权限，威胁行为者试图说服其潜在受害者安装一个虚假但功能齐全的应用程序。一旦目标点击网站的下载按钮，托管在同一服务器上的myScript.js就会执行，为恶意 AridSpy 生成正确的下载文件路径。此脚本向位于同一服务器上的api.php发出 AJAX 请求，并返回特定的文件目录和名称。

#### **被木马感染的消息应用程序**

按时间顺序，我们首先看一下冒充 LapizaChat 的活动，这是一款恶意 Android 应用程序，可从专用的lapizachat[.]com网站下载。该网站于 2022 年 1 月16日注册，现已停止运营。其界面如图 4 所示。

![]()

*图 4. LapizaChat 网站*

*LapizaChat 网站*在服务器上的一个开放目录中，实际上有三个 LapizaChat Android 应用程序，它们存储在不同的目录中。其中一个应用程序是合法[StealthChat：私人消息应用程序的副本，没有恶意功能。它包含与 StealthChat 相同的合法消息代码，但应用程序图标、名称和程序包名称不同。该应用程序自 2022 年 1 月 18](https://play.google.com/store/apps/details?id=com.rockliffe.stealth)日起在分发网站上可用。

另外两个应用程序是 StealthChat: Private Messaging 的木马版本，与 AridSpy 的恶意代码捆绑在一起。根据最后修改日期，它们分别自 2023 年 7 月 5 日和 2023 年 9 月 18 日起在服务器上可用。这两个恶意应用程序彼此非常相似；后一个样本包含相同的恶意代码，只有微小的、不重要的变化。受害者在单击“立即下载”按钮后会从网站下载此版本。文件名、最后修改日期和哈希值列于表 1 中。

表 1. lapizachat[.]com网站上的样本

|  |  |  |  |
| --- | --- | --- | --- |
| **文件名** | **上一次更改** | **SHA-1** | **描述** |
| Lapiza聊天 | 2022-01-18 | D99D9689A7C893AFCE84 04D273D6BA31446C998D | 合法的[StealthChat：私人消息](https://play.google.com/store/apps/details?id=com.rockliffe.stealth)应用程序，版本 1.8.42 (6008042)。 |
| LapizaChat\_old.apk | 2023‑07‑05 | 3485A0A51C6DAE251CDA D20B2F659B3815212162 | StealthChat 被 AridSpy 木马病毒感染，以 LapizaChat 名义分发。 |
| Lapiza聊天 | 2023‑09‑18 | F49B00896C99EA030DCC A0808B87E414BBDE1549 |

我们发现了另外两个在 LapizaChat 之后开始分发 AridSpy 的活动，这次伪装成名为 NortirChat 和 ReblyChat 的消息应用程序。它们通过 2022 年 9 月 21 日注册的网站 nortirchat[.]com 和 2023 年 4 月 30 日注册的网站 reblychat[.]com 进行分发（点击下载按钮后）；见图5。

![]()

*图 5. NortirChat（左）和 ReblyChat（右）分发网站*

与前一种情况类似，我们能够从开放目录中检索到更多样本，包括消息应用程序的干净版本和木马版本。NortirChat 基于合法的[Session](https://getsession.org/)消息应用程序，而 ReblyChat 基于合法的[Voxer Walkie Talkie Messenger](https://play.google.com/store/apps/details?id=com.rebelvox.voxer)。在这两种情况下，木马应用程序具有相同的代码，但恶意软件开发人员更改了应用程序图标、名称和程序包名称。表 2 和表 3 列出了从这些服务器检索到的应用程序的详细信息。

表 2. nortirchats[.]com网站上的样本

|  |  |  |  |
| --- | --- | --- | --- |
| **文件名** | **上一次更改** | **SHA-1** | **描述** |
| NortirChat\_old.apk | 2022‑09‑28 | 13A89D28535FC1D53794 6D7D017DA02671227924 | 合法的[Session](https://getsession.org/)消息应用程序，版本 1.16.5 (3331)。 |
| Nortir聊天工具 | 2023‑03‑19 | 1878F674F59E81E86986 0EB9A2269046DF5CE855 |
| NortirChat\_old.apk | 2023‑06‑14 | 2158D88BCE6368FAC3FC B7F3A508FE6B96B0CF8A | 会话应用程序被 AridSpy 木马病毒感染，以 NortirChat 的名义分发。 |
| Nortir聊天工具 | 2023‑09‑11 | DB6B6326B772257FDDCB 4BE7CF1A0CC0322387D8 |

表 3. reblychat[.]com网站上的样本

|  |  |  |  |
| --- | --- | --- | --- |
| **文件名** | **上一次更改** | **SHA-1** | **描述** |
| 重新聊天 | 2023‑06‑08 | FFDD0E387EB3FEF7CBD2 E3DCA5D8924275C3FB94 | 合法的[Voxer Walkie Talkie Messenger](https://play.google.com/store/apps/details?id=com.rebelvox.voxer)应用程序，版本 4.0.2.22408 (3669119)。 |
| r...