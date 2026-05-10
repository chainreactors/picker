---
title: 等保测评命令——达梦数据库 DM
url: https://mp.weixin.qq.com/s/qzjVhM1UcLEmsS4h1CtEQg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:30.649845
---

# 等保测评命令——达梦数据库 DM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JJfExzHZwzEk1mpGtS2eLkZXahKUwert05bwjYZuBicu1bLeicGx76QicDjXOstvvLA8IKRgicT1zK39F7PPHlWCuG9ApZxMw0IblbIckRXibRxY/0?wx_fmt=jpeg)

# 等保测评命令——达梦数据库 DM

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

根据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合 **达梦数据库 DM8** 官方安全指南及多家测评机构现场实践，给出可直接落地的 **测评命令清单**。

已在 **DM8 2023Q4 / DM8 2024Q1** 环境验证通过，支持 **Standalone / Data Watch / DMDSC / 读写分离集群** 部署模式。

---

## 一、身份鉴别（8.1.4.1）

### 1.1 账户唯一性与密码策略

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 默认账户检查 | `SELECT USERNAME, ACCOUNT_STATUS FROM SYS.DBA_USERS WHERE USERNAME IN ('SYSDBA', 'SYS', 'SYSAUDITOR');` | 修改初始密码，状态为OPEN |
| 空口令检查 | `SELECT USERNAME FROM SYS.DBA_USERS WHERE PASSWORD_VERSIONS IS NULL;` | 无输出 |
| 密码有效期 | `SELECT USERNAME, EXPIRY_DATE FROM SYS.DBA_USERS WHERE PROFILE='DEFAULT';` | ≤90天 |
| 密码复杂度 | `SELECT * FROM SYS.DBA_PROFILES WHERE PROFILE='DEFAULT' AND RESOURCE_NAME LIKE '%PASSWORD%';` | 启用PWD\_POLICY，长度≥8，复杂度要求 |
| 密码历史 | `SELECT RESOURCE_NAME, LIMIT FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME='PASSWORD_REUSE_MAX';` | ≥12次不可重复 |

**达梦特有配置：**

```
# 查看密码策略参数
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME LIKE '%PWD_POLICY%';

# 查看具体用户密码策略
SELECT USERNAME, PASSWORD_VERSIONS, LOCK_DATE, EXPIRY_DATE
FROM SYS.DBA_USERS WHERE ACCOUNT_STATUS='OPEN';

# 查看用户锁定状态
SELECT USERNAME, ACCOUNT_STATUS, LOCK_DATE, EXPIRY_DATE
FROM SYS.DBA_USERS WHERE ACCOUNT_STATUS='LOCKED';

# 查看审计用户（SYSAUDITOR）配置
SELECT USERNAME, ACCOUNT_STATUS FROM SYS.DBA_USERS WHERE USERNAME='SYSAUDITOR';
```

---

### 1.2 登录失败处理与会话超时

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 登录失败锁定 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='FAILED_LOGIN_ATTEMPTS';` | 5-10次 |
| 锁定时间 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='PASSWORD_LOCK_TIME';` | ≥30分钟 |
| 会话超时 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='IDLE_TIME';` | 30-60分钟 |
| 连接数限制 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='MAX_SESSIONS';` | 根据业务设置 |

**达梦特有配置：**

```
# 查看登录失败处理参数
SELECT PARA_NAME, PARA_VALUE, DESCRIPTION
FROM V$DM_INI
WHERE PARA_NAME IN ('FAILED_LOGIN_ATTEMPTS', 'PASSWORD_LOCK_TIME', 'IDLE_TIME', 'CONN_IDLE_TIME');

# 查看当前会话信息
SELECT SESS_ID, SQL_ID, STATE, CREATE_TIME, CLNT_IP, CURR_SCH
FROM V$SESSIONS WHERE STATE='ACTIVE';

# 查看空闲会话
SELECT SESS_ID, CLNT_IP, CURR_SCH, LAST_SEND_TIME
FROM V$SESSIONS
WHERE DATEDIFF(MINUTE, LAST_SEND_TIME, SYSDATE) > 30;

# 强制断开空闲会话（测试用）
-- ALTER SYSTEM KILL SESSION 'SESS_ID';
```

---

### 1.3 远程管理安全

