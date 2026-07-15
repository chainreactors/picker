---
title: 聊一聊CORS跨域漏洞的危害
url: https://mp.weixin.qq.com/s/s6hhOyoq3xKgy22nJLMAsQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:45:48.298285
---

# 聊一聊CORS跨域漏洞的危害

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bcFEmmDxVAjo6RicJM4j9JgQY12FUlnrLZt0icaXia1jysWLEP0ZJmhEj4snh9ZD4jM4LAymtMAcacy0Hndzib2N1ps1CJ04mibb3sIJEkQJxS0w/0?wx_fmt=jpeg)

# 聊一聊CORS跨域漏洞的危害

原创

AugustTheodor
AugustTheodor

重生之成为赛博女保安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

从危害、利用、防护三点来说。

## 定义

要讲CORS首先得讲浏览器的跨域策略。

当两个网站中的端口|协议|域名三者中有任意一个不同时，我们认为这两个网站不在一个域内（跨域）。浏览器的同源策略禁止域A网站中的JS读取向域B发送请求的响应（能发送请求但不可读取响应）。

如果此时域B需要A能够获取其响应，就会在响应中使用特定的响应头标注。这些响应为：

```
Access-Control-Allow-Origin: https://abc# 允许哪个源跨域访问；* 代表允许所有源Access-Control-Allow-Credentials: true# 是否允许携带Cookie；在较新的浏览器中（可认为除了IE之外的基本都算）这个头和上文中的头不能同时为true和*Access-Control-Allow-Methods: GET,POST# 允许的请求头Access-Control-Allow-Headers: Content-Type# 这个配置的保存时间Access-Control-Max-Age: 86400
```

## 危害

假设存在原网站A，攻击者的网站B。当CORS因各种原因失效时，用户访问钓鱼网站B，B从前端将请求原样转发给A，当A的响应返回时，其可以被B网站的JS读取，造成数据窃取。

当A的请求为简单请求或被CORS允许的请求时，B可以向A发送请求，但读取不到响应。

### 简单请求

这个不用记太详细，稍微记一下。

请求为GET POST HEAD;

Content-Type为`application/x-www-form-urlencoded` `multipart/form-data` `text/plain`；

没有其它自定义头。

### 易错点

**CORS失效窃取的是已登录用户的响应，登录页面钓鱼跟CORS失效没关系。**

**同时，跟与CORS类似的但“发送请求就达到目的”的漏洞一般叫做CSRF。**

## 利用

利用分为两种场景。

这些场景通常都需要Access-Control-Allow-Credentials: true，且凭证在Cookie里（如果窃取的是登录态数据）。

### CORS失效

我们需要知道，CORS（ACAO）是一个响应头。它可能通过各种方式被设置，很多情况下，ACAO会根据前端的ORIGIN来设置（**为什么，因为网站域名跟网站没啥关系，很多时候程序员为了方便不会写死**）。

在后端校验CORS存在缺陷的情况下，我们可以用各种方式绕过。假设网站abc.com后端校验时使用不严谨的过滤逻辑（比如endswith or include）：

```
Origin: http://att-abc.comOrigin: http://abc.com.att.com
```

构造一个通过逻辑的域名以获得一个允许的ACAO即可。

### null允许

一些情况下后端允许origin为null（也就是当前端origin为null时后端会返回一个null的ACAO）：

```
Access-Control-Allow-Origin: nullAccess-Control-Allow-Credentials: true
```

而我们可以使用如iframe造出一个origin为null的请求：

```
<iframe sandbox="allow-scripts">
```

### ACAO反射漏洞

在一些情境下，**后端会直接反射前端的Origin为ACAO**。此时等同于Access-Control-Allow-Origin: \*。

这个漏洞应该是最常问的，探测方式就是直接BP改Origin看看服务端会不会跟随。

### 其它情况

存在一些间接利用的情况，这里简单描述一下。

1.CORS宽松+旁站XSS：cors为主域名通配符，旁站存在XSS，可以窃取目标站的响应。2.**钓鱼站盲打内网：用户在内网点击钓鱼网站，如果内网网站CORS宽松且打中路由，就可以将返回数据带回。**

## 防护

简单说说，浏览器机制太多。

一个是写ACAO的时候最好写死或者使用不可利用的校验（且不能写null），同时控制ACAC为true的情况，非必要不授予；

一个是设置Cookie为SameSite=Lax/Strict防止跨站使用（在不影响业务的情况下；当然如果不怕XSS也可以不把凭证存在Cookie）。

最应该做的是严格校验ACAO（治本）。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LN229gZh2CBArnntUrW3YlvB7yBzXlKkAx2TUg8DvhFtvVGyO4mUVHAM9kISeDaUxm13uCDEHPAfkfKCv4cx7Q/0?wx_fmt=png)

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