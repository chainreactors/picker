---
title: 等保测评命令——人大金仓数据库
url: https://mp.weixin.qq.com/s/UUDCWOKWrjgQV-LLESxTZg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:34.921109
---

# 等保测评命令——人大金仓数据库

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JJfExzHZwzFchS18ZMKWib2cOCmm8u5qY72szWE0Fh0aIuAC26NUFic9lB5dQctyE697LEKb5Y0oAhRC6B93QPInM7PSxt2Bha9no0CTsjl2A/0?wx_fmt=jpeg)

# 等保测评命令——人大金仓数据库

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

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合金仓数据库官方安全指南及现场测评实践，给出可直接落地的测评命令清单。

**适用版本**：KingbaseES V8R3 / V8R6 / V8R9

---

## 一、身份鉴别（8.1.4.1）

### 1.1 数据库账户与口令策略

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级管理员账户 | `ksql -U system -W -c "SELECT * FROM sys_user WHERE usesysid=10;"` | system账户受控 |
| 空口令检查 | `ksql -U system -W -c "SELECT usename FROM sys_user WHERE passwd IS NULL;"` | 无输出 |
| 弱口令检查 | `ksql -U system -W -c "SELECT usename FROM sys_user WHERE passwd LIKE '%md5%' AND length(passwd)<35;"` | 无输出 |
| 密码复杂度 | `ksql -U system -W -c "SHOW passwordcheck.enable;"` | on |
| 密码有效期 | `ksql -U system -W -c "SHOW passwordcheck.password_valid_until;"` | ≤90天 |
| 密码历史 | `ksql -U system -W -c "SHOW passwordcheck.password_reuse_max;"` | ≥5次 |
| 登录失败锁定 | `ksql -U system -W -c "SHOW sysaudit.login_lock_max_failed;"` | ≤5次 |
| 锁定时间 | `ksql -U system -W -c "SHOW sysaudit.login_lock_duration;"` | ≥30分钟 |

**金仓特有配置：**

```
# 连接数据库（需先切换到kingbase用户）
su - kingbase
ksql -U system -dtest-W

# 查看所有用户及状态
SELECT usename, usesuper, usecreatedb, valuntil,
       CASE WHEN passwd LIKE 'md5%' THEN 'md5' ELSE '其他' END as pwd_type
FROM sys_user;

# 查看密码策略详细配置
SHOW passwordcheck;
SHOW passwordcheck.min_length;        -- 最小长度≥8
SHOW passwordcheck.min_upper_case;    -- 大写字母≥1
SHOW passwordcheck.min_lower_case;    -- 小写字母≥1
SHOW passwordcheck.min_digit;         -- 数字≥1
SHOW passwordcheck.min_special;       -- 特殊字符≥1

# 查看登录失败锁定配置
SHOW sysaudit.login_lock;
SHOW sysaudit.login_lock_max_failed;  -- 最大失败次数
SHOW sysaudit.login_lock_duration;    -- 锁定时间（秒）
SHOW sysaudit.login_lock_auto_unlock; -- 是否自动解锁

# 查看被锁定的用户
SELECT * FROM sysaudit.sysaudit_login_lock WHERE is_locked =true;
```

### 1.2 远程管理与连接控制

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 监听地址 | `cat ${KINGBASE_DATA}/kingbase.conf | grep listen_addresses` | 非'\*'或限定IP |
| 端口检查 | `ss -tulnp | grep 54321` | 默认54321，可修改 |
| SSL连接 | `ksql -U system -W -c "SHOW ssl;"` | on |
| 客户端证书 | `ls -la ${KINGBASE_DATA}/server.crt` | 存在且权限600 |
| 最大连接数 | `ksql -U system -W -c "SHOW max_connections;"` | 根据业务配置 |

**金仓特有配置：**

