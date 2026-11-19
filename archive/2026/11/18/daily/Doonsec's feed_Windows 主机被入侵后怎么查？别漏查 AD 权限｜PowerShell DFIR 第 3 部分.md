---
title: Windows 主机被入侵后怎么查？别漏查 AD 权限｜PowerShell DFIR 第 3 部分
url: https://mp.weixin.qq.com/s/6KjKxVcU5mzApNxrayjHXQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:13.582674
---

# Windows 主机被入侵后怎么查？别漏查 AD 权限｜PowerShell DFIR 第 3 部分

# Windows 主机被入侵后怎么查？别漏查 AD 权限｜PowerShell DFIR 第 3 部分

aeverj
aeverj

红队工坊

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 原文标题： PowerShell for DFIR, Part 3: Audits and ACL Security

用于审计 Windows 终端和 Active Directory ACL 的脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2eAS82ic5pRqhOJ6x5jF0jbE9fqf48kiaYYD6Ay8LNdAMx58DzCsAzPanuVs9zrGuvXUXBpibjQYkuibFQrSAS4QFAngNCPR20kiakg/640?wx_fmt=jpeg&from=appmsg)

前两篇我们分别检查了 Windows 日志和主机持久化。但清理恶意文件、重置相关凭据后，攻击者就一定失去控制了吗？不一定。

在本篇实验环境中，一个看似普通、并未加入特权组的账户 lowpriv，却对 AdminSDHolder 和 Administrators 组拥有 Full Control。只检查终端日志和持久化项目，很容易漏掉留在 Active Directory 权限中的控制路径。

这篇文章从两个层面展开：先用 Windows 审计脚本检查终端安全配置，再用 ADACLScanner 检查 DACL/SACL、AdminSDHolder 和关键对象权限，最后通过可信基线比较判断哪些变化值得进一步调查。

## ■**审计**

**代码仓库：**https://github.com/mr-r3b00t/windows\\_audit

这个审计脚本由 @UK\_Daniel\_Card 发布，目标是生成 HTML 报告，帮助检查工作站安全配置。它覆盖密码安全、网络协议、补丁级别、漏洞利用防护（exploit protection）等多个维度。

需要注意：该项目 README 目前仍标注 In Dev、use at own risk、not complete or validated。它适合作为检查辅助，不应被当作经过完整验证的安全基线工具。使用前应审查脚本，并在测试环境验证结果。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2dqMnedLPRzfkUecmXuNAuE2CaViaPXpibEoW5cfDYVlXLD5E7VACPshokFjlH0wCI2cf18YzUkszSBqAk67soRiaREZx5yyGH6XA/640?wx_fmt=jpeg&from=appmsg)

这份报告最出色的地方之一，是问题结果的呈现方式。在每个类别下，问题会按照严重程度分层展示。影响大的发现会被清楚标出，而严重性较低的问题也同样会记录下来，并附上实用建议。如果某个方面没有发现问题，报告也会给出提示信息，确认这项配置是可接受的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2cRpFicebkH5Z4OSENVHSJCl6LjdH16Z0ib9eKgHQDibeibZ84eEYFScz9cuIDYZ0ngcuFiaLqGD7MCLpXQiceiaF2q8mnKz7736zpdicw/640?wx_fmt=jpeg&from=appmsg)

报告可能指出某个关键问题，例如账户密码永不过期或本地管理员账户过多。本地管理员数量没有适用于所有组织的统一阈值，应结合主机用途、运维职责和组织基线判断，不要把“三个”直接当成通用标准。报告中的其他低严重性建议，也可以作为长期改进安全基线的参考。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2dg8CkHjPFgk9qXOmyaw0Zqb5DpAP2xJll81OEniaDIribe27W0icDRPHmtltpVurib0RY8LQhszkXMxRQryG32jo1RiaIm2rOeVSf8/640?wx_fmt=jpeg&from=appmsg)

