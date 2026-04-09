---
title: CUPS漏洞链使远程攻击者能够以root用户身份执行恶意代码
url: https://mp.weixin.qq.com/s/Wxubco1gpR9_ESvdn3g3YA
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:28.490438
---

# CUPS漏洞链使远程攻击者能够以root用户身份执行恶意代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PggyddSMwl7FWE3KtS7vBns1bGiaLmWoLOjXibJF9am3lUDE4NhxiboiaApAYDHIX4371ic3KN2d5ozU50jSffwib3k2e9n9f06BsjE/0?wx_fmt=jpeg)

# CUPS漏洞链使远程攻击者能够以root用户身份执行恶意代码

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

通用 Unix 打印系统 (CUPS)中存在一个关键漏洞链，允许未经身份验证的远程攻击者以 root 系统权限执行任意恶意代码。

安全研究员 Asim Viladi Oglu Manizada 和他的团队发现了两个零日漏洞，官方编号分别为 CVE-2026-34980 和 CVE-2026-34990，影响 CUPS 2.4.16 及更早版本。

这种复杂的攻击链通过利用遗留的打印队列和操纵本地主机身份验证机制，将网络入侵升级为对整个系统的完全控制 。

## **使用传统队列绕过身份验证**

攻击的第一阶段利用了 CVE-2026-34980，目标是 CUPS 服务器的默认策略，该策略允许在通过网络公开共享的 PostScript 队列时接受匿名打印作业。

通过向该队列发送恶意构造的打印请求，远程攻击者可以绕过身份验证层并操纵内部队列配置。

该漏洞源于解析错误，作业属性中嵌入的换行符在系统的转义过程中得以保留，从而允许攻击者将恶意命令偷偷植入受信任的调度程序控制记录中。

将恶意过滤器条目注入 PostScript 打印机描述文件中，即可授予攻击者以非特权“lp”服务用户身份执行远程代码的能力。

一旦获得初始访问权限，威胁行为者就会利用第二个漏洞 CVE-2026-34990 将权限从受感染的“lp”用户提升到完全 root 访问权限。

默认策略允许任何低权限帐户命令 CUPS 服务在本地主机接口上创建临时本地打印机，而无需管理员批准。

攻击者通过设置恶意伪造打印机监听器，拦截设置过程，并强迫 CUPS 守护程序使用可重用的本地授权令牌进行身份验证。

攻击者利用窃取的管理员令牌，利用竞争条件绕过正常的设备 URI 限制，将临时打印机转换为直接指向敏感系统文件路径的持久队列，从而导致任意根文件覆盖。

截至 2026 年 4 月初，还没有官方软件补丁可以解决这些漏洞。

然而，最初的远程代码执行缺陷需要刻意选择通过网络公开共享的 PostScript 队列。

为了缓解这种威胁，管理员应该禁用共享的旧式队列，限制 CUPS 守护程序的网络暴露，或者对所有打印作业提交强制执行严格的身份验证，正如 heyitsas 所强调的那样。

在 AppArmor 或 SELinux 等强大的强制访问控制系统下运行 CUPS 服务，还可以防止受感染的进程在其安全环境之外修改关键文件，从而限制影响范围。

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