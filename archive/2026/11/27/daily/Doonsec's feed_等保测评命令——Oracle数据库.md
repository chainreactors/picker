---
title: 等保测评命令——Oracle数据库
url: https://mp.weixin.qq.com/s/T0d_0-iAbDqLD7VNQ3J8oA
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:38:40.446758
---

# 等保测评命令——Oracle数据库

# 等保测评命令——Oracle数据库

北京路劲科技
北京路劲科技

北京路劲科技有限公司

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**摘要**：本文整理了Oracle数据库在等保测评中的常用检查命令，覆盖身份鉴别、访问控制、安全审计等9个安全控制点，每条命令均包含达标判据与整改建议，并附有一键巡检脚本与高风险核查清单，帮助测评人员高效完成测评工作。

⚠️ **免责声明**：本文命令整理依据 GB/T 22239-2019、GB/T 28448-2019 标准，但不同厂商产品版本、配置方式存在差异。文中命令仅供参考，实际测评请以标准原文及测评机构要求为准。执行命令前请确认权限与环境，避免因操作失误导致业务中断。

一、身份鉴别

8.1.4.1 / 8.1.2.4

**1.1 账户唯一性与密码策略**

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 数据库用户 | SELECT username, account\_status, lock\_date, expiry\_date, created FROM DBA\_USERS WHERE account\_status NOT LIKE '%EXPIRED%' AND account\_status NOT LIKE '%LOCKED%' ORDER BY username | 无冗余/测试/共享账户，账户状态正常 |
| 默认账户锁定 | SELECT username, account\_status FROM DBA\_USERS WHERE username IN ('SYS','SYSTEM','SCOTT','HR','OE','PM','SH') | 默认账户已锁定或密码已修改 |
| 密码策略 | SELECT profile, resource\_name, resource\_type, limit FROM DBA\_PROFILES WHERE resource\_type = 'PASSWORD' ORDER BY profile, resource\_name | 密码复杂度、长度、过期策略符合三级要求 |
| 密码历史 | SELECT profile, limit FROM DBA\_PROFILES WHERE resource\_name = 'PASSWORD\_LIFE\_TIME' | PASSWORD\_LIFE\_TIME ≤ 90天 |
| 密码复杂度 | SELECT profile, limit FROM DBA\_PROFILES WHERE resource\_name IN ('PASSWORD\_VERIFY\_FUNCTION','PASSWORD\_REUSE\_TIME') | 设置复杂度校验函数，禁止近期密码重用 |

**Oracle特有配置：**

-- 查看所有用户账户状态

```
SELECT username, account_status, account_locked, expiry_date, password_last_changed, createdFROM DBA_USERSORDER BY username;
```

-- 查看已锁定账户

```
SELECT username, lock_date, account_statusFROM DBA_USERSWHERE account_status LIKE '%LOCKED%';
```

-- 查看即将过期账户（30天内）

```
SELECT username, account_status, password_last_changed, expiry_dateFROM DBA_USERSWHERE account_status = 'OPEN'AND expiry_date IS NOT NULLAND expiry_date < SYSDATE + 30;
```

-- 查看默认密码账户（使用默认密码的账户）

```
SELECT username, account_statusFROM DBA_USERSWHERE account_status NOT LIKE '%EXPIRED%'AND account_status NOT LIKE '%LOCKED%'AND username IN ('SYS','SYSTEM','SCOTT','HR','OE','PM','SH','APEX_PUBLIC_USER','ORDSYS','ORDDATA','MDSYS','EXFSYS','CTXSYS');
```

-- 查看密码策略设置

```
SELECT profile, resource_name, resource_type, limitFROM DBA_PROFILESWHERE resource_type = 'PASSWORD'ORDER BY profile, resource_name;
```

-- 查看密码复杂度验证函数

```
SELECT function_name, function_type, function_libraryFROM DBA_SECUREFILE_PWD_POLICIES;  -- Oracle 19c+
```

-- 或

```
SELECT * FROM DBA_AUDIT_POLICIES WHERE type = 'PASSWORD';
```

-- 查看密码历史（Oracle 12c+）

```
SELECT username, password_old_versionsFROM DBA_USERSWHERE password_old_versions IS NOT NULL;
```

