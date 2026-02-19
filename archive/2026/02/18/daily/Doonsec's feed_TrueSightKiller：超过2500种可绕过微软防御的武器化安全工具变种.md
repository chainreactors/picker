---
title: TrueSightKiller：超过2500种可绕过微软防御的武器化安全工具变种
url: https://mp.weixin.qq.com/s/APX18AbVDAW5SnhN7O8WLg
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:15:44.525014
---

# TrueSightKiller：超过2500种可绕过微软防御的武器化安全工具变种

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0HlywncJbB12TK1TY95XXHmmicMYSSusdLv5LrjyBzC5zM6gUjian1Eia1IMRD93ialowxibgwKnNQpZHg4JwMBKXyQ/0?wx_fmt=jpeg)

# TrueSightKiller：超过2500种可绕过微软防御的武器化安全工具变种

TtTeam

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB12TK1TY95XXHmmicMYSSusdn2Dg84BpLP1fBI12kcWXGQgmSeZ3cOXTabndfrd5aDxbiaPZfNMARhA/640?wx_fmt=png&from=appmsg)

一场大规模的攻击活动正在利用一款合法的安全工具来破坏您的防御系统。超过2500 个经过有效签名的 truesight.sys 驱动程序变种（该驱动程序是 Adlice Software 公司 RogueKiller 防病毒套件的一个组件）正被攻击者利用，在部署勒索软件和远程访问木马之前，破坏终端安全防护。

讽刺的是，一款旨在保护系统免受恶意软件侵害的驱动程序，如今却成了摧毁安全软件的主要武器。

Check Point Research 于 2025 年 1 月发现了这一攻击活动，并记录了攻击者如何利用 Windows 驱动程序签名策略漏洞，允许 2015 年之前签名的驱动程序加载到现代 Windows 11 系统上。

关键事实：

* 超过 2500 个具有有效数字签名的独特变体
* 通过证书篡改绕过微软的易受攻击驱动程序阻止列表
* 自 2024 年 6 月起开始运营，每周都有新样本发布。
* 包括 Silver Fox、勒索软件组织和 APT 在内的多个威胁行为者
* 97%的自动驾驶飞机规避率——73台发动机中只有2台检测到

MagicSword 正在积极监控这一威胁，并提供实时情报，以帮助防御者阻止这些攻击。

攻击原理

武器化安全工具

TrueSight.sys 是Adlice Software 旗下 RogueKiller 防病毒软件的合法内核模式驱动程序，RogueKiller 是全球安全专家广泛使用的工具。但其旧版本 2.0.2 存在一个严重漏洞：可任意终止进程。

攻击者发现，他们可以发送特定的 IOCTL 命令 (0x22E044) 来终止系统上的任何进程，包括通常无法从用户模式终止的受保护安全软件。

攻击链

初步妥协：

```
带有恶意附件的网络钓鱼邮件虚假网站提供合法软件被入侵的 Telegram 频道水坑袭击
```

多阶段部署：

第一阶段：伪装成合法安装程序的下载器

第二阶段：通过计划任务建立持久性，使用 DLL 侧加载

第三阶段：部署 EDR 杀手模块 + 最终有效载荷（Gh0st RAT）

EDR杀手模块：

Check Point 的研究人员发现了一个复杂的模块（受 VMProtect 保护），该模块针对192 个安全产品进程，其中包括：

CrowdStrike Falcon、哨兵一号、Sophos Endpoint、趋势科技、卡巴斯基、ESET、赛门铁克、迈克菲以及其他184人

模块的操作：

```
如果 TrueSight 驱动程序尚未安装，请下载该驱动程序。将驱动程序安装为名为 TCLService 的服务。发送 IOCTL 以终止所有目标安全进程从磁盘中删除安全软件部署最终有效载荷，防御系统完全无法察觉。
```

从最初妥协到完全控制所需时间：仅需 30 分钟。

技术诀窍：为什么传统防御会失败

证书篡改

攻击者并非使用未签名的恶意软件或被盗证书，而是通过操纵有效签名的驱动程序来绕过所有传统防御措施。

Check Point 的分析显示，攻击者仅修改了驱动程序中的8 个字节：

```
4 字节：校验和字段（证书检查期间不进行验证）4 字节：证书填充（加密签名数据之外）
```

这样可以生成2^64 个可能的唯一文件哈希值，同时保持驱动程序的有效数字签名。

微软的黑名单差距

微软的易受攻击驱动程序黑名单使用待签名（TBS）哈希值来阻止恶意证书。TrueSight 证书的 TBS 哈希值

(1D7E838ACCD498C2E5BA9373AF819EC097BB955C)已在微软的黑名单中，但它与不同的易受攻击驱动程序（例如 Kaspersky 和 Zemana）相关联。

屏蔽列表条目并未明确提及 truesight.sys，因此 2.0.2 版本得以漏网。微软直到2024 年 12 月 17 日才弥补这一漏洞，此时距离此次攻击活动开始已过去了六个月。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

TtTeam

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

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