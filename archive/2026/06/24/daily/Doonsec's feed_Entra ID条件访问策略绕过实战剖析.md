---
title: Entra ID条件访问策略绕过实战剖析
url: https://mp.weixin.qq.com/s/lf0IAKRiG5V1VpJDTAZWFQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:40.550455
---

# Entra ID条件访问策略绕过实战剖析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Kric7mM9eA5Baboe7BFOBmb0HibL7sGXibdg0FjFNgFu2rWjkVibSKXvrg2bBicyz4AYcL126gRKviaV7ZJIKCe6m4pczV7VbgQP7ECAcIbG4BNDw/0?wx_fmt=jpeg)

# Entra ID条件访问策略绕过实战剖析

Dubito
Dubito

云原生安全指北

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 注：本文翻译自 Dirk-jan Mollema[1] 的文章《Bypassing Conditional Access policies that have a resource exclusion》[2]，可点击文末“阅读原文”按钮查看英文原文。

## 一、引言

条件访问策略中存在一个有文档记录的强制实施缺口[3]，该缺口出现在那些应用于“所有资源”但同时又排除了至少一个资源的策略中。而文档中没有记录到的是，这个缺口比人们预期的要大得多，而且文档中给出的缓解措施实际上并不起作用。如果你是一名Entra管理员，好消息是：微软现在认为这是旧版行为，正在对其进行更改。如果你的租户尚未自动迁移，你可以选择启用新行为，该行为能够解决并修复此问题。如果你的策略中存在资源排除项，我强烈建议你应用此项更改。

## 二、为何写这篇博客

这个绕过问题背后有一些故事，并且主要基于先人研究。去年，在我与Fabian Bader合作进行TROOPERS演讲[4]时，我已经意识到了该问题的存在记录的部分。而未记录的部分则是在过去一年中逐渐浮出水面的，当时有几个人联系我，讨论条件访问的异常行为——尽管存在本应阻止的条件访问策略，但仍然可以获得具有有限范围（scope）的令牌。因此，虽然我自己也对此主题做了一些研究，但大部分内容其实已经被其他人发现了。据我所知，唯一公开描述此问题的资源是Syntax-Err0r的这篇博客[5]，他在BloodHound Slack上的昵称是`Jmcgill`。该博客还提到，此问题已向MSRC报告，并被认定为“设计如此”。我认为，微软方面处理此问题的人将其标记为“设计如此”是一个错误，很可能是由于对这一流程所涉及的复杂性缺乏理解所致。

我决定对此主题做进一步研究，作为Fabian和我去年开始的、旨在映射已知CA绕过方法工作的一部分。在确认了相同问题及其影响后，我提交了包含根本原因分析和影响说明的报告给MSRC，希望能改变他们的看法。在与Fabian反复讨论后，他发现微软针对此问题推荐的缓解措施[6]实际上也不起作用，这为这个故事带来了新的转折，并催生了更多MSRC报告。与之前其他研究人员的报告不同，微软这次承认了该问题，并且正在推出一个默认修复此绕过的更改，不过何时能收到新设置可能取决于你的租户。

尽管部分内容已经公开，我还是决定写这篇博客，原因如下：

* • 进一步提高大家对CA策略存在资源排除项时所面临风险的认识。
* • 解释为何最初会有此排除项的技术背景，以及是什么机制使得绕过成为可能，因为这是一个复杂的问题，我觉得大多数人并不理解。
* • 鼓励租户管理员尽快选择启用新行为，或者至少在他们无法迁移时，能准确了解其中的风险。

这些说完，让我们深入实际机制。

## 三、资源排除行为详解

在OAuth2身份验证流程中，我们指定两个重要参数：**client** 和 **resource**。client是我们正在使用的客户端应用程序，例如Teams或Outlook（两个常见的Microsoft客户端）。这些客户端获得的token是针对特定资源的，例如`https://graph.microsoft.com`或`https://sharepoint.com`。资源是托管我们数据的API，或是我们访问的应用。条件访问策略是按资源创建的，这意味着如果我创建了一个针对Exchange的策略，那么它不依赖于我登录时使用的客户端，而是任何为Exchange请求令牌的客户端都会触发该策略。CA策略中的“资源”部分过去被称为“云应用”，这个术语并不能很好地反映支撑身份验证流程的机制。

