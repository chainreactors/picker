---
title: Timeroasting：用NTP时间差烤出AD计算机账户的NTLM Hash
url: https://mp.weixin.qq.com/s/7eaqNjazqtoUMGtR32Fwlg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:45.169478
---

# Timeroasting：用NTP时间差烤出AD计算机账户的NTLM Hash

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNDSTb7x2QImT5yiaOl7rzIu6rdpOtBwyyrWRCtQJbRct2dUwoYcBG4rg/0?wx_fmt=jpeg)

# Timeroasting：用NTP时间差烤出AD计算机账户的NTLM Hash

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

我们将继续推出“面向黑客的 PowerShell”系列文章，今天将介绍如何在实际渗透测试和紫队演练中使用 PowerShell。我们将探讨一种名为“Timeroasting”的攻击。不过，我们不仅关注计算机，还将探讨如何利用修改后的脚本滥用用户帐户。该技术的最终结果是生成一个用户哈希值，该哈希值已预先格式化，可以直接使用 hashcat 进行破解。

在深入探讨之前，有一点需要澄清。这种攻击依赖于修改 Active Directory 中用户帐户的属性。这意味着您必须已经拥有域管理员权限。通常情况下，一旦攻击者攻破域管理员帐户，组织的安全就岌岌可危了。该帐户拥有对域的完全控制权。但即便拥有如此高的权限，有时您可能仍然需要特定域用户的凭据，并且不希望触发明显的、高风险的操作。

防御者可以监控诸如转储 NTDS、提取 LSASS 内存或执行 DCSync 等技术。在某些情况下，这些方法要么被阻止，要么被监控，要么根本不理想。我们今天讨论的脚本正是为此类情况而设计的。它能以一种更隐蔽的方式检索哈希值，使其更接近正常的域行为。

Timeroasting

您可能想知道 Timeroasting 究竟是什么。Timeroasting 是一种最初设计用于从域计算机而非用户获取哈希值的技术。它利用了某些计算机和信任帐户在 Active Directory 中存储密码方式的漏洞。这些计算机密码随后被用于计算 MS-SNTP 身份验证材料，攻击者可以收集这些材料并尝试离线破解。通常，域中的计算机帐户都使用非常长且随机生成的密码。由于这种复杂性，破解它们通常是不切实际的。然而，情况并非总是如此。一些较旧的系统，包括所谓的“Windows 2000 之前的计算机”，有时会存储弱密码或可预测的密码。正是这些遗留系统使得 Timeroasting 显得格外引人注目。

该攻击最初由Secura公司的Tom Tervoort发现并记录。他展示了如何利用Active Directory中计算机或信任帐户的弱密码。例如，如果一个计算机帐户拥有执行DCSync的足够权限，并且其密码足够弱，那么在DCSync等攻击中，甚至可以直接使用计算机名作为密码。问题在于，现代系统的计算机密码通常很长且很复杂。即使使用强大的字典文件来运行这些哈希值，也可能需要很长时间，而且最终可能仍然失败。这就是为什么最初的Timeroasting攻击的应用范围非常有限的原因。

Giulio Pierantoni解决了这一局限性，他在原有思路的基础上进行了改进。他证明域用户帐户也可以用类似的方式被滥用，这显著改变了此类攻击的价值和应用场景。

Targeted Timeroasting

Giulio Pierantoni 将这种技术称为“目标定时烘焙”（Targeted Timeroasting），其原理与目标 Kerberoasting 和 AS-REP 烘焙类似。由于域管理员可以修改用户帐户的属性，因此您可以暂时将用户帐户转换为类似于域计算机帐户的帐户，从而说服域控制器将其视为域计算机帐户并返回其哈希值。换句话说，域控制器会认为该帐户是一台计算机，因此会公开通常与计算机帐户关联的身份验证材料，只不过现在它属于人类用户。

每个 Active Directory 用户对象都有一个名为sAMAccountType的字段。该字段定义了帐户类型。通常情况下，普通用户帐户和计算机帐户具有不同的值。例如，普通用户帐户属于SAM\_NORMAL\_USER\_ACCOUNT类别，而计算机帐户属于SAM\_MACHINE\_ACCOUNT 类别。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNRduhqEiaAGJ5mgc3Af8GLDreKicDmnAt2HEZnOeuUITk4g5jmZCuiaQmg/640?wx_fmt=webp&from=appmsg)

虽然您无法直接修改此字段，但还有一个名为userAccountControl 的属性。这是一组标志，用于确定帐户的特征。其中一些标志对应于工作站、服务器或域控制器。当userAccountControl值更改为表示工作站信任帐户的标志时，sAMAccountType属性会自动更新。此时，域控制器会认为它正在处理计算机帐户。

根据正常的安全规则，您不应该能够将一种类型的帐户转换为另一种。但是，域管理员不受此限制。这正是目标定时攻击（Targeted Timeroasting）成为可能的原因。这种技术无法由非特权用户执行，因此不同于目标 Kerberoasting、AS-REP 攻击、影子凭证或 ESC14 等技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNklEf4piax2PVVu8NoEE7r9qgiciaSlDaUHQvON8pcK522IFcCRUAWjU4g/640?wx_fmt=webp&from=appmsg)