```
# 查看数据库监听配置
cat${KINGBASE_DATA}/kingbase.conf |grep-E'listen_addresses|port|ssl'

# 查看SSL详细配置
SHOW ssl_cert_file;      -- 证书路径
SHOW ssl_key_file;       -- 私钥路径
SHOW ssl_ca_file;        -- CA证书
SHOW ssl_crl_file;       -- 吊销列表
SHOW ssl_ciphers;        -- 加密算法

# 查看当前连接情况
SELECT client_addr, usename, state, backend_start, query_start
FROM sys_stat_activity
WHERE client_addr IS NOT NULL;

# 查看认证配置文件
cat${KINGBASE_DATA}/sys_hba.conf
# 核查要点：
# - 拒绝trust认证方式
# - 拒绝host all all 0.0.0.0/0 md5
# - 采用hostssl强制SSL连接
```

### 1.3 双因子认证（高风险项）

```
# 检查是否启用证书认证
cat${KINGBASE_DATA}/sys_hba.conf |grep cert

# 检查是否集成外部认证（LDAP/RADIUS/AD）
ksql -U system -W-c"SHOW krb_server_keyfile;"# Kerberos
ksql -U system -W-c"SHOW ldapserver;"# LDAP

# 检查审计是否记录认证事件
ksql -U system -W-c"SHOW sysaudit.enable;";
ksql -U system -W-c"SHOW sysaudit.log_connections;";
```

---

## 二、访问控制（8.1.4.2）

### 2.1 账户权限管理

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级用户数量 | `ksql -U system -W -c "SELECT usename FROM sys_user WHERE usesuper='t';"` | ≤2个 |
| 默认账户处理 | `ksql -U system -W -c "SELECT usename FROM sys_user WHERE usename IN ('kingbase', 'system');"` | 已修改默认口令 |
| 角色分离 | `ksql -U system -W -c "SELECT rolname FROM sys_roles;"` | 存在安全管理员、审计管理员 |
| 权限授予 | `ksql -U system -W -c "\dp *.*"` | 最小权限原则 |

**金仓特有配置：**

```
# 查看三权分立配置（金仓特有安全特性）
SHOW sepofpowers;  -- 是否启用三权分立

# 查看安全管理员（sso）配置
ksql -U sso -W-c"SELECT current_user;"

# 查看审计管理员（sao）配置
ksql -U sao -W-c"SELECT current_user;"

# 查看所有角色及成员关系
SELECT r.rolname, ARRAY(SELECT b.rolname
       FROM sys_catalog.sys_auth_members m
       JOIN sys_catalog.sys_roles b ON (m.roleid = b.oid)
       WHERE m.member = r.oid) as memberof
FROM sys_catalog.sys_roles r
WHERE r.rolname !~ '^pg_';

# 查看对象权限详情
SELECT grantor, grantee, table_schema, table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee NOT IN ('PUBLIC', 'system');

# 检查PUBLIC角色权限
SELECT * FROM information_schema.table_privileges WHERE grantee='PUBLIC';
-- 应回收PUBLIC对敏感表的权限
```

### 2.2 敏感数据访问控制

```
# 查看行级安全策略（RLS）配置
SELECT schemaname, tablename, rowsecurity FROM sys_tables WHERE rowsecurity=true;

# 查看具体RLS策略
SELECT * FROM sys_policies;

# 查看列级加密配置（金仓特有）
SHOW transparent_encrypt;
SHOW transparent_encrypt_kms_url;

# 查看数据脱敏配置（金仓特有）
SELECT * FROM sys_redaction_policies;
SELECT * FROM sys_redaction_columns;
```

---

## 三、安全审计（8.1.4.3）

### 3.1 审计服务启用

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 审计开关 | `ksql -U system -W -c "SHOW sysaudit.enable;"` | on |
| 审计模式 | `ksql -U system -W -c "SHOW sysaudit.mode;"` | all或std |
| 审计日志路径 | `ksql -U system -W -c "SHOW sysaudit.log_directory;"` | 非数据目录，独立磁盘 |
| 审计日志格式 | `ksql -U system -W -c "SHOW sysaudit.log_format;"` | csv或json |
| 审计日志保留 | `ksql -U system -W -c "SHOW sysaudit.log_rotation_age;"` | ≥6个月 |

**金仓特有配置：**

