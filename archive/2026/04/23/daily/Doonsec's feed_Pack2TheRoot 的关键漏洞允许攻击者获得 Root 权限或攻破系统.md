---
title: Pack2TheRoot 的关键漏洞允许攻击者获得 Root 权限或攻破系统
url: https://mp.weixin.qq.com/s/CE2Bwu3NQUOldJqFY4K9gA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:51:48.931445
---

# Pack2TheRoot 的关键漏洞允许攻击者获得 Root 权限或攻破系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NPM9b9pUQjIesibnmSOqlJ47XLVb7Lm2eSdgG4OUtjXYNlU6vGQGBvnVicClHqznoHKg2r2lNchmuW7uhibVFsm15YuABtapVKrA/0?wx_fmt=jpeg)

# Pack2TheRoot 的关键漏洞允许攻击者获得 Root 权限或攻破系统

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

德国电信红队公开披露了一个高危权限提升漏洞，名为 Pack2TheRoot（CVE-2026-41651，CVSS 3.1：8.8），该漏洞会影响多个主流Linux 发行版的默认安装。

该漏洞允许任何本地非特权用户静默安装或删除系统软件包，最终无需密码即可获得完全 root 权限。

该漏洞存在于 PackageKit 守护程序中，这是一个广泛部署的跨发行版软件包管理抽象层，在 Debian、Ubuntu、Fedora 和 Red Hat 等系统中均有使用。

利用此漏洞，具有基本本地访问权限的攻击者可以完全绕过授权控制，安装恶意软件包或删除关键安全组件，从而破坏系统。

据 Telekom Security 称，从 1.0.2 到 1.3.4 的所有 PackageKit 版本均受到影响，跨越 12 年的发布时间，造成了极其广泛的攻击面。

由于 PackageKit 也是 Cockpit 服务器管理项目的可选依赖项，因此运行 Cockpit 的企业服务器（包括运行 Red Hat Enterprise Linux (RHEL) 的服务器）也可能受到影响。

已在以下默认安装环境中测试并确认存在漏洞：

* Ubuntu Desktop 18.04、24.04.4 LTS 和 26.04 LTS Beta 版
* Ubuntu Server 22.04 和 24.04 LTS
* Debian Desktop Trixie 13.4
* Rocky Linux Desktop 10.1
* Fedora 43 桌面版和服务器版

任何启用了 PackageKit 功能的分发包都应被视为潜在安全漏洞。

该漏洞由德国电信安全团队在针对现代Linux系统本地权限提升途径进行专项研究时发现。该团队最初注意到，一条`pkcon install`命令可以在Fedora工作站上安装系统软件包而无需输入密码。

从 2025 年开始，研究人员利用 Anthropic 公司的 Claude Opus 工具来指导和加速他们的调查，最终发现了可利用的漏洞。所有发现都经过人工审核，之后负责任地披露给了 PackageKit 的维护人员，他们确认了该问题及其可利用性。

虽然目前不会公开发布，但已经存在一个可行的概念验证（PoC），可以在几秒钟内可靠地执行 root 代码。

## **如何检查您是否存在安全漏洞**

由于 PackageKit 和 Cockpit 并非始终作为持久进程运行（它们可以通过 D-Bus 按需激活），因此简单的进程列表检查是不够的。请使用以下命令：

* **Debian/Ubuntu：**

  `dpkg -l | grep -i packagekit`
* **基于转速：**

  `rpm -qa | grep -i packagekit`
* **检查守护进程状态：**

  `systemctl status packagekit`或`pkmon`

尽管该攻击可在数秒内被利用，但会留下可检测的痕迹。利用该漏洞会导致 PackageKit 守护进程遭遇断言失败并崩溃，此过程会被记录并可由 systemd 恢复。防御者应监控以下日志特征：

`journalctl --no-pager -u packagekit | grep -i emitted_finished`

断言失败`pk-transaction.c:514`是积极利用漏洞的有力指标。

## **减轻**

该漏洞已在 PackageKit 1.3.5 中修复，该版本于 2026 年 4 月 22 日发布。针对特定发行版的已修复软件包也已提供：

* Debian：CVE 跟踪器位于 security-tracker.debian.org
* Ubuntu：Launchpad CVE 漏洞跟踪器
* Fedora 42–44：已在 PackageKit-1.3.4-3 中修复，由 Koji 提供

强烈建议系统管理员立即应用补丁，尤其是在运行 Cockpit 的面向互联网的服务器上。

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