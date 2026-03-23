---
title: CrackArmor 严重漏洞使 1260 万台 Linux 服务器面临完全 root 权限被控制的风险
url: https://mp.weixin.qq.com/s/srhONdrYItujLCFzjBNECw
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:29.991696
---

# CrackArmor 严重漏洞使 1260 万台 Linux 服务器面临完全 root 权限被控制的风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EoVWMDZd6EYnvcF6qd2Hl6sZgzAjvR4CB7RicUoJvVBWhgUiclia4RIicKORJVxxhLWwLGDpOiaBGH27bEGN7XmRUSI46jiaJJJz4oaS4PS0wAjc/0?wx_fmt=jpeg)

# CrackArmor 严重漏洞使 1260 万台 Linux 服务器面临完全 root 权限被控制的风险

TtTeam

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EoVWMDZd6GXkab7P9GVfFd4K0cpo4sBuI8Ev83nXtPWlScicKs3l7OYFuRkmpe7Y1HwugvtjlDMMFEmTibib1cobDxicDdRzZezu4VO3ZwJe0o/640?wx_fmt=png&from=appmsg)

AppArmor 旨在通过限制单个应用程序的特定功能（而不是广泛的用户帐户）来强制执行零信任状态。

CrackArmor 利用了这种架构中的“混淆代理”漏洞。非特权攻击者无法直接修改系统安全策略，但他们可以操纵受信任的高权限工具（例如 Sudo 或 Postfix）来代表自己执行操作。

![](https://mmbiz.qpic.cn/mmbiz_png/5EoVWMDZd6FcpdEFuhvnxEwsTcRCAXdBSzcD64M28eZhQJHCezdEHVwOqpjuK8t2q2uoa8k5WNjWQTUicFmVood3Fkdo4ZoQSn57mlt2MoWk/640?wx_fmt=png&from=appmsg)

通过欺骗这些受信任的进程，攻击者可以写入位于 AppArmor 内核目录中的受保护的伪文件，从而绕过用户命名空间限制。

这类似于入侵者说服拥有万能钥匙的楼宇管理员打开受限金库。

由于根本问题是内核模块代码中的实现错误，而不是强制访问控制模型本身的缺陷，因此安全边界会静默失效。

当攻击者成功篡改这些 AppArmor 配置文件时，整个安全体系就会崩溃。主要技术后果包括：

本地权限提升 (LPE)： 攻击者可以绕过命名空间限制来获取 root 权限。在用户空间，拒绝 Sudo 的特定权限可以强制 Postfix 以 root 身份执行命令。在内核空间，释放后使用漏洞允许攻击者覆盖系统密码文件中的 root 密码行。

拒绝服务攻击 (DoS)： 攻击者通过创建深度嵌套的子配置文件，可以在移除配置文件时强制内核耗尽其堆栈内存。这种溢出会导致内核崩溃和系统完全重启。

容器突破： 加载特定的命名空间配置文件允许非特权用户创建功能齐全的环境，从而突破标准容器隔离限制。

安全降级： 攻击者可以移除关键后台服务的保护措施，使其容易受到远程攻击，或者加载“拒绝所有访问”配置文件来阻止合法的管理员访问权限。

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