**1.2 登录失败处理与会话超时**

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 登录失败锁定 | SELECT profile, resource\_name, limit FROM DBA\_PROFILES WHERE resource\_name IN ('FAILED\_LOGIN\_ATTEMPTS','PASSWORD\_LOCK\_TIME') | FAILED\_LOGIN\_ATTEMPTS ≤ 5，PASSWORD\_LOCK\_TIME 配置合理 |
| 会话空闲超时 | SHOW PROFILE 或 SELECT profile, limit FROM DBA\_PROFILES WHERE resource\_name = 'SESSIONS\_PER\_USER' | 应配置合理的会话数限制 |
| 空闲会话 | SELECT sid, username, serial#, last\_call\_et, status FROM V$SESSION WHERE status = 'INACTIVE' AND last\_call\_et > 600 | 空闲会话超过10分钟的应被清理 |

**Oracle特有配置：**

-- 查看登录失败锁定策略

```
SELECT profile, resource_name, resource_type, limitFROM DBA_PROFILESWHERE resource_name IN ('FAILED_LOGIN_ATTEMPTS','PASSWORD_LOCK_TIME');
```

-- 查看空闲会话

```
SELECT s.sid, s.serial#, s.username, s.program, s.status,s.last_call_et, s.logon_time, s.idle_timeFROM V$SESSION sWHERE s.status = 'INACTIVE'AND s.last_call_et > 300ORDER BY s.last_call_et DESC;
```

-- 查看会话参数配置

```
SELECT name, value, value_typeFROM V$PARAMETERWHERE name IN ('sessions', 'processes', 'open_cursors','sql_trace', 'trace_enabled');
```

-- 查看当前会话配置

```
SHOW PARAMETER sessions;SHOW PARAMETER processes;SHOW PARAMETER open_cursors;
```

-- 查看审计的登录失败记录

```
SELECT username, account, os_username, terminal, returncode, timestampFROM DBA_AUDIT_TRAILWHERE action_name = 'FAILED LOGIN'ORDER BY timestamp DESC;
```

**1.3 远程管理安全**

-- 查看监听器配置（需OS层面检查，但可查询网络服务名）

```
SELECT a.service_name, a.network_service_bannerFROM V$NETWORK_SERVICE_BANNER a;
```

-- 查看TCP连接来源

```
SELECT s.sid, s.serial#, s.username, s.osuser, s.osuser,s.machine, s.program, s.module, s.sql_id,s.logon_time, s.action, s.statusFROM V$SESSION sWHERE s.type = 'USER'ORDER BY s.logon_time DESC;
```

-- 查看远程连接IP

```
SELECT DISTINCT s.username, s.osuser, s.machine, s.network_idFROM V$SESSION sWHERE s.type = 'USER'AND s.machine IS NOT NULL;
```

-- 查看TCP参数配置

```
SHOW PARAMETER sql_trace;SHOW PARAMETER os_authent_prefix;SHOW PARAMETER os_roles;
```

-- 查看监听器状态（需通过lsnrctl）

-- 在OS层面执行：lsnrctl status

-- 检查telnet端口是否开启

-- 查看加密网络传输

```
SELECT name, value, value_typeFROM V$PARAMETERWHERE name IN ('sqlnet.crypto_checksum_algorithm','sqlnet.crypto_checksum_type','sqlnet.crypto_checksum_send','sqlnet.crypto_checksum_receive','sqlnet.crypto_check','os_authent_prefix');
```

**高风险项**：默认账户（SYS、SYSTEM）未锁定、使用OS认证(os\_authent\_prefix)未限制来源IP，直接判定不符合三级要求。

**1.4 双因子认证（高风险项）**

**测评方法**：访谈确认是否采用"本地密码 + Oracle Advanced Security"（如Oracle 12c+的PAM + RADIUS/LDAP集成），或通过Oracle Wallet + OS认证组合实现双因子。

**核查命令**：

-- 查看是否配置了RADIUS/LDAP认证（需Oracle Advanced Security）

-- 通过SQLNET.ORA检查

-- 在OS层面执行：

```
-- grep -i "ldap\|radius\|authentication_services" $ORACLE_HOME/network/admin/sqlnet.ora
```

