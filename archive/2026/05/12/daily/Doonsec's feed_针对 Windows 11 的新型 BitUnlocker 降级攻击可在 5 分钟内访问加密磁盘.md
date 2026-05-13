---
title: 针对 Windows 11 的新型 BitUnlocker 降级攻击可在 5 分钟内访问加密磁盘
url: https://mp.weixin.qq.com/s/oNRHKr8lkKy8AGrf3bACmg
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:45:06.027791
---

# 针对 Windows 11 的新型 BitUnlocker 降级攻击可在 5 分钟内访问加密磁盘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PA3Pem5ic2p85cFHl5zdDURyJPpU2d5wIEiatA2aFYAQ7VLub4LAaUiajzgEuOODwvfac1Y4gNnY9f2OXwPK8gpONBWnrPjrMmVk/0?wx_fmt=jpeg)

# 针对 Windows 11 的新型 BitUnlocker 降级攻击可在 5 分钟内访问加密磁盘

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一款名为 BitUnlocker 的新工具揭示了一种针对微软 BitLocker 加密的实用降级攻击，攻击者可以利用修补和证书吊销之间的关键漏洞，在 5 分钟内，通过物理访问的方式解密已打补丁的 Windows 11 计算机上的受保护卷。

此次攻击源于 CVE-2025-48804，这是微软安全测试与攻击研究 (STORM) 团队发现的四个关键零日漏洞之一，并在 2025 年 7 月的“补丁星期二”活动中进行了修复。

根据 Intrinsec 的研究，该漏洞存在于Windows 恢复环境 (WinRE)中，并且涉及系统部署映像 (SDI) 文件机制。

当启动管理器加载 SDI 引用的合法 WIM（Windows 映像格式）文件以进行完整性验证时，它同时允许将第二个由攻击者控制的 WIM 附加到 SDI 的 blob 表中。

启动管理器验证了第一个（合法的）WIM，但实际上是从第二个启动，该第二个启动包含一个修改过的WinRE映像，该映像可以启动时`cmd.exe`BitLocker卷已被解密并挂载。

微软`bootmgfw.efi`于 2025 年 7 月通过 Windows 更新为所有受支持的系统发布了已修补的二进制文件。但是，仅靠补丁并不能消除攻击面。

## **BitUnlocker 降级攻击 Windows 11**

BitUnlocker 攻击的关键弱点不是缺少补丁，而是未撤销的签名证书。

安全启动验证的是二进制文件的签名证书，而不是版本号。在 2025 年 7 月的修复程序发布之前，所有启动管理器都使用旧版 Microsoft Windows PCA 2011 证书进行签名。除非在 2026 年初之后进行了全新的 Windows 安装，否则该证书在当前几乎所有计算机的安全启动数据库中仍然受信任。

这意味着，即使存在漏洞，根据 PCA 2011 签名的预补丁`bootmgfw.efi`仍被安全启动视为完全有效。

大规模撤销 PCA 2011 对微软来说是一个重大的运营挑战，因为它会影响整个生态系统中各种合法的签名二进制文件。

基于最初的 STORM 研究和之前对“bitpixie”降级漏洞的研究，研究人员开发了一个可行的 PoC，将这些弱点串联起来，在不到五分钟的时间内发起攻击。

据 Intrinsec 称，攻击者只需要对目标工作站进行物理访问，使用 USB 驱动器或 PXE 启动服务器，而无需任何专用硬件。

攻击过程如下：攻击者准备一个修改过的 BCD（启动配置数据）文件，指向一个被篡改的 SDI，并通过 USB 或 PXE 启动提供一个旧的、易受攻击的 PCA 2011 签名的启动管理器。

目标机器加载了补丁前的启动管理器，正常通过了安全启动验证。

由于受信任的 PCA 2011 证书下 PCR 测量值 7 和 11 仍然有效，TPM 会在不触发任何警报的情况下释放 BitLocker 卷主密钥。结果：打开命令提示符，操作系统卷已完全解密并挂载。

仅运行 TPM BitLocker（没有 PIN）且其安全启动数据库仍然信任 PCA 2011 的系统完全易受攻击。

配置了 TPM + PIN 的机器受到保护，因为在启动前身份验证期间，如果没有用户交互，TPM 不会解封 VMK。

已完成KB5025885 迁移（将启动管理器签名移至更新的 Windows UEFI CA 2023 证书）的系统也能免受此降级路径的影响。

## **缓解措施**

安保团队应立即采取以下措施：

* **启用 TPM + PIN 预启动身份验证**——这是最有效的控制措施，可防止 TPM 在任何被篡改的启动序列期间释放 VMK。
* **部署 KB5025885** — 此 Microsoft 更新将启动管理器签名迁移到 CA 2023，并引入撤销控制，从而消除降级路径。
* **验证启动管理器证书**——挂载 EFI 分区并使用`sigcheck`它来确认活动证书`bootmgfw.efi`是根据 CA 2023 签名的，而不是根据旧版 PCA 2011 签名的。
* **在无法强制执行启动前身份验证的高安全性工作负载中，删除 WinRE 恢复分区**，从而最大限度地减少此类漏洞利用的攻击面。

PoC 已在 GitHub 上公开提供，这促使企业防御者更加迫切地需要审核其 BitLocker 配置，并在机会主义攻击者利用此技术进行有针对性的入侵之前加快 CA 2023 迁移。

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