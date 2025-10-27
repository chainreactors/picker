---
title: PHP代码审计-某cms逻辑漏洞导致getshell
url: https://www.secpulse.com/archives/197859.html
source: 安全脉搏
date: 2023-03-21
fetch_date: 2025-10-04T10:07:32.064099
---

# PHP代码审计-某cms逻辑漏洞导致getshell

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# PHP代码审计-某cms逻辑漏洞导致getshell

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-20

33,924

**以下文章来源于亿人安全 ，作者N1eC**

**文章首发在：奇安信攻防社区**

**https://forum.butian.net/share/2142**

前言 如果存在exec进行拼接的漏洞，该如何绕过 &lt;mark&gt;一黑俩匹配 &lt;/mark&gt;？当前如果是拼接和编码这种手法就不说了，现在在看的师傅您是审计大牛的话，这文章可以忽略不看。黑名单...

# 前言

如果存在exec进行拼接的漏洞，该如何绕过 <mark>一黑俩匹配 </mark>？
当前如果是拼接和编码这种手法就不说了，现在在看的师傅您是审计大牛的话，这文章可以忽略不看。

## 黑名单

```
$_GET[
$_POST[
$_REQUEST[
$_COOKIE[
$_SESSION[
file_put_contents
file_get_contents
fwrite
phpinfo
base64
`
shell_exec
eval
assert
system
exec
passthru
pcntl_exec
popen
proc_open
print_r
print
urldecode
chr
include
request
__FILE__
__DIR__
copy
call_user_
preg_replace
array_map
array_reverse
array_filter
getallheaders
get_headers
decode_string
htmlspecialchars
session_id
strrev
substr
php.info
```

## 第一个匹配：

```
/([w]+)([x00-x1Fx7F/*<>%ws\\]+)?(/i
```

## 第二个匹配：

这里不能有$符号，这里是重点 ,当然如果你想编码也可以，或者啥的手法都行，不过我在此之前没想到过，可以继续往下看

```
/{pboot:if(([^}^$]+))}([sS]*?){/pboot:if}/
```

# 正文

先看效果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291096.png)

## 审计流程

通过审计工具半自动筛选出漏洞点。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291098.png)

跟进该漏洞点文件：apps/home/controller/ParserController.php

最终是通过了`$matches[1][$i]`进入到eval函数中。

### 第一个黑名单

接着往上看，这里有黑名单，如果`$matches[1][$i]`有黑名单就会跳出解析

<mark>这里的\是社区编辑器默认加上防止转义，太多就懒得改了</mark>

```
// 过滤特殊字符串

if (preg_match('/(\([\w\s\.]+\))|(\$_GET\[)|(\$_POST\[)|(\$_REQUEST\[)|(\$_COOKIE\[)|(\$_SESSION\[)|(file_put_contents)|(file_get_contents)|(fwrite)|(phpinfo)|(base64)|(`)|(shell_exec)|(eval)|(assert)|(system)|(exec)|(passthru)|(pcntl_exec)|(popen)|(proc_open)|(print_r)|(print)|(urldecode)|(chr)|(include)|(request)|(__FILE__)|(__DIR__)|(copy)|(call_user_)|(preg_replace)|(array_map)|(array_reverse)|(array_filter)|(getallheaders)|(get_headers)|(decode_string)|(htmlspecialchars)|(session_id)|(strrev)|(substr)|(php.info)/i', $matches[1][$i])) {

$danger = true;

}

// 如果有危险函数，则不解析该IF

if ($danger) {

continue;

}
```

黑名单分别是拦截以下内容：

```
$_GET[

$_POST[

$_REQUEST[

$_COOKIE[

$_SESSION[

file_put_contents

file_get_contents

fwrite

phpinfo

base64

`

shell_exec

eval

assert

system

exec

passthru

pcntl_exec

popen

proc_open

print_r

print

urldecode

chr

include

request

__FILE__

__DIR__

copy

call_user_

preg_replace

array_map

array_reverse

array_filter

getallheaders

get_headers

decode_string

htmlspecialchars

session_id

strrev

substr

php.info
```

这可以看出过滤了好多函数，当然既然是黑名单就有绕过的方式，这里可以是加密形式绕过，不过加密后的密文做成payload就逆向解密不了了，因为是由特殊不可见数据流存在就会导致反解密会不到原来的明文。

这里可以用file和fputs函数绕过

### 第一个过滤

继续往上看，看到这个if判断，这里也是将`$matches[1][$i]`进行过滤，保证用户输入的字符串是无危害的，简单来说就是‘括号前面不能有字母、数字字符串’。

```
// 带有函数的条件语句进行安全校验

if (preg_match_all('/([\w]+)([\x00-\x1F\x7F\/\*\<\>\%\w\s\\\\]+)?\(/i', $matches[1][$i], $matches2)) {

foreach ($matches2[1] as $value) {

if (function_exists(trim($value)) && ! in_array($value, $white_fun)) {

$danger = true;

break;

}

}

foreach ($matches2[2] as $value) {

if (function_exists(trim($value)) && ! in_array($value, $white_fun)) {

$danger = true;

break;

}

}

}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-16792910981.png)

当然这里也是黑名单，直接`/*--*/`绕过

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-16792910982.png)

### 4.3. 第三个过滤

这个就比较好过了就是指定的标签语法，使用这个`{pboot:if(312313)}(13123){/pboot:if}`

#### 4.3.1. 注意：

这里不能有$符号，这里是重点

```
$pattern = '/\{pboot:if\(([^}^\$]+)\)\}([\s\S]*?)\{\/pboot:if\}/';

if (preg_match_all($pattern, $content, $matches)) {

}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291099.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291100.png)

### 构建payload

由于这里不能用美元符号”$“，前面第一个过滤说过，可用file函数绕过，如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291103.png)

通过上面file函数获取的美元符号，并且通过fputs进行写文件，当然需要绝对路径才能读取美元符，这里就比较简单了，直接让cms报错就好了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-16792911031.png)

### 调用链

```
ParserController.php:84, app\home\controller\ParserController->parserAfter()

TagController.php:47, app\home\controller\TagController->index()

IndexController.php:50, app\home\controller\IndexController->_empty()

2:2, core\basic\Kernel::axqjlxzuuxaapu328937ae1368b88e8bf79cb6b342866a()

2:2, core\basic\Kernel::run()

start.php:17, require()

index.php:23, {main}()
```

访问首页就会进入到apps/home/controller/IndexController.php的`_empty()`方法，需要get的参数带有tag就可进入该判断

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291107.png)

跟进到apps/home/controller/TagController.php的`inde()`方法，跟进第47行并跟进到apps/home/controller/ParserController.php`parserAfter()`方法，最后就会到84行的漏洞方法中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291111.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197859-1679291113.png)

### 目前新版本未发现有该处函数

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197859.html**](https://www.secpulse.com/archives/197859.html)

Tags: [$符号](https://www.secpulse.com/archives/tag/%E7%AC%A6%E5%8F%B7)、[cms逻辑漏洞](https://www.secpulse.com/archives/tag/cms%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E)、[php](https://www.secpulse.com/archives/tag/...