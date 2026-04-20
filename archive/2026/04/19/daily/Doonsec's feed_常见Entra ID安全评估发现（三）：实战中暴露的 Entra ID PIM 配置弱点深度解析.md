---
title: 常见Entra ID安全评估发现（三）：实战中暴露的 Entra ID PIM 配置弱点深度解析
url: https://mp.weixin.qq.com/s/TAHKx0FnF7ujKSps8KiPiQ
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:55:22.411605
---

# 常见Entra ID安全评估发现（三）：实战中暴露的 Entra ID PIM 配置弱点深度解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibduy2LPdbTmZnjDkibDkKicKfJzaEATcibRCY9azTMX4OUic5dDlEhJ51Y1AHgbLBPMGuCVBRCKSibok06ric4T5eDHibSnFjUWJBYD4g/0?wx_fmt=jpeg)

# 常见Entra ID安全评估发现（三）：实战中暴露的 Entra ID PIM 配置弱点深度解析

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 许多企业部署了 Entra ID 特权身份管理，却因为配置宽松，安全效果大打折扣。本文基于真实的攻防对抗场景，深入剖析 PIM 的常见配置弱点、攻击者如何利用，并给出分层的加固建议。光有工具还不够，配置才是关键。

## PIM保护伞下的幻觉

微软 Entra ID 的特权身份管理已经成为保护云管理员账号的标准配置。按理说，它应该是一道坚固的防线：即时激活、时间限制、多因素认证、审批流程，听起来很美好。但实际情况是，我们经常在渗透测试和红队评估中看到，企业部署了 PIM，心里就踏实了，觉得管理员已经是“受 PIM 保护”的人了。

这种想法挺危险的。安全界有个现象，一旦采用了某种被认为“高级”的控制措施，其他基础性但重要的加固措施就可能被忽略。PIM 就是这样，它本身是个强大的工具，但如果配置得松松垮垮，反而会让人产生错误的安全感，实质防护效果远低于预期。

这就像给金库装了一道华丽的自动门，却忘记锁上旁边的普通木门。

## 那些司空见惯的宽松配置

PIM 的配置选项不少，但默认设置往往偏向于用户体验而非安全性。评估下来，我们反复撞见下面几种配置问题：

* 高特权角色未被纳入 PIM。企业通常记得把“全局管理员”放进 PIM，但像“身份验证管理员”、“域管理员”这类同样拥有巨大权力的角色，却常常被遗忘，处于永久分配状态。
* 依赖内置的 Azure MFA。这是最常见的场景，角色激活时只要求“完成 Azure MFA”。问题在于，如果一个攻击者通过网络钓鱼等手段，窃取到的访问令牌本身就携带着 MFA 声明，那么他在激活特权角色时，系统会认为“用户已经完成 MFA”，从而直接放行。
* 允许永久性活动分配。打开了这个口子，PIM 的时间限制就如同虚设。
* 缺失关键通知。高特权角色本应只在特殊情况下使用。如果缺少激活和分配通知，管理员在非工作时间激活角色的可疑行为就很难被发现。
* 过长的激活时长。一个全局管理员激活角色只是为了给另一个管理员赋权，几分钟就能搞定。但很多企业将最大激活时长设置为 4 小时、8 小时甚至更长。虽然用户可以选择一个更短的时效，但实际操作中，很少有人去改，这就给攻击者留下了过大的时间窗口。

## 两个生动的攻击案例

说理论太枯燥，我们直接看攻击者如何在真实场景中利用这些配置弱点。这两个例子都围绕一个核心：**PIM 只在角色激活那一刻提供保护，它不管激活前或激活后的事情。**

### 案例一：轻松搞定“条件访问管理员”

假设环境里，管理员账户 Alice 有条件访问管理员角色的合格分配。PIM 配置只要求 Azure MFA，无需审批。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd9kNEgPoZp22TI255WYuZcZjZBKxLNyYzNGz9FaDrKLVtwCKSjAQcIMNjKtiboDiaOqCBFc1LibsG3AbhRZ4QNYUyE6MuUyw70rI/640?wx_fmt=png&from=appmsg)

攻击者通过钓鱼拿到了 Alice 登录 Azure 门户的会话令牌。这个令牌的 `amr` 声明里已经包含了 `mfa`，证明 Alice 已经完成过 MFA。

PS> invoke-parseJwt $tokens.access\_token

aud                 : https://graph.microsoft.com
amr                 : {pwd, mfa}
app\_displayname     : Azure Portal
...
upn                 : adm\_alice@notasecuretenant.ch

