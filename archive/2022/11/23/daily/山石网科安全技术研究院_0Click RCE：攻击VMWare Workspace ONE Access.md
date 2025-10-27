---
title: 0Click RCE：攻击VMWare Workspace ONE Access
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247497573&idx=1&sn=497d359ecd88e851b8824180a0ec5256&chksm=fa5222dbcd25abcd961a9aa09376e304d0ea62650887931afb070d3b423ad9ff0ab58d65567d&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-11-23
fetch_date: 2025-10-03T23:30:19.914046
---

# 0Click RCE：攻击VMWare Workspace ONE Access

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRcIo3zjtulicBH0zX1gHBH48vyscyMicwQCWZOPPu7rnNv7kwicKlEx5GcrcoELa2NAAdmkd2x0GIaQ/0?wx_fmt=jpeg)

# 0Click RCE：攻击VMWare Workspace ONE Access

原创

应用安全实验室

山石网科安全技术研究院

**IAM 介绍**

**00**

身份和访问管理（IAM）全称Identity and Access Management，IAM 是提供用户用来管理用户对 [AWS](https://so.csdn.net/so/search?q=AWS&spm=1001.2101.3001.7020) 资源的访问权限及其身份验证的服务。基本上的特性有：

- IAM账户使用者可以分为根使用者 (root user) 与一般使用者 (IAM user)。

- 创建用户、组和角色，并为其附加策略以控制其对 AWS 资源的访问权限。

也就是说，IAM就是将身份认证和授权访问管理集成到一个单一的解决方案中。

身份认证（Identity ）通常是通过密码验证和联合身份验证完成的，例如单点登录 (SSO) 技术，其中用到就有像安全断言标记语言 (SAML)这样的技术，下面会进行介绍。

而授权访问管理（Access）就是给已通过身份验证的用户给定资源的特权或访问权限。例如Open Authorization (OAuth2)技术和用于数据交换的 Java Web Token (JWT)。

IAM可以说是近年来攻击者的主要目标，它主要有以下几个特点：

- 完全控制认证和授权过程

- 必须暴露在外网

- 必须使用足够复杂的技术栈和协议

这也意味着如果破坏了外网的IAM也就表示破坏了统一控制的其他几个系统的正常使用。

> 相关术语：

> - 访问控制决策：访问控制决策是一个布尔值，指示是否允许请求的操作。它基于呼叫者的身份和访问控制策略。

> - 访问控制策略：访问控制策略用于定义访问特定对象（如服务接口）必须满足的约束。

>   政策决策点（PDP）：PDP做出访问控制决策。它通过检查访问控制策略来确定是否允许自适应应用程序执行请求的任务。

> - 政策执行点（PEP）：PEP通过从PDP请求访问控制决策来中断自适应应用程序请求期间的控制流，并强制执行该决策。

> - 意图Intent：意图是应用程序标识的属性。仅当请求的AA拥有该特定资源所必需的所有已确认意图时，才会授予对AUTOSAR资源（例如服务接口）的访问权。意向在其应用程序清单中分配给AAs。

> - 授予Grant：在部署自适应应用程序期间，应确认设计阶段要求的每个意图。Grant元素在元模型中可用。赠款将支持集成商审查意向，但不允许部分接受意向。

> - 中间标识符（IntID）：一个标识符，用于识别正在运行的POSIX进程并映射到已建模的AUTOSAR进程。IntID的具体性质取决于用于验证运行POSIX进程的机制。

> - 自适应应用程序标识（AAID）：自适应应用程序的建模标识由AUTOSAR流程表示。

> - 自适应应用程序标识符：对AAID的引用，即AUTOSAR流程，精确指向一个AAID。

**身份认证 - SAML**

SAML全称是安全断言标记语言（Security Assertion Markup Language）是一个基于XML的开源标准数据格式。用于在不同的安全域之间交换认证和数据授权。在SAML标准定义了身份提供者（IDP）和服务提供者（SP），这两者构成了前面所说的不同的安全域。

SAML解决的最重要的需求是Web端应用的单点登录（SSO）。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSVkcaTkRAQv5de5aP1SnYvshxolMToGlrsQHZlFPKicC8DzKGGrNJwVI387dv6PiaHv1I8PUZEKzfQ/640?wx_fmt=png)

如图，认证流程入下：

1. 用户请求访问 Web 应用系统。Web 应用系统生成一个 SAML 身份验证请求。

2. Web 应用系统将重定向网址发送到用户的浏览器。重定向网址包含应向SSO 服务提交的编码 SAML 身份验证请求。IDP 对 SAML 请求进行解码。

3. 用户发起验证请求，IDP对用户进行身份验证。

4. 认证成功后，IDP生成一个 SAML 响应，其中包含经过验证的用户的用户名。然后将SAML 响应编码并返回到用户的浏览器。

5. 浏览器将 SAML 响应转发到 Web 应用系统 ACS URL。Web 应用系统（SP）使用 IDP 的公钥验证 SAML 响应。

6. 如果成功验证该响应，ACS 则会将用户重定向到目标网址。用户将重定向到目标网址并登录到 Web 应用系统。