在计算哈希值之前，域控制器还会检查sAMAccountName是否以美元符号结尾。对于域管理员来说，除非已存在同名帐户，否则更改此设置非常简单。修改userAccountControl和sAMAccountName值后，域控制器即可向任何提出正确请求的用户提供该帐户的 MS-SNTP 哈希值。

Giulio Pierantoni 分享了一个重要的操作注意事项。当用户帐户转换为工作站信任帐户时，该用户将失去登录工作站的权限。但是，这不会影响现有的活动会话。如果在提取哈希值后立即还原这些属性，用户可能根本不会注意到任何变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aN4xPszlcKO1aandSCJFc3o4l7s9Vgj8b40hQXU8fSd5XKp6zYygLsVQ/640?wx_fmt=webp&from=appmsg)

开发

我们修改了 Jacopo Scannella 的原始 PowerShell Timeroasting 脚本，创建了一个粗略的概念验证脚本。该脚本现已发布在GitHub上：https://github.com/OffsecDeer/TargetedTimeroast。

要使用它，您需要是域管理员，并且运行在已加入域的系统上，该系统必须已安装 Active Directory PowerShell 模块。

该脚本按几个逻辑步骤运行。首先，它检索目标帐户的重要属性，例如objectSid和userAccountControl值。然后，它更改userAccountControl属性，使该帐户被视为工作站信任帐户。之后，它在 sAMAccountName 后附加一个美元符号，使用户看起来像一个计算机帐户。属性更新后，脚本提取 RID，向域控制器发送客户端 MS-SNTP 请求，并从响应中检索生成的哈希值。最后，它恢复所有原始值，使一切看起来都正常。

从数据包捕获中观察，整个过程看起来像是一个简单的 NTP 事务。请求中包含 RID，响应中包含根据账户的 NTP 哈希值生成的签名。盐值也取自 NTP 响应数据包。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNcF58ldrZwNGM6g8f5EibXOlfdQXYoM1ia2tulHV0X1AqFF9YTpaCQFEQ/640?wx_fmt=webp&from=appmsg)

修改后的脚本作者提供了两种使用模式。一种模式允许你单独针对特定用户进行攻击。另一种模式允许你攻击指定列表中的所有用户。

要针对特定用户，通常需要运行以下命令：

```
PS > .\TargetedTimeroast.ps1-domainControllerIP-v-victimUSERNAME
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNW7JRIBNSvGTyUuz3schaRicLIZvd8fAxKXZVc81GVdCliaI3l7kMwjxA/640?wx_fmt=webp&from=appmsg)

如果要同时定位多个用户，可以准备一个列表并运行：

```
PS > .\TargetedTimeroast.ps1-v-file .\users.txt-domainControllerIP
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNyxJSngTHw2lbzicwibugrLysRQ5blXOiavlLsENNdwT1k3LpRz7V1SZUA/640?wx_fmt=webp&from=appmsg)

Hashcat

收集到所需的哈希值后，就可以在 Kali 系统上使用 hashcat 开始破解它们。建议您移除每个哈希值的 RID，以避免破解过程中出现问题。您的命令如下所示：

```
bash$ > sudo hashcat -a 0 -m 31300 hashes.txt dictionary.txt
```

如果密码强度较弱或重复使用，您可能可以相对快速地找回密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNjb3iaiciaBD9ib3qdFUBfib9qMryVQFppLQ5Zctqd2U58g6n5WvWzEeUjqA/640?wx_fmt=webp&from=appmsg)

检测

防御者应重视本节内容。尽管此攻击需要域管理员权限，但仍应对其进行监控，因为内部威胁或管理员权限被攻破的情况确实存在。以下几种关键行为可能表明正在发生 Timeroasting 或 Targeted Timeroasting 攻击。例如，单个主机发送大量 MS-SNTP 客户端请求，但这些请求包含不同的 RID。又如，这些请求中的 RID 属于用户帐户而非普通计算机帐户。您可能还会观察到一个或多个用户帐户的userAccountControl值从普通用户值变为工作站信任帐户值，然后很快又变回普通用户值。此外，用户帐户的sAMAccountName末尾可能会短暂地添加一个美元符号。

这些行为在正常环境下并不常见。如果能对其进行妥善监控，攻击者利用此漏洞的机会将大大减少。遗憾的是，许多组织机构很少进行此类监控。

概括

这是对一种由来已久的攻击概念的创新应用。这种技术很可能被从红队成员到恶意攻击者等各类群体广泛采用。我们也应警惕内部威胁，因为域管理员无需进一步提升权限即可轻松实施此技术。如果已具备相应的访问权限，整个过程会出奇地简单。

因此，用户在企业域内应使用强密码和复杂密码，不仅要满足最低策略要求，更要超越这些要求。此外，切勿重复使用密码，甚至不要在不同系统中重复使用相同风格的密码。尽可能启用双因素身份验证。良好的架构和强大的监控机制将大大降低“目标定时攻击”等技术的吸引力，并使其更容易被检测到。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNDZIsM3icvQIibOvKOibSuCOA4NvY3vWf55odHszDue9J2RuxorXWTwVTA/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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