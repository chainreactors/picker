---
title: 2026最新sqlmap使用手册，超详细
url: https://mp.weixin.qq.com/s/tSMxwBNCHv6UW-zDRY_jHg
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:47.156273
---

# 2026最新sqlmap使用手册，超详细

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNHW55V6LnkkGOSEXKqrrIxaawFtS3WiaGj8kicUbnAXystXuIYOUMUN0aWG6voXvre5XNeLz0Nhu6ib5mnMc2ysj2xFIBqf9m1ibs/0?wx_fmt=jpeg)

# 2026最新sqlmap使用手册，超详细

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器中沉浸阅读

## 一、前言

### 1.1 什么是SQLMap？

**SQLMap**，它其实是一个能让 **SQL 注入**验证流程自动化的开源项目，它的核心用途，是在你拿到授权后，去确认系统里的 **SQL 注入漏洞**是否真实存在，同时评估这漏洞可能掀起多大风浪，顺便还能检验下**防火墙（WAF）** 之类的防护措施到底管不管用。

### 1.2 合法使用原则

然而，使用这件工具的规矩必须讲清楚，

依余之见，最根本的一条就是**授权**，只有在测试自己有所有权、或是拿到了明确书面许可的系统时，才能使用它，对未获授权的系统发起测试，这无疑是踩了红线，是绝对不被法律允许的情形。

### 1.3 工具价值体现

于**安全工程师**而言，它能极大程度地将漏洞验证工作自动化，从而腾出精力去全面衡量安全风险，也为后续的修复方案提供了坚实的技术支撑，

而对于**开发者**，这工具则像一个活教材，它直观地揭示了 **SQL 注入**的整条攻击链路，让他们能更深刻地理解如何构筑有效的防御，从根本上拔高了编码人员的安全意识。

想要学习更多的渗透测试知识？欢迎关注我们官方的B站，每天更新在线的学习视频，点击右边文字====》官方B站账号视频学习

> ❝
>
> **💖 温馨提示：**本文一切操作基于本地环境复现，请不要利用文章中的任何技术对未授权的靶标进行渗透测试，这样属于违法行为，如有使用，还请自行承担所造成后果，与智榜样网络安全无关。

## 二、SQLmap 工具使用

聊聊 **SQLmap** 这东西，主要是看它环境咋样，能不能用，

**SQLmap** 这个工具，此乃一个开源项目，它把发现漏洞、注入利用、直到最后把数据掏出来这一整套活儿，都自动化处理了，在 **Kali Linux** 的环境里头，存在它本身就是个预置组件的情形，一般就躺在 `/usr/share/sqlmap` 这个路径下，

想知道它能不能跑起来也简单，

你只管在终端里敲个 `sqlmap`，要是版本信息跟用法说明都弹出来了，那就说明没问题，

我们拿来做演示的靶场，是一套云上跑的 **SQL-labs**，它的源码你上 **GitHub** 找或者直接问作者要都行，

倘若想找点别的目标练练手，用必应搜一搜那些可能存在的注入点，比如下面这种格式，

![image-20251119192343031](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauMyjjZgCw9VcXAT8QicJkib96QWiaDE2993FVVj4xiayX56EA7xA7NmJAZ8SUOBfALhLXwzdSExKricP1v2Gl0P3O6n7zumAX3uokZg/640?wx_fmt=other&from=appmsg)

image-20251119192343031

我们拿来做演示的靶场，是一套在云上跑的 SQL-labs，它的源码你上 GitHub 找或者直接问作者要都行，

源码地址：https://github.com/Audi-1/sqli-labs

倘若想找点别的目标练练手，可以用必应的黑客语法搜一搜那些可能存在的注入点，比如下面这种格式，

```
inurl:news.asp?id=site:edu.cn
inurl:news.php?id=site:edu.cn
inurl:news.aspx?id=site:edu.cn
```

![image-20251119192438409](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauP41nygIMOnlXWcDV65aO3IUbj2gB6au1YoeKVzmI0el79ZNx5OYjNhKQuDoT3ibReZddCLYww5SXCC4VlNcvyP6micibLjRBiaOvw/640?wx_fmt=other&from=appmsg)

image-20251119192438409

> ❝
>
> **💖 温馨提示：**所有渗透测试必须在**合法授权**的前提下进行，未经允许的渗透测试行为涉嫌违法。

### 2.1 目标配置的五种核心玩法

启动任何注入测试之前，首先要做的就是通过参数把目标给框定下来，这可以说是 **SQLmap** 运作的逻辑起点。

#### 2.1.1 单 URL （-u 参数）

要对付一个带参数的特定 URL，`-u` 参数就是你的首选，记得把整个 URL 用引号包起来，免得那些特殊字符在解析时捣乱，命令格式大致如此：

```
sqlmap -u 'http://192.168.31.180/Less-1/?id=1'
```

