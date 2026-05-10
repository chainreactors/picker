---
title: 等保测评命令——南大通用数据库GBase
url: https://mp.weixin.qq.com/s/kMKOHb7IZrQVXaFP13_a3Q
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:42.811595
---

# 等保测评命令——南大通用数据库GBase

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JJfExzHZwzHKEWicLKfIgugMVM9ibSacaic2zibzKM6mgicwOfTsvrIibickMHfYK35zLTpvKp1mtXJwCtoLDd35GKtp67whgo1L9N9o2mHgS0QfJ0/0?wx_fmt=jpeg)

# 等保测评命令——南大通用数据库GBase

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

各位大佬，想看那种网络设备/操作系统/数据库/中间件的**测评命令清单，可在留言区留言！**

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合南大通用各产品官方安全指南及现场测评实践。

**适用产品**：GBase 8a MPP Cluster / GBase 8s / GBase 8c / GBase XDM

---

## 一、GBase 8a MPP Cluster（分析型数据库）

### 1.1 身份鉴别

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级管理员 | `gccli -u root -p -e "SELECT * FROM gbase.user WHERE user='root';"` | root账户受控 |
| 空口令检查 | `gccli -e "SELECT user FROM gbase.user WHERE authentication_string='';"` | 无输出 |
| 密码复杂度 | `gccli -e "SHOW VARIABLES LIKE 'validate_password%';"` | 启用策略 |
| 密码有效期 | `gccli -e "SELECT user, password_lifetime FROM gbase.user;"` | ≤90天 |
| 登录失败锁定 | `gccli -e "SHOW VARIABLES LIKE 'gbase_login_lock%';"` | 启用锁定 |
| 连接加密 | `gccli -e "SHOW VARIABLES LIKE 'ssl%';"` | 启用SSL |

**GBase 8a特有配置：**

```
# 连接GBase 8a（coordinator节点）
gccli -u root -p-h192.168.1.100 -P5258

# 查看所有用户及认证方式
SELECT
    user,
    host,
    authentication_string,
    plugin,
    password_lifetime,
    account_locked,
    password_expired
FROM gbase.user;

# 查看密码策略详细配置（GBase 8a V9.5+）
SHOW VARIABLES LIKE 'validate_password%';
-- validate_password_policy=MEDIUM（策略级别）
-- validate_password_length=8（最小长度）
-- validate_password_mixed_case_count=1（大小写）
-- validate_password_number_count=1（数字）
-- validate_password_special_char_count=1（特殊字符）

# 查看登录失败锁定配置（GBase特有）
SHOW VARIABLES LIKE 'gbase_login_lock%';
-- gbase_login_lock_enabled=ON（启用锁定）
-- gbase_login_lock_max_failed=5（最大失败次数）
-- gbase_login_lock_duration=1800（锁定时间秒）

# 查看被锁定账户
SELECT user, host, account_locked, lock_time
FROM gbase.user
WHERE account_locked='Y';

# 查看SSL配置
SHOW VARIABLES LIKE 'ssl%';
SHOW VARIABLES LIKE 'require_secure_transport';

# 查看当前连接加密状态
SELECT
    id,
    user,
    host,
    ssl_type,
    ssl_cipher
FROM gbase.processlist
WHERE ssl_type IS NOT NULL;
```

### 1.2 访问控制

```
-- 查看GBase 8a权限系统（类似MySQL但增强）
SELECT
user,
    host,
    Select_priv,
    Insert_priv,
    Update_priv,
    Delete_priv,
    Create_priv,
    Drop_priv,
    Grant_priv,
    Super_priv
FROM gbase.user
WHEREuserNOTIN('gbase','root');

-- 查看数据库级权限
SELECT
    host,
    db,
user,
    Select_priv,
    Insert_priv,
    Create_priv
FROM gbase.db;

-- 查看表级权限
SELECT
    host,
    db,
user,
    table_name,
    table_priv
FROM gbase.tables_priv;

-- 查看GBase 8a特有角色（V9.5+）
SELECT
    role_name,
    role_type,
    is_default
FROM gbase.roles;

-- 查看用户角色映射
SELECT
user,
    host,
    role_name
FROM gbase.role_edges;

-- 查看资源队列（GBase 8a特有，用于访问控制）
SELECT
    queue_name,
    priority,
    max_memory,
    max_cpu,
    max_concurrency
FROM gbase.queues;

-- 查看用户资源限制
SELECT
user,
    max_queries_per_hour,
    max_updates_per_hour,
    max_connections_per_hour,
    max_user_connections
FROM gbase.user_resources;
```