```
# 查看审计总开关
SHOW sysaudit;

# 查看审计详细配置
SHOW sysaudit.log;                    -- 审计日志总开关
SHOW sysaudit.log_catalog;            -- 是否审计系统表
SHOW sysaudit.log_level;              -- 审计级别
SHOW sysaudit.log_connections;        -- 审计连接
SHOW sysaudit.log_disconnections;     -- 审计断开
SHOW sysaudit.log_ddl;                -- 审计DDL
SHOW sysaudit.log_dml;                -- 审计DML
SHOW sysaudit.log_select;             -- 审计查询
SHOW sysaudit.log_parameter;          -- 审计参数

# 查看审计规则（精细化审计）
SELECT * FROM sysaudit.sysaudit_rules;

# 查看审计日志文件
ls-la${KINGBASE_DATA}/sysaudit/ 2>/dev/null ||ls-la /var/lib/kingbase/sysaudit/

# 查看审计日志内容（CSV格式）
head-5${KINGBASE_DATA}/sysaudit/sysaudit-*.csv

# 审计日志大小检查
du-sh${KINGBASE_DATA}/sysaudit/

# 查看审计表空间（应独立表空间）
SELECT spcname FROM sys_tablespace WHERE spcname='sysaudit';
```

### 3.2 审计记录保护

```
# 检查审计日志权限
ls-la${KINGBASE_DATA}/sysaudit/sysaudit-*.csv
# 应：640 kingbase:kingbase

# 检查审计日志是否定期归档
crontab-l|grep sysaudit
ls /backup/sysaudit/ 2>/dev/null

# 查看审计日志自动清理配置
SHOW sysaudit.log_truncate_on_rotation;
SHOW sysaudit.log_rotation_age;
SHOW sysaudit.log_rotation_size;

# 检查审计管理员权限（仅能查询审计日志，不能修改）
ksql -U sao -W-c"SELECT * FROM sysaudit.sysaudit_log LIMIT 5;"
```

---

## 四、入侵防范（8.1.4.4）

### 4.1 数据库加固与漏洞修复

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 版本补丁 | `ksql -U system -W -c "SELECT version();"` | 最新稳定版本 |
| 危险函数 | `ksql -U system -W -c "SELECT proname FROM sys_proc WHERE proname IN ('pg_read_file', 'pg_ls_dir', 'copy_from_program');"` | 已回收权限 |
| 扩展插件 | `ksql -U system -W -c "SELECT * FROM sys_extension;"` | 仅安装可信扩展 |
| 外部表 | `ksql -U system -W -c "SELECT * FROM sys_foreign_data_wrapper;"` | 受控使用 |

**金仓特有配置：**

```
# 查看数据库版本及补丁
SELECT version();
SHOW server_version;
SHOW server_version_num;

# 检查危险存储过程
SELECT proname, prosrc FROM sys_proc
WHERE proname IN ('pg_read_file', 'pg_read_binary_file', 'pg_ls_dir',
'pg_database_size', 'pg_relation_size', 'pg_size_pretty')
AND prosecdef =true;

# 检查COPY PROGRAM权限（高危命令）
SHOW allow_system_table_mods;  -- 应为off

# 检查外部数据封装器
SELECT fdwname, fdwowner::regrole, fdwoptions FROM sys_foreign_data_wrapper;

# 检查dblink和file_fdw（可能用于越权访问）
SELECT * FROM sys_extension WHERE extname IN ('dblink', 'file_fdw', 'postgres_fdw');

# 检查自定义函数安全性
SELECT n.nspname, p.proname, p.prosecdef, p.proowner::regrole
FROM sys_proc p JOIN sys_namespace n ON p.pronamespace = n.oid
WHERE n.nspname NOT IN ('pg_catalog', 'information_schema', 'sys_catalog')
AND p.prosecdef =true;  -- 安全定义者函数需重点审查
```

### 4.2 资源限制与防护

```
# 查看资源限制配置
SHOW max_connections;           -- 最大连接数
SHOW superuser_reserved_connections;  -- 超级用户保留连接

#...