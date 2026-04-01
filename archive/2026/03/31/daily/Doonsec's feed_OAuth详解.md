---
title: OAuth详解
url: https://mp.weixin.qq.com/s/1HPNw7jplkmkz1SpYTXexw
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:08.336017
---

# OAuth详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qkajCoyKpkCP1LwP4HCthy2SUWlLcQ7AkDS9LJMvC8WKIBouYTDiaNicSFQqIoFrpf5GVm6Su2ZXwpXBsjcqCPFZwOvVeDgJqrrGHxUGMt09k/0?wx_fmt=jpeg)

# OAuth详解

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

### 什么是OAuth

* OAuth (Open Authorization) 是一个开放标准的授权协议，目前主流版本为 OAuth 2.0，并在 2026 年逐步全面过渡到更安全的 OAuth 2.1 标准
* 一般只有中大型网站才会使用OAuth（有用户需求、体验，有大量流量、请求）
* 核心目的：允许用户（资源所有者）授权第三方应用（客户端）访问其在另一个服务（资源服务器）上的资源，而无需将用户名和密码提供给第三方应用
* 核心区别：OAuth 是授权 (Authorization) 协议，不是认证 (Authentication) 协议。虽然常被用于登录（第三方登录），但其本质是颁发“访问令牌”
* 通俗类比：

+ 传统模式： 你把酒店房间的主钥匙（密码）复制一把给保洁人员（第三方应用），保洁人员拥有和你一样的全部权限，且永久有效
+ OAuth 模式： 酒店前台（授权服务器）给保洁人员一张限时、限权限的门卡（Access Token）。这张卡只能打开特定房间，且第二天失效。你不需要把主钥匙给保洁人员

### 怎么判断是OAuth

* 看请求，后面会讲到
* 是否有第三方登录/授权(如QQ、微信、微博等第三方)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDnRKic2FtDFiaujAItxAtJY81dPeWlg3byM4RzjhLr7UwPeAcD9SarY948wGXhYmLA3OibZ9ko9wSrgIKMIO0RbHdia8P6fM6NNNo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBZOTxy8ohnIDzvB2DbJjvv070DdTyZk6ptNTDBh6Yq1CcWm605tdvGpEaib0Jo8umPFtN9yzMZ61skDNPr3GQAK6B9ZsWek7HI/640?wx_fmt=png&from=appmsg)

### OAuth核心角色

* 资源所有者（Resource Owner）：拥有账户和数据的人，通常是用户
* 客户端（Client）：请求访问资源的第三方应用，如 APP / 网站 / 小程序
* 授权服务器（Authorization Server）：验证用户身份并颁发令牌的服务器，如微信开放平台、Google Login
* 资源服务器（Resource Server）：存储用户受保护资源的 API 服务器，如微信用户信息接口、Google Calendar API
* 注意： 在实际架构中，授权服务器 (AS) 和资源服务器 (RS) 通常由同一提供商维护（如 Google）

### 常用令牌类型

* 不记名令牌(Bearer Token)：

+ 最常见的类型。HTTP 头格式：Authorization: Bearer <token>
+ 缺陷： 一旦通过 HTTPS 泄露（如日志、中间人），攻击者可直接使用
+ 特点：谁持有谁使用，无需额外证明。类似现金
+ 安全性：中。主流但逐渐被替代。易被重放、拦截

* 引用令牌(Reference Token)：

+ 格式如 Bearer 3b8d7f...。资源服务器收到后，调用授权服务器的 /introspect 接口验证有效性
+ 优势： 授权服务器可立即撤销令牌，无需等待过期
+ 特点：一串随机字符，本身无意义。资源服务器需向授权服务器查询（Introspection）验证
+ 安全性：高。推荐。可随时撤销，泄露后危害可控

* 自包含令牌(JWT)：

+ 格式如 eyJhbG...。包含 Header, Payload (claims), Signature
+ 缺陷： 无法直接撤销（除非使用黑名单），需严格保护签名密钥
+ 特点：包含用户信息签名，资源服务器可本地验证，无需查询
+ 安全性：中。主流。需注意密钥泄露和算法攻击

* 持有者证明令牌(DPoP Token)：

+ 格式类似 Bearer，但使用时需额外发送 DPoP HTTP 头，包含用私钥签定的请求证明
+ 优势： 即使令牌被盗，攻击者没有私钥也无法构造合法的 DPoP 证明，令牌作废
+ 特点：令牌与客户端公钥绑定。请求时需附带私钥签名证明
+ 安全性：极高。2026 年推荐标准。防止令牌被盗后重用

### 安全增强机制（OAuth2.1）

为了应对 OAuth 固有漏为了应对 OAuth 固有漏洞，2026 年标准引入了以下增强机制洞，2026 年标准引入了以下增强机制

* PKCE (Proof Key for Code Exchange)：

+ 原理： 客户端生成随机验证码 code\_verifier，哈希后作为 code\_challenge 发送。换取令牌时需提供原值
+ 作用： 防止授权码拦截攻击。即使攻击者截获了 Code，没有 Verifier 也无法换 Token
+ 现状： 2026 年所有客户端（包括机密客户端）强制使用