**授权验证 -  OAuth2**

OAuth2.0是一种允许第三方应用程序使用资源所有者的\*\*凭据\*\*获得对资源有限访问权限的一种授权协议。

OAuth 2.0 主要有4类角色：

- resource owner：资源所有者（RO），即能够有权授予对保护资源访问权限的实体。例如我们使用通过微信账号登陆豆瓣网，而微信账号信息的实际拥有者就是微信用户，也被称为最终用户。

- authorization server： 授权服务器（AS）， 认证服务器，即服务提供商专门用来处理认证授权的服务器。例如微信开放平台提供的认证服务的服务器。

- resource server：资源服务器（RS），承载受保护资源的服务器，能够接收使用访问令牌对受保护资源的请求并响应，它与授权服务器可以是同一服务器，也可以是不同服务器。在上述例子中该角色就是微信服务器。

- client：客户端，代表向受保护资源进行资源请求的第三方应用程序。

**认证流程**

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSVkcaTkRAQv5de5aP1SnYviafn703LmZDJU6cHkqmCqnM6Fwc4eWoojiaz1ZmibV72tMSuXJT0cC5eA/640?wx_fmt=png)

如图，验证流程入下：

1、 在客户端web项目中构造一个oauth的客户端请求对象（OAuthClientRequest），在此对象中携带客户端信息（clientId、accessTokenUrl、response\_type、redirectUrl），将此信息放入http请求中，重定向到服务端。此步骤对应上图步骤1

2、 在服务端web项目中接受第一步传过来的request，从中获取客户端信息，可以自行验证信息的可靠性。同时构造一个oauth的code授权许可对象（OAuthAuthorizationResponseBuilder），并在其中设置授权码code，将此对象传回客户端。此步骤对应上图步骤2

