---
title: 【漏洞通告】Linux Kernel ptrace 权限提升漏洞
url: https://mp.weixin.qq.com/s/x97x810gB4_vgAjnpQkKkg
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:01:36.132980
---

# 【漏洞通告】Linux Kernel ptrace 权限提升漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/APc6NwjLsxQ4ZEoksC4q6iaxcKYpklkmKyBHqwuvWFic0R50xSbEdibOgeTVn6If9ZzQuBRyHhvjHic8tVMgWcI1dbiccd8k4XyGjiahCwJzpUhlI/0?wx_fmt=jpeg)

# 【漏洞通告】Linux Kernel ptrace 权限提升漏洞

深瞳漏洞实验室
深瞳漏洞实验室

深信服千里目安全技术中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxThhm1Xb1hrxoHknIwY55jALK3RuJUaBYicwcUY5RRnNqpR6ysQFshMely7e2IDayaic41KE4KS6TzT7K038Kum59uy5v4NDaQq4/640?wx_fmt=gif&from=appmsg)

**漏洞名称：**

Linux Kernel ptrace 权限提升漏洞

**组件名称：**

Linux Kernel

**影响范围：**

commit version < 31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a（截至 2026 年 5 月18日全部稳定版本均受影响）

目前确定受影响的版本：

Raspberry Pi OS Bookworm 6.12.75

Debian 13

Ubuntu 22.04 / 24.04 / 26.04

Arch

CentOS 9

**漏洞类型：**

权限提升

**利用条件：**

1、用户认证：需要用户认证

2、前置条件：默认配置

3、触发方式：本地

**综合评价：**

<综合评定利用难度>：中等，需要本地低权限执行条件。

<综合评定威胁等级>：高危，可读取密码等高敏感文件。

**官方解决方案：**

已发布

**漏洞分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxQNg6FpS9KjKyx3p6q7D4EkeEWyLjT5qnjGQ1AVCyC5DYjGK9PMbcMP8Vl0pZcmQLqgflGkibqe6HhHzm7P0jnYY4B7nQEZPNm4/640?wx_fmt=gif&from=appmsg)

**组件介绍**

Linux内核（Linux Kernel）是一个开源的操作系统内核，它是Linux操作系统的核心组件，负责管理计算机的硬件资源，并提供了许多系统服务，如进程管理、内存管理、文件系统管理和设备驱动程序等。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTm6PyUrK9XIe5bYr8jWviccelpwFknZqAS0iaDUPZKmib1hT8QEHqOwOpmIWaMn6zQ1jB8ib2IL31GcUPlxqUsRtI1SRMYH8s2pQs/640?wx_fmt=gif&from=appmsg)

**漏洞简介**

2026年5月15日，深瞳漏洞实验室监测到一则Linux Kernel组件存在权限提升漏洞的信息，漏洞威胁等级：高危。

该漏洞核心在于ptrace\_may\_access()在目标进程内存映射为空（task->mm == NULL）时会跳过关键的 dumpable 安全检查；**进程退出时先调用exit\_mm()清空内存映射、再调用exit\_files()关闭文件描述符，这一顺序形成高危竞争窗口，同 UID 攻击者可通过pidfd\_getfd()窃取进程退出瞬间仍持有的打开文件描述符。**

深瞳漏洞实验室已成功复现Linux Kernel ptrace 权限提升漏洞(SF\_2026\_16430)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/APc6NwjLsxRO6lJYb8UYiaqQQb861NOR2P9ibVicHBza1GCDNsY1ege20xV328UcXpMferRpVnibqibERtqZPrJF4MwbGmu4Oe2LpAuTbicTnTibk0/640?wx_fmt=png&from=appmsg)

**影响范围**

目前受影响的Linux Kernel版本：

commit version < 31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a（截至 2026 年 5 月 14 日全部稳定版本均受影响）

目前确定受影响的版本：

Raspberry Pi OS Bookworm 6.12.75

Debian 13

Ubuntu 22.04 / 24.04 / 26.04

Arch

CentOS 9

**解决方案**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxRfX2LptFZJVl0T4Vu65kMTicQnat6Ej1KSoCFeQ6vdJ0GlxWiaT8PhchPhBqsRLyluddOOm0cAAuvsbOGFtcBJvKc2hAxlATjKA/640?wx_fmt=gif&from=appmsg)

**官方修复建议**

Linus Torvalds 已于 2026 年 5 月 14 日提交修复 commit 31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a。用户应尽快将内核升级至已包含此补丁的版本。
下载地址：
https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTyCeiaHUvKX4OcUIuoCxxRK8vrpYJqP0qWmYwR2gjOv00EHqb7hVUOPxURpUDdbmhFzXmQHC5Piabqez7mWsicRY3FC9NAlqoTh8/640?wx_fmt=gif&from=appmsg)

**临时修复建议**

执行以下代码将kernel.yama.ptrace\_scope设置为3能彻底阻止普通用户使用ptrace和pidfd\_getfd相关功能

echo "kernel.yama.ptrace\_scope = 3" | sudo tee /etc/sysctl.d/99-ptrace-restrict.conf

sudo sysctl -p /etc/sysctl.d/99-ptrace-restrict.conf

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxRxrjzURqIVTCL1nW6xiao4Fwbc9U4RF9TScFIM57qOcVmiaXA9O9hIu9wicx0YuicxeA8u4WnNtiaLl6Jju1gBv5rqRaAAF5qyOwVk/640?wx_fmt=gif&from=appmsg)

**深信服解决方案**

**漏洞主动检测**

支持对Linux Kernel ptrace 权限提升漏洞(SF\_2026\_16430)的主动检测，**可批量快速检出业务场景中是否存在漏洞风险，**相关产品如下：

**【深信服云镜YJ】**预计2026年05月30日发布检测方案，规则ID:SF-2026-00914。

**【深信服可拓展检测响应平台XDR】**预计2026年05月30日发布检测方案（需要具备云镜组件能力），规则ID:SF-2026-00914。

**参考链接**

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a

**时间轴**

**2026/05/15**

深瞳漏洞实验室监测到Linux Kernel ptrace 权限提升漏洞信息。

**2026/05/18**

深瞳漏洞实验室发布漏洞通告。

点击**阅读原文**，及时关注并登录深信服**智安全平台**，可轻松查询漏洞相关解决方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/APc6NwjLsxQ8xdcUrwueyia647WuwMLFicZP6cD7uHX0CvoSep7ebu77QWrWtY2NVXHrsnAUvs2KYIRvkGwAro6NwSHj5EUAvse0yrs5GPrsc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zvcIHbwGGYKbqDVYsVKzNNia1jYtHf49C7133AlDXAgex2W4lFvpia56tjQQDkiauNBrl08YbxqG01A/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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