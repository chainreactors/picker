---
title: 利用 BloodHound OpenGraph 映射欺骗方案 - Configuration Manager 篇
url: https://mp.weixin.qq.com/s/6ahSAebPOqxErm7eFYNV3Q
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:37:46.669778
---

# 利用 BloodHound OpenGraph 映射欺骗方案 - Configuration Manager 篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSjQmulEibPB9NZfT7ibRmxEtXiciaialsVwGHWGxCmcrLaficIDvt9MK1oaWWuDDb1ia6K2MvSzM9K62TqQgZW2UQkMqTxHl4aPQOdUVk/0?wx_fmt=jpeg)

# 利用 BloodHound OpenGraph 映射欺骗方案 - Configuration Manager 篇

Joshua Prager
Joshua Prager

securitainment

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjFmsYGsuu4yGiaGuFpu97IJHLG4MUGwU6iaBk9pK8gdqOPURTPd7YRQILj2UolZibtIRhewK4kdLvtdNeJicwt6Xm6fgmEA2klSbs/640?wx_fmt=png&from=appmsg)

| 原文链接 | 作者 |
| --- | --- |
| https://specterops.io/blog/2026/02/19/mapping-deception-solutions-with-bloodhound-opengraph-configuration-manager/ | Joshua Prager |

***摘******要：****SpecterOps 从多个视角审视攻击路径管理，其中包括识别适合部署高质量欺骗方案的位置。本文探讨如何在 Configuration Manager (SCCM) 基础设施中识别可用于部署欺骗方案的关键区域，并结合 Chris Thompson 的 ConfigManBearPig 和 Ben Schroeder 的 deceptionClone 项目，提供在 OpenGraph 中映射这些关键区域的实操示例。*

## 欺骗方案方法论

作为安全顾问，我曾多次参与私营和公共部门的欺骗方案项目。根据我的经验，最有效的欺骗方案会利用对手认为具有吸引力的现有攻击路径来达成目标，而非在环境中随机散布 canary 账户或文件 (例如 *passwords.txt*)。

随机放置的 canary 存在一个核心盲区：真实的对手通常以最少的步骤达成目标 (即阻力最小的攻击路径)。我曾见过 APT 组织仅通过转储外部 SharePoint 服务器上交互式登录的 Domain Administrator 账户凭据，便从该服务器的 Local Administrator 提权至 Domain Administrator。随后，对手利用窃取的凭据横向移动至域控制器 (DC) 并转储 \_NTDS.dit\_。

HasSession 攻击路径已经摆在对手面前，他们直接加以利用。在此场景下，对手没有理由四处搜寻某个文件共享上的 "passwords.txt"。这个 canary 文件对攻击者缺乏吸引力，也未能与环境充分融合，不会被纳入对手的目标规划。

在为客户开发欺骗方案的过程中，SpecterOps 认为有效的欺骗方案需满足以下属性：

* **融合性**

  : 能与环境自然融为一体
* **吸引力**

  : 攻击者能够发现该欺骗方案 (并且会主动利用)
* **零新增风险**

  : 不会引入可被利用的新攻击路径
* **高保真度**

  : 访问行为能被可靠检测

Ben Schroeder 撰写了 Mapping Deception with BloodHound OpenGraph，深入阐述了 SpecterOps 的欺骗方案开发方法论。前文已对该方法论做了概要介绍，此处不再赘述。接下来，我们将重点讨论如何利用 Configuration Manager 实施欺骗方案。如果你希望进一步了解 SpecterOps 的方法论，或为内部威胁团队及检测工程团队构建类似的方法论框架，推荐阅读 Ben 的博客。

## 使用 OpenGraph 实现欺骗方案

防御者可以利用 BloodHound OpenGraph 来映射环境中已部署的欺骗方案，以便于规划和追踪。BloodHound OpenGraph 于 BlackHat 2025 前后发布，在 BloodHound 社区版和企业版中均可使用。OpenGraph 功能使组织能够将任意数据映射为图形 (我说的是真正的任意数据——我们的 Adversary Tactics and Detection 课程中，学生就在 BloodHound OpenGraph 里构建了端点检测与响应 [EDR] 遥测模型)。

BloodHound OpenGraph 的 *设计*用途是帮助组织将企业环境数据的映射范围扩展到 Active Directory 和 Entra ID 之外，覆盖第三方服务和应用程序。例如，OpenGraph 可以将 Active Directory 用户与 GitHub 访问模型关联起来，再从 GitHub 访问模型追溯到 AWS secrets。组织现在能够跨多个分散且看似独立的技术栈，以图形方式呈现访问模型。目前，我们正在开展 OpenGraph Community Incentive Program，社区成员可以通过映射独特的应用程序和身份提供者来参与，并有机会获得 SO-CON 2026 的全额赞助参会资格 (含门票、机票和酒店)。

