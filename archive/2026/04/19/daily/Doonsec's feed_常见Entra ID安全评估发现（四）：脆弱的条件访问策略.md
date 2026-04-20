---
title: 常见Entra ID安全评估发现（四）：脆弱的条件访问策略
url: https://mp.weixin.qq.com/s/uBWkg7-l2EaR8WrNeVpsRg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:57.042017
---

# 常见Entra ID安全评估发现（四）：脆弱的条件访问策略

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibd6lH6ZQVZHqEuhPoskSUmI9XzFcXWicfmFG8NY6rFibrhJbB548cbiaqYzZfEFKjOyRPE8J7y1ZJQSmzGqSPbmdrjhn9xjfrRTdQ/0?wx_fmt=jpeg)

# 常见Entra ID安全评估发现（四）：脆弱的条件访问策略

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 设置一大堆条件访问策略并不意味着安全。本文基于实战评估经验，剖析了配置中常见的雷区：从身份覆盖不全、资源定位失准，到内置绕过和策略缺失。文章用真实攻击案例，展示了攻击者如何利用这些缝隙，最后提供了简洁的排查工具和加固原则。

这是系列文章的第四篇，聊聊我们在企业环境中做微软Entra ID安全评估时，经常发现的条件访问策略问题。

## 条件访问策略是个好东西，但容易用坏

说条件访问策略是Entra ID里最重要的安全控制之一，应该没人反对。它决定了用户在什么情况下才能访问租户资源，比如是否要求多因素认证（MFA），设备需要什么状态，只能在特定地点登录，或者对敏感应用实施更严格的控制。

但问题就出在复杂性上。策略的效果不光看你有没有设，更看你怎么设计、范围划多大、以及后续怎么维护。这里面的坑，比很多人想象的多。

所以这篇不讲入门教程，聚焦在那些削弱政策有效性的常见配置失误和设计缺陷上。都是我们在实战中一次次碰见的。

## 策略设计配置中的常见问题

复盘现有的条件访问策略，是每次Entra ID评估的重头戏。下面挑几个最具代表性的问题说说。

### 身份覆盖不全：策略找不到人

策略得明确对哪些人生效。这里的短板经常让关键用户处于保护伞之外。

**通过组来圈定用户**是常规操作，比如把强制MFA的策略应用到某个安全组。理想很丰满，现实很骨感——我们经常发现，目标组里并没包含所有相关用户。有些人就这么溜出策略范围，完全没享受到应有的保护。

**基于角色的覆盖**是另一个常用手段，专门针对管理员账户。想法不错，但我们总能看到租户里有些正在使用的特权角色，根本没被相关策略覆盖到。还有个微软的“特性”要留意：条件访问策略里的角色定位，**不考虑范围受限的角色分配**。比如一个用户的“用户管理员”角色只限定在某管理单元（Administrative Unit）内，那以该角色为目标的条件访问策略，根本管不着他。

### 资源定位狭窄：你以为的“全部”不是全部

有时候，重要的保护机制只被应用到特定资源上。比如，只对“Microsoft管理门户”要求钓鱼攻击防护的MFA。

这里有个认知偏差：这些预设资源的选择，其覆盖范围并不总是你想的那样。“Microsoft管理门户”只保护基于网页的管理门户，而敏感操作完全可以直接通过Microsoft Graph API来完成。定位不准，等于给攻击者开了侧门。

### 条件太多：安全网变得全是窟窿

有人把条件访问比作身份防火墙。这个比喻挺误导人。和传统防火墙不同，条件访问默认不会拒绝所有认证活动。默认情况放行，除非有适用的策略施加强制控制或阻断。

这意味着策略范围极其重要。你在策略里每多加一个条件（比如网络地址、设备平台、客户端应用），它适用的认证事件数量就减少一层。条件有时是必要的，但太多就会意外制造出很多保护盲区。我们常见到策略的实际范围比管理员预想的要窄得多。

一个典型例子：一个策略同时包含了“登录风险”和“用户风险”作为条件。这两个条件是**“与”**的关系，必须同时满足才能触发策略。但问题是，同一个登录行为下，这两者往往不重合。登录风险是在认证过程中评估的，而用户风险是后台单独计算，可能通过离线检测才被提升。结果就是，这种策略在实践中极少被触发，防护效果大打折扣。

### 内置绕过：平台总有自己的后门

就算策略覆盖了所有用户和所有云应用，也不意味着每个相关动作都能管到。

有些动作，比如注册安全信息或加入设备，必须有专门针对性的策略才能覆盖。此外，微软自己实现了一些内置绕过和例外。这可能是为了避免破坏重要的平台功能。麻烦在于，这些并非都有清晰的文档说明，容易让人对实际保护力度产生误判。

一个广为人知的例子就是，只要求合规设备的策略有一个内置绕过，它仍允许有限的操作，比如读取设备信息。

所以，即使范围宽广的策略，也别想当然地认为它覆盖了所有操作。

### 策略缺失：以为到位了，其实空白

据我们观察，现在大部分租户都用条件访问来强制MFA了。但在评估时，其他关键策略的缺失依然常见：

