---
title: 网络罪犯操纵 GitHub 平台传播恶意程序
url: https://www.anquanke.com/post/id/298491
source: 安全客-有思想的安全新媒体
date: 2024-07-27
fetch_date: 2025-10-06T17:41:17.654084
---

# 网络罪犯操纵 GitHub 平台传播恶意程序

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

# 网络罪犯操纵 GitHub 平台传播恶意程序

阅读量**173978**

发布时间 : 2024-07-26 14:59:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Antonis Terefos，文章来源：checkpoint

原文地址：<https://research.checkpoint.com/2024/stargazers-ghost-network/>

译文仅供参考，具体内容表达以及含义原文为准。

* **Check Point Research** 发现了一个 GitHub 帐户网络（**Stargazers、Ghost Network**），该网络通过网络钓鱼存储库分发恶意软件或恶意链接。该网络由多个帐户组成，这些帐户分发恶意链接和恶意软件，并执行其他操作，例如加星标、分叉和订阅恶意存储库以使其看起来合法。
* 该网络是一种高度复杂的操作，充当**分发即服务** （**DaaS**）。它允许威胁行为者共享恶意链接或恶意软件，以便通过高度面向受害者的网络钓鱼存储库进行分发。
* **Check Point Research** 正在追踪这项服务背后的威胁组织，即 **Stargazer Goblin。**该组织提供、运营和维护 **Stargazers Ghost Network**，并通过其 GitHub Ghost 帐户分发恶意软件和链接。
* 该网络分发了各种恶意软件系列，包括 **Atlantida Stealer**、**Rhadamanthys**、**RisePro、Lumma Stealer 和 RedLine**。
* 我们的最新计算表明**，超过 3,000** 个活跃的 Ghost 帐户是该网络的一部分。根据核心 GitHub Ghost 帐户，我们认为该网络在 **2022 年 8 月**左右首次开始小规模开发或测试。
* **Check Point Research** 在暗网论坛中发现了一个广告商，该广告商提供了确切的 GitHub 操作。第一个广告于 **2023 年 7 月 8 日**发布，来自前一天创建的帐户。
* 根据 **2024** **年 5 月中旬**至 6 月中旬的监测活动，我们估计 **Stargazer Goblin** 的收入约为 **8,000 美元**。但是，我们认为这个金额只是演员在此期间所赚的一小部分。据估计，在业务生命周期内的总金额约为**100,000美元。**
* **Stargazers Ghost Network** 似乎只是大局的一部分，其他 Ghost 账户在不同的平台上运行，构建了一个更大的**分发即服务**宇宙。

#

# 介绍

威胁行为者不断改进其策略，以保持领先于检测。通过包含恶意附件的电子邮件分发恶意软件的传统方法受到严格监控，公众对这些策略的认识越来越高。最近，**Check Point Research** 观察到威胁行为者使用 GitHub 通过使用新方法实现初始感染。以前，GitHub 用于直接分发恶意软件，恶意脚本会下载原始加密脚本代码或恶意可执行文件。

他们的战术现在已经发生了变化和发展。威胁行为者现在运营着一个由“幽灵”账户组成的网络，这些账户通过在其存储库上的恶意链接和加密档案作为发布来分发恶意软件。该网络不仅分发恶意软件，还提供各种其他活动，使这些“幽灵”帐户看起来像正常用户，从而为他们的行为和相关存储库提供虚假的合法性。Check Point Research 观察到这些帐户分叉、加星标和监视恶意存储库，营造出合法项目的假象，并引诱受害者下载“广告”内容。

在短时间的监控中，我们发现了 **2,200** 多个发生“幽灵”活动的恶意仓库。在 2024 年 1 月左右发生的一次活动中，该网络分发了 **Atlantida stealer**，这是一种新的恶意软件家族，会窃取用户凭据和加密货币钱包以及其他个人身份信息 （**PII**）。这场运动非常有效，因为在不到 **4 天**的时间里，超过 **1,300** 名受害者感染了 **Atlantida stealer**。指向 GitHub 存储库的恶意链接可能是通过 Discord 频道分发的。这些存储库针对各种类型的受害者，他们希望增加在 YouTube、Twitch 和 Instagram 上的关注者，并且还包含用于破解软件和其他加密相关活动的网络钓鱼模板。

![]()

*图 1 – Stargazer Ghost 帐户。*

#

# Stargazers Ghost 网络

很长一段时间以来，GitHub 一直被用作分发恶意代码的平台。通常，此类活动中涉及的仓库是为特定活动新创建的，并且通常会长时间保持在线状态，然后被 GitHub 关闭或被威胁参与者清理。但是，这些存储库中的内容通常不会向普通用户建议他们应该下载并执行任何托管脚本或可执行文件。

这些类型的攻击并非旨在引诱用户直接从存储库本身下载和执行有效负载。相反，它们通常涉及从看似合法的网站或来源下载和执行有效负载的脚本。这种方法有助于保持合法性的外观，同时向受害者提供恶意内容。