一个很好的例子是建议部署 Sysmon 来增强日志记录。Sysmon（System Monitor）是微软开发的一个 Windows 系统服务和驱动，能提供对进程创建、网络连接、文件创建以及其他底层活动的详细可见性。在安全运营中，Sysmon 常被用来丰富终端遥测（telemetry）数据，把高质量数据送入 SIEM。它不会取代杀毒软件或 EDR 方案，但如果配合适当的日志与告警规则，能显著提升检测能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2dsSIAwEB9w6clLaaEPXgYK39CfpoibP2XMjqjFyYoBwpV4DLWfpQ5OMNfZ5RmKgMXMeWXj9JHanr6aI6Azw0YQT0UPX1LET4kM/640?wx_fmt=jpeg&from=appmsg)

Windows 的默认配置并不是以最高安全性为设计目标的，它追求的是易用性与性能之间的平衡。审计脚本会列出那些一旦保持启用就会带来显著风险的可选 Windows 功能。一个常见的例子是 PowerShell 版本 2，它缺少脚本块日志记录（script block logging）这类现代安全特性。在 **PowerShell for Hackers** 系列里，我们讨论过攻击者如何有意降级到 PowerShell v2，以绕过日志记录、逃避检测。如果你的检测流程没有明确查找降级攻击，恶意活动就可能悄无声息地溜过去。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2fQT5AXcTZvoyQFYMlpcaC5SROJ1vbP14Gricv293GJ1oqDwk3kq7cjqbDhOBQfHibR872oUSsZ8XSljk0bDxr07YZqYdkVLOAb0/640?wx_fmt=jpeg&from=appmsg)

在报告的最开头，脚本会给出一个高层概览，汇总系统的整体安全健康状况。这个快速快照能帮助响应人员和管理员立刻判断自己面对的只是小的卫生问题，还是系统性的弱点。在我们的测试环境里，结果清楚地显示这台系统远远算不上完美。这种情况比大多数组织愿意承认的要普遍得多。

### **扫描**

使用审计脚本非常简单。脚本可以直接从 GitHub 下载，在本地执行。运行后，它会问你一个简单的问题：是否要在报告中混淆 MAC 地址、用户名和主机名这类敏感细节。在大多数内部环境中，并不需要做混淆。

`PS > .\audit.ps1`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2eXJhvHt0tZY1WWu4gNBM5obmEuBUjE4tVUPguiaoM53XU9MxqLjkrxI1WRgcEYmGzXMox9AiaJs7H1GbQrxwB9Xg96GjO2AqTQE/640?wx_fmt=jpeg&from=appmsg)

启动之后，脚本就会自动开始审计系统。视配置和系统性能而定，这可能需要一些时间。如果你打算用组策略（Group Policy）把这个脚本部署到整个域，建议针对自己的环境做一下调整。在精心设计的方案里，脚本会通过 GPO 执行，并把输出写到集中式文件共享位置，方便日后分析。每份报告都包含主机名，导航和关联都很简单。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2flsxlibQlDCXWibB0FWqeIv7U4FHfcZFLPuFlDKnQMk5gZClpzjUnJB9tKAyYodqoIV7ON0Z6dHqnovFQZhcDqVuOUQ8h3kZR0o/640?wx_fmt=jpeg&from=appmsg)

审计完成后，你会拿到报告的文件名，以及一份简短摘要。请花点时间仔细分析这些发现，把它们当作改进自身安全基线的路线图。

## ■**AD ACL 扫描器**

**代码仓库：https://github.com/canix1/ADACLScanner**

**项目 README 当前列出的版本为 9.6（2026-07-07），支持 GUI/CLI、DACL/SACL 报告和基线比较；实际使用前请以仓库当前 Release 和说明为准。**

终端安全问题往往看得见，而 Active Directory 中的 DACL 滥用（DACL abuse）则是另一个危险问题，很多事件响应人员完全没注意到。DACL，即自由访问控制列表（Discretionary Access Control List），定义了谁被允许或拒绝访问 Active Directory 中的某个对象，以及可以执行哪些操作。当攻击者操纵这些权限，给自己授予持久且往往隐蔽的控制权时，就构成了 DACL 滥用。

