---
title: 微软将三条 Salesforce 攻击路径与 ShinyHunters 一年的活动联系起来
url: https://mp.weixin.qq.com/s/CfNbH_ZV7nOgeUhW6C1PBg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:42:11.249182
---

# 微软将三条 Salesforce 攻击路径与 ShinyHunters 一年的活动联系起来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OAOCG6CicBYH2qRxSeqhUzwkhGKN0Du3qB3bjibDgKDlZxr0t13Ozia6zMhZmeygCO9iaWQZtJicAAaufntk0GyvHpZ0Hck7xGl25k/0?wx_fmt=jpeg)

# 微软将三条 Salesforce 攻击路径与 ShinyHunters 一年的活动联系起来

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

与数据勒索组织ShinyHunters使用相同方法的攻击者，在过去一年中，无需利用 Salesforce 平台的任何漏洞，就能入侵企业 Salesforce 环境。

进入该领域的途径是该组织已经给予的信任，通常是通过 OAuth 连接将 Salesforce 与其周围的应用程序和第三方供应商联系起来。

微软在7月13日发布的研究中，将这些从2025年中期持续到2026年中期的攻击活动归纳为三种不同的技术。此外，微软还与Salesforce合作，推出了新的检测和治理工具，旨在解决活动身份验证日志遗漏的问题。

正因如此，这种行为才难以被发现。当访问权限来自已授权连接应用的真实用户，或来自公司已信任的集成时，流量会被识别为正常使用，登录和身份验证监控几乎无法检测到。

重要的是应用程序或账户登录后会做什么，而这恰恰是大多数 Salesforce 日志记录功能并非旨在显示的。

微软将这些活动归纳为三种入侵路径：

* **通过语音钓鱼电话**诱骗员工批准恶意联网应用程序，
* 从被入侵的软件供应商处**窃取的 OAuth 令牌，以及**
* Salesforce 站点**访客访问权限配置错误。**

每一起事件都与 Salesforce 过去一年发生的一起事件相对应，微软表示，他们发现零售、教育和制造业等行业的租户都出现了这种活动。

## 电话

第一条路径是整个攻击活动的开端。从 2025 年年中开始，攻击者冒充 IT 支持人员拨打语音钓鱼（vishing）电话，诱导员工完成 Salesforce 的 OAuth 授权流程，最终让他们授权一个由攻击者控制的、伪装成 Salesforce 数据加载工具的联网应用程序。

一旦获得许可，该应用程序就可以以该用户的身份发出 API 调用，使攻击者能够枚举组织的 Salesforce 数据，持久访问 CRM 记录，并寻找可能打开通往其他 SaaS 平台大门的凭据。

没有恶意软件，不会重放被盗密码。只需一个电话和一个同意点击即可。

这是谷歌威胁情报小组 (GTIG) 和 Mandiant在 2025 年中期记录的攻击活动，追踪了初始访问（UNC6040）和后续勒索（UNC6240），两者都声称自己是 ShinyHunters，以加大对受害者的压力。

谷歌证实，其一个企业级 Salesforce 系统实例于 2025 年 6 月遭到攻击，攻击者窃取了大量公开的商业联系人数据，之后谷歌切断了连接。香奈儿和潘多拉的数据泄露事件也被公开提及，阿迪达斯、澳洲航空、安联人寿以及多家路威酩轩集团旗下品牌也被认为是攻击目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PjCXIHr92Wiar3zObeNcms9iaADEYtvkuHyhmEqo3iaTNiaTBPYXWVdvBZZOPWRcdXBvy09t5H96GictWiczDHpTs8fO3lSjxtKJQtM/640?wx_fmt=jpeg)

Mandiant 给防御者的建议很直白：这些电话利用了服务台乐于助人的本能，标准的身份检查通常不适用，安全的做法是挂断电话，然后通过已知的可靠渠道重新拨打。

## 从受信任的供应商处窃取的代币

第二种攻击路径完全绕过了员工。攻击者不去钓鱼用户，而是入侵第三方供应商，该供应商的应用程序已经拥有对其客户 Salesforce 组织的 OAuth 访问权限，窃取连接密钥或令牌，并利用它们一次性查询和导出多个下游实例中的数据。

由于流量来自已批准的集成，因此不会触发登录警报，并融入正常的自动化流程。

微软指出了三起事件。其中，2025 年 8 月的Salesloft Drift 漏洞事件规模最大，也最为明确：攻击者窃取了与 Drift AI 聊天集成相关的 OAuth 和刷新令牌，并将其用于攻击 Salesforce 客户环境。

谷歌估计，Drift 代币被盗事件可能危及 700 多家机构，其中包括 Cloudflare、Zscaler、Palo Alto Networks、Proofpoint、PagerDuty 和 Tanium。谷歌将该集群追踪为 UNC6395；Cloudflare 的 Cloudforce One 将其称为 GRUB1。

