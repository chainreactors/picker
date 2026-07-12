---
title: 炸裂！这款 BurpSuite 插件让 Web 漏洞探测效率提升十倍
url: https://mp.weixin.qq.com/s/nbUUN3_k5H4rJKUA3GhGfw
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:09:05.255175
---

# 炸裂！这款 BurpSuite 插件让 Web 漏洞探测效率提升十倍

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UpPy2lqYfjLB1JFQT8G56j3klOg0hfuPcAzia6rKVOic81KOrpADnzV3b1iaS2Ee5bYWu6eWrg47x0fGafX6YYnBVeMib6KTeP9BuQ/0?wx_fmt=jpeg)

# 炸裂！这款 BurpSuite 插件让 Web 漏洞探测效率提升十倍

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

郑重声明：本文仅做技术分享，使用该工具进行未经授权的安全测试属于违法行为。

## 重点导读概述

xia\_tan（瞎探）是一款面向 BurpSuite 的自动化漏洞探测插件，专注于对常见 Web 漏洞进行初步扫描。插件以 Java 开发，无任何外部依赖，体积精小却功能强悍。

## 重点导读核心能力

### PART 01检测范围

* 反射型 XSS
* SQL 注入（10 种数据库引擎）
* SSTI 模板注入（6 大家族 20+ 引擎）
* NoSQL 注入

### PART 02技术亮点

采用行级 Jaccard 相似度算法替代传统响应长度对比，有效规避误报。内置多步布尔盲注对照算法，仅需 2~3 个请求即可确认漏洞，检测效率大幅领先同类工具。

## 重点导读漏洞检测

### PART 03XSS 探测

通过注入唯一标记 `<xia0tan>` 检测反射情况。未编码反射判定为高严重性，编码反射判定为信息级。JSON 响应类型自动跳过，避免无效探测。

### PART 04SQL 注入

覆盖 MySQL/MariaDB、MSSQL、PostgreSQL、Oracle、SQLite、DB2、Informix、Sybase、MS Access、HQL/Hibernate 等 10 种数据库。检测方式涵盖 ORDER BY 注入、数字型注入、报错探针、MySQL XPATH 报错、布尔盲注、延时注入等多种手段。

延时注入模块集成 WAF 绕过技巧，包括 BENCHMARK、JSON\_KEYS、注释混淆、大小写变异等手法。

### PART 05SSTI 探测

覆盖 Jinja2、Twig、Freemarker、Mako、ERB、SpEL、Razor、Smarty 等 6 大模板引擎家族。通过发送数学运算 payload 并计算返回结果，精准识别模板注入。

### PART 06NoSQL 注入

支持 MongoDB、CouchDB、Elasticsearch、Cassandra、Redis 等数据库。采用 JavaScript 风格语法的布尔盲注，结合操作符注入（$gt、$ne、$regex、$exists、$where），覆盖 24 种错误模式。

## 重点导读架构设计

### PART 07扫描流程

单参数扫描流程：XSS 与 SSTI 合并探测（1 个请求）→ SQL 注入检测（2~8 个请求）→ NoSQL 注入检测（2~4 个请求）。总计约 5~13 个请求完成全量检测。

### PART 08相似度算法

行级 Jaccard 相似度将响应按换行符分割为行集合，计算交集与并集之比。阈值默认 0.9，超过则判定响应相同，低于则判定存在显著差异。

### PART 09布尔盲注算法

OR/AND 多步对照算法通过恒真/恒假 payload 与基线对比，无论基线结果如何均能通过对照逻辑定位注入点，彻底规避传统方案中 payload 字符串差异导致的误报。

### PART 10基线降噪

检测前建立基线响应，基线中已存在的数据库错误特征、XSS 标记、SSTI 运算结果自动跳过，避免重复报告。

## 重点导读配置管理

### PART 11检测开关

| 模块 | 默认状态 |
| --- | --- |
| XSS | 启用 |
| SQLi | 启用 |
| SSTI | 启用 |
| NoSQLi | 启用 |
| Time-SQLi | 启用 |
| Cookie | 关闭 |

### PART 12CUD 过滤

增删改操作扫描默认关闭，通过关键词匹配路径（create、insert、delete、remove、update、edit 等）判断接口类型，避免对业务数据产生副作用。

### PART 13过滤规则

域名白名单、路径黑名单、路径白名单支持通配符匹配。静态资源文件（.js、.css、.png 等）、二进制响应、超长参数值（≥512 字符）自动跳过。

### PART 14参数控制

排除参数列表默认过滤 csrf、token、\_t、timestamp 等敏感字段。请求间隔、延时注入阈值、相似度阈值均可自定义配置。

## 重点导读项目结构

```
xia_tan/
├── src/main/java/burp/
│   ├── BurpExtender.java          # 插件入口、右键菜单、HTTP 监听
│   ├── XiaTanPanel.java           # UI 面板、配置管理
│   ├── ScanEngine.java            # 核心扫描引擎、布尔盲注、CUD 过滤
│   ├── ResponseComparer.java      # 行级 Jaccard 相似度、域名路径匹配
│   ├── XSSDetector.java           # 反射 XSS 检测
│   ├── SQLiDetector.java          # SQL 注入检测（10 数据库）
│   ├── SSTIDetector.java          # SSTI 检测（6 家族 20+ 引擎）
│   ├── NoSQLiDetector.java        # NoSQL 注入检测
│   ├── ScanResult.java            # 结果数据模型
│   └── ScanTableModel.java        # 结果表格模型
├── build.bat                      # 编译脚本
└── build.gradle                   # Gradle 配置
```

## 重点导读使用方式

### PART 15手动扫描

在 Proxy/Repeater/Target 模块中右键请求，选择「Send to xia\_tan」进行全量扫描，或选择「xia\_tan scan...」指定检测类型。

### PART 16自动监控

勾选 Monitor Proxy 和 Monitor Repeater，插件自动拦截经过的请求并执行扫描。

### PART 17结果查看

结果表格展示主机、方法、URL、参数、漏洞类型、检测细节、判定证据、严重性、响应长度、响应时间、状态码等信息。点击结果行查看完整请求响应，右键复制 URL 或 Payload。

### PART 18严重性等级

红色为高置信度确认，橙色为中置信度，白色为低置信度需人工确认，蓝色为信息性提示。

## 重点导读编译部署

环境要求 JDK 1.8 及以上，Windows 操作系统。执行 build.bat 编译，首次编译自动从 Maven 中央仓库下载 burp-extender-api。编译产物为 build/libs/xia\_tan-1.0.jar。

安装步骤：打开 BurpSuite → Extender → Extensions → Add → Extension type 选择 Java → 选择 xia\_tan-1.0.jar → 加载成功后出现 xia\_tan 标签页。

本文介绍的项目开源地址如下：

```
https://github.com/mapl3miss/xia_tan
```

本公众号非项目作者，仅做技术分享。

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uricnaz49eYhPl2COjpqMUVrL9HibnbmFLmIqKYSYhZHvDoHvNK8SsVZRbyewBCIlhoyoqiadl3iapfdHAL6PeqeNSU0DPgtk16CGA/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Ur2gibX8hRDFoepCj7KxGY4xaH1Rw5FkXvuNJu959focic71VzicLVkUElia2InUzRNcZokDF7mI72HicZ0wDGeD18hDZPF69RosH4U/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过