### 1.3 安全审计

```
-- 查看审计总开关（GBase 8a企业版）
SHOW VARIABLES LIKE'gbase_audit%';

-- 查看审计详细配置
SHOW VARIABLES LIKE'gbase_audit_log%';
-- gbase_audit_log=ON（审计开关）
-- gbase_audit_log_file=/var/log/gbase/audit.log（审计文件路径）
-- gbase_audit_log_format=JSON（审计格式）
-- gbase_audit_log_buffer_size=16M（缓冲区大小）
-- gbase_audit_log_rotate_on_size=100M（轮转大小）
-- gbase_audit_log_rotations=10（保留文件数）

-- 查看审计规则（精细化审计）
SELECT
    audit_id,
    user_name,
    host_name,
    db_name,
    table_name,
    operation_type,
    enabled
FROM gbase.audit_rules;

-- 查看审计日志内容（需审计管理员权限）
SELECT
    event_time,
    user_name,
    host_name,
    operation_type,
    db_name,
    table_name,
    sql_text,
    return_code
FROM gbase.audit_log
WHERE event_time > DATE_SUB(NOW(),INTERVAL7DAY)
ORDERBY event_time DESC
LIMIT100;

-- 查看审计日志文件（操作系统层）
-- ls -la /var/log/gbase/audit*.log
-- 权限应为640 gbase:gbase
```

### 1.4 数据安全与加密

```
-- 查看透明加密配置（GBase 8a企业版）
SHOW VARIABLES LIKE'gbase_encrypt%';

-- 查看列级加密（GBase特有）
SELECT
    table_schema,
    table_name,
    column_name,
    encryption_algorithm
FROM gbase.encrypted_columns;

-- 查看数据脱敏策略（GBase 8a V9.5+）
SELECT
    policy_name,
    table_schema,
    table_name,
    column_name,
    mask_function
FROM gbase.masking_policies;

-- 查看脱敏策略应用
SELECT
    user_name,
    policy_name,
    grant_option
FROM gbase.masking_grants;
```

---

## 二、GBase 8s（事务型数据库，基于Informix）

### 2.1 身份鉴别

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级管理员 | `dbaccess -e -c "SELECT * FROM sysusers WHERE usertype='DBA';"` | informix/管理员受控 |
| 操作系统认证 | `onstat -c | grep DBSERVERALIAS` | 优先使用OS认证 |
| 口令复杂度 | 检查INFORMIXDIR/etc/ONCONFIG | 启用复杂度和过期 |
| 登录失败 | `onstat -u | grep -i locked` | 锁定策略生效 |
| 连接加密 | `onstat -c | grep SSL` | 启用SSL |

**GBase 8s特有配置：**

```
# 设置GBase 8s环境变量
exportGBASEDBTSERVER=gbase8s
exportGBASEDBTDIR=/opt/gbase8s
exportPATH=$GBASEDBTDIR/bin:$PATH
exportINFORMIXDIR=$GBASEDBTDIR
exportONCONFIG=onconfig.gbase8s

# 连接GBase 8s
dbaccess - -

# 查看数据库管理员（DBA）
SELECT
    username,
    usertype,
    priority
FROM sysusers
WHERE usertype IN ('DBA', 'DBSA', 'DBSSO', 'AAO');

-- GBase 8s特有权限角色：
-- DBA: 数据库管理员
-- DBSA: 数据库系统管理员
-- DBSSO: 数据库安全官（审计）
-- AAO: 审计分析官

# 查看用户认证方式
SELECT
    username,
    usertype,
    password,
    locked
FROM sysusers
WHERE username NOT LIKE 'public%';

# 查看密码策略（通过onconfig文件）
onstat -c|grep-E'PASSWORD|LOCK|SECURITY'

# 关键配置项：
-- DBSERVERALIAS: 监听别名
-- DB_LOCALE: 本地字符集
-- CLIENT_LOCALE: 客户端字符集
-- SECURITY_LOCALE: 安全策略
-- PASSWORD_HISTORY: 密码历史
-- PASSWORD_MIN_LENGTH: 最小长度
-- PASSWORD_MAX_AGE: 最大有效期
-- FAILED_LOGIN_ATTEMPTS: 失败尝试次数
-- LOCKOUT_TIME: 锁定时间

# 查看SSL配置
onstat -c|grep-i ssl
onstat -g ssl  # 查看SSL状态

# 查看当前会话
onstat -g ses |head-20
```

