---
title: 前后端分离渗透实战：当API成为盲区，你还在扫目录？
url: https://mp.weixin.qq.com/s/Wc107OOrtBj3WFf3vSe6uQ
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:32:50.334118
---

# 前后端分离渗透实战：当API成为盲区，你还在扫目录？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3oR6eMARh6zSPQ6t0torzZ6x3tLcwibmX05W73NFiaWQQGway4gwFfzytVlNUGgyNWqZzk3AaTfUI0jpnianIPBI7C7u8oKeR88sI0zqhPNK5E/0?wx_fmt=jpeg)

# 前后端分离渗透实战：当API成为盲区，你还在扫目录？

原创

逍遥
逍遥

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年3月，安全研究员对Bambuddy开源项目进行测试时，发现了一个典型的“前后端分离致死链”。他首先在源码里找到了硬编码的JWT签名密钥，然后用这个密钥伪造了管理员令牌。但最致命的是——当他尝试不带任何认证头访问API时，发现大量端点根本没有校验Token，直接返回了完整的用户数据。

这就是前后端分离渗透的核心矛盾：后端API成为了盲区，而大多数测试方法仍然停留在“扫Web目录、测表单注入”的旧范式上。

本文将2026年实战中验证过的前后端分离渗透方法完整拆开——从信息收集、认证绕过、授权突破到供应链风险，每条链路都附真实CVE和脱敏案例。

**第一章：前后端分离的核心攻击面——信任被前移到了最危险的边界**

传统Web应用，后端渲染页面时天然附带CSRF Token、服务端Session、同源策略。前后端分离后，前端只是展示层，后端API独立运行、跨域通信、无状态认证。很多API接口根本没做鉴权，只要知道路由格式，直接发请求就能拿到数据。

这种架构的本质是“信任前移”——后端不再验证请求来源，只认Token。而前端代码完全暴露在浏览器里，里面藏着的API路由、认证逻辑、甚至密钥，全都可以被攻击者拿到。

**第二章：信息收集——从前端源码到API全景图**

**JS逆向：几行脚本挖出隐藏API和云密钥**

前后端分离的SPA应用，所有路由、API端点、甚至认证逻辑都在JS里。核心技巧是在浏览器Sources面板搜索`accessKey`、`secretKey`、`token`、`password`、`/api/`等关键字。

常见暴露模式：云服务密钥硬编码（阿里云OSS的AccessKey在JS里明文可见，攻击者拿到后可接管整个云资源）；隐藏管理接口（前端路由里藏着`/admin/api/exportUsers`等路径，后端可能根本没做权限校验）；版本信息泄露（JS文件名带hash如`app.8f3d2a.js`，结合Source Map可还原完整前端源码）。

**Swagger文档泄露：API的“使用说明书”被公开**

Swagger在前后端分离项目中几乎是标配，但生产环境经常忘记关。访问`/swagger-ui.html`、`/swagger/index.html`、`/api-docs`、`/v2/api-docs`、`/v3/api-docs`即可直接拿到完整API文档。

2026年4月的实战案例：某系统错误地将swagger-ui.html重定向至主页，但主页JS里暴露了后台管理的全部API接口。攻击者利用这些未授权API直接实现任意用户密码重置，成功登录管理系统。

某头部新能源车企的案例：Swagger文档暴露了`/v3/internal/ota/firmware/verify`接口，该接口可绕过JWT鉴权直接返回完整的S3预签名URL。

**GraphQL内省查询：一键获取完整数据库结构**

GraphQL的内省查询直接暴露了所有数据类型、字段、Query和Mutation。即使生产环境禁用内省，部分框架的WebSocket端点可能绕过中间件，仍可获取完整Schema。CVE-2026-32594：Parse Server的GraphQL WebSocket端点绕过了Express中间件链，无需认证即可内省查询并执行任意GraphQL操作。

**第三章：认证绕过——从Token伪造到接口裸奔**

**JWT七种攻击手法**

JWT是前后端分离API认证的主流方案，但实现缺陷极其常见。排名前七的攻击模式：

**1. 硬编码密钥。** 后端源码或公开文档里写死了JWT签名密钥，攻击者拿到后直接伪造任意用户Token。CVE-2026-25505（Bambuddy）：密钥`bambuddy-secret-key-change-in-production`硬编码在源码里，攻击者用Python一行代码即可伪造admin令牌。

**2. 算法混淆。** 把JWT头部的`alg`从RS256改成HS256，用服务器公钥作为对称密钥签名，即可伪造任意Token。

**3. alg: none。** 某些JWT库错误地接受了无签名算法。

