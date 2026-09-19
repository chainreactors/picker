---
title: 浅谈API安全
url: https://mp.weixin.qq.com/s/vpZxK91HQp0W3QWIE9OP4Q
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:56:11.641942
---

# 浅谈API安全

# 浅谈API安全

搜狐安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/tD6Xsicic7CBic2juibZhNKsic15Io2s7S9FnjztLW5uhI7EpGiaRAR2xwGPmqoTsER2LV4RcX3N2qJDXQAvnmYzvZdQ/640?wx_fmt=png)

引言

![](https://mmbiz.qpic.cn/mmbiz_png/oMhY28hE0NDebWDV9vG2iagAybWTzM7kS9W2dToqSnktZgjtEowvsiau26W5iabV3mSvEEZbhr4ZGmhbVyLosjNIQ/640?wx_fmt=png)

应用程序编程接口（API）已成为现代应用的基石。从银行、零售到物联网、自动驾驶，API是移动应用、SaaS和Web应用的关键组成部分。如今，API更是大模型（LLM）与AI智能体（Agent）落地的"神经系统"。然而，API天然暴露应用逻辑和敏感数据，这使其日益成为攻击者的首要目标。

现实数据触目惊心：

• 据Salt Security《State of API Security Report Q1 2025》，99%的组织在过去12个月遭遇过API安全问题，95%的API攻击来自"已通过认证"的来源，98%的攻击尝试针对对外暴露的API——仅靠认证的传统防线已经失效。

• Akamai统计，2023年1月至2024年6月全球记录在案的API攻击达1080亿次；Imperva《2025 Bad Bot Report》显示，自动化流量首次超过人类流量（占51%），其中44%的高级机器人流量定向攻击API。

• 亚太地区企业因API安全事件造成的平均财务损失超过58万美元（Akamai 2025年研究）；而据Akamai 2026年最新研究，这一数字已飙升至超过100万美元，涨幅约72%——其中43%的受访企业遭遇了与AI技术相关的API攻击，但仅22%的企业完全掌握自己的API资产。

OWASP（开放Web应用安全项目）发布的《API Security Top 10》系统梳理了API面临的最关键安全风险，其中对象级授权失效（BOLA）连续两版蝉联榜首。Salt Labs数据显示，80%的API攻击手法都能对应到OWASP API Security Top 10，其中安全配置错误占观察到的攻击的54%，BOLA占27%。理解API类型及其各自的安全漏洞，是构建安全防护体系的第一步。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

API类型及漏洞

1

REST API常见漏洞

REST API概述：REST（Representational State Transfer）是基于HTTP协议的API设计风格，通过URL定位资源，使用GET、POST、PUT、DELETE等标准HTTP方法操作资源。因其简单、灵活、可缓存，REST是目前使用最广泛的API类型。

REST API常见漏洞：

1. 对象级授权失效（BOLA/IDOR）：OWASP API Security Top 10排名第一的风险。REST API通过URL中的对象ID（如/api/users/123）标识资源，若未验证当前用户是否有权访问该对象，攻击者只需修改ID即可越权访问他人数据。

2. 身份验证失效：JWT令牌未设置过期时间、使用弱密钥、登录接口无限流等。

3. 批量分配：攻击者在请求中提交不应被修改的字段，如通过提交{"role": "admin"}提升权限。

4. 安全配置错误：CORS策略配置为\*、生产环境启用调试接口、错误信息暴露堆栈等。

5. 注入攻击：SQL注入、NoSQL注入等。

安全建议：

1. 对每一个对象访问请求实施所有权校验，不信任客户端提供的任何ID；

2. 使用短生命周期的OAuth2/OIDC令牌替代长期静态API密钥；

3. 对可接受的属性进行白名单校验，使用严格的DTO（数据传输对象）；

4. 实施每客户端速率限制，设置合理的超时和请求体大小限制；

5. 使用UUID替代连续数字ID作为外部标识符；

6. 将合作伙伴/渠道API纳入与公开API同等级别的授权管控。

2

GraphQL API常见漏洞

GraphQL概述：GraphQL是一种API查询语言，允许客户端精确指定所需数据，避免过度获取或获取不足。所有请求通常只通过一个端点（如/graphql），查询灵活但复杂度高。

GraphQL API常见漏洞：

1. 内省查询滥用：GraphQL默认开启内省功能，允许客户端通过\_\_schema查询获取完整API schema。攻击者可借此一键导出全部数据模型。若未关闭此功能，相当于向攻击者提供了完整的API使用手册。

2. 字段级授权缺失：系统仅校验用户是否登录，未按角色划分字段访问权限，导致普通员工可读取高管、财务等私密数据。

3. 嵌套查询攻击（资源耗尽）：GraphQL支持多层嵌套关联查询，若无深度和复杂度限制，一次恶意嵌套查询即可耗尽服务器资源，造成拒绝服务。

4. 调试接口暴露：GraphiQL等调试面板在生产环境未关闭，相当于向攻击者公开了完整的API交互界面。

5. 信息泄露：GraphQL错误信息可能返回完整堆栈、字段提示和内部命名，持续泄露系统底层实现细节。

安全建议：

1. 生产环境彻底关闭GraphiQL等调试面板；

2. 关闭全局内省查询；

3. 实施字段级权限控制，区分前端和管理员两套独立Schema；

4. 设置查询深度限制和查询复杂度阈值；

5. 对Schema做脱敏处理，隐藏手机号、身份证号等敏感字段。

3

SOAP API常见漏洞

SOAP概述：SOAP（Simple Object Access Protocol）是基于XML的严格协议，内置WS-Security等企业级安全标准。结构严谨但相对复杂沉重，常用于金融系统、支付网关、企业级应用等对安全性和事务性要求极高的场景。

SOAP API常见漏洞：

1. XML外部实体注入（XXE）：SOAP基于XML传输，若XML解析器未正确配置，攻击者可通过外部实体引用读取服务器文件、发起内网请求（SSRF）。

2. 信息泄露：SOAP错误信息可能泄露过多细节。

3. 身份验证绕过：例如HID ActivID Appliance的JAX-WS SOAP API存在认证机制缺陷，未经身份验证的攻击者可窃取已登录管理员会话。

4. 业务逻辑缺陷：例如WSO2产品的账户恢复SOAP管理服务存在授权缺陷，攻击者可重置任意用户密码，实现账户接管。

5. 任意文件上传：SOAP管理服务中输入验证不当可导致任意文件上传，进而实现远程代码执行。

安全建议：

1. 禁用XML外部实体解析（如设置FEATURE\_SECURE\_PROCESSING并关闭DTD），防止XXE攻击；

2. 统一错误信息格式，避免泄露账户状态等细节；

3. 对SOAP管理服务实施严格的网络访问控制，限制仅可信来源可访问；

4. 实施严格的输入验证，特别是对SOAP管理服务中的用户输入；

5. 使用WS-Security等标准安全扩展强化认证与加密。

４

WebSocket API常见漏洞

WebSocket概述：WebSocket是一种全双工、持久化的通信协议，允许服务器主动向客户端推送消息，实现实时双向通信。常用于在线聊天、实时协作、游戏、金融行情推送、物联网设备监控等场景。

WebSocket API常见漏洞：

1. 跨站WebSocket劫持（CSWSH）：这是WebSocket最典型的安全威胁。若WebSocket握手时未验证Origin头，攻击者可诱使已认证用户访问恶意网站，从而以受害者身份建立WebSocket连接。

2. 会话标识可预测：WebSocket会话ID若可预测，攻击者可结合授权规则缺陷劫持他人会话。

3. 资源耗尽：WebSocket客户端若未对内存消耗设置上限，攻击者控制的服务器可导致客户端内存耗尽。

4. Header注入：WebSocket升级请求中的CRLF注入可导致请求走私、日志污染、认证头伪造等问题。

5. 消息体输入漏洞：WebSocket 传输的消息内容若未经过滤，仍可触发 SQL 注入、XSS、命令执行等传统 Web 漏洞，因为协议本身不负责内容安全 。

安全建议：

1. 在WebSocket握手时严格验证Origin头，仅允许可信来源；

2. 使用加密不可预测的会话标识符（如CSPRNG生成）；

3. 对WebSocket消息频率和大小实施限制；

4. 使用WSS（WebSocket over TLS/SSL）加密所有通信；

5. 实施消息内容校验，防止注入攻击。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**漏洞案例**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iacaRmHibfpib6RzzXpoJt7JgLMn2yzDTy5rmnoJeMeAF7tJdHGNOTjJQibrD6BHNqudib6BQwIV2ONsh9Xo3dtBdaQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

1

GraphQL 内省查询

![](https://mmbiz.qpic.cn/mmbiz_png/CjqZia4uEGNL1rurzMCWUPUAnP1PD4BLPK73ibu1PsmQwuPibjWSqibJOWc2Bz5ZECAgQNvysibOjW0VH0c9zDayBcw/640?wx_fmt=png)

GraphQL默认开启内省功能，允许客户端通过\_\_schema查询获取完整API schema。若未关闭此功能，相当于向攻击者提供了完整的API使用手册。如下图攻击者利用GraphQL内省查询获取整个 API 的数据模型、所有可用的查询、字段类型和参数等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1XjNzUonBicx6wwNx80rwhEypohyicprPeMXT6rVQggkuXjaN27p67SHkpbykqw4RfjsShVyUXwWUCjFf8gutsl20giaeSoTCWPtk/640?wx_fmt=png&from=appmsg)

２

REST API 越权漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/CjqZia4uEGNL1rurzMCWUPUAnP1PD4BLPK73ibu1PsmQwuPibjWSqibJOWc2Bz5ZECAgQNvysibOjW0VH0c9zDayBcw/640?wx_fmt=png)

