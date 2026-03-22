---
title: Web鉴权机制总结(全网最全版)
url: https://mp.weixin.qq.com/s/0jaO8IFKqCeYk8Y5RtU6vw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:34.409451
---

# Web鉴权机制总结(全网最全版)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w583TgvLJRaEBoJwBt7bBULVy7CstU37DsVGtT4N8S936nprG1CLmFp0icibl55we4Q2mqzsY4ABY5CiaH6pSUWiaGu6IK1eEmVib6ej4seA3wDA/0?wx_fmt=jpeg)

# Web鉴权机制总结(全网最全版)

原创

平平无奇 n1
平平无奇 n1

N1&杨安全

![]()

在小说阅读器中沉浸阅读

## 前言

这几天倒是一直在忙一些创业和社交相关的事,公众号倒是搁置了,今天突然想静下心来输出一篇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRYguiacqCmeKJQUwjemedB1pILclDDlTAZIg4MjbcBQ9Z3eQPE6HasyYskEMx2PK0LxkvsCDrJCGqD7cOD1Sn874R0P7QaOI6lM/640?wx_fmt=png&from=appmsg)

思前想后,继续给大家补一补web安全的基础吧:**web鉴权机制总结**

今天只是带领大家去**梳理总结一下**,很多还需要你们去问AI或者自学一下,有不懂的可以私信问我(有时间都会回)

推荐练习的靶场

* Portswigger中的JWT-labs以及其他

地址:https://portswigger.net/web-security/all-labs

## 概述

`鉴权(Authorization) 与身份验证(Authentication)`共同构成防止未授权的第一道防线,所以也是学习**未授权漏洞的基础**

那什么是**鉴权**呢?

其实就是看某用户**是否有权访问某资源**比如你是普通用户,还是管理员用户,能看到的东西肯定有所不同了

那什么又是**口令验证**呢?

其实就是通过某一串口令来对用户进行**身份识别**

# 鉴权机制与常见漏洞

这里带大家熟悉和梳理一下

![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRabn5RH6icG4sRHocHpicla4rH4bsRanicvrqD1nF8icGF5iacpleaicJyGUhhr8Fuz0QujCHAzzvrWav78xFCoB0kOczchmjf9jLC2g/640?wx_fmt=png&from=appmsg)

## cookie+session

```
<?php
session_start(); // 激活 Session 机制，生成或读取 PHPSESSID
// 模拟登录逻辑
if($_GET["username"] === "admin" && $_GET["password"] === "secret_pass"){
    // 坑点：直接把敏感信息存入 Cookie 是极度危险的
    setcookie("is_admin", "true", time()+3600);
    $_SESSION["user_id"] = 1;
    $_SESSION["role"] = "admin";
}

// 鉴权逻辑
if(isset($_SESSION["role"]) && $_SESSION["role"] === "admin"){
    echo"Welcome, Admin. [SessionID: ".session_id()."]";
} else {
    header("HTTP/1.1 403 Forbidden");
    echo"Access Denied.";
}
?>
```

用户登录后，服务器生成一个 `Session ID`，存储在服务端（如内存、Redis 或文件），并且将`Session ID`放入 `Cookie`返回给浏览器。后续用户请求通过 `Cookie` 自动携带，服务端通过 `Session ID`识别用户身份。

除了基础的 `Session+Cookie`，实战中更多遇到的是**无状态或签名类鉴权**：

## Http Basic / Digest Auth：

* Basic: Authorization: Basic [Base64]。Base64 是编码非加密，抓包即死。
* Digest： 引入了随机数（Nonce）和哈希，防止重放攻击，比 Basic 安全但部署复杂。

## 随机Token(一次性,短生命周期)

常用于 **CSRF 防护或单次接口调用**。关键看其**熵值（是否可预测）**和销毁机制。

## JWT (JSON Web Token)

又叫做**无状态Token**

那什么叫**无状态**呢?

就是服务端不存数据，全靠`Header.Payload.Signature`自校验

这也是出现漏洞最多最有名最常见的一种鉴权机制

## 挑战应答 (Challenge-Response) / AKSK / API Key

原理的话如图,自己看,看不懂就多看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRbp9zNYvA2Dpxrc2Sn8EfO5RaAP2BBwTsQoDyUiaxzCDZ200ETJwxflasLWkIwlAJVB0B2b2EkeHORhhbM6ygEsnbf57L6HTibYw/640?wx_fmt=png&from=appmsg)

你会发现,其实关键还是在于**SK的安全性**

这是**云原生**和 **API 接口**主流。客户端用 SK（Secret Key）对`请求内容（Method+Path+Timestamp+Body）`进行 `HmacSHA256` 签名。

**关键：** 只要 SK 不泄露，攻击者即使拦截了请求也无法伪造签名，因为 Timestamp 保证了时效性。