作为在 BloodHound OpenGraph 中映射欺骗方案的实操示例，防御者可以使用 Ben Schroeder 的 deceptionClone 项目来修改 OpenGraph 节点属性，以展示已部署的欺骗方案。本文将同时展示欺骗方案在 deceptionClone 项目修改节点前后的对比效果。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjmicFydMEtX2posQVJzo3eQNuKsBY46bz5kwDOIHRHNiaZFWx906yWdfUhx6aHX1A09H0cHtG7GiaHpezwiaxrzJroEruP4ibFf6ko/640?wx_fmt=png&from=appmsg)

*在 GitHub 仓库中可视化欺骗凭据*

## ConfigManBearPig

Chris Thompson 发布了 ConfigManBearPig，用于映射组织环境中的 System Center Configuration Manager (SCCM) 基础设施。该工具生成 JSON 数据供 BloodHound OpenGraph 导入，以图形化呈现支撑 Misconfiguration Manager 项目攻击路径遍历的基础设施边关系。

ConfigManBearPig 是一个 BloodHound 收集器，通过 LDAP 识别对 `System Management`容器具有 "Full Control" 权限的对象来采集站点服务器信息。它还会收集 objectClass 为 `mSSMSSite`的主站点信息。收集器会继续枚举 SCCM 基础设施，发现管理点、中央管理站点 (CAS) 和 SCCM 客户端设备。关于该 BloodHound 收集器的工作原理和使用方法，请参阅 Introducing ConfigManBearPig, a BloodHound OpenGraph Collector for SCCM。在该文中，Chris Thompson 对收集器进行了详细描述并说明了完整的使用方法。本文将使用 ConfigManBearPig 项目中的 "sample\_data" 作为实操示例。

## Configuration Manager 欺骗方案

Configuration Manager 近来频繁成为攻击性安全研究的目标。随着 SpecterOps Misconfiguration Manager 项目的推出，攻击方已开始利用客户的端点管理基础设施执行脚本和部署载荷。Configuration Manager 之所以成为对手眼中极具价值的目标，是因为其基础设施对站点内的每个端点都拥有管理权限。

SCCM 由多个关键基础设施组件构成，这些组件支撑着 SCCM 站点内每个端点的管理功能。如需了解这些节点在 OpenGraph 中的基础设施视图和操作指南，请参阅 Chris Thompson 的博客 "Introducing ConfigManBearPig, a BloodHound OpenGraph Collector for SCCM"。以下章节将直接介绍欺骗方案，假设你对 SCCM 基础设施已有一定了解。

## 欺骗方案：Canary NAA

Site Distribution Points 是面向客户端的内容服务器，负责托管客户端可检索和执行的内容。Site Distribution Points 经常成为对手的攻击目标，因为它们托管了供首次加入环境的客户端使用的 Pre-Boot Execution (PXE) 媒体 (后文将详细讨论)。Management Points 则是客户端任务服务器，客户端会定期向 Management Points 发送消息以签到，并根据 SCCM 策略请求更新。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSh5Zh0ibXa4Ja60I3ofjfd8sv2iaTG4PoTwYEpUgqBakDfeR3g8ywXkt8ImWfke2WYPKNDB6wA6wq674iaymQlvVEKMoOJ4go1Qqc/640?wx_fmt=png&from=appmsg)

*Site Distribution Points 与 Management Points*

根据 Misconfiguration Project 的 CRED-1 技术，PXE 媒体从 Site Server 分发至 Distribution Point，未加域的客户端可通过 TFTP 从 Distribution Point 下载启动映像。正如 CRED-1 描述中所述："此过程可被滥用，因为无需启动 PXE 媒体即可访问相关文件和策略。"攻击者通过发送 `DHCPDISCOVER`请求，即可发现 Distribution Point 并下载启动媒体。启动媒体使用密码加密，可借助 hashcat 破解并恢复密码哈希。启动媒体解密后，攻击者可能从中识别出网络访问账户 (NAA)。

NAA 是一个通常在 Site Server 上配置的域账户。SCCM 站点客户端使用 NAA 账户来访问和检索软件、更新及策略。NAA 往往是一个权限过高的账户——我们过去见过该账户对所有工作站拥有 `AdminTo`权限，甚至被配置为 SCCM 管理员账户或 Domain Administrator 账户。该域账户存储在每台 SCCM 客户端上。攻击者利用 PXE 媒体和 NAA 的合法流程来获取可用于横向移动的域账户。

ConfigManBearPig 不会采集 NAA 的节点和边关系，因为收集器无法保证 NAA 凭据的有效性。不过，从欺骗方案的角度，我们可以部署 canary NAA 凭据，并通过手动编辑 ConfigManBearPig JSON 输出在 BloodHound OpenGraph 中对该关系进行建模。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjtYdQK2smpEVyGh83G2Z2NcbdYgB8BfYSchdFN7lWzkT6duOlcB4ibUiaHY2u8HWicQZv6CFyrvE9tVYg1hUbrVZFKiaVnia8lH1jo/640?wx_fmt=png&from=appmsg)

*手动添加的 Contains NAA*