有一种特定的登录形式，其中“云应用”这一术语是合理的，那就是当我们使用OpenID Connect流程登录Web应用程序时。在这种情况下，client和resource是相同的，因为我们登录的是应用本身，而不是某个特定的上游API（资源）。这也就是为什么如果我们创建一个针对基于Web的应用（作为目标资源）的策略时，该策略会在我们登录该应用时生效。

现在来说排除项。如果我们将策略应用于“所有资源”，那么无论我们在登录流程中指定什么资源，该策略都会触发，并且CA引擎可以在每次登录流程中强制执行控制（除少数由用户操作覆盖的边缘情况外）。一旦我们添加了排除项，事情就变得复杂一些了。假设我们希望对所有登录强制执行某项控制（如MFA），但有一个应用我们认为不重要，或者强制控制会导致其故障，因此我们将其排除。于是我们添加了一个排除资源，即我们要排除的那个应用。除了登录到那个被排除应用的流程外，所有登录流程都应该强制执行该策略。但这里有一个问题，与Microsoft Graph（以及之前的Azure AD Graph，不过现在几乎所有应用都已经无法使用它了）有关。在现实世界中，应用通常不仅仅使用OpenID Connect流程（由`openid`scope体现），还会为Microsoft Graph请求一个令牌，以查询有关用户的一些信息。这通常通过非常基础的范围（scope）（例如`User.Read`）来完成。你可以在多个示例中看到这一点，例如下面的代码片段，这是一个关于使用Microsoft身份验证库（MSAL）的示例flask应用[7]：

![MSAL示例请求User.Read](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5CWRqfv3M60mheUncqBlzcz4046qLT3JFkfR1YFPPdutMIbmIbePYXR5C14cibXsoNYpFkBgq2wsV1bjicA9vKOwfY7JUZ2HVxHA/640?from=appmsg "null")

MSAL示例请求User.Read

此时条件访问策略评估就变得复杂一些了。我们不仅要登录到应用程序，还要为Microsoft Graph资源请求一个令牌。Microsoft Graph资源比较特殊，因为根据我们的应用程序所拥有的委托权限（scopes），Microsoft Graph API可用于访问许多后端资源中的信息。如果我们严格强制执行条件访问策略（这正是新行为所做的），那么为Microsoft Graph作为资源请求任何令牌都**不会**命中我们策略中的排除部分，因为我们只排除了一个特定应用，而不是Microsoft Graph。这意味着该策略仍然会触发，这可能不是管理员所期望的，并且可能会中断登录流程。而且，我们无法将Microsoft Graph本身添加为策略的排除项，这使得我们无法允许该应用进行这种有限的信息访问。

为了让管理员更容易处理此流程，微软决定，一旦你的“所有资源”策略中存在排除项，并且被排除的应用仅请求非常有限的范围（scope）（例如`User.Read`），他们将允许签发具有这些scope的令牌。实际上，他们会允许**所有应用**请求这些低权限scope而不会触发该策略。有趣的是，即使你创建了另一个不同的策略来覆盖那个被排除的资源并强制相同的控制，它仍然会允许低权限的scope。这意味着，“所有资源”策略与一组两个策略（其中一个应用于所有资源但带1个排除项，另一个针对该排除项单独设置）之间存在一个缺口。Fabian在我们的Troopers演讲中很好地介绍了这一点，并在他关于此主题的博客[8]中也进行了讨论。

当然，问题是攻击者可以利用这一点做什么。如果我们阅读文档，会发现一个允许的低权限范围（scope）列表：

![此例外中允许的scope。公共客户端的情况最值得关注。](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BUKvcILR1rM4jx3VH0iaGud4icoAraBxIDCMshGeoM7cvdQJicbo7mepM9FhT2QIaibgfnD8q6sNNM8xO0bzpKKxHVnJrxx4kibPuQ/640?from=appmsg "null")

此例外中允许的scope。公共客户端的情况最值得关注。

