---
title: 不同数据库被”拖库”特征-托管vs自建+是/否开启审计日志取证实测
url: https://zgao.top/%e4%b8%8d%e5%90%8c%e6%95%b0%e6%8d%ae%e5%ba%93%e8%a2%ab%e6%8b%96%e5%ba%93%e7%89%b9%e5%be%81-%e6%89%98%e7%ae%a1vs%e8%87%aa%e5%bb%ba%e6%98%af-%e5%90%a6%e5%bc%80%e5%90%af%e5%ae%a1%e8%ae%a1%e6%97%a5/
source: Zgao's blog
date: 2026-06-27
fetch_date: 2026-06-28T06:08:19.452879
---

# 不同数据库被”拖库”特征-托管vs自建+是/否开启审计日志取证实测

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 不同数据库被”拖库”特征-托管vs自建+是/否开启审计日志取证实测

* [首页](https://zgao.top)
* [不同数据库被”拖库”特征-托管vs自建+是/否开启审计日志取证实测](https://zgao.top:443/%E4%B8%8D%E5%90%8C%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A2%AB%E6%8B%96%E5%BA%93%E7%89%B9%E5%BE%81-%E6%89%98%E7%AE%A1vs%E8%87%AA%E5%BB%BA%E6%98%AF-%E5%90%A6%E5%BC%80%E5%90%AF%E5%AE%A1%E8%AE%A1%E6%97%A5/)

[6月 27, 2026](https://zgao.top/2026/06/)

### 不同数据库被”拖库”特征-托管vs自建+是/否开启审计日志取证实测

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E4%B8%8D%E5%90%8C%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A2%AB%E6%8B%96%E5%BA%93%E7%89%B9%E5%BE%81-%E6%89%98%E7%AE%A1vs%E8%87%AA%E5%BB%BA%E6%98%AF-%E5%90%A6%E5%BC%80%E5%90%AF%E5%AE%A1%E8%AE%A1%E6%97%A5/)

在入侵类应急响应中，客户最常见的诉求之一是：**“帮我判断数据库到底有没有被黑客拖库？”** 但数据库类型种类众多，每种数据库的拖库手法、留下的痕迹、可用的取证手段都不一样；而且**是否开启了审计日志**，直接决定了能拿到的证据等级。

本文在腾讯云上用 tccli 真实开通了 **7 种托管数据库**，插入 10 万行/文档级别的敏感样本数据（身份证、手机号、银行卡、密码哈希），分别在 **不开审计 / 开启审计** 两种情况下模拟拖库；并对其中差异最大的 **SQL Server、Elasticsearch、Redis、MySQL、PostgreSQL 额外做了「自建 vs 托管」对照实测**（自建实例上启用原生审计、复现托管版封掉的危险能力）。每个结论都附实际抓取的日志/截图，最后给出应急响应取证清单与加固建议。

全文所有日志、命令、API 输出均为真实实测结果。

文章目录

[ ]

* [测试环境与方法论](#%E6%B5%8B%E8%AF%95%E7%8E%AF%E5%A2%83%E4%B8%8E%E6%96%B9%E6%B3%95%E8%AE%BA "测试环境与方法论")
* [MySQL（腾讯云 CDB）](#MySQL%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_CDB%EF%BC%89 "MySQL（腾讯云 CDB）")
  + [拖库手法](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95 "拖库手法")
  + [场景 A：不开审计时的痕迹](#%E5%9C%BA%E6%99%AF_A%EF%BC%9A%E4%B8%8D%E5%BC%80%E5%AE%A1%E8%AE%A1%E6%97%B6%E7%9A%84%E7%97%95%E8%BF%B9 "场景 A：不开审计时的痕迹")
  + [场景 B：开启审计后的痕迹](#%E5%9C%BA%E6%99%AF_B%EF%BC%9A%E5%BC%80%E5%90%AF%E5%AE%A1%E8%AE%A1%E5%90%8E%E7%9A%84%E7%97%95%E8%BF%B9 "场景 B：开启审计后的痕迹")
  + [取证要点](#%E5%8F%96%E8%AF%81%E8%A6%81%E7%82%B9 "取证要点")
  + [对照实测：自建 MySQL](#%E5%AF%B9%E7%85%A7%E5%AE%9E%E6%B5%8B%EF%BC%9A%E8%87%AA%E5%BB%BA_MySQL "对照实测：自建 MySQL")
* [PostgreSQL（腾讯云 PostgreSQL）](#PostgreSQL%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_PostgreSQL%EF%BC%89 "PostgreSQL（腾讯云 PostgreSQL）")
  + [拖库手法](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95-2 "拖库手法")
  + [默认日志配置（很关键）](#%E9%BB%98%E8%AE%A4%E6%97%A5%E5%BF%97%E9%85%8D%E7%BD%AE%EF%BC%88%E5%BE%88%E5%85%B3%E9%94%AE%EF%BC%89 "默认日志配置（很关键）")
  + [场景 A：不开审计时的痕迹](#%E5%9C%BA%E6%99%AF_A%EF%BC%9A%E4%B8%8D%E5%BC%80%E5%AE%A1%E8%AE%A1%E6%97%B6%E7%9A%84%E7%97%95%E8%BF%B9-2 "场景 A：不开审计时的痕迹")
  + [场景 B:开启审计后的痕迹](#%E5%9C%BA%E6%99%AF_B_%E5%BC%80%E5%90%AF%E5%AE%A1%E8%AE%A1%E5%90%8E%E7%9A%84%E7%97%95%E8%BF%B9 "场景 B:开启审计后的痕迹")
  + [对照实测：自建 PostgreSQL](#%E5%AF%B9%E7%85%A7%E5%AE%9E%E6%B5%8B%EF%BC%9A%E8%87%AA%E5%BB%BA_PostgreSQL "对照实测：自建 PostgreSQL")
* [Redis（腾讯云 Redis 6.2）](#Redis%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_Redis_62%EF%BC%89 "Redis（腾讯云 Redis 6.2）")
  + [拖库手法与实测结果](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95%E4%B8%8E%E5%AE%9E%E6%B5%8B%E7%BB%93%E6%9E%9C "拖库手法与实测结果")
  + [检测痕迹](#%E6%A3%80%E6%B5%8B%E7%97%95%E8%BF%B9 "检测痕迹")
  + [对照实测：自建 Redis](#%E5%AF%B9%E7%85%A7%E5%AE%9E%E6%B5%8B%EF%BC%9A%E8%87%AA%E5%BB%BA_Redis "对照实测：自建 Redis")
* [MongoDB（腾讯云 MongoDB 6.0 副本集）](#MongoDB%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_MongoDB_60_%E5%89%AF%E6%9C%AC%E9%9B%86%EF%BC%89 "MongoDB（腾讯云 MongoDB 6.0 副本集）")
  + [拖库手法](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95-3 "拖库手法")
  + [场景 A:不开审计时的痕迹](#%E5%9C%BA%E6%99%AF_A_%E4%B8%8D%E5%BC%80%E5%AE%A1%E8%AE%A1%E6%97%B6%E7%9A%84%E7%97%95%E8%BF%B9 "场景 A:不开审计时的痕迹")
  + [场景 B:开启审计后的痕迹](#%E5%9C%BA%E6%99%AF_B_%E5%BC%80%E5%90%AF%E5%AE%A1%E8%AE%A1%E5%90%8E%E7%9A%84%E7%97%95%E8%BF%B9-2 "场景 B:开启审计后的痕迹")
  + [取证要点](#%E5%8F%96%E8%AF%81%E8%A6%81%E7%82%B9-2 "取证要点")
* [SQL Server（腾讯云 SQL Server 2017 企业版）](#SQL_Server%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_SQL_Server_2017_%E4%BC%81%E4%B8%9A%E7%89%88%EF%BC%89 "SQL Server（腾讯云 SQL Server 2017 企业版）")
  + [拖库手法与实测](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95%E4%B8%8E%E5%AE%9E%E6%B5%8B "拖库手法与实测")
  + [场景 A / B 实测结论](#%E5%9C%BA%E6%99%AF_A_B_%E5%AE%9E%E6%B5%8B%E7%BB%93%E8%AE%BA "场景 A / B 实测结论")
  + [对照实测：自建 Windows SQL Server 的原生 Audit](#%E5%AF%B9%E7%85%A7%E5%AE%9E%E6%B5%8B%EF%BC%9A%E8%87%AA%E5%BB%BA_Windows_SQL_Server_%E7%9A%84%E5%8E%9F%E7%94%9F_Audit "对照实测：自建 Windows SQL Server 的原生 Audit")
* [ClickHouse（腾讯云 CDWCH）](#ClickHouse%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_CDWCH%EF%BC%89 "ClickHouse（腾讯云 CDWCH）")
  + [拖库手法](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95-4 "拖库手法")
  + [检测痕迹：内置 system.query\_log](#%E6%A3%80%E6%B5%8B%E7%97%95%E8%BF%B9%EF%BC%9A%E5%86%85%E7%BD%AE_systemquery_log "检测痕迹：内置 system.query_log")
  + [取证要点](#%E5%8F%96%E8%AF%81%E8%A6%81%E7%82%B9-3 "取证要点")
* [Elasticsearch（腾讯云 ES 7.10）](#Elasticsearch%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91_ES_710%EF%BC%89 "Elasticsearch（腾讯云 ES 7.10）")
  + [拖库手法](#%E6%8B%96%E5%BA%93%E6%89%8B%E6%B3%95-5 "拖库手法")
  + [场景 A:搜索慢日志](#%E5%9C%BA%E6%99%AF_A_%E6%90%9C%E7%B4%A2%E6%85%A2%E6%97%A5%E5%BF%97 "场景 A:搜索慢日志")
  + [场景 B:全量审计](#%E5%9C%BA%E6%99%AF_B_%E5%85%A8%E9%87%8F%E5%AE%A1%E8%AE%A1 "场景 B:全量审计")
  + [对照实测：自建 ES 开启全量审计](#%E5%AF%B9%E7%85%A7%E5%AE%9E%E6%B5%8B%EF%BC%9A%E8%87%AA%E5%BB%BA_ES_%E5%BC%80%E5%90%AF%E5%85%A8%E9%87%8F%E5%AE%A1%E8%AE%A1 "对照实测：自建 ES 开启全量审计")
* [拖库横向对比](#%E6%8B%96%E5%BA%93%E6%A8%AA%E5%90%91%E5%AF%B9%E6%AF%94 "拖库横向对比")
  + [拖库指纹速查](#%E6%8B%96%E5%BA%93%E6%8C%87%E7%BA%B9%E9%80%9F%E6%9F%A5 "拖库指纹速查")
  + [审计能力与取证等级](#%E5%AE%A1%E8%AE%A1%E8%83%BD%E5%8A%9B%E4%B8%8E%E5%8F%96%E8%AF%81%E7%AD%89%E7%BA%A7 "审计能力与取证等级")
  + [拖库通用规律](#%E6%8B%96%E5%BA%93%E9%80%9A%E7%94%A8%E8%A7%84%E5%BE%8B "拖库通用规律")
* [数据库应急取证排查思路](#%E6%95%B0%E6%8D%AE%E5%BA%93%E5%BA%94%E6%80%A5%E5%8F%96%E8%AF%81%E6%8E%92%E6%9F%A5%E6%80%9D%E8%B7%AF "数据库应急取证排查思路")
* [应急加固建议](#%E5%BA%94%E6%80%A5%E5%8A%A0%E5%9B%BA%E5%BB%BA%E8%AE%AE "应急加固建议")

## 测试环境与方法论

| 项目 | 说明 |
| --- | --- |
| 云平台 | 腾讯云（广州 ap-guangzhou），全部按量计费，测完即销毁 |
| 实例 | 共 **7 种**：CDB MySQL 8.0 / PostgreSQL 15 / Redis 6.2 / MongoDB 6.0（三节点副本集）/ SQL Server 2017 企业版（AlwaysOn）/ ClickHouse 21.8（HA 集群，2 数据+3 ZK）/ Elasticsearch 7.10（2 节点） |
| 样本数据 | 统一一张表/一个集合/一个索引 members，**10 万行**，字段含 id\_card / phone / bank\_card / password\_hash / address 等典型 PII |
| 攻击侧 | 公网客户端直连（MySQL/PG/Redis/SQLServer）+ **VPC 内跳板机**直连内网（MongoDB/ClickHouse/Elasticsearch），后者还原“攻击者已拿下内网一台机器后横向拖库”的真实场景 |
| 两种场景 | **场景 A：不开审计**（默认状态）/ **场景 B：开启审计**，逐一对比可取到的痕迹 |
| 取证手段 | 全程用 tccli 调云端 API（DescribeAuditLogs / DescribeSlowLog / DescribeXEvents / GetMonitorData 等）+ 数据库内置系统表，模拟应急响应方“只能拿到云控制台/API”的真实条件 |
| 自建对照 | 另用 tccli 开 CVM 自建：**Windows SQL Server 2022（原生 Audit）/ ES 7.10（X-Pack 全量审计）/ Redis 7（MONITOR+–rdb）/ MySQL 8（INTO OUTFILE）/ PostgreSQL 16（COPY TO PROGRAM）**，与托管版逐一对照 |

**核心结论先行**：

**云上托管数据库，即使不开审计，也并非“零痕迹”**——慢查询日志、命令统计、网络出向流量监控，往往足以发现“大批量数据外带”这一行为本身（实测拖库瞬间出流量可达基线 170 倍）。

**审计日志是唯一能还原“具体执行了哪条语句、拖走了哪张表/哪些字段”的证据**。不开审计，只能证明“有人导了很多数据”；开了审计，能证明“谁、在什么时间、用什么语句、拖走了 members 表的 10 万行敏感数据”。

**各数据库审计能力分三档**：

**第一档（内置/全量，开箱即用）**：ClickHouse 内置 query\_log 默认全量；MySQL / PostgreSQL / MongoDB 一键开启即得完整语句级审计。

**第二档（弱/受限）**：Redis 只有慢日志、无命令级审计；Elasticsearch 托管版无法动态开 X-Pack 审计；SQL Server 托管版只有慢/阻塞 XEvent。

取证便捷度从高到低：ClickHouse ≈ MySQL/PG > MongoDB ≫ Redis / SQLServer / ES。

**“开了审计”不等于“一定查得到”**：实测 SQL Server 托管版的慢 XEvent 阈值按**服务端执行时间**计——攻击者用最朴素的 SELECT \* FROM 大表 慢慢拉数据，服务端执行飞快（0.1s），即便开了审计也照样绕过。

**托管 vs 自建是另一条主线**：取证上——SQL Server/Elasticsearch 托管版审计基本残废，**自建开原生审计后吊打**（连客户端 IP、拖了哪些字段都记）攻击面上——托管把 INTO OUTFILE/COPY TO PROGRAM/SYNC 等危险能力收敛掉了。但自建默认敞开、攻击面更大。

## MySQL（腾讯云 CDB）

### 拖库手法

```
# 手法1:mysqldump 全库导出(最经典)
mysqldump -h <host> -P <port> -uroot -p<pwd> --single-transaction shop members > dump.sql

# 手法2:SELECT * 全表查询(SQL注入/应用层导出)
mysql ... -e "SELECT * FROM members;" > out.txt

# 手法3:分页 LIMIT 慢速抓取(规避检测)
mysql ... -e "SELECT ... FROM members LIMIT 20000 OFFSET 40000;"

# 手法4:SELECT ... INTO OUTFILE(落地文件)
```

**实测关键发现**：

**手法4 INTO OUTFILE 在托管实例上被直接阻断**：ERROR 1227 (42000): Access denied; you need (at least one of) the FILE privilege(s) CDB 默认 secure\_file\_priv=NULL、root 账号无 FILE 权限，**攻击者无法在数据库服务端落地文件**，只能把数据通过网络外带到客户端。这是云数据库相比自建的一个天然...