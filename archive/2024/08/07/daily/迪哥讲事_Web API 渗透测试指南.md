---
title: Web API 渗透测试指南
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495465&idx=1&sn=da54f074c1545923764458c7c02b8b87&chksm=e8a5e54adfd26c5ceda107deb79ebc5b58853aba0ef90a49f6dbee49764449c4c14762e2b80d&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-07
fetch_date: 2025-10-06T18:04:54.275365
---

# Web API 渗透测试指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6TLcqrDVrELSlibiaBTIpyV1meqxkMGJTFMlicDNPsKoqvY0QNOSLngaNVuyxyTaicMoibrNlNnicgwZaQ/0?wx_fmt=jpeg)

# Web API 渗透测试指南

迪哥讲事

以下文章来源于Hack All Sec
，作者Hack All

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5s3ZRBYQa0A234O10brMpTXETodZLOpwpfApdGMiceMTQ/0)

**Hack All Sec**
.

专注于网络安全，渗透测试，文章和工具分享，包括但不限于Web安全、物联网安全、车联网安全，我们的目标是Hack All！

# **概述**

API（Application Programming Interface，应用程序编程接口）是一个允许不同软件应用程序之间进行通信和数据交换的接口。API定义了一组规则和协议，软件开发者可以使用这些规则和协议来访问操作系统、库、服务或其他应用程序的功能。

## **[****API的基本概念****]**

**接口（Interface）**:

* API提供了一组公开的方法和端点，供外部系统调用。
* 这些方法和端点通常通过URL、函数名或服务名称来表示。

**请求和响应（Request and Response）**:

* 客户端向API发送请求，请求中包含所需的操作和相关数据。
* 服务器处理请求并返回响应，响应中包含操作结果和数据。

**协议（Protocol）**:

* API使用特定的协议来通信，常见的协议包括HTTP、HTTPS、FTP等。
* 例如，基于HTTP协议的API通过HTTP请求和响应进行通信。

**数据格式（Data Format）**:

* API请求和响应的数据通常以标准格式表示，常见的格式包括JSON、XML、CSV等。
* JSON是最常用的数据格式，因为它轻量级且易于解析。

## **[****API的作用****]**

**数据访问**:

* 提供一种访问应用程序或服务中数据的方式。
* 例如，数据库API允许应用程序访问和操作数据库中的数据。

**功能调用**:

* 允许应用程序调用另一程序的功能或服务。
* 例如，支付API允许应用程序集成支付功能。

**系统集成**:

* 实现不同系统或服务之间的集成和互操作。
* 例如，社交媒体API允许应用程序发布内容到社交媒体平台。

## **[****API的类型****]**

**Web API**:

* 通过HTTP协议进行通信的API，常用于Web服务和应用程序。
* 例如，RESTful API、GraphQL API。

**库和框架API**:

* 提供特定编程语言或框架功能的API，供开发者在应用程序中使用。
* 例如，Java API、Python标准库。

**操作系统API**:

* 提供操作系统功能访问的API。
* 例如，Windows API、POSIX API。

**远程API**:

* 允许在网络上远程访问服务的API。
* 例如，SOAP API、XML-RPC API。

常用的Web API有：

