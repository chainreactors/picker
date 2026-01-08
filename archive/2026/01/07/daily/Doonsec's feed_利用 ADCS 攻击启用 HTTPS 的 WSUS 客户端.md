---
title: 利用 ADCS 攻击启用 HTTPS 的 WSUS 客户端
url: https://mp.weixin.qq.com/s/BRGKqIW9APv9GuB_Iro2AA
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:28:32.919535
---

# 利用 ADCS 攻击启用 HTTPS 的 WSUS 客户端

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqibGjzsS2lEQKL0RvOTZolHUUpIev67ROW5kxxgSTaR4ibB1Q9mD0yQ7Q/0?wx_fmt=jpeg)

# 利用 ADCS 攻击启用 HTTPS 的 WSUS 客户端

Alexander Neff

securitainment

![]()

在小说阅读器中沉浸阅读

Active Directory 证书服务 (ADCS) 领域在过去几年一直是极具价值的研究目标。审计证书模板已成为企业防范 ESC1 接管等攻击的必要措施（详见下文）。虽然 ADCS 自身配置中的漏洞已被广泛研究，但将其他服务与 ADCS 结合使用仍可能产生新的攻击路径。几个月前，TrustedSec 的 Austin Coontz 揭示了如何利用特制证书配合对 Windows Server Update Service (WSUS) 的攻击，为 NTLM 中继攻击创造了有趣的机会。他的研究也是首次将原本被认为安全的 HTTPS 版本 WSUS 通信作为攻击目标。

这引起了我们的兴趣，不仅因为作者之一正是 Austin 在文章中提到的 "wsuks" 工具的维护者。我们以他的研究发现为起点，将其扩展到原始的 WSUS 攻击——该攻击能够在任何可拦截流量的启用 WSUS 的 Windows 机器上获得本地命令执行权限。在内部讨论中，我们意识到根本问题并非 WSUS 所特有，而是源于 ADCS 以及 Active Directory 中的信任关系。因此，我们建议引入一个新的 ESC 编号，以便轻松识别和缓解证书模板的这种特定配置。

## 重新审视 ESC1 模板

让我们快速回顾一下 ADCS，特别是通常被称为 "ESC1" 的攻击。关于该主题的初始研究由 SpecterOps 在 2021 年提出。他们超过 100 页的白皮书 "Certified Pre-Owned" 中最著名的部分是八种提权技术 ESC1 至 ESC8。需要注意的是，ADCS 攻击上下文中的 "escalation" 一词指的是 SpecterOps 所说的 "域提权"，即在 Windows Active Directory 域环境中提升权限。这项研究已被众多研究者扩展，诞生了两个主要的枚举和利用工具：certify 和 certipy，分别用于 Windows 和 Linux。

毫无疑问，ESC1 是最强大的提权方法之一，因其攻击链短小精悍，往往能够导致完全的域沦陷。如果你还不熟悉 ESC1 攻击的利用方式，强烈建议学习相关内容。SpecterOps 和 certipy 都提供了优秀的详细资料。

使证书模板易受 ESC1 攻击的关键错误配置包括：

* 设置了 "Enrollee Supplies Subject" 标志
* 配置了允许域身份验证的 "Extended Key Usage" (EKU)
* 授予了宽松的注册权限，例如允许 "Domain Users" 注册此模板
* 未设置有效的安全门控来阻止请求，例如未设置 "CA certificate manager approval" 选项

反过来说，缓解这些要求中的任何一项都能阻止攻击，至少在理论上如此。这意味着理论上只需启用以下配置之一就能使模板变得 "安全"：

* 禁用 SAN
* 移除危险的 EKU 值
* 将注册权限限制为特权实体
* 启用 "Manager Approval requirement" 或使用注册代理（参见 ESC3）

根据我们的经验，易受 ESC1 攻击的证书模板通常用于为 Web 服务器颁发证书，这解释了为何需要指定自定义 SAN（注册者不会为自己请求证书，而是为 "webserver.ad.example.com" 请求）。因此，将 EKU 限制为看似无害的 "Server Authentication" 可能特别诱人，因为这种改动对业务的影响最小（毕竟，Web 服务器无需使用此证书向 AD 进行身份验证，因此一开始就可能不需要任何其他 EKU）。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeq6jCxb1HO3LMcTfFVl2dNKj3JgHvicKo7icrKP9iaktal2ibwAoBGyRzO2Q/640?wx_fmt=png&from=appmsg)

