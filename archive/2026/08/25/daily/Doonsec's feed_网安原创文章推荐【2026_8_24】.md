---
title: 网安原创文章推荐【2026/8/24】
url: https://mp.weixin.qq.com/s/PCKzfbuPgKvgzZn8LUAQnQ
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:04:18.856319
---

# 网安原创文章推荐【2026/8/24】

# 网安原创文章推荐【2026/8/24】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 2026-08-24 微信公众号精选安全技术文章总览

> 洞见网安 2026-08-24

---

### 0x1 [把Linux伪装成苹果设备也可拿到Find My的共享位置数据](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451188227&idx=1&sn=0173111153eacfab13f8975dabda356b&scene=21#wechat_redirect "把Linux伪装成苹果设备也可拿到Find My的共享位置数据")

> 黑鸟 2026-08-24 23:28:24

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDowXn61LicKZCrGJ7wGPib7ZVVllFvSzYYdwZ5nA4AyhFJ9sUMH4X7JE9WvTkewiaZuesybKwWmfgorhZxUKMx0ia75tdJZan92Fhk/640?wx_fmt=jpeg)

本文介绍了安全研究员Zerotistic对苹果Find My People网络进行逆向工程的研究。Zerotistic成功地将一台Linux机器伪装成苹果设备，并获取了好友已授权共享的实时位置数据。这项研究并非用于追踪陌生人，而是基于好友已主动开放位置共享的前提。研究过程中，Zerotistic详细分析了苹果Find My的底层私有协议，并通过反编译和不断尝试，逐步解密并获取了位置数据。文章详细描述了整个过程的步骤，包括获取令牌、模拟苹果客户端、注册设备、监听消息、解密位置报告等。研究揭示了苹果Find My People的端到端加密协议的实现细节，并提醒用户位置共享的敏感性，建议用户谨慎授权。

逆向工程

移动安全

苹果iOS安全

加密技术

安全漏洞

安全研究

位置隐私

软件安全

---

### 0x2 [Apache Commons Collections 反序列化漏洞：从 Transformer 到调用链触发](https://mp.weixin.qq.com/s?__biz=MzkwMjQyMDA5Nw==&mid=2247485934&idx=1&sn=16141fea2a739b23b68dea91336899d9&scene=21#wechat_redirect "Apache Commons Collections 反序列化漏洞：从 Transformer 到调用链触发")

> Hack All Sec 2026-08-24 21:00:05

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DRxB6PWsueZT2mNbxZv90kJCTTRtCsgZb4WJhmYvfKJFl83FLSXfwy8sDBEfZQFJ7icic1QUZw0NxSNlsIttMZzaE9RiaFiaa3f4RMRjkP5RDRs/640?wx_fmt=jpeg)

1、从原生反序列化到 Commons Collections 调用链（CC链）\\x0d\\x0a2、Transformer 如何实现自动调用？\\x0d\\x0a3、InvokerTransformer 如何实现反射调用？\\x0d\\x0a4、ChainedTransformer 如何链式调用？\\x0d\\x0a5、怎么把这些 Gadget 链起来？

---

### 0x3 [ChainDrop npm 蠕虫分析：Runner 内存窃密、区块链 C2 与自传播](https://mp.weixin.qq.com/s?__biz=MzkyMjM0ODAwNg==&mid=2247489045&idx=1&sn=d95bd1ba61fc1f3467b8546024014cad&scene=21#wechat_redirect "ChainDrop npm 蠕虫分析：Runner 内存窃密、区块链 C2 与自传播")

> TIPFactory情报工厂 2026-08-24 20:20:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/UhfibIyPpmuPaPR2NLJUTibvrdFcDELIMeusdNWjug3jrHibJMmt9BocgtQcUO6bttEyWV4iciauZbyOfzicXIfU1DcibSdqK2tdYeQyJxKFCwd9z0/640?wx_fmt=jpeg)

