---
title: 大象要一口一口吃：PHP PDO扩展中的NUL字节SQL注入与空指针解引用漏洞
url: https://mp.weixin.qq.com/s/foMleOiYvmBA-d3hq8ks_g
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:58:05.233126
---

# 大象要一口一口吃：PHP PDO扩展中的NUL字节SQL注入与空指针解引用漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdcicA9mmIgBxG8caBkKSJ1hE5YZhUPgRSAxR5L7bzTap0ZxEib2Ed2lU2kNdoboHZibqicttV9hryctndv0Xnwy04w5AgOBW6MpvY/0?wx_fmt=png&from=appmsg)

# 大象要一口一口吃：PHP PDO扩展中的NUL字节SQL注入与空指针解引用漏洞

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> PHP核心及其扩展常被视为成熟且经过充分加固的攻击面，但底层实现bug仍然会溜进来。本文深入剖析PDO扩展中两个代表性漏洞：pdo\_firebird驱动中因NUL字节处理不当导致的SQL注入（CVE-2025-14179），以及pdo\_pgsql在模拟预处理模式下因libpq报错引发的空指针解引用（CVE-2025-14180）。这两个问题暴露了一个共同根因——PHP托管环境与C级库之间对边界输入的不安全处理。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdicz5utWjQ9ZbkZc2qHueBEHNTWd6TTwJpInI5OYdEgpte03SFUXktR5unXet5UG13z79JlgLxbKMvnUWiaraqf0dVIOQoEbiaIo/640?wx_fmt=jpeg&from=appmsg)

PHP核心和捆绑扩展通常被看作成熟且加固过的攻击面，但底层实现层面的bug照样能溜进去。我们在之前的研究文章《Hack the Elephant One Bite at a Time: JPEG-Related Memory-Safety Bugs in PHP》[1]里展示了PHP解析JPEG时触发的内存安全问题。

沿着这个方向，我们对PDO整体及其各组件——也就是连接不同数据库后端的DBMS特定驱动——做了一次更深入的审查。这项工作越挖越深，最终在第三方依赖中也发现了漏洞。具体来说，我们在PostgreSQL客户端库（libpq）中识别出一个整数溢出，详见《Attack arithmetic: how an integer overflow in PostgreSQL libpq leads to denial of service》[2]。还在Firebird 3客户端库（fbclient）中发现了一个信息泄露问题[3]：当Firebird 3客户端与Firebird 4或更高版本服务器通信时，XSQLDA字段中不正确的长度值会触发越界读取，暴露非预期数据。

不过，我们这次工作的核心成果还是跟PDO扩展本身的架构有关。审查过程中，我们记录了大量驱动特定行为，以及驱动与目标DBMS交互时的多个缺陷。本文挑两个代表性漏洞来细说：

* CVE-2025-14179[4]：pdo\_firebird中通过引用字符串内NUL字节实现的SQL注入
* CVE-2025-14180[5]：PDO引用过程中的空指针解引用

通过实际示例，你会看到对关键驱动例程的深度审查如何暴露了Web应用开发者多年来信赖的防御机制中的严重弱点。

## 与DBMS的交互是怎么回事

PHP不直接跟数据库对话。连接和查询执行始终通过扩展进行。在实践中，数据库相关扩展通常分两类：通用PDO接口（依赖pdo\_pgsql等数据库特定驱动）和原生扩展，如mysqli、pgsql或sqlite3。在内部，这些组件可能使用DBMS供应商的官方客户端C库（比如libpq）、嵌入式进程内引擎（如SQLite）或中间ODBC层。所以，你选择的扩展及其底层实现细节不仅决定了功能和兼容性，也塑造了攻击面和漏洞向量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdcicA9mmIgBxG8caBkKSJ1hE5YZhUPgRSAxR5L7bzTap0ZxEib2Ed2lU2kNdoboHZibqicttV9hryctndv0Xnwy04w5AgOBW6MpvY/640?wx_fmt=png&from=appmsg)

▲ PHP中DBMS访问的整体架构

这张图展示了PHP中DBMS访问的整体架构。应用代码调用PHP扩展（要么通过抽象PDO接口，要么通过原生扩展）。从那里，查询被转发到目标DBMS的客户端库、嵌入式进程内引擎（如SQLite）或通用ODBC层。这个多阶段结构很关键：扩展层加上它依赖的底层库，共同决定了兼容性、可用功能集、操作系统特定行为以及相关的漏洞向量。

下面拆解这个架构中三个经常让人困惑的细节。

### 1. ODBC是什么？为什么画成单独一层？

开放数据库连接（ODBC）是一个标准化的、供应商中立的数据库访问接口。应用程序（或PHP扩展）调用ODBC API，ODBC驱动管理器将这些调用路由到DBMS特定的ODBC驱动。在架构图中，ODBC通常画成独立一层，因为它把公共API表面跟DBMS特定的底层实现细节干净地分开了。

### 2. 为什么MS SQL Server的调用栈比其他数据库复杂？

