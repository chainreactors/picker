---
title: 虚假客服攻击利用 Teams 和快速协助功能入侵目标
url: https://mp.weixin.qq.com/s/xAgh35G6XUGBLBhP-tSoPg
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:45:34.378270
---

# 虚假客服攻击利用 Teams 和快速协助功能入侵目标

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7P7ibKDfIelJGEepCKWLJUxkqc4gQAZ9m2KhFiaxqNQMViauY6y1AnloEtFKd7gOhoqHtJ36eMzl0sGfskLgujbp6cIpjBD9OFneE/0?wx_fmt=jpeg)

# 虚假客服攻击利用 Teams 和快速协助功能入侵目标

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

攻击者越来越多地滥用 Microsoft Teams 和 Windows 快速助手，发起以服务台为主题的社会工程攻击链，最终导致企业全面入侵和隐蔽的数据窃取。

通过冒充 IT 支持人员，并依靠合法的工具和协议，攻击者可以横向移动并窃取数据，同时融入正常的管理活动中。

他们使用“帮助台”或“IT支持”等名称，利用外部协作功能，使他们的联系看起来像是例行支持，而不是传统的网络钓鱼。

Teams 内置的防御机制，例如外部标签、接受/阻止提示和垃圾邮件/网络钓鱼横幅，都存在，但攻击的关键在于说服用户忽略这些警告。

语音钓鱼通常叠加在聊天之上，以增加紧迫感，迫使受害者在不核实来电者身份的情况下按照指示行事。

在最近的攻击活动中，攻击者冒充内部 IT 或服务台人员，发起跨租户 Microsoft Teams 聊天和通话。

这使得攻击者能够以解决问题为幌子，立即对工作站进行交互式远程控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NqFXuhjYSYd4M356q1xnJVNeZlI0ia3SHqbXUy3hPcz6pAk7hquLy0kpxXib3lpFRjTkJ3ibB9icjfGj2eL6XRnbca9Ooe2zdm3HE/640?wx_fmt=png&from=appmsg)

一旦建立起信任关系，攻击者就会指示用户启动快速协助会话，输入短代码，并批准所有权限提升提示。

## **从快速协助到隐秘处决**

攻击者获得访问权限后，会在最初的一两分钟内运行 cmd.exe 和 PowerShell 等命令，以确认用户权限、域成员身份和网络可达性。

如果主机拥有足够的权限，他们就会将小型暂存包放入 ProgramData 等位置，并通过受信任的、供应商签名的二进制文件使用 DLL 侧加载来运行攻击者提供的模块。

外部接受/阻止屏幕会向用户发出有关首次联系事件的通知，提示用户在接受之前检查发件人的身份。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PX4Ot1m2q6u1yTLia6P3JuAicoYXvcCOtTCpf8qtqJsMuiaMVupPPz68G0iamELpoaSBLAARKrq0gGRYiaSCiavwJmaXUjc5AYqAx9c/640?wx_fmt=png&from=appmsg)

观察到的加载器包括更新或安全主题的可执行文件，这些可执行文件从非标准路径加载恶意 DLL，从而允许代码在受信任的进程名称下执行。

攻击者还会将大量的编码值写入用户上下文注册表位置，以存储加密的配置数据，然后通过侧加载的模块在内存中解密这些数据。

这种轻文件方法与现代入侵防御框架类似，后者将命令与控制 (C2) 设置保存在注册表中，以便在重启和一些修复操作后仍然有效。

然后，通过端口 443的出站 HTTPS 连接，从被劫持的更新程序式进程建立到云托管基础设施的 C2 连接，伪装成正常的网络流量。

植入程序生效后，威胁行为者可以利用 TCP 5985 上的原生 Windows 远程管理 (WinRM) 在网络内部进行跳板，从而访问其他已加入域的系统。

微软观察到，基于凭证的横向移动正从这些用户发起的会话转移到以身份为中心的资产，包括域控制器和其他高价值基础设施。

安全链接功能可在点击时发出警告，提醒用户 Teams 聊天消息中的 URL 可能存在恶意行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7Ohib7e6QHgzicYNtku64Fn3pGibQgT4ibzH4Mzc6NzgjRWGepnC8gDCadbQ3pxNSQU5iaP14AWRAF87dNJ5pRgptba42T4IKM918Mk/640?wx_fmt=png&from=appmsg)

为了扩大控制范围，攻击者通过 msiexec 远程部署商业远程管理工具，从而获得一个看起来像标准 IT 软件的持久性辅助通道。

对于数据窃取，犯罪分子依靠 Rclone 等工具将选定的业务文档同步到外部云存储。

传输过滤器通常会进行调整，以排除噪声文件类型，同时专注于与业务相关的数据，从而减少文件数量和检测可能性。

因为每一步都使用了合法的应用程序和管理协议（Teams、Quick Assist、签名二进制文件、WinRM、商业 RMM 和云同步），所以入侵过程与端到端的例行支持活动非常相似。

## **风险与防御指导**

这种攻击链会显著增加严重依赖 Teams 和远程支持的企业的风险，因为它绕过了以电子邮件为中心的网络钓鱼控制，并滥用了用户对内部服务台工作流程的信任。

在权限受限的系统（例如自助服务终端、VDI 或未加入公司的设备）上，攻击者可能会暂停而不部署有效载荷，只留下短暂的侦察活动。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MnjT602c6d0CJIFThVhYrBQDQGfOguMa7xjbjcHS01OThqSdSUgSQGzd4Y8lwTQc2KQkgxtdkbFqr1aV5W3Q7YQlyQrdSXASI/640?wx_fmt=png&from=appmsg)

有效的缓解措施需要加强外部协作策略，限制远程协助的发起者，并加强端点对 DLL 侧加载和未经批准的远程工具的防护。

微软建议为 Teams 启用安全链接和零时自动清除 (ZAP)，对特权角色强制执行带有 MFA 的条件访问，将 WinRM 限制在授权的管理员工作站，并通过搜寻和自定义检测来监控 Rclone 等工具。

用户教育仍然至关重要：组织应清楚地解释真正的 IT 人员将如何联系员工，如何识别 Teams 中的外部租户和警告横幅，以及为什么未经请求的远程协助请求应被视为可疑并报告给安全团队。

微软 Defender 的跨身份、端点和协作平台的关联遥测数据可以帮助检测和阻止这种用户发起的访问路径，防止其升级为全面入侵。

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