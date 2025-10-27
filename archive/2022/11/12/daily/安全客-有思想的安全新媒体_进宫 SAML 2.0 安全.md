---
title: 进宫 SAML 2.0 安全
url: https://www.anquanke.com/post/id/283008
source: 安全客-有思想的安全新媒体
date: 2022-11-12
fetch_date: 2025-10-03T22:28:34.334464
---

# 进宫 SAML 2.0 安全

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 进宫 SAML 2.0 安全

阅读量**601124**

发布时间 : 2022-11-11 10:30:01

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

SAML始于2001年，最终的SAML 2.0版本发布于2005年，此后也没有发布大版本，SAML 2.0一直延续到了现在。SAML已经是老古董了，现在SSO里面使用更多的是OAuth。在某些漏洞平台看到过一些SAML漏洞报告，一些大型应用依然出现过它的身影，最近看到的一个议题《Hacking the Cloud With SAML》[[1]](https://drive.google.com/file/d/1p1tTTIjg3RoJecYSU3CetvNw6-ZZdMXn/view)也提到了，考考古学学也不亏，至少它的一些概念现在仍在延用。

## SAML 2.0

**SAML**: Security Assertion Markup Language，一种用于安全性断言标记的语言。

SAML的用途：

* 单点登录（SSO Single Sign-ON）
* 联合认证（Federated Identity）
* 在其他架构内使用SAML，例如WS-Security

后续的内容主要是SAML SSO的部分。

SAML协议中的三方：浏览器，身份鉴别服务器(IDP，Identity Provider)，服务提供者(SP，Service provider)，以及这三方相互的通讯次序，加密方法，传输数据格式。

可能大家在网络上看到的一些流程图会多一两个步骤或少一两个步骤，那只是开发人员在具体选择和实现SAML传输时存在的一些差异，对于我们了解整个SAML认证流程问题不大，知一反三就行。基本的认证流程如下：

![]()

图先大概浏览下，后续会在OpenSAML的案例中看到每个环节的细节。

## 通过OpenSAML请求包看SAML SSO

**OpenSAML**是SAML协议的一个开源实现，在github找了一个用OpenSAML实现的SSO [demo](https://github.com/OpenConext/Mujina)，使用的是HTTP-POST传输SAML，有几百个star。将项目跑起来，正常的登录一遍看下完整的通信包过程，9090端口是SP，8080端口是IDP

### 用户访问SP服务

request:

```
GET /user.html?force-authn=true HTTP/1.1
Host: 192.168.0.104:9090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.0.104:9090/
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,vi;q=0.7
Cookie: mujinaSpSessionId=2E15F753B56E4646FA4CACCE4DD2ED6D; mujinaIdpSessionId=6203026E878EFB44F90769F285FB05D9
Connection: close
```

response:

```
HTTP/1.1 200
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Type: text/html;charset=UTF-8
Content-Language: zh-CN
Date: Sat, 22 Oct 2022 10:29:57 GMT
Connection: close
Content-Length: 889

<!DOCTYPE html>
<html>
<head>
    <title>Mujina Service Provider</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="/main.css"/>
    <script src="/sp.js"></script>
</head>
<body>
<section class="login-container-wrapper">
    <section class="login-container">
        <section class="login">
            <h1>Mujina Service Provider</h1>
            <a id="user-link" class="button" href="/user.html?force-authn=false">Login</a>
            <section class="force-authn">
                <input type="checkbox" id="force-authn" name="force-authn"/>
                <label for="force-authn">Force Authn request?</label>
            </section>
        </section>
        <a class="powered-by" href="https://openconext.org/" target="_blank">Copyright Â© 2018 OpenConext</a>
    </section>
</section>
</body>
</html>
```

返回SP登录页，用户点击登录。

### SP返回重定向

request:

```
GET /user.html?force-authn=true HTTP/1.1
Host: 192.168.0.104:9090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.0.104:9090/
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,vi;q=0.7
Cookie: mujinaSpSessionId=2E15F753B56E4646FA4CACCE4DD2ED6D; mujinaIdpSessionId=6203026E878EFB44F90769F285FB05D9
Connection: close
```

response:

```
HTTP/1.1 200
Set-Cookie: mujinaSpSessionId=F6BCE4D93AA256056960B9459E27B374; Path=/; HttpOnly
Cache-control: no-cache, no-store
Pragma: no-cache
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Frame-Options: DENY
Content-Type: text/html;charset=UTF-8
Date: Sat, 22 Oct 2022 10:30:02 GMT
Connection: close
Content-Length: 4483

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
    </head>
    <body onload="document.forms[0].submit()">
        <noscript>
            <p>
                <strong>Note:</strong> Since your browser does not support JavaScript,
                you must press the Continue button once to proceed.
            </p>
        </noscript>

        <form action="http://192.168.0.104:8080/SingleSignOnService" method="post">
            <div>

<input type="hidden" name="SAMLRequest" value="PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c2FtbDJwOkF1dGhuUmVxdWVzdCB4bWxuczpzYW1sMnA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgQXNzZXJ0aW9uQ29uc3VtZXJTZXJ2aWNlVVJMPSJodHRwOi8vMTkyLjE2OC4wLjEwNDo5MDkwL3NhbWwvU1NPIiBEZXN0aW5hdGlvbj0iaHR0cDovLzE5Mi4xNjguMC4xMDQ6ODA4MC9TaW5nbGVTaWduT25TZXJ2aWNlIiBGb3JjZUF1dGhuPSJ0cnVlIiBJRD0iYWhnZzRhNDVkZWg5aTY3aDBmMmllZGdhMDc1NWciIElzUGFzc2l2ZT0iZmFsc2UiIElzc3VlSW5zdGFudD0iMjAyMi0xMC0yMlQxMDozMDowMi4xMTVaIiBQcm90b2NvbEJpbmRpbmc9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpiaW5kaW5nczpIVFRQLVBPU1QiIFZlcnNpb249IjIuMCI+PHNhbWwyOklzc3VlciB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI+aHR0cDovL21vY2stc3A8L3NhbWwyOklzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG5zOmRzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjIj48ZHM6U2lnbmVkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyIvPjxkczpTaWduYXR1cmVNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNyc2Etc2hhMjU2Ii8+PGRzOlJlZmVyZW5jZSBVUkk9IiNhaGdnNGE0NWRlaDlpNjdoMGYyaWVkZ2EwNzU1ZyI+PGRzOlRyYW5zZm9ybXM+PGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNlbnZlbG9wZWQtc2lnbmF0dXJlIi8+PGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyIvPjwvZHM6VHJhbnNmb3Jtcz48ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2Ii8+PGRzOkRpZ2VzdFZhbHVlPlc0dGxMc3RsVWQ3Rk9zU25JNFBtTVMwMFhybTFQQmExRDExNU03RkRxbkk9PC9kczpEaWdlc3RWYWx1ZT48L2RzOlJlZmVyZW5jZT48L2RzOlNpZ25lZEluZm8+PGRzOlNpZ25hdHVyZVZhbHVlPm9lOGQzQTZMVU1Wd05FUmd4UHIwdEl1Uk9vKzBSdzV6MTJuOTlQSnhKS05XYXZlVEdiZkFBMVBNRTQ5NFQyalZnNUhtTmVLUHJDQk1Ubk93RGZpcm16VFNDc3hUT3F3aFpJMXNOcW5rSXNMSnljenVGUjUyWUVMbVpMbms5NzQzeWVRRDBkSndLR1lRR0JCcklEOEFKdWhvQUtIWU83NFkvYWJlZDBWYTZrdmV2ZjR2a3RxY1A0R1lhc2M2MW44ajhTc2VHZ0M0a1RYdE9wdWg2UFpnLzdlZlJlNndpT3JVNDZodjdRRVpQbjZKc09mbDZxSjd0TWVjZUV6b05zTnVvcjRidjZVV05ZemlPN3U3SmkzTkdOWnQ0RXdtekNTR1dxcWdoTE5XLzVZd2FwWnpxc0ppaTBYMHEvZnZSMXFkNVQwSmpheHZpZUtZS2tmTGV0SHhiZz09PC9kczpTaWduYXR1cmVWYWx1ZT48ZHM6S2V5SW5mbz48ZHM6WDUwOURhdGE+PGRzOlg1MDlDZXJ0aWZpY2F0ZT5NSUlERXpDQ0FmdWdBd0lCQWdJSkFLb0svaGVCamNPWU1BMEdDU3FHU0liM0RRRUJCUVVBTUNBeEhqQWNCZ05WQkFvTUZVOXlaMkZ1DQphWHBoZEdsdmJpd2dRMDQ5VDBsRVF6QWVGdzB4TlRFeE1URXhNREV5TVRWYUZ3MHlOVEV4TVRBeE1ERXlNVFZhTUNBeEhqQWNCZ05WDQpCQW9NRlU5eVoyRnVhWHBoZEdsdmJpd2dRMDQ5VDBsRVF6Q0NBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQQURDQ0FRb0NnZ0VCDQpBTkJHd0ovcXBUUU5pU2dVZ2xTRTJVekVrVW93K3dTOHI2N2V0eG9FaGx6SlpmZ0svazVUZkcxd0lDRHFhcEhBeEVWZ1VNMTBhQkhSDQpjdE5vY0E1d21sSHR4ZGlkaHpSWnJvcUh3cEt5MkJtc0tYNVoyb0syNVJMcHN5dXNCMUtyb2VtZ0EvQ2pVbkk2cklMMXh4Rm4zS3lPDQpGaDFaQkxVUXRLTlFlTVM3SEZHZ1NEQXArc1h1VEZ1anoxMkxGRHVnWDBUMEtCNWExKzBsOHkwUEVhMHlHYTFvaTZzZU9OeDg0OVpIDQp4TTBQUnZVdW5Xa3VUTStmb1owalpwRmFwWGUwMnlXTXFoYy8yaVlNaWVFLzNHdk9ndUpjaEp0NlIrY3V0OFZCYjZ1YktVSUdLN3BtDQpvcS9UQjZEVlhwdnNIcXNESlhlY2h4Y2ljdTRwZEtWREhTZWM4NTBDQXdFQUFhTlFNRTR3SFFZRFZSME9CQllFRks3UnFqb29kU1lWDQpYR1RWRWRMZjNrSmZsUC9zTUI4R0ExVWRJd1FZTUJhQUZLN1Jxam9vZFNZVlhHVFZFZExmM2tKZmxQL3NNQXdHQTFVZEV3UUZNQU1CDQpBZjh3RFFZSktvWklodmNOQVFFRkJRQURnZ0VCQUROWmt4bEZYaDRGNDVtdUNiblFkK1dtYVhsR3ZiOXRrVXlBSXhWTDhBSXU4SjE4DQpGNDIwdnBuR3BvVUFFK0h5M2V2Qm1wMm5rckZBZ21yMDU1ZkFqcEhlWkZnRFpCQVBDd1lkM1ROTURlU3lNdGEzS2Erb1M3R1JGRGVQDQprTUVtK2tINC9y...