REST API通过URL中的对象ID标识资源，若未验证当前用户是否有权访问该对象，攻击者只需修改ID即可越权访问他人数据。如下某系统存在越权漏洞，攻击者修改id越权获取其他用户的敏感信息（姓名、手机号、邮箱、身份证照片等）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1UjSXMqFLTURBPLEp5ILSsA30C4XQnicaJsy1rOOiau8dOIM8UkJbAvVYz8k9stzMkLEIhb7Dv6ibXRNIgGLrxTzgqxwxeWciaPKIQ/640?wx_fmt=png&from=appmsg)

３

SOAP XXE漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/CjqZia4uEGNL1rurzMCWUPUAnP1PD4BLPK73ibu1PsmQwuPibjWSqibJOWc2Bz5ZECAgQNvysibOjW0VH0c9zDayBcw/640?wx_fmt=png)

SOAP基于XML传输，若XML解析器未正确配置，攻击者可通过外部实体引用读取服务器文件、发起内网请求（SSRF）。如下图，利用SOAP接口的XXE漏洞发起内网探测请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1W8VKqlGibYUZXTCFT8muUNta923aDIu9gkverXrGAOFjB4lpaT3eWXwm8CKLD0n5P43xZB6ochpeCeY87Wf2cAOcJUtd1IibRjo/640?wx_fmt=png&from=appmsg)