Stargazers Ghost Network 通过提供一个恶意存储库来改变游戏规则，其中恶意链接被多个 GitHub 帐户“加星标”和“验证”，从而支持其合法性。

![]()

*图 2 – 恶意 GitHub 帐户引诱 Twitch 用户。*

通常，网络使用相同的标签和图像，但将“目标受众”从一个社交媒体应用程序或破解软件切换到另一个，但使用相同的模板。这表明网络运营商可以自动化这些活动，从而确保其运营的效率和可扩展性。

![]()

*图 3 – TikTok、YouTube、Twitch、Instagram、…使用相同的网络钓鱼模板。*

网络钓鱼模板包含指向外部网站的恶意链接。在某些情况下，此链接会将受害者重定向到恶意 GitHub 存储库的“发布”部分。GitHub 通常会尝试检测恶意文件或档案，尽管在许多情况下，网络使用受密码保护的档案来“隐藏”扫描解决方案中的任何恶意活动。`README.md``DOWNLOAD`

![]()

*图 4 – 恶意软件通过密码加密的存档版本进行分发。*

在这种情况下，包含一个网络钓鱼下载链接，该链接甚至不会重定向到存储库自己的版本。相反，它使用三个具有不同“职责”的 GitHub Ghost 帐户：`README.md`

1. 第一个帐户提供“网络钓鱼”存储库模板。
2. 第二个帐户提供用于网络钓鱼模板的“图像”。
3. 第三个帐户在发布中以受密码保护的存档形式提供恶意软件。

这种结构和操作方法使 **Stargazer Goblin** 能够快速“修复”由于帐户或仓库被禁止进行恶意活动而可能发生的任何断开链接。通过在多个账户之间分配责任，网络确保了更换其受损组件的灵活性。这最大限度地减少了对其运营的干扰，使他们能够迅速适应并继续在 GitHub 上进行恶意活动。

第三个帐户为恶意软件提供服务，更有可能被检测到。发生这种情况时，GitHub 会禁止整个帐户、仓库和相关版本。作为对此类行为的回应，**Stargazer Goblin** 使用指向新的活动恶意发布的新链接更新了第一个帐户的网络钓鱼存储库。这使网络可以在恶意软件服务帐户被禁止时以最小的损失继续运行。

```
# [Download](hxxps://github.com/soulkeeper500/soulkeeper500/releases/tag/lat)

![trovos](hxxps://github.com/Minori702/Trovo-Toolkit/assets/154011813/98f626f2-0e25-4379-8902-801bd93892aa)

### ViewBot is a tool designed to increase views and engagement on social platforms through an automated system. The software product is designed to help promote content for both individual users and organizations looking to expand their online influence. ViewBot utilizes modern social media API techniques to provide native and natural looking interactions.

**Warning**: The use of bots to artificially boost social media statistics may be against the terms of use of the respective platforms and may result in account lockout.

## Features

- Live viewers
- Trovo Account creator
- Chat bot
- Follow bot
- Shares
- Mass report
- Support for multiple accounts to create organic traffic
- Customize time intervals between "views" to simulate a real user
- Simple and easy-to-use user interface
- Support for proxy servers for anonymity and security

## Technologies

- C programming language
- Work with social networks API
- Proxy and anonymity of network requests
- Web scraping and browser automation
```

从有经验的人来看，这些存储库似乎很可疑。令我们感到惊讶的是，这些仓库中的每一个都收到了大量的“星星”。进一步调查发现，负责为这些恶意仓库加星标/“点赞”的账户是同一操作不可或缺的一部分。

![]()

*图 6 – 恶意存储库的观星者。*

我们观察到许多名为 Stargazer Ghost 的账户具有一种模式，这些账户包含具有以下特征的仓库：

* 仓库名称：`.{username}1`
* 创建了两个文件：
  + 许可证文件：`LICENSE`
  + 说明文件：`README.md`
* 此外，`README.md` 文件的标题是账户名后跟文本 `"1"`。具体来说，`README.md` 文件的内容如下：

```
README.md
# {username}1
1
```

这里 `{username}` 是具体的用户名部分，会被替换成实际的用户名。

![]()

*图 7 – GitHub Ghost 帐户存储库模式。*

当我们搜索该特定模式时，我们发现了 1,100 多个存储库，这表明可能有 1,100 多个 Ghost GitHub 帐户属于这个恶意的 Stargazers 网络。

![]()

*图 8 – README.md 内容模式。*

Stargazers 网络中的每个 Ghost-Stargazer 并不局限于只与一个存储库交互。其中许多帐户与多个存储库交互，其中很大一部分显然涉及恶意活动。但是，其他一些带星号的存储库看起来同样可疑，例如一些与 WordPress 相关的游戏模组工具。

![]()

*图 9 – Ghost 帐户加星标的仓库。*

根据这些 **Ghost Stargazers** 的广泛项目和“兴趣”——从玩 Counter-Strike 到 Instagram 影响者，再到使用破解的防病毒软件黑客攻击和保护机器——我们能够发现更多的恶意模板并进一步扩大我们的 **Ghost Stargazer** 账户集合。

