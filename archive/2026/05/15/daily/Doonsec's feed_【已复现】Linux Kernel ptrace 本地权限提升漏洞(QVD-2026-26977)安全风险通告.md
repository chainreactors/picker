---
title: 【已复现】Linux Kernel ptrace 本地权限提升漏洞(QVD-2026-26977)安全风险通告
url: https://mp.weixin.qq.com/s/SIs8VZVo_vnjeVuBB7NGsA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:17.336421
---

# 【已复现】Linux Kernel ptrace 本地权限提升漏洞(QVD-2026-26977)安全风险通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555sCS5F4aUEEkGDrVTyWldCq6a0n7S66iaf4DBCnq2ibic0Dib6UlK8x8Zh4ZZmHQu0BQfTIxEjPNDmS7J7nvwoL1v7caftlicFQ8Ncs/0?wx_fmt=jpeg)

# 【已复现】Linux Kernel ptrace 本地权限提升漏洞(QVD-2026-26977)安全风险通告

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Linux Kernel ptrace 本地权限提升漏洞 | | |
| **漏洞编号** | QVD-2026-26977 | | |
| ****公开时间**** | 2026-05-14 | ****影响量级**** | 百万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **7.8** |
| **威胁类型** | 权限提升、信息泄露 | **利用可能性** | ****高**** |
| **POC状态** | **已公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **已公开** | **技术细节状态** | **已公开** |
| **危害描述：**本地低权限攻击者可利用 pidfd\_getfd 窃取高权限文件描述符，读取 /etc/shadow 和 SSH 主机私钥等敏感文件并实现权限提升。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

Linux 内核是一款开源的类 UNIX 操作系统内核，作为 Linux 系统的核心组件，负责管理系统硬件资源、进程调度、内存管理、文件系统与网络通信等核心功能，为各类应用程序提供底层支撑与系统调用接口。其广泛应用于服务器、桌面终端、移动设备、嵌入式系统与云计算环境，是全球主流 IT 基础设施的核心运行载体，具备高稳定性、高可移植性与高扩展性，支持多架构、多任务与多用户并发运行，支撑着互联网、金融、政企、云计算等关键领域的业务系统稳定运转。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复Linux Kernel ptrace 本地权限提升漏洞(QVD-2026-26977)，该漏洞源于 Linux Kernel 的 ptrace\_may\_access 权限校验逻辑中，因进程退出时 exit\_mm 与 exit\_files 的执行顺序存在竞态窗口，且 task->mm 为 NULL 时会跳过 dumpable 检查，导致本地低权限攻击者可利用 pidfd\_getfd 窃取高权限文件描述符，读取 /etc/shadow 和 SSH 主机私钥等敏感文件并实现权限提升。目前该漏洞PoC和技术细节已公开。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

未应用 commit 31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a 之前的所有 Linux 内核版本（截至2026年5月14日的所有稳定版本均受影响）

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现Linux Kernel ptrace 本地权限提升漏洞(QVD-2026-26977)，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555vy5zQLtI3picx0mfepia2tRNAhsLwJSf2Y1ofp49ck8ia0tZAB7zZhzxza5G7a1y0iaoq5kbicfSdYEuIZzpwk2IFZbTf56QbnbxWw/640?wx_fmt=png&from=appmsg)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

官方暂未发布补丁，请及时关注并更新至最新版本

Linus Torvalds 已于 2026 年 5 月 14 日提交修复 commit 31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a。用户应尽快将内核升级至已包含此补丁的版本。

下载地址：

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a

临时缓解方案：

禁用不必要的 setuid 辅助程序、限制 pidfd\_getfd 使用（如通过 seccomp 或AppArmor/SELinux 策略）。

**05**

**参考资料**

[1]https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a

[2]https://securityonline.info/linux-kernel-ptrace-vulnerability-poc-public-disclosure-root-file-theft/

**06**

**时间线**

2026年05月15日，奇安信 CERT发布安全风险通告。

**07**

**漏洞情报服务**

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BY9IJ0MPzeiashvK2XLpdl3XtTtCD91h0jS26fqvuWpEMXgmXa85qLkoA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3 "漏洞订阅上线.png")

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=5 "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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