* 没有限制安全信息注册的策略
* 没有封堵设备代码流的策略
* 没有强制特权管理员账户使用钓防护MFA的策略
* 没有限制特权管理员从什么设备/地点访问租户的策略
* 没有限制用户从什么设备访问关键业务资源的策略

这里特别提一下**安全信息注册限制**，这个漏洞的影响时常被低估。

### 排除（大段）IP范围：为省事而冒险

我们经常看到重要策略（比如MFA要求）排除了一些特定IP段。很多时候这样做是为了减少用户的MFA弹窗次数。

但这种排除往往没必要，尤其是在使用混合加入（Hybrid Joined）或Entra加入设备的混合环境中，主刷新令牌（Primary Refresh Token， PRT）机制本身就已经能减少重复的MFA提示。

更糟的是，有时排除的IP段范围很大，比如/24或/23子网。特别是在较小的组织里，这些子网里可能不只是员工的公网IP，还混杂着访客Wi-Fi或DMZ网络。这种大开方便之门大大削弱了防护，增加了滥用的风险。

## 攻防演练：当理论变成实际的风险

光说问题可能不够直观，看看下面的攻击场景，你会更清楚这些配置疏漏意味着什么。

### 滥用缺失的安全信息注册保护

针对“注册安全信息”这个用户操作的条件访问策略，可以限制用户在什么条件下才能注册MFA方法或使用自助密码重置（SSPR）。

很多人下意识认为，只有当账户已被完全攻破（比如通过中间人钓鱼或令牌窃取）后，MFA方法注册才成为问题。但还有一个场景容易被忽略：如果一个用户**尚未注册任何MFA方法**，且没有策略保护“注册安全信息”这个操作，那么这个账户当前的保护就只剩密码。

于是，如果一个攻击者搞到了密码（比如通过密码喷洒），他仍然有可能在通用的MFA条件访问策略生效前，去注册一个新的MFA因子。然后，这个新注册的因子就能让他在后续登录中满足MFA要求。

假设租户只有一个要求所有用户MFA的策略。Alice的账户是新创建的，还没配MFA。 那么，一个拿到Alice密码的攻击者，仍然可以先注册自己的MFA因子，从而满足要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcOPm54eZqWmpWnmVoM0Kmqxl5FsKibC1RayiafxzE2tcyNjHWDrTEsialxIoiaNXa9442qPSCDSau6hcXQmausb7JcvfADD7GLNwo/640?wx_fmt=png&from=appmsg)

甚至在一些更严格的环境下，比如配置了要求合规设备或已加入设备，或者存在一个本该完全阻断Alice访问的策略，这个攻击路径仍可能走通。下图是一个此类策略配置的例子：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfKg0zIk1kVkTQWfFpsahZIzZFjCMCHy2Ik3v1PYnoCOJOe5FVcy2qcsewIJibcnbziagNqvIFmOWLa8vs2C7lKKzicuhZjicKgzU4/640?wx_fmt=png&from=appmsg)

在正常的门户登录流程中，MFA注册向导可能不再出现，取而代之的会是一个错误提示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibdmtl8TmBCNZvGDbQ2anaqZPzy3CJibSmB9kicYJzy9cH6Ce0eiaohAeSSuFPicJQBL19GtKlMsia4m9oFVBgm34BFAasxGXc2aWIv8/640?wx_fmt=png&from=appmsg)

然而，在某些特定条件下，仍然可能通过利用已知条件访问绕过的应用来触发MFA流程，从而注册新因子。比如使用像**EntraTokenAid**（https://github.com/zh54321/EntraTokenAid）这样的工具，可以强制执行Nexus（NGC）MFA流程：

PS> invoke-Auth -ClientID 1950a258-227b-4e31-a9cf-717495945fc2 -RedirectURL http://localhost:13824 -api 26a4ae64-5862-427f-a9b0-044e62572a4f -ForceNgcMfa -DisableCAE
[\*] Local redirect URL used. Starting local HTTP Server..
[+] HTTP server running on http://localhost:13824/
[i] Listening for OAuth callback for 180 s (HttpTimeout value)

作为此流程一部分打开的浏览器窗口里，又可以注册新的MFA因子了：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfEsb3Ac56IXUia8icDyRqj5efniaskb6r72PvYNJNUVo1ZFAIIlJmbUQpPYRKHDcRicK3mpNqq2ukQ4HNPIj60avUS6pIvMBJUpia0/640?wx_fmt=png&from=appmsg)

> 注意：在第二种场景下，攻击者可能只能注册**额外的**MFA因子，而无法直接访问资源。要真正访问，仍然需要依赖现有策略中的弱点或绕过。

关键点在于，即使是限制所有资源的目标、看上去很严格的条件访问策略，也未必能防住每一个动作。保护具体的用户操作（比如注册安全信息），必须靠专门的条件访问策略。

除了实施专门的策略，其他措施也很重要：

* 对用户强制更严的身份验证要求，例如基于设备的限制，这样仅靠掌握密码和MFA是无法访问的。
* 避免账户使用弱的或重复的初始密码。
* 避免将不必要的账户（如本地服务账户或管理账户）同步到云端。

