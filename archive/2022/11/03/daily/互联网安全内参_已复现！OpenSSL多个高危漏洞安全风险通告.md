---
title: 已复现！OpenSSL多个高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247506559&idx=2&sn=d6c171a7788894e50fb3da15a958b053&chksm=ebfa9d5fdc8d1449f4cd0b01e6ce464182d60b292f3fc9509a2c540bca6a1b749e763bbe94e5&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2022-11-03
fetch_date: 2025-10-03T21:40:14.225232
---

# 已复现！OpenSSL多个高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tIulPDz5ibgpewZ7SXp4ww1CSlicUoicCiaiasbjcv0KCwNoKtzXdn8Ohn619jPrFFdUxVdLoYcFsfDLg/0?wx_fmt=jpeg)

# 已复现！OpenSSL多个高危漏洞安全风险通告

安全内参

编者荐语：

此次公布的漏洞可能不像HeartBleed那样容易可被广泛利用，用户不必过于惊慌，但仍建议尽快升级到安全版本。

以下文章来源于奇安信 CERT
，作者QAX CERT

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6XPxB5kkgQy0RWNKZLKRRmvVAb4XjaNGHgJxezpMHdibg/0)

**奇安信 CERT**
.

为企业级用户提供高危漏洞、重大安全事件安全风险通告和相关产品解决方案。

OpenSSL 是用于传输层安全 (TLS) 协议（以前称为安全套接字层 (SSL) 协议）的强大、商业级、功能齐全的开源工具包，协议实现基于全强度通用密码库，用于保护计算机网络上的通信免受窃听，被互联网服务器广泛使用（包括大多数HTTPS网站）。

近日，奇安信CERT监测到OpenSSL官方发布了漏洞安全更新，**包括OpenSSL拒绝服务漏洞(CVE-2022-3786)和OpenSSL远程代码执行漏洞(CVE-2022-3602)**，攻击者利用CVE-2022-3786漏洞，制作包含恶意电子邮件地址的证书，以溢出包含"."的任意字节数，此缓冲区溢出可能导致服务崩溃。CVE-2022-3602漏洞存在于ossl\_punycode\_decode函数，当客户端或服务器配置为验证X.509证书时调用此函数，攻击者可以通过在电子邮件地址字段的域中创建包含 punycode 的特制证书来利用该漏洞，可能导致服务崩溃或潜在的远程代码执行。

**由于CVE-2022-3602可能引发远程代码执行，官方在预先公告中将其视为“严重”漏洞，因为很多平台已经实现了堆栈溢出保护，可以降低远程代码执行利用风险，所以此漏洞被降级为“高危”漏洞。**