![image-20251119194951764](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauOiaoezibGWo1za59QJgyskV9NESpVMUxS48SJ9fttZTicBs5cpOCAUO2ibORYb6JnoRItnAOp2DdYTfqwDL6HSHA2ekVvggSlSJxc/640?wx_fmt=other&from=appmsg)

image-20251119194951764

**关键说明**：

重点在于，这个 URL 里头必须得有个能下手的地方，比如 `id=1` 这种，光秃秃的页面 **sqlmap** 是没法测的，

![image-20251119194909220](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPgI8VTTpEzMibXwSq5PZ3lcSEGSSeBfic8CDiacUFQSsLDSheNsOUIibQQia81HOx42K6NnC1gVbjAcztKEpmJQDGtYfq8vPq4n5YM/640?wx_fmt=other&from=appmsg)

image-20251119194909220

要是中途跳出询问你是否继续，输入 “y” 就能让它继续跑。

![image-20251119194751426](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMlAOkcJHegkZoSCXQZI5VXjBBOloDCRoDfJXKvRCSVbcQSFAlxCpNAPoVMt0Qct9qfxKf2f1OENuchIicOibYtmzTPiaKtYDaWicQ/640?wx_fmt=other&from=appmsg)

image-20251119194751426

检测完成后，工具会输出支持的注入类型（如联合查询、盲注）及数据库版本信息。

![image-20251119194631072](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauNiahQZ2WicJ6N4hfjr5lWkrRicrnmNRMpq7xw766LvaAf2P1JaCtN8WGKsYVxP8fozhPzfib6uvSdA1BHeAZXS8Q3obiagTVS6uEP8/640?wx_fmt=other&from=appmsg)

image-20251119194631072

#### 2.1.2 批量 URL 检测（-m 参数）

如果你手上有一串目标列表，`-m` 参数就能派上用场，让 **sqlmap** 批量处理，

操作也直接，把所有网址一行一个塞进一个文本文件里，譬如 `urls.txt`

![image-20251119195711365](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMTuRqnXjWa51icb4j3cvHA6OYHVk1iaa22eibYVDo2TvTQMZW0UX2CRCdqqMOiaapPZVEjEWdrSd9EP3O1Jdj4dGxP0Us73xIjeBU/640?wx_fmt=other&from=appmsg)

image-20251119195711365

然后用命令去调用它，

```
sqlmap -m urls.txt
```

![image-20251119200450476](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauPyTz8uyTOdJrBDHVicdw4TrDuyvLRYQicQwXmAxKseicPDfy89pD1EBcaORt6jFbbUialBOFricHQpzFLv5pf45PdZeWIpicVTGKumw/640?wx_fmt=other&from=appmsg)

image-20251119200450476

> ❝
>
> **🌞我的经验：**想省事儿的话，可以追加一个 `--batch` 参数，这样它就自己确认所有提示，不用你一直守着了。

#### 2.1.3 数据库 / 表 / 字段精准定位

依余之见，为了更快地拿到想要的东西，直接指定数据库、表乃至字段是最高效的打法，

这需要 `-D`, `-T`, 和 `-C` 这几个参数协同运作，层层递进地锁定范围。

**典型应用命令**：

```
sqlmap -u 'http://xx/?id=1' -D 'security' -T 'users' -C 'username' --dump
```

![image-20251119200741631](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMt4ENk28gYwTibBCo100WOLybfJyeoyxyltVIebZYaicWBODHAHVRfTmN0pPTBRdDibkNRCms8Ir25Nicl0y2VJy03GnX37BfViboc/640?wx_fmt=other&from=appmsg)

image-20251119200741631

> ❝
>
> **⚠️避坑指南：**但这里有个规矩，你不能跳着用，比如只给了 `-D` 库名却不指定 `-T` 表名，程序就会报错。

#### 2.1.4 POST 请求注入（-r 参数）

处理那些通过 **POST** 方法提交的数据，情况就有所不同了，你得先用 **Burp Suite** 这类工具把整个 **HTTP 请求**，包括请求头和请求体里的具体参数，原封不动地抓下来存成一个文件，

![image-20251119201340637](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauOnPFeL89SI3QEXialK7MbPUb6Apeia35Pmq4lKlBbGm7krgvacYRbxrBrcsnU4jbRFw9tYkFhboNMVXQySz2ARjZ4f4RSHdZYVg/640?wx_fmt=other&from=appmsg)

image-20251119201340637

保存为文本文件（如 `bp.txt`，或者 `post.txt`），

![image-20251119201928280](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPGfRwU9cAWsI4hZPlJNXLgfc3UwGbJbwRT7TVw4DVrwoRrblZicAJBPmpf8poic1ym0AGFickiaHa694xJWz5uB2EPhvian5bCWsCU/640?wx_fmt=other&from=appmsg)

image-20251119201928280

