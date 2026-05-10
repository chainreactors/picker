---
title: 等保测评命令——神州数据库
url: https://mp.weixin.qq.com/s/sXx9_uas4yCiS_HV5rVqSw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:39.685258
---

# 等保测评命令——神州数据库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JJfExzHZwzELOMTIcNWQTlicicHLQxrApjz8pAdFGkpWOwOVrkZMYcWygjms0vIcE65kQC2UarFXMIhx8MicUFG9gUZdHAFyd0tP9sarxUdt6E/0?wx_fmt=jpeg)

# 等保测评命令——神州数据库

Sec Online

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于汪汪虚拟空间
，作者初恋是小马

![](http://wx.qlogo.cn/mmhead/ibkKkoaQFco6tfIIq0gLqqv5a4nPiawT7sTia17cAoV5PMialOoAaWjZmUkGGYaR1EibW0qAX5StwTXU/0)

**汪汪虚拟空间**
.

汪汪·虚拟空间｜专注学习分享这里有计算机、数学、英语等干货笔记愿你在这里，找到需要的知识，遇见更好的自己

各位大佬，想看那种网络设备/操作系统/数据库/中间件的**测评命令清单，可在留言区留言，我会以最快速度给你们总结，然后发出来！**

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合神州数据库官方安全指南及现场测评实践。

**适用版本**：ShenzhouDB V2.0 / V3.0 / V4.0（基于PostgreSQL 11/12/14深度定制）

---

## 一、身份鉴别（8.1.4.1）

### 1.1 数据库账户与口令策略

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级管理员账户 | `szsql -U szadmin -c "SELECT * FROM pg_user WHERE usesysid=10;"` | szadmin账户受控 |
| 空口令检查 | `szsql -U szadmin -c "SELECT usename FROM pg_user WHERE passwd IS NULL;"` | 无输出 |
| 弱口令检查 | `szsql -U szadmin -c "SELECT usename FROM pg_shadow WHERE passwd LIKE '%md5%' AND length(passwd)<35;"` | 无输出 |
| 密码复杂度 | `szsql -U szadmin -c "SHOW passwordcheck.enable;"` | on |
| 密码有效期 | `szsql -U szadmin -c "SELECT usename, valuntil FROM pg_shadow WHERE valuntil IS NOT NULL;"` | ≤90天 |
| 密码历史 | `szsql -U szadmin -c "SHOW sz_password_reuse_max;"` | ≥5次 |
| 登录失败锁定 | `szsql -U szadmin -c "SHOW sz_login_lock_max_failed;"` | ≤5次 |
| 锁定时间 | `szsql -U szadmin -c "SHOW sz_login_lock_duration;"` | ≥30分钟 |

**神州数据库特有配置：**

```
# 连接数据库（需先切换到szuser用户或配置环境变量）
su - szuser
szsql -U szadmin -d szdb -W

# 查看所有用户及状态
SELECT usename, usesuper, usecreatedb, valuntil,
       CASE WHEN passwd LIKE 'md5%' THEN 'md5'
            WHEN passwd LIKE 'SCRAM-SHA-256%' THEN 'scram-sha-256'
            ELSE '其他' END as pwd_type,
passwd IS NULL as is_empty
FROM pg_user;

# 查看密码策略详细配置（神州特有插件）
SHOW passwordcheck;
SHOW passwordcheck.min_length;        -- 最小长度≥8
SHOW passwordcheck.min_upper;         -- 大写字母≥1
SHOW passwordcheck.min_lower;         -- 小写字母≥1
SHOW passwordcheck.min_digit;         -- 数字≥1
SHOW passwordcheck.min_special;       -- 特殊字符≥1

# 查看神州数据库特有安全参数
SHOW sz_security;
SHOW sz_login_lock;                   -- 登录失败锁定开关
SHOW sz_login_lock_max_failed;        -- 最大失败次数（默认5）
SHOW sz_login_lock_duration;          -- 锁定时间（秒，默认1800）
SHOW sz_login_lock_auto_unlock;       -- 是否自动解锁

# 查看被锁定的用户（神州特有视图）
SELECT * FROM sz_login_lock_status WHERE is_locked =true;

# 查看用户密码过期信息
SELECT usename,
       CASE WHEN valuntil < NOW() THEN '已过期'
            WHEN valuntil < NOW() + INTERVAL '7 days' THEN '即将过期'
            ELSE '正常' END as pwd_status,
       valuntil as expire_time
FROM pg_shadow
WHERE valuntil IS NOT NULL;
```

### 1.2 远程管理与连接控制

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 监听地址 | `cat ${SZDATA}/postgresql.conf | grep listen_addresses` | 非'\*'或限定IP |
| 端口检查 | `ss -tulnp | grep 5432` | 默认5432，可修改 |
| SSL连接 | `szsql -U szadmin -c "SHOW ssl;"` | on |
| 国密SSL | `szsql -U szadmin -c "SHOW sz_ssl_gm;"` | on（神州特有） |
| 客户端证书 | `ls -la ${SZDATA}/server.crt` | 存在且权限600 |
| 最大连接数 | `szsql -U szadmin -c "SHOW max_connections;"` | 根据业务配置 |

**神州数据库特有配置：**

```
# 查看数据库监听配置
cat${SZDATA}/postgresql.conf |grep-E'listen_addresses|port|ssl'

# 查看SSL详细配置
SHOW ssl_cert_file;      -- 证书路径
SHOW ssl_key_file;       -- 私钥路径
SHOW ssl_ca_file;        -- CA证书
SHOW ssl_crl_file;       -- 吊销列表
SHOW ssl_ciphers;        -- 加密算法

# 查看神州数据库国密SSL配置（V3.0+支持）
SHOW sz_ssl_gm;          -- 国密SSL开关
SHOW sz_ssl_gm_cert_file;    -- 国密证书
SHOW sz_ssl_gm_key_file;     -- 国密私钥
SHOW sz_ssl_gm_ciphers;      -- 国密算法套件（SM2/SM3/SM4）

# 查看当前连接情况
SELECT client_addr, usename, state, backend_start, query_start,
       ssl, ssl_version, ssl_cipher, ssl_client_dn
FROM pg_stat_activity
WHERE client_addr IS NOT NULL;

# 查看认证配置文件（神州数据库支持pg_hba.conf扩展）
cat${SZDATA}/pg_hba.conf
# 核查要点：
# - 拒绝trust认证方式
# - 拒绝host all all 0.0.0.0/0 md5
# - 采用hostssl强制SSL连接
# - 优先使用scram-sha-256认证

# 查看神州数据库扩展认证方式
cat${SZDATA}/sz_hba.conf 2>/dev/null  # 神州特有扩展认证配置
```

### 1.3 双因子认证（高风险项）

```
# 检查是否启用证书认证
cat${SZDATA}/pg_hba.conf |grep cert
cat${SZDATA}/sz_hba.conf 2>/dev/null |grep cert

# 检查是否集成外部认证（LDAP/RADIUS/AD）
SHOW ldapserver;          -- LDAP服务器
SHOW ldapport;            -- LDAP端口
SHOW ldapbasedn;          -- LDAP基础DN

# 检查RADIUS认证配置（神州特有）
SHOW sz_radius_server;
SHOW sz_radius_secret;
SHOW sz_radius_port;

# 检查国密证书认证（神州特有）
SHOW sz_gm_cert_auth;
cat${SZDATA}/sz_cert.conf 2>/dev/null  # 国密证书映射配置

# 检查审计是否记录认证事件
SHOW log_connections;
SHOW log_disconnections;
SHOW sz_audit_log_auth;   -- 神州特有认证审计开关
```

---

## 二、访问控制（8.1.4.2）

### 2.1 账户权限管理

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级用户数量 | `szsql -U szadmin -c "SELECT usename FROM pg_user WHERE usesuper='t';"` | ≤2个 |
| 默认账户处理 | `szsql -U szadmin -c "SELECT usename FROM pg_user WHERE usename IN ('szadmin', 'szuser', 'postgres');"` | 已修改默认口令 |
| 角色分离 | `szsql -U szadmin -c "SELECT rolname FROM pg_roles;"` | 存在安全管理员、审计管理员 |
| 权限授予 | `szsql -U szadmin -c "\dp *.*"` | 最小权限原则 |

**神州数据库特有配置：**

```
# 查看三权分立配置（神州数据库核心安全特性）
SHOW sz_sepofpowers;  -- 是否启用三权分立

# 查看安全管理员（szsso）配置
szsql -U szsso -c"SELECT current_user;"

# 查看审计管理员（szsao）配置
szsql -U szsao -c"SELECT current_user;"

# 查看系统管理员（szadmin）权限限制
-- 启用三权分立后，szadmin不能查看审计日志，不能修改安全策略

# 查看所有角色及成员关系
SELECT r.rolname, r.rolsuper, r.rolinherit,
       ARRAY(SELECT b.rolname
             FROM pg_catalog.pg_auth_members m
             JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid)
             WHERE m.member = r.oid) as memberof
FROM pg_catalog.pg_roles r
WHERE r.rolname !~ '^pg_';

# 查看对象权限详情
SELECT grantor, grantee, table_schema, table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee NOT IN ('PUBLIC', 'szadmin');

# 检查PUBLIC角色权限（应回收PUBLIC对敏感表的权限）
SELECT * FROM information_schema.table_privileges WHERE grantee='PUBLIC';

# 查看神州数据库特有安全角色
SELECT rolname FROM pg_roles WHERE rolname LIKE 'sz_%';
-- sz_security_admin: 安全管理员角色
-- sz_audit_admin: 审计管理员角色
-- sz_backup_admin: 备份管理员角色
```

### 2.2 敏感数据访问控制

```
# 查看行级安全策略（RLS）配置
SELECT schemaname, tablename, rowsecurity FROM pg_tables WHERE rowsecurity=true;

# 查看具体RLS策略
SELECT * FROM pg_policies;

# 查看列级加密配置（神州数据库特有透明加密）
SHOW sz_transparent_encrypt;
SHOW sz_transparent_encrypt_kms_url;    -- 密钥管理服务URL
SHOW sz_transparent_encrypt_algorithm;  -- 加密算法（SM4/AES256）

# 查看加密表空间
SELECT spcname, spcencrypt FROM pg_tablespace WHERE spcencrypt =true;

# 查看数据脱敏配置（神州数据库特有动态脱敏）
SELECT * FROM sz_redaction_policies;
SELECT * FROM sz_redaction_columns;

# 查看脱敏策略详情
SELECT policy_name, table_name, column_name, function_type, expression
FROM sz_redaction_policies sp
JOIN sz_redaction_columns sc ON sp.policy_id = sc.policy_id;
```

---

## 三、安全审计（8.1.4.3）

### 3.1 审计服务启用

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 审计开关 | `szsql -U szsao -c "SHOW sz_audit.enable;"` | on |
| 审计模式 | `szsql -U szsao -c "SHOW sz_audit.mode;"` | all或std |
| 审计日志路径 | `szsql -U szsao -c "SHOW sz_audit.log_directory;"` | 非数据目录，独立磁盘 |
| 审计日志格式 | `szsql -U szsao -c "SHOW sz_audit.log_format;"` | csv或json |
| 审计日志保留 | `szsql -U szsao -c "SHOW sz_audit.log_rotation_age;"` | ≥6个月 |

**神州数据库特有配置：**

```
# 查看神州数据库审计总开关（需用szsao登录）
SHOW sz_audit;

# 查看审计详细配置
SHOW sz_audit.log;                    -- 审计日志总开关
SHOW sz_audit.log_catalog;            -- 是否审计系统表
SHOW sz_audit.log_level;                -- 审计级别（DEBUG/INFO/WARNING/ERROR）
SHOW sz_audit.log_connections;          -- 审计连接
SHOW sz_audit.log_disconnections;       -- 审计断开
SHOW sz_audit.log_ddl;                  -- 审计DDL
SHOW sz_audit.log_dml;                  -- 审计DML
SHOW sz_audit.log_select;               -- 审计查询
SHOW sz_audit.log_parameter;            -- 审计参数
SHOW sz_audit.log_statement_once;       -- 是否单次记录

# 查看神州数据库特有审计功能
SHOW sz_audit_log_admin;                -- 审计管理员操作
SHOW sz_audit_log_security;             -- 审计安全操作
SHOW sz_audit_log_privilege;            -- 审计权限变更
SHOW sz_audit_log_object;               -- 审计对象访问

# 查看审计规则（精细化审计）
SELECT * FROM sz_audit_rules;

# 查看审计对象配置
SELECT * FROM sz_audit_objects;

# 查看审计用户配置
SELECT * FROM sz_audit_users;

# ...