除非你密切监控高价值 AD 对象的变化，否则很难检测 DACL 滥用。可是监控一切并不现实。过多的告警会压垮 SIEM 平台、耗尽 SOC 团队的精力，反而提高了真正威胁被忽视的可能性。攻击者对此心知肚明。这也是为什么许多人选择把持久化（persistence）做在 DACL 层面。控制了权限，就控制了恢复过程。

你可能发现一台被攻陷的工作站，把它隔离，并重置所有凭据。表面上，事件似乎已经控制住了。但如果攻击者给自己授予了对关键 AD 对象的 GenericAll 权限，他们就能看起来像一个普通的域计算机账户、甚至一个已停用的用户对象，把你的补救步骤全部撤销。

### **AdminSDHolder**

我们在 Sliver 系列这类攻防文章里讲过 AdminSDHolder，但这里必须从防御视角来看它。每个 Active Directory 环境都包含 AdminSDHolder 对象。它的作用是通过强制执行一致的安全描述符（security descriptor）来保护特权账户和组。SDProp 进程会定期把这个描述符应用到受保护的对象上。

黑客喜欢 AdminSDHolder，是因为一旦获得对它的 GenericAll 权限，实际上就等于获得了对特权账户的长期控制权。滥用这类权限时常常会用到 BloodyAD 一类的工具，只要拿到足够的访问权限，修改权限就变得很容易。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2eAs9lMDy0tQONfQdB0fUagh8sic42AhZxKaTuO2MvbFicCWWcyqzxiaze53urL0qsYVnezMdoTpOicxzoQFzibqYuo0KLtIu3QrPN0/640?wx_fmt=jpeg&from=appmsg)

攻击者偏爱不依赖活跃账户的持久化方式。用户账户的密码可能被改掉，所以它们并不可靠。于是攻击者常常转而利用已停用的用户对象或域计算机对象。默认情况下，每个域用户都有 10 的机器账户配额（Machine Account Quota, MAQ），也就是说可以在 Active Directory 中创建最多 10 个计算机对象。这个特性本是为了简化合法工作站的加入流程，但它同时也打开了多条攻击路径。

把 MAQ 降为零，就能消除大量 Active Directory 攻击向量。基于资源的约束委派滥用（resource-based constrained delegation abuse）、影子凭据（shadow credentials）以及某些持久化技术，都直接依赖于能否创建计算机对象。

ADACLScanner 可以帮助识别关键权限配置，并将当前结果与事先保存的可信基线进行比较。扫描发现应结合对象用途、权限继承关系和变更记录人工验证，不要仅凭单条结果认定恶意行为。

### **扫描**

脚本同时支持 GUI 和 CLI 两种使用方式。本文重点讲 GUI。下载并执行脚本后，会弹出一个新窗口。