### 2.2 访问控制

```
-- 查看数据库级权限
SELECT
    d.grantor,
    d.grantee,
    d.tabauth[1,10],
    d.colauth[1,10]
FROM sysdbauth d;

-- 查看表级权限
SELECT
    t.grantor,
    t.grantee,
    t.tabname,
    t.tabauth
FROM systabauth t
WHERE t.grantee !='public';

-- 查看存储过程权限
SELECT
    p.grantor,
    p.grantee,
    p.procname,
    p.procauth
FROM sysprocauth p;

-- 查看角色（GBase 8s V14+）
SELECT
    rolename,
    owner
FROM sysroleauth;

-- 查看行级安全标签（LBAC，企业版）
SELECT
    labelid,
    labelname,
type
FROM sysseclabels;

-- 查看安全策略
SELECT
    policyid,
    policyname,
type,
    defaultlabel
FROM syssecpolicies;
```

### 2.3 安全审计

```
# 查看审计配置（onconfig）
onstat -c|grep-E'AUDIT|AAO'

# 关键审计配置：
-- ADTFILES: 审计文件数量
-- ADTPATH: 审计文件路径
-- ADTROWS: 审计行数限制
-- ADTMODE: 审计模式（0=关，1=开，2=连续）

# 查看审计日志
ls-la$GBASEDBTDIR/audit/
onaudit -l# 列出审计记录

# 查看审计规则
onaudit -c# 查看当前配置
onaudit -q# 查询审计记录

# 查看审计事件类型
onaudit -e# 查看事件掩码

# 查看AAO（审计分析官）配置
SELECT
    username,
    usertype
FROM sysusers
WHERE usertype ='AAO';
```

### 2.4 数据加密

```
-- 查看列级加密（GBase 8s内置加密）
SELECT
    tabname,
    colname,
    coltype,
    extended_id
FROM syscolumns c
JOIN systables t ON c.tabid = t.tabid
WHERE coltype ='BLOB'-- 加密数据通常存储为BLOB
AND extended_id IN(
SELECT extended_id
FROM sysxtdtypes
WHERE name LIKE'%encrypt%'
);

-- 查看表空间加密（企业版）
SELECT
    name,
    fchunk,
    flags,
    is_encrypted
FROM sysdbspaces
WHERE is_encrypted =1;

-- 查看加密配置
SELECT
    cf_name,
    cf_effective,
    cf_default
FROM sysconfig
WHERE cf_name LIKE'%CRYPTO%'
OR cf_name LIKE'%ENCRYPT%';
```

---

## 三、GBase 8c（分布式数据库，基于PostgreSQL）

### 3.1 身份鉴别

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 超级管理员 | `gsql -U gbase -d postgres -c "\du"` | gbase账户受控 |
| 空口令检查 | `gsql -U gbase -c "SELECT usename FROM pg_user WHERE passwd IS NULL;"` | 无输出 |
| 密码复杂度 | `gsql -U gbase -c "SHOW passwordcheck.enable;"` | on |
| 密码有效期 | `gsql -U gbase -c "SELECT usename, valuntil FROM pg_shadow;"` | ≤90天 |
| 登录失败锁定 | `gsql -U gbase -c "SHOW gbase_login_lock.max_failed;"` | ≤5次 |

**GBase 8c特有配置：**

```
# 连接GBase 8c（coordinator节点）
gsql -U gbase -d postgres -h192.168.1.100 -p5432

# 查看所有用户
SELECT
...