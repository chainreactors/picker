---
title: hvv 2026 - 不用 Cobalt Strike，照样控全域：攻击者如何把 GPO 变成天然 C2
url: https://mp.weixin.qq.com/s/bPsRkox07Q0vbzjq4_TB8Q
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:46:10.006892
---

# hvv 2026 - 不用 Cobalt Strike，照样控全域：攻击者如何把 GPO 变成天然 C2

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMDw8xvQgJWOKyhS4O3lfARvKIPueia3GGqoTqiavlhSVUrCwS5kq1BhHhiaOxoLohI65z6w6g5tZatnrfCYI5b3jGZD0yDqen1BGI/0?wx_fmt=jpeg)

# hvv 2026 - 不用 Cobalt Strike，照样控全域：攻击者如何把 GPO 变成天然 C2

原创

MessFeel
MessFeel

MessFreeSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

护网里碰到一种情况：你手上有个账号，能改某个 GPO，但别的啥也干不了。没 DCSync，没 ADCS，没 Kerberoast 目标，域控也登不上去。

很多人这时候就开始翻 ADCS 的 ESC 系列或者找委派配置去了。

但如果这个 GPO 刚好链到了域管跳板机、服务器 OU，或者运维日常登录的那几台终端——事情就变了。

域内主机本来就会定期去 AD 查自己该跑什么策略，然后从 SYSVOL 拉配置。计划任务、本地组、注册表、脚本、文件分发、防火墙规则，这些都是管理员批量运维的常规操作。但当策略写权限落到攻击者手里，这整套机制就变成了：域帮你识别目标、帮你分发任务、帮你触发执行。

不用连陌生域名，不用维持 Beacon 心跳，甚至不用直接访问目标主机。

**攻击者不一定要把 C2 带进域里。很多时候，域自己已经铺好了投递路线。**

---

DEF CON 33 上有个 59 页的议题，《Turning your Active Directory into the attacker's C2》。Synacktiv 的 Quentin Roland 和 Wilfried Bécard 没放什么"普通账号秒变域管"的 0day，而是把一个长期被低估的管理面拆成了四块：

* 从现有 GPO 里低噪声画横向路径；
* 利用错误委派的 GPO 写权限往目标下发动作；
* 通过 NTLM Relay 只改 LDAP 指针，让客户端去别处读策略文件；
* 利用 OU 的 gPLink 写权限，把额外策略挂到受保护对象的范围里。

![DEF CON 33 原版议题页](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMD6Zul0Xyz9R2GxAnBB5zm83pUTEBU5AZqW33qX1AcTAfeMLBC9bBSHYWZymFbJPNWXnYFzaVDDqhTXMZkWjEU1VTfBkAEZN9c/640?wx_fmt=png&from=appmsg)

先说清楚标题里的"天然 C2"是什么意思。GPO 自带身份认证、目标分组、周期触发和配置下发，但它不是 Cobalt Strike——没有实时回传、没有会话管理、没有 Beacon 那些交互能力。这是个比喻。

"控全域"也一样，不是无条件的。你得先有初始落点，还得有相关 GPO、GPC 或 gPLink 的有效写权限。最终能影响多少机器，取决于链接、继承、筛选、刷新周期和执行上下文。

但这份报告真正让我觉得值得写的地方是这层意思：

**GPO 不是帮你从零变出权限的漏洞。它干的事情更微妙——把一个你还没当回事的委派错误，放大成域原生的批量投送能力。**

![被低估的 GPO 攻击面](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMB2lNViaibEcxUH5Znav9cnLtH6KgzkS3YzbzQL7tKgKlEUCPUZtcibQt0z3rP2gicbAGF1Tm7tb1Eibz4Noql0oWlvv51RftHibA75Y/640?wx_fmt=png&from=appmsg)

---

## GPO 不是你想象中那个勾选框——它是一条会自己跑的管理链

大多数人对 GPO 的印象就是 gpmc.msc 里勾几个选项，策略就自动生效了。

但底层是两套东西。

**Group Policy Container（GPC）** 是 AD 域分区里的 LDAP 对象，存的是策略名称、版本、启停状态、CSE 类型、权限，以及策略文件该去哪里读。位置在 `CN=Policies,CN=System` 下面，每条策略一个 GUID。