* mTLS (Mutual TLS)：

+ 原理： 客户端与授权服务器/资源服务器之间建立双向证书认证
+ 作用： 替代 client\_secret 进行客户端认证，防止密钥泄露。同时实现发送者约束令牌（令牌绑定证书）
+ 现状： 高安全场景（如金融 API）标配

* DPoP (Demonstrating Proof of Possession)：

+ 原理：客户端生成密钥对。请求令牌时发送公钥哈希。使用令牌访问资源时，用私钥对请求签名
+ 作用：防止令牌重放和令牌泄露。令牌与特定客户端绑定
+ 现状：OAuth 2.1 推荐用于替代 Bearer Token

* 刷新令牌轮换 (Refresh Token Rotation)：

+ 原理：每次使用 Refresh Token 换取新 Access Token 时，授权服务器颁发一个新的 Refresh Token，并使旧的立即失效
+ 作用：防止刷新令牌滥用。如果攻击者盗用了旧 Refresh Token 尝试使用，授权服务器检测到“已轮换的令牌被重用”，可判定泄露并撤销整个授权链
+ 现状：2026 年最佳实践强制要求

* 令牌内省 (Token Introspection)：

+ 原理：资源服务器调用授权服务器的 /introspect 接口查询令牌状态
+ 作用：实时确认令牌是否有效、是否被撤销。主要用于 Reference Token
+ 现状：配合引用令牌使用，解决 JWT 无法撤销的问题

* 发送者约束令牌 (Sender-Constrained Tokens)：

+ 原理：泛指 DPoP 和 mTLS 绑定的令牌。令牌的有效性依赖于请求者的特定属性（密钥或证书）
+ 作用：解决 Bearer Token“谁拿到谁能用”的根本缺陷
+ 现状：2026 年高安全 API 的首选

|  |  |  |  |
| --- | --- | --- | --- |
| 特性 | 旧标准 (OAuth 2.0) | 新标准 (OAuth 2.1 / 2026 实践) | 安全收益 |
| 隐式模式 | 允许 | 禁止 | 防止 Token 通过 URL 泄露 |
| 密码模式 | 允许 | 禁止 | 防止用户密码泄露给第三方 |
| PKCE | 仅公共客户端推荐 | 所有客户端强制要求 | 防止授权码拦截攻击 |
| 令牌类型 | Bearer Token | 推荐DPoP或mTLS | 防止令牌重放攻击 |
| 刷新令牌 | 可选 | 推荐启用并实施轮换 | 限制令牌泄露后的危害范围 |
| 重定向 URI | 允许部分匹配 | 精确匹配 | 防止重定向篡改 |

### 授权模式

#### 授权码模式（Authorization Code Grant）

* 适用场景：Web 服务器端应用（机密客户端），有后端服务可安全存储 client\_secret
* 安全性： 高（最推荐，2026 年标准强制配合 PKCE）
* 特点： 引入中间码（Authorization Code），避免令牌直接在浏览器暴露。令牌交换在后端进行

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkClZzBPQErOibtuc6LanBibTBQLcFybZiaIcicSuQ4m8ADNw9jeReRH8qbJWKPjS7QOYuk8fDIGs908BfphUo61QXzwHEBF8mZnbPc/640?wx_fmt=png&from=appmsg)

详细步骤：

1. 客户端发起授权请求：客户端将用户重定向到授权服务器的授权端点，携带以下参数：

```
授权请求：https://auth.example.com/authorize?response_type=code&client_id=abc123&redirect_uri=https://client.com/callback&state=xyz&scope=read
```

+ response\_type=code：指定授权流程类型，code表示使用授权码模式
+ client\_id：客户端标识符，用于识别应用
+ redirect\_uri：授权完成后重定向回客户端的 URI，必须与注册时一致
+ scope：请求的权限范围（如 read、write，也可以是用户的基本信息，如profile、phone、email、roles），使用空格分隔
+ state：客户端生成的随机值，用于防止 CSRF 攻击，授权服务器原样返回

2. 用户认证与授权：授权服务器验证用户身份（如果未登录则提示登录），然后询问用户是否同意授予客户端所请求的权限
3. 返回授权码：用户同意后，授权服务器将用户重定向回 redirect\_uri，并在 URL 查询参数中附加 code（一次性授权码）和原样返回的 state
4. 客户端换取访问令牌：客户端收到授权码后，向授权服务器的令牌端点发送 POST 请求，携带：

```
令牌请求(POST)：POST /token HTTP/1.1Host: auth.example.comContent-Type: application/x-www-form-urlencoded
grant_type=authorization_code&code=AUTH_CODE&client_id=abc123&client_secret=secret&redirect_uri=https://client.com/callback
```

+ grant\_type：令牌端点使用的授权类型，此处为authorization\_code
+ client\_id 和 client\_secret（机密客户端必须提供）
+ client\_secret：客户端密码，仅机密客户端使用
+ code：上一步获得的授权码，一次性，有效期极短(通常几分钟)
+ redirect\_uri：必须与第一步的 redirect\_uri 一致