然后把这个文件丢给 `-r` 参数去读取。

**操作命令**：

```
sqlmap -r bp.txt
```

![image-20251119201848411](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauNqfmwwRN9C9ul9Du1iaHqBWbwjs5e3iatV0V7hUIDcl5bqrBRFoLrTwEwianJGnPbhFKoOH3CAnraIDalEKSuPatb4MhjkAHLdkY/640?wx_fmt=other&from=appmsg)

image-20251119201848411

#### 2.1.5 Cookie 注入（--cookie 参数）

有时候，注入点并不在明面上，而是藏在 **Cookie** 里，

首先来到 **sqlilabs** 的第 20 关，随便输入一个账号密码，点击登录

![image-20251119203407171](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMziaTc2SFTB7W5KNXiaSkdO1mdPKUQeFaMxGRQRNeL8IGic8526zicNCv5HrrJEtNibZtNtlerHvX6VL9s5nuOPl53wKGeLPVB2No0/640?wx_fmt=other&from=appmsg)

image-20251119203407171

然后就能看到它报了个 cookie 是 `uname=admin and xxxxxx`

![image-20251119203423371](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMrWEkmUia7oJIOBCc9EPNe82jOPXEnUiayvMIWaOfHHHmicTft5wZ0WOxWARMeBjykibMJ5lRzWErs8Wcic5iahfKSOCQD2iaK5oqyFY/640?wx_fmt=other&from=appmsg)

image-20251119203423371

获取数据包，可以看到包含了一个参数 `uname`，那么就针对这个 cookie 进行注入，将全部的 cookie 值给复制

![image-20251119203628711](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauO294OJAhLVbaDpQNS9o0nJsaC2rw25QIoFU6A8mlVmeOvTVu4W5AdT0zlbM3OiaQV7wpCycibkknKbpsUe16sEaIRBPeAugde5A/640?wx_fmt=other&from=appmsg)

image-20251119203628711

然后咱贴到下面这个 `cookie` 参数中并在 `uname` 参数后面的值添加一个 `*` 号，代表着将在这里进行注入，不然 **sqlmap** 找不到注入点

**操作命令**：

```
sqlmap -u "http://xxxxx/Less-20/index.php" --cookie="uname=admin*; SITE_TOTAL_ID=0e207f952f25b4996467158140d6c9b6; vue_admin_template_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzYzNjM4NzQ3LCJlbWFpbCI6IiJ9.0_DJJ2GSNUpDNO7sQK_TtA6gJ5mGl2L3w1N1npVgq4g" --dbs --batch
```

![image-20251119213415317](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauP1ZhiaxMzRaJHAFmz5NWI3OjuqBHyXibnicmedqjpm5kyRLCcibcAuA7lXzfPPLkgMj4N5icAibw8z4fl7MnyVCZib9IaQHxgVwvwVqs/640?wx_fmt=other&from=appmsg)

image-20251119213415317

**适用场景：** 参数无注入点，但 **Cookie** 中存在用户 ID、会话标识等可测试字段。

### 2.2 全流程脱库操作

脱裤是什么意思呢？脱裤主要是用来获取数据中的所有数据，包括且不限于每一张表，每一个数据库，用户信息，操作系统信息等等

#### 2.2.1 全量获取（-a 参数）

`-a`（all）参数可自动获取所有可提取信息，包括数据库结构、用户权限、系统信息等，但耗时较长

```
sqlmap -u 'http://xx/?id=1' -a
```

适合此处的注入类型，图中包含了布尔注入、报错注入、联合注入等等

![image-20251119213713420](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauNDnLvCHTbkIPqW5aI8rhCYEo7JuYYPQs8VKsnHWLNr3NdXtFH2bqgMk1Sp0LCYIZHhYQzuN5Ria9dSG1PicGRGMUhJZzHbzQ1uE/640?wx_fmt=other&from=appmsg)

image-20251119213713420

爆出来的数据表数据信息

![image-20251119214035006](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPAH1HltmP1YzLsjibS6SIcUtuDmpWJciahfLtjCoLYYu8ibKP0QoRsTo2YsU1d0y0g7IUmeMr7icOQ80mzofb2L0JkDwpuw1xgXkc/640?wx_fmt=other&from=appmsg)

image-20251119214035006

各种配置信息

![image-20251119214355115](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauOrdhmOZ4PnOgKUVZDc2qN1T1ibe303WTOh4IYt0iaEqETuoC18Q1aEZkFsjB71FAjdHrRaas2sR3nGCAZT7HqYOxiaAtXzv1Fibow/640?wx_fmt=other&from=appmsg)

image-20251119214355115

有了这些东西，能够获取更多的信息，帮助我们进一步渗透测试，拿取到系统的最高权限

#### 2.2.2 数据库基础信息探测

获取数据库版本命令：

```
sqlmap -u 'http://xx/?id=1' -b
`...