该欺骗方案记录在 Misconfiguration Manager 项目的 CANARY-1 中。防御者可以在 Active Directory 中创建新用户，使用与其他 SCCM 相关服务类似的命名规范 (例如 "`<DOMAIN>-SCCM-NAA`" 或 "`SVC-SCCM-NAA`") 来创建 canary NAA。此欺骗方案可用于检测使用开源 SCCM 工具枚举或窃取 NAA 账户凭据的对手，例如 Chris Thompson 的 SharpSCCM 和 Adam Chester 的 SCCMWTF。

**注意：**我在实操配置示例中使用的靶场与 BloodHound OpenGraph 截图中展示的 ConfigManBearPig 项目 "sample\_data" 靶场不同。

0. 在 DC 上运行 *dsa.msc*
1. 在 Active Directory 中创建新的 NAA 用户，使用上述类似的命名规范 (例如 "`<DOMAIN>-SCCM-NAA`" 或 "`SVC-SCCM-NAA`")，并为账户添加逼真的描述 (最好与现有 NAA 描述风格一致)
2. 将密码设置为看起来逼真的内容 (例如 16 位随机字符 **别担心，我们稍后会将密码重置为更安全的密码)**)
3. 账户在 Active Directory 中创建完成后，点击账户属性中的 "Security" 选项卡，为该账户配置 SACL 审计
4. 点击 "Advanced" 按钮，然后点击 "Auditing" 选项卡
5. 点击 "Add" 按钮
6. 在 "Auditing Entry for " 弹窗中，点击 "Select a Principal" 按钮![选择要审计的主体](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShoZdjLYtlmbzgAbt16m6jb313KwicSwWXMzvQoAqhWn8YLeDkhNr4FvL5QFuQicpvBicpfI9shIS4PCauBp5l2BvRf5q29mLW0Y8/640?wx_fmt=png&from=appmsg)

   选择要审计的主体
7. 选择 "Everyone" 作为审计主体，然后点击 "OK"
8. 在 "Type" 下拉菜单中选择 "All"
9. 勾选以下审计权限：

   List Contents

   Read all properties

   Write all properties

   Read permissions

   Modify permissions

   Modify owner

   All extended rights

   Allowed to authenticate

   Change password

   Receive as

   Reset password

   Send as

   Read msDS-OperationsforAzTaskBL

   Read msDS-parentdistname

   ![SACL 中的审计权限](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSh4wC6qyBkkAUcf0y2QYibweiciaOiakjeVXALibJCuSXVibGbQ8O1ISkic8tH3Q1pIl1Zzicocy6ukPGo5xoUI8ROGgy9X4dnuamussxc/640?wx_fmt=png&from=appmsg)

   SACL 中的审计权限

为创建有效的欺骗方案，防御者可以编辑该账户以限制交互式登录，避免引入新的可利用攻击路径。

1. 仍在 *dsa.msc*中，右键点击该账户并选择 "Account" 选项卡
2. 点击 "Log On To…" 对话框按钮
3. 选择 "The following computers" 并将列表留空
4. 点击 "OK"，然后点击 "Apply" 保存配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgkicWmfuCxwZibmdg1h2TYrjQgIx1jjfXMg2ibL6EH73WBU0kAibEjiaDMefgoAezKyIzTbSNcicJA2IQdISjOX1hBia1VnGhbdNVHGk/640?wx_fmt=png&from=appmsg)

*禁用交互式登录*

为确保该账户不被滥用，请确认账户配置如下：

* 密码永不过期
* 用户无法更改密码

账户在 Active Directory 中创建完成且 SACL 已设置后，登录 System Center Configuration Manager 控制台：

1. 登录后，导航至 "Administration" 菜单并点击 "Site Configuration" 下拉菜单
2. 点击 "Site" 链接，选择要部署 canary NAA 的站点
3. 点击 "Configure Site Components" 并选择 "Software Distribution"
4. 弹窗出现后，选择 "Network Access account" 选项卡，点击太阳图标选择新的 NAA canary

![Adding the Canary NAA to Configuration Manager](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSglGKZ4dq4tk9psaT9glTlShibeo9URBwvXLIiaibgFGo0tbswSXUZwEy1ZLM5hjTzsYL7a0ncBmycUa3eDjZmKodH4wnbWLn6pP0/640?wx_fmt=png&from=appmsg)

Adding the Canary NAA to Configuration Manager

*将 Canary NAA 添加到 Configuration Manager*

##### 超级重要提示 (认真的！别跳过这一步！)

账户已在 Active Directory 中创建并作为 NAA 添加到 SCCM 后，你需要在 Active Directory 中将 NAA 账户的密码轮换为新的 64 位随机字符密码 (后文将详细说明)。

我们可以使用 cloneDeception.py 脚本将自定义边插入到 NAA canary 所在站点的 Distribution Points，从而在 BloodHound OpenGraph 中对 NAA canary 进行建模。

![Canary NAA Account in OpenGraph](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgE11TEKT3xk46N5...