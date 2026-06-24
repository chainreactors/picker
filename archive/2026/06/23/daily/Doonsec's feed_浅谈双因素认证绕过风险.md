---
title: 浅谈双因素认证绕过风险
url: https://mp.weixin.qq.com/s/7Ucb5s2-mT5OrU1zmO9l2Q
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:02:31.992856
---

# 浅谈双因素认证绕过风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gdu7PMCZg1VL1EpWwPS1he0R5icRicEEleZuiajzyml9ibibG089rXHGfsC3FjGBCHao8gniapgfYpcYYazzf9bu9ZMUqcqlM8yIGoNia13TH706HM/0?wx_fmt=jpeg)

# 浅谈双因素认证绕过风险

搜狐安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

![](https://mmbiz.qpic.cn/mmbiz_png/SrOXk7eUN2AEGyvFib1GMFVd2LlrpHOyWDGYx0Fia3TevSvufdmYzGcqicZlSs5Xp2KB33HkBpGOHwe4SsoYxGx5w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/vS6eQicRY6DAILuiaPanZx5LaibWTlBwRd3w5FCFhdn0BVIgqakmJDhHSrmdIXaQUtYzGWic4Wvic95JO45tlWZibFuw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ibiam3zEgeEV5NCZHFlFGjd1Xfcq3GtWaheaQ6AiaZIXOu9grVg2JWZgON6VRKHdMw3FGzH0xCXa1w71HqPcicXURA/640?wx_fmt=png)

在当前的企业网络安全边界防御中，双因素认证（2FA / MFA）已被公认为降低凭据泄露风险的基石。无论是落实合规要求，还是部署零信任架构，引入第二阶段验证（如动态口令、硬件令牌）都是标准配置。

然而，安全对抗是一个动态演进的过程。随着 2FA 的普及，攻击者针对认证链路的攻击技术也已走向成熟。本文将介绍当前主流的 2FA 绕过技术路径，并探讨企业应如何升级防御维度。

![](https://mmbiz.qpic.cn/mmbiz_png/aFb4Q75OW00TY4hfnVcdkRcCPKVSEdAfXKwiaCIRMztick8iaQJ5ic5ePp3knJ2fp249qPtgYGtvbr17NXuQSTKAfw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icTPiaaqor4ibZ6bExU5nT2CNpeNibcSIJpHc63evNrLibyjq68g4ZgXlIC4FfHW5Hd5W75zwgMOyY69tJz6B0nYHKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1UPEtJh3hRyesctoVPiasqjqZV0FVfrVP9I9ZE2ORw4aibAgqGmTRFDPDUJHZkPrzjAwFhIgW2a1j8Mk5STVyLIEvEicf14vb0kRc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/vS6eQicRY6DAILuiaPanZx5LaibWTlBwRd3w5FCFhdn0BVIgqakmJDhHSrmdIXaQUtYzGWic4Wvic95JO45tlWZibFuw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ibiam3zEgeEV5NCZHFlFGjd1Xfcq3GtWaheaQ6AiaZIXOu9grVg2JWZgON6VRKHdMw3FGzH0xCXa1w71HqPcicXURA/640?wx_fmt=png)

双因素身份验证 (2FA，也称为多因素身份验证或 MFA) 是一种安全方法，要求用户在登录帐户时提供两种或多种不同类型的证明来验证其身份。传统上，网站会结合邮箱和密码来验证用户身份并确认其访问权限。然而，弱密码或普遍存在的不安全身份验证机制往往会降低这种方法对应用程序整体安全性的保障。双因素身份验证 (2FA) 是一种额外的身份验证方法，它基于用户必须拥有并提供的临时凭证，而不能仅仅记住该凭证。这种方法安全性更高，因为额外的安全层可以防止恶意行为者未经授权访问用户帐户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1Ud0TJkwmlH01nhic7QysPeC6ej3qP1dvibCB3ZIz1RAjRvaHS5duzcWbVbjVIfvyZnu3GXmSMR1AEBZddibFqW1NLUXzRNpLxibdw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/aFb4Q75OW00TY4hfnVcdkRcCPKVSEdAfXKwiaCIRMztick8iaQJ5ic5ePp3knJ2fp249qPtgYGtvbr17NXuQSTKAfw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icTPiaaqor4ibZ6bExU5nT2CNpeNibcSIJpHc63evNrLibyjq68g4ZgXlIC4FfHW5Hd5W75zwgMOyY69tJz6B0nYHKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif)

双因素认证的信任边界

![](https://mmbiz.qpic.cn/mmbiz_png/vS6eQicRY6DAILuiaPanZx5LaibWTlBwRd3w5FCFhdn0BVIgqakmJDhHSrmdIXaQUtYzGWic4Wvic95JO45tlWZibFuw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ibiam3zEgeEV5NCZHFlFGjd1Xfcq3GtWaheaQ6AiaZIXOu9grVg2JWZgON6VRKHdMw3FGzH0xCXa1w71HqPcicXURA/640?wx_fmt=png)

2FA 的核心逻辑是通过引入“用户拥有的物品”（如手机、硬件凭证）或“用户固有的特征”（如生物识别），来弥补单一密码认证（用户知道的信息）的脆弱性。

但从系统架构角度来看，2FA 并非在所有阶段持续生效，它仅存在于身份鉴别（Authentication）的交汇点。一旦身份验证完成，系统的信任机制就会转化为基于会话（Session）的授权。这种机制设计，为攻击者提供了绕过认证逻辑的空间。

遗憾的是，并非所有双因素身份验证 (2FA) 都按照安全标准和最佳实践正确实施。有些实现方式可以被完全绕过，从而再次暴露出身份验证漏洞。这主要是因为企业自行部署 2FA，而另一些企业则倾向于依赖第三方服务。当进行额外修改或忽视安全最佳实践时，各种 2FA 漏洞都可能出现，使任何人能够绕过任何强制性的多因素身份验证。

![](https://mmbiz.qpic.cn/mmbiz_png/aFb4Q75OW00TY4hfnVcdkRcCPKVSEdAfXKwiaCIRMztick8iaQJ5ic5ePp3knJ2fp249qPtgYGtvbr17NXuQSTKAfw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icTPiaaqor4ibZ6bExU5nT2CNpeNibcSIJpHc63evNrLibyjq68g4ZgXlIC4FfHW5Hd5W75zwgMOyY69tJz6B0nYHKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif)

双因素身份验证漏洞

双因素身份验证 (2FA) 漏洞的出现，是因为 2FA 实现本身存在缺陷（例如令牌过于简单易预测）或开发不足（例如逻辑错误）。此外，还可以通过其他间接方式绕过 2FA（例如，利用 CSRF 或 IDOR 漏洞）。

下面，将探讨几种利用 2FA 漏洞并利用其不安全实现中任何现有逻辑缺陷的方法。

01

利用基本的双因素身份验证漏洞

**强制浏览**

某些双因素身份验证 (2FA) 实现无法将验证令牌与当前会话状态关联起来。实际上，这种情况类似于以下示例：

1. 用户登录其帐户

2. 用户的会话状态现在设置为“已验证”。

3. 然后用户将被重定向到多因素身份验证页面，在该页面上，他/她需要提供 2FA 令牌。

这种实现方式存在缺陷，因为任何攻击者都可以有效地跳过第三步，仍然能够访问账户。恶意用户只需尝试请求任何其他只有已认证用户才能访问的页面，例如个人资料页面，即可在无需提供双因素身份验证令牌的情况下获得访问权限。

**响应篡改**

部分系统在前端依赖响应中的状态字段（如"success":false）判断认证结果，若后端未校验响应完整性，攻击者可通过篡改响应字段，将"success":false改为"success":true，从而绕过验证。

**状态操纵**

若系统根据HTTP状态码（如4xx表示失败）判断认证结果，攻击者可尝试将状态码从4xx改为200 OK，使系统误判为认证成功。

**暴力破解**

缺乏速率限制，再加上令牌的可预测性和/或较短，使得任何双因素身份验证 (2FA) 实现都容易受到暴力破解攻击。一些应用程序使用 4 位字符的 2FA 令牌，没有设置速率限制，并且令牌的有效期也足够长。这些配置错误可以帮助我们使用 BurpSuite 或 ZAProxy 等自动化工具猜测出唯一的令牌，从而完全绕过 2FA！

**弱双因素认证口令**

绕过双因素身份验证的另一种简单方法是检查令牌并确认：

• 可以重复使用之前的令牌，也可以完全不提供令牌。

• 可以重复使用任何备份令牌。

• 该令牌与会话无关。

• 令牌可能出现在 HTTP 响应中的任何位置

• 用于测试和开发的任何令牌，例如“0000”或“123456”，在生产环境中仍然被接受。

**可重复使用的双因素认证令牌**

第二次登录时，请检查之前使用的令牌是否仍然有效。双因素身份验证令牌应该是临时的，并且仅在固定期限内有效。该令牌也必须在首次使用后过期。

备用双因素认证令牌也遵循同样的规则。此外，还必须测试是否存在逻辑错误，可能导致在未提供令牌的情况下跳过双因素认证验证。尝试发送不带令牌甚至不带任何参数的请求。

**双因素身份验证与会话无关**

如果双因素认证 (2FA) 未与用户会话关联，则很可能意味着它已保存在数据库中，作为已接受令牌的集合。这种方法存在缺陷，攻击者可以利用 2FA 令牌解锁其他帐户。

测试这种极端情况的最佳方法是设置两个测试账户。使用第一个账户登录并保存双因素身份验证令牌，然后使用第二个账户登录，并使用从第一个测试账户保存的双因素身份验证令牌。

**HTTP 响应中暴露了 2FA 令牌**

某些应用程序设计为服务器在触发2FA的响应中可能泄露生成的验证码，攻击者通过检查响应内容或分析JS文件，获取验证码后直接用于验证。

**测试令牌在生产环境可用**

开发人员在开发过程中通常会使用静态双因素身份验证 (2FA) 令牌，以避免每次登录时都输入唯一的 2FA 令牌。但是，如果这些令牌在生产环境中也被接受，它们可以导致攻击者完全绕过 2FA 的实现。

在测试中可以尝试使用常见的 2FA 测试令牌，例如“0000”、“1111”甚至“123456”，具体取决于应用程序接受的令牌格式和类型。

**网络钓鱼**

攻击者诱导受害者在攻击者控制的设备上发起身份验证请求，系统生成设备代码后，要求受害者在其个人设备上访问特定URL并输入代码完成授权，攻击者控制的设备即获得对受害者账户的合法访问权限。

02

利用高级双因素身份验证漏洞

**跨站请求伪造（CSRF）**

跨站请求伪造（甚至点击劫持）也可以通过构建一个能够禁用双因素身份验证的概念验证来绕过双因素身份验证机制。这种攻击方式需要最终用户的操作，因此必须确保：

1. CSRF 攻击是可能的。

2. 负责禁用双因素身份验证的端点不需要密码或任何其他唯一凭证。

当满足这些条件时，就有可能绕过双因素身份验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1Xt4M99rkew9CwmJ3iaiaI9o7UD3bjbibwcK5OWIZLpmibXTkZPiafUAPpgtyM5nCTvHbFSNaZiawdu8tibnZFK7WkCXPSuld1uDhydCc/640?wx_fmt=png&from=appmsg)

**不安全的对象引用（IDOR）**

如果负责禁用 2FA 的端点容易受到 IDOR 攻击，只要该端点不需要之前的 2FA 令牌，我们就可以有效地禁用受害者的 2FA 并完全绕过此安全实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1WIA4v9wibUxL8xuSiaiamYyqicM5YUTvV94sibI2FOfotKicca3BJcBZ6OvV7FeOSGlZdTNjAPgbcGuMiaGowaTLTzUtsQCicV4T34zibM/640?wx_fmt=png&from=appmsg)

**密码重置**

密码重置功能旨在帮助那些不小心忘记密码而无法再次访问其帐户的用户。然而，在某些情况下，当用户请求新密码时，此功能还会自动禁用该帐户的双重验证 (2FA)。即使在设置新密码之前，也可能发生这种情况。

仅仅发起新的密码重置操作就会禁用双因素身份验证，从而使攻击者能够绕过多因素身份验证。

**通过路径遍历绕过二阶双因素认证**

通过路径遍历绕过二阶双因素身份验证 (2FA) 的情况在复杂的应用程序中非常罕见，通常是由于输入验证不足造成的。该应用程序采用的验证方法存在缺陷，使得我们可以绕过账户的 2FA。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1UdHh26LXgkRoOVJC7FiaZTser4edm6EnhjCjUiaPbWcyRKLS9saoU4q9K9ibsUEhWNOvk6HyWPbNqcyaqiaaf3D8uUZ4DH6QKCZoI/640?wx_fmt=png&from=appmsg)

