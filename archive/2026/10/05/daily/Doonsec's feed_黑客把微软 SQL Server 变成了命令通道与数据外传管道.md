---
title: 黑客把微软 SQL Server 变成了命令通道与数据外传管道
url: https://mp.weixin.qq.com/s/Tn__i3Z8hoC0sIQ6QjFaDQ
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:16.227302
---

# 黑客把微软 SQL Server 变成了命令通道与数据外传管道

# 黑客把微软 SQL Server 变成了命令通道与数据外传管道

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnsIlGmqnbib3IEicaQoUicWHW6YrPuibg0SVlAUickJyXTTwa83uNxdWLoGPrtWYoZOsnvXevPnjxiaC4zun1GUuhsibYQPYSxSjrqKsM/640?wx_fmt=png&from=appmsg)

在一次与 Viva Aerobus 环境相关的入侵事件中，攻击者将一台 Microsoft SQL Server 改造成了执行系统命令、回传窃取文件的通道。而他们自用的那台可公开访问的服务器，随后把攻击工具和被盗材料暴露给了无关的互联网用户。

该活动发生于 2026 年 9 月 25 日至 29 日之间，涉及凭证抓取、源码收集以及为访问其他系统所做的准备。

调查并未确认攻击者的初始入口，也没有匹配到已知的恶意软件家族。现有记录显示的是一套工具集（toolkit），而非单一植入体（implant）。这些暴露的基础设施由 ThreatMon 研究团队在日常威胁狩猎中发现。

ThreatMon 在提供给 Cyber Security News（CSN）的报告中指出，这台服务器上存放着 17 个具名工具，为外界提供了异常详细的“入侵后操作”视角。

本次发现属于**叠加在原始入侵之上的二次暴露**，并不等同于确认发生了旅客数据泄露。研究人员没有找到证据证明攻击者成功访问了其他系统，也没有证据表明敏感的旅客信息、支付数据或同类业务数据已被窃取。

#### 黑客把微软 SQL Server 变成了命令通道

攻击者启用了 `xp_cmdshell`——这是 SQL Server 的一项功能，开启后可直接执行操作系统命令。恢复出的工具正是通过数据库会话投递 Windows 命令和经过编码的 PowerShell，从而让“数据库访问权限”变成了通往底层 Windows 系统的有效通道。

这种机制与此前针对 SQL 服务器的攻击案例相似：拿到数据库权限后，进一步在数据库之外执行系统命令。

本次恢复的证据只描述了**入侵之后**的活动，并未证明具体的初始入口是某个漏洞、口令攻击还是其他手段。

同一条数据库连接还能被用来向外带出文件。恢复出的工具会读取文件内容，将其切分成小块，转成 Base64 文本，再通过 SQL 查询结果集返回——全程无需另建通信信道。

**Base64 只是数据的文本化表示方式，并非加密**。在这套流程里，它的作用是让文件内容能够顺着数据库响应被“运”出来。于是，一条原本用来下发命令的连接，也能顺带把收集到的信息带回，攻击者因此不再依赖传统的恶意软件控制服务器。

数据库执行命令的危险性此前也在 Mjobtime 应用利用案中出现过，不过 ThreatMon 并未将本次入侵与该软件关联。两者的相似点仅在于：都是借数据库功能触达操作系统并执行命令。

HTTP 记录显示，受害环境于 9 月 25 日 16:20 拉取了一次载荷；16:21 至 16:23 之间，一台无关主机探测了这台暴露的服务器；18:04 至 18:05 之间，又有其他主机从中下载了工具和已被收集的产物。

#### 凭证暴露

暴露出的工具集中，包含了用于抓取浏览器与 Windows 凭证、测试 SQL 登录以及传输文件的脚本。

现场留下的 Mimikatz 痕迹表明存在凭证转储活动。该手法同样见于 HiddenGh0st 凭证窃取行动，但两者之间并未建立关联。

研究人员还恢复了 SQL Server Management Studio 的连接历史、数据库用户名，以及受 Windows DPAPI 保护的保存密码材料。

这些记录能帮助攻击者锁定更多目标，但**其存在并不等于所有保存的密码都已被成功解密**。

收集到的源码和配置文件涉及数据库连接、OAuth、邮件、SFTP，以及支付或报表类集成接口。

ThreatMon 在公开材料中刻意隐去了敏感值、受害主机名、用户名及其他私密内容，避免二次泄露可复用的密钥。

此外，恢复出的实用程序还会拿凭证组合去试探其他 SQL 系统，并检查对 SMB 管理共享的访问权限。

现有证据只能说明攻击者**尝试复用凭证并为在网络内移动做准备**，不能证明他们确实攻陷了那些额外系统。

防御方应使用已公开的指标回溯历史网络连接，并在终端上检索匹配的哈希值及报告中的工作目录。

凡出现异常的 `xp_cmdshell` 调用、编码后的 PowerShell，或 SQL Server 服务账户下的可疑文件操作，均应立即展开调查。

保存的数据库连接与密码记录本身也应视为敏感信息。ThreatMon 警告称，凡是流入那台暴露暂存服务器的凭证或密钥，都必须当作**已失陷**处理——因为无关第三方已经接触过这些材料，而原始攻击者未必是唯一的接收方。

#### 失陷指标（IoC）

| 类型 | 指标 | 说明 |
| --- | --- | --- |
| IPv4 地址 | 151[.]243.232.123 | 攻击者暴露的暂存服务器及存放被盗材料的服务器 |
| SHA256 | c38f49ba68b891bb476510704cddf080798f3c70075e2a517e98e04e833f64fa | .exfil.py 的公开哈希 |
| SHA256 | 33aeaaa3d57b7785ef2be5b8ccd39d534b8af50e0cd32a5036fdb64601a52fc9 | .upload.py 的公开哈希 |
| SHA256 | 8b6c53e3d57b4c3049f3d0765a44d9a52feb6af78f1eaa5aff19daf1b9665998 | .sqlspray.ps1 的公开哈希 |
| Windows 路径 | C:\Windows\Temp\artex | 用于终端排查的工作目录 |
| 文件名 | chrome\_dump.ps1 | 提取浏览器凭证的脚本 |
| 文件名 | cred\_dump.ps1 | 提取 Windows 凭证的脚本 |
| 文件名 | cred\_enum.ps1 | 枚举可用凭证的脚本 |
| 文件名 | sqlspray.ps1 | 针对目标系统测试 SQL 凭证的工具 |
| 文件名 | mssqltest.ps1 | 针对目标系统测试 SQL 凭证的工具 |
| 文件名 | exfil.py | 恢复出的文件传输工具 |
| 文件名 | upload.py | 恢复出的文件传输工具 |
| 文件名 | vault.cmd | 疑似用于访问 Windows Credential Manager / Vault |
| 文件名 | vtest.ps1 | 疑似用于访问 Windows Credential Manager / Vault |
| 目录 | loot/ | 暴露目录，内含已收集的材料 |
| 目录 | loot2/ | 另一个暴露目录，内含已收集的材料 |
| 文件名 | cred\_dec.txt | 从暴露服务器恢复的产物 |
| 文件名 | mdump.txt | 从暴露服务器恢复的产物 |
| 文件名 | httpd.log | 从暴露服务器恢复的 HTTP 日志产物 |
| 执行产物 | cmd.exe | 合法 Windows 命令解释器；若在 SQL Server 服务账户下异常执行需调查 |
| 执行产物 | powershell.exe | 合法 PowerShell 可执行文件；若经 xp\_cmdshell 异常调用需调查 |

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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