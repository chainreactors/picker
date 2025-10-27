---
title: 实战打靶之trick
url: https://www.freebuf.com/articles/web/349401.html
source: FreeBuf网络安全行业门户
date: 2022-11-11
fetch_date: 2025-10-03T22:23:42.954462
---

# 实战打靶之trick

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

实战打靶之trick

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

实战打靶之trick

2022-11-10 13:48:44

所属地 北京

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 信息收集

### 端口扫描

首先使用nmap对端口进行探测。找到了SSH (22) 和 HTTP (80)。2个端口。

![1668058679_636c8e37d1127860c747d.png!small?1668058681290](https://image.3001.net/images/20221110/1668058679_636c8e37d1127860c747d.png!small?1668058681290)

接着使用nmap对SMTP 协议去爆破一些用户名。

![1668058685_636c8e3dd4147a9e446a5.png!small?1668058687405](https://image.3001.net/images/20221110/1668058685_636c8e3dd4147a9e446a5.png!small?1668058687405)

### 使用脚本爆破SMTP协议

使用smtp-user-enum [脚本](https://github.com/cytopia/smtp-user-enum)来检查这些用户：

![1668058714_636c8e5ae574a263bd9bb.png!small?1668058716509](https://image.3001.net/images/20221110/1668058714_636c8e5ae574a263bd9bb.png!small?1668058716509)

使用telnet发现也不能成功。

![1668058721_636c8e619c36aef21bde0.png!small?1668058722963](https://image.3001.net/images/20221110/1668058721_636c8e619c36aef21bde0.png!small?1668058722963)

### DNS协议

使用 DNS来看域名的的解析情况。

![1668058729_636c8e6927839bdad2444.png!small?1668058730559](https://image.3001.net/images/20221110/1668058729_636c8e6927839bdad2444.png!small?1668058730559)

### 子域名枚举

接着使用wfuzz对子域名进行枚举。

![1668058735_636c8e6f7d1f94da0191f.png!small?1668058737173](https://image.3001.net/images/20221110/1668058735_636c8e6f7d1f94da0191f.png!small?1668058737173)

![1668058742_636c8e768731bea20fc0a.png!small?1668058744054](https://image.3001.net/images/20221110/1668058742_636c8e768731bea20fc0a.png!small?1668058744054)

访问主页查看页面有没有一些可用的东西。

![1668058752_636c8e80374b6661a2be4.png!small?1668058753571](https://image.3001.net/images/20221110/1668058752_636c8e80374b6661a2be4.png!small?1668058753571)

## 漏洞利用

### 万能密码登录

当我搜索[http://preprod-payroll.trick.htb](http://preprod-payroll.trick.htb/)时，它会自动将我重定向到登录页面。
![1668058804_636c8eb4e09017f512798.png!small?1668058806431](https://image.3001.net/images/20221110/1668058804_636c8eb4e09017f512798.png!small?1668058806431)

然后f12查看到，是一个员工管理系统，然后搜索nday漏洞。发现该系统存在sql注入漏洞。

![1668058775_636c8e974cee0e5208b1f.png!small](https://image.3001.net/images/20221110/1668058775_636c8e974cee0e5208b1f.png!small)

**漏洞详情链接：**

https://www.sourcecodester.com/php/14475/payroll-management-system-using-phpmysql-source-code.html

![1668058852_636c8ee415085e3144583.png!small?1668058853652](https://image.3001.net/images/20221110/1668058852_636c8ee415085e3144583.png!small?1668058853652)

使用' or 1=1--，对该网站可以通过万能密码登录。

![1668058858_636c8eea8c6b99776ff19.png!small?1668058859841](https://image.3001.net/images/20221110/1668058858_636c8eea8c6b99776ff19.png!small?1668058859841)

### sql注入漏洞

### 手动测试

登录框处存在一个时间盲注。

进行手动测试，输入1=1 和1=2进行对比，发现返回的结果1个是1，1个是3。

![1668058872_636c8ef8cea5dc4e75f27.png!small?1668058874237](https://image.3001.net/images/20221110/1668058872_636c8ef8cea5dc4e75f27.png!small?1668058874237)

### ![1668058881_636c8f0128a384aab29c0.png!small?1668058882539](https://image.3001.net/images/20221110/1668058881_636c8f0128a384aab29c0.png!small?1668058882539)

### sqlmap测试

接着使用sqlmap进行从测试。

先判断注入点：sqlmap -r x.txt --dbms --batch

![1668058890_636c8f0a1440d9e58974f.png!small?1668058891586](https://image.3001.net/images/20221110/1668058890_636c8f0a1440d9e58974f.png!small?1668058891586)

然后找到注入点之后，使用--current-user枚举当前数据库的用户

![1668058897_636c8f11c056f42aa6c4a.png!small?1668058899242](https://image.3001.net/images/20221110/1668058897_636c8f11c056f42aa6c4a.png!small?1668058899242)

接着去枚举数据库里面的表。

![1668058905_636c8f193d28335b685aa.png!small?1668058906765](https://image.3001.net/images/20221110/1668058905_636c8f193d28335b685aa.png!small?1668058906765)

![1668058913_636c8f21ee3813acc9713.png!small?1668058915372](https://image.3001.net/images/20221110/1668058913_636c8f21ee3813acc9713.png!small?1668058915372)

接着去枚举表里面的用户。

### ![1668058921_636c8f295b78e79da84c8.png!small?1668058922873](https://image.3001.net/images/20221110/1668058921_636c8f295b78e79da84c8.png!small?1668058922873)

### 使用sqlmap读取文件

可以配置 SQL，以便我可以通过注入读取文件。sqlmap允许使用--file-read参数。有用：

![1668058928_636c8f3084dd09bb90400.png!small?1668058930276](https://image.3001.net/images/20221110/1668058928_636c8f3084dd09bb90400.png!small?1668058930276)

接着使用wfuzz枚举子域名。成功枚举出新的子域名。

### ![1668058935_636c8f37e597b9d46e93e.png!small?1668058937360](https://image.3001.net/images/20221110/1668058935_636c8f37e597b9d46e93e.png!small?1668058937360)

### 文件包含漏洞

该网站在使用前面的万能密码登录之后，存在文件包含漏洞。接着尝试使用 PHP 过滤器对 URL 进行本地文件包含 (LFI)。

<http://preprod-payroll.trick.htb/index.php?page=php://filter/convert.base64-encode/resource=index>

先去读doductions文件，然后使用base64解密。

![1668058942_636c8f3edc1be863fb550.png!small?1668058944726](https://image.3001.net/images/20221110/1668058942_636c8f3edc1be863fb550.png!small?1668058944726)

接着去读index文件，然后解密之后发现新的php。

![1668058957_636c8f4d7eab60d9e02ad.png!small?1668058959216](https://image.3001.net/images/20221110/1668058957_636c8f4d7eab60d9e02ad.png!small?1668058959216)

接着继续去读login文件。继续解密。

![1668058965_636c8f556d7f098862817.png!small?1668058967143](https://image.3001.net/images/20221110/1668058965_636c8f556d7f098862817.png!small?1668058967143)

最后发现了db\_connect.php,读出了数据库的用户名和密码。

![1668058972_636c8f5c48bda6ae43956.png!small?1668058973730](https://image.3001.net/images/20221110/1668058972_636c8f5c48bda6ae43956.png!small?1668058973730)

![1668058980_636c8f64ca399ba992412.png!small?1668058982175](https://image.3001.net/images/20221110/1668058980_636c8f64ca399ba992412.png!small?1668058982175)

接着就可以使用ssh进行登录。

![1668058988_636c8f6c1dda44cfc4b47.png!small?1668058989524](https://image.3001.net/images/20221110/1668058988_636c8f6c1dda44cfc4b47.png!small?1668058989524)

### 目录遍历漏洞

### 源码分析

目录遍历

尝试在 web 目录之外加载一个文件（/etc/passwd这是一个通用文件，因为它是世界可读的并且总是在同一个地方）使用绝对路径（http://preprod-marketing.trick.htb/index.php?page=/etc/passwd）和相对路径（ ）都会失败http://preprod-marketing.trick.htb/index.php?page=../../../../../../../../../etc/passwd。

阅读 index.php 源码

只需包含index.php类似http://preprod-marketing.trick.htb/index.php?page=index.php, as 的index.php内容将再次执行，而不是返回源代码。尝试获取源代码的一种方法是使用 PHP 过滤器。访问http://preprod-marketing.trick.htb/index.php?page=php://filter/convert.base64-encode/resource=index.php可以在包含之前进行base64编码index.php，然后只会出现base64文件。接着继续使用sqlmapap读文件--file-read=/var/www/market/index.php

![1668058997_636c8f75649fda3ac7c5d.png!small?1668058999048](https://image.3001.net/images/20221110/1668058997_636c8f75649fda3ac7c5d.png!small?1668058999048)

发现源码将../进行过滤。我们可以使用....//进行绕过。

```
<?php
$file = $_GET['page'];

if(!isset($file) || ($file=="index.php")) {
   include("/var/www/market/home.html");
}
else{
        include("/var/www/market/".str_replace("../","",$file));
}
```

![1668059006_636c8f7eb50805202dfe3.png!small?1668059007958](https://image.3001.net/images/20221110/1668059006_636c8f7eb50805202dfe3.png!small?1668059007958)

成功遍历到了/etc/passwd。

![1668059014_636c8f861ab7af75e74d6.png!small?1668059015542](https://image.3001.net/images/20221110/1668059014_636c8f861ab7af75e74d6.png!small?1668059015542)

接着去遍历id\_rsa。

![1668059021_636c8f8d0271bd30f2f61.png!small?1668059022548](https://image.3001.net/images/20221110/1668059021_636c8f8d0271bd30f2f61.png!small?1668059022548)

###...