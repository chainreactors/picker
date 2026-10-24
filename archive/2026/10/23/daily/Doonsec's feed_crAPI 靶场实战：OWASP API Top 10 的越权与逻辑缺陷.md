---
title: crAPI 靶场实战：OWASP API Top 10 的越权与逻辑缺陷
url: https://mp.weixin.qq.com/s/RnPJ2b8tUtfpwvOLH0Cunw
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:54.842885
---

# crAPI 靶场实战：OWASP API Top 10 的越权与逻辑缺陷

# crAPI 靶场实战：OWASP API Top 10 的越权与逻辑缺陷

运维安全入门
运维安全入门

运维安全入门

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前 11 篇里我们打的都是「单点靶标」：一个 Web 页面、一个漏洞、一个成因。但真实的互联网应用早就不长这样了。前端是 SPA，后端是 API 网关加一堆微服务，身份靠 JWT 传递，支付走回调，漏洞不再表现为一个报错页面，而是**一组业务接口的信任关系被滥用**。

这一章的主角是 **crAPI**（completely ridiculous API，OWASP 出品的「荒唐 API」）。它把 **OWASP API Security Top 10 2023** 里的每一类风险，都做成了一个可以在浏览器里亲手触发的业务场景。

**🛡️ 授权声明**　本文所有测试均在本地 Docker 环境中进行。对生产 API 开展安全测试必须取得书面授权，并明确测试账号、数据范围与时间窗口。

本文目录

1. crAPI 是什么：为什么传统扫描器对它几乎无效
2. 架构解剖：一个电商 API 的完整拓扑
3. 部署：Docker Compose 一条命令拉起
4. 核心机制：OWASP API Top 10 与靶场的映射关系
5. 实战一：BOLA 越权与批量 ID 遍历
6. 实战二：Broken Function Level Authorization
7. 实战三：JWT 密钥硬编码与算法篡改
8. 实战四：Mass Assignment 与属性注入
9. 实战五：支付绕过与业务逻辑重放
10. 排错清单
11. 防守与等保：API 安全的落地治理
12. 总结

## 01crAPI 是什么：为什么传统扫描器对它几乎无效

先说结论：**如果你的安全预算只够买一个 Web 扫描器，你大概率会在 crAPI 上颗粒无收。**

这不是扫描器不行，而是 API 安全的本质决定的。传统 Web 扫描的逻辑是「爬页面 → 发现参数 → 塞 Payload → 看报错」，而现代 API 的逻辑是**「带合法身份 → 换掉参数值 → 看返回了什么别人也能拿到的东西」**。后者的每一步请求都是「合法」的——状态码 200，没有 XSS 特征，没有 SQL 报错，只是返回的数据本不该属于你。

| 检测手段 | 对 crAPI 的效果 | 原因 |
| --- | --- | --- |
| 传统 Web 漏洞扫描 | 几乎无效 | 漏洞不在参数值里，而在对象归属与权限边界上 |
| CVE 特征匹配 | 无效 | 漏洞逻辑来自设计缺陷，没有可匹配的指纹 |
| 单一账号黑盒测试 | 漏报严重 | 正常功能对管理员账号完全正常 |
| 多角色差分测试 | 有效 | 同一接口在不同身份下返回结果不同即暴露问题 |
| 业务流回放 | 有效 | 支付、改密、发货等流程存在状态机缺陷 |

crAPI 的设计目的正是把这个结论变成肌肉记忆：**它几乎不给你「明显的」漏洞信号，却处处是越权与逻辑缺陷**。这与 Juice Shop 有共同点，但侧重点不同——Juice Shop 的重点是前端交互，crAPI 的重点是**接口契约**。

## 02架构解剖：一个电商 API 的完整拓扑

crAPI 的架构刻意做得「像真的」，因为只有像真的，你的测试方法才有迁移价值。它的核心是一个用 Spring Boot 写的电商后端，配套一个邮箱服务用于触发验证码类流程。

| 组件 | 作用 | 关键端口 | 实战中的意义 |
| --- | --- | --- | --- |
| API 主服务 | 用户、商品、订单、支付等全部接口 | 8888 | 主战场 |
| MailHog | 本地 SMTP 收信服务，捕获邮件 | 8025 | 截获验证码，验证认证流程缺陷 |
| 前端页面 | 驱动 API 的业务场景 | 同主服务 | 帮你理解业务流与参数含义 |
| 数据库 | 业务数据存储 | 内部 | 理解对象归属关系 |

