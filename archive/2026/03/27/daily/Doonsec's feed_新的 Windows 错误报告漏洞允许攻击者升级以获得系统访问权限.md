---
title: 新的 Windows 错误报告漏洞允许攻击者升级以获得系统访问权限
url: https://mp.weixin.qq.com/s/IyAA2ODg1nY1u8XQyEdtWA
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:14:33.165267
---

# 新的 Windows 错误报告漏洞允许攻击者升级以获得系统访问权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MAfeE3scY19OTVmBht1bWntOZyYsCuNicKiblMV7dA9fXhZGaL5mXO44eUkjLFYH7nfwJn46IMG0sl63KKQqicANEKB9MxNtPiaL0/0?wx_fmt=jpeg)

# 新的 Windows 错误报告漏洞允许攻击者升级以获得系统访问权限

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Windows 错误报告（WER）服务中一个新发现的本地权限提升漏洞，使攻击者能够轻易获得完整的系统访问权限。

该漏洞被追踪为 CVE-2026-20817，其结构危险性极大，以至于微软彻底移除了这一存在漏洞的功能，而非尝试传统的代码修补。

该安全漏洞存在于 Windows 错误报告服务的主要可执行库中，具体来说是 WerSvc.dll 文件。

据 GMO Cybersecurity 的漏洞研究人员丹尼斯·费乌斯托夫（Denis Faiustov）和鲁斯兰·赛菲耶夫（Ruslan Sayfiev）称，该服务在处理特定客户端请求时，对权限不足的情况处理不当。

这种架构缺陷为权限较低的本地用户提供了可靠途径，使其能够触发高级别的命令执行漏洞。

从历史上看，由于 Windows 错误报告服务复杂的进程间通信需求，它一直是特权提升攻击的常见目标。

攻击者精心构造一条包含文件映射对象的消息，诱使内部的 ElevatedProcessStart 函数复制句柄，并使用 MapViewOfFile API 读取恶意的命令行参数。

最终，会调用 CreateElevatedProcessAsUser 函数，这无意中以具有高度特权的 SYSTEM 权限以及攻击者高度控制的参数启动了合法的 WerFault.exe 应用程序。

安全分析师在对 WerSvc.dll 文件的 10.0.26100.7309 版本和 10.0.26100.7623 版本进行二进制差异分析时发现，微软采取了不同寻常的激进措施来进行修复。

开发人员没有添加权限检查或输入清理例程，而是引入了一个严格的 \_\_private\_IsEnabled() 功能测试，永久禁用了 SvcElevatedLaunch 功能。

如果执行了修补后的代码，该函数会立即返回 0x80004005（E\_FAIL）错误代码，通过完全移除该功能从而有效地消除了整个攻击面。

虽然该漏洞确实能成功以 SYSTEM 身份强制执行 WerFault.exe，但攻击者必须结合特定的命令行选项以及高级的 Windows 内部技巧才能实现任意代码执行。

在漏洞利用过程中，WER 服务通过使用父进程 ID 伪造技术，使新生成的具有提升权限的进程看起来就像是攻击者低权限客户端的直接子进程。

由于这种特定的进程欺骗技术被现代恶意软件大量滥用，像微软防御者这样的安全解决方案能够主动检测此类行为，并立即发出警报。

网络安全专家在研究这一特定的本地权限提升威胁时必须保持高度警惕。

在诸如 GitHub 等平台上，出现了多个关于 CVE-2026-20817 漏洞的虚假且可能具有恶意性质的演示代码库。

这些具有欺骗性的项目文件通常会包含隐藏的恶意软件代码，这强烈提醒我们，在执行任何下载的安全工具之前，必须对其进行严格的隔离和静态分析。

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