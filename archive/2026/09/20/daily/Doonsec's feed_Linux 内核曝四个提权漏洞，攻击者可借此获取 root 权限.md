---
title: Linux 内核曝四个提权漏洞，攻击者可借此获取 root 权限
url: https://mp.weixin.qq.com/s/Euc-zl-ioMRCVfYQoFNPhg
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:25:23.729563
---

# Linux 内核曝四个提权漏洞，攻击者可借此获取 root 权限

# Linux 内核曝四个提权漏洞，攻击者可借此获取 root 权限

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnu5XETDicz5ia0Mwib27lFqREib3Lvp908WcLLcsShy18A4Lw8R9yHGLBnX4J6QvvguGb8KnmXuoCCBAUOrkBTu2ibKPqnc97PxUOkA/640?wx_fmt=png&from=appmsg)

最新披露的四个 Linux 内核漏洞，可能让本地攻击者破坏内核内存，并在受影响系统上将权限提升至 root。

这些漏洞分别被命名为 DirtyAH6、TUNderflow、PPPoEject 和 DiagSpill，均存在于长期使用的网络代码中，目前上游已提供修复。对应的 CVE 编号为 CVE-2026-80844、CVE-2026-81000、CVE-2026-68121 和 CVE-2026-74469。

### DirtyAH6：IPv6 认证头处理越界

DirtyAH6（CVE-2026-80844）影响 Linux IPsec/XFRM 代码中的 IPv6 认证头处理。当内核处理格式异常的 IPv6 路由头值时，未能正确校验 segments\_left 字段，导致内部指针偏移到预期内存区域之外，触发越界内存操作。

该漏洞主要是一个本地提权问题——前提是攻击者能够创建或控制合适的网络命名空间。不过，在特定条件下，作为 IPv6 路由器或网关并使用传输模式 AH 的系统，也可能面临远程拒绝服务风险。

研究人员在实验室环境中通过内存布局整理（memory grooming）演示了远程获取 root 权限的过程，但也指出纯远程攻击的实现难度极高。

### TUNderflow：TUN/TAP 子系统整数下溢

TUNderflow（CVE-2026-81000）存在于 TUN/TAP 虚拟网络设备子系统中。恶意本地用户可利用特定网络设备配置（包括 Open vSwitch 路径）传入过大的接收头空间值，从而触发漏洞。

该错误会在套接字缓冲区分配时引发整数下溢，使数据包数据落到分配区域之外，进而造成越界读写。

### PPPoEject：PPPoE 释放后重用

PPPoEject（CVE-2026-68121）是 Linux PPP over Ethernet 实现中的释放后重用（use-after-free）漏洞。pppoe\_sendmsg() 函数在调用下层设备头函数时，仍保留着指向 PPPoE 头的指针。

而该回调操作可能重新分配套接字缓冲区，使原指针失效。后续通过悬空指针进行的写入，可能破坏已被释放的内核内存。上游补丁的做法是在创建设备头之后重新加载头指针。

### DiagSpill：SCTP 诊断报告缓冲区溢出

DiagSpill（CVE-2026-74469）影响通过 sock\_diag 的 SCTP 诊断报告功能。一个 SCTP 关联最多可包含 65536 个对端传输对象，但相关计数器仅有 16 位宽。

当计数达到上限时会回绕归零，导致诊断代码在拷贝对端信息前预留的空间不足，最终产生的溢出会远远超出预期的 Netlink 响应缓冲区范围。

与前三个漏洞不同，只要系统支持 SCTP 和 sctp\_diag，DiagSpill 就不需要非特权用户命名空间或特殊的 Linux 能力（capabilities）。此外，若启用了 SCTP 地址配置功能，还可能存在远程触发崩溃的条件，但该功能默认处于关闭状态。

### 修复与缓解建议

应升级到包含全部四项修复的内核版本。首批完整修复这四个问题的稳定版本为：Linux 5.10.270、5.15.221、6.1.188、6.6.157、6.12.109、6.18.50 和 7.2.4。

若无法立即打补丁，组织应限制非特权用户命名空间，并禁用未使用的 AH6、TUN/TAP、PPPoE、SCTP 或 sctp\_diag 功能。但需注意，关闭用户命名空间无法缓解 DiagSpill，不能替代应用厂商的内核更新。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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