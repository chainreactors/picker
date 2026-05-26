---
title: JWT渗透姿势
url: https://mp.weixin.qq.com/s/UxrCRRFcwLOUE3sXsgidtg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:03:17.825215
---

# JWT渗透姿势

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaGzkko2lDJ9iaxYANpFzd1PHrknIETXFMZibcEV53iadfh4Gfsib16F9DQw/0?wx_fmt=jpeg)

# JWT渗透姿势

StudySec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于EhiSec
，作者EhiSec

![](http://wx.qlogo.cn/mmhead/OM4v0FU2h0tMPiabTfKF3nmU0AmzJCOu3U7LZEE7zA3anMTq8f2lVBn4BSwKiaI2ibmxweCCmsEAKw/0)

**EhiSec**
.

分享安全学习文章

## 前言

最近打渗透遇到很多JWT相关的站点，然后在网上搜了一下，发现相关的文章也比较少，这里总结一下我自己常用的一些思路，同时附有靶场复现过程

JWT（JSON Web Token）是一种无状态认证机制，通过将用户身份和权限信息存储在令牌中，实现安全地在网络应用间传递信息。它具有跨域支持、扩展性和灵活性、安全性以及可扩展的验证方式等特点，成为现代应用开发中重要的认证和授权解决方案。

## 什么是jwt？

JWT 全称 JSON Web Token，是一种标准化格式，用于在系统之间发送加密签名的 JSON 数据。

原始的 Token 只是一个 uuid，没有任何意义。

JWT的结构由三部分组成，分别是Header、Payload和Signature，下面是每一部分的详细介绍和示例：

### Header 部分

在 JWT 中 Header 部分存储的是 Token 类型 和加密算法，通常使用 JSON 对象表示并使用 Base64 编码，其中包含两个字段：alg 和 typ

* alg（algorithm）：指定了使用的加密算法，常见的有HMAC、RSA和ECDSA等算法
* typ（type）：指定了JWT的类型，通常为JWT

下面是一个示例Header：

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### Payload 部分

Payload包含了JWT的主要信息，通常使用JSON对象表示并使用Base64编码，Payload中包含三个类型的字段：注册声明、公共声明和私有声明

* 公共声明：是自定义的字段，用于传递非敏感信息，例如：用户ID、角色等
* 私有声明：是自定义的字段，用于传递敏感信息，例如密码、信用卡号等
* 注册声明：预定义的标准字段，包含了一些JWT的元数据信息，例如：发行者、过期时间等

下面是一个示例 Payload：

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

其中sub表示主题，name表示名称，iat表示JWT的签发时间

### Signature 部分

Signature是使用指定算法对Header和Payload进行签名生成的，用于验证JWT的完整性和真实性

* Signature的生成方式通常是将Header和Payload连接起来然后使用指定算法对其进行签名，最终将签名结果与Header和Payload一起组成JWT
* Signature的生成和验证需要使用相同的密钥

下面是一个示例Signature

```
HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload),secret)
```

其中HMACSHA256是使用HMAC SHA256算法进行签名，header和payload是经过Base64编码的Header和Payload，secret是用于签名和验证的密钥，最终将Header、Payload和Signature连接起来用句点(.)分隔就形成了一个完整的JWT

### 完整的JWT

第一部分是Header，第二部分是Payload，第三部分是Signature，它们之间由三个 `.` 分隔，注意JWT 中的每一部分都是经过Base64编码的，但并不是加密的，因此JWT中的信息是可以被解密的，下面是一个示例JWT

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

## 解密平台

下面是一个JWT在线构造和解构的平台：

https://jwt.io/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaCkBfEk7BGadfOZdicGOJ4499JyHG8SaKeAKztL1Ule9CdDH5NTBC9kg/640?wx_fmt=png&from=appmsg)

当然也可以直接上工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqia36GrJMTyxmAKkx0HBO2FR5Zk7zoNic5w7MKeBxPRpOMaux9Qfcens7g/640?wx_fmt=png&from=appmsg)

## 工作原理

JWT的工作流程如下：

* 用户在客户端登录并将登录信息发送给服务器
* 服务器使用私钥对用户信息进行加密生成JWT并将其发送给客户端
* 客户端将**JWT存储在本地**，每次向服务器发送请求时携带JWT进行认证
* 服务器使用公钥对JWT进行解密和验证，根据JWT中的信息进行身份验证和授权
* 服务器处理请求并返回响应，客户端根据响应进行相应的操作

