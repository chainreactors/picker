---
title: 恶意广告通过伪造文本分享站点传播AMOS malext窃密木马来针对macOS用户
url: https://www.anquanke.com/post/id/315006
source: 安全客-有思想的安全新媒体
date: 2026-03-04
fetch_date: 2026-03-05T04:05:45.839869
---

# 恶意广告通过伪造文本分享站点传播AMOS malext窃密木马来针对macOS用户

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 恶意广告通过伪造文本分享站点传播AMOS malext窃密木马来针对macOS用户

阅读量**19560**

发布时间 : 2026-03-04 10:33:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/amos-malext-macos-infostealer/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场大规模**恶意广告攻击**正针对 macOS 用户展开：攻击者利用伪造的谷歌广告，将用户导向恶意文本分享网站，并投放名为 **malext** 的 **AMOS 窃密木马变种**，窃取浏览器凭证、加密货币钱包等敏感数据。

可疑的密码输入弹窗暴露了此次攻击，关联到的初始域名包括：

`optimize-storage-mac-os.medium.com`、`octopox.com`、`vagturk.com`。

谷歌广告库显示，超过 **34 条广告**伪装成 Medium 文章进行诱骗，攻击者在账号被封后会迅速更换新账号。

分析发现至少 **53 个**被入侵的广告账号，其中甚至有账号同时推广邮轮广告与虚假 macOS 修复工具。

类似恶意广告还出现在 Evernote、mssg.me、[kimi.com](https://kimi.com) 等平台。

安全研究者 @itspappy 与 Gi7w0rm 在一次险些中招的事件后揭露了该攻击链：

一名用户搜索 macOS 存储修复工具时，点击了谷歌置顶结果，进入一篇伪造的 Medium 文章，其中包含恶意 Shell 命令。

![]()

诱饵页面高度模仿 macOS 故障排查指南或软件安装教程，标题类似 “此方法可修复 X 问题”，并诱导用户复制粘贴终端命令。

攻击链使用 **Base64 混淆的 curl** 命令逐级下载载荷，并通过 `xattr -c` 移除隔离属性，**绕过 Gatekeeper 防护**。

部分攻击链会通过循环弹窗**骗取管理员密码**，将密码保存在 `~/.pass`，供后续提权使用。

这种社会工程学手段可在无系统告警的情况下提升载荷执行成功率。

---

## 攻击链分析

攻击者下载的是同时支持 **x86\_64 与 ARM 架构**的 Mach‑O 二进制文件。

样本通过混淆的 AppleScript 执行虚拟机 / 沙箱检测，使用 `system_profiler` 判断 QEMU/VMware 环境或异常硬件特征。

在 VirusTotal 运行的已修补样本中，暴露出一段超过 **59000 字符**的 `osascript` 载荷。

去混淆后可见代码使用**凯撒密码加密字符串**与随机变量名。

脚本会隐藏终端窗口，收集系统信息，并通过 `malext.com` 或 `38.244.158.56` 外发数据。

![]()

**malext** 作为 AMOS 变种，窃取范围极广：

* Apple Notes 数据库
* Safari Cookie
* 桌面 / 文档目录文件（txt/pdf/docx/wallet，上限 30MB）
* OpenVPN 配置文件
* Telegram 数据
* 已安装应用列表

该恶意软件的特殊之处在于：

**单个 Mach‑O 文件内同时打包了两种不同 CPU 架构的攻击载荷**。

![]()

**malext** 作为 AMOS 变种，窃取范围极广：

* Apple Notes 数据库
* Safari Cookie
* 桌面 / 文档目录文件（txt/pdf/docx/wallet，上限 30MB）
* OpenVPN 配置文件
* Telegram 数据
* 已安装应用列表

该恶意软件的特殊之处在于：

**单个 Mach‑O 文件内同时打包了两种不同 CPU 架构的攻击载荷**。

![]()

| 功能 | 说明 | 攻击目标 |
| --- | --- | --- |
| 数据窃取 | 浏览器、钱包、密钥链、文件 | Chrome、Electrum、备忘录 |
| 对抗检测 | 虚拟机检测、xattr -c、gzip/Base64 | Gatekeeper、沙箱 |
| 持久化 | LaunchDaemon、木马化应用 | `~/.agent`、Ledger |
| C2 服务器 | HTTP POST 重试、备用 IP | `malext.com`、199.217.98.33 |

多项特征（`com.finder.helper.plist`、BuildID 头、`/zxc` 路径等）表明该家族属于 **AMOS**，而非 Odyssey。

该活动从 **2025 年底**开始活跃，依靠大量廉价一次性账号扩张，疑似由流量团伙运营。

本文翻译自gbhackers [原文链接](https://gbhackers.com/amos-malext-macos-infostealer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315006](/post/id/315006)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/amos-malext-macos-infostealer/)

如若转载,请注明出处： <https://gbhackers.com/amos-malext-macos-infostealer/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

### 热门推荐

文章目录

* [攻击链分析](#h2-0)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)