注意 MailHog 这个组件——它是整个靶场的**叙事支点**。真实系统里「忘记密码」会发一封带六位验证码的邮件，攻击者的目标就是绕过这个验证码直接改密。而 MailHog 把邮件拦在本地，让测试者可以随意查看验证码，从而专注于观察**「验证码校验逻辑本身」是否可绕过**，而不是卡在收不到邮件上。

**💡 提示**　这个设计值得蓝队学习：在自己的测试环境里搭一个 MailHog，能把「验证码绕过」这类测试的效率提升一个数量级，同时避免真实邮箱被轰炸。

![crAPI 组件拓扑图：浏览器 → API 网关 → 微服务 → 数据库，MailHog 旁路接收邮件](https://mmbiz.qpic.cn/mmbiz_png/0l1UjZtX9tzPKRcNcfVVSfk51OAibP0dAcmVaQCfoRk137pP3p9ib2knhgchHI3F9RUrOhXUVo8Js9Yye3MdvKP7ib14XDgd45Fuia9ur6mSmsM/640?from=appmsg)

图：crAPI 组件拓扑图：浏览器 → API 网关 → 微服务 → 数据库，MailHog 旁路接收邮件

## 03部署：Docker Compose 一条命令拉起

crAPI 官方提供了 Docker 镜像与 compose 编排，部署难度是所有 OWASP 靶场里最低的一档。

crAPI 完整部署流程

```
# 1. 克隆仓库 git clone https://github.com/owasp/crAPI.git cd crAPI  # 2. 启动全部服务（首次会构建镜像，耗时较长） docker compose up -d  # 3. 确认服务状态 docker compose ps  # 4. 停止并清理 docker compose down
```

如果官方 compose 与你的 Compose V2 版本有兼容问题，常见的报错是端口绑定或网络定义解析失败。这时可以手动起服务，核心命令如下：

手动部署的兜底方案

```
# 单独启动 API 服务 docker build -t crapi-api:latest . docker run -d --name crapi-api -p 8888:8080 crapi-api:latest  # 单独启动 MailHog（捕获邮件） docker run -d --name mailhog -p 8025:8025 mailhog/mailhog
```

| 访问地址 | 用途 |
| --- | --- |
| http://localhost:8888 | API 主服务与前端页面 |
| http://localhost:8025 | MailHog 邮件查看界面 |

### 默认账号说明

crAPI 会预置若干演示账号，用来展示「不同角色看到不同世界」。这些账号的用途不是让你直接登录看答案，而是**让你做横向对比**：

* **admin**

  ：管理员，可见全部数据，权限最高。
* **普通用户**

  ：只能看到自己的订单与地址，权限受限。
* **另一个普通用户**

  ：与上一个用户数据完全不同，是验证越权的关键对照组。

**⚠️ 注意**　务必记住这三个角色的对照关系。API 越权测试的全部本质就是：**用 A 的身份，请求本应属于 B 的资源，看能不能拿到。**没有对照组，测试就退化成猜测。

## 04核心机制：OWASP API Top 10 与靶场的映射关系

OWASP API Security Top 10 2023 是当前 API 安全的通用语言。crAPI 的每个业务场景，几乎一一对应着其中一类风险。把这张映射表刻在脑子里，你面对任何一个陌生的 API 都能快速建立测试假设。

| 编号 | 风险名称 | crAPI 中的体现 |
| --- | --- | --- |
| API1 | Broken Object Level Authorization（BOLA） | 改 URL 里的商品/订单 ID 拿到别人的数据 |
| API2 | Broken Authentication | 重置密码流程中验证码校验缺失或可绕过 |
| API3 | Broken Object Property Level Authorization | 响应中包含用户无权看到的敏感字段 |
| API4 | Unrestricted Resource Consumption | 分页参数无限制，可一次拖垮服务 |
| API5 | Broken Function Level Authorization | 低权限账号调用管理员专属接口成功 |
| API6 | Unrestricted Access to Sensitive Business Flows | 批量下单、刷优惠等流程滥用 |
| API7 | Server Side Request Forgery | 处理图片/链接的接口拉取内网地址 |
| API8 | Security Misconfiguration | 接口文档、调试端点被直接暴露 |
| API9 | Improper Inventory Management | 遗留的旧版本 / 测试接口仍在线 |
| API10 | Unsafe Consumption of APIs | 第三方回调未验签，被伪造 |

![OWASP API Top 10 → crAPI 业务场景的对应关系图](https://mmbiz.qpic.cn/sz_mmbiz_png/0l1UjZtX9txZjjx5LbFJSmUVIhib7lGfj6vMdic7KnyLCYZX86UURWFPc5mX1xwJORXGSajmcfIia2ysOgJgMXS2SJ1qewoZJCdoE8bTVdpAbA/640?from=appmsg)

图：OWASP API Top 10 → crAPI 业务场景的对应关系图

值得注意的是，这份清单和前一阶段的 OWASP Web Top 10 有一个根本差异：**Web Top 10 里排第一的是注入类漏洞，API Top 10 里排第一的是访问控制**。这不是因为 API 没有注入问题，而是因为 API 的攻击面高度结构化，攻击者面对的是接口、对象和权限，而不是页面和参数。

## 05实战一：BOLA 越权与批量 ID 遍历

### 一、原理：BOLA 到底在破什么

BOLA（Broken Object Level Authorization）的中文是**「对象级授权失效」**。正常的业务逻辑应该是：「这个订单属于当前用户，他才看得到」。如果服务端只校验了「登录了吗」，而没有校验「这个订单是不是你的」，那么改一下订单号就能看到别人的订单。

BOLA 验证的最小操作序列

```
# 1. 用自己的账号登录，调用"我的订单"接口 GET /api/orders/me  → 返回 [{ "id": 1001, "user": "alice", ... }]  # 2. 直接把请求里的订单 ID 换成别人的 GET /api/orders/1002  → 若返回 alice 以外用户的数据，即为 BOLA  # 3. 低频遍历相邻 ID，观察归属变化 GET /api/orders/1003 GET /api/orders/1004 # 出现不同 user 字段即证明越权成功
```

### 二、为什么手动测试远胜于自动化

理论上你可以通过比较两个账号的响应差异来批量检测 BOLA，但在实际测试中，**「自己建立一个有效的对照组」往往比跑工具更快**。

一个更隐蔽的变体是**字段级越权**：接口返回了整个用户对象，其中包含手机号、邮箱、地址等字段，而接口设计者根本没打算把这些字段暴露给普通用户。这种 BOLA 的变体不会报错、不会越权到别人的数据，但它造成了**数据过度暴露**——这就是 API3 的典型场景。

**💡 提示**　检测字段级越权的技巧：拿普通用户的响应与管理员的响应做差分，多出来的字段就是「本不该给你看的数据」。这个差分方法在合规审计中同样极其有效，它能快速发现「接口响应模型未被精确定义」的问题。

## 06实战二：Broken Function Level Authorization

上一节破的是「横向越权」——你拿别人东西。这一节破的是「纵向越权」——你用小权限干大事。

典型场景：管理后台有个接口用于查询所有用户的订单，路径大概是 `/api/admin/users/orders`。如果服务端只在 UI 上隐藏了入口，而接口层没做角色校验，那么任何登录用户直接访问这个路径都能拿到全量数据。

纵向越权验证要点

```
# 登录普通用户账号后，直接请求管理员专属接口 GET /api/admin/users/orders Authorization: Bearer <普通用户的令牌>  # 若返回 200 且包含他人订单 → Function Level Authorization 失效  # 正确的响应应当是 401 或 403 # 实际项目中最常见的错误是返回 200 + {"error": "forbidden"} # 这依然是漏洞，因为数据可能已在服务端加载完成
```

这里有一个特别值得强调的细节，很多测评报告里都会忽略：**状态码正确不等于实现正确。**有些团队只在 Controller 层加了个异常抛出，但查询语句**已经把全量数据读进内存了**才抛出异常。从外部看是 403，从内部看是一次全表扫描。在资源受限或数据量巨大的场景下，这就是一次可被利用的 DoS 放大。

![横向越权（BOLA）与纵向越权（BFLA）的攻击面对照图](https://mmbiz.qpic.cn/mmbiz_png/0l1UjZtX9txepgYAzwky5dE8TRuST9o5bTnt98VSNBAib5ib2DQib6hkvicianNEjBdA0Yu9vb489UCH1ZqNmB0Iw9icI7pH2iby4icg5OgnpVPHPEU/640?from=appmsg)

图：横向越权（BOLA）与纵向越权（BFLA）的攻击面对照图

## 07实战三：JWT 密钥硬编码与算法篡改

crAPI 有意在 JWT 的处理上留下了教科书式的缺陷，这一节我们把它拆开讲，因为这是**密码学实战中「密钥管理」这一课的最好教材**。

### 一、JWT 的信任链

JWT 的安全性完全建立在一条假设上：**只有服务端持有签名密钥**。一旦签名密钥泄露或可预测，攻击者就能凭空造出任意身份令牌，所有基于 JWT 的授权全部失效。

JWT 三段结构与信任边界

```
# 典型结构：header.payload.signature # 先把 Authorization 头里的令牌粘出来看结构 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 .eyJzdWIiOiIxMjMiLCJyb2xlIjoiYWRtaW4ifQ .SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c  # 三段分别是：头部（算法）、载荷（声明）、签名  # 关键检查点： # 1) header 里的 alg 是什么？若是 "none" 或 HS256/HS512 混用，需要警惕 # 2) payload 里的 role/sub 是否可预测或可任意指定
```

### 二、三类典型缺陷

| 缺陷类型 | 具体表现 | 危害 | 修复方向 |
| --- | --- | --- | --- |
| 密钥硬编码 | 签名密钥写死在源码或配置文件中 | 任何人拿到代码即可伪造任意身份 | 密钥托管、定期轮换 |
| 算法混淆 | 服务端接受客户端指定的 alg，允许 none 或 RSA/HMAC 混用 | 签名被绕过 | 服务端固定算法白名单 |
| 声明不校验 | 直接信任 payload 中的 role 字段 | 普通用户提权为管理员 | 服务端解析并校验授权声明 |

### 三、无害化验证原则

涉及令牌的验证必须遵守一条铁律：**只在你自己的账号上做，不要修改或重放他人令牌。**即便如此，在授权测试中也应优先使用「解码 + 结构比对」而不是「尝试伪造有效令牌」，前者能提供等价证据，风险却低得多。

**💡 提示**　这里正好呼应你的密码学背景：JWT 的问题从来不是 SHA-256 有漏洞，**而是「密钥是怎么产生、存在哪、怎么轮换」这一串工程问题**。密码学原语的强度，抵不过一个放在 Git 仓库里的明文密钥。

## 08实战四：Mass Assignment 与属性注入

Mass Assignment（批量赋值）是 API 特有的经典漏洞。成因很朴素：后端把客户端传来的 JSON **整个对象绑定到数据库实体上**，而没有对字段做白名单限制。

Mass Assignment 的典型利用形态

```
# 正常请求：只提交该提交的字段 {   "username": "eve",   "address": "somewhere" }  # 攻击者追加一个本不该由客户端控制的字段 {   "username": "eve",   "address": "somewhere",   "role": "admin",          # 提权   "balance": 999999,        # 篡改业务数据   "id": 1                   # 覆盖主键 }  # 若服务端未做字段白名单，上述字段会被直接写入
```

这个漏洞的隐蔽性在于：所有请求在格式上都是合法的 JSON，服务端也不会报任何错。防守方的检测手段也相对弱——传统的漏洞扫描器不会知道 `balance` 字段本来就不该出现在请求体里。

对应的修复方案非常明确：**服务端对每个接口声明允许更新的字段白名单**，不在白名单内的字段一律丢弃。这个看似简单的约束，在等保测评中对应的是「应保证服务端对接收的数据进行合法性校验」这一条，但很多系统恰恰栽在「校验了格式，没校验语义」。

## 09实战五：支付绕过与业务逻辑重放

前四节都是「技术型」缺陷。这一节是最难自动化的一类：**业务逻辑漏洞**。

一个设计良好的支付流程本应是不可逆的状态机：「创建订单 → 待支付 → 已支付 → 已发货 → 已完成」。而漏洞往往出现在**状态机的边**上——比如允许已完成的订单被重新置为待支付，或者允许跳过「已支付」直接进入「已发货」。

* **价格篡改类**

  ：提交订单时价格由客户端指定，服务端未从商品库重新读取。
* **状态跳变类**

  ：直接调用「发货」接口，跳过了支付环节。
* **重放类*...