## JWT名词

1. JWS（Signed JWT）

   JWS是指已签名的JWT。它由JWT的Header、Payload和Signature组成，其中Signature是使用密钥对Header和Payload进行数字签名得到的。通过验证签名，可以确保JWT的完整性和真实性。
2. JWK（JSON Web Key）

   JWK是指用于JWT的密钥。它可以是对称加密密钥（例如密码），也可以是非对称加密密钥（例如公钥/私钥对）。JWK用于生成和验证JWT的签名，确保只有拥有正确密钥的一方能够对JWT进行操作。
3. JWE（Encrypted JWT）

   JWE是指经过加密的JWT。它是在JWS基础上进行了进一步的加密，将JWT的Payload部分加密后得到的结果。JWE可用于保护敏感信息，确保只有授权的接收方能够解密和读取JWT的内容。
4. JKU（JSON Web Key Set URL）

   JKU是 JWT Header 中的一个字段，该字段包含一个 URI，用于指定用于验证令牌密钥的服务器。当需要获取公钥或密钥集合时，可以使用JKU字段指定的URI来获取相关的JWK信息
5. X5U

   X5U 是 JWT Header 中的一个字段，它是一个URL，指向一组 X.509 公钥证书。类似于JKU，X5U字段用于指定可用于验证 JWT 的公钥证书的位置。
6. X.509标准

   X.509是一种密码学标准，定义了公共密钥基础设施（PKI）中的数字证书格式。这些证书包含有关实体（例如个人、组织或设备）的信息，以及相关的公钥和数字签名。X.509证书在许多互联网协议中广泛使用，如TLS/SSL等。

## JWT 基础安全问题

### 未对签名进行验证

JWT 库会通常提供一种验证令牌的方法和一种解码令牌的方法，比如：Node.js 库 jsonwebtoken 有 verify() 和 decode()，有时开发人员会混淆这两种方法，只将传入的令牌传递给decode()方法，这意味着应用程序根本不验证签名，我们可以利用这一点进行提权

下边我们通过 portswigger 靶场来演示一下这个漏洞案例：

靶场地址：https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiacSjPZemMjRykFB7BCTjdYmdzWWKthLVVuKYmWOyglSX9BvhuuaaJZg/640?wx_fmt=png&from=appmsg)

（1）首先看看通关要求：修改您的会话令牌以访问管理面板`/admin`，然后删除用户`carlos`

（2）前文我们说到，JWT 需要开发者提供一个 Signature（签名），如果我们不对签名进行验证，极有可能产生如下的越权情况。

（3）打开靶场，登录，访问`/admin`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiadEmaibxQX6tYUtquhDGF6eZjWHEVK8669NL2XuKyvsdDRBR79oaKH0A/640?wx_fmt=png&from=appmsg)

（4）因为我们使用的 jwt，所以权限相关的设置肯定在 jwt 中。我们抓个包拿到 jwt 解密看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiauKOzMricCFf1aopnBBzT4xshjiaO1KRTnDUckOP2xe8VD09NgicOibgibZg/640?wx_fmt=png&from=appmsg)

（5）把`wiener`修改成`administrator`，然后直接放包即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiae5M6CW83PBBd8RPdYDN1h7Rf2kIIQiaIvzKGFTXicAzD7vFxqMPHtYFA/640?wx_fmt=png&from=appmsg)

然后利用这个JWT越权删除用户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiavORFCHcYdDjzUbCLkvAzkAmxovK7sia36FGtc6jS3leQ9teQQ3LtQjA/640?wx_fmt=png&from=appmsg)

### 未对加密算法进行强验证

在 JWT 的Header中 alg 的值用于告诉服务器使用哪种算法对令牌进行签名，从而告诉服务器在验证签名时需要使用哪种算法，目前可以选择HS256，即HMAC和SHA256，JWT同时也支持将算法设定为"None"，如果"alg"字段设为"None"，则标识不签名，这样一来任何token都是有效的，设定该功能的最初目的是为了方便调试，但是若不在生产环境中关闭该功能，攻击者可以通过将alg字段设置为"None"来伪造他们想要的任何 token，接着便可以使用伪造的token冒充任意用户登陆网站