3、 在在客户端web项目中接受第二步的请求request，从中获得code。同时构造一个oauth的客户端请求对象（OAuthClientRequest），此次在此对象中不仅要携带客户端信息（clientId、accessTokenUrl、clientSecret、GrantType、redirectUrl），还要携带接受到的code。再构造一个客户端请求工具对象（oAuthClient），这个工具封装了httpclient，用此对象将这些信息以post(一定要设置成post）的方式请求到服务端，目的是为了让服务端返回资源访问令牌。此步骤对应上图步骤3。（另外oAuthClient请求服务端以后，会自行接受服务端的响应信息。

4、 在服务端web项目中接受第三步传过来的request，从中获取客户端信息和code，并自行验证。再按照自己项目的要求生成访问令牌（accesstoken），同时构造一个oauth响应对象（OAuthASResponse），携带生成的访问指令（accesstoken），返回给第三步中客户端的oAuthClient。oAuthClient接受响应之后获取accesstoken，此步骤对应上图步骤4

5、 此时客户端web项目中已经有了从服务端返回过来的accesstoken，那么在客户端构造一个服务端资源请求对象（OAuthBearerClientRequest），在此对象中设置服务端资源请求URI，并携带上accesstoken。再构造一个客户端请求工具对象（oAuthClient），用此对象去服务端靠accesstoken换取资源。此步骤对应上图步骤5

6、 在服务端web项目中接受第五步传过来的request，从中获取accesstoken并自行验证。之后就可以将客户端请求的资源返回给客户端了。

**认证方式**

OAuth 2.0 共有 4 种访问模式：

- 授权码模式(Authorization Code)，适用于一般服务器端应用

  授权码模式（authorization code）是功能最完整、流程最严密的授权模式。

- 简化模式(Implicit)，适用于纯网页端应用

  简化模式是对授权码模式的简化，用于在浏览器中使用脚本语言如JS实现的客户端中，它的特点是不通过客户端应用程序的服务器，而是直接在浏览器中向认证服务器申请令牌，跳过了“授权码临时凭证”这个步骤。其所有的步骤都在浏览器中完成，令牌对访问者是可见的，且客户端不需要认证。

- 密码模式(Resource owner password credentials)

  在密码模式中，用户需要向客户端提供自己的用户名和密码，客户端使用这些信息向“服务提供商”索要授权。这相当于在豆瓣网中使用微信登录，我们需要在豆瓣网输入微信的用户名和密码，然后由豆瓣网使用我们的微信用户名和密码去向微信服务器获取授权信息。

- 客户端模式(Client credentials)

  客户端模式是指客户端以自己的名义，而不是以用户的名义，向“服务提供方”进行认证。严格地说，客户端模式并不属于OAuth2.0协议所要解决的问题。在这种模式下，用户并不需要对客户端授权，用户直接向客户端注册，客户端以自己的名义要求“服务提供商”提供服务。

用到最多的还是授权码模式，这里重点介绍下授权码模式。

**授权码模式**

步骤如下：

> （A）用户访问客户端，后者将前者导向认证服务器。

> （B）用户选择是否给予客户端授权。

> （C）假设用户给予授权，认证服务器将用户导向客户端事先指定的"重定向URI"（redirection URI），同时附上一个授权码。

> （D）客户端收到授权码，附上早先的"重定向URI"，向认证服务器申请令牌。这一步是在客户端的后台的服务器上完成的，对用户不可见。

> （E）认证服务器核对了授权码和重定向URI，确认无误后，向客户端发送访问令牌（access token）和更新令牌（refresh token）。

下面是上面这些步骤所需要的参数。

A步骤中，客户端申请认证的URI，包含以下参数：

- response\_type：表示授权类型，必选项，此处的值固定为"code"

- client\_id：表示客户端的ID，必选项

- redirect\_uri：表示重定向URI，可选项

- scope：表示申请的权限范围，可选项

- state：表示客户端的当前状态，可以指定任意值，认证服务器会原封不动地返回这个值。

下面是一个例子:

```
GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz
        &redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
Host: server.example.com
```

D步骤中，客户端向认证服务器申请令牌的HTTP请求，包含以下参数：

- grant\_type：表示使用的授权模式，必选项，此处的值固定为"authorization\_code"。

- code：表示上一步获得的授权码，必选项。

- redirect\_uri：表示重定向URI，必选项，且必须与A步骤中的该参数值保持一致。

- client\_id：表示客户端ID，必选项。

下面是一个例子

```
POST /token HTTP/1.1
Host: server.example.com
Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA
&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb
```

E步骤中，认证服务器发送的HTTP回复，包含以下参数：

- access\_token：表示访问令牌，必选项。

- token\_type：表示令牌类型，该值大小写不敏感，必选项，可以是bearer类型或mac类型。

- expires\_in：表示过期时间，单位为秒。如果省略该参数，必须其他方式设置过期时间。

- refresh\_token：表示更新令牌，用来获取下一次的访问令牌，可选项。

- scope：表示权限范围，如果与客户端申请的范围一致，此项可省略。

下面是一个例子:

```
HTTP/1.1 200 OK
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "access_token":"2YotnFZFEjr1zCsicMWpAA",
       "token_type":"example",
       "expires_in":3600,
       "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
       "example_parameter":"example_value"
     }
```

从上面代码可以看到，相关参数使用JSON格式发送（Content-Type: application/json）。此外，HTTP头信息中明确指定不得缓存。

**IAM 漏洞类型**

**01**

**攻击身份认证服务端(Authentication - Server-side)**

- XML令牌解析（XXE、SSRF、XSLT等）

- 签名验证（Signature verification）绕过（XSW攻击、XML签名攻击绕过等）

这些都是直接针对IdP或SP的服务器端可进行的攻击方法

**攻击授权验证客户端（Authorization - Client-side）**

- Access token、授权码（authorization code）泄露等

- XSS、CSRF、URL重定向、点击劫持等等

**IAM 产品相关历史漏洞**

**02**

**IAM相关产品**

**Oracle Access Manager (OAM)**

Oracle Access Manager是Oracle公司的产品，并与Oracle的Weblogic AS捆绑使用。就像名字起的那样，主要就是用于访问控制，但是主要是粗粒度的鉴权，通过url来定义不同的资源，通过制定相应的认证策略和授权策略来控制用户的访问，现在用的比较多的功能是单点登录。

**ForgeRock OpenAM**

ForgeRock OpenAM是美国ForgeRock（Forgerock）公司的一套开源的单点登录框架（SSO）。该框架通过提供核心的标识服务（CoreServer）以实现在一个网络架构中的透明单点登录（如集中式、分布式的单点登录）。

**VMWare Workspace ONE Access**

正式名称为 VMWare Identity Manager (vIDM) ，是VMWare的IAM旗舰解决方案，虽然相对较新，但仍被几家财富500强公司使用。

**相关历史漏洞**

**CVE-2021-35587**

**Oracle Access Manager对不可信的数据进行反序列化：**

简单说下这个漏洞的原理，oracle.security.am.pbl.transport.http.AMServlet调用 `handleRequest()` 然后调用 `PBLFlowManager.processRequest()` 来处理我们传入的请求，如果我们传入的是/oam/server/opensso/sessionservice这样一个URI，会 映射到一个名为 `OPENSSO\_CHECK\_VALID\_SESSION` 的事件名称(eventName)，然后根据这个名称创建一个EventHint，然后使用该eventHint从映射中获取requestHandler

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSVkcaTkRAQv5de5aP1SnYvwOOQVHj1wGUaLoeciadgzRAyXvp7wskxZresEtArAynoMUXqNmdSsqw/640?wx_fmt=png)

获取的是一个AgentRequestHandler，然后会去调用`AgentRequestHandler.process()`解析、验证传入的XML数据，如果传入的 xml 请求包含名为`requester`的属性，则其数据将被 base64 解码并设置为名为`Requester`的属性

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSVkcaTkRAQv5de5aP1SnYvtOJJdDqmg3c8iaXzYY9ical5zq2t4l5UeibIuEC2tuBagEVwmnWlH2XmA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSVkcaTkRAQv5de5aP1SnYvS3YVicwBrgm2wZVbSV9DQRXqlv44eNlP5IxSpgicwAunUdtY9FO255Zw/640?wx_fmt=png)

接着，PBLFlowManager.handleBaseEvent() 将继续...