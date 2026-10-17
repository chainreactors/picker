---
title: Vulnhub 靶场实战：独立分析五阶段法与提权路径全解析
url: https://mp.weixin.qq.com/s/svKuAZN6EwruEI_xVlrC-A
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:25:19.168880
---

# Vulnhub 靶场实战：独立分析五阶段法与提权路径全解析

# Vulnhub 靶场实战：独立分析五阶段法与提权路径全解析

原创

不懂安全的运维
不懂安全的运维

运维安全入门

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

第六章的 Metasploitable3 有一个特点：**它是设计好的**。漏洞的位置、深度、利用路径都被预先规划好，你只需要按部就班地走完流程。

但真实世界不是这样的。真实的入侵中，**没有标签告诉你「这里有漏洞」**，你面对的只有一台陌生的机器、一个 IP 地址，和一个必须解决的问题：拿到 root 权限。

**Vulnhub** 正是为此而生。它是全球最知名的社区制靶机平台，安全研究者把自己设计的虚拟机上传分享，任何人可以免费下载、在本地搭建、尝试攻破。**没有官方答案，没有通关徽章，有的只是「你是否真的拿到了 root」**。

**🛡️ 授权声明**　Vulnhub 靶机仅供个人学习与授权环境中的安全测试使用。请勿在未获授权的任何系统上进行测试。

本文目录

1. Vulnhub 是什么，它和前面靶场的根本差异
2. 靶机获取与虚拟化环境配置
3. 虚拟机网络配置与常见踩坑
4. 核心机制：Writeup 生态与难度分级
5. 实战一：标准解题流程的完整拆解
6. 实战二：信息收集的完整清单
7. 实战三：常见漏洞线索与识别方法
8. 实战四：提权的四条主要路径
9. 实战四：典型靶机实战思路复盘
10. 常见问题与效率提升技巧
11. 等保视角：把 Vulnhub 方法论用在真实评估
12. 总结

## 01Vulnhub 是什么，它和前面靶场的根本差异

Vulnhub 成立于 2010 年左右，定位是「Free Virtual Machines for Security Testing」。它的运作模式很简单：**社区贡献 + 免费下载 + 自主通关**。

### Vulnhub 与前面靶场的本质差异

| 维度 | DVWA / Juice Shop | Vulnhub |
| --- | --- | --- |
| 信息 | 明确告知漏洞类型 | 完全未知，需自行发现 |
| 目标 | 完成指定操作 | 唯一的：拿到 root |
| 线索 | 内置提示/分级提示 | 只有他人写的 writeup |
| 环境 | Web 应用，形态固定 | 完整系统，形态各异 |
| 路径 | 唯一或少数 | 多条路径，多种解法 |
| 难度 | 可预期 | 从入门到高难，差异极大 |

**💡 提示**　**这个差异决定了学习方式必须改变。**在 DVWA 里，你可以先看讲解再动手；在 Vulnhub，*你必须先形成假设，再用工具验证*。如果一上来就抓狂，说明方法论出了问题，而不是你能力不够。

### 为什么仍然值得花时间做 Vulnhub

* **它训练的是「推理能力」而非「工具使用」**

  ：同样的 nmap 输出，在不同靶机上含义完全不同。
* **它暴露真实系统的复杂度**

  ：没有统一入口、没有统一账号，你必须自己找到突破口。
* **它的 writeup 生态是极好的学习材料**

  ：高手的完整思考过程，比任何教材都珍贵。
* **它直接对应漏洞赏金与红队工作**

  ：CTF 打手的思维，与真实渗透是相通的。

**界面说明** Vulnhub 首页是虚拟机靶场列表，每台机器配封面图并标注难度、提交时间与下载量，支持按热度与难度排序。每台靶机页面下方通常由作者给出说明段落，包含目标说明、初始凭据、虚拟机网络配置（IP、DHCP 或静态）以及通关标准。选题时建议先按难度由低到高、优先选择提供官方 writeup 的机器，练完可对照复盘自己的思路偏差。

## 02靶机获取与虚拟化环境配置

### 下载靶机

Vulnhub 的靶机以两种格式发布：