下边我们通过 portswigger 靶场来演示一下这个漏洞案例：

靶场地址：https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqia2G3nPDLicTzZRl5EGsZV0gI9v0LZNKuQmPxHJslGjACpvyEOzEolH1A/640?wx_fmt=png&from=appmsg)

这关与上边的漏洞原理不同，但最终的效果都是可以伪造 token，攻击手法与上一关卡相同，唯一不同的是这次是需要把 header 中的 alg 参数的值改为 none 即可！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiasIWictqahWTueo9H6aPJ0r7YqynJsl4hhDd7EP3v1EqaycF0x06UKUA/640?wx_fmt=png&from=appmsg)

记得登录一下，不然没有cookie，登录之后抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaBTzqXj5dxnYyDd0ZKVRjMh3hON3tUuazwR17iaMbjxJGBxTtHhB6nbQ/640?wx_fmt=png&from=appmsg)

url直接变色了，说明我们的插件检测到JWT令牌了，我们拿到第一部分，也就是Header，修改签名算法为None，同时要修改角色为管理员，同时因为我们修改为了无签名算法，所以我们需要将JWT令牌的最后一部分删除掉，然后重新编码拼接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiayxfCVwoYqzaPciaJN6tGiaCFrcTb3sTKb9L5pGNLQ97YYvoibYBIequOA/640?wx_fmt=png&from=appmsg)

这里我们只选用上面两部分，也就是Header以及Payload，然后我们修改cookie（cookie最后那个点还是要加的）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiacb4ILBBwZ4x0odHYxEhRxsricMDboPcQRd9ZhUhic8uWrsPezc1mlyWQ/640?wx_fmt=png&from=appmsg)

然后我们返回浏览器操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaqXgMdmWnne3HYX44KqXuau7wkbJQicQCSgPfrick311KSNiasEC1ySLSA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaRIsv9DxRibEiaNFx6DZklXqgtic38K5CxXQta1sdNEMMAt85eQgOfiabmA/640?wx_fmt=png&from=appmsg)

### 弱密钥

在实现 JWT 应用程序时，开发人员有时会犯一些错误，比如：忘记更改默认密码或占位符密码，他们甚至可能复制并粘贴他们在网上找到的代码片段然后忘记更改作为示例提供的硬编码秘密，在这种情况下攻击者使用众所周知的秘钥来暴力破解服务器的秘钥是很容易的

下边我们通过portswigger靶场来演示一下这个漏洞案例：

靶场地址：https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaCNHiaKmwzSEuCNIicEofKt6cickGoQGEFGqBfVnJU77L71AG95tY7mcpw/640?wx_fmt=png&from=appmsg)

这个就简单了，说白了就是爆破，可以使用工具JWT\_Tools，地址：https://github.com/ticarpi/jwt\_tool

JWT字典：https://github.com/wallarm/jwt-secrets

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiadC40SdlNtc1bJicYekSnG9t6vKn5cpicplMKSMBvJHWuZJLGGRkscCpQ/640?wx_fmt=png&from=appmsg)

这里我就不用这个了，我直接使用 Tscan 里面自带的 JwtCrack 功能了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiatdmb3u0IrCgyllT3F83v2WEk9hN9l7l1Hh7KtD1NoA3gNDmiadP0gIQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiavoNw0IlxRCI70wAtEsTgQ4fpIsyWBIaXp7D2Uia7AnuPbCBsmribs03g/640?wx_fmt=png&from=appmsg)

ok，爆破成功，拿到签名密钥为：secret1，我们利用这个密钥篡改jwt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zJ5s7YlpdicBFyiaCJrw6QVtfeP8upzOqiaXBqNGk1KbQRd5mrKuOlXvCg754Kp2SD7iaTylqbTLEsVoME5m2pAb5Q/640?wx_fmt=png&from=appmsg)

利用这个新的JWT登录

```
eyJraWQiOiJmYzI2ZDFmYy0yYzk3LTQzZDQtYTE0OS05MzAwOWE3NWRkY2MiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc1Mjg1MTA0Mywic3ViIjoiYWRtaW5pc3RyYXRvciJ9.MVzoj_Igww...