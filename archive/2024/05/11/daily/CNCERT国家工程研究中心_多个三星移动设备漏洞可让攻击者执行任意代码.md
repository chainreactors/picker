---
title: 多个三星移动设备漏洞可让攻击者执行任意代码
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247544511&idx=4&sn=e534c9301c354ce82b2432df461e824e&chksm=fa93987ecde411680c23b31d24a508894409f38608846abdcfb79d0a9b9d4b934b4f6df451c0&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-05-11
fetch_date: 2025-10-06T17:17:43.738399
---

# 多个三星移动设备漏洞可让攻击者执行任意代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nkTt9WmE1kjNQblxmVeYmeDW83xmPBRpmUibAsMRStI9nhk8HXeElpvJyiaav5TOSKyoA6Vrx7RE0Q/0?wx_fmt=jpeg)

# 多个三星移动设备漏洞可让攻击者执行任意代码

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nkTt9WmE1kjNQblxmVeYmewJ68ZKBciamgqfMzwWHsv51l0edibPwQ0Zib437mLJQrAV9iciaPDah3JLw/640?wx_fmt=jpeg&from=appmsg)

在最新网络安全更新中，三星宣布修补了其移动设备中的 25 个漏洞，旨在增强其抵御潜在的代码执行和权限升级攻击的能力。

这是三星持续增强智能手机和平板电脑安全性的一部分举措，以此确保用户的安全和隐私。

这些漏洞被确定为三星漏洞和暴露（SVE）项目。这些缺陷涉及三星设备的各个组件，包括操作系统、固件以及三星开发的某些专有软件。这些漏洞可能允许恶意分子在设备上执行任意代码或提升其权限，从而获取对敏感信息或系统功能的未经授权的访问。

三星对这些安全威胁迅速响应，通过在 2024 年 5 月的安全维护版本 (SMR) 中包含了这 25 个 SVE 项目的补丁，三星已采取主动措施来减轻与这些漏洞相关的风险。

# **已修复的一些特定安全缺陷的详细信息**

SVE-2023-1778 (CVE-2024-20866)

这是安装向导中的身份验证绕过漏洞，允许未经授权的用户绕过设备设置身份验证机制。该漏洞的补丁涉及在安装过程中删除不必要的互联网访问，以防止未经授权的访问。

SVE-2023-2193 (CVE-2024-20855)

此缺陷是多任务框架内的不当访问控制问题。它允许未经授权的用户访问和操纵多任务功能，从而导致权限升级攻击。该更新通过实施更严格的访问控制来纠正这一问题。

SVE-2023-2265 (CVE-2024-20856)

三星安全文件夹中的一个不正确的身份验证漏洞已修复。此缺陷允许攻击者绕过身份验证措施并访问存储在安全文件夹中的敏感信息。

SVE-2024-0092 (CVE-2024-20861) 和 SVE-2024-0096 (CVE-2024-20862)

SveService 中的这些相关漏洞分别包括释放后使用问题和越界写入缺陷。如果被利用，两者都可能导致任意代码执行。这些补丁解决了这些内存损坏问题，防止了此类漏洞的发生。

SVE-2024-0234 (CVE-2024-20865)

这是引导加载程序中的身份验证绕过，以前允许物理攻击者刷新任意图像。该补丁添加了适当的验证检查，以防止未经授权的刷新，从而增强设备启动过程的安全性。

SVE-2024-0357 (CVE-2024-20864)

DarManagerService 中的不当访问控制漏洞已得到纠正。此缺陷允许对 DarManagerService 进行未经授权的访问，从而导致进一步的利用。

修补的漏洞是安全更新更广泛的一部分，该更新还包含谷歌的修复程序，解决与 Android 操作系统相关的问题。三星和谷歌之间的这种合作方式确保三星设备不仅可以收到针对专有问题的补丁，还可以从 Android 平台提供的更广泛的安全增强功能中受益。

三星敦促其移动设备的所有用户将其软件更新到最新版本，以便享受这些安全增强功能的防护。

**参考及来源：**

https://gbhackers.com/25-flaws-patched-samsung/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

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