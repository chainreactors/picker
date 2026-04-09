---
title: [工具推荐]BurpSuite 多漏洞自动化探测插件xia_tan (瞎探)
url: https://mp.weixin.qq.com/s/63yJUkiNWR_K1eVh1-poyA
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:28:09.112195
---

# [工具推荐]BurpSuite 多漏洞自动化探测插件xia_tan (瞎探)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboRPtbHJxYncrEchb4RslXEfLiaxZkzhx18VFWLxTWACR8QMkdN5nBPFvXyTEOKG2ZCxs4eCL2XWqDiaCR5REK35f8l6hdS4GB8SI/0?wx_fmt=jpeg)

# [工具推荐]BurpSuite 多漏洞自动化探测插件xia\_tan (瞎探)

mapl3miss
mapl3miss

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

前言

通过修改请求参数对常见 Web 漏洞进行自动化初步探测的 BurpSuite 扩展插件。支持反射 XSS、SQL 注入（10 种数据库）、SSTI 模板注入（6 大家族 20+ 引擎）、NoSQL 注入，采用行级 Jaccard 相似度算法替代传统响应长度对比，结合多步布尔盲注对照算法大幅降低误报率。

功能特性

### 1. 反射 XSS 探测

* 注入唯一 HTML 标记 `<xia0tan>` 检测反射
* **未编码反射**（标签原样返回）→ 严重性 **High**
* **编码反射**（标记文本返回但 HTML 标签被编码）→ 严重性 **Info**
* 自动跳过 `Content-Type: application/json` 的响应（JSON 响应无 XSS 风险）
* 基线中已包含标记时自动跳过（降噪）

### 2. SQL 注入探测

#### 2.1 支持的数据库（10 种）

| 数据库 | 报错特征 | 示例特征 |
| --- | --- | --- |
| MySQL/MariaDB | 21 | `SQL syntax.*MySQL`, `XPATH syntax error`, `Division by 0` |
| MSSQL | 12 | `Unclosed quotation mark`, `Divide by zero error` |
| PostgreSQL | 10 | `ERROR: syntax error at or near`, `division by zero` |
| Oracle | 8 | `ORA-\d{4,5}`, `divisor is equal to zero` |
| SQLite | 7 | `SQLITE_ERROR`, `unrecognized token` |
| DB2 | 5 | `CLI Driver.*DB2`, `SQLCODE` |
| Informix | 3 | `com.informix.jdbc` |
| Sybase | 3 | `Adaptive Server` |
| MS Access | 3 | `JET Database Engine` |
| HQL/Hibernate | 4 | `org.hibernate.QueryException` |

#### 2.2 检测方式

| 阶段 | 类型 | 说明 |
| --- | --- | --- |
| 2A | ORDER BY 注入 | 针对排序参数（sort, order 等），使用 UPDATEXML/EXTRACTVALUE/FLOOR 报错 + CASE WHEN 条件差异 |
| 2B | 数字型注入 | 纯数字参数追加 `/1` 和 `/0`，对比响应差异和除零报错 |
| 2C | 报错探针 | 发送 `'"\` 触发语法错误，正则匹配 10 种数据库特征 |
| 2D | MySQL XPATH 报错 | 5 种 UPDATEXML/EXTRACTVALUE payload，覆盖单引号/括号/数字型上下文 |
| 2E | **布尔盲注** | **全新 OR/AND 多步对照算法**（见下方详细说明） |
| 2F | 延时注入 | 5 种数据库 SLEEP/WAITFOR/pg\_sleep 快速轮询，命中即停 |

#### 2.3 延时注入 WAF 绕过

| 数据库 | 绕过技巧 |
| --- | --- |
| MySQL | `BENCHMARK()`, `ST_Buffer()`, `JSON_KEYS()`, `ELT()`, `XOR`, 注释混淆 `SLEEP/**/()`, 大小写变异 `SlEEp()` |
| MSSQL | `WAITFOR DELAY`, 变量延迟 `DECLARE @d`, 条件延迟 `IF(1=1)` |
| PostgreSQL | `pg_sleep()`, 子查询延迟, `|| pg_sleep()` 拼接 |
| Oracle | `DBMS_PIPE.RECEIVE_MESSAGE()`, `DBMS_LOCK.SLEEP()`, `UTL_INADDR` |
| SQLite | `RANDOMBLOB()` 大计算量延迟, `LIKE(UPPER(HEX(...)))` |

### 3. SSTI 模板注入探测

覆盖 **6 大家族 20+ 模板引擎**，每个家族使用不同的唯一操作数，通过计算结果精确定位被执行的模板语法。

| 表达式语法 | 覆盖引擎 | 操作数示例 |
| --- | --- | --- |
| `{{A*B}}` | Jinja2, Twig, Pebble, Nunjucks, Handlebars, Smarty3 | 91371×91373 |
| `${A*B}` | Freemarker, Mako, Groovy, EL/JSP, Velocity, Thymeleaf | 91374×91376 |
| `<%=A*B%>` | ERB (Ruby), EJS (Node.js), ASP | 91377×91379 |
| `#{A*B}` | SpEL (Spring), Jade/Pug | 91380×91382 |
| `@(A*B)` | Razor (.NET) | 91383×91385 |
| `{A*B}` | Smarty2 (PHP) | 91386×91388 |