如上图所示，该应用程序包含两个服务：后端 API 和内部验证 API。后端 API 会转发我们的双因素身份验证令牌，而不会对输入进行任何验证。此外，该 API 仅检查内部验证 API 返回的状态码是否为 200 OK。

这样我们就可以发送带有路径遍历有效载荷的双因素身份验证，从而成功绕过多因素身份验证：

1234/../../../../

实际上，请求会是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1WFMlaWB6l2ic9XsWicyiad2oUELppiacm1HibUickKvskiax6Suf46JlBZet2jCvkP2uSzxJTUFjHOCMYwW01ibsnxTicbegZpRmF3pbcs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/zZ00aKlc6O6HTo0nVMk5qic2IZj1prQ9icMP7gmqiawKLAIyBVGricYnuXiatUCKVsvsSl9xot1YIaIicfn7ic3ib1f0ibw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/KmkB6c8YOcQSET5klCfw1hD10H2eJu8UW1jicvkVtdrL0VkFopcmRmXPvmZul9Zq0tVQHA6FHLemADOd6jYbtdw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Fh7c6Q44tXHAqALWOqMPDC6tX0gqjxicSlDGTt5vKhpeVFDHhGKVJzphl1RxfO9XJ6YqFVfrd4kjvXto6qEKhOA/640?wx_fmt=png)

结语

![](https://mmbiz.qpic.cn/mmbiz_png/5Gic6Z7hN4xgXlVWcicgWbFy5I57t92bhDFJupLY56qIia5423oVoI9llOUEFSBasr8mB3xTpDtKj06bbsbUe2tAA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/vS6eQicRY6DAILuiaPanZx5LaibWTlBwRd3w5FCFhdn0BVIgqakmJDhHSrmdIXaQUtYzGWic4Wvic95JO45tlWZibFuw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ibiam3zEgeEV5NCZHFlFGjd1Xfcq3GtWaheaQ6AiaZIXOu9grVg2JWZgON6VRKHdMw3FGzH0xCXa1w71HqPcicXURA/640?wx_fmt=png)

必须明确的是，2FA 绕过风险的出现，并不意味着该技术的失效。2FA 依然是阻断海量无差别自动化攻击（如暴力破解、撞库）最高效的手段。

但对企业开发者而言，应当放弃“2FA 验证...