### 利用薄弱的资源定位

我们经常看到条件访问策略只保护特定资源。一个实际的例子是：只对“Microsoft管理门户”应用额外保护（比如特定IP限制、设备要求或钓防护MFA），意图是防止攻击者执行管理操作。

问题在于，这些内置资源选择的实际覆盖范围并不总是那么清晰。“Microsoft管理门户”保护的是网页版管理门户，但**不保护**其他接口，例如通过不同OAuth客户端直接访问Microsoft Graph API。

举个例子，我们启用官方的Microsoft策略模板“要求对Microsoft管理门户进行多重身份验证”。这个策略以全局管理员和其他特权角色为目标，应用于“Microsoft管理门户”资源，并强制要求MFA：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdiaoMcS1Af8euSibgQtpI90s2B8QmJ4W21PrdyuHE3Yia96PJQT7JXg5KvPnKPuVYGROhshmhfdQcp2fw8RANUsCUKNu7r6yKWbI/640?wx_fmt=png&from=appmsg)

但如果全局管理员Bob，使用第一方应用“现代工作区客户API原生”（Client ID： 2e307cd5-5d2d-4499-b656-a97de9f52708）的客户端ID，向Microsoft Graph API请求令牌会怎样？这个策略不会生效。结果就是，他甚至可以从控制台直接用资源所有者密码凭证流登录：

PS> $tokens = Invoke-ROPC -ClientID 2e307cd5-5d2d-4499-b656-a97de9f52708 -Username adm\_bob@notasecuretenant.test -Password "[CUT-BY-COMPASS]" -Api graph.microsoft.com
[\*] Starting ROPC flow: API graph.microsoft.com / Client id: 2e307cd5-5d2d-4499-b656-a97de9f52708 / User: adm\_bob@notasecuretenant.test
[+] Got an access token and a refresh token
[i] Audience: https://graph.microsoft.com / Expires at: 04/03/2026 17:02:46

PS> $tokens
token\_type      : Bearer
expires\_in      : 86399
ext\_expires\_in  : 86399
access\_token    : eyJ0eXAiOiJKV1QiL[CUT-BY-COMPASS]
Expiration\_time : 03.04.2026 17:02:46
scp             : Application.Read.All AuditLog.Read.All DeviceManagementApps.ReadWrite.All DeviceManagementConfiguration.ReadWrite.All DeviceManagementManagedDevices.PrivilegedOperations.All DeviceManagementManagedDevices.ReadWrite.All DeviceManagementRBAC.ReadWrite.All DeviceManagementServiceConfig.ReadWrite.All Directory.AccessAsUser.All email Group.ReadWrite.All Mail.Send openid Policy.Read.All Policy.ReadWrite.ConditionalAccess profile Reports.Read.All
                  User.ReadWrite.All WindowsUpdates.ReadWrite.All
tenant          : 9f412d6a-xxxx-xxxx-xxxx-32e31a6af459
user            : adm\_bob@notasecuretenant.test
client\_app      : Modern Workplace Customer API Native
client\_app\_id   : 2e307cd5-5d2d-4499-b656-a97de9f52708
auth\_methods    : {pwd}
ip              : [CUT-BY-COMPASS]
audience        : https://graph.microsoft.com
api             : graph.microsoft.com
xms\_cc          : {CP1}

在对应的登录日志里，能看到那条强制MFA的条件访问策略确实没有被应用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcGadPicHxrgc3JzVLKMcKOHxQp7rXpA8zEyBBQgz8MSxQy3MBU9pdaaq9CbT1jT6BSwjyU81YxHrggEvBib1ILJHxJFgRVoMSkc/640?wx_fmt=png&from=appmsg)

结果就是，Bob可以直接通过Microsoft Graph API执行管理任务，根本不用走门户。他甚至可以**禁用一条条件访问策略**：

PS> Connect-MgGraph -AccessToken ($Tokens.access\_token | ConvertTo-SecureString -AsPlainText -Force)

Welcome to Microsoft Graph!
Connected via userprovidedaccesstoken access using 2e307cd5-5d2d-4499-b656-a97de9f52708

PS> Get-MgIdentityConditionalAccessPolicy | ft Displayname,ID,State

DisplayName Id                                   State
----------- --                                   -----
EnforceMFA  edafc746-76e3-4a04-9a0d-e9ccb1e5939c enabled

PS> Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "edafc746-76e3-4a04-9a0d-e9ccb1e5939c" -BodyParameter @{state = "disabled"}

PS> Get-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "edafc746-76e3-4a04-9a0d-e9ccb1e5939c" | ft Displayname,ID,State

DisplayName Id                                   State
----------- --                                   -----
EnforceMFA  edafc746-76e3-4a04-9a0d-e9ccb1e5939c disabled

### 展示针对合规设备要求的内置绕过

还有一些微软没有明确记录的内置绕过。例如，Dirk-jan Mollema在2023年发现，可以使用OAuth客户端“Microsoft Intune Company Portal”（客户端ID：9ba1a5c7-f17a-4de9-a1...