---
title: 【已复现】Linux Kernel Dirty Frag 本地权限提升漏洞
url: https://mp.weixin.qq.com/s/OVq7H4MiUBckIG_bHSDdEw
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:06:52.776727
---

# 【已复现】Linux Kernel Dirty Frag 本地权限提升漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P5dz00jGoyR1d52JRaLmOVtWhibcHAPcfRTQicPsUMIHt0icKp5AS1NOxph9D0wf2gU9UaDh0B6O25ImPMDiaeMO4ejsAuicD48PoMic19zG04bBQ/0?wx_fmt=jpeg)

# 【已复现】Linux Kernel Dirty Frag 本地权限提升漏洞

安恒CERT
安恒CERT

安恒信息CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![安恒信息安全通告](https://mmbiz.qpic.cn/sz_mmbiz_png/P5dz00jGoyRJer7FFHBSKYU8MhfJayX59Fq5ZBeuSTibjcjIBwu5nDtPVQASvYVOd4Knb3TWC2TfRuicOROkiaicrYoUnPiaHxrgyBR8ia9wEbHhE/640?from=appmsg)

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Linux Kernel Dirty Frag 本地权限提升漏洞 | | |
| **安恒CERT评级** | 2级 | **CVSS3.1评分** | 7.8 |
| **CVE编号** | 未分配 | **CNVD编号** | 未分配 |
| **CNNVD编号** | 未分配 | **安恒CERT编号** | WM-202605-000001 |
| **POC情况** | 已发现 | **EXP情况** | 未发现 |
| **在野利用** | 未发现 | **研究情况** | 已复现 |
| **危害描述** | 该漏洞源于 xfrm-ESP（自2017年）和RxRPC（自2023年）两个独立模块的逻辑缺陷，攻击者可以实现对页缓存的写入，从而在几乎所有主流Linux发行版上稳定提权。 | | |

该产品主要使用客户行业分布广泛，漏洞危害性极高，建议客户尽快做好自查及防护。

**安恒研究院卫兵实验室已通过恒脑AI代码审计智能体复现此漏洞。**

![screenshot](https://mmbiz.qpic.cn/mmbiz_jpg/P5dz00jGoyTsEgWNRbqrDVNrOG4Io8jEg0oLwWw6hUnhDf8NZwrkibtJHc9QSHcDOF06yTs6rbsJWvaYXXsIMsc1dLwVEGQzVocHqrnPG1yk/640?from=appmsg)

**漏洞信息**

Linux 内核是 Linux 操作系统的核心组件，负责进程调度、内存管理、网络协议栈和驱动管理等功能。

**漏洞描述**

**漏洞危害等级：**高危

**漏洞类型：**内存缓冲区操作限制不当

**影响范围**

**影响版本：**xfrm-ESP: cac2661c53f3 (2017-01-17) 至今所有上游内核；RxRPC: 2dc334f1a63a (2023-06) 至今所有上游内核。已知受影响发行版版本包括：Ubuntu 24.04.4 (6.17.0-23-generic)、RHEL 10.1 (6.12.0-124.49.1.el10\_1.x86\_64)、openSUSE Tumbleweed (7.0.2-1-default)、CentOS Stream 10 (6.12.0-224.el10.x86\_64)、AlmaLinux 10 (6.12.0-124.52.3.el10\_1.x86\_64)、Fedora 44 (6.19.14-300.fc44.x86\_64)

**CVSS向量**

访问途径（AV）：本地

攻击复杂度（AC）：低

所需权限（PR）：低

用户交互（UI）：不需要用户交互

影响范围（S）：不变

机密性影响（C）：高

完整性影响（I）：高

可用性影响（A）：高

**修复方案**

**官方修复方案**

官方暂未发布补丁。上游内核已合入修复补丁，在 espinput/esp6input 的 skipcow 分支中检查 SKBFLSHAREDFRAG 标志，确保 splice 引入的外部固定页始终进入 skbcowdata 路径，阻止攻击者固定的页缓存页进入就地 AEAD 的目标 SGL。修复补丁 commit: f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4。各发行版 backport 后请及时更新至最新版本。

信息来源：https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4

**临时缓解方案**

临时缓解方案（基于漏洞暴露面的保守缓解）：可通过禁用存在漏洞的内核模块来防止漏洞被利用。执行以下命令禁用 esp4、esp6 和 rxrpc 模块：sh -c "printf &#x27;install esp4 /bin/false install esp6 /bin/false install rxrpc /bin/false &#x27; > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true"。注意：禁用这些模块可能会影响 IPsec ESP 加密和 RxRPC 远程过程调用功能。

信息来源：https://www.openwall.com/lists/oss-security/2026/05/07/8

**参考资料**

https://www.openwall.com/lists/oss-security/2026/05/07/8

https://github.com/V4bel/dirtyfrag

https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/id=f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4

**产品能力覆盖**

|  |  |
| --- | --- |
| **产品名称** | **覆盖补丁包** |
| 明鉴漏洞扫描系统 | V1.0.3778.0及以上 |

**技术支持**

如有漏洞相关需求支持请联系400-6059-110获取相关能力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Qiao60gtLmwVcoDMnCe4IdPoVDPOdqoc7brmYf1OS0B11CjaFfmbP2PjSbSmyFJYvCqoVr9cNkDibZriaTicYCnRVQ/0?wx_fmt=png)

安恒信息CERT

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Qiao60gtLmwVcoDMnCe4IdPoVDPOdqoc7brmYf1OS0B11CjaFfmbP2PjSbSmyFJYvCqoVr9cNkDibZriaTicYCnRVQ/0?wx_fmt=png)

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