ChainDrop npm 蠕虫通过投毒 npm 包的方式，将恶意代码植入其中，实现自动传播。该蠕虫能够在安装过程中悄无声息地执行，扫描并窃取开发者的敏感信息，包括云凭据、发布权限以及各种认证令牌。它能够在非 CI 环境中以后台进程运行，在 CI 环境中直接在 job 内执行。ChainDrop 能够通过多种方式传播，包括利用被盗的 npm token 进行自传播，以及通过 GitHub Actions 的 Runner.Worker 进程读取内存中的凭据。此外，它还具备将恶意代码作为 C2 路由器的能力，并通过 Ethereum 智能合约来动态更新其通信渠道。该蠕虫的检测和处置需要综合考虑多个方面，包括回滚 npm tag、检查相关文件和进程、轮换凭证以及使用可丢弃的 CI runner 等。

供应链攻击

内存窃密

区块链攻击

自传播

凭证窃取

持久化

混淆技术

自动化工具利用

开源软件安全

---

### 0x4 [重磅预警！点开邮件就中招！罗国APT TA488  “半点击”零日攻击爆发，换密码、重装电脑都清不掉后门](https://mp.weixin.qq.com/s?__biz=Mzg3OTYxODQxNg==&mid=2247488885&idx=1&sn=59e3e91f9c7e09eda0b537060f570428&scene=21#wechat_redirect "重磅预警！点开邮件就中招！罗国APT TA488 “半点击”零日攻击爆发，换密码、重装电脑都清不掉后门")

> AI紫队安全研究 2026-08-24 12:00:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/E3ZvvAXyiaiblCR89mHogpzBlCbicibcGffpv0DjypPKguJ3L1fBFRbiaKlglSajdU009Qmqwmibqx2wCAecySya0yiaEVwLgwX5TSCDFfEXg4oFcs/640?wx_fmt=jpeg)

本文由AI紫队安全研究发布，针对近期俄系间谍组织TA488（代号Void Blizzard/洗衣熊）大规模投放的新型邮件间谍攻击进行了详细分析。攻击者利用Exchange OWA零日漏洞CVE-2026-42897，通过“半点击”攻击方式，即用户只需打开或预览邮件，恶意脚本便会自动执行并植入自研隐形后门OWAReaper。文章介绍了攻击原理、漏洞细节、后门驻留手段、隐蔽的C2通道和数据窃取隧道，以及攻击目标和组织背景。文章还提供了企业紧急自查和修复操作清单，强调了企业应采取的安全措施，如安装补丁、排查受影响主机、边界防护拦截等，以应对这一网络安全威胁。

APT攻击

零日漏洞

半点击攻击

邮件钓鱼

后门植入

数据窃取

网络安全预警

企业安全

漏洞利用

---

### 0x5 [6层防御搭建实操：用Prompt Guard + Llama Guard + Garak给本地LLM穿上防弹衣](https://mp.weixin.qq.com/s?__biz=MzkwMzI5MzMxNA==&mid=2247485308&idx=2&sn=764ddde50035130926df60bbbc293f14&scene=21#wechat_redirect "6层防御搭建实操：用Prompt Guard + Llama Guard + Garak给本地LLM穿上防弹衣")

> 306Safe 2026-08-24 10:57:09

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N46S2sKsyIDNniaUZQvV4g5GNyI9RdwmrlogUSmQaXyD1Kkn97jDSicmG0ed1dPc19icH3BYc47gSU6AwXCFy0vbfvPD3HyQ0M7gr1Knm9JDr0/640?wx_fmt=jpeg)

本文详细介绍了针对 Prompt Injection（提示注入）威胁的 6 层防御体系，该威胁被列为 OWASP LLM Top 10（2026版）的第一位。文章首先强调了单一防御机制的不足，随后提出了多层次的纵深防御策略。L1 层使用正则表达式拦截已知攻击模式；L2 层部署 Prompt Guard 86M 模型检测注入和越狱尝试；L3 层通过系统提示词和指令层级标记区分指令与数据；L4 层使用 Llama Guard 3 8B 模型拦截有害输出；L5 层通过 Docker 沙箱和 Pydantic 限制工具权限；L6 层则引入人工审批机制确认高风险操作。文章还提供了详细的实操步骤和代码示例，并建议使用 Garak 进行红队扫描以验证防御效果。最后，文章总结了各层的防御作用和延迟，强调了持续红队扫描的重要性，指出没有银弹解决方案，但多层防御能将风险降至可接受水平。

