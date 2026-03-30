---
title: 【数据库】PostgreSQL等保核查命令大全｜亲测有效 + 持续更新
url: https://mp.weixin.qq.com/s/-h3DCDmnQgB45BTZBJNv_Q
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:17.675224
---

# 【数据库】PostgreSQL等保核查命令大全｜亲测有效 + 持续更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2r1REgdXKkqxfibYmnrhN1t34NESu6cibJibXY8nz68ODzhwnMISYrg6Ow7NATSJWGYiaDyxbeQPKyuZASGBL4WepVTcNmd0jg1RuR0E3Ca9Pwc/0?wx_fmt=jpeg)

# 【数据库】PostgreSQL等保核查命令大全｜亲测有效 + 持续更新

Sec Online

![]()

在小说阅读器中沉浸阅读

以下文章来源于汤池杂货铺
，作者Fuyuanzi

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5J0Y2dAfZtVROkAVlm3W1h1cT95E1sJ3cFJ0nGNSmcJA/0)

**汤池杂货铺**
.

是一个什么都想学一点的小邋遢

---

解决以下3个痛点：

1️⃣能查到的大部分检查命令没有运行结果的截图，无法确定命令是否有效。

2️⃣不同版本的被侧目标可能使用不同的命令，过时或者较新的命令可能无法有效运行，明显降低检查效率**。**

3️⃣**网络公开的检查方法整体缺乏系统性与持续维护**

💽测试环境：虚拟机

💽测试镜像版本：Rocky-10.1-x86\_64-dvd1.iso

💽数据库版本：PostgreSQL 15.15

📚文末可提取本文的无水印PDF版本的百度网盘下载链接，方便各位在无网络环境下的使用。

👇如果有更加好的检测命令或者需要修改的地方，请在评论区留言。我会及时更新改正，并上传新的离线文件。

---

目录结构：

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkrRPNNxg3bkmUibTCufJYD8iaHhAjbTjsibXcFGmrCwzaeSOGdnZDMZwMicXOfbIeiaEjj8ObnLdKzIOuc5nDUlYw49ozEKydT5SI9M/640?wx_fmt=png&from=appmsg)

---

# 一、身份鉴别

## 1.1 账号管理

PostgreSQL 中每个角色（role）名称在集群内必须是唯一的，这是由系统强制保证的。但你可以通过以下 SQL 查询确认所有具有登录权限的角色：

```
SELECT *  FROM pg_roles WHERE rolcanlogin = true;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkr6ICTnCX4SG26fpfh8wibibYeKPzC0v7hgDOsibk3zuibQiagM3y1lwA9z0p1FKM7iaK0l2NuUHTXHzybFicjdmXSSFh7kwqDm163S98/640?wx_fmt=png&from=appmsg)

PostgreSQL 的密码存储在 `pg_authid` 系统表中（需超级用户权限）：

```
SELECT rolname, rolpassword FROM pg_authid WHERE rolcanlogin = true;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkphKeN0WdAibt03DOOFPByEiaRQ434BfEj254tT5aqcxXQtXz6ic8XtKmKQcJYrMw69GDiatJKpBxSaZYdRUBnKlnaFU6NlBMBdves/640?wx_fmt=png&from=appmsg)

## 1.2 密码复杂度

PostgreSQL 原生不支持密码复杂度策略，但可通过以下扩展实现：

### **方法一：安装 `pg_password_policy` 扩展（第三方）**

```
- 支持最小长度、数字/大小写字母/特殊字符要求等。
- 需手动编译安装，并在 `postgresql.conf` 中配置。
```

```
# 查看是否存在第三方安全扩展
cat /var/lib/pgsql/15/data/postgresql.conf | grep "扩展名"
```

存在复杂度设置的示例：

```
# 加载扩展
shared_preload_libraries = 'pg_password_policy' # 若已有其他扩展，用逗号分隔

# 配置密码策略（按需调整）
password_policy.min_length = 8 # 密码最小长度
password_policy.digits = 1 # 至少1个数字
password_policy.uppercase = 1 # 至少1个大写字母
password_policy.lowercase = 1 # 至少1个小写字母
password_policy.special = 1 # 至少1个特殊字符
password_policy.max_length = 64 # 密码最大长度
password_policy.reuse_check = 3 # 禁止复用最近3次密码
```

### **方法二：使用 `pam` + `pam_pwquality`（通过 PAM 认证）**

```
- 在 `pg_hba.conf` 中配置 `pam` 认证；
- 系统级 PAM 模块可强制密码复杂度。
```

```
# 查看用户是否启用了pam认证
cat /var/lib/pgsql/15/data/pg_hba.conf
```

如果进行了PAM配置，则配置内容基本如下：