| API类型 | 描述 | 优点 | 适用场景 |
| --- | --- | --- | --- |
| RESTful API | REST是一种软件架构风格，用于设计网络应用程序。RESTful是基于HTTP协议的遵循REST的**API风格**。使用标准HTTP方法操作资源，数据格式常为JSON或XML。 | 扩展性好、可维护性强 | 大多数Web服务和应用程序 |
| GraphQL API | GraphQL是一种用于API的**查询语言**，由Facebook在2015年开源。GraphQL API是使用GraphQL查询语言和运行时构建的API。允许客户端指定所需数据的精确结构，通过**单个端点（URL）**处理复杂查询。 | 高灵活性、高效率 | 复杂查询、减少数据过多或不足的问题 |
| gRPC API | gRPC是由Google开发的一个高性能、开源的远程过程调用（RPC）框架，使用HTTP/2进行通信，并通过Protocol Buffers（protobuf）进行数据序列化。gRPC API是使用gRPC框架构建的API。 | 低延迟、高吞吐量 | 需要高性能和高效通信的系统 |
| JSON-RPC API | 使用JSON格式进行编码的RPC协议，通过HTTP或WebSocket通信，支持双向通信。 | 轻量级、实时应用 | 简单、轻量级API，实时应用 |
| SOAP API | SOAP（Simple Object Access Protocol，简单对象访问协议）是一种基于XML的协议，用于在网络上交换结构化信息。SOAP API是基于SOAP协议实现的API。 | 高级安全性、事务支持 | 企业级应用、需要高级功能的系统 |
| OData API | OData（Open Data Protocol）是用于查询和更新数据的协议，基于REST架构，提供标准化的数据访问接口。OData API是使用此协议实现的API。 | 简化CRUD操作 | 企业数据集成和共享 |
| HATEOAS API | HATEOAS（Hypermedia as the Engine of Application State）是一种RESTful API设计原则，HATEOAS的核心思想是通过超媒体（例如链接）将客户端引导到可以进行的下一步操作，而不是依赖于硬编码的URL或其他客户端。 | 增强自描述性和导航性 | 复杂系统的自发现和自适应 |
| WebSub API | WebSub（以前称为 PubSubHubbub）是一种用于Web上实现实时通知和推送更新的协议。它基于发布/订阅（Pub/Sub）模式，使得发布者可以将更新推送到订阅者，而不需要订阅者不断轮询发布者获取更新。 | 低延迟通知 | RSS/Atom feed的实时更新 |
| Falcor API | Falcor 是一个用于构建高效数据获取和管理的 JavaScript 库，由 Netflix 开发。它提供了一种简化的数据访问模型，使客户端能够通过统一的 API 请求所需的数据，并处理复杂的数据获取逻辑。 | 高效数据传输、灵活查询 | 需要高效数据传输和灵活查询的应用 |
| XML-RPC API | XML-RPC 是一种简单的远程过程调用（RPC）协议，它使用 XML 作为数据编码格式，通过 HTTP 协议进行通信。 | 简单、易于实现 | 需要与老旧系统或不同平台互操作的应用 |
| WSDL API | WSDL（Web Services Description Language）是一种用于描述 Web 服务的标准格式。它基于 XML，定义了 Web 服务的接口，包括可用的方法、参数、返回值及其数据类型。 | 标准化描述和发现Web服务 | 企业级应用、需要标准化描述的系统 |

**Web API 渗透测试**

## **[****测试工具****]**

* 拦截数据包：Burp Suite等
* 构造API请求：Postman、Apifox、Apipost等
* 扫描工具：Owasp Zap、Awvs、Xray等

## **[****信息收集****]**

信息收集是 Web API 渗透测试的重要步骤，无论是黑盒测试还是白盒测试，都需要系统地收集相关信息。在白盒测试中，测试人员可以直接获取API文档和代码等详细信息。在黑盒测试中，测试人员无法直接获取API文档，代码等资源，只能从外部自行收集。以下是API信息收集的方法：

**1. 目录扫描**

* 大多数Web API位于网站`/api/`、`/v1/api/`、`/v2/api/`等目录中，通过目录扫描可以发现
* 使用Burp Suite主动扫描和被动扫描也不错
* 使用Xray被动扫描也不错

**2. 网络流量分析**

* 有些系统的API和Web应用的端口是独立的，但是只要有交互通过分析流量就可以获取API接口，如Burp Proxy组件记录、浏览器开发者工具网络组件
* 有些API会写在经过混淆后的Javascript文件中，无法直接获取，可以使用此方法

**3. 使用互联网资源**

* 通过Github查询开源系统是否存在API及API目录和文档等
* 通过Google、Shodan、Censys、Fofa等搜索引擎搜索

收集到API接口信息后，可以分析API的目录结构、接口命名规则、参数命名规则、功能和业务逻辑等，根据这些信息可以进行接口枚举和参数枚举。

## **[****漏洞检测****]**

其实针对Web API的渗透测试和Web应用的渗透测试差不多，不过通常API的功能可能没有Web应用那么多，涉及的测试项较少：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficXHyjKMZiaAodEucF4PRnIh7ic66oQwESz2JVIn2B5iacx9Htnkqkluwiag/640?wx_fmt=png&from=appmsg)