在这种边缘情况下，公共客户端和机密客户端之间存在差异。对于攻击者而言，公共客户端场景最有可能出现，因为拥有机密客户端意味着攻击者已经控制了受害者租户中的一个应用，并拥有client secret或证书来对该客户端进行身份验证，这不太可能是初始访问场景。公共客户端则更容易攻击，因为我们可以在登录流程中直接使用client ID来伪装成这些公共客户端之一。许多微软拥有（第一方）的公共客户端都是可用的，你可以在entrascopes.com[9]上找到它们，这是Fabian和我创建的项目，用于映射这些信息。

如果我们查看公共客户端允许的scope，会发现这些权限并不高，仅影响用户自身的数据。如果我们拥有一个用户的有效凭证，我们就有可能绕过带有资源排除项的策略，但访问权限仅限于读取该用户的个人资料。不是什么大问题，对吧？而且，如果你真的想堵住这个缺口，微软还在“保护目录信息”部分记录了一种缓解措施，尽管它相当复杂，涉及创建自定义属性并将其填充到Azure AD Graph服务主体上。

## 四、Scope是假的

如果文档是准确的，并且这些scope能被正确强制执行，那么这一切都不会成为大问题。但在过去几年里，有几个人带着奇怪的边缘情况来找我，即Microsoft应用能够通过Microsoft Graph访问Entra ID信息，即使令牌中的scope表明这应该不可能。遗憾的是，这是另一个例子，说明我们在Microsoft Learn上读到的文档限制对于**我们自己的**应用是准确的，但并非总是适用于Microsoft自己的应用。事实证明，对于某些Microsoft应用，令牌中的scope会被忽略，并且允许的数据访问范围比实际强制执行scope时应该允许的范围要大。这让我想起了Eric Woodruff几年前的研究，他发现Microsoft应用可以通过某种不透明、未记录且对租户管理员不可见的权限系统，通过Microsoft Graph执行操作。这同样适用于令牌中的scope。即使令牌没有访问租户中用户或组信息的scope，调用Graph API请求这些信息时，实际上也会返回数据。

我决定将此纳入我的一个测试脚本中。现在，该脚本不仅会收集scope，还会尝试通过Microsoft Graph请求数据，即使scope表明我们没有那种访问权限。利用这种技术，我们识别出了几个应用，尽管访问权限有限，但仍然可以枚举Entra ID中的数据。例如，应用“Microsoft Bing Search”，其client ID为`cf36b471-5b44-428c-9ce7-313bf84528de`。我们请求一个具有有限scope的令牌，并在文档行为的界限内进行操作：

```
roadtx interactiveauth -s 'https://graph.microsoft.com/User.Read email profile openid' -c cf36b471-5b44-428c-9ce7-313bf84528de
```

在下方的截图中，我们可以看到，当对此客户端进行身份验证时，我们获得的令牌确实只包含我们请求的有限scope：

![令牌中的Scopes](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5ARfCUiakEXJw4ibfRm4SRwEU2Ld0N3E2TyYdbtYkco27mrbWlPvlSA4hiaNIn8LicxiceIO8lPqA3h8FbicRRso3ZtxibEGaOONou7UQ/640?from=appmsg "null")

令牌中的Scopes

当我们忽略scope的声明，直接尝试调用Microsoft Graph时，我们确实能够读取租户信息，在此例中是列出租户中的组：

![作为MS Graph查询结果返回的ServicePrincipals](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5Dr62nuxxmozNLECXy0XBtiapmZ6pJMMOHibbmxAyAUO03aC07EPPetZk9CWn8J4SS3m9WN8QnFc3K8zykiaU5xpibjaIoVbTjYiawI/640?from=appmsg "null")

作为MS Graph查询结果返回的ServicePrincipals

对于这个特定的客户端，尽管scope不允许这种数据访问，但我们可以查询Entra ID中的以下信息（基于Microsoft Graph上可用的端点）：

* • users
* • groups
* • devices
* • contacts
* • applications
* • servicePrincipals
* • directoryRoles