**Group Policy Template（GPT）** 是 SYSVOL 里真正存配置文件的目录。计划任务写在 `ScheduledTasks.xml`，组成员在 `Groups.xml`，注册表在 `Registry.xml`，安全选项在 `GptTmpl.inf`，脚本就是脚本文件。客户端通过 SMB 来读。

![GPC 与 GPT 双组件架构](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMCBCIA1OLT1WPymBUNPRcdTTgiaGTDV0QRSTr6tuh1ibuMia8BXBicEF2uEMwaMO5fCDVL2CRVoZT1QgYbCVPqPQQsy2czeX89MoAE/640?wx_fmt=png&from=appmsg)

这意味着一次 GPO 修改要跨两套复制和审计体系——GPC 走 AD 复制，GPT 走 SYSVOL 的 DFSR。两边不是原子提交，短暂的版本差异可能是正常复制延迟。但如果 SOC 只看 LDAP，或者只在 SYSVOL 上做文件监控，你看到的永远是半条链。

GPO 也不是直接绑到某台机器上的。它被链到 Site、Domain 或 OU，再叠加继承、强制、安全筛选、WMI 筛选、用户配置和计算机配置的启用状态，算出最终作用范围。

客户端正常的处理流程大概是这样：

1. LDAP 查自己这个范围关联了哪些 GPO；
2. 读 GPC，确认状态、版本和 GPT 路径；
3. SMB 拉 GPT 里的配置文件；
4. 丢给对应的 CSE（Group Policy Client-Side Extension）执行。

![GPO 正常应用流程](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMBwiaUia47y4KTyLBBVtialUZesW3iciasvELECvTpLTOPh2s0YSCtHTib04HwCE8VhregfERhma2H0pKQsO4VcsCyRgzbOpJjNt3Vwk/640?wx_fmt=png&from=appmsg)

而且这不是一次性的。普通客户端和服务器默认每 90 分钟查一次策略变化，加 0-30 分钟随机偏移；域控的计算机策略大约每 5 分钟查一次。启动、登录也会触发前台处理，有些扩展（比如软件安装）只在特定阶段跑。

![GPO 默认刷新周期](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMBkCfn3foQytJXdx6ZuqoXlzjp7z62baTlXT24az99hwAm9WbUXUgb6AOiczib2sOHKbv7J61yGrjv18I1wRlfrKEOb2cjLpqzYc/640?wx_fmt=png&from=appmsg)

运维视角看这是稳定、可扩展的配置管理。攻击视角看，它已经有了几项跟 C2 很像的东西：

* AD 和 OU 结构 = 目标选择；
* LDAP + SYSVOL = 任务传递；
* 客户端 CSE = 本地执行；
* 周期刷新 = 重复触发 + 扩大覆盖。

真正要命的地方不在于 GPO 里能不能塞一条命令。而在于域内每台客户端生来就被设计成信任这条管理链。

---

## 你还没开始动手，GPO 先帮你画好了横向地图

报告的第一部分不是利用，是枚举。

这一步经常被跳过，因为普通域用户本来就能读 GPO——客户端正常工作就需要读策略，蓝队也不会把一次 SYSVOL 读取当入侵。

但 GPT 里的东西远不止"密码长度必须大于多少"。

你能从中看到：

* 哪些域组被加进了哪些终端的本地 Administrators、Remote Desktop Users、Remote Management Users；
* 哪些主机开了 RDP、WinRM 或特定防火墙规则；
* 哪些账号拿到了高风险本地权限；
* LLMNR、NBNS、mDNS、LDAP 签名、SMB 签名有没有开；
* RunAsPPL、Credential Guard 之类加固有没有部署；
* 有没有装额外安全软件或运维组件；
* 哪些计划任务、登录脚本和注册表项会周期性跑。

说白了，GPO 不只是配置仓库，也是组织写给所有域成员的"安全架构说明书"。

![从 GPO 读取 RDP 关系](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDDHRMNU82HoOj3zYt1uyIXpWibDLAAQLhOOqqlK3pom0ncJZDWdboCDWXPv9LxSghej57E0s97z5reSfG9cBzvKO5EKiaCfLnoE/640?wx_fmt=png&from=appmsg)