5. 返回令牌：授权服务器验证授权码、redirect\_uri 及客户端身份后，返回 access\_token（访问令牌）和可选的 refresh\_token（刷新令牌）

#### 隐式模式（Implicit Grant）

* 适用场景：单页应用（SPA）、移动应用等公共客户端（已不推荐，OAuth 2.1 已移除）
* 特点： 授权服务器直接返回 Access Token，不经过授权码环节
* 风险： Token 直接暴露在 URL 中，易被拦截或泄露；已不推荐使用

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDibnUF9q6LWhDe0IGfsBDCyyA5loichIRSe1TUaxTjxWQadEiciaIcQ71SDVco4o0W84XD1kkk1zmvT1bzW2p4KXyntNlJDyia6a0c/640?wx_fmt=png&from=appmsg)

详细步骤：

1. 客户端发起授权请求：与授权码模式类似，但 response\_type=token

```
授权请求：https://auth.example.com/authorize?response_type=token&client_id=abc123&redirect_uri=https://client.com/callback&state=xyz&scope=read
```

+ response\_type：刷新令牌，用于换取新的 Access Token，长期有效
+ scope：实际授权范围，可能比请求的范围小

2. 用户认证与授权：同授权码模式
3. 返回访问令牌：授权服务器将用户重定向回 redirect\_uri，在 URL 片段（#）中直接返回 access\_token，同时可选 token\_type、expires\_in 等

```
响应：https://client.com/callback#access_token=eyJ...&token_type=Bearer&expires_in=3600&state=xyz
```

+ access\_token：访问令牌，属于核心资产，拥有它即可访问资源
+ token\_type：令牌类型，通常使用 Bearer 模式
+ expires\_in：过期时间，令牌有效期
+ state：状态参数，防止 CSRF 攻击的关键

4. 客户端提取令牌：前端 JavaScript 从 location.hash 中提取令牌，并用于后续 API 请求

##### 资源所有者密码凭证模式（Resource Owner Password Credentials Grant）

* 适用场景：高度信任的客户端（如官方第一方应用），用户提供用户名密码直接换取令牌（已不推荐）
* 风险：客户端直接获取用户密码，违反 OAuth 设计初衷；易导致凭据泄露

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkC9mk4AdAXWiaz8uniaibB4LIjP3JQ5eQI2j0NGgAkicBO1OoDDxFmSv0zCdsFG3DStbf4o9eVXbHY1fgyHNHFvWSNWvmUA6ALiaTu4/640?wx_fmt=png&from=appmsg)

详细步骤：

1. 客户端收集用户凭证：用户在客户端界面输入用户名和密码
2. 客户端向令牌端点请求：发送 POST 请求，携带：

```
POST /token HTTP/1.1Host: auth.example.comContent-Type: application/x-www-form-urlencoded
grant_type=password&username=alice&password=secret&client_id=abc123&client_secret=secret
```

+ grant\_type：令牌端点使用的授权类型，此处固定为password
+ username：资源所有者的用户名
+ password：资源所有者的密码
+ client\_id：客户端标识（可选，但建议提供）
+ client\_secret：客户端密码（机密客户端提供）

3. 返回令牌：授权服务器验证凭证后返回 access\_token 和 refresh\_token

#### 客户端凭证模式（Client Credentials Grant）

* 适用场景：客户端自身访问自己的资源（非用户委托），如机器对机器的 API 调用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDTG7fx9zicguSyPOHyewubjHfIX9BFwbaWOMdFzibJl4vRg3pkaAqrBpEiaXwIEhbXUTrZAaYW9MSpicAC8uf18tUeua7uKmMzXhg/640?wx_fmt=png&from=appmsg)

详细步骤：

1. 客户端向令牌端点请求：发送 POST 请求，携带：

```
POST /token HTTP/1.1Host: auth.example.comContent-Type: application/x-www-form-urlencoded
grant_type=client_credentials&client_id=abc123&client_secret=secret
```

+ grant\_type：令牌端点使用的授权类型，此处固定为 client\_credentials
+ client\_id：客户端标识
+ client\_secret：客户端密码

2. 返回访问令牌：授权服务器验证客户端身份后返回 access\_token（通常不含刷新令牌）

#### 设备码模式（Device Authorization Grant）

* 适用场景：无浏览器的输入受限设备（如智能电视、命令行工具）

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCal7c7jPe5nNZGIZKy4Lmr8rJCLs5D6XQvnw8RQhlUjOVxCpBxoNknnspcRNCZRhiceLHewCeB7M4LIjezaicTUs8dvOqNcm6H8/640?wx_fmt=png&from=appmsg)

详细步骤：

1. 客户端请求设备码：向授权服务器的设备授权端点发送 POST 请求，携带 client\_id 和 scope

```
设备授权请求：POST /device_authorization HTTP/1.1Host: auth.example.comContent-Type: application/x-www-form-urlencoded
client_id=abc123&scope=read
```

+ client\_id：客户端标识
+ scope：实际授权范围，可能比请求的范围...