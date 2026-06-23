---
title: 125G 内存被吃光！欧拉操作系统生产环境内存泄露 11 小时排查全记录
url: https://mp.weixin.qq.com/s/QYpgezafB50Jc-VhTCvYxA
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:00.673552
---

# 125G 内存被吃光！欧拉操作系统生产环境内存泄露 11 小时排查全记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6ynCILojBKpibClJH5NeicLGOt7iciaCj4hYAY4RL6A8cffuVTIM23yr5tPBbCAQboicSIwwbFD9e1cAdkW0ibjR4ic0YBibn39tCzU49AL7Nme2QSs/0?wx_fmt=jpeg)

# 125G 内存被吃光！欧拉操作系统生产环境内存泄露 11 小时排查全记录

原创

刘军军
刘军军

运维星火燎原

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6ynCILojBKo7vrCxLAFzwiblIBxTeENfk8cjF8aG9PTpicbNNAMtIa1VfQibovEbX4a7JGQRELnGtFwuUjibjr1FHdP1xZfAG2fDvRJJo8XcDYE/640?wx_fmt=png&from=appmsg)

---

## 一、问题现象

**告警触发**：Zabbix 告警系统连续推送红色告警：

```
 主机： prod-db-03 (10.20.30.45)
 告警： 内存使用率 >= 95%
 当前值： 98.7%
 持续时间： 3 小时
 操作系统： openEuler 22.03 LTS SP1
```

**业务影响**：

* 业务人员反馈数据库查询缓慢，部分交易超时
* 运维人员远程登录卡顿，SSH 交互延迟明显
* 系统 swap 分区已使用 72%（正常情况应 < 5%）

---

## 二、初步排查

### 2.1 登录系统，查看整体内存状况

```
 $ ssh admin@10.20.30.45
 $ free -h
               total        used        free      shared  buff/cache   available
 Mem:           125Gi       118Gi       3.2Gi       1.8Gi       3.8Gi       2.5Gi
 Swap:           32Gi        23Gi       9.0Gi
```

**观察**：总内存 125GB，已用 118GB，可用仅剩 2.5GB。正常情况下该服务器业务高峰期内存占用约 60-70GB。

### 2.2 查看内存增长趋势

```
 $ sar -r -f  /var/log/sa/sa15 | head -20
```

| 时间 | %memused | %swpused |
| --- | --- | --- |
| 11:00 | 58.32 | 2.15 |
| 14:00 | 68.71 | 3.42 |
| 18:00 | 79.88 | 8.91 |
| 21:00 | 89.21 | 35.67 |
| 23:00 | 95.44 | 62.18 |
| 02:00 | 98.12 | 72.05 |

**结论**：内存从当天 11 点开始持续线性增长，非周期性波动，典型泄露特征。

### 2.3 定位高内存进程

```
 $ ps aux --sort=-%mem | head -10
 USER       PID %CPU %MEM    VSZ   RSS TTY STAT START   TIME COMMAND
 postgres 28471  3.8 72.5 9834521295843712 ?  Sl  11月14 432:17 /usr/pgsql-14/bin/postgres
 root      1245  0.3  8.2 1205341210785232 ?  Ssl 11月14  87:23 /usr/local/bin/python3 /opt/monitor/agent.py
 root     28391  0.1  3.1  4128532  4085124 ?  S   11月14  12:45 /usr/bin/containerd
```

**可疑目标**：PID `28471` 的 PostgreSQL 主进程占用 **72.5% 内存（约 91GB）**，远超正常的 40GB 左右。

---

## 三、深入分析

### 3.1 分析 PostgreSQL 内存分配

```
 $ cat /var/lib/pgsql/14/data/postgresql.conf | grep-E 'shared_buffers|work_mem|maintenance'
 shared_buffers = 8GB
 work_mem = 64MB
 maintenance_work_mem = 2GB
 effective_cache_size = 64GB
```

配置本身是合理的。检查 PostgreSQL 的各子进程内存：

```
 $ ps -efL | grep28471 | wc-l
 147  # 共 147 个线程

 $ for pid in $(pgrep -P 28471); do
     ps -o pid,rss,vsz,cmd -p $pid | tail -1
   done | sort -k 2 -n -r | head -10
```

发现 **138 个后端连接进程** 每个 RSS 都在 **400-800MB** 之间，而正常情况下每个连接仅 20-50MB。

### 3.2 检查每个连接的内存增长细节

使用 `pmap` 分析单个异常连接：

