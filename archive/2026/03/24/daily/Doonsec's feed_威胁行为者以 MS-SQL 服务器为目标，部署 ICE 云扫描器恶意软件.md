---
title: 威胁行为者以 MS-SQL 服务器为目标，部署 ICE 云扫描器恶意软件
url: https://mp.weixin.qq.com/s/MBEBqMqg6aL0VgcprxiaWg
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:15:03.965553
---

# 威胁行为者以 MS-SQL 服务器为目标，部署 ICE 云扫描器恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7P18eeFyEfFicXfRzhrfGULIoIfKLMcBkgmBS0rLCibCrSwvD6PdAIVBAhKqpiajXLkX4VmVrJjvqCwBZzsOiayjTzcbvJclr1ZYOI/0?wx_fmt=jpeg)

# 威胁行为者以 MS-SQL 服务器为目标，部署 ICE 云扫描器恶意软件

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

2026 年，威胁行为者继续积极攻击 Microsoft SQL (MS-SQL) 服务器，新的证据表明，他们部署了一种名为 ICE Cloud Client 的扫描恶意软件。

Larva-26002 一直专注于保护暴露在互联网上的安全性较差的 MS-SQL 服务器。

这些系统通常通过使用弱凭据的暴力破解或字典攻击而被攻破。

一旦获得访问权限，攻击者就会执行一系列侦察命令，例如检查主机名、用户上下文、网络配置、活动连接和正在运行的进程，以了解受感染的环境。

根据 AhnLab 安全情报中心 (ASEC) 的说法，该活动与Larva-26002 威胁组织有关，该组织此前曾在早期的攻击活动中传播过 Trigona 和 Mimic 勒索软件。

这并非首次发起此类攻击。2024年，同一犯罪团伙就曾利用MS-SQL服务器部署Trigona和Mimic勒索软件，并使用AnyDesk等工具实现持久化和远程访问。

到 2025 年，攻击者改进了策略，引入了 Teramind 等远程监控工具，并部署了用 Rust 编写的自定义扫描器。2026 年的攻击活动标志着又一次转变，攻击者用名为 ICE Cloud 的基于 Go 语言的恶意软件取代了之前的工具。

## **滥用 BCP 实用程序进行恶意软件攻击**

在所有攻击活动中都观察到的一个关键技术是滥用批量复制程序 (BCP) 工具，该工具是MS-SQL 中用于数据导入和导出的合法工具。攻击者将恶意载荷存储在数据库表中，然后将其提取为可执行文件并部署到系统中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MreUsx0KFTibX7eDSnqiaxfZib51Nxhnp5QjGdicflsdO40nOCQpdI80S349EsuQWc4EvclMRp07pc8gCeIic2D9v0fXNKeW5Ria1iaQ/640?wx_fmt=png&from=appmsg)

在最近的攻击中，恶意软件使用预定义格式的文件，从名为“uGnzBdZbsi”的表中导出到类似“C:\ProgramData\api.exe”的文件中。这些标识符自2024年以来一直保持不变，表明攻击手段仍在持续。

在某些 BCP 不可行的情况下，攻击者会转而使用 curl、bitsadmin 或 PowerShell 等工具从远程服务器检索有效载荷，从而采用其他下载方法。

被投放的有效载荷通常名为 api.exe，它会下载并安装 ICE Cloud Client。该恶意软件使用 Go 语言编写，兼具扫描器和暴力破解工具的功能。在执行过程中，它会以“ICE Cloud Launcher”的标签运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NdCMM4nklj9pR32NyGCNT5ia36Aomeer1QoTLhykrJjepD268xLS5tAKCnVPoKqvyKpyC6ydOKJAH19icqSYG03PibM8biaiaS8AEE/640?wx_fmt=png&from=appmsg)

恶意软件执行后，会与命令与控制 (C2) 服务器通信以进行身份验证并接收指令。然后，它会下载 ICE 云客户端主组件，并将其伪装成随机文件名，以模仿合法应用程序。

ICE 云客户端负责扫描目标 MS-SQL 服务器。值得注意的是，其二进制文件包含土耳其语字符串，这一特征此前曾与 Mimic 勒索软件攻击活动相关联。

执行日志中出现表情符号表明可能在开发或混淆过程中使用了生成式人工智能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PcLkckDViaUMnXKHDuvQKJMf1cicU6tEZB5hZMib5wdhRxVaQMtyXJY0OQaIA3LqOguW6B0vzdS8QaaVIqaryhWzhHHYRXc20mH8/640?wx_fmt=png&from=appmsg)

在向 C2 服务器注册后，恶意软件会收到目标 IP 地址列表以及凭据（通常为“ecomm/ecomm”）和标记为“TASK”的指令。

然后，它会尝试对这些目标进行身份验证，并将成功的入侵报告给服务器。

## **缓解措施**

基础设施、技术和标识符的持续再利用表明 Larva-26002 正在不断发展，而不是重新发明其运作方式。

扫描目标协议为“mssql”，ID/PW为“ecomm/ecomm”，并附带字符串“TASK”。在通过C&C服务器身份验证后，扫描器会继续进行注册过程，服务器会根据注册过程发送一份攻击前MS-SQL服务器地址列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7Nq9XxbwIzk9yBfPjjkqibwbkDXeNSWDiceAMeWEJ3L41b7Y5uVwUKdyWAerD5sM0TkEvdfzwZH7PeGxXGCBnjLfwsia5Qjn9rZ9c/640?wx_fmt=png&from=appmsg)

从勒索软件部署到基于扫描器的传播的转变表明，攻击者采取了一种更广泛的策略，旨在扩大对易受攻击系统的访问权限，然后再执行进一步的攻击。

运行 MS-SQL 服务器的组织应立即采取措施降低风险并防止信息泄露：

* 使用强密码和复杂密码，并强制定期轮换凭据。
* 尽可能禁用或限制对数据库服务器的外部访问。
* 实施防火墙规则，将访问限制在受信任的 IP 地址范围内。
* 监控 BCP、curl 和 PowerShell 等工具的可疑使用情况。
* 保持终端安全解决方案更新，以便检测和阻止恶意软件。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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