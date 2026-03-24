---
title: VoidStealer 无需注入或权限提升即可窃取 Chrome 密钥
url: https://mp.weixin.qq.com/s/VVE_Ud-GwV5zjmf7jDMFbQ
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:13:44.543209
---

# VoidStealer 无需注入或权限提升即可窃取 Chrome 密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PCia1uCkTibJkgQkvtzVW6EdiaVuibCE7qK3icY1QsfLofibXGE99SXbVdtjgGJeTkFHibqY8Kfxvf0C1bbiaphoTSuCWhYvmCHyLfNro/0?wx_fmt=jpeg)

# VoidStealer 无需注入或权限提升即可窃取 Chrome 密钥

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

MaaS 信息窃取程序 VoidStealer 的一个新变种已成为第一个在野外发现的恶意软件，它利用基于调试器的绕过 Google Chrome 应用程序绑定加密 (ABE) 的漏洞，使用硬件断点直接从浏览器内存中窃取 Chrome 的 v20\_master\_key。

与以往的 ABE 绕过方法不同，这种方法既不需要系统级权限提升，也不需要向浏览器进程注入代码，从而大大减少了检测的可能性，同时仍然允许攻击者完全访问受 ABE 保护的 cookie 和凭据。

ABE 将 cookie 等秘密信息以及某些配置中的密码存储为 v20 前缀值，并使用每个应用程序的 AES-GCM 密钥（通常称为 v20\_master\_key）进行加密，该密钥本身使用 NT AUTHORITY\SYSTEM 下的 CryptProtectData 进行保护，并在 Chrome 调用 IElevator::Decrypt 时通过Google Chrome Elevation Service进行解密。

传统的信息窃取者已经开发出多种绕过方法，包括以 SYSTEM 权限运行并复制服务逻辑，或者注入浏览器以从 Chrome 上下文内部通过 COM 调用 IElevator::DecryptData。然而，这两种方法在 EDR 遥测数据中都会产生相对较大的噪声。

Google于 2024 年 7 月在 Chrome 127 中引入了 ABE，通过将解密与 Chrome 的身份和特权提升服务绑定，使 cookie 和其他秘密窃取尝试更容易被发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MHDPibFsx1LAqQQ0omibAqB3vJ7aiaFlcD3YvJXgiatoO4ibY5FhYka0ibibKW92xON7jOTgLfOQxrDiad2Re30HKhEsiaycOOdMBNiacMk/640?wx_fmt=png&from=appmsg)

VoidStealer 遵循这一模式，实现了“经典的”基于 COM 的 IElevator::DecryptData 注入技术作为备选方案。

然而，v2.0 的突出特点是调试器驱动的方法，该方法通过在正常 ABE 解密期间主密钥以明文形式存在的短暂瞬间窃取主密钥，从而绕过了 SYSTEM 和注入要求。

这使得新的绕过方法对那些想要规避以权限提升、进程空心化和远程线程注入浏览器为重点的行为检测的威胁行为者来说尤其具有吸引力。

## **基于调试器的 v20\_master\_key**

这项新技术几乎直接复制自 Meckazin 的开源 ElevationKatz 项目，其关键在于将 Chrome 或 Edge 浏览器作为调试器进行连接，并利用硬件断点在 Chrome 解密 v20\_master\_key 以处理 ABE 保护的数据时拦截该密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MiaqAzIPYBbibkycRhibwjpvJmaLLrbTpzkBQq3dtTAWicpGs5zTXQxbD1IYSvwtGXqticFkamYAsQlhm9NqDqfl3LTfPSQ9hH0iaks/640?wx_fmt=png&from=appmsg)

VoidStealer v2.0 首先使用 SW\_HIDE 和 CREATE\_SUSPENDED 通过 CreateProcessW 生成一个隐藏的浏览器实例，然后快速恢复它，并通过 DebugActiveProcess 将其附加为调试器，利用浏览器通常在启动期间加载和解密 cookie 的事实。

一旦附加，VoidStealer 会等待 LOAD\_DLL\_DEBUG\_EVENT 通知，识别 chrome.dll 或 msedge.dll，并使用 ReadProcessMemory 扫描模块的 .rdata 部分，以找到 OSCrypt.AppBoundProvider.Decrypt.ResultCode 字符串，该字符串是 Chromium 在 ABE 解密路径中调用 os\_crypt::DecryptAppBoundString 之后立即放置的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PZtcxcdtjCseJF2mwN6fdCicibiaMMX7iacgSsOel95WAkVAtlA9HQ01ma4UWSh0F90zIdeKPBjw2QC5tMbz1rwTjLVgzM8fJHickc/640?wx_fmt=png&from=appmsg)

然后，它扫描 .text 段，查找 LEA 指令（48 8D 0D …），这些指令的计算位移解析为该字符串，从而产生一个精确的指令地址，当 v20\_master\_key 以明文形式驻留时，该指令将被执行。

VoidStealer 使用 NtGetNextThread 和 SetThreadContext 在所有现有和新创建的浏览器线程的该地址处配置硬件断点 (DR0/DR7)，从而避免了软件断点所需的任何浏览器内存修补。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NaC4urSqTWcibONxAMs445eMicFPmGNUK2U4KkLzRumYIZh2naFQ51YBs2JeUe7XNvqboFER1SoUCYgAcficvqxPxBTDF5J6fXpg/640?wx_fmt=png&from=appmsg)

当浏览器在启动期间遇到此断点时，当前版本的 Chrome 和 Edge 会在 R15（Chrome）或 R14（Edge）中放置指向 v20\_master\_key 的指针，从而允许 VoidStealer 跟踪寄存器值并使用一对 ReadProcessMemory 调用提取密钥，而无需在受害者进程中使用任何 CryptUnprotectData 或 CryptUnprotectMemory。

一旦获取了 v20\_master\_key，信息窃取者就可以从浏览器 SQLite 数据库中离线解密任何以 v20 为前缀的受 ABE 保护的 cookie 和凭据，从而有效地使该配置文件的 ABE 保护失效。

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