**4. kid参数注入。** JWT头部的kid参数可被利用做路径遍历或SQL注入。

**5. JWKS欺骗。** 如果服务器从URL加载公钥，攻击者搭建自己的JWKS端点，用自签名密钥伪造Token。

**6. 敏感信息泄露。** JWT的payload仅Base64编码而非加密，可直接解码查看其中的密码、API密钥、内网IP。

**7. 弱密钥爆破。** JWT使用HS256但密钥极弱（如`secret`、`password`），可用hashcat暴力破解。

**API接口无认证——直接被跳过的“第一道防线”**

部分后端接口根本没接认证中间件，不需要任何Token就能直接调用。测试方法：截取API请求，删除所有认证头，重放观察返回。如果仍返回200和敏感数据，说明接口裸奔。

**第四章：授权突破——对象级授权的结构性漏洞**

**BOLA/IDOR：OWASP API安全第一名的漏洞**

前后端分离API里，BOLA是最普遍的高危漏洞。API用对象ID（数字或UUID）访问资源，但后端从不验证“这个资源是不是属于你”。测试方法：用账号A登录，访问`GET /api/users/1001/orders`拿到自己的订单，然后把1001改成1002、1003继续访问。如果返回了其他人的数据，就是水平越权。

2026年典型CVE：Open WebUI的知识库检索API只校验了`user-memory-*`和`file-*`前缀，但知识库使用UUID作为集合名，完全没有权限校验。任何认证用户只需知道一个知识库UUID，就能通过检索API读取任意私有知识库的全部内容。

Craft CMS的GraphQL地址解析器：一个低权限的GraphQL API Token，可以读取系统中所有用户的地址信息——包括全名、邮寄地址、组织名称、税号等PII数据。

不可遍历ID的UUID越权并非无法突破。攻击者可以从其他API响应中提取UUID列表（如搜索接口、公共页面），或利用错误信息泄露（如“用户XXX不存在”中暴露的有效ID），或在JS文件中直接找到硬编码的UUID。拿到UUID列表后，配合BOLA漏洞即可批量窃取数据。

**BFLA：功能级授权缺失——普通用户能调管理员接口**

BFLA允许低权限用户执行高权限操作。用管理员账号操作敏感功能（创建用户、修改配置），将请求中的Cookie或Token替换为普通用户的凭据，若操作仍然成功则存在功能级越权。

**Mass Assignment：批量赋值——把不该改的字段一起改了**

批量赋值漏洞是前后端分离架构的典型缺陷。后端框架将HTTP请求中的JSON参数直接映射到数据库模型，没有过滤哪些字段可以被修改。典型场景：`PUT /api/user/update`请求中包含`{"name":"新名字","role":"admin"}`——`role`字段本不应该被用户修改，但后端没有过滤，直接写入数据库。

测试方法：从API文档或JS源码中获取对象的完整字段列表，在常规更新请求中添加敏感字段（如`role`、`isAdmin`、`balance`），观察是否被成功赋值。

**第五章：CORS、SSRF与数据导出——边界防御的盲区**

**CORS配置错误**

前后端分离需要后端配置CORS来允许跨域请求。典型的致命配置：`Access-Control-Allow-Origin: *`配合`Access-Control-Allow-Credentials: true`——允许任意域携带Cookie发起请求，攻击者构造恶意页面窃取用户数据。

CVE-2026-28792：TinaCMS同时存在`Access-Control-Allow-Origin: *`和路径穿越漏洞，攻击者只需诱导开发者访问一个恶意网站，即可在其本机枚举文件系统、写入任意文件、删除任意文件。CVSS评分9.7。

测试方法：发起一个带`Origin: https://evil.com`的跨域请求，观察响应头的`Access-Control-Allow-Origin`是返回了`*`还是具体`evil.com`，配合`Access-Control-Allow-Credentials`判断是否可被利用。

**API内网代理与SSRF**

前后端分离架构中，后端API经常充当内网代理，直接拼接用户输入的URL发起请求。`/api/proxy?url=xxx`、`/api/fetch?path=xxx`、`/api/webhook/test?url=xxx`这类接口是SSRF重灾区。利用这些接口可扫描内网、访问云元数据、攻击内部服务。

**CSV/Excel公式注入：前端输入，后端导出，管理员中招**

很多管理系统导出用户提交的数据（昵称、留言、反馈）为Excel或CSV文件。如果前端接收的输入未经处理就被写入导出文件，攻击者可以在输入中嵌入恶意公式。当管理员用Excel打开该文件时，`=cmd|'/c calc'!A0`这类公式就会在管理员本机执行任意命令。

