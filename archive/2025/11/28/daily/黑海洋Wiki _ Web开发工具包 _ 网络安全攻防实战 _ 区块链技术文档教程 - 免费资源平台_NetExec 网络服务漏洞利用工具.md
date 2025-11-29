---
title: NetExec 网络服务漏洞利用工具
url: https://blog.upx8.com/4910
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-11-28
fetch_date: 2025-11-29T03:11:56.213957
---

# NetExec 网络服务漏洞利用工具

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# NetExec 网络服务漏洞利用工具

发布时间:
2025-11-28 New Article

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
1492

## NetExec简介

*NetExec（又名 nxc）是一种网络服务漏洞利用工具，可帮助自动评估大型*网络的安全性。

该项目最初由@byt3bl33d3r（当时名为CrackMapExec）于2015年创建。2019年，@mpgn\_x64开始维护该项目，并在接下来的四年里添加了许多优秀的工具和功能。2023年9月，他退休，不再维护该项目。

我们（NeffIsBack、Marshall-Hallenbeck 和 zblurx）与许多其他贡献者一起开发了新功能、修复了错误，并帮助维护了原始项目 CrackMapExec。在此期间，由于同时存在私有和公共代码库，社区贡献难以轻易合并到项目中。代码库之间 6-8 个月的差异导致了许多开发问题，并严重削弱了社区驱动的开发。随着 mpgn 维护者角色的结束，我们（剩下的最活跃贡献者）决定将该项目作为一个完全免费开源的项目，以新名称**NetExec** 🚀 进行维护。展望未来，我们的目标是维护一个由社区驱动和维护的项目，并定期更新供所有人使用。

[![NetExec 网络服务漏洞利用工具](https://www.ddosi.org/wp-content/uploads/2025/09/101133.webp)](https://www.ddosi.org/wp-content/uploads/2025/09/101133.webp)

## 功能特色

| 功能类别 | 核心功能点 | 简要说明与典型应用 |
| --- | --- | --- |
| **协议支持** | SMB, LDAP, WinRM, MSSQL, SSH, FTP, RDP, WMI, VNC, NFS | 广泛覆盖各类网络协议与服务，是进行自动化评估的基础。 |
| **信息枚举** | 枚举共享/用户/组/会话、获取密码策略、发现主机/服务 | 全面收集目标网络信息，绘制网络地图，为后续行动提供情报。 |
| **凭证安全** | 密码喷洒与爆破、哈希传递（PtH）、Kerberos 票据利用 | 测试账户凭证强度，利用已获取的凭据进行横向移动。 |
| **横向移动** | 远程命令/脚本执行、文件上传与下载 | 在获得访问权限的主机上执行命令或传输文件，扩展控制范围。 |
| **凭证提取** | 转储 SAM/LSA/NTDS.dit、使用 Mimikatz 等模块 | 从内存或数据库中提取登录凭证，通常需要管理员权限。 |
| **模块化扩展** | 漏洞检测（如 Zerologon）、数据收集（如 BloodHound） | 通过模块支持漏洞扫描、安全产品枚举等高级渗透测试功能。 |

## 安装方法

```
pip install pipx
python -m pipx ensurepath
python -m pipx install git+https://github.com/Pennyw0rth/NetExec
NetExec
```

## 命令参数

```
用法: netexec [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--verbose] [--debug] [--no-progress] [--log LOG] [-6]
               [--dns-server DNS_SERVER] [--dns-tcp] [--dns-timeout DNS_TIMEOUT]
               {ldap,nfs,ftp,mssql,smb,winrm,wmi,rdp,ssh,vnc} ...

     .   .
    .|   |.     _   _          _     _____
    ||   ||    | \ | |   ___  | |_  | ____| __  __   ___    ___
    \\( )//    |  \| |  / _ \ | __| |  _|   \ \/ /  / _ \  / __|
    .=[ ]=.    | |\  | |  __/ | |_  | |___   >  <  |  __/ | (__
   / /˙-˙\ \   |_| \_|  \___|  \__| |_____| /_/\_\  \___|  \___|
   ˙ \   / ˙
     ˙   ˙

选项:
  -h, --help            显示此帮助信息并退出

通用选项:
  适用于所有协议的通用选项

  --version             显示 nxc 版本
  -t, --threads THREADS
                        设置要使用的并发线程数
  --timeout TIMEOUT     每个线程的最大超时时间（秒）
  --jitter INTERVAL     设置每次认证之间的随机延迟间隔

输出选项:
  设置详细级别和控制输出的选项

  --verbose             启用详细输出
  --debug               启用调试级别信息
  --no-progress         在扫描期间不显示进度条
  --log LOG             将结果导出到自定义文件

DNS选项:
  -6                    启用强制 IPv6
  --dns-server DNS_SERVER
                        指定 DNS 服务器（默认：使用 hosts 文件和系统 DNS）
  --dns-tcp             对 DNS 查询使用 TCP 而不是 UDP
  --dns-timeout DNS_TIMEOUT
                        DNS 查询超时时间（秒）

可用协议:
  {ldap,nfs,ftp,mssql,smb,winrm,wmi,rdp,ssh,vnc}
    ldap                使用 LDAP 协议
    nfs                 使用 NFS 协议
    ftp                 使用 FTP 协议
    mssql               使用 MSSQL 协议
    smb                 使用 SMB 协议
    winrm               使用 WINRM 协议
    wmi                 使用 WMI 协议
    rdp                 使用 RDP 协议
    ssh                 使用 SSH 协议
    vnc                 使用 VNC 协议
```

## 使用文档

[https://www.netexec.wiki](https://www.netexec.wiki/)

## 项目地址

GitHub:
<https://github.com/Pennyw0rth/NetExec>

[取消回复](https://blog.upx8.com/4910#respond-post-4910)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2025 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")