与 XSS 探测合并在同一请求中发送，节省请求数量。基线中已包含计算结果时自动跳过（降噪）。

### 4. NoSQL 注入探测

#### 4.1 布尔盲注（字符串上下文）

使用与 SQLi 相同的 **OR/AND 多步对照算法**，但语法为 JavaScript 风格：

| Payload | 语义 |
| --- | --- |
| `' || '1'=='1` | OR 恒真 |
| `' || '1'=='2` | OR 恒假 |
| `' && '1'=='1` | AND 恒真 |
| `' && '1'=='2` | AND 恒假 |

#### 4.2 操作符注入（JSON 请求体）

将 JSON 字段值替换为 MongoDB 操作符，检测响应差异和错误：

| 操作符 | Payload |
| --- | --- |
| `$gt` | `{"$gt":""}` |
| `$ne` | `{"$ne":""}` |
| `$regex` | `{"$regex":".*"}` |
| `$exists` | `{"$exists":true}` |
| `$where` | `{"$where":"return true"}` |

扫描流程

```
每个参数的完整扫描流程:
Phase 1: XSS + SSTI 合并探测 ........................ 1 request  └─ 一个 payload 同时测试 HTML 反射 + 6 种模板语法  └─ JSON 响应自动跳过 XSS 检测
Phase 2: SQL 注入 ................................... 2~8 requests  ├─ 2A: ORDER BY 注入 (仅排序参数)  ├─ 2B: 数字型注入 /1 vs /0 (仅数字参数)  ├─ 2C: 报错探针 '"\  ├─ 2D: MySQL XPATH 报错 (2C 未触发时)  ├─ 2E: 布尔盲注 OR/AND (2A~2D 均未确认时)  └─ 2F: 延时注入 (2A~2E 均未确认且非排序参数时)
Phase 3: NoSQL 注入 ................................. 2~4 requests  ├─ 3A: 布尔盲注 OR/AND (字符串上下文)  └─ 3B: 操作符注入 (仅 JSON 请求体)
总计: 每个参数约 5~13 个请求 (大部分情况 5~7 个)
```

## 配置说明

### 检测模块开关

| 选项 | 说明 | 默认 |
| --- | --- | --- |
| XSS | 反射 XSS 检测 | ✅ 启用 |
| SQLi | SQL 注入检测 | ✅ 启用 |
| SSTI | 模板注入检测 | ✅ 启用 |
| NoSQLi | NoSQL 注入检测 | ✅ 启用 |
| Time-SQLi | 延时注入检测 | ✅ 启用 |
| Cookie | Cookie 参数探测 | ❌ 关闭 |

> **Cookie 说明**：启用后，Cookie 中的每个参数都会被当作普通参数进行注入探测。建议配合 `Exclude params` 排除 CSRF token 等敏感 Cookie，避免因修改认证 Cookie 导致请求失败。

### CUD 增删改扫描开关

控制是否扫描增/删/改操作的接口，**默认全部关闭**以避免对业务数据产生副作用。

| 选项 | 说明 | 默认 | 匹配关键词 |
| --- | --- | --- | --- |
| 增(C) | 创建/新增类接口 | ❌ 关闭 | create, insert, save, register, signup, upload, submit, add, new, post, write |
| 删(D) | 删除类接口 | ❌ 关闭 | delete, remove, destroy, purge, del, drop, erase, clear |
| 改(U) | 修改/更新类接口 | ❌ 关闭 | update, edit, modify, change, patch, alter, set, put, revise |

**路径匹配规则：**

按 `/` 分割路径段，逐段检查是否以关键词开头：

| 路径示例 | 匹配结果 | 原因 |
| --- | --- | --- |
| `/api/deleteUser` | ✅ 删(D) | `deleteUser` 以 `delete` 开头 + 驼峰边界 |
| `/api/user_delete` | ✅ 删(D) | `user_delete` 分割后 `delete` 精确匹配 |
| `/api/add` | ✅ 增(C) | `add` 精确匹配 |
| `/api/addOrder` | ✅ 增(C) | `addOrder` 以 `add` 开头 + 驼峰边界 |
| `/api/address` | ❌ 不匹配 | `address` 虽以 `add` 开头但后续字符 `r` 非大写/分隔符 |
| `/api/delivery` | ❌ 不匹配 | `delivery` 虽以 `del` 开头但 `i` 非大写/分隔符 |
| `/api/settings` | ❌ 不匹配 | `settings` 虽以 `set` 开头但 `t` 非大写/分隔符 |

### 域名与路径过滤

| 配置项 | 说明 | 默认值 | 示例 |
| --- | --- | --- | --- |
| Domain scope | 域名白名单，空=全部 | 空 | `*.example.com, *.com, target.io` |
| Path blacklist | 路径黑名单，匹配则跳过 | 空 | `/static/*, *.js, *.css, /health*` |
| Path whitelist | 路径白名单，空=全部 | 空 | `/api/*, /search*, /user/*` |