此前有多篇文章将CVE-2022-3602漏洞与2014年的**HeartBleed**相提并论，引起大量安全人员的关注，**由于此漏洞利用前提条件是必须配置客户端或服务器以验证证书中恶意电子邮件地址，同时仅影响 OpenSSL 3.x，进一步限制了漏洞的利用范围，此次更新的漏洞可能不像HeartBleed那样容易可被广泛利用，所以用户不必过于惊慌，但仍建议尽快升级到安全版本。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **OpenSSL****拒绝服务漏洞** | | |
| **公开时间** | 2022-11-01 | **更新时间** | 2022-11-02 |
| **CVE****编号** | CVE-2022-3786 | **其他编号** | QVD-2022-43322 |
| **威胁类型** | 拒绝服务 | **技术类型** | 缓冲区溢出 |
| **厂商** | OpenSSL | **产品** | OpenSSL |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **中危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | 此缓冲区溢出可能导致崩溃（导致拒绝服务），在TLS客户端中，这可以通过连接到恶意服务器来触发，在TLS服务器中，如果服务器请求客户端身份验证并且与恶意客户端连接，则可以触发此操作。 | | |
| **影响版本** | OpenSSL 3.x < 3.0.7 | | |
| **不受影响版本** | OpenSSL 1.x == 1.1.1  OpenSSL 1.x == 1.0.2  OpenSSL 3.x == 3.0.7 | | |
| **其他受影响组件** | Amazon Linux 2022  Broadcom Symantec Endpoint Protection Manager 14.3 RU5  Canonical Ubuntu Squid  Debian 12 "Bookworm"  Dockerhub clojure latest  Dockerhub centos latest  Dockerhub ghost latest  Dockerhub hipache latest  Dockerhub lightstreamer latest  Dockerhub mariadb latest  Dockerhub maven latest  Dockerhub node latest  Dockerhub orientdb latest  Dockerhub photon latest  Dockerhub r-base latest  Dockerhub ros latest  Dockerhub tomcat latest  Dockerhub ubuntu-debootstrap latest  Dockerhub ubuntu-upstart latest  Dockerhub ubuntu latest  EuroLinux 9  Fedora Linux 36  Fedora Linux 37  Intel System Usage Report (Codename: Queencreek) 2.4.0.8919  Linux Mint 21 Vanessa  Mageia cauldron  NixOS unstable  Offensive Security Kali 2022.3  OpenMandriva 4.3  OpenMandriva 4.2  OpenMandriva rolling  OpenMandriva cooker  OpenSUSE tumbleweed  Oracle Linux 8.x  Red Hat Universal Base Images >= 9.0  Softether VPN 4.39 Build 9772 Beta  SUSE Enterprise Linux Server 15 SP4  Tenable Nessus 10.3.0  Tenable Nessus Agent 10.2  Tenable Nessus Network Monitor 6.1.0  VMware Harbor <=2.6.1  VMware Tools 12.0.0  VMware Tools 12.1.0  Juniper  JunOS Evolved >22.1R1-EVO | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **OpenSSL****远程代码执行漏洞** | | |
| **公开时间** | 2022-11-01 | **更新时间** | 2022-11-02 |
| **CVE****编号** | CVE-2022-3602 | **其他编号** | QVD-2022-43319 |
| **威胁类型** | 代码执行、拒绝服务 | **技术类型** | 缓冲区溢出 |
| **厂商** | OpenSSL | **产品** | OpenSSL |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| **已公开** | 未发现 | 未发现 | **已公开** |
| **漏洞描述** | 漏洞存在于ossl\_punycode\_decode函数中，当客户端或服务器配置为验证X.509证书时调用此函数，攻击者可以通过在电子邮件地址字段的域中创建包含 punycode 的特制证书来利用该漏洞。 | | |
| **影响版本** | OpenSSL 3.x < 3.0.7 | | |
| **不受影响版本** | OpenSSL 1.x == 1.1.1  OpenSSL 1.x == 1.0.2  OpenSSL 3.x == 3.0.7 | | |
| **其他受影响组件** | Amazon Linux 2022  Broadcom Symantec Endpoint Protection Manager 14.3 RU5  Canonical Ubuntu Squid  Debian 12  "Bookworm"  Dockerhub clojure latest  Dockerhub centos latest  Dockerhub ghost latest  Dockerhub hipache latest  Dockerhub lightstreamer latest  Dockerhub mariadb latest  Dockerhub maven latest  Dockerhub node latest  Dockerhub orientdb latest  Dockerhub photon latest  Dockerhub r-base latest  Dockerhub ros latest  Dockerhub tomcat latest  Dockerhub ubuntu-debootstrap latest  Dockerhub ubuntu-upstart latest  Dockerhub ubuntu latest  EuroLinux 9  Fedora Linux 36  Fedora Linux 37  Intel System Usage Report (Codename: Queencreek) 2.4.0.8919  Linux Mint 21 Vanessa  Mageia cauldron  NixOS unstable  Offensive Security Kali 2022.3  OpenMandriva 4.3  OpenMandriva 4.2  OpenMandriva rolling  OpenMandriva cooker  OpenSUSE tumbleweed  Oracle Linux 8.x  Red Hat Universal Base Images >= 9.0  Softether VPN 4.39 Build 9772 Beta  SUSE Enterprise Linux Server  15 SP4  Tenable Nessus 10.3.0  Tenable Nessus Agent 10.2  Tenable Nessus Network Monitor 6.1.0  VMware Harbor <=2.6.1  VMware Tools 12.0.0  VMware Tools 12.1.0  Juniper  JunOS Evolved >22.1R1-EVO | | |