```
# 基本 PAM 认证配置
# TYPE  DATABASE    USER    ADDRESS     METHOD
host    mydb        myuser  192.168.1.0/24  pam

# 带参数的 PAM 认证配置
host    mydb        myuser  192.168.1.0/24  pam pamservice=postgresql pam_use_hostname=1
```

## 1.3 登录失败处理

在 PostgreSQL 中，**原生并不直接提供“账户锁定”或“登录失败次数限制”等传统意义上的登录失败处理机制**（如 Oracle、SQL Server 或 Windows AD 中的账户锁定策略）。但是可以通过第三方安全工具实现。

## 1.4 远程登录管理

```
cat /var/lib/pgsql/15/data/postgresql.conf | grep -E "listen_addresses|port"
# 检查数据库配置的远程管理的监听地址
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqdlq1sAHxS7m6KH228EwZvVibHQSHYN6towEpb8iaH7t1pFE1WUg0W819XTaLhRELJbBfkY2X6wXkFdRIReOZCgYfZJzpK7pNIA/640?wx_fmt=png&from=appmsg)

> `*`：允许监听任意IPv4地址，也可以将其替换为指定IPv4

```
cat /var/lib/pgsql/15/data/pg_hba.conf | grep -v "^#\|^$"
# 查看允许访问数据库的IP范围
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkpAR0fUfDBBLean8FHEndWAftyRsibmNAN8CWBVea149oHry2dsqHCpE0M9lAN451ZrkMDYm9RVicg6b3NiaibIxvgK6BDZ2AD3ynk/640?wx_fmt=png&from=appmsg)

常见的 “认证方式” 取值：

* • **`scram-sha-256`**：推荐的安全加密认证方式，比 `md5` 更安全。
* • **`md5`**：使用 MD5 哈希密码认证（兼容性较好，但安全性不如 SCRAM）。
* • **`peer`/`ident`**：仅适用于本地连接，通过操作系统用户名验证。
* • **`trust`**：无需密码直接允许连接（仅在绝对可信的内网环境中临时使用，生产环境禁止）。

## 1.5 双因素认证

PostgreSQL **原生不直接支持双因素认证（2FA / MFA）**，但可以**通过 PAM配置来集成 2FA**

```
cat /etc/pam.d/postgresql
```

拿 **Google Authenticator** 举例，如果安装了 **Google Authenticator PAM 模块（Linux）** 则可以在`/etc/pam.d/postgresql`中找到如下的配置：

```
# /etc/pam.d/postgresql
auth      required    pam_google_authenticator.so
auth      include     system-auth
account   include     system-auth
```

# 二、访问控制

## 2.1 账户权限划分

结合1.1账号管理的内容可以进行可登录账号的权限查看是否存在多种类型的可登录账户用以划分权限👇：

```
SELECT *  FROM pg_roles WHERE rolcanlogin = true;
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqlulYhrhSoq02kIia1dHibUf4MIepAzzaVGPm7zpKZJ0ibmGXXS21X3z6rxBy0CDtBxId9KpXicItyG8EIZP1TDic1ibM3RWRvp7ibiaQ/640?wx_fmt=png&from=appmsg)

| 字段名 | 值 | 含义 |
| --- | --- | --- |
| rolname | postgres | 角色名称，这是 PostgreSQL 安装时默认创建的超级用户 |
| rolsuper | t | 该角色是**超级用户**，拥有数据库的所有权限 |
| rolcreaterole | t | 允许该角色创建其他数据库角色 |
| rolcreatedb | t | 允许该角色创建新的数据库 |
| rolcanlogin | t | 该角色允许登录数据库（这也是你查询的过滤条件） |
| rolreplication | t | 该角色拥有**流复制权限**，可以用于主备复制场景 |
| rolconnlimit | -1 | 对该角色的并发连接数无限制（`-1` 表示不限制） |
| rolpassword | \*\*\*\*\*\*\*\* | 该角色已设置密码（出于安全考虑，密码显示为星号） |
| rolbypassrls | t | 该角色可以绕过行级安全策略（RLS） |

## 2.2 默认账户/口令

PostgreSQL 在 `initdb` 初始化集群时，会创建一个**与操作系统当前用户同名的角色**（通常是 `postgres`）。**该角色默认具有 `SUPERUSER` 权限**，且**无密码**（依赖 `peer` 或 `ident` 认证本地登录）。

结合 **1.2 密码复杂度** 判断是否存在默认口令、默认账户的情况。

```
SELECT
  *
FROM
  pg_authid
WHERE
  rolcanlogin = true;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkq1wSQg7AMxvibm7SR8XUUmFYjl1va2yeV7oXDZdtbF6flnKDupfD7yxsFFa6BqCEHoH169TUHNUwoyTMqLJeheqeU7L6zJk2Jo/640?wx_fmt=png&from=appmsg)

