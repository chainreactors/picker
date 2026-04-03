---
title: 赛门铁克DLP代理漏洞允许攻击者提升权限
url: https://mp.weixin.qq.com/s/KIdRHmMcRrOMjBs4-_V6mQ
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:24:14.072519
---

# 赛门铁克DLP代理漏洞允许攻击者提升权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NW9icOBiaKKYge8n0E1VcY13DAHjK7ia2RO3hWSeECd7ib5HgdwkaaYTbt8I58zt92rWmq2nTZ57mxCUnLs6tsNeIhdZyDonVQtEw/0?wx_fmt=jpeg)

# 赛门铁克DLP代理漏洞允许攻击者提升权限

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Symantec数据丢失防护 (DLP) Windows 代理程序中发现了一个高危安全漏洞。

该漏洞编号为 CVE-2026-3991，允许低权限的本地攻击者将其系统权限提升到最高级别。

安全研究员曼努埃尔·费费尔发现了这个漏洞，博通公司最近发布了补丁来解决这个问题。

该漏洞的 CVSS 评分为 7.8。利用该漏洞无需任何特殊配置，这意味着使用默认设置运行的代理程序完全暴露。

## **赛门铁克 DLP 代理漏洞**

核心问题源于 OpenSSL 库的编译方式以及将其集成到 Symantec DLP Agent 中的方式。

该库的构建过程中使用了硬编码的配置路径，指向一个特定的开发目录，而该目录在标准的 Windows 安装中并不存在。

由于 Windows 通常默认授予已认证用户在根目录级别创建缺失文件夹的权限，因此任何低权限用户都可以重现此开发路径。易受攻击的进程 edpa.exe以 SYSTEM 权限运行。

当此过程开始时，它会在攻击者控制的硬编码位置搜索其OpenSSL 配置文件(openssl.cnf)。

要成功利用 CVE-2026-3991，具有基本本地访问权限的威胁行为者必须遵循一条简单的攻击路径。

* 攻击者在 C:\VontuDev\workDir\openssl\output\x64\Release\SSL\ 创建缺失的目录结构。
* 他们将恶意 OpenSSL.cnf 文件和有效载荷 DLL 放入这个新创建的文件夹中。
* 精心构造的配置文件使用标准的 OpenSSL 指令 dynamic\_path 直接指向攻击者的 DLL。
* 当 Symantec DLP Agent 服务重新启动或触发 OpenSSL 初始化时，它会读取恶意配置文件。
* 系统将攻击者的DLL 作为动态引擎加载，并立即以 SYSTEM 权限执行它。

由于恶意代码直接在受信任的 DLP 代理进程中执行，因此该攻击对企业网络尤其危险。

威胁行为者可以利用这种技术绕过终端安全保护，并完全规避系统遥测。

此外，攻击者可以利用这种被入侵的进程，在主机上保持深度、持久的访问权限，同时对安全监控工具而言，这看起来完全合法。

## **受影响版本和已修复版本**

博通公司于 2025 年 11 月首次获悉该问题，并于 2026 年 3 月 30 日发布了正式的安全公告和修复程序。

依赖赛门铁克数据防泄漏 (DLP) 的组织应立即更新其Windows 端点代理，以缓解此威胁。

该漏洞会影响 16.1 MP2 或 25.1 MP1 之前的 Symantec DLP 代理。

强烈建议系统管理员升级到以下数据丢失防护 (DLP) 的修复版本：DLP 25.1 MP1、DLP 16.1 MP2、DLP 16.0 RU2 HF9、DLP 16.0 RU1 MP1 HF12 和 DLP 16.0 MP2 HF15，如Infoguard Labs 公告中所述。

管理员应优先考虑这些补丁，尤其是在内部威胁、本地权限提升或横向移动是重大安全问题的环境中。

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