传统横向侦察的逻辑是扫网段、探 445 和 3389、试远程服务，然后从响应里拼资产关系。GPO 枚举反过来：先读组织已经写好的策略，再只碰真正值得碰的目标。噪声小得多，而且能发现图数据库未必自动表达的路径。

报告第 33 页有个例子：策略已经允许 Domain Users 通过 RDP 进 WKS01，但默认 BloodHound 关系图没把这条 CanRDP 路径呈现出来。

![BloodHound 中缺失的策略关系](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDzCRfHjvhBBg3WwlS2iaibOEicKZ8IKGOJbtnJSjwZ63FzwUYsdWKbKDQAiczCJ7t3Hn8SDMvXWEzO2Jwt8YpdOAEQuT79lO4Xcw0/640?wx_fmt=png&from=appmsg)

研究者为此发了 gpoParser：同时读 LDAP 和 SYSVOL，算链接、继承、启停状态和策略内容，把 AdminTo、CanRDP、CanPSRemote 这些关系补进 BloodHound。

![gpoParser 的分析能力](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCmfClJcZiaALUoYTt3k4oibAW9PcmuwlJotyiblubVXFjWNGMEv5KseTGA1KC5vTRUNDLGjhYnMP01AfqMiaRupcR2zUZzclPtLMU/640?wx_fmt=png&from=appmsg)

蓝队要做的事不是封 gpoParser——普通客户端本来就要读大量策略，工具特征不是可靠边界。更应该反过来用同样的解析思路：定期把 GPO 内容转成权限和横向关系，看组织是不是无意中给过大的群体开了 RDP、WinRM、本地管理员或敏感用户权限。

如果红队能从 GPO 里读出真实横向路径，蓝队就不能还只把 GPO 当个合规配置项。

---

## 第一条利用链：改一个关键 GPO，让受管主机替你干活

到这里才进入最直观的部分。

前提：你已经控制了一个对目标 GPO 有有效写权限的身份。权限可能来自分层运维账号、历史委派、嵌套组，或者某次临时授权事后没回收。普通域用户一般改不了 GPO，所以这不是"随便一个账号都能打"的无权限攻击。

但现实是，很多组织只把 Domain Admin、DCSync、ADCS 管理员当高风险权限。"能改一个关键 GPO"根本没被放到同一档。

![GPO 写权限的影响范围](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMA6EsVefFjK2gFcDWcLcgibHUVWn859SNPCKftv0Raw9vdQCvKnlA6O0G7eicBpiaK7HKlR4ZTFibooL1pA9cUu6wFV9Jms3iaABYTI/640?wx_fmt=png&from=appmsg)

GPO 不用额外装 Agent，直接用 Windows 自带能力就能下发：

* 计划任务或立即任务；
* 本地组成员修改；
* 文件分发并触发执行；
* 注册表和安全选项；
* 登录/注销/启动/关机脚本；
* 开 WinRM、改防火墙、调系统服务。

![GPO 可调用的域原生动作](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMBwQ1hYrCFV6pXTziaNicYKxX4K7yN4XmcPnHMicCSzgvcKc0gEEILE9AbtiawClkOcC5PVhVBCW4z6icHPZk8BIGpia8GwnLNibbu2ao/640?wx_fmt=png&from=appmsg)

报告的核心案例是一台域管跳板机。攻击者不能直接连这台跳板机，但控制了能改它关联 GPO 的账号。利用链就变成：

1. 找到覆盖跳板机的可写 GPO；
2. 往策略里塞一条定向任务；
3. 等跳板机刷新策略，或等目标用户进入对应执行阶段；
4. 动作在高权限上下文里发生；
5. 借这次执行扩大域内权限。

![域管跳板机利用场景](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMAzg8USIWIa38AqHGr88LNqDIic5HWomq2zJn83aFTUpO42EmqaUmvIaicJfjCarseBl1oKSa1pD6vwhlu8XF3NSYB7d8mpy724s/640?wx_fmt=png&from=appmsg)

有个细节很容易搞混：GPO 写权限本身不等于域管权限。它给的是一个执行和配置的窗口。只有当策略范围覆盖了域控、管理员跳板机或其他高价值对象，而且具体 CSE、任务上下文、触发条件都配合的时候，影响才可能放大到域接管。

但这也恰恰说明为什么光看权限名容易低估风险——攻击者不需要从自己的落点访问隔离区，只要目标还能访问域服务、正常刷新策略，管理链就可能替他跨过网络隔离。