在PHP中，SQL Server支持通常由pdo\_sqlsrv或sqlsrv扩展提供。这些扩展构建在Microsoft ODBC Driver for SQL Server之上，在类Unix系统上还需要一个ODBC驱动管理器，比如unixODBC。这种分层模型是有意为之：微软拥有并维护实现SQL Server特定行为（认证、TLS和协议细节）的底层驱动，而PHP扩展暴露熟悉的PDO接口。还有一个替代方案是pdo\_dblib，它通过FreeTDS库绕过ODBC，但这不是主流选择。

### 3. libmysqlclient和mysqlnd在MySQL场景下有什么不同？

历史上，PHP的MySQL扩展可以针对两种不同的客户端库编译：

* libmysqlclient是MySQL生态维护的传统外部客户端库。
* mysqlnd（MySQL Native Driver）是PHP的原生MySQL驱动，专门为PHP运行时构建，与Zend Engine内存管理器紧密集成。

PHP官方文档建议使用捆绑的mysqlnd库而不是libmysqlclient，因为mysqlnd性能更好、内存占用更少，而且不需要安装第三方系统组件。当然，遗留部署环境可能仍然支持任一种后端。

> 推荐使用mysqlnd库而非MySQL Client Server库（libmysqlclient）。两个库都受支持并在持续改进中。
> https://www.php.net/manual/en/mysqlinfo.library.choosing.php

## PHP Data Objects（PDO）

PDO（PHP Data Objects）是PHP的标准数据库抽象层，提供一致、面向对象的API来与多种DBMS交互。顾名思义，连接和结果集都暴露为对象（PDO和PDOStatement）。结果是，像准备和执行语句、管理事务、获取行这类常见工作流，不管后端驱动是什么，看起来几乎一模一样。这降低了数据库特定耦合，让应用代码更容易长期维护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc8JfBiaFrYLLOic2gJQtC16ut5X6tmFcvGPIax0eA6icueJl3NnyLqhYw86fLFq0peADGC3BOjYP7TpSlrTEyWqmlhJnajic47DW0/640?wx_fmt=png&from=appmsg)

在实践中，目标DBMS在连接初始化时选定。DSN前缀——DSN中冒号之前的部分（例如pgsql:、mysql:、sqlite:）——告诉PHP加载哪个PDO驱动。之后，所有数据库访问都通过相同的PDO API进行，差异主要限于支持的DSN选项、SQL方言细节和驱动特定行为。

<?php
 // 连接到PostgreSQL
 $dsn\_pg = 'pgsql:host=localhost;port=5432;dbname=db';
 $pdo\_pg = new PDO($dsn\_pg, 'user', 'password');

// 连接到Firebird
$dsn\_fb = 'firebird:dbname=192.168.1.2:/data/db.fdb;charset=utf8;';
$pdo\_fb = new PDO($dsn\_fb, 'user', 'password');

### 选项1：模拟模式（默认）

在这种模式下，参数准备完全在PHP端完成。pdo\_mysql驱动自己转义数据，把它插入SQL模板，然后发送一条完整的文本查询到服务器。

PHP代码（pdo\_prepare.php）：

<?php
$pdo = new PDO('mysql:host=127.0.0.1;dbname=db;charset=utf8mb4', 'user', 'password');

$stmt = $pdo->prepare('SELECT id, name FROM users WHERE id = ?');
$stmt->execute([1]); // 传入数字1作为参数

foreach ($stmt->fetchAll() as $row) {
    echo $row['id'] . ':' . $row['name'] . PHP\_EOL;
}

MySQL通用日志：

-- 服务器收到纯文本语句（Query命令）。
-- 注意：PHP端整数1在日志中显示为带引号的字符串'1'。

Id Command    Argument
48 Connect    user@localhost on db using TCP/IP
48 Query      SELECT id, name FROM users WHERE id = '1'
48 Quit

### 选项2：关闭模拟（原生语句）

关闭模拟后，PDO切换到MySQL的原生二进制协议。SQL模板和绑定的参数分两步分别传输：先准备语句，然后执行系统调用，参数值以未修改的数据形式发送。

PHP代码（pdo\_prepare.php）：

<?php
$options = [
    PDO::ATTR\_EMULATE\_PREPARES => false, // 关闭模拟
];
$pdo = new PDO('mysql:host=127.0.0.1;dbname=db;charset=utf8mb4', 'user', 'password', $options);

$stmt = $pdo->prepare('SELECT id, name FROM users WHERE id = ?');
$stmt->execute([1]); // 传入值1

foreach ($stmt->fetchAll() as $row) {
    echo $row['id'] . ':' . $row['name'] . PHP\_EOL;
}

MySQL通用日志：

-- 服务器分两个阶段处理语句（Prepare和Execute）。
-- 注意：Execute阶段，原始值1不带引号发送。

Id Command    Argument
49 Connect    user@localhost on db using TCP/IP
49 Prepare    SELECT id, name FROM users WHERE id = ?
49 Execute    SELECT id, name FROM users WHERE id = 1
49 Close stmt
49 Quit

下面这张表汇总了各PDO驱动对预处理语句模拟的支持情况和行为差异：