在我的测试案例中，实施的控制是多因素认证，但无论控制是什么，此绕过都有效。如果存在一个排除了某个资源的策略，无论该控制是什么，都可以被绕过，并且我们可以基于签发的令牌查询Entra ID数据。虽然这是一种有限的绕过（我们无法用它来访问邮件或文件），但我们可以利用它来绕过策略，并可能暴露用户的个人信息。我在多个真实场景中遇到过此类策略，在这些场景中，它可以被用来绕过MFA并枚举租户数据，所以这不仅仅是理论上的练习。它也不仅限于读取信息，因为我已经发现一些具有隐藏scope的应用，如果用户拥有足够的权限，这些scope也可以用来**修改**租户中的信息。

## 五、“保护目录信息”缓解措施

如果此行为（当“所有资源”策略存在排除项时，允许签发有限scope）的文档化部分是不可取的，微软提供了缓解措施[6]来修复此缺口。这涉及相当多的步骤，因为该缓解措施需要针对“Windows Azure Active Directory”资源，而这只能通过自定义安全属性来完成。如果你费了很大功夫（我从未在任何真实场景中见过这样做），你会认为现在无法再请求这些令牌了。如果我们运行与之前相同的命令，现在会提示我们进行MFA：

```
roadtx interactiveauth -s 'https://graph.microsoft.com/User.Read email profile openid' -c cf36b471-5b44-428c-9ce7-313bf84528de
```

![提示MFA](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DhjPHwtXUbPZicugGhxiaVyqMzt338icAF7SictVnYzWJWhlcuBjbLgQVm3xibficI2k3GbleS6wzkafpY50KDwpu6hcHhJGcFw08TQ/640?from=appmsg "null")

提示MFA

我和Fabian讨论了这个问题，几周后他进行了一些自己的测试，发现了更多异常情况。即使实施了更严格的策略，他仍然发现对于少数特定客户端，单因素身份验证可以成功。事实证明，如果你只请求`openid` scope，你仍然会被签发令牌。如果我们修改上面的命令以反映这一点，那么身份验证实际上会再次成功：

```
roadtx interactiveauth -s 'https://graph.microsoft.com/openid' -c cf36b471-5b44-428c-9ce7-313bf84528de
```

虽然现在令牌不再包含`User.Read` scope，但我们仍然可以像之前一样请求相同的Entra ID信息，这并不奇怪，因为我们之前已经发现后端完全忽略了这些scope。

登录日志也反映，用于保护目录信息的策略并未被应用。

![策略未应用](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5ApSFre7Qx7qiaNY06qADWIy6kPePzH6agcHAsCOwibXkBjmL9G02jGMias7akrlxPFxaBsUlW2Eian3dqcahlN0SuDKX0Kd7z6fvs/640?from=appmsg "null")

策略未应用

总而言之，即使你应用了文档中针对此缺口的缓解措施，该策略仍然可以被绕过，攻击者仍然可以枚举和修改租户中的数据。

## 六、修复方案

正如微软在一月份宣布的[10]，这些策略的强制执行将从6月15日开始改变。该公告博客没有提及旧版行为中未记录的缺口，只提到了行为将如何变化。我认为，租户管理员应该意识到，只要这项更改未在其租户中自动推出（这可能需要数月时间），或者当他们选择继续使用旧版行为时，他们所面临的风险。不过也有好消息，那就是你已经可以选择启用新行为，如文档[11]所述。

为此，你需要通过此Entra管理中心的直接链接[12]访问一个隐藏界面，并将基线scope强制实施配置为启用状态。

![基线scope用户界面](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5CqwPb205LDftZSpoOBglFxVNvlcyWe656xS8n97iauL2ywiaVPVaRCgxVLVjhV7hK3H5sdwPTnWdW1wLam2GulqicLbHTPdMEsNo/640?from=appmsg "null")

基线scope用户界面

启用该强制实施后，CA策略绕过将停止工作，并且当这些应用为Microsoft Graph请求令牌时，相关控制将被强制执行。

#### 引用链接

`[1]` Dirk-jan Mollema: *https://dirkjanm.io*
`[2]` 《Bypassing Conditional Access policies that have a resource exclusion》: *https://dirkjanm.io/bypassing-conditional-access-with-resource-exclusion/*
`[3]` 有文档记录的强制实施缺口: *https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#legacy-conditional-acc...