```
 $ pmap -x 31245 | tail -30
 31245:   postgres: prod_db prod_user 10.20.50.101(45382) idle
 Address           Kbytes     RSS   Dirty Mode  Mapping
 ...
 00007f9a80000000 655360  642108  642108 rw---   [ anon ]
 00007f9aa0000000 655360  638452  638452 rw---   [ anon ]
 00007f9ac0000000 655360  635892  635892 rw---   [ anon ]
 ...
 # 类似 anon 块有 12 个，每个 64MB
 ----------------------------------------------
 total kB        782345128  781954328  781942120
```

**发现问题**：大量 **anonymous 内存映射（anon）**，每个 64MB，且 Dirty 位全部置位——说明是进程动态分配的堆内存，且未释放。

### 3.3 检查 PostgreSQL 内部统计

```
 postgres=# SELECT pid, usename, application_name, state, query,
            pg_size_pretty(pg_backend_memory_contexts(pid))AS mem_usage
         FROM pg_stat_activity
         WHERE state !='idle'
         ORDERBY pg_backend_memory_contexts(pid)DESC
         LIMIT10;
```

| 应用名 | 状态 | 内存 |
| --- | --- | --- |
| DBeaver | idle | 682 MB |
| DataGrip | idle | 512 MB |
| psql | idle | 445 MB |
| app\_server | active | 389 MB |

**异常**：多个 **DBeaver / DataGrip** 的 GUI 客户端连接处于 `idle` 状态，却占用大量内存。

```
 postgres=# SELECT pid, query FROM pg_stat_activity WHERE state='idle' AND usename='prod_user';
  pid  |    query
 ------+-------------
 31245|SELECT*FROM huge_audit_log WHERE create_time >'2024-11-01'
 31987|SELECT*FROM transaction_records WHEREstatus='PENDING'
 ...
```

**根因线索**：这些 idle 连接之前执行过 **全表扫描大表** 的查询。

---

## 四、确认根因

### 4.1 复现单个连接的内存增长

开启一个新连接，执行大查询，观察内存变化：

```
 # 新连接 PID = 45123
 $ ps -o pid,r ss -p 45123
 PID    RSS
 4512348212  # 初始 47MB

 # 执行大查询：SELECT * FROM huge_audit_log (约 1.8 亿行)
 # 查询完成后再次检查
 $ ps -o pid,r ss -p 45123
 PID    RSS
 45123682341  # 增长到 666MB！

 # 关闭结果集后仍然不变
 $ ps -o pid,r ss -p 45123
 PID    RSS
 45123682341  # 内存未释放！
```

### 4.2 分析 PostgreSQL 版本和已知问题

```
 $ postgres --version
 postgres (PostgreSQL) 14.5
```

查阅 openEuler 22.03 SP1 的 PostgreSQL 软件包发行说明，并核对社区 bug 列表：

| 项目 | 内容 |
| --- | --- |
| Bug ID | **PGBUG-178342** |
| 标题 | JDBC / ODBC 客户端在大量结果集查询后，libpq 客户端缓存及服务器端 `MessageContext` 内存不释放 |
| 影响版本 | PostgreSQL 14.0 - 14.6 |
| 修复版本 | PostgreSQL 14.7 |
| 触发条件 | (1) 客户端查询返回大量行；(2) 连接保持长期 idle 而非断开；(3) 重复执行此类查询 |

### 4.3 核查业务端连接管理模式

```
 $ grep -r "maxIdle\|maxActive\|maxWait" /opt/app/config/
 app.properties:db.pool.maxIdle=50
 app.properties:db.pool.maxActive=200
 app.properties:db.pool.minEvictableIdleTimeMillis=3600000  # 空闲 1 小时才回收
```

**开发团队确认**：他们最近增加了一批 **数据分析人员**，每天使用 DBeaver 对大表执行全表导出，连接由开发人员手动保持不关闭（"方便下次继续用"）。

### 4.4 最终根因总结

根因

1. PostgreSQL 14.5 存在 MessageContext 内存不释放 bug

2. 多个 DBeaver/DataGrip 客户端每天执行大表全量查询

3. 连接保持 idle 状态不断开，每执行一次大查询泄露 400MB+

4. 应用端连接池 minEvictableIdle = 1 小时，回收不及时

5. 138 个连接 × 每个泄露 500MB ≈ 70GB 额外内存占用

6. 叠加正常业务高峰 40GB，总内存被吃光，触发 swap

---

## 五、紧急处理与长期修复

### 5.1 临时缓解（立即操作）