Salesloft 后来追溯到攻击者早在 2025 年 3 月就访问了其 GitHub 账户，并利用该账户入侵了 Drift 的 AWS 环境，窃取了令牌。攻击者的目标是获取机密信息，他们运行 SOQL 查询，筛选支持案例和其他对象，寻找 AWS 密钥、Snowflake 令牌和密码，然后删除查询作业，以阻碍调查人员的行动。

2025年11月，Gainsight事件也采用了类似的策略，但这次的攻击对象是另一家供应商。Salesforce在发现异常API活动后，下架了Gainsight发布的应用程序。GTIG随后将此次攻击活动与ShinyHunters的关联公司联系起来，涉及超过200个受影响的Salesforce实例。

ShinyHunters 背后的团队声称 Salesloft 和 Gainsight 的推广活动总共影响了近 1000 个组织，但这一数字尚未得到独立证实。

最近的案例发生在 2026 年 6 月，是Klue 系统遭到入侵。攻击者利用一个长期未使用但仍处于激活状态的旧凭证入侵了这个竞争情报平台。该凭证是之前从未部署过的测试集成遗留下来的。攻击者推送了一个代码更新，窃取了客户的 OAuth 令牌，并利用这些令牌访问了 Klue 客户（包括Huntress和 Recorded Future）的 Salesforce 和 Gong 数据。

微软将 Klue 的幕后黑手追踪为 Storm-3138。对于任何交叉核对报告的人来说，这里有一个命名上的疑点：包括 Huntress 和 Datadog 在内的大多数业内人士都将 Klue 勒索案与一个自称 Icarus 的组织联系起来，而一个自称 ShinyHunters 的 Telegram 帐户也声称对此负责。

这些标签变得模糊不清，因为这些身份相互重叠，并且会被人投机取巧地认领，这种情况在整个系列活动中都存在。

## 访客通道未关闭

第三种途径完全不需要任何凭证。微软发现针对 Salesforce Aura 端点（Experience Cloud 站点背后的框架）的可疑访客用户活动有所增加。在访客用户权限配置错误的情况下，攻击者无需身份验证即可访问 Aura 功能。

他们调用 GraphQL Aura 控制器，使用基于游标的分页功能，获取了超过标准 2,000 条记录查询限制的记录，获取的记录远远超过了访客角色应该公开的记录数。

微软的相关检测结果指向了用于探测这些端点的AuraInspector工具。此次攻击并未涉及任何漏洞利用。该组织赋予了访客角色超出其权限的访问权限，攻击者充分利用了这些信息。

## 微软和 Salesforce 推出了什么来应对这种情况

存在的信号存在于访问之后发生的事情中：哪个已连接的应用程序发出了调用，它持有哪些 OAuth 范围，它查询了多少，以及这些对于租户来说是否正常。

微软与 Salesforce 合作，在 Defender for Cloud Apps 中实现了这一功能。对于运行 Salesforce Shield 事件监控的客户，升级后的 Salesforce 连接器集成了实时事件监控框架，可实现近乎实时的检测，并增加了连接应用归因功能，将活动与特定应用身份及其授予的 OAuth 权限范围关联起来，同时还提供更多会话和 API 上下文信息。

除了检测功能外，微软还为连接的 OAuth 应用添加了姿态和治理功能：查看具有提升权限范围的高权限应用，查找已闲置 90 天或更长时间但仍保持有效权限的未使用应用，以及为每个应用提供 0 到 100 的风险评分，团队可以将其与警报和策略关联起来。

目标是在其他人之前找到那些权限过高且已被遗忘的集成。

## 缩小 OAuth 攻击面

微软的指导意见很实用，与供应商在每次事件发生后的说法一致：将 Salesforce 实例连接到 Defender for Cloud Apps 以获取额外的遥测数据，启用并实际查看 Salesforce 事件日志，并锁定 Experience Cloud 来宾用户的访问权限。

除了针对特定产品的步骤之外，持久有效的解决方案往往是常见的做法。清点已连接的应用，移除无人使用的应用，将剩余应用的权限范围限定在最小权限原则下，并在集成出现异常行为时立即撤销并轮换令牌。

这三条路径下的模式相同。过去十年里，大多数公司构建的身份控制机制都是针对人工登录的：多因素身份验证 (MFA)、条件访问控制和会话策略。而真正执行现代 Salesforce 技术栈中实际工作的 OAuth 应用、集成帐户和服务凭证，大多游离于所有这些机制之外，缺乏监管且权限过高。

攻击者利用这个漏洞运行了一年，而且不止一次，入侵的途径只不过是有人忘记关闭某个凭证而已。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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