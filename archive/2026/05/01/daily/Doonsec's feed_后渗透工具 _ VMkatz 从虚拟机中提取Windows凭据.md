---
title: 后渗透工具 | VMkatz 从虚拟机中提取Windows凭据
url: https://mp.weixin.qq.com/s/OQ06vNLnWheYgk3iWWK0Gw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:58:53.985616
---

# 后渗透工具 | VMkatz 从虚拟机中提取Windows凭据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVn5Df322wNTk4hWIU34Q1lOXZZEr7ibUneJ4QnIr3KnhicqDic2ia1IRBagvERuz3KdTFfhiaiadRONNLJY3vypYQ3pFLexr6tK7vibdM/0?wx_fmt=jpeg)

# 后渗透工具 | VMkatz 从虚拟机中提取Windows凭据

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 1218，阅读大约需 7 分钟

## 前言

师傅们，五一快乐。

VMkatz 可从虚拟机文件中提取 Windows 凭据。

项目地址：https://github.com/nikaiw/VMkatz

![1a9352d029d2482f5e8589615590d073.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk9zBtYk5oclibqemuWlTXN1CsVEUiaicwv98DoGXiceiabDxGmfqx9Eg9OgXHFEKYib04EItWFiaibno5UYy3oibH7gkEMwzSCMSN8rN9o/640?from=appmsg "null")

1a9352d029d2482f5e8589615590d073.png

## 场景

在红队渗透测试场景中，最令人头疼的场景之一莫过于：费尽周折渗透到虚拟化集群挂载的 NAS 设备，发现了存储着域控制器、管理员工作站等核心资产的`.vmdk`、`.vmsn`等虚拟机文件，却因网络带宽限制（比如 200KB/s 的传输速率），提取一个 100GB 的磁盘镜像需要整整六天——漫长的传输过程不仅效率低下，更意味着被 SOC（安全运营中心）发现、阻断渗透链路的风险呈指数级上升。

而 VMkatz 的出现，彻底改变了这一局面。这款轻量级工具能够直接在虚拟机文件存储位置（NAS、虚拟化主机等）提取 Windows 核心机密，无需完整导出动辄上百 GB 的磁盘镜像，仅需一个约 3MB 的静态二进制文件，就能让红队人员快速获取高价值凭据，大幅降低渗透暴露风险。

## 核心能力：从虚拟机中精准提取关键机密

VMkatz 的核心价值在于“就地读取”，它能从虚拟机内存快照、虚拟磁盘等多种介质中，精准提取 Windows 系统的核心敏感信息，覆盖红队渗透所需的几乎所有凭据类型。

### 1. 内存快照提取（LSASS 层面）

针对`.vmsn`、`.sav`等虚拟机内存快照文件，VMkatz 实现了 mimikatz 的全部 9 种 SSP 凭据提供者解析能力，同时还能提取 BitLocker 密钥，具体包括：

* • **MSV1\_0**：NT/LM 哈希、SHA1 值（支持分页条目物理扫描兜底）；
* • **WDigest**：明文密码（链表遍历+`.data`段兜底）；
* • **Kerberos**：AES/RC4/DES 密钥、Kerberos 票据（`.kirbi`/`.ccache`格式，支持已释放会话的票据雕刻）；
* • **TsPkg**：RDP 会话明文密码；
* • **DPAPI**：主密钥缓存（GUID+解密后的密钥，支持离线 DPAPI 解密）；
* • **SSP/LiveSSP/Credman**：各类明文凭据（涵盖服务、凭据管理器存储的凭证）；
* • **CloudAP**：Azure AD 令牌（本地登录场景下通常为空）；
* • **BitLocker FVEK**：通过内存池标签（`FVEc`/`Cngb`）扫描提取全卷加密密钥。

**从 vmware 快照中提取 Windows 凭据**

```
./vmkatz snapshot.vmsn
```

结果
![410051dd60860d1204024a995e9ea2ba.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn4uw3luglAFKg6Ms6ewuexIurY7LKbaxq1XxMjJKn00mdgliao6onrlXastOrxLhbpcvH5p4TMBEt77EgjNykrQdZyawicOWNWc/640?from=appmsg "null")

410051dd60860d1204024a995e9ea2ba.png