```
# 查看监听配置
SELECT * FROM V$DM_INI WHERE PARA_NAME LIKE '%LISTEN%';

# 查看当前连接来源IP
SELECT DISTINCT CLNT_IP, COUNT(*) AS CONN_COUNT
FROM V$SESSIONS
GROUP BY CLNT_IP
ORDER BY CONN_COUNT DESC;

# 查看是否启用SSL连接
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='ENABLE_ENCRYPT';

# 查看通信加密配置
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME LIKE '%COMM_ENCRYPT%';

# 查看管理工具IP限制（通过登录触发器或防火墙）
SELECT TRIGGER_NAME, STATUS FROM SYS.DBA_TRIGGERS WHERE TRIGGER_NAME LIKE '%LOGIN%';
```

> **高风险项**：SYSDBA允许远程直接登录、未启用通信加密、未配置登录IP白名单，直接判定不符合三级要求。

---

### 1.4 双因子认证（高风险项）

**测评方法：**

* **访谈确认**：是否采用"数据库密码+堡垒机/动态口令"组合认证
* **技术核查**：

```
# 检查是否配置证书认证
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='ENABLE_SSL';

# 查看SSL证书配置
SELECT * FROM V$DM_INI WHERE PARA_NAME LIKE '%SSL%';

# 检查是否配置LDAP/AD集成
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME LIKE '%LDAP%';

# 查看外部认证配置
SELECT * FROM SYS.DBA_EXTERNAL_AUTHENTICATION;

# 检查是否配置操作系统认证
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='ENABLE_OS_AUTH';
```

---

## 二、访问控制（8.1.4.2）

### 2.1 账户与权限管理

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 三权分立 | `SELECT USERNAME, ACCOUNT_STATUS FROM SYS.DBA_USERS WHERE USERNAME IN ('SYSDBA', 'SYSAUDITOR', 'SYSSSO');` | 三个独立管理员账户 |
| 角色分离 | `SELECT GRANTEE, GRANTED_ROLE FROM SYS.DBA_ROLE_PRIVS WHERE GRANTEE IN ('SYSDBA', 'SYSAUDITOR', 'SYSSSO');` | 权限不重叠 |
| 对象权限 | `SELECT * FROM SYS.DBA_TAB_PRIVS WHERE GRANTEE NOT IN ('PUBLIC', 'SYSDBA');` | 最小权限原则 |
| 系统权限 | `SELECT * FROM SYS.DBA_SYS_PRIVS WHERE ADMIN_OPTION='YES';` | 无滥用WITH ADMIN OPTION |

**达梦三权分立核查：**

```
# 达梦数据库三权分立核心检查
# SYSDBA: 数据库管理员（系统管理）
# SYSAUDITOR: 安全审计员（审计管理）
# SYSSSO: 安全保密员（安全管理）

-- 检查三权分立账户是否存在
SELECT USERNAME, ACCOUNT_STATUS, CREATED
FROM SYS.DBA_USERS
WHERE USERNAME IN ('SYSDBA', 'SYSAUDITOR', 'SYSSSO');

-- 检查权限分离（关键）
-- SYSDBA不应有审计权限
-- SYSAUDITOR不应有数据管理权限
-- SYSSSO不应有系统运维权限

-- 查看角色授予情况
SELECT GRANTEE, GRANTED_ROLE, ADMIN_OPTION
FROM SYS.DBA_ROLE_PRIVS
WHERE GRANTEE IN ('SYSDBA', 'SYSAUDITOR', 'SYSSSO');

-- 查看系统权限
SELECT GRANTEE, PRIVILEGE, ADMIN_OPTION
FROM SYS.DBA_SYS_PRIVS
WHERE GRANTEE IN ('SYSDBA', 'SYSAUDITOR', 'SYSSSO');

-- 查看对象权限
SELECT GRANTEE, OWNER, TABLE_NAME, PRIVILEGE
FROM SYS.DBA_TAB_PRIVS
WHERE GRANTEE IN ('SYSDBA', 'SYSAUDITOR', 'SYSSSO');
```

---

### 2.2 默认账户清理

```
# 检查默认测试账户
SELECT USERNAME, ACCOUNT_STATUS FROM SYS.DBA_USERS
WHERE USERNAME IN ('TEST', 'DEMO', 'SCOTT', 'HR');

# 检查示例模式
SELECT OWNER FROM SYS.DBA_TABLES WHERE OWNER IN ('DMHR', 'BOOKSHOP', 'OTHER');

# 锁定或删除不必要的账户
-- ALTER USER TEST ACCOUNT LOCK;
-- DROP USER TEST CASCADE;

# 检查PUBLIC角色权限（应最小化）
SELECT TABLE_NAME, PRIVILEGE FROM SYS.DBA_TAB_PRIVS WHERE GRANTEE='PUBLIC';

# 回收PUBLIC过度授权
-- REVOKE ALL ON SYS.DBA_USERS FROM PUBLIC;
```