```
PS > Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/canix1/ADACLScanner/refs/heads/master/ADACLScan.ps1' -OutFile ADACLScan.ps1

PS > .\ADACLScan.ps1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2fT54lIpwqEHqqDo65OA7lu03MDDhWSh0qeSRSEd55TpI4GDicSPy9GeQEWprGxZFa72b8naDTQllbXooE4ianwCicWSZsCJxFHEk/640?wx_fmt=jpeg&from=appmsg)

乍一看，界面上的选项多到让人有点发怵。其实按上图选中那些选项就足以完成一次扫描了。你可能会注意到有 DACL 和 SACL 两种扫描类型。DACL 定义权限（谁能做什么），而 SACL 定义审计规则，指定哪些访问尝试应该记录到 Windows 事件日志中，无论成功还是失败。

第一步是连接到你的域。如果你以域用户身份运行脚本，就不需要额外提供凭据。用左侧的 **List Domains** 选择正确的域，这在存在多个信任关系的环境里很有用。连接之后展开节点，选中想要的对象。在 **Assessments** 选项卡中启用着色，能让报告更易读。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2fJ8X1qic0SFf0RoZfr0brCyBUsFHXHFibfIr9lHhLh5b360m9DNzLSAhPLBLJvYCcKO19VIiaDr5yiayC5icKOLmibYNRZTWolZuWa8/640?wx_fmt=jpeg&from=appmsg)

点击 **Run Scan** 开始分析。扫描完成后，结果会以 HTML 报告的形式打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2f712qMU6Sa5tKeelDnTfWewnEYFKh8C1ErH7HEiaxicczzzXNo8oCJMznssjib7HOdjIEEQs3IqgwHDZFlGUa3ibPQPYcnYHl4SLg/640?wx_fmt=jpeg&from=appmsg)

在我们的例子里，报告立刻标出了一个严重问题。往下滚动可以看到，用户 lowpriv 对 AdminSDHolder 拥有完全控制权（Full Control）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2c33TpCJpTibDKzRA7c7ksO1GUY73LVZxqB9GNhJRnwCahicYkTwp0ZZbnJ4tfdaBthBPFiaLA1NRuZMTPIj2CUKLaVTaPj7iaShUk/640?wx_fmt=jpeg&from=appmsg)

同一个用户还对 Administrators 组拥有完全控制权。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2f0Ha7kicrjEpapOGvbGzpJAVj6xdtoKxLAJZic9RQKeqO4KpuSzCRFxY8lcsgvcKtYrpXQEYXkmWicng57x2a7FsD8ibM6w56k4SQ/640?wx_fmt=jpeg&from=appmsg)

这个账户在人工检查时看上去完全无害。它不是任何特权组的成员，却控制着所有特权组。这就是监控 DACL 的重要性所在。

## ■**对比**

一旦你建立了可信的 DACL 或 SACL 基线，就可以定期把 Active Directory 的当前状态与基线做比对。这样能及早发现变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iauzMfibvvF2cLpYHS1gibCbCLTLwGk4qQ8br0icCDtEjLfA3HrMGU7pvbGxOZOmWl15dHyrGayQ1zQ9jjDaH9hctXuIxGuRVmlq9JzSFvvklkM/640?wx_fmt=jpeg&from=appmsg)

建立基线时，应固定扫描范围和对象类型；后续对比尽量保持相同条件，避免把正常变化误判为异常。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iauzMfibvvF2dXCHoA9QNf9giaFxib44VJpNWKWKqzCdoIKJjw3Pf9vlxb4BPm0OvZ2BicX9fYBduYJC54uvZYEibrWN46wt8bs8WubwW3NibRN7Zk/640?wx_fmt=jpeg&from=appmsg)

## ■**总结**

安全审计和 ACL 扫描是成熟安全体系的基础环节。终端配置错误与隐蔽的权限滥用常常同时存在、彼此强化，而且很容易被忽略。通过定期审计系统、建立可信基线，并理解攻击者如何在凭据之外维持持久化，防御方就能从被动清理转向主动控制。

**本篇的重点不是单次扫描，而是建立可比较的安全基线：终端审计检查主机配置，AD ACL 检查关键对象的授权变化。发现异常后，还要结合对象用途、权限继承和变更记录进行验证。**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/9QEM1M4pZoC0qMZDT2PRWE5SEXdYUQ7GEPWyjhlUAvH1dO0kGOAxn8eJgG3m5dn4xpXtCFXNETtrs55B2eNbgA/640?from=appmsg)****你在事件响应中会优先检查哪些 AD 对象？欢迎留言交流。**
> **免责声明：** 本文仅供安全技术研究与学习交流之用。 严禁将本文所提及的技术用于任何非法用途，包括但不限于未经授权的渗透测试、网络攻击、恶意代码传播等。

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9QEM1M4pZoC2fAL6iaEWeibYnmGtM1yg4JiaDP1QBBYbMtpGpnrJGhYsiaS38X3DCznMpyKv8ujQXc1WwISaVjqUEw/0?wx_fmt=png)

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

...