Prompt Injection

LLM Security

Defense in Depth

Regular Expressions

Prompt Guard

Prompt Engineering

Output Filtering

Tool Sandboxing

Human-in-the-Loop

Red Team Testing

Redaction / PII Anonymization

---

### 0x6 [一个注册表单能创建管理员：WordPress 站点先停掉错误角色](https://mp.weixin.qq.com/s?__biz=MzI2ODU2MjM0OA==&mid=2247493194&idx=1&sn=7a4357b69387088286ae39436d8f31a5&scene=21#wechat_redirect "一个注册表单能创建管理员：WordPress 站点先停掉错误角色")

> 字节脉搏实验室 2026-08-24 10:50:16

![](https://mmbiz.qpic.cn/mmbiz_jpg/nOo5YmK1PHxWX08NsSCPy3yGtyeByxr4QiaHdUict70YWAfPiapST6CNMPRMh0YcDfdh9GIEehdY1Y3Og8bmjhAJQFz44mDOdK4ibKIQXNqztwU/640?wx_fmt=jpeg)

CVE-2026-13598影响RestrictMate 1.3.0之前版本，特定注册流程可能让未登录访客获得管理员角色。本文给网站负责人明确的止血、升级、账户核查与恢复信任顺序。

---

### 0x7 [GitLab 新漏洞进入披露窗口：升级前先回答谁能写入包注册表](https://mp.weixin.qq.com/s?__biz=MzI2ODU2MjM0OA==&mid=2247493194&idx=3&sn=01af85e8b57c373085c03deab3c539e9&scene=21#wechat_redirect "GitLab 新漏洞进入披露窗口：升级前先回答谁能写入包注册表")

> 字节脉搏实验室 2026-08-24 10:50:16

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nOo5YmK1PHyaSk9Pw4Ze4kfSBtUJs5pqUZSGVTgIC2BXEL5dDkllAiaeAibSq9k8qvfHYzJIVPCuj9LIOWHvBan35jdYDvc9LAjM3jMksgmOY/640?wx_fmt=jpeg)

本文分析了GitLab软件包注册表路径穿越漏洞（CVE-2026-10053）的风险和应对策略。该漏洞可能导致已登录用户实现远程代码执行，对企业安全构成威胁。文章强调了在升级前，企业需要评估哪些账号有权向哪些项目写包，以及这些项目连接的构建能力。文章提出了四步处置流程，包括评估实例版本、升级到安全版本、审查日志和收紧权限。同时，强调了在审计时要注意“能看到项目”和“能改变供应链”两种权限，以及不要仅查互联网入口。最后，文章建议企业应确保软件物料清单的质量，并补充资产视图中的发布者和解析环境信息。

漏洞披露

代码执行

企业安全

版本升级

身份权限管理

供应链安全

安全审计

事件响应

软件安全

---

### 0x8 [从一行注释到拿下整站：二阶 SQL 注入的暗黑艺术](https://mp.weixin.qq.com/s?__biz=MzIxODQzOTA5Mg==&mid=2247488243&idx=1&sn=1d3ae3c65c3e949cccb14a0043707bd0&scene=21#wechat_redirect "从一行注释到拿下整站：二阶 SQL 注入的暗黑艺术")

> 黑客网络安全 2026-08-24 08:38:03