然而，*鼓点响起*，仅将 EKU 值更改为 "Server Authentication" 的前 ESC1 模板仍可能对环境构成安全风险，正如 Austin 通过滥用此配置来拦截启用 HTTPS 的 WSUS 流量所展示的那样。

下文将演示如何利用此配置在启用 WSUS 的 Windows 机器上获得本地管理权限。

## WSUS

### WSUS 攻击简史

针对 WSUS 的攻击绝非新鲜事物。2015 年，Context Information Security 的 Paul Stone 和 Alex Chapman 发表了出色的研究成果（Black Hat 演讲、白皮书），导致了 WSUSpect Proxy 的发布，并为后续所有 WSUS 攻击奠定了大部分基础。他们发现可以拦截 WSUS 服务器与其客户端之间的通信并向其中注入恶意更新。值得注意的是，有效更新必须由 Microsoft 签名，Stone 和 Chapman 通过使用 SysInternals 工具套件中的 PsExec 实现了这一点。随着时间推移，多人改进了工具，但大多仍坚持最初的攻击思路。2017 年，Marcio Almeida 发布了 WSUXploit，展示了完全武器化的版本。2020 年 9 月，GoSecure 开始关注该主题并启动了一系列博客文章。第一篇伴随着 PyWSUS 的发布，这是 WSUS 服务器组件的恶意 Python 实现。为了让渗透测试人员的工作更轻松，作者 Alex Neff 在今年早些时候发布了 wsuks。

> 为了完整性，还应注意其他研究者从完全不同的角度处理 WSUS 生态系统。特别是对于红队而言，利用受损的 WSUS 服务器向 WSUS 客户端传递恶意更新是一种有趣的方法。我们找到的关于该主题的首个研究是法国公司 Alsid 和法国当局 ANSSI 的联合成果，于 2017 年 6 月发布了 WSUSpendu（演示文稿、（已删除）Github 存储库）。据我们所知，该技术已被改编两次，分别在 2018 年 10 月发布了 Thunder\_Woosus，以及在 2022 年 5 月发布了 SharpWSUS。

GoSecure 的研究在第一篇之后不久继续推出了第二部分，该部分基于 Windows 客户端中的一个漏洞（CVE-2020-1013，现已修复），并由其软件 WSuspicious 实现。通过配置自定义代理服务器，用户可以欺骗系统使用本地 PyWSUS 实例，从而导致本地权限提升。直到最近，这是唯一能够针对启用 HTTPS 的 WSUS 安装实施的攻击。

2021 年 11 月，GoSecure 发布了系列第三部分，讨论了利用 WSUS 客户端（针对仅 HTTP 的 WSUS 实例）发出的身份验证请求进行 NTLM 中继攻击的可能性。这正是 Austin 在其文章中扩展的攻击。

此外，几周前在 WSUS 服务器组件中发现了远程代码执行漏洞（CVE-2025-59287）。尽管此类漏洞与上述攻击无关，但目前撰写 WSUS 博客文章时不提及它几乎是不可能的。

> **总结：WSUS 目前是热门话题。**

### 缓解措施

从 WSUS 攻击出现之初，所有人推荐的最重要（说实话，也是唯一的）缓解技术就是开始通过 HTTPS 使用 WSUS。例如，2015 年的 Context 白皮书指出："任何使用非 HTTPS URL 从 WSUS 服务器获取更新的 Windows 计算机都容易受到注入攻击 …"。关于 CVE-2020-1013 的 GoSecure 研究已经暗示这可能并非万无一失的解决方案，但它要求攻击者能够访问受害者客户端并能够注入自定义证书。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqaSBia3kUKfstvTs4M1qRNa0Kgejgp4w4b2BgKvElnXDqAypJYMO3aAA/640?wx_fmt=png&from=appmsg)

### 将 WSUS 攻击扩展到 HTTPS