| 格式 | 说明 | 使用场景 |
| --- | --- | --- |
| OVA | VirtualBox 通用格式 | VirtualBox 用户直接导入 |
| VMX | VMware Workstation 格式 | VMware 用户直接导入 |
| 7z/tar | 仅含磁盘镜像（VMDK/VHD） | 需要自行配置虚拟机 |

官方发布页会明确标注需要哪个版本的 VirtualBox 或 VMware，**下载前务必确认版本兼容性**——格式不匹配是最常见的翻车原因。

### VirtualBox 导入步骤

务必创建基线快照，避免搞乱环境后无法重置

```
# 方式一：图形界面 # File -> Import Appliance -> 选择 .ova 文件 # 确认 CPU/内存/磁盘设置 -> Import  # 方式二：命令行 VBoxManage import ./target.ova --vsys 0 --name "Vulnhub-Target"  # 建议：导入后立即创建一个快照，作为干净基线 VBoxManage snapshot "Vulnhub-Target" take "clean-baseline"
```

**💡 提示**　**创建基线快照，是做 Vulnhub 最重要的一条工作习惯。**很多靶机在解题过程中会安装东西、改配置、写文件，一旦环境被弄乱（或者你触发了某个「一次性」的服务），就只能重新导入重打一遍。*快照就是你的存档点*。

### VMware 用户

VMware 兼容性通常更好，但版本差异也可能导致启动异常

```
# VMware Workstation / Player 可直接打开 .ova / .vmx # 若仅有磁盘镜像： # 1) 新建虚拟机时选择「我已有一个磁盘」 # 2) 指向解压出的 .vmdk 文件 # 3) 网卡类型建议选 NAT 或仅主机模式
```

**💡 提示**　如果 VMware 提示「该文件需要转换」或「CPU 不兼容」，通常需要修改虚拟机的 CPU 兼容性设置：在虚拟机设置 → 处理器 中，勾选「虚拟机中启用 IO APIC」并调整 CPU 模式。不同靶机对 CPU 特性的依赖不同，遇到启动失败可以先试这个。

## 03虚拟机网络配置与常见踩坑

网络配置直接决定你能不能扫到靶机。这是新手卡住最多的环节。

| 配置项 | 推荐值 | 说明 |
| --- | --- | --- |
| 网卡模式 | Host-only（仅主机） | 最安全，靶机仅宿主机可达 |
| 网卡类型 | Intel PRO/1000 或 I82540EM | 兼容性最好 |
| 启动时连接 | 勾选 | 否则开机后无网络 |
| 攻击机位置 | 同一 host-only 网段 | 确保 IP 互通 |

**⚠️ 注意**　**网卡类型一定要选对。**VirtualBox 的默认网卡在某些老旧系统（如 CentOS 6、某些较老的 Linux 发行版）上无法识别，表现为「靶机里 `ip a` 看不到网卡」或「网卡状态 down」。遇到这种情况，*关机后修改网卡类型为 Intel 系列即可解决*。

先查网段，再给攻击机配 IP，不要凭记忆填

```
# 确认 host-only 网络网段 VBoxManage list hostonlyifs  # 假设输出显示： # Name: vboxnet0, IP Address: 192.168.56.1, Mask: 255.255.255.0 # 那么把攻击机（如 Kali）的网卡加到同网段： sudo ip addr add 192.168.56.100/24 dev eth0 sudo ip link set eth0 up
```

**💡 提示**　如果你是 Windows 攻击机且装的是 VirtualBox，也可以直接用 Windows 的网络适配器连接到 VirtualBox Host-Only 网络，在「网络连接 → 更改适配器属性 → IPv4」里手动填一个同网段的 IP。前提是防火墙不拦截 ICMP（否则 ping 不通会误判为网络不通，但实际上 Nmap 可能仍然能扫到端口）。

## 04核心机制：Writeup 生态与难度分级

### Writeup 生态：Vulnhub 的灵魂

这是 Vulnhub 与其他靶场**最本质的区别**。因为没有内置提示，社区里形成了一个庞大的 writeup（解题文章）文化：打通关的人会把完整过程写成文章发布出来。

这带来一个独特的**学习闭环**：

1. 遇到卡关的靶机，先自己尝试 2-3 小时。
2. 仍然无解，找一篇 writeup，**但只读到「思路」部分，先自己按思路再做一遍**。
3. 做完后再读完整 writeup，对比自己的思路与作者的差异。
4. 把作者用到的、你没想到的技巧记下来。

