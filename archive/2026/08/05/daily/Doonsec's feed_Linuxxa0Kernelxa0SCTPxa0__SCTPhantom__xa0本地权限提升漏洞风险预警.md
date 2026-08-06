---
title: Linuxxa0Kernelxa0SCTPxa0\"SCTPhantom\"xa0本地权限提升漏洞风险预警
url: https://mp.weixin.qq.com/s/lu1ihodwp1bq45U235uT4A
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T04:58:49.848583
---

# Linuxxa0Kernelxa0SCTPxa0\"SCTPhantom\"xa0本地权限提升漏洞风险预警

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VL7Qr6N3skg64n8ODibBjB8ZwpQOYIxw4c5aW28iaEaghkrWbmIS895icIPutO4UE0OhYbMqYK2up6q6t7lxh3iacR7D2ao8LT2ibv3Q8GH9mvwU/0?wx_fmt=jpeg)

# Linux Kernel SCTP "SCTPhantom" 本地权限提升漏洞风险预警

云鼎实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 概述

Linux Kernel 是全球最广泛使用的开源操作系统内核，负责管理硬件资源、进程调度、内存管理、文件系统和网络功能等底层任务。其中，SCTP（Stream Control Transmission Protocol）是 Linux 内核中的传输层协议，支持多宿主和动态地址重配置（ASCONF），被部分电信信令业务等场景广泛采用。

TencentOS安全团队在 Linux 内核的 SCTP 协议处理模块中发现存在本地权限提升漏洞，漏洞编号 **CVE-2026-64564**，代号"SCTPhantom"。该漏洞可导致本地攻击者通过构造特制的 SCTP 数据包，触发内核访问已释放的内存，从而实现本地权限提升或容器逃逸等危害，风险等级为高风险。建议受影响用户立即开展安全自查，并及时进行更新修复。

## 漏洞详情

| 字段 | 内容 |
| --- | --- |
| 漏洞名称 | Linux Kernel SCTP 本地权限提升漏洞 |
| 漏洞编号 | **CVE-2026-64564** |
| 漏洞代号 | SCTPhantom |
| 危害等级 | 高风险 |
| 漏洞类型 | 内存释放后使用（Use-After-Free，UAF） |
| 影响范围 | Linux Kernel >= 2.6.25，< commit 9b2854f |
| 参考链接 | https://git.kernel.org/stable/c/9b2854f86f0b56e9027d68e7a3fc909d1a9b566f |

在 Linux 内核 SCTP 协议处理中，`sctp_process_asconf()` 函数在处理 ASCONF 块时，将 `asconf->transport` 缓存为当前处理该块的传输控制块。当 `__sctp_rcv_asconf_lookup()` 通过地址参数定位 ASCONF 块时，缓存的传输控制块可能与数据包源地址对应的传输控制块不一致。

攻击者可构造包含顺序执行的 ASCONF 参数：首先对非源地址的地址 L 执行 DEL-IP（通过 D8 检查），释放 `asconf->transport` 指向的传输控制块；随后执行通配符 DEL-IP（0.0.0.0），此时 `asconf->transport` 已为悬空指针，后续在 `sctp_assoc_set_primary()` 和 `sctp_assoc_del_nonprimary_peers()` 中重用该悬空指针，从而触发内存释放后使用（UAF），最终实现本地权限提升或容器逃逸。

## 影响版本

受影响版本：

* Linux Kernel >= 2.6.25，< commit 9b2854f

目前已知受影响的操作系统：

* TencentOS Server 2.4
* TencentOS Server 2.6
* TencentOS Server 3.1
* TencentOS Server 3.2
* TencentOS Server 3.3
* TencentOS Server 4.4
* TencentOS Server 4.5
* Debian 14
* Debian 13
* Debian 12
* Debian 11
* Ubuntu 24.04 LTS

安全版本：

* Linux Kernel >= commit 9b2854f
* TencentOS Server 官方发布的安全补丁

## 排查方法

1. 检查所使用的 Linux Kernel 版本：

```
uname -r
```

2. 确认 sctp 模块的加载状态（若命令无任何输出，说明 sctp 模块未加载，则当前环境不受该漏洞影响）：

```
lsmod | grep sctp
```

## 处置建议

官方已发布漏洞补丁，建议评估业务是否受影响后，升级至安全版本。

### 修复方案（推荐）

针对 TencentOS Server，官方已将修复补丁合入各分支内核仓库，执行以下命令更新：

```
yum update kernel -y && reboot
```

完成内核更新并重启后，执行以下命令确认当前运行内核已切换至修复版本：

```
uname -r
```

确认输出版本不低于对应 TencentOS 修复版本后，可视为内核修复已生效。

### 缓解措施（临时）

如暂时无法完成内核升级，可禁止 sctp 内核模块的加载。

**注：**此操作可能导致依赖 SCTP 协议的应用（如部分电信信令业务）无法正常工作，请业务方排查后执行。

以 root 用户执行以下命令：

```
sh -c "printf 'install sctp /bin/false\n' > /etc/modprobe.d/block-CVE-2026-64564.conf; rmmod sctp 2>/dev/null; true"
```

执行完成后检查是否成功（以 root 用户执行）：

```
cat /etc/modprobe.d/block-CVE-2026-64564.conf
# 应当回显：
# install sctp /bin/false

cat /proc/modules | grep -w sctp
# 应当回显空
```

建议在升级前做好数据备份工作，避免出现意外。

**-END-**

**——关注云鼎实验室，获取更多安全情报——**

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

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