如引言中所述，几周前 Austin Coontz 重新审视了中继攻击并将其扩展到 WSUS over HTTPS。当我们阅读他的文章时，尤其震惊的是 Austin 不动声色地展示了一项新技术：他演示了如何利用 ADCS 获取 WSUS 客户端信任的证书。

本质上，我们需要一个为 WSUS 服务器主机名颁发的证书，使客户端在建立 TLS 会话时信任该证书。幸运的是，在配置了 ADCS 的 Active Directory 环境中，加入域的 Windows 客户端会信任内部 CA 颁发的所有证书。允许用户提供 SAN 并包含 "Server Authentication" EKU 的证书模板完全符合我们的需求。总体而言，这与 ESC1 的要求极其相似（见上文），只是 EKU 要求不同。

虽然 Austin 使用证书将 NTLM 中继攻击路径扩展到启用 HTTPS 的 WSUS，但它当然也适用于原始攻击路径，允许将恶意更新注入到加密的 WSUS 流量中。

尽管 Austin 更偏好中继方法，但我们个人更倾向于在受害者上执行代码 ;)。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqhWOMgaLly4PEz1y1dsyojNLkeKL6wtRTvMyTxoL3vJa4M5XYH87OEA/640?wx_fmt=png&from=appmsg)

如果你已经了解 ADCS 和明文 WSUS 攻击，那么攻击过程非常直接，如下所示：

#### 步骤 1：识别 WSUS 服务器

作为渗透测试人员，你通常一开始并不知道目标基础设施中是否配置了 WSUS。Austin 在描述如何找到它方面做得很出色。这里提供使用 `wsuks`的替代方法：

* 使用 `--only-discover`标志运行 wsuks，以便在域控制器中搜索引用 WSUS 服务器的一个或多个 GPO：

```
wsuks -u <any_domain_user> -p <password> -d <domain.tld> --dc-ip <ip> --only-discover
```

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqTXialib0SyIZ88qZN7ZkLTxTeeOOib5VOQ4ZepTYeSKmRto6mkj9S8oicw/640?wx_fmt=png&from=appmsg)

如果没有结果，WSUS 仍可能已被配置，因为并非严格要求使用 GPO 激活它。花时间进一步分析你的目标。尝试找出它使用哪个 WSUS 服务器（如果网络上有多个不同服务器可用），或者它是否配置为完全不使用 WSUS 服务器。

* 如果你对系统具有低权限访问，则无法通过网络轻松检查这一点。如果你拥有 RDP 或物理访问权限，可以检查 `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`下的注册表值，特别是 `AU`子键下的 `UseWUServer`。只有当此键设置为 `1`时，Windows 才会使用 WSUS 服务器。
* 如果你根本没有访问权限，也可以尝试执行以下步骤看看是否会发生什么，或者使用 Austin 的 `wsusniff.py`。

#### 步骤 2：识别合适的证书模板

与这篇博客文章一起，我们针对 `certipy`软件创建了一个 pull request，以直接将这些模板识别为 "ESC17"（见下文，了解我们为何认为这是合理的）。

使用此 pull request，你可以简单地运行：

```
certipy find -dc-ip <ip> -u <any_domain_user> -p <password> -stdout -vuln
```

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqU5mOIpEZKP5KAKfbX5Xia4WYHxibS0SjjmlXiaoaFMKkUeKueyLiaMbSpw/640?wx_fmt=png&from=appmsg)

或者，参见 Austin 的博客文章，了解使用 `jq`解析上游 `certipy`输出以实现类似结果的方法。

#### 步骤 3：请求并转换证书

一旦识别出合适的模板，就可以使用标准 `certipy`功能请求它：

```
certipy req -dc-ip <ip> -u <user_with_enrollment_perms> -p <password> -template <template-name> -target <fqdn_of_ca> -ca <ca_name> -dns <fqdn_of_wsus>
```

> 注意 `-dns`标志：这是确保证书对 WSUS 服务器的 DNS 名称有效的方法

要与 `wsuks`一起使用，需要将证书转换为 PEM 格式：

```
openssl pkcs12 -in <wsus_hostname>.pfx -out <wsus_hostname>.pem -nodes --passin pass:
```

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeq6MDVED3iaU49KXwKctKotDTbeNrw5CrctMjQwOUXWTjt0UHiaNpNqAzQ/640?wx_fmt=png&from=appmsg)