### 2. 虚拟磁盘离线提取

针对`.vmdk`、`.vdi`、`.qcow2`等虚拟磁盘文件，VMkatz 可离线解析出磁盘内的核心凭据，无需启动虚拟机：

* • SAM 哈希：本地账户 NT/LM 哈希（附带账户状态，如禁用、空密码）；
* • LSA 机密：服务账户密码、自动登录凭据、机器账户密钥；
* • 缓存域凭据：DCC2 哈希（最近 N 次域登录记录）；
* • DPAPI 主密钥：兼容 Hashcat 的哈希格式（支持 15300/15310/15900/15910 等破解模式）；
* • NTDS.dit：通过原生 ESE 解析器提取域控制器完整 AD 哈希；
* • BitLocker 解密：结合内存提取的 FVEK 实现磁盘透明解密。

![f6d07d0ebcbe104313e5e8efadc9e7b3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlaibBbth4zsLYWia7X54baXD0oic0E3Kibxwgydm3tkXq8Hic5uOtk3B56gzTNFDs68fqO7Txmh6PaDR6ZeODIGhiaql1JNgicpIWTzY/640?from=appmsg "null")

f6d07d0ebcbe104313e5e8efadc9e7b3.png

## 广泛的兼容性：适配主流虚拟化环境与文件格式

VMkatz 的另一大优势是兼容性极强，几乎覆盖了当前主流的虚拟化平台、文件格式与 Windows 系统版本，无需针对不同环境适配工具。

### 1. 支持的输入格式

从虚拟化快照到原始注册表文件，VMkatz 能自动识别并解析多种格式，包括：

| 类型 | 扩展名/路径 | 来源 | 状态 |
| --- | --- | --- | --- |
| VMware 快照 | `.vmsn` + `.vmem`/纯`.vmsn` | Workstation、ESXi | 已测试 |
| VirtualBox 保存状态 | `.sav` | VirtualBox | 已测试 |
| QEMU/KVM 状态 | 自动检测/`.elf` | Proxmox、QEMU | 已测试 |
| Hyper-V 保存状态 | `.vmrs` | Hyper-V 2016+ | 未测试 |
| 虚拟磁盘 | `.vmdk` /`.vdi`/`.qcow2`/`.vhdx`/`.vhd` | 主流虚拟化平台 | 已测试 |
| 裸设备 | `/dev/disks/...` （VMFS）、`/dev/...`（LVM） | ESXi、Proxmox | 已测试 |
| 原始文件 | SAM/SYSTEM/SECURITY 注册表 hive、ntds.dit、LSASS minidump | Windows 系统 | 已测试 |
| VM 目录 | 任意文件夹 | 自动发现所有相关文件 | 已测试 |

### 2. 支持的目标系统

覆盖从 Windows Server 2003 到 Windows Server 2025、Windows 11 24H2 的全版本（兼容 x86 PAE 与 x64 架构），几乎适配所有企业级 Windows 环境。

## 快速上手

VMkatz 的使用方式极为简洁，无需复杂配置，仅需几行命令就能完成核心凭据提取，以下是典型场景示例：

```
# 从VMware快照提取LSASS凭据
./vmkatz snapshot.vmsn

# 结合磁盘文件解析分页出的凭据（提升提取完整性）
./vmkatz --disk disk.vmdk snapshot.vmsn

# 从虚拟磁盘提取SAM/LSA/DCC2哈希
./vmkatz disk.vmdk

# 从域控制器磁盘提取AD哈希
./vmkatz --ntds dc-disk.qcow2

# 指向VM目录，自动发现并提取所有可用凭据
./vmkatz /path/to/vm-directory/

# 输出Hashcat兼容格式的哈希（便于破解）
./vmkatz --format hashcat snapshot.vmsn

# 导出Kerberos票据
./vmkatz --kirbi snapshot.vmsn        # 导出.kirbi格式
./vmkatz --ccache snapshot.vmsn       # 导出.ccache格式

# 导出BitLocker FVEK密钥（用于dislocker解密）
./vmkatz --bitlocker-fvek /tmp/keys snapshot.vmsn
```

## 总结

项目地址：https://github.com/nikaiw/VMkatz

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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