**💡 提示**　**关键在第 2 步：不要一上来就读完整 walkthrough。**直接看答案会让训练彻底失去意义——你会产生「我也会」的错觉，但下次遇到新机器依然束手无策。正确做法是*读思路、自己做、再对答案*，这个顺序不能反。

### 难度分级的现实情况

| 难度 | 特征 | 典型所需知识 | 建议投入 |
| --- | --- | --- | --- |
| Easy | Web/服务漏洞明显，少量枚举 | 基础工具使用 | 1-3 小时 |
| Medium | 需要 2-3 个漏洞链，有凭据复用 | 信息收集+基础提权 | 4-10 小时 |
| Hard | 内核/二进制利用、复杂过滤绕过 | 二进制安全、提权 | 1-3 天 |
| Insane | 定制内核模块、复杂密码学 | 内核开发、密码学 | 3 天以上 |

**⚠️ 注意**　Vulnhub 上的难度**没有官方标准**，完全取决于作者的标注。建议初学者从标注 Easy-Medium 的机器开始，*并且优先选择有高质量 writeup 的靶机*——有 writeup 意味着有人验证过它的可解性。

## 05实战一：标准解题流程的完整拆解

尽管每台靶机各不相同，但 Vulnhub 靶机的解题流程**高度模式化**。掌握这个通用框架，你面对任何靶机都不会手足无措。

### 五阶段流程

1. **阶段一：环境准备**

   ——导入虚拟机、配置网络、确认靶机 IP 可达、建立基线快照。
2. **阶段二：信息收集**

   ——这是花时间最多、但价值最高的阶段。端口、服务、目录、源码、凭据。
3. **阶段三：突破口**

   ——从信息中找到一个可行的攻击面，取得初步的代码执行或文件读取能力。
4. **阶段四：提权**

   ——从低权限账户提升到 root。
5. **阶段五：旗标**

   ——通常在 root 家目录或 `/root/flag.txt`、`/root/root.txt`。