虽然这个令牌不能直接读取条件访问策略，但通过 EntraTokenAid 等工具，利用 BroCi 身份验证流，可以交换到拥有 `Policy.Read.All` 等大量权限的新令牌。

这时，攻击者通过查询，确认 Alice 有资格激活“条件访问管理员”角色：

DisplayName                      Id
-----------                      --
Conditional Access Administrator b1be1c3e-b65d-4f19-8427-f6fa0d97feb9

然后，攻击者直接调用 Graph API，模拟 Alice 自己激活了该角色，并给自己设定了 5 小时的有效期。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibccyZFfzUxsrn2DbSYubibUvak3Wqtr3juwM1zaeRLyfvCiaIdZ1tchW61E6Q8eYD2x4xOasR3QibFItFM7Elxl0mwd3sDh1GIMmQ/640?wx_fmt=png&from=appmsg)

激活成功后，攻击者刷新令牌，重新连接 Microsoft Graph PowerShell，现在他就能看到并修改所有条件访问策略了。比如，直接禁用掉一条强制执行全员 MFA 的策略：

PS> Get-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "da2a711b-6404-4287-b784-90b36442ccdf" | ft Displayname,ID,State

DisplayName          Id                                   State
-----------          --                                   -----
Enforce\_MFA\_All\_User da2a711b-6404-4287-b784-90b36442ccdf disabled

这个案例的核心教训是：如果攻击者拿到的是一个来自管理门户的“热乎的”、已经包含 MFA 声明的令牌，而 PIM 激活仅依赖内置 MFA 检查，那么这道防线会轻易失效。

如果配置了要求在激活时进行**身份验证上下文**，强制执行“每次”重新认证，这个攻击路径就会难得多。

### 案例二：你有耐心就行：利用被盗的刷新令牌

这个例子更有意思。假设一个“用户管理员”角色的激活需要 MFA，但 Alice 正常登录 Microsoft Teams 时，并没有触发 MFA。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcEEmbO9IW4ZCuFtPJN8AXkl9icLAmQNicOjx7FAibWOG9phcuHtEhgy374KgTZeYDic1a9bFynrEwdXibOuDC8ibBnBTjUvdPuJ7ekk/640?wx_fmt=png&from=appmsg)

攻击者拿到了 Alice Teams 客户端的令牌，其 `amr` 声明只有 `pwd`，没有 `mfa`。因此，攻击者无法直接激活角色。

但 PIM 只保护激活的那一刻。如果条件访问策略没有限制会话生命周期，一个被盗的刷新令牌最长可以活 90 天，并且可以不断续期。攻击者只需要……等待。

假设过了一会，Alice 本人因为工作需要，通过门户激活了“用户管理员”角色。这时，她被 PIM 强制执行了 MFA。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcQTgcvJWKguLmLwFEcyWqnltSwhn9xahWmY8YJHjFlHsf5hSicU8ZbvA9GCT8FtzFLIydouJd7VVJGJwKOUDEZt50OOGAkwLG4/640?wx_fmt=png&from=appmsg)

一直在旁“蹲守”的攻击者，此刻只需要用他手里那个老的、不带 `mfa` 声明的刷新令牌去刷新一下，就能拿到一个包含新激活权限的访问令牌。更妙的是，利用 FOCI（客户端 ID 族）特性，他可以把令牌交换到 Office 365 Management 这个客户端应用上，这个应用预同意了一个强大的权限：`User.ReadWrite.All`。

PS> invoke-parseJwt $tokens.access\_token

aud                 : https://graph.microsoft.com
amr                 : {pwd}
app\_displayname     : Office 365 Management
scp                 : ... User.ReadWrite.All

现在，攻击者虽然没有完成 MFA，但他手里令牌的权限因为 Alice 的合法激活而“水涨船高”。他可以轻松地重置其他用户的密码，完全绕过 MFA。

PS> Update-MgUser -UserId Alex@notasecuretenant.ch -PasswordProfile @{ ForceChangePasswordNextSignIn = $false; Password = $newPassword }

这个案例清楚地揭示了 PIM 机制的本质：它不撤销现有会话，也不在角色激活后要求再次 MFA。它只在激活触发时设一道“安检门”，一旦合法用户刷脸过去了，他身后的“尾随者”可能也就混进去了。

## 补丁与局限：身份验证上下文不是万能的

上面两个例子都提到身份验证上下文是关键的补充防护。但它就万无一失吗？未必。

微软文档里藏着一个容易被忽略的限制：当策略设置为“每次”都要求重新认证时，它会有**5分钟的时钟容差**。这是为了避免用户在短时间内被频繁弹窗打断。但这5分钟，就成了攻击者的“黄金时间窗口”。

