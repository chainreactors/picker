---
title: JWT安全解析：从设计哲学到致命漏洞
url: https://mp.weixin.qq.com/s/VoJOaP_A909qRPBO1Z0s_g
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:29:48.741502
---

# JWT安全解析：从设计哲学到致命漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vRBYx9F4Zf6QWdOHc9xZZewOXXOKkTMKtF3PfMrSc6BCdK903mp7icsWrBHXauAjGB3wvN9Odxv9sBpYUzUuO2A/0?wx_fmt=jpeg)

# JWT安全解析：从设计哲学到致命漏洞

极客零零七

![]()

在小说阅读器中沉浸阅读

在现代Web应用和微服务架构中，JSON Web Token (JWT)已成为事实上的身份认证标准。它以其轻量、自包含和跨语言的特性，解决了传统认证机制在分布式环境中遇到的诸多痛痛点。然而，这种强大的灵活性也伴随着复杂的安全挑战。

本文将分为两部分：第一部分，我们将深入探讨JWT的核心设计原则，理解它为何以及如何工作。第二部分，我们将切换到攻击者的视角，剖析针对JWT的常见攻击技术，并通过经典的CVE案例来揭示一个微小实现错误如何导致整个安全体系的崩溃。

---

## 第一部分：JWT的设计哲学与工作原理

### 问题的根源：有状态认证的枷锁

