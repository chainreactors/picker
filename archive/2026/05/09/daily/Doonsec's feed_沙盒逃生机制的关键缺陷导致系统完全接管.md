---
title: 沙盒逃生机制的关键缺陷导致系统完全接管
url: https://mp.weixin.qq.com/s/ZmTGecqEmxQg6Log1KPY1Q
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:31.587711
---

# 沙盒逃生机制的关键缺陷导致系统完全接管

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/y1BJgHFkOkriaoeJEtAqY8KEksA4X9ztOQMWVMBbaH5D4P40uHTWMhPiaCbBWOB60FD3zspueTkReJembXr20iaAmZeMGhxtRqzDuEL3MAU8Q8/0?wx_fmt=jpeg)

# 沙盒逃生机制的关键缺陷导致系统完全接管

sec随谈
sec随谈

sec随谈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

多年来，安全专家和普通技术用户都依赖 Sandboxie 作为一道坚不可摧的屏障——一个安全的运行环境，可以在不永久修改本地驱动器或 Windows 注册表的情况下，清除不受信任的应用程序。然而，这道屏障如今已被打破。

安全研究人员披露了 Sandboxie 架构中的两个灾难性**漏洞**。这些漏洞不仅绕过了软件的保护机制，而且还使沙箱本身成为攻击目标，为攻击者提供了一条直接且隐蔽的系统完全控制途径。

第一个**漏洞**（CVE-2026-34459）是 SbieSvc 代理服务中存在的未初始化内存泄漏和堆栈缓冲区溢出的组合漏洞。

在处理特定的进程间通信 (IPC) 消息时，恶意沙箱进程可以发送人为夸大的请求，诱使代理服务器将高达 32KB 的未初始化堆栈内存转储回不受信任的客户端。这是一个严重的架构缺陷。

正如公告中所述，“这种大规模内存转储可靠地暴露了返回地址（绕过 ASLR）和残留堆栈 cookie（绕过/GS）。”

有了泄露的内存映射，攻击者就可以触发攻击的第二阶段：发送一个超大的有效载荷，完美地恢复堆栈 cookie，同时用恶意的面向返回编程 (ROP) 链覆盖保存的返回地址。

该安全公告警告说：“即使在经过安全加固的沙箱中，无需用户交互即可逃逸沙箱并提升到 SYSTEM 权限（无需 UAC），也是可能影响软件的最严重漏洞。”

关于现代硬件防御的说明：虽然使用英特尔控制流强制技术 (CET) 的环境可以阻止 ROP 链的执行，但 32KB 内存泄漏仍然完全可利用，为高级威胁行为者提供了必要的内存原语，从而有可能设计出 CET 绕过。

第二个漏洞，编号为CVE-2026-34458，此 INI 注入漏洞允许任何未经身份验证或标准本地用户完全绕过严格的配置限制，例如 EditAdminOnly 和 ConfigPassword。

**Sandboxie-Plus的缺陷**在于其处理后台服务 IPC 消息的方式。为了允许普通用户在无需管理员权限的情况下管理自己的设置，如果设置项以 UserSettings\_ 开头，软件会跳过授权检查。然而，负责添加或设置这些配置的函数完全没有对输入进行回车换行符 (CRLF) 的清理。

攻击者可以通过注入 CRLF (\r\n) 序列来操纵 Sandboxie.ini 文件的解析。该安全公告强调了关键的故障点：“由于输入未经清理，攻击者可以提供包含新节头的有效载荷，从而完全突破受限的 [UserSettings\_…] 块。”

下次重新加载配置时，软件会解析新注入的这部分代码，从而允许攻击者定义一个完全不受限制的恶意沙箱环境。这提供了一条简单的逃逸路径，可以直接进行任意文件写入并提升至完整的 SYSTEM 权限。

任何在沙箱内运行的受感染进程都可以利用这些漏洞利用链突破防线，并完全控制宿主操作系统。

Sandboxie 1.17.2 及更早版本存在漏洞。所有用户和企业管理员必须立即将其部署的 Sandboxie 更新到1.17.3版本，该版本修复了这两个关键**漏洞**。

参考链接：

https://github.com/sandboxie-plus/Sandboxie/security/advisories/GHSA-7cpc-5hv7-rfmh

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bziakiaSIiab3gicgEN5oibyibqGbjykE3b4sDfuWj0RZXsWhP7mg3YaIjklIlBbHxma0EZ5WicksaTehmL4g/0?wx_fmt=png)

sec随谈

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bziakiaSIiab3gicgEN5oibyibqGbjykE3b4sDfuWj0RZXsWhP7mg3YaIjklIlBbHxma0EZ5WicksaTehmL4g/0?wx_fmt=png)

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