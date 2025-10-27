---
title: 微软禁用 BitLocker 安全修复程序，建议手动缓解
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577602&idx=1&sn=d60cc005be831f93d97548d01656764c&chksm=e9146038de63e92ec433dccdeb10ce0e8cdf803791eae875fee0ff8e9bfa2ac7113781335fab&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-08-21
fetch_date: 2025-10-06T18:04:31.263807
---

# 微软禁用 BitLocker 安全修复程序，建议手动缓解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic6JOiaZkPNfDN6dGYZESd3S8TuSmEiaeAcjnxYaiccGKUoaWnm8vCmmiaZfiaFpeDPFIFibUoRY1KMWiaicQ/0?wx_fmt=jpeg)

# 微软禁用 BitLocker 安全修复程序，建议手动缓解

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

由于固件不兼容问题导致已修补的 Windows 设备进入 BitLocker 恢复模式，Microsoft 已禁用针对 BitLocker 安全功能绕过漏洞的修复。

该漏洞被标记为 CVE-2024-38058，它可让攻击者绕过 BitLocker 设备加密功能，并通过物理访问目标设备来访问加密数据。

该公司在更新中解释道：“当客户将针对此漏洞的修复程序应用于他们的设备时，我们收到了有关固件不兼容问题的反馈，这些问题导致 BitLocker 在某些设备上进入恢复模式。因此，随着 2024 年 8 月安全更新的发布，我们将禁用此修复程序。”

禁用修复程序后，微软建议那些想要保护其系统和数据免受 CVE-2024-38058 攻击的用户应用 KB5025885 公告中详述的缓解措施。

但是，他们现在不必部署安全更新，而是必须经历一个 4 阶段的过程，该过程还需要重新启动受影响的设备八次。

此外，微软警告说，在具有安全启动功能的设备上应用缓解措施后，即使重新格式化磁盘，他们也无法再将其删除。

在设备上启用此问题的缓解措施后，即已应用缓解措施，如果用户继续在该设备上使用安全启动，则无法恢复。即使重新格式化磁盘也无法删除已应用的撤销。

在本月的补丁星期二，雷德蒙德还修复了 7 月 Windows 安全更新引发的一个已知问题，该问题导致一些 Windows 设备启动到 BitLocker 恢复。

虽然这与迫使微软禁用 CVE-2024-38058 修复的固件不兼容问题相符，但该公司没有提供任何有关实际根本原因或如何解决该问题的信息。

微软只是建议受影响的客户为他们的设备安装最新更新，因为它包含重要的改进和问题解决方，而没有以任何方式将该错误或其修复与 CVE-2024-38058 漏洞联系起来。

参考及来源：https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-bitlocker-security-fix-advises-manual-mitigation/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic6JOiaZkPNfDN6dGYZESd3SaVF7VCNibwrUJqaZxk4h1UEEkRLBQib7Du9iapTX1DialNeBWeDxgsFZQA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic6JOiaZkPNfDN6dGYZESd3SaNQcDFq5ibh0k958AsXmhrfj3jeE1BtT6juQExibCJop73icvc7MwDwlA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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