![]()

*图 10 – 游戏作弊存储库*。

当恶意链接重定向到 GitHub 版本时，我们观察到关联帐户通过喜欢这些恶意版本来做出反应的情况。这种行为进一步强化了项目对毫无戒心的用户所感知的“合法性”。

![]()

*图 11 – 释放反应。*

为了进一步区分帐户及其操作，我们发现了一些情况，即也是该网络一部分的其他帐户提交了恶意网络钓鱼文件。`README.md`

![]()

*图 12 – 提交到另一个人的帐户项目。*

目前尚不清楚所有这些帐户是否都是由 **Stargazer Goblin** 出于恶意目的创建的。正如我们后来的研究表明的那样，其中一些帐户已遭到入侵。这使得信息窃取者获得的 GitHub 凭据变得有价值，而且，价值足以在地下市场上出售和购买。

#

## “下架”和“维护”周期

多种不同的角色提供了便于网络维护，因为 GitHub 不会关闭与分发恶意软件的存储库相关的所有帐户。这使得以下帐户在对托管恶意软件的存储库采取行动时以最小的“损害”继续其操作：

1. 存储库-网络钓鱼帐户。
2. 提交链接帐户。
3. 观星者账户。
4. 和任何其他帐户。

下面的存储库自那时以来一直处于活动状态，并经历了 **6** 次链接更改。这 **6** 次提交是由 进行的，通过更新恶意软件链接来维护攻击链。`buttercupserial/HubSpot-activation-by-nuat``2024-05-28``buttercupserial/168463497+buttercupserial@users.noreply.github.com`

![]()

*图 13 – 维护提交。*

|  |  |
| --- | --- |
| **提交日期** | **恶意软件 URL** |
| 2024-05-28T10：21：50Z | hxxps://github[.]com/bludmooncutie2/bludmooncutie2/releases/tag/latest |
| 2024-05-29T07：35：32Z | hxxps://github[.]com/witch12138/test/releases/tag/lat |
| 2024-06-04T06：51：50Z | hxxps://github[.]com/soulkeeper500/soulkeeper500/releases/tag/lat |
| 2024-06-06T07：40：15Z | hxxps://github[.]com/xumuk71discoatoh/xumuk71discoatoh/releases/tag/new |
| 2024-06-10T02：09：27Z | hxxps://goo[.]su/gisof1sda –> hxxps://github[.]com/zigzagcharming643/zigzagcharming643/releases/tag/lat |
| 2024-06-10T09：13：52Z | hxxps://github[.]com/xumuk71discoatoh/xumuk71discoatoh/releases/tag/new |

提交精确地修改了下载链接，同时保持网络钓鱼模板的其余部分完好无损。

![]()

*图 14 — 链路更改。*

最新的链接指向一个版本，该版本具有受密码保护的存档，该存档执行GO下载器`Git_softwares_v1.1.2.7z``Setup_v1.1.2.exe` (`SHA256:98B7488B1A18CB0C5E360C06F0C94D19A5230B7B15D0616856354FB64929B388`)

![]()

*图 15 – 受密码保护的释放。*

该网络的维护和恢复过程似乎是自动的，会检测被禁止的帐户/存储库，并在必要时进行修复。使用不同的账户角色可确保在 GitHub 对违反其规则的账户或仓库采取行动时，只会造成最小的损害。

![]()

*图 16 – Stargazers Ghost Network 角色概述。*

大多数时候，我们观察到 **Repository 和 Stargazer 账户**不受禁令和仓库下架的影响，而 **Commit 和 Release 账户**通常在检测到其恶意仓库后被禁止。找到包含被禁止**的 Release-Repositories** 链接的 **Link-Repositories** 是很常见的。发生这种情况时，与 **Link-Repository** 关联的 **Commit 帐户**会使用新链接更新恶意链接。

**Commit 账户**与 **Repository 账户**下的所有仓库保持一对一的关系。这意味着同一个**提交账户**可以对属于同一**仓库账户**的仓库进行多次提交。

对于典型的广告系列，我们通常会遵守以下要求：

* 一个**存储库帐户，**即托管要下载的链接的网络钓鱼存储库的所有者。
* 一个 **Commit 账户，**用于对属于 **Repository 账户**的仓库进行提交
* 一个 **Release 帐户**，用于创建恶意存档并将其添加到存储库的发布中，并每天更新存档以在更长的时间内不被发现。
* X **Stargazer 帐户**，它分叉/星标/喜欢存储库和发布。

在上述场景中，**Release 帐户**通常是第一个被禁止的。然后，网络运营商创建一个新的恶意链接，并使用其相关的**提交帐户**更新所有**链接仓库**。总之，2 个账户（**Repository/Commit**），加上 X 个**观星者**，仍然处于雷达之下，而 **1** 个 **Release 账户**可能会在未来的某个时候被禁止。这些网络角色设法以某种方式“绕过”GitHub 的安全度量。

#

# 战役一，Starga...