**域名匹配规则：**

输入的域名会自动清洗，去除 `http://`/`https://` 前缀、端口号和尾部 `/`，然后做精确比对：

| 用户输入 | 清洗后 | 匹配效果 |
| --- | --- | --- |
| `example.com` | `example.com` | 精确匹配 `example.com` |
| `https://example.com` | `example.com` | 精确匹配 `example.com` |
| `example.com:8080` | `example.com` | 精确匹配 `example.com` |
| `https://example.com:443/` | `example.com` | 精确匹配 `example.com` |
| `*` | `*` | 匹配所有域名 |
| `*.com` | `*.com` | 匹配所有 `.com` 结尾的域名 |
| `*.example.com` | `*.example.com` | 匹配 `example.com` 及其所有子域名 |

> Burp 的 `IHttpService.getHost()` 返回的是纯主机名（不含端口），插件会对用户输入和实际主机名做相同的清洗处理后再做精确比对。匹配失败时会在 Burp Output 输出详细日志（含原始值和清洗后的值），便于排查。

**路径匹配规则：**

* `/api/*` → 匹配 `/api/` 开头的路径
* `*.php` → 匹配 `.php` 结尾的路径
* `*admin*` → 匹配包含 `admin` 的路径
* `/login` → 精确匹配

### 参数与阈值

| 选项 | 说明 | 默认值 |
| --- | --- | --- |
| Exclude params | 排除的参数名（逗号分隔） | `csrf,token,_t,timestamp` |
| Delay(ms) | 请求间隔毫秒数 | `0` |
| Time thresh(ms) | 延时注入判定阈值 | `4000` |
| Sim thresh | 响应相似度阈值 (0.0~1.0) | `0.9` |

### 自动过滤规则

以下内容会被自动跳过，无需手动配置：

* **静态资源**: `.js`, `.css`, `.png`, `.jpg`, `.gif`, `.svg`, `.ico`, `.woff`, `.pdf`, `.zip` 等
* **二进制响应**: `image/*`, `audio/*`, `video/*`, `application/octet-stream`, `application/pdf`, `application/zip`
* **Cookie 参数**: 默认不扫描，需勾选 **Cookie** 开关手动启用
* **XML/Multipart 参数**: 不扫描 XML 属性和 Multipart 属性参数
* **超长参数值**: 值长度 ≥ 512 字符的参数自动跳过
* **去重**: 相同 `主机+方法+路径+参数名+参数类型` 不会重复扫描

### 编码处理

| 参数类型 | 编码方式 |
| --- | --- |
| GET 参数 (PARAM\_URL) | `URLEncoder.encode()` 全编码 |
| POST 表单参数 (PARAM\_BODY) | 选择性编码（空格、`<>&+#|\[\]{}\\`） |
| JSON 参数 | JSON 转义（`"`, `\`, `\n`, `\r`, `\t`, `\b`, `\f`） |

## 使用方法

### 手动扫描

在 Proxy/Repeater/Target 等模块中右键请求：

* **Send to xia\_tan** — 使用当前配置进行全量扫描
* **xia\_tan scan...** — 选择特定检测类型（XSS/SQLi/SSTI/NoSQLi）

### 自动监控

勾选 `Monitor Proxy` 和/或 `Monitor Repeater`，插件会自动拦截经过的请求并进行扫描。

### 查看结果

| 列 | 说明 |
| --- | --- |
| # | 序号 |
| Host | 目标主机 |
| Method | HTTP 方法 |
| URL | 请求 URL |
| Param | 注入参数名 |
| Type | 漏洞类型 (XSS/SQLi/SSTI/NoSQLi) |
| Detail | 检测细节 |
| Evidence | 判定证据 |
| Severity | 严重性 (High/Medium/Possible/Info) |
| Length | 响应长度 |
| Time | 响应时间 |
| Code | HTTP 状态码 |

点击结果行可在下方查看完整的请求和响应内容。右键可复制 URL 或 Payload。

### 严重性说明

| 颜色 | 级别 | 含义 |
| --- | --- | --- |
| 🔴 红色 | High | 高置信度确认（报错注入、布尔盲注确认、延时确认、未编码 XSS 反射、SSTI 运算确认） |
| 🟠 橙色 | Medium | 中置信度（NoSQLi 操作符差异、编码反射等） |
| ⚪ 白色 | Possible | 低置信度（仅相似度差异、需人工确认） |
| 🔵 蓝色 | Info | 信息性（编码反射等） |

实战测试

直接找一个国外的测试一下

```
https://4.178.62.156/dvwa/security.php
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRptpBHHq0J1xYKyq4ic1cCN55ZduoXhz2uDTcUK9RPDhu3Sy3D97HnE6MrC6SfYiaV7Gk2JRHiaMb1X9Hfiaq73OpobH4TRk5iaicW0/640?wx_fmt=png&from=appmsg)

测试一下xss

![](https://mmbiz.qpic...