## 加解密身份票据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRZyFrXpxshKkwjrB9I33w6ukkFH1ELCqbicBiaWQVwck0T4OnHxFDXm7xMbQEWB2qR6ibqc09Hy7h2bVvy1DdL9Etvb2G2BicibD2to/640?wx_fmt=png&from=appmsg)

依旧取决于 **Key 的保管机制**

## 总结一下：核心在于Key

无论是 `Encrypted Token`（如 C# 的 MachineKey 加密）还是`签名机制`，其安全性完全取决于 **Key 的保管**。

**泄露途径**： GitHub 源码泄露、配置文件权限过大、硬编码在前端 JS 中、通过 LFI（本地文件包含）读取环境变量。

所以我们平时在做渗透测试的时候需要着重去看一看

那问题来了,这时候就有**臭弟弟**要说,**N1,N1我学了这么多鉴权机制,脑袋都快炸了,实战中我们又如何区分呢?**

其实你也不需要区分,只需要知道是什么在鉴权就足够了

![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRYlo1O7u0Srtwrl4S3KMtazxPqnszMibIa9ia3WOhe0A9iaXKDIHiaibnEqKicicodbdfGQHeTa9iafaQDgxgY7j8ibdibVdhOrbt5OY16sw/640?wx_fmt=png&from=appmsg)

## 如何识别鉴权机制

### 删除法

抓包后**逐个删除 Header** 中的 **Cookie、Authorization、X-Token**，观察哪个会导致 401/403,或者导致用户权限发生变化。

### 特征识别

* ey... 开头：典型的 JWT。
* Basic ...：Http 基础认证。
* Bearer ...：常见于 OAuth2。
* 长随机字符串：可能是 SessionID 或自定义 Token

## 常见漏洞

1. 弱 cookie
2. Session 劫持

CSRF,XSS打组合拳

配合 **XSS** 获取 **document.cookie**等。

3. Session 固定会话攻击(Fixation)

漏洞复现 用户登录后,固定的**SESSIONID** 成为了用户的身份凭证,导致可以访问到用户的界面

**验证**:观察登录前和登录后 SessionID 有没有变化

**防御**:登录之后应该强制刷新 SessionID

我们来举个**实际场景**

**场景**： 攻击者先获取一个合法的 `PHPSESSID=123`，诱导用户用该 ID 登录。

**验证**： 登录前抓包记下 `SessionID`，登录后再看，如果没变，则存在此风险。

防御： `session_regenerate_id(true)`; 登录成功必须强制刷新 I

4. Baisc 认证之 Tomcat 暴力破解
5. JWT 漏洞(高频)

**a. 不校验签名**

服务端直接没对签名做校验,不过很少了就是

**b. alg:none 攻击**空签名攻击

修改`Header`为 `{"alg":"none"}`，删掉签名部分，看后端是否直接放行（由于库漏洞，部分旧后端会认为签名已验证）。

**c. JWT 弱口令**

如果 JWT 使用 `HS256（对称加密）`，可以使用`hashcat` 对签名进行暴力破解。

\*\* d. JWK 劫持和 JKU 劫持\*\*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRYnAEvGQSBiahwYxXlO9egXvAhqsXWEPMC8QRAFaYLM3s9ibyDV5oDVbl0SicoCBVoJQZeQx0LcIicefToAzicpsDlXh2EKbEQRicDb8/640?wx_fmt=png&from=appmsg)

在 `Header` 中注入 `jku` 参数，指向攻击者控制的恶意公钥地址，让服务器用你的公钥验你的签。

**e. KID注入**

`kid`字段用于指定密钥。如果后端将其直接拼接进 SQL 或目录，会导致 SQL 注入或任意文件读取。

6. 服务端组件漏洞

Tomcat Basic 认证爆破： 针对 /manager/html 页面，利用字典进行 Authorization 头爆破。

### 总结一下

鉴权渗透的本质是**“身份越权”**。

**总结一下渗透路径**：识别机制 -> 寻找 Key 泄露/逻辑弱点 -> 尝试伪造/劫持 -> 实现纵向或横向越权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRZjIs45hNYbMqrejG2D2PpbiceFP3XXvxHKG77vz5JliaQ2KI78sWPzibApX8qMAsCOEU7W2QzJquj1kuPHloeoBdm11DANqgicoFc/640?wx_fmt=png&from=appmsg)

我是N1,一名拥有四年经验的渗透测试工程师,欢迎大家关注哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Gib89iarpRhQZz8nIkpOECzBxgFAUicKI8vOvI877OQG4FCagbXDRqdP1HOUK17ojq0Qs4ibkIG9VjewvSAzaevcmQ/0?wx_fmt=png)

N1&杨安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Gib89iarpRhQZz8nIkpOECzBxgFAUicKI8vOvI877OQG4FCagbXDRqdP1HOUK17ojq0Qs4ibkIG9VjewvSAzaevcmQ/0?wx_fmt=png)

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