2026年典型案例：hustoj在线评判系统（CVE-2026-23873），攻击者注册时将昵称设为`=cmd|'/c calc'!A0`，管理员导出比赛排名后打开Excel文件，公式被执行。MaxKB（CVE-2026-39424）的聊天导出功能将聊天记录中的公式字符直接写入.xlsx文件，管理员打开后触发任意代码执行。

防御很简单：导出数据时，在所有以`=`、`+`、`-`、`@`开头的单元格内容前加上单引号`'`。

**第六章：数据格式解析差异——绕过WAF与安全网关**

前后端分离架构中，JSON是主流传输格式，但正是JSON解析的灵活性带来了大量解析差异漏洞。

**JSON Key大小写绕过。** CVE-2026-27896：Go的`encoding/json`库默认大小写不敏感，`Method`和`method`都被接受。安全工具（WAF）严格遵循大小写敏感的JSON-RPC规范，只拦截`method`而不拦截`Method`。攻击者只需把JSON的key首字母大写，就能绕过整个WAF规则集。

**Null Byte注入实现Key覆盖。** segmentio/encoding存在Null Byte注入漏洞（GHSA-Q382-VC8Q-7JHJ）：攻击者在JSON key后追加`\u0000`字符（如`"method\u0000":"malicious"`），解析器认为这不是冲突key，但最终取值时覆盖了原始的`method`字段。安全过滤器看到的是第一个`method`，但后端执行的是被覆盖的恶意值。

**Content-Type切换绕过。** WAFFLED的研究揭示了更底层的攻击面：超过90%的生产环境网站同时接受`x-www-form-urlencoded`、`multipart/form-data`和`application/json`三种请求格式。攻击者用Content-Type切换重新编码同一个请求体，WAF解析器和后端框架使用不同的Content-Type解析逻辑，绕过效果极其稳定。

**第七章：自动化武器库**

**API端点发现：**

```
# JS文件中提取API端点grep -rE "(/api/|/v1/|/v2/|/graphql)" *.js | sort -u
# 提取隐藏路径grep -rE "(path|route|url)\s*:\s*['\"]/[^'\"]+['\"]" *.js
# GraphQL内省查询curl -X POST https://target.com/graphql -H "Content-Type: application/json" -d '{"query":"{__schema{types{name,fields{name}}}}"}'
# Kiterunner API路径爆破kr scan https://api.target.com -w routes-large.kite
```

**BOLA自动化检测：**

```
import requestsdef test_bola(base_url, endpoint, id_range, cookies_a, your_id):    vulnerable = []    for obj_id in id_range:        if str(obj_id) == str(your_id): continue        r = requests.get(f"{base_url}{endpoint}/{obj_id}", cookies=cookies_a, timeout=5)        if r.status_code == 200 and len(r.text) > 100:            print(f"[!!] BOLA漏洞：{endpoint}/{obj_id}")            vulnerable.append(obj_id)    return vulnerable
```

**第八章：防御维度——安全必须从API层重新设计**

前后端分离的安全防御必须在API层面进行重构：生产环境必须关闭Swagger UI和GraphQL内省查询，对所有API端点强制鉴权和对象级授权校验，导入第三方依赖时必须校验签名和完整性。API网关应拒绝包含`\u0000`的JSON payload，Content-Type应限制为业务实际使用的格式。所有用户输入在导出为Excel/CSV前，对公式触发字符（`=`、`+`、`-`、`@`）进行转义。JWT密钥不得硬编码在源码中，禁用`alg: none`，严格指定RS256或HS256算法。

**结语**

前后端分离没有创造新漏洞。BOLA/IDOR还是越权，Mass Assignment还是赋值缺陷，CORS还是跨域策略问题。但它让每一个老漏洞都换了新包装——变成了JSON body里的一个参数、JWT payload里的一个字段、JS文件里的一行注释。

当你不再扫Web目录，而是仔细阅读`app.js`里的每一行注释；当你不测试表单XSS，而是用Burp的Repeater直接向`/api/v1/`发JSON请求——前后端分离的真正攻击面才开始在你眼前展开。它不为传统的爬虫和扫描器开放，只向那些愿意静下心来读源码的人敞开。

**严正声明**

本文所有技术内容仅供安全从业者在获得被测试方明确书面授权的前提下进行安全评估和红队演练。所有CVE信息均来自公开披露的安全公告，所有案例均已脱敏处理。任何利用本文技术对未授权系统实施攻击的行为均属违法，与作者无关。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

昆仑AI安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

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