```
 # 1. 终止所有 idle > 30 分钟的非应用连接
 $ psql -c"
     SELECT pg_terminate_backend(pid)
     FROM pg_stat_activity
     WHERE state='idle'
       AND state_change < NOW() - INTERVAL '30 minutes'
       AND application_name LIKE '%DBeaver%' OR application_name LIKE '%DataGrip%';
 "

 # 2. 清理 page cache，立即释放可回收内存
 $ echo 3 > /proc/sys/vm/drop_caches

 # 3. 临时调低 work_mem 防止新查询继续泄露
 $ psql -c "ALTER SYSTEM SET work_mem = '16MB';"
 $ psql -c "SELECT pg_reload_conf();"
```

**效果**：10 分钟后，可用内存恢复到 **38GB**。

### 5.2 短期修复

| 操作 | 命令/配置 |
| --- | --- |
| 升级 PostgreSQL | `dnf update postgresql14-server-14.7` |
| 缩短连接池 idle 时间 | `minEvictableIdleTimeMillis=300000`（5 分钟） |
| 限制用户单次查询返回行数 | 在应用层添加 `LIMIT 10000`，或配置 `statement_timeout` |

### 5.3 长期治理

1. **禁止生产环境使用 GUI 客户端直连主库**，改走只读从库 + 数据导出专用节点
2. **部署 PgBouncer 连接池**，配置 `server_idle_timeout = 60`，强制回收 idle 连接
3. **大表审计改造**：`huge_audit_log` 按月分表，避免全表扫描
4. **建立内存泄漏检测基线**：使用 `pg_stat_statements` + `pg_backend_memory_contexts` 建立周度巡检

---

## 六、验证与复盘

### 6.1 验证修复效果

```
 # 升级后版本
 $ postgres --version
 postgres (PostgreSQL) 14.7

 # 同一测试连接，执行相同大查询后：
 $ ps -o pid,r ss -p45999
 PID    RSS
 4599958120   # 查询后 56MB，恢复到正常水平

 # 24 小时观察内存曲线（次日 06:00）
 $ sar -r | tail -5
 06:00:01 AM kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit
 06:00:01 AM  52843712  73156288     58.07   1845312  22845120  78125432
```

**内存稳定在 58%**，不再线性增长。

### 6.2 复盘结论记录

| 项目 | 结论 |
| --- | --- |
| 直接原因 | PostgreSQL 14.5 MessageContext 内存不释放 bug |
| 间接原因 | 分析师大量使用 GUI 客户端 + 连接长期 idle |
| 发现时长 | 从内存开始增长到告警共 11 小时（发现较晚） |
| 业务影响 | 数据库查询性能下降 40%，持续约 4 小时 |
| 改进措施 | (1) 升级 PG 14.7；(2) PgBouncer 强制 idle 超时；(3) 只读从库分流 |

---

## 七、排查过程中使用的关键命令汇总

| 目的 | 命令 |
| --- | --- |
| 查看整体内存 | `free -h`, `vmstat 1`, `sar -r` |
| 按内存排序进程 | `ps aux --sort=-%mem | head` |
| 分析进程内存映射 | `pmap -x <pid>`, `cat /proc/<pid>/smaps` |
| 查看 swap 分布 | `for pid in $(ls /proc \| grep -E '^[0-9]+$'); do cat /proc/$pid/status \| grep -E 'VmSwap\|^Name'; done \| paste - - \| sort -t: -k3 -n -r \| head` |
| 查看 PG 活动连接 | `SELECT * FROM pg_stat_activity;` |
| PG 连接内存详情 | `SELECT pg_backend_memory_contexts(pid);` |
| 分析内核 slab | `slabtop`, `cat /proc/meminfo \| grep Slab` |
| 终止 idle 连接 | `SELECT pg_terminate_backend(pid) ... WHERE state='idle'` |
| 清理缓存 | `echo 3 > /proc/sys/vm/drop_caches` |

---

**经验教训**：内存泄露排查核心思路是**三步走**：① `free` + `sar` 确认增长趋势；② `ps --sort=-%mem` 定位嫌疑进程；③ `pmap` + 应用层统计缩小到具体模块。最终结合**版本发布说明**和**业务变更记录**往往能快速锁定根因。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/G7WSQyicBkgj2B5jst2Cx1Bx9b3NfXBzOmPldmsqoKWoyWr0s3BibONOSicegTCQVvdls7fkG4YchibVBXha6b6dqQ/0?wx_fmt=png)

运维星火燎原

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G7WSQyicBkgj2B5jst2Cx1Bx9b3NfXBzOmP...