![Vulnhub 标准解题流程：环境准备 → 信息收集 → 突破口 → 提权 → 旗标](https://mmbiz.qpic.cn/sz_mmbiz_png/0l1UjZtX9txrwrGdcSeLzI3PTSSFE5ncpcemchLD8iaHIAJG6X8Vm0AnEeEgDiawJ1G2QvIF9pUgFJTibMrEib8NAmMvMibNCqRD1HVwNpiacXzRw/640?from=appmsg)

图：Vulnhub 标准解题流程：环境准备 → 信息收集 → 突破口 → 提权 → 旗标

## 06实战二：信息收集的完整清单

信息收集是 Vulnhub 的核心技能。下面这份清单覆盖了实战中 90% 的情况，建议作为标准动作执行。

### 网络层

全端口 + UDP 是 Vulnhub 的标配动作

```
# 1) 主机发现（确认 IP 是否正确） netdiscover -r 192.168.56.0/24 arp-scan -localnet  # 2) 全端口扫描（必须扫全，Vulnhub 常把服务放在非标准端口） nmap -p- --min-rate 5000 192.168.56.4 -oN allports.txt  # 3) 服务版本探测 nmap -sV -sC -p <从上面得到的端口> 192.168.56.4 -oN detail.txt  # 4) UDP 端口（容易被忽视，但常藏关键服务） nmap -sU --top-ports 50 --min-rate 5000 192.168.56.4
```

**⚠️ 注意**　**关于「非标准端口」：**Vulnhub 靶机经常把 Web 服务放在 8080、8081、甚至 12345 这样的端口上。*如果你只扫 1-10000 端口，很可能直接错过唯一的入口*。养成 `nmap -p-` 的习惯。

### Web 层：拿到 HTTP 入口之后

枚举结果要看状态码与响应长度，不只看 200

```
# 目录/文件枚举 gobuster dir -u http://192.168.56.4 -w /usr/share/wordlists/dirb/big.txt.txt \   -x php,txt,bak,html -t 50 --no-error -k  # 技术栈识别 whatweb http://192.168.56.4 nikto -h http://192.168.56.4  # 源码/备份文件 #   *.bak  *.old  *.swp  *~  .git/  .svn/  .DS_Store #   .htaccess  web.config  robots.txt  sitemap.xml  # 源码泄露（WebGoat 的 php://filter 技巧同样适用） curl "http://192.168.56.4/index.php?page=php://filter/convert.base64-encode/resource=index"
```

### 主机层：拿到低权限 shell 之后

提权四件套：sudo -l、SUID、可写文件、凭据

```
# 身份与能力 id && whoami && hostname && uname -a cat /etc/os-release            # 精确版本很重要 sudo -l                         # 关键！查看 sudo 权限  # 提权线索搜索 find / -perm -4000 -type f 2>/dev/null    # SUID 文件 find / -perm -2000 -type f 2>/dev/null    # SGID 文件 find / -writable -type f 2>/dev/null | head -50   # 可写文件  # 凭据搜索（提权最重要的线索来源） find / -iname '*.conf' -o -iname '*.cfg' -o -iname '*.ini' 2>/dev/null | head -50 grep -ri 'password' /etc /var/www /home 2>/dev/null | head -30 cat ~/.bash_history 2>/dev/null             # 历史命令极有价值
```

**💡 提示**　**`sudo -l` 是提权环节的第一动作，永远不要跳过。**很多靶机的突破口就藏在这里——某个看起来无害的命令被允许以 root 运行，而该命令存在提权可能。*看到 `(ALL) NOPASSWD: ALL` 就基本结束了；看到限定命令也要逐个研究其用法。*

![Vulnhub 信息收集全景：网络层 → Web 层 → 主机层三层递进](https://mmbiz.qpic.cn/sz_mmbiz_png/0l1UjZtX9tz9rJeic1rcbzcMshFuE7YpLttqBvPcfPFClaMdy3W1HVQ9ibZLLGHQe1LibcJpic9Hen8koM0wibfsemWzEHGgZz6voxfKM4PW4EJ4/640?from=appmsg)

图：Vulnhub 信息收集全景：网络层 → Web 层 → 主机层三层递进

## 07实战三：常见漏洞线索与识别方法

Vulnhub 靶机的漏洞类型虽多，但识别线索有规律可循。下面按「线索 → 可能的漏洞方向」整理。

| 观察到的线索 | 可能的漏洞方向 | 验证方式 |
| --- | --- | --- |
| 老版本软件（CentOS 6 等） | 已知的本地提权漏洞 | searchsploit linux kernel |
| Web 页面老旧（Gmail 风格） | 特定 CMS/应用的已知漏洞 | whatweb 识别后查 CVE |
| 目录可列、源码可见 | 源码审计找逻辑漏洞 | 下载全部源码本地审计 |
| 有上传功能 | 任意文件上传 | 尝试上传 webshell |
| 有文件包含参数 | LFI/RFI | php://filter 读源码 |
| SSH 端口开放 | 弱口令 / 凭据复用 | 用收集到的密码尝试 |
| 数据库端口开放 | 弱口令 / 未授权 | 直接尝试连接 |
| 计划任务/crontab 可写 | 定时任务提权 | 检查权限与内容 |

**💡 提示**　**`searchsploit` 必须掌握。**它是 Kali/Parrot 上自带的漏洞查询工具，按关键词、CVE 号、产品名搜索公开的漏洞利用代码。在 Vulnhub 上遇到「老版本软件」时，*先搜 searchsploit 往往能直接找到突破口*。

searchsploit 让你不必依赖互联网就能查询公开漏洞

```
# searchsploit 常用命令 searchsploit apache 2.4.49        # 按关键词 searchsploit CVE-2021-41773        # 按 CVE searchsploit linux kernel 4.4      # 组合条件 searchsploit -t sshd                # 只看远程利用 searchsploit -l kernel             # 列出本地提权  # 复制并阅读 PoC searchsploit -p 50465 searchsploit 50465 -p  # 打印完整内容
```

## 08实战四：提权的四条主要路径

拿到低权限 shell 后，提权是最后一个大关。Vulnhub 靶机的提权路径基本可以归为四类。

### 路径一：sudo 权限滥用

GTFOBins 收录了上千种 sudo 提权命令的利用方式

```
# 查看可用 sudo 权限 sudo -l  # 常见可利用的 sudo 命令 sudo ...