![](https://mmbiz.qpic.cn/mmbiz_jpg/kIVkyn9uKmiccXhaEiaOMDy1ljNluAZziaaadhYoJ9TjSsVlmyUt1Fib0KnFvUgNesLJX3B4UXVyziaINqSFlkTpE6bNExhZibgMwfsCwSWAUIIicQ/640?wx_fmt=jpeg)

【声明】本文内容仅用于授权安全测试、漏洞研究与防御教育。未经授权对任何真实系统进行测试均属违法行为。

---

### 0x9 [当 WAF 沉睡时：DOM 型 XSS 的变异与 CSP 绕过实录](https://mp.weixin.qq.com/s?__biz=MzIxODQzOTA5Mg==&mid=2247488243&idx=2&sn=f0a09f71e99d58449846b794547da2b5&scene=21#wechat_redirect "当 WAF 沉睡时：DOM 型 XSS 的变异与 CSP 绕过实录")

> 黑客网络安全 2026-08-24 08:38:03

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kIVkyn9uKmicoFerg3Ef4NOoicbp4haibmNn4y4kK2wyXEpic0zr4S4auibLGQAdibKMAd0eDPOLOeOSdlj7MqibjT1uakbiaZibfgqln7o1tnlXiahS4/640?wx_fmt=jpeg)

本文深入探讨了现代Web前端安全中的复杂战场，包括DOM型XSS、变异XSS（mXSS）以及绕过内容安全策略（CSP）的技巧。文章从浏览器解析模型出发，分析了DOM XSS的发生机制和防御方法，如上下文敏感的转义和避免直接使用innerHTML、document.write、eval等。接着，文章介绍了mXSS的原理和防御策略，强调了在DOM层面进行过滤的重要性。对于CSP，文章指出其配置不当可能导致安全漏洞，并提供了绕过CSP的常见路径和防御建议。最后，文章强调了Trusted Types作为一种结构性防御措施的重要性，并总结了前端XSS防御的关键点，强调安全是一个需要持续维护的工程纪律。

Web Security

XSS (Cross-Site Scripting)

Content Security Policy (CSP)

WAF (Web Application Firewall)

Security Testing

Security Education

Browser Security

Security Best Practices

---

### 0xa [12KB后门把C2藏在desktop.ini空格里：KB Backdoor技术剖析](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621457&idx=4&sn=f99eee7b2bf0f050086b74c10126a609&scene=21#wechat_redirect "12KB后门把C2藏在desktop.ini空格里：KB Backdoor技术剖析")

> 黑白之道 2026-08-24 08:25:57

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6O4QSwfQUEvCfwrm7zkrEBy3r7M78BLPmmvUYibcv3iabiaxEWXGgx6KJxogOEKjeSRchvI0pGVTYIujia3vkcmCa1Tj6feKonVpxM/640?wx_fmt=jpeg)

导语：在狩猎WMI持久化异常时，安全研究人员在一台企业工作站上发现了一个极不寻常的后门程序。12KB

---

### 0xb [Intel TDX  MMIO 暗门](https://mp.weixin.qq.com/s?__biz=MzI3OTM3OTAyNw==&mid=2247486621&idx=1&sn=434ebdba81a9f79ab3a8a8db3b8d2373&scene=21#wechat_redirect "Intel TDX MMIO 暗门")

> Ghost Wolf Lab 2026-08-24 04:03:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/Yvub5gSYgRibsBPgwC9nibK85TuhR7bnnRzwoBdReFTOolc7OvVfhicRRr67TNY1NVehUetSTglW36Qo6J8nwzctMv5Slic96Wty96E38NDh55k/640?wx_fmt=jpeg)

本文分析了Intel TDX（Trust Domain Extensions）的安全漏洞。TDX旨在通过内存加密和测量技术为虚拟机提供硬件级隔离，以防止VMM攻击。然而，由于TD与VMM共享内存的设计，攻击者可以在TD访问共享页时，通过切换EPT映射实现L2地址劫持，从而绕过远程验证。文章详细描述了TDX的工作原理，包括信任域、EPT映射、MMIO共享通道等，并揭示了攻击者如何利用这些机制进行攻击。文章还讨论了攻击的时序控制、性能计数器监控等技巧，以及与TDX证明的脱节问题。最后，文章提出了检测与防御措施，如EPT变更检测、共享页的非对称...