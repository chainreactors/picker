---
title: Web-pwn的栈溢出和堆机制详细入门
url: https://forum.butian.net/share/3716
source: 奇安信攻防社区
date: 2024-09-13
fetch_date: 2025-10-06T18:21:06.588356
---

# Web-pwn的栈溢出和堆机制详细入门

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Web-pwn的栈溢出和堆机制详细入门

* [CTF](https://forum.butian.net/topic/52)

Web-pwn的栈溢出和堆机制详细入门

参考
==
[https://xz.aliyun.com/t/15166?time\\_\\_1311=GqjxuQi%3DDQ%3D0yRx%2BxCqiKwmmm93Y5Lox#toc-1](https://xz.aliyun.com/t/15166?time\_\_1311=GqjxuQi=DQ=0yRx%2BxCqiKwmmm93Y5Lox#toc-1)
简介
==
Webpwn目前大多数针对的是Php，我们需要重点分析的是 PHP 加载的外部拓展，漏洞点通常在 so拓展库中。由于 php加载扩展库来调用其内部函数，所以和常规 PWN题最大的不同点，就是我们不能直接获得交互式的shell。这里通常是需要采用 popen或者 exec函数族来进行执行 bash命令来反弹 shell，直接执行 one\\_gadget或者 system是不可行的。
生命周期
====
1. 扩展模块的生命周期:
a) Module Init (MINIT):PHP解释器启动，加载相关模块，在此时调用相关模块的MINIT方法，仅被调用一次
例子: 假设我们有一个数据库连接池扩展。
```c
PHP\_MINIT\_FUNCTION(db\_pool)
{
// 初始化连接池
initialize\_connection\_pool();
return SUCCESS;
}
```
这个函数在PHP启动时只调用一次,用于初始化连接池。
b) Request Init (RINIT):每个请求达到时都被触发。SAPI层将控制权交由PHP层，PHP初始化本次请求执行脚本所需的环境变量，函数列表等，调用所有模块的RINIT函数。
例子: 一个会话管理扩展。
```c
PHP\_RINIT\_FUNCTION(session\_manager)
{
// 为每个请求创建新的会话
create\_new\_session();
return SUCCESS;
}
```
每个HTTP请求开始时都会调用此函数,为每个请求创建新会话。
c) Request Shutdown (RSHUTDOWN):请求结束，PHP就会自动清理程序，顺序调用各个模块的RSHUTDOWN方法，清除程序运行期间的符号表。
例子: 清理请求特定资源的扩展。
```c
PHP\_RSHUTDOWN\_FUNCTION(resource\_cleaner)
{
// 清理请求期间分配的资源
free\_request\_resources();
return SUCCESS;
}
```
每个请求结束时调用,用于清理该请求使用的资源。
d) Module Shutdown (MSHUTDOWN):服务器关闭，PHP调用各个模块的MSHUTDOWN方法释放内存。
例子: 关闭数据库连接池。
```c
PHP\_MSHUTDOWN\_FUNCTION(db\_pool)
{
// 关闭连接池
shutdown\_connection\_pool();
return SUCCESS;
}
```
PHP终止时调用,用于清理模块级资源。
2. PHP的运行模式:
a) CLI运行模式 (单进程SAPI):
例子:
```bash
php script.php
```
这会启动PHP解释器,执行script.php,然后退出。整个过程只有一个MINIT和一个MSHUTDOWN,但RINIT和RSHUTDOWN会为脚本执行调用一次。
b) CGI运行模式 (大部分 多进程SAPI):
例子: Apache with mod\\_cgi
当收到HTTP请求时,Apache会为每个请求fork一个新的PHP进程。
```php
[Apache] <- HTTP Request
|
├── [PHP Process 1] (MINIT -> RINIT -> Execute -> RSHUTDOWN -> MSHUTDOWN)
|
├── [PHP Process 2] (MINIT -> RINIT -> Execute -> RSHUTDOWN -> MSHUTDOWN)
|
└── [PHP Process 3] (MINIT -> RINIT -> Execute -> RSHUTDOWN -> MSHUTDOWN)
```
每个进程处理一个请求后就终止,所以每个请求都会经历完整的模块生命周期。
> 其中fork的进程，和原进程的内存布局一般来说是一模一样的，所以这里如果能拿到/proc/{pid}/maps文件，则可以拿到该进程的内存布局，形成内存泄露，此方式在De1CTF中的这道WEBPWN上是第一个突破点，利用的其有漏洞的包含函数来读取/proc/self/maps，可以拿到所有基地址，从而无视PIE保护。
```bash
llk@ubuntu:~/Desktop/tools/php-src/ext/hello/modules$ cat /proc/90065/maps
555555554000-555555627000 r--p 00000000 08:05 286222 /usr/bin/php7.4
555555627000-555555891000 r-xp 000d3000 08:05 286222 /usr/bin/php7.4
555555891000-555555957000 r--p 0033d000 08:05 286222 /usr/bin/php7.4
555555958000-5555559e3000 r--p 00403000 08:05 286222 /usr/bin/php7.4
5555559e3000-5555559e5000 rw-p 0048e000 08:05 286222 /usr/bin/php7.4
5555559e5000-555555ba0000 rw-p 00000000 00:00 0 [heap]
7ffff3f22000-7ffff3fa3000 rw-p 00000000 00:00 0
7ffff3fcc000-7ffff3fd0000 r--p 00000000 08:05 280238 /usr/lib/x86\_64-linux-gnu/libgpg-error.so.0.28.0
7ffff3fd0000-7ffff3fe3000 r-xp 00004000 08:05 280238 /usr/lib/x86\_64-linux-gnu/libgpg-error.so.0.28.0
7ffff3fe3000-7ffff3fed000 r--p 00017000 08:05 280238 /usr/lib/x86\_64-linux-gnu/libgpg-error.so.0.28.0
7ffff3fed000-7ffff3fee000 r--p 00020000 08:05 280238 /usr/lib/x86\_64-linux-gnu/libgpg-error.so.0.28.0
7ffff3fee000-7ffff3fef000 rw-p 00021000 08:05 280238 /usr/lib/x86\_64-linux-gnu/libgpg-error.so.0.28.0
7ffff3fef000-7ffff3ffb000 r--p 00000000 08:05 280162 /usr/lib/x86\_64-linux-gnu/libgcrypt.so.20.2.5
7ffff3ffb000-7ffff40c9000 r-xp 0000c000 08:05 280162 /usr/lib/x86\_64-linux-gnu/libgcrypt.so.20.2.5
7ffff40c9000-7ffff4106000 r--p 000da000 08:05 280162 /usr/lib/x86\_64-linux-gnu/libgcrypt.so.20.2.5
7ffff4106000-7ffff4108000 r--p 00116000 08:05 280162 /usr/lib/x86\_64-linux-gnu/libgcrypt.so.20.2.5
7ffff4108000-7ffff410d000 rw-p 00118000 08:05 280162 /usr/lib/x86\_64-linux-gnu/libgcrypt.so.20.2.5
7ffff410d000-7ffff4111000 r--p 00000000 08:05 280080 /usr/lib/x86\_64-linux-gnu/libexslt.so.0.8.20
7ffff4111000-7ffff411f000 r-xp 00004000 08:05 280080 /usr/lib/x86\_64-linux-gnu/libexslt.so.0.8.20
7ffff411f000-7ffff4123000 r--p 00012000 08:05 280080 /usr/lib/x86\_64-linux-gnu/libexslt.so.0.8.20
7ffff4123000-7ffff4124000 r--p 00015000 08:05 280080 /usr/lib/x86\_64-linux-gnu/libexslt.so.0.8.20
```
c) FastCGI运行模式 (多进程SAPI,但进程可复用):
例子: Nginx with PHP-FPM
```php
[Nginx] <- HTTP Requests
|
├── [PHP-FPM Process 1] (MINIT -> [RINIT -> Execute -> RSHUTDOWN] x N -> MSHUTDOWN)
|
└── [PHP-FPM Process 2] (MINIT -> [RINIT -> Execute -> RSHUTDOWN] x N -> MSHUTDOWN)
```
PHP-FPM进程在处理多个请求后才会退出,所以MINIT和MSHUTDOWN只在进程启动和结束时调用一次,而RINIT和RSHUTDOWN则为每个请求调用。
php扩展模块
=======
[小猪教你开发php扩展](https://blog.yanjingang.com/?p=3070)
在 Linux环境下，PHP 拓展通常为 .so文件，拓展模块放置的路径可以通过如下方式查看：
搭建php
-----
```bash
sudo apt install php php-dev # 安装php，以及php开发包头
php -v # 查看php版本 直到当前对应的版本是7.4.3
```
根据版本下载对应源码
<https://github.com/php/php-src/tree/PHP-7.4.3>
```bash
git clone https://github.com/php/php-src.git
cd php-src
git checkout PHP-7.4.3
git fetch
```
源码目录结构
```c
php-src
|\_\_\_\_build --和编译有关的目录，里面包括wk，awk和sh脚本用于编译处理，其中m4文件是linux下编译程序自动生成的文件，可以使用buildconf命令操作具体的配置文件。
|\_\_\_\_ext --扩展库代码，例如Mysql，gd，zlib，xml，iconv 等我们熟悉的扩展库，ext\_skel是linux下扩展生成脚本，windows下使用ext\_skel\_win32.php。
|\_\_\_\_main --主目录，包含PHP的主要宏定义文件，php.h包含绝大部分PHP宏及PHP API定义。
|\_\_\_\_netware --网络目录，只有sendmail\_nw.h和start.c，分别定义SOCK通信所需要的头文件和具体实现。
|\_\_\_\_pear --扩展包目录，PHP Extension and Application Repository。
|\_\_\_\_sapi --各种服务器的接口调用，如Apache，IIS等。
|\_\_\_\_scripts --linux下的脚本目录。
|\_\_\_\_tests --测试脚本目录，主要是phpt脚本，由--TEST--，--POST--，--FILE--，--EXPECT--组成，需要初始化可添加--INI--部分。
|\_\_\_\_TSRM --线程安全资源管理器，Thread Safe Resource Manager保证在单线程和多线程模型下的线程安全和代码一致性。
|\_\_\_\_win32 --Windows下编译PHP 有关的脚本。
|\_\_\_\_Zend --包含Zend引擎的所有文件，包括PHP的生命周期，内存管理，变量定义和赋值以及函数宏定义等等。
```
扩展模块初始化
-------
```bash
cd ext
php ext\_skel.php --ext extend\_name 在当前目录生成一个extend\_name 的文件夹
```
```bash
cd hello
ls
config.m4 config.w32 hello.c php\_hello.h tests
```
1. config.m4
- 用途：用于 Unix-like 系统的配置脚本
- 作用：定义扩展的编译选项，包括依赖项、编译标志等
- 在运行 ./configure 时使用
2. config.w32
- 用途：用于 Windows 系统的配置脚本
- 作用：类似于 config.m4，但针对 Windows 环境
- 在 Windows 上编译扩展时使用
3. hello.c
- 用途：扩展的主要源代码文件
- 作用：
- 包含扩展的核心功能实现
- 定义 PHP 函数、类、常量等
- 包含模块初始化和关闭函数
4. php\\_hello.h
- 用途：扩展的头文件
- 作用：
- 声明在 hello.c 中定义的函数
- 定义扩展使用的常量和宏
- 可能包含其他必要的结构定义
5. tests/ 目录
- 用途：存放扩展的测试文件
- 作用：
- 包含 .phpt 文件，用于测试扩展的功能
- 帮助确保扩展在不同环境下正常工作
- 可以使用 `make test` 运行这些测试
编写扩展模块
------
编写PHP扩展是基于Zend API和一些宏的，所以如果要编写核心代码，我们首先要弄清楚PHP Extension的结构。因为一个PHP Extension在C语言层面实际上就是一个zend\\_module\\_entry结构体
关于其类型zend\\_module\\_entry的定义可以在PHP源代码的“Zend/zend\\_modules.h”文件里找到，下面代码是zend\\_module\\_entry的定义
```c
typedef struct \_zend\_module\_entry zend\_module\_entry;
struct \_zend\_module\_entry {
unsigned short size;
unsigned int zend\_api;
unsigned char zend\_debug;
unsigned char zts;
const struct \_zend\_ini\_entry \*ini\_entry;
const struct \_zend\_module\_dep \*deps;
const char \*name; # PHP Extension的名字
const struct \_zend\_function\_entry \*functions; # 存放我们在此扩展中定义的函数的引用
int (\*module\_startup\_func)(INIT\_FUNC\_ARGS); # 函数指针，扩展模块加载时被调用
int (\*module\_shutdown\_func)(SHUTDOWN\_FUNC\_ARGS); # 函数指针，扩展模块卸载时时被调用
int (\*request\_startup\_func)(INIT\_FUNC\_ARGS); # 函数指针，每个请求开始时时被调用
int (\*request\_shutdown\_func)(SHUTDOWN\_FUNC\_ARGS); # 函数指针，每个请求结束时时被调用
void (\*info\_func)(ZEND\_MODULE\_INFO\_FUNC\_ARGS); # 函数指针，这个指针指向的函数会在执行phpinfo()时被调用，用于显示自定义模块信息。
const char \*version; # 模块的版本
size\_t globals\_size;
#ifdef ZTS
ts\_rsrc\_id\* globals\_id\_ptr;
#else
void\* globals\_ptr;
#endif
void (\*...