在JWT出现之前，Web世界普遍采用基于Session的认证方式。这种模式的核心是有状态（Stateful）：
![](https://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6QWdOHc9xZZewOXXOKkTMKLLiaic7JfYnRvT8dp5VfwzqXibGW9afk4Qhb75wiaqTZ2D50WwqHAIKWxA/640?wx_fmt=png&from=appmsg "null")

1. 1. 用户登录后，服务器创建一个Session对象存储用户信息，并生成一个session\_id。
2. 2. session\_id通过Cookie返回给客户端。
3. 3. 客户端此后的每次请求都携带session\_id。
4. 4. 服务器通过session\_id查找对应的Session数据，以确认用户身份。

这种模式的弊端在分布式架构中被无限放大：

* • 扩展性瓶颈：每台服务器都需要能访问到Session存储（通常是内存或Redis），这导致了对中心化存储的依赖和同步的复杂性。
* • 服务端负担：服务器需要维护数百万用户的Session信息，消耗大量资源。
* • 跨域与移动端不友好：基于Cookie的Session机制在处理CORS和移动App原生调用时，配置繁琐且容易出错。

### **解决方案：JWT的无状态革命**

JWT的核心思想是无状态（Stateless）和自包含（Self-Contained）。服务器不再存储任何会话信息，所有验证所需的数据都包含在Token本身。一个JWT是一个由三部分组成的字符串，以.分隔：Header.Payload.Signature。示例JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiZXhwIjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**a. Header (头部)**
头指定了签名算法（alg）和令牌类型（typ）。它是一个JSON对象，经过Base64Url编码后构成了JWT的第一部分。

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**b. Payload (载荷)**
载荷包含了被称为“声明”（Claims）的数据。这是关于用户或其他实体的陈述，例如用户ID、角色、过期时间等。它同样是一个经过Base64Url编码的JSON对象。

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "exp": 1516239022
}
```

一个至关重要的警告：Payload仅仅是编码，而非加密。任何人都可以解码并读取其内容。因此，绝对不能在Payload中存放任何敏感信息，如密码或个人隐私数据。

**c. Signature (签名)**
签名是JWT安全性的基石。它的作用是验证发送者的身份并确保消息在传输过程中未被篡改。签名的生成过程如下（以HMAC-SHA256为例）：

```
HMACSHA256(
base64UrlEncode(header) + "." +
base64UrlEncode(payload),secret_key
)
```

服务器使用一个仅自己知道的密钥（`secret_key`）对编码后的Header和Payload进行签名。当服务器收到一个JWT时，它会用相同的密钥重新执行一次签名计算，并比对计算结果与JWT自带的签名是否一致。如果不一致，说明数据被篡改或签名是伪造的，请求将被拒绝。

这个密钥永远不会传输给客户端，从而保证了签名的可靠性。

## 第二部分：攻破壁垒 - 针对JWT的攻击

JWT的规范本身是安全的，但其安全性高度依赖于开发者的正确实现。错误的配置或代码逻辑会打开致命的攻击窗口。

### **1. 签名攻击：信任的崩溃**

**a. 算法混淆 (CVE-2015-2951): RS256 -> HS256 的经典一击**

这是JWT历史上最著名的漏洞之一，它巧妙地利用了非对称与对称算法的实现差异。RS256 (RSA): 非对称算法。使用私钥签名，使用公钥验证。公钥可以安全地公开。HS256 (HMAC): 对称算法。使用同一个密钥进行签名和验证。攻击流程:

1. 1. 假设一个应用使用RS256。服务器持有私钥，并将对应的公钥发布出去供客户端或资源服务器验证。
2. 2. 攻击者获取了这个公开的公钥。
3. 3. 攻击者创建一个恶意的JWT，并在Header中将算法alg篡改为HS256。
4. 4. 最关键的一步：攻击者使用获取到的公钥作为HMAC的密钥，对这个HS256的Token进行签名。
5. 5. 攻击者将这个伪造的Token发送给服务器。

漏洞成因: 易受攻击的服务器在验证Token时，会执行以下错误逻辑：

1. 1. 读取Header，发现alg是HS256。
2. 2. 于是，它加载用于验证签名的“密钥”。在代码实现中，这个密钥变量可能被设计为同时存储RS256的公钥或HS256的密钥。
3. 3. 它将加载的公钥当作HMAC密钥来验证签名。

由于攻击者和服务器使用了完全相同的“密钥”（即公钥）和相同的HMAC算法，签名验证成功通过！攻击者由此可以伪造任意身份。

防御策略: 永不信任来自Token Header的`alg`字段。服务器必须在验证逻辑中强制指定并检查算法。如果你的系统设计使用RS256，那么代码必须拒绝任何alg不等于RS256的Token。

**b. 算法置空攻击 (`alg: none`)**

JWT规范允许alg字段为"none"，表示这是一个未签名的Token。如果服务器库配置不当，没有明确指定必须验证签名，它可能会接受这个alg: "none"的Token，从而完全跳过安全验证。

防御策略: 在服务器端建立一个可接受算法的白名单（例如 ['HS256', 'RS256']），并拒绝任何不在白名单中的算法，尤其是"none"。

### 2. 实现层攻击：利用逻辑漏洞

**a. 弱密钥暴力破解**
如果使用HS256算法，但密钥过于简单（如 "secret", "123456"），攻击者可以离线进行字典攻击或暴力破解。

防御策略: 使用由密码学安全随机数生成器产生的高熵密钥，并将其作为最高机密通过环境变量或密钥管理服务（KMS）来管理。

**b. KID注入攻击**
kid (Key ID) Header用于指定验证签名时应使用的密钥，这对于密钥轮换非常有用。但如果服务器端代码直接将kid的值用于路径拼接或数据库查询，就会引发严重漏洞。

* • 目录遍历: kid: "../../../../dev/null"
* • SQL注入: kid: "key1' UNION SELECT 'malicious\_key' --"

防御策略: 对kid进行严格的清理和验证。最佳实践是维护一个允许的kid到实际密钥的映射表（Map），任何不在表中的kid都应被拒绝。

### 3. 生命周期与存储攻击

**a. XSS导致Token泄露**
将JWT存储在localStorage或sessionStorage中是一个常见的错误。任何XSS漏洞都允许恶意脚本读取并窃取这些Token，然后攻击者就可以用它来冒充用户。

防御策略: 将JWT存储在`HttpOnly` Cookie中。这可以防止客户端JavaScript访问它，从而有效缓解XSS带来的Token盗窃风险。

**b. 缺乏撤销机制**
JWT的无状态特性意味着一旦签发，在过期之前它就一直有效。如果Token被盗，或者用户更改了密码，旧Token依然可以被使用。

防御策略:

* • 短生命周期: 签发生命周期极短的Access Token（如5分钟），并配合使用长生命周期的Refresh Token。
* • 撤销列表（黑名单）: 在Redis等高速缓存中维护一个已撤销Token的ID（jti声明）列表。这虽然牺牲了部分无状态性，但在高安全要求的场景下是必要的。

### 结论

JWT是一个强大而优雅的认证工具，它极大地简化了现代分布式应用的身份验证流程。然而，它的安全性并非与生俱来，而是完全建立在审慎和严谨的实现之上。

作为开发者，我们必须超越“能用就行”的层面，深刻理解其工作原理和潜在的攻击面。通过始终使用经过良好维护的库、强制校验算法、安全管理密钥并遵循存储最佳实践，我们才能真正驾驭JWT的力量，构建既灵活又安全的应用系统。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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