４

WebSocket API XSS

![](https://mmbiz.qpic.cn/mmbiz_png/CjqZia4uEGNL1rurzMCWUPUAnP1PD4BLPK73ibu1PsmQwuPibjWSqibJOWc2Bz5ZECAgQNvysibOjW0VH0c9zDayBcw/640?wx_fmt=png)

WebSocket协议本身不负责内容安全，传输的消息内容若未经过滤，仍可触发 SQL 注入、XSS、命令执行等传统 Web 漏洞。如下在WebSocket传输的内容中注入HTML 标签，导致XSS漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1X1txjU87yBfwDbr5pBtWYBJTUUJs0WRqRSIaxGskjl1Iz78jroHMMJoxFlMicrH96Zib07hSvGa3TAP02dNKQamyk7vf3BqxZkI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1X8dA92N3Wciciaao374dMHJB93UuIibdnQd99KRFQkCGNSwIaep7AqOiastEECLPD6GyV7qdlGeNz084mY28rUpF2nIl5f3zOV6ib8/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/2Dkp7U8D8pM29mxCMDMwNrl5MC6Bia8clV6blVZ4X92GhoiaqDibkKjeuibkSeerbrVksRxaFFYUyic0O9icPKxuColQ/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

总结

API安全已不再是"锦上添花"，而是企业数据安全的生命线。纵观各类API的安全漏洞，几个共性问题反复出现：

第一，授权是一切安全的基础。BOLA（对象级授权失效）连续位居OWASP API安全风险榜首。无论是REST的IDOR、GraphQL的字段级越权，还是SOAP的业务逻辑缺陷、Schemata的租户隔离缺失，根源都在于"信任了客户端输入而未做服务端校验"。

第二，"影子API"和"僵尸API"是巨大的安全隐患。未记录的API、已废弃的API版本、生产环境中遗留的调试接口，往往缺乏维护和安全更新。Salt Security调查显示，仅15%的组织对自己API清单的准确性有充分信心，仅10%拥有API态势治理战略——而Akamai 2026年研究显示，仅22%的企业完全掌握自己的API资产。AI浪潮下，为LLM和Agent服务的API正在成为新的"影子资产"重灾区。

第三，API安全需要贯穿全生命周期。从设计阶段的威胁建模、开发阶段的代码审查与安全测试、部署阶段的配置加固，到运行阶段的持续监控与异常检测，每个环节都不可或缺。

第四，加密传输不容忽视。仍有相当比例面向客户的API未强制HTTPS。在明文传输面前，所有其他安全措施都形同虚设。

第五，AI正在重塑API威胁面。Akamai 2026年亚太研究显示，针对AI应用、AI Agent与LLM相关API的攻击已成为该地区最常见的API事件类型（43%）。

面对日益严峻的API安全威胁，应优先落实以下基础措施：建立完整的API资产清单并持续维护（含第三方API）、实施严格的认证与授权（OAuth 2.0/OIDC，并对合作伙伴API执行同等准入审查）、对所有输入进行白名单校验、按客户端与按业务流双重部署速率限制、强制HTTPS/WSS加密、关闭生产环境调试功能与内省、建立持续的监控与日志审计体系。API安全没有"银弹"，唯有构建纵深防御体系，才能在攻击者面前筑起坚实的防线。

END

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/O15JbwwWJFKlwVwAoOicgJNpUJZeX3iby3NricILYblPLFq9F16t8uNibNBuzqPCFicN84Wv0jEj69AUjIQQ8ygujKQ/0?wx_fmt=png)

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