-- 查看OS认证配置

```
SHOW PARAMETER os_authent_prefix;SHOW PARAMETER os_roles;
```

-- 查看是否启用了数据库审计登录认证

```
SELECT * FROM DBA_AUDIT_SESSION;
```

-- 查看用户认证方式

```
SELECT username, account_status, authentication_typeFROM DBA_USERS;  -- Oracle 19c+
```

二、访问控制

8.1.4.2 / 8.1.2.2

**2.1 权限管理与角色分离**

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 用户角色分配 | SELECT grantee, granted\_role, admin\_option FROM DBA\_ROLE\_PRIVS ORDER BY grantee | 按运维/审计/业务划分角色，禁止SYSDBA全权 |
| 系统权限 | SELECT grantee, privilege, admin\_option FROM DBA\_SYS\_PRIVS WHERE grantee NOT LIKE 'SYS%' ORDER BY grantee | 系统权限最小化分配 |
| 对象权限 | SELECT grantee, owner, table\_name, privilege FROM DBA\_TAB\_PRIVS WHERE grantee NOT LIKE 'SYS%' ORDER BY grantee | 对象权限按最小权限原则 |
| 权限审查 | SELECT \* FROM DBA\_PRIVILEGE\_ANALYSIS | Oracle 19c+启用权限分析 |
| 审计角色分离 | SELECT role, privilege FROM DBA\_SYS\_PRIVS WHERE grantee IN (SELECT grantee FROM DBA\_ROLE\_PRIVS WHERE granted\_role = 'AUDIT') | 审计账户权限独立 |

**Oracle特有配置：**

-- 查看所有角色

```
SELECT role, common, enabled, default_roleFROM DBA_ROLESORDER BY role;
```

-- 查看角色分配（用户-角色映射）

```
SELECT grantee, granted_role, admin_option, default_roleFROM DBA_ROLE_PRIVSWHERE admin_option = 'YES'ORDER BY grantee;
```

-- 查看系统权限分配

```
SELECT grantee, privilege, admin_optionFROM DBA_SYS_PRIVSWHERE privilege IN ('DBA', 'SYSDBA', 'SYSOPER', 'RESOURCE','CONNECT', 'SELECT ANY TABLE', 'INSERT ANY TABLE','UPDATE ANY TABLE', 'DELETE ANY TABLE','DROP ANY TABLE', 'CREATE ANY TABLE','ALTER ANY TABLE', 'EXECUTE ANY PROCEDURE')ORDER BY grantee, privilege;
```

-- 查看表级对象权限

```
SELECT grantee, owner, table_name, privilege, grant_optionFROM DBA_TAB_PRIVSWHERE privilege IN ('SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'ALTER')ORDER BY grantee, owner, table_name;
```

-- 查看权限授予的权限（grant option分析）

```
SELECT grantee, owner, table_name, privilegeFROM DBA_TAB_PRIVSWHERE grant_option = 'YES';
```

-- 查看谁拥有审计权限

```
SELECT username, account_status, granted_roleFROM DBA_USERS uJOIN DBA_ROLE_PRIVS r ON u.username = r.granteeWHERE r.granted_role IN ('AUDIT', 'AUDIT_VIEW_ROLE', 'DBA');
```

-- 查看角色继承关系

```
SELECT role, parentFROM ROLE_ROLE_PRIVSORDER BY role;
```

**2.2 安全策略与VPD**

-- 查看VPD（Virtual Private Database）策略

```
SELECT policy_name, object_owner, object_name, policy_type,enabled, static_policy, schema_enabledFROM DBA_POLICIESORDER BY policy_name;
```

-- 查看VPD策略详情

```
SELECT policy_name, object_owner, object_name,policy_function, statement_types, update_checkFROM DBA_POLICIESORDER BY policy_name;
```

-- 查看审计策略（Unified Auditing, Oracle 12c+）

```
SELECT policy_name, policy_type, enabled, audit_type,condition_type, failure_conditionFROM AUDIT_UNIFIED_POLICIESORDER BY policy_name;
```

-- 查看统一审计用户

```
SELECT grantee, audit_system_actions, audit_privilegesFROM AUDIT_UNIFIED_GRANTS;
```

-- 查看统一审计活...