#### 步骤 4：拦截受害者客户端和 WSUS 服务器之间的 WSUS 流量

你需要达到能够查看和拦截客户端指向 WSUS 服务器的请求的状态。我们可以想到许多可能的场景：

* ARP 欺骗
* 发送虚假的 IPv6 路由器通告（最常见的是使用软件 mitm6）
* 各种 DNS 中毒攻击（你希望欺骗客户端，使其认为 WSUS 主机名属于你的 IP 地址）。理论上，你可能处于控制整个内部 DNS 服务器的情况。
* 你可以访问网络流量的任何其他场景（控制网络交换机/防火墙/路由器，控制客户端或服务器所在虚拟机的虚拟机管理程序，...）。

遵循 WSUS 攻击的历史，`wsuks`工具专注于 ARP 欺骗变体。

**免责声明：**针对生产环境的中间人 (MitM) 攻击本质上具有风险，因为它们会重定向流量并可能破坏现实世界的东西。只有在你确定不会破坏任何东西的情况下才执行此操作。我们认为作为渗透测试人员你应该知道这一点，但在撰写有关此类主题的博客时有义务告知你。注意：wsuks 应该自行安全地处理所有事情。

从版本 1.1.0 开始，`wsuks`允许通过命令标志指定 TLS 证书（PEM 格式）。在这种情况下，内部 WSUS 服务器（主要基于 GoSecure 的 PyWSUS 实现）被包装在 TLS 通道中并在端口 8531 上启动。使用以下命令启动 `wsuks`：

```
sudo wsuks -t <victim_ip> --WSUS-Server <dns_name_of_wsus> --tls-cert <wsus_hostname>.pem
```

`wsuks`将启动并：

* 自动启动 ARP 欺骗以拦截受害者的流量
* 等待受害者的 WSUS 连接（由于 Windows 更新的轮询时间，这可能需要长达一天！）
* 传递一个 PsExec64.exe 载荷，该载荷执行 Powershell 脚本，该脚本将：
* 创建新的本地管理员帐户（默认行为）
* 或将域用户添加到本地管理员组（如果在命令行中指定）

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqJY2iaAK2iao35HpyGeEER0ws8ajUpGPe91neEHu3fAVbeGBiau2GFy2AQ/640?wx_fmt=png&from=appmsg)

有关更多详细信息，请参阅 `wsuks`的 README。

#### 步骤 5：获利

在 `wsuks`在命令行上显示对 PsExec64.exe 的 GET 请求后，你可以使用 `Ctrl+C`终止它。它将恢复 ARP 欺骗，你现在应该对受害者拥有管理访问权限。这可以以任何你喜欢的方式使用，例如：

```
nxc smb <victim_ip> -u <user_created_by_wsuks> -p <password_created_by_wsuks> --local-auth
```

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCMZatCS54UdELZRrCOszpeqbrFiaOUuFSttfVC4iau9kSuBStosxhFWHupOUqDVsO9MBdM1e08XiazEw/640?wx_fmt=png&from=appmsg)

仅这一点就是 WSUS 攻击的出色扩展，因为使用 ADCS 证书进行虚假服务器的想法绕过了自 2015 年首次发现攻击以来一直被宣传的唯一核心缓解方法：**"为 WSUS 服务器启用 HTTPS"。**

## 第 17 集——一种新的 ESC 方法

在讨论 Austin 的博客文章时，我们意识到该问题不仅限于 WSUS，而是适用于所有依赖可信证书但不强制执行更严格保护（如证书固定）的安全通道。获得具有 Server Authentication EKU 的证书允许窃听使用客户端常规证书存储的任何 TLS 加密通信，*而不会*触发证书警告。首先，这允许被动读取可能包含敏感信息的传输数据（例如，通过 LDAPS 传输的 LAPS 密码）。其次，这也允许操纵传输或将其重定向到其他目标，正如 Austin 在他关于 NTLM 中继攻击的研究中所做的那样。此外，想想所有支持 NTLM 身份验证的内部 Web 界面（我是不是听到基于 Sharepoint 的 ...