在第一个案例里，如果攻击者在用户完成认证后5分钟内，拿着新鲜的、带MFA声明的令牌去激活角色，即使配置了身份验证上下文，也可能依然成功。我们的测试发现，即使要求受管设备或合规设备，这个5分钟窗口有时也存在。

一个实战的加固技巧是：为同一个身份验证上下文，额外创建一个条件访问策略，要求访问必须来自受信任的IP地址或特定设备。虽然这不是微软官方文档的标准做法，但我们的测试表明，这可以有效封堵那5分钟的漏洞。说白了，就是给那道“安检门”再加一道地理围栏或设备锁。

## 用工具发现“隐形”漏洞

手动检查几十上百个角色的PIM配置很不现实。我们可以利用像 EntraFalcon 这样的开源评估工具。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdeCZCv53Gmyy26PPJPf0f6YXhEgIWVgF7wUNdG9vqjydoUOPKjImZOFzylEERMiclXVQCzeqYHibPSxnUhR0xCjaPcoRaYDhIjU/640?wx_fmt=png&from=appmsg)

它不仅能枚举所有PIM设置，还内置了多项安全检查。例如：

* PIM-002：检查是否存在绕过PIM、直接分配到Tier-0角色的情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd9xUHyHZ4xpXsEN3P2weVmeiaNxIFgb974PFy48YQ6y5RENppuflJZcR0UH2386eoQwiaxlO56JvfeI57bMOS3FewgbBar0uygA/640?wx_fmt=png&from=appmsg)

* PIM-009：检查Tier-0角色的激活是否需要审批或身份验证上下文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibek3cFPZtdAJmcVQRf0n44vytKyh9zvnhzXoJAI2iaTaoXJiaVwBkAic67kVLribqEfDoe5vOaPRw8Pn11AjoUj80iaJy5nGHbJcTvw/640?wx_fmt=png&from=appmsg)

工具还会生成一份详细的HTML报告，清晰列出每个角色的所有配置项，哪里弱了一目了然。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibenoDV0r03T3Uch8fqGKYiaTFR6l0ucibMjyicFicCHymNkpQ0qLicPVRuYcpbM3WCSgWUZo32JXibYeZchCrEnGa9qXqHFjHY1wTkBk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeAmRQufgKUbefSBoY1TvMBn7SicsbvB2ZbHXicia6axH36To0ysbENUWJ5onKtrjWo6HT0KGBTjEfR6ImW5jcGQ77RyP0PYtibECQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdWWBhpunZYxR8Wuertfu3sxt26uctaicYEJEH5FXUibsQqSECAr2iaFWHWRUqJ600TW25cU8FCfGmicKiaegqB4f61Em3iachD3p2eQ/640?wx_fmt=png&from=appmsg)

## 给你的PIM分层加固

没有放之四海而皆准的配置，但根据角色层级设定基线是可行的。记住，PIM本身不足以完全保护特权访问，必须结合严格的、基于设备或IP的条件访问策略。

### Tier0/控制平面角色

这类角色（全球管理员、特权角色管理员等）只用于执行特定、短暂的任务。配置必须最严格。

* 最大激活时长：2到4小时。
* 激活要求：绑定一个强身份验证上下文，强制执行钓鱼防护MFA，且“登录频率”设置为“每次”。
* 可以考虑在上下文中附加要求（如特定IP范围或设备），来对抗5分钟漏洞。
* 激活时要求填写理由：是。
* 激活需要审批：是。这是防止攻击者自助激活的最后一道有效闸门，即使他控制了管理员设备。
* 发送激活通知：是。
* 允许永久活动分配：否（仅限应急账户考虑）。

### 较低层级角色

这类角色（如服务台人员使用的）可能用于日常操作。每次激活都审批和通知，会让人疲于奔命，最后变成摆设。

可以采取一个更实用的基线：

* 最大激活时长：10到12小时。
* 激活要求：身份验证上下文（要求MFA，“每次”）。
* 激活时要求填写理由：是。
* 激活需要审批：否。
* 发送激活通知：否。

对于其中一些仍涉及敏感操作或极少使用的角色，可以在这个基础上酌情收紧。

说到底，配置 PIM 是一场在安全性与可用性之间的精准平衡。最危险的配置不是“没有”，而是“有却没用对”，它让你误以为自己很安全，却在攻击者面前门户大开。打开你的 PIM 配置页，对照检查一下，你的“金库自动门”，旁边那扇木门锁好了吗？

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过