| PDO驱动 | ATTR\_EMULATE\_PREPARES | 默认值 | 查询如何准备 |
| --- | --- | --- | --- |
| pdo\_firebird | — | 始终原生prepare | — |
| pdo\_mysql | ON | 模拟；可关闭 | — |
| pdo\_odbc | — | 始终原生（通过ODBC SQLPrepare） | — |
| pdo\_pgsql | OFF | 原生；仅在明确配置或特殊模式下模拟 | — |
| pdo\_sqlite | — | 始终原生prepare | — |
| pdo\_sqlsrv | OFF | 原生；模拟为可选项 | — |

对于使用模拟的驱动，预处理语句实际上变成了客户端查询重写：PDO替换占位符、转义值，然后把最终文本查询发给服务器。

## 发现的漏洞

### 漏洞1：pdo\_firebird中通过引用字符串内NUL字节实现的SQL注入

▲ 安全公告，CVE-2025-14179，高危，Aleksey Solovev、Nikita Sveshnikov（Positive Technologies）

分析pdo\_firebird如何分词和准备SQL查询时，我们发现了一个破坏查询结构的漏洞。这里反直觉的地方在于：驱动端的引用例程（quoter）本身工作正常，产生的是正确转义的输出。问题出在后面：在PDO::prepare期间，pdo\_firebird重新解析并重建SQL，错误地处理了包含NUL字节（\0）的字符串字面量。结果是驱动丢弃了终止引号，让攻击者控制的输入从引用字面量中溢出，进入可执行SQL上下文，实现SQL注入。

#### 技术细节

在Firebird PDO驱动中，初始字符串清洗由firebird\_handle\_quoter处理，这个函数通过PDO::quote暴露。这个组件行为是正确的。

我们来验证引用例程。下面这个测试确认firebird\_handle\_quoter在多种编码和表示形式下都能正确转义特殊字符，包括引号、反引号和显式NUL字节：

PHP清洗测试代码：

<?php
$pdo = new PDO('firebird:dbname=127.0.0.1:/var/lib/firebird/data/mirror.fdb;charset=utf8;', 'user', 'password');

$p1 = $pdo->quote("alice'\x27\u{27}`\x60\u{60}\"\x22\u{22}\x00\u{00}");
$p2 = $pdo->quote("offensive'\x27\u{27}`\x60\u{60}\"\x22\u{22}\x00\u{00}");

$sql = "SELECT \* FROM users WHERE username = $p1 AND department = $p2";
file\_put\_contents('./sql\_query.dump', $sql);

Dump输出（字符串和通过xxd查看原始字节）：

$ ./php cli.php && cat sql\_query.dump
SELECT \* FROM users WHERE username = 'alice''''''```"""' AND department = 'offensive''''''```"""'
$ xxd sql\_query.dump
00000000: 5345 4c45 4354 202a 2046 524f 4d20 7573  SELECT \* FROM us
00000010: 6572 7320 5748 4552 4520 7573 6572 6e61  ers WHERE userna
00000020: 6d65 203d 2027 616c 6963 6527 2727 2727  me = 'alice'''''
00000030: 2760 6060 2222 2200 0027 2041 4e44 2064  '```"""..' AND d
00000040: 6570 6172 746d 656e 7420 3d20 276f 6666  epartment = 'off
00000050: 656e 7369 7665 2727 2727 2727 6060 6022  ensive''''''```"
00000060: 2222 0000 27                             ""..'

firebird\_handle\_quoter表现符合预期：它把单引号加倍，并正确地在由'（27）分隔的字符串字面量内保留了NUL字节（00）。引用的字符串上下文保持完好。

#### PDO::prepare内部逻辑是怎样被破坏的

问题在已经引用过、语法有效的SQL字符串被传入语句准备路径时触发。对查询的破坏性转换可以直接在PHP核心调用流中追踪：

**1. 进入PDO核心的入口点**

在应用层，代码调用$pdo->prepare($query)。PDO核心按原样接受SQL字符串，不做额外标准化或安全检查，直接通过调用驱动的preparer回调[6]转发给数据库特定驱动。

/\* ext/pdo/pdo\_dbh.c \*/

if (dbh->methods->preparer(dbh, query, &stmt, driver\_options)) {

**2. 控制权转移到Firebird驱动**

此时，执行进入Firebird PDO驱动。驱动把SQL字符串直接转发到其内部语句准备路径php\_firebird\_alloc\_prepare\_stmt[7]，PDO层不做任何额外标准化。

/\* ext/pdo\_firebird/firebird\_driver.c \*/

/\* allocate and prepare statement \*/
if (!php\_firebird\_alloc\_prepare\_stmt(dbh, sql, &num\_sqlda, &s, np)) {
    break;
}

**3. 查询解析和预处理启动**

php\_firebird\_alloc\_prepare\_stmt调用php\_firebird\_preprocess[8]，后者对传入的SQL字符串进行分词。分词器实现为php\_firebird\_get\_token[9]状态机，逐字节扫描SQL字符串并将其拆分为逻辑token。然后驱动通过遍历switch(tok)循环中的token类型，将对应片段追加到sql\_out缓冲区来重建语句：

/\* ext/pdo\_firebird/firebird\_drive...