报告里还提了几种实际场景：

* 往网络隔离的工作站投文件；
* 通过策略开 WinRM 并加防火墙例外；
* 被发现后用不太显眼的策略项维持权限；
* 用 Item-Level Targeting 只命中少数指定客户端，控制异常面。

![GPO 的更多横向与持久化场景](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMD7SK0MszNEyB8f44L3T4O9yp7b2a4twVONZEhsyEVstzJeTDicAjQfibsAudumphLofiaJDqq2B9EYHbIFNEF4QsLaNJy73oMia7s/640?wx_fmt=png&from=appmsg)

研究团队发的 GroupPolicyBackdoor 还支持备份、创建、链接、细粒度定向、清理和回滚。对防守方来说最棘手的不是工具名，而是"回滚"这个动作——攻击者可以短时间改 GPO，等目标应用完，再恢复策略对象。管理面的异常消失了，但客户端上已经落地的计划任务、本地组、文件、注册表和凭据影响不一定一起消失。

**恢复 GPO ≠ 恢复受影响的终端。**

---

## 第二条利用链：碰不到 SYSVOL，只改 LDAP 照样劫持策略

传统 GPO 利用一般要求同时能改 LDAP 里的 GPC 和 SYSVOL 里的 GPT。

报告里提了一个更刁钻的场景。

环境允许把 NTLM 认证中继到 LDAP，你截获到的身份刚好对目标 GPC 有写权限，但这个身份没有 SYSVOL 的写权限。也就是说能改策略的"身份证"，但碰不到策略正文。

![NTLM Relay 利用链的前置条件](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCO7P1D95btfA49iaHnLYsIzf8ib3XmrpPpPOkjkg9jXMl9NGB4oRP97nhBaz5uh9rZZz89JJUrat9oaq4XSl6NWkwQyr2ZRSj2M/640?wx_fmt=png&from=appmsg)

关键在 GPC 的一个属性：`gPCFileSysPath`。它告诉客户端，当前 GPO 的 GPT 该从哪个 UNC 路径读。正常情况指向域的 SYSVOL 命名空间，客户端自己定位域控，不是永远固定到某台 PDC。

Synacktiv 的研究发现，只要能改这个属性，就能把 GPT 位置换成攻击者控制的 SMB 共享。客户端还是正常查 AD，只是 AD 返回的"取件地址"变了。

![gPCFileSysPath 决定 GPT 地址](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMAwto53o9SHib1uiaqaQkey1ztD4g91Zjib16PXzHwzVzQCnH5XCffXO25upiaVanUOYdbPbiaVGv3yqtpCtTPKkYLBPl1mVYhx2aEI/640?wx_fmt=png&from=appmsg)

GPOddity 把这条链自动化了，整体逻辑：

1. 诱发或截获一个有目标 GPC 写权限身份的 NTLM 认证；
2. 把认证中继到接受该方式的 LDAP 服务；
3. 改目标 GPC 的 gPCFileSysPath；
4. 受影响客户端转向受控 SMB 位置读另一套 GPT；
5. 客户端把这套配置当作正常域策略处理。

![GPOddity 攻击链](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMANgzG2E50VUcNiaTIxUk870Ns9JaILtfEacuLuribCYicAyBLhpqmHsMobnqKQG1vfCkUbtPyO2SH4dacwWQ66DyJt7C8me1MYa4/640?wx_fmt=png&from=appmsg)

条件当然不能少：

* 被中继身份本来就得有目标 GPC 的写权限；
* 域控 LDAP/LDAPS 得接受相应中继认证；
* 目标 GPO 得真实作用于有价值的客户端；
* 客户端得能访问新的 SMB 位置并成功读策略；
* 安全筛选、WMI 筛选、策略状态和网络规则不能阻断后续处理。

这不是匿名远程接管域，也不是新 CVE。更准确的说法是：一个合法的策略路径属性 + 过宽的 GPO 委派 + 可中继的 NTLM + 客户端对域策略的信任，拼出了一条新路线。

蓝队有两个很强的检测点。第一，`gPCFileSysPath` 几乎不应该突然指向 IP 字面量、陌生域、非标准共享或跟 GPO GUID 对不上的目录。第二，策略路径改完以后，域...