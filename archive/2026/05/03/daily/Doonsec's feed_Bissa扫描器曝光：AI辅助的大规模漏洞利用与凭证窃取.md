---
title: Bissa扫描器曝光：AI辅助的大规模漏洞利用与凭证窃取
url: https://mp.weixin.qq.com/s/8YGRQb2Wy7SlxP5ZLRZMRw
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:27:04.409106
---

# Bissa扫描器曝光：AI辅助的大规模漏洞利用与凭证窃取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquPdsJ0oo6OWQDibbLdVwv5MhKLxq9TtROgdicyYrhykt2g7hPhjUlFDDKqzfBGhibdicJLr3TpdzYe0ETTFian4mrleaYulLofbjzLE/0?wx_fmt=jpeg)

# Bissa扫描器曝光：AI辅助的大规模漏洞利用与凭证窃取

梦鱼
梦鱼

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

安全研究人员发现一台暴露的错误配置服务器，揭开了一个代号为"Bissa"的自动化扫描攻击行动。攻击者利用 React2Shell漏洞（CVE-2025-55182）进行大规模扫描，成功入侵900+家公司，窃取数万个环境配置文件，涵盖AI、云服务、支付等核心凭证。更值得关注的是，攻击者使用 Claude Code 和 OpenClaw 等AI工具辅助工作，让整个攻击流程变得"正规化"。

一、关键发现•服务器被发现用于多目标漏洞利用、数据暂存、结果审查和访问验证，构成了完整的攻击链条•攻击者日常工作中深度依赖 Claude Code 和 OpenClaw，用AI写代码、调试扫描器、优化工作流•核心是利用 React2Shell漏洞（CVE-2025-55182）的大规模利用行动，扫描数百万目标，日志确认900+成功入侵•入侵后行动具有选择性，对窃取数据进行分级"诊疗"，主要精力集中在金融、加密货币和零售行业•窃取密钥是首要任务，env配置文件中包含AI、云服务、支付、数据库等凭证•服务器暴露了基于Telegram的告警和命令基础设施，直接指向背后操作者二、运作机制：工业化攻击服务器上有超过13000个文件，分布在150多个目录里，涉及漏洞利用、受害者数据暂存、凭证窃取和操作员工作流管理。攻击者用 Claude Code 理解和优化扫描器代码，用 OpenClaw 作为本地的AI控制界面，用于故障排除、流程编排和数据收集管道完善。整个 Bissa 扫描器是一个成熟、模块化的操作平台，支撑着一个有组织的行动，目标是在大规模获取访问权限的同时，将最高价值的结果"操作化"。

三、被盗"秘密"：AI和云凭证成重灾区窃取的凭证覆盖现代SaaS的每个层级，AI提供商相关的密钥成为数量最多的单一类别：类别 平台/服务AI平台 Anthropic, Google, OpenAI, Mistral, OpenRouter, Groq, Replicate, DeepSeek, HuggingFace云服务提供商 AWS, Cloudflare, Azure, Google Cloud / Firebase, DigitalOcean, Alchemy消息服务 Resend, Telegram, SendGrid, Twilio, Vonage, Postmark支付平台 Stripe, PayPal, Shopify, Square监控与分析 Sentry, Segment, Intercom, Mixpanel其他关键服务 Plaid(银行), Supabase/MongoDB(数据库), GitHub(代码), Auth0/Okta(身份), RevenueCat(移动收入), Fireblocks(加密货币托管), Slack(协作)一个 .env 文件泄露，可能意味着公司的AI能力、云基础设施、客户通讯渠道、支付网关和核心数据库全部沦陷。

四、受害者画像：金融与加密资产成焦点受害者A（税务咨询公司）：一家中型税务咨询和财务顾问公司。数据包包含：Plaid银行连接令牌、IRS税务记录、ACH转账记录、Twilio通话记录、Salesforce联系人，以及包含SSN和出生日期的客户案例数据。受害者B（数字资产公司）：一家大型数字资产、支付和企业金融公司。数据通过Oracle Fusion REST接口导出，涉及供应商、发票、采购订单、支付流程和银行账户数据。受害者C（薪资/HR平台）：一家中型薪资、人力资源和稳定币支付平台。数据包括薪资单、结算记录、Fireblocks加密货币托管集成信息，以及HRIS相关材料。目标非常明确，这些数据不是网站页面，而是直接能用来欺诈、勒索或了解企业内部财务状况的核心商业机密。

五、攻击者画像：独狼"Dr. Tube"Bissa扫描器里的脚本硬编码了一个Telegram机器人令牌，指向机器人 @bissapwned\_bot（显示名"BissaPwned"），目标聊天ID对应一个只有机器人和一个真人操作员的聊天室。操作员身份：操作员的公开Telegram身份是用户名 @BonJoviGoesHard，显示名字叫"Dr. Tube"。开源的OpenClaw日志中还提到了 @bissa\_scan\_bot 账号，说明 Dr. Tube 至少运行着两个专用机器人，分别负责扫描告警和AI控制子系统。

六、攻击能力：模块化与规模化扫描器核心是围绕 Next.js 的 React2Shell漏洞（CVE-2025-55182）构建的工作流。扫描器依赖两个关键文件：包含目标列表的"获取器"文件和定义漏洞利用类型的"租约"文件。目标列表从托管在 cs2.ip.thc.org 的ZIP压缩包中获得，分配CVE-2025-55182漏洞利用模块后部署载荷。载荷尝试枚举 .env 文件、云服务元数据、Kubernetes服务账户、本地凭证存储、数据库和Redis访问权限、加密货币钱包信息等高价值"秘密"。"confirmed hits"文件显示，超过900家公司通过这个工作流被成功入侵。扫描器还包括一个专门针对WordPress的模块，目标是CVE-2025-9501（W3 Total Cache插件未授权命令注入漏洞）。攻击者使用与S3兼容的 Filebase 服务作为受害者的 .env 文件的"场外归档库"。扫描器监控 results/ 目录，将 .env 文件批量打包成ZIP，上传到 Filebase 的 bissapromax 存储桶。Filebase存储桶历史显示三个阶段：2025年9月的bissa、2025年11月的bissa2、2025年12月至今的bissapromax。这些S3存储桶中的完整数据包包含400多个原始env-batch-\*.zip对象，涵盖超过30000个不同的 .env 文件名，时间跨度从2026年4月10日到4月21日。

七、防御建议•积极打补丁：：保持面向互联网的应用和框架处于快速更新节奏，别等安全事件发生才听说关键漏洞•密钥管理：当作秘密来管：将生产环境凭据从 .env 文件移到真正的密钥管理器，运行时注入，缩短密钥有效期•缩小爆炸半径：径：使用工作负载身份代替长期密钥，加固云服务元数据访问控制，收紧RBAC，禁用未使用的服务账户令牌•控制出站流量：量：将应用层出站流量路由到有日志记录的代理服务器，阻止静默访问云服务或攻击者基础设施•定期轮换检测：检测：定期轮换凭证，扫描源代码和构建产物里的嵌入密钥，布置"蜜罐令牌"监控泄露•演练响应流程：程：清楚哪些密钥能几分钟内轮换、哪些需几天，确保供应商联系人有效，每年做一次密钥泄露桌面推演执法部门已介入，所有主要受害者都已收到直接通知，协调披露和受害者通知工作正在进行中。

声明：本文仅供技术研究与安全加固参考，请勿用于非法用途。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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