奇安信CERT第一时间分析并复现了**OpenSSL远程代码执行漏洞 (CVE-2022-3602)**，复现截图如下:

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs49vXGibPBYEssNog2hTiaTZe3p3AQRsOT7Gmpzs3QqK3SaJZ9B5bZBwxLf3pXvSVYiaWUa9GXO847E4w/640?wx_fmt=png)

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **OpenSSL****拒绝服务漏洞** | | | |
| **CVE****编号** | CVE-2022-3786 | **其他编号** | | QVD-2022-43322 |
| **CVSS 3.1****评级** | **中危** | **CVSS 3.1****分数** | | 5.9 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 高 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 无 | | 需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 无 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 无 | | 高 | |
| **危害描述** | 攻击者制作包含恶意电子邮件地址的证书，以溢出包含"."的任意字节数，此缓冲区溢出可能导致服务崩溃。 | | | |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **OpenSSL****远程代码执行****漏洞** | | | |
| **CVE****编号** | CVE-2022-3602 | **其他编号** | | QVD-2022-43319 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 7.1 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 高 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 无 | | 需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 低 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 攻击者制作包含恶意电子邮件地址的证书，溢出栈上四个可控字节，可能导致服务崩溃或潜在的远程代码执行。 | | | |

处置建议

**一、OpenSSL 3.x产品检测规则**

**1. YARA检测规则**

(1) OpenSSL的所有静态编译都包含一个版本字符串，如 'OpenSSL 3.0.6 2022 年 10 月 11 日'，其中3.0.6是版本号，以下规则主要检测其中的字符串。

```
rule openssl_version {strings:$re1 = /OpenSSL\s3\.[0-6]{1}\.[0-9]{1}[a-z]{,1}/
condition:$re1}
```

(2) 该规则思路主要是查找依赖OpenSSL的主应用程序，但解析可执行文件的导入。

```
import "elf"import "pe"

rule elf_import_openssl {    condition:        (elf.type == elf.ET_EXEC or elf.type == elf.ET_DYN) and        (            for any i in (0..elf.symtab_entries):            (                elf.symtab[i].name contains "@OPENSSL_3"            )        )}rule pe_import_openssl {    condition:        pe.is_pe and        (            for any i in (0..pe.number_of_imports):            (                pe.import_details[i].library_name contains "libcrypto-3" or pe.import_details[i].library_name contains "libssl-3"            )        )}
```

**2. OSQuery查询**

利用 Osquery 的 YARA 表在所有正在运行的进程上运行以下规则。

```
WITH FIRST_QUERY AS (SELECT DISTINCT    proc.pid,    proc.path,    proc.cmdline,    proc.cwd,    mmap.path AS mmap_pathFROM process_memory_map AS mmapLEFT JOIN processes AS proc USING(pid))SELECT *FROM FIRST_QUERYJOIN yara ON yara.path = FIRST_QUERY.mmap_pathWHERE sigrule = 'rule openssl_3 {strings:$re1 = /OpenSSL\s3\.[0-6]{1}\.[0-9]{1}[a-z]{,1}/

condition:$re1}'AND yara.count > 0
```

更多漏洞支持参考：https://www.akamai.com/blog/security-research/openssl-vulnerability-how-to-effectively-prepare

**二、漏洞影响产品排查**

由于OpenSSL是一个核心的开源组件，很多软件或产品可能会受到影响，用户需要及时关注已使用软件的安全公告，目前部分厂商已经发布自身产品受影响的相关公告：

https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2022-0023

https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-openssl-W9sdCc2a

**三、版本升级...