---

### 2.3 文件系统权限

```
# 检查达梦安装目录权限（Linux环境）
ls -la $DM_HOME/
stat -c '%a %U:%G' $DM_HOME/

# 检查数据文件权限
ls -la $DM_HOME/data/
stat -c '%a %U:%G' $DM_HOME/data/DAMENG/

# 检查关键配置文件
stat -c '%a %U:%G' $DM_HOME/data/DAMENG/dm.ini
stat -c '%a %U:%G' $DM_HOME/data/DAMENG/dm.ctl

# 检查归档日志权限
ls -la $DM_HOME/arch/
stat -c '%a %U:%G' $DM_HOME/arch/

# 检查备份文件权限
ls -la $DM_HOME/bak/
stat -c '%a %U:%G' $DM_HOME/bak/

# 检查日志文件权限
ls -la $DM_HOME/log/
stat -c '%a %U:%G' $DM_HOME/log/dm_DW*.log 2>/dev/null
```

---

## 三、安全审计（8.1.4.3）

### 3.1 审计服务启用

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 审计开关 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='AUDIT_FLAG';` | 1（启用审计） |
| 审计级别 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='AUDIT_LEVEL';` | 2或3（语句级或对象级） |
| 审计日志模式 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='AUDIT_FILE_FULL_MODE';` | 1（按文件大小切换）或2（按时间切换） |
| 审计日志保留 | `SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='AUDIT_MAX_FILE_SIZE';` | ≥50MB，保留≥6个月 |

**达梦审计配置核查：**

```
# 查看审计参数配置
SELECT PARA_NAME, PARA_VALUE, DESCRIPTION
FROM V$DM_INI
WHERE PARA_NAME LIKE '%AUDIT%';

# 关键审计参数说明：
# AUDIT_FLAG: 0-关闭, 1-打开审计
# AUDIT_LEVEL: 0-不审计, 1-只审计成功, 2-语句级, 3-对象级
# AUDIT_FILE_FULL_MODE: 1-按大小切换, 2-按时间切换
# AUDIT_MAX_FILE_SIZE: 单个审计文件大小（MB）

# 查看当前审计配置
SELECT * FROM V$AUDIT_CFG;

# 查看审计记录（需要SYSAUDITOR权限）
SELECT * FROM V$AUDITRECORDS ORDER BY OPTIME DESC FETCH FIRST 20 ROWS ONLY;

# 查看审计日志文件
SELECT * FROM V$AUDIT_FILES ORDER BY CREATE_TIME DESC;

# 查看审计空间使用
SELECT PATH, TOTAL_SIZE, FREE_SIZE FROM V$DISK_SPACE WHERE PATH LIKE '%AUDIT%';
```

---

### 3.2 审计策略与内容

```
# 查看系统级审计规则（SYSAUDITOR执行）
SELECT * FROM SYSAUDITOR.SYSAUDIT;

# 查看语句级审计规则
SELECT * FROM SYSAUDITOR.SYSAUDITSQL;

# 查看对象级审计规则
SELECT * FROM SYSAUDITOR.SYSAUDITOBJECT;

# 查看审计用户
SELECT * FROM SYSAUDITOR.SYSAUDITUSER;

# 配置关键操作审计（示例）
-- 审计所有DDL操作
AUDIT DDL;

-- 审计特定表
AUDIT SELECT, INSERT, UPDATE, DELETE ON SCHEMA.TABLE;

-- 审计特权用户
AUDIT ALL PRIVILEGES BY SYSDBA;

-- 审计登录失败
AUDIT CONNECT WHENEVER NOT SUCCESSFUL;
```

---

### 3.3 审计日志保护

```
# 检查审计日志文件权限（Linux）
ls -la $DM_HOME/data/DAMENG/AUDIT/
stat -c '%a %U:%G' $DM_HOME/data/DAMENG/AUDIT/*.log 2>/dev/null | head -5

# 查看审计日志是否加密
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='AUDIT_ENCRYPT';

# 查看审计日志是否压缩
SELECT PARA_NAME, PARA_VALUE FROM V$DM_INI WHERE PARA_NAME='AUDIT_COMPRESS';

# 检查审计日志备份
ls -la /backup/dm/audit/ 2>/dev/nul...