## 2.3 共享账户

最佳判断方式是通过日志进行分析👇：

```
ls var/lib/pgsql/15/data/log
# 查看当前文件夹下是否存在日志信息

cat postgresql-Tue.log | grep "用户名"
# 分析用户的链接状况
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqJw1WhTIz7HIE0ozhnpNj2Fibso9BEYvhia66ScgVGj7dxvFcfd2TsBEfaktkk5XXwneXkbLX6Lnl5vl3NOjbQrJec7icFJS0QAU/640?wx_fmt=png&from=appmsg)

## 2.4 最小权限原则

结合 **2.1 账户权限划分** 判断账户权限是否按照最小权限原则进行权限划分

检查 `PUBLIC` 角色是否被过度授权，`PUBLIC` 是隐式包含所有角色的组，对其授权等于对所有人授权。

```
SELECT
  *
FROM
  information_schema.table_privileges
WHERE
  grantee = 'PUBLIC';
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkrGwNJibZYibMdWVCsUWMiayWZetYQkjiciaS7IzKcUlTgML2kebkO0bRFWrx3PrrSBybtLrCGXbEUbz0colEfpYKwB8EUzwff5Ugia4/640?wx_fmt=png&from=appmsg)

```
-- 查看是否有角色被授予 ALL PRIVILEGES on ALL TABLES（过度授权）
SELECT
  grantee,
  COUNT(*) AS num_tables,
  STRING_AGG(table_name, ', ') AS tables
FROM
  information_schema.table_privileges
WHERE
  privilege_type IN ('SELECT', 'INSERT', 'UPDATE', 'DELETE')
GROUP BY
  grantee
HAVING
  COUNT(DISTINCT table_schema || '.' || table_name) > 50;
-- 阈值根据实际数据库拥有的表数目进行修改
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkrcE0cxUFjmz6IG4aGwRq9Wte9IvUCGoTgyExhx5hQC7ETaIJP5ia2icg2CzUxCqiaibLjicXhWEHeYzibnVMzBdiboQm0qH1UsZNDicfk/640?wx_fmt=png&from=appmsg)

## 2.5 由授权主体配置访问控制策略

检查授权主体，仅少数可信角色（如 `postgres`、`db_sec_admin`）具备授权能力，普通用户拥有 `CREATEROLE`权限，可自行授权 ，这违反了“由授权主体配置”：

```
SELECT
  rolname
FROM
  pg_roles
WHERE
  rolsuper = true
  OR rolcreaterole = true;
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkoR7I5okU6OCYvUiaNZkV7xrSu7uhXuOYyW4c7cYv5NBmvZSDWq89I5Lic1I1WJeQ8IuCo27XpRhfa03mUPwV2H2epicSNNOz9R6k/640?wx_fmt=png&from=appmsg)

## 2.6 访问控制的粒度

结合**2.4 最小权限原则** 中角色权限查看的信息进行判断，`PUBLIC` 相当于“所有用户”，对其授权等于放弃访问控制粒度，任何返回结果均视为**不符合细粒度要求**。

## 2.7 强访问控制

```
-- 检查哪些角色可绕过 RLS
SELECT
  rolname
FROM
  pg_roles
WHERE
  rolbypassrls = true;
```

除极少数审计账号外，**不应授予普通用户 `BYPASSRLS`**。

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkoufThMjK4X0WBl1t4fwFicdrYqy531htvomv84gFpzc2A73mnKqHwx09vomm2AzISfEBEH9H7iaicDkA8NfYe8icGW9Wib6oSibVibck/640?wx_fmt=png&from=appmsg)

## 3.1 安全审计功能

```
-- 查看关键审计相关参数
SELECT
  name,
  setting
FROM
  pg_settings
WHERE
  name IN (
    'log_destination',
    'logging_collector',
    'log_directory',
    'log_filename',
    'log_statement',
    'log_connections',
    'log_disconnections',
    'log_min_duration_statement',
    'log_line_prefix'
  );
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkrZLE24Xt3iaISjKK2aYHkYLPE6dgvQKgwlTbTKOzFVWkjt8nasq9cdFgKRtr9QUTicUOHBTS0RRiblB4siaXVnKwOwibPNs1sPcubE/640?wx_fmt=png&from=appmsg)

| 参数 | 推荐值 | 作用 |
| --- | --- | --- |
| `logging_collector` | `on` | 启用日志收集 |
| `log_connections` | `on` | 记录登录 |
| `log_disconnections` | `on` | 记录登出 |
| `log_statement` | `'ddl'` 或 `'mod'` | - `none`：不记录 - `ddl`：记录 DDL（CREATE/ALTER/DROP） - `mod`：DDL + DML（INSERT/UPDATE/DELETE） - `all`：记录所有 SQL（含 SELECT，慎用） |
...