| 测试项 | 测试方法 |
| --- | --- |
| 接口枚举 | 根据接口命名规则进行枚举，获取一些隐藏接口，如当前用户无权限或暂时未使用到的接口 |
| 参数枚举 | 根据参数命名规则可以枚举接口的隐藏参数或隐藏接口的参数 |
| 敏感信息泄露 | 响应中是否返回明文或Base64等可恢复明文的编码技术编码后的密码、密钥等 |
| SQL注入 | 对参数进行SQL注入测试，手工测试或使用sqlmap等工具，通常盲注多一些 |
| XSS | 构造XSS Payload对参数进行测试，检查响应是否包含未过滤或未转义的XSS数据 |
| 命令注入 | 对参数进行命令注入测试，检查是否可以注入成功，通常无回显 |
| SSRF | 构造SSRF Payload对参数进行测试，检查是否存在SSRF漏洞 |
| 任意文件读取/下载 | 对文件内容读取或下载的接口进行测试，检查是否存在漏洞 |
| 任意文件上传 | 对文件上传功能进行测试，检查是否可以上传任意文件或绕过限制上传其它文件 |
| 路径穿越 | 对文件读取、下载、上传等功能的接口进行路径穿越测试，检查是否未可以造成路径穿越 |
| XXE | 对传递的数据为XML数据的API接口参数中注入XXE Payload，检查是否存在XXE漏洞 |
| 反序列化 | 对于Json类型API接口，构造畸形Json数据，检查响应是否包含fastjson等组件名称和版本信息，进一步检测是否存在反序列化漏洞 |
| CRLF注入 | 查看参数是否被添加到HTTP响应中，构造包含CRLF的数据尝试注入HTTP响应头 |
| 错误信息泄露 | 通过在参数中插入特殊字符、访问不存在的API接口或构造畸形数据使服务端返回错误响应，查看报错信息中是否包含服务器代码信息、数据库连接信息、SQL语句、框架和组件信息或者敏感文件的路径等信息。 |
| 拒绝服务 | 构造超长字符串对Header或参数进行测试，检测服务器是否拒绝服务 |
| 用户名枚举 | 使用用户名密码登录失败是否提示“用户不存在”等信息 |
| 暴力破解 | 检查是否有锁定机制，或防重放机制，防止暴力破解 |
| 令牌伪造 | 检查令牌随机性，是否容易伪造，是否使用JWT弱密码等 |
| 令牌有效期过长 | 检查令牌是否长时间（超过2小时）有效 |
| 令牌重用 | 会话注销后，检查令牌是否仍然可以重复使用 |
| MFA绕过 | 删除或修改多因素认证步骤中的部分数据包，检查是否可以绕过多因素认证 |
| 任意密码修改/重置 | 检查密码修改/重置机制的安全性，是否可以绕过认证修改/重置任意用户密码 |
| 未授权访问 | 删除令牌后，检查是否仍然可以访问需要授权的资源 |
| 不安全的直接对象引用 (IDOR) | 通过直接引用对象 ID 来访问未授权的数据 |
| 业务流程跨越 | 绕过正常的业务流程，查看是否存在漏洞 |
| 越权 | 修改请求参数的用户ID或角色ID，检查是否可以越权访问其他用户信息或高权限资源 |

**[****实战案例****]**

### 接口枚举

根据响应状态或响应提示判断存在的接口和不存在的接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLfic8XetdO7HgjplGhdOhTzKFpkdEDQWqdEM8erx0aH94HZgjWoRWytnoQ/640?wx_fmt=png&from=appmsg)

### 参数枚举

根据响应提示判断参数是否存在。如参数不存在时响应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficoVfqSzicjrIMgh0MI8NXpGVfOGKDP3F7xBJOjVQbNZDHBia1qXM5ja1Q/640?wx_fmt=png&from=appmsg)

参数存在时响应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficybmoSHUiaAvHWjicKKfBn1hIr2cHsR6A7YvUZc6fiagjmESLuSOBjiboFw/640?wx_fmt=png&from=appmsg)

### 用户名枚举

用户名不存在时响应:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLfickZXsjn95OfXntekrR8HxtxK9xVEflR0xH111ia3ZnXgf4brqJWEtFIg/640?wx_fmt=png&from=appmsg)

用户名存在时响应：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficVgZMYh0Dick8CDB1HAiaxAxFkHqRvt1PUDQwCKDFNuvTOXBcB0gteNew/640?wx_fmt=png&from=appmsg)

### 暴力破解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficKlv6Eksd9YkSibxDP71iadriaCPJIwNJLicJJoTtd3mAy9RgF2AkoVg29Q/640?wx_fmt=png&from=appmsg)

### 错误信息泄露

错误信息中包含物理路径、后端语言、CMS等信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficJicAgBib4hECh1YcAXubtdnp41VnuArcaPLHngstg89esAj9rTtyVqzg/640?wx_fmt=png&from=appmsg)

### CRLF注入

参数添加到了响应头：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLfic1jdibffUs6iaUuyxxgCiatnY85DGhaoYia5ngPiaiakvpgiajibMCV7ekgN4qw/640?wx_fmt=png&from=appmsg)

利用CRLF注入进行XSS攻击：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficwbmDr3gXY2z8tUpIllV3IaofR8fz1D49EYuQQzuwv02ePvdY5AtAGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/s7bObPUU0RTxet89OhmFYmPY3asPCLficBVSBXufwHmO5x55BgGYQOXM9938BZw2Rp4jic9HFibuFNeoOnXNjIB7A/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3d...