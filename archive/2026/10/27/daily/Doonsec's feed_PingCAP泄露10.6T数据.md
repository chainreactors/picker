---
title: PingCAP泄露10.6T数据
url: https://mp.weixin.qq.com/s/oZq2URohTckvj9lxvRu62w
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:45:13.900505
---

# PingCAP泄露10.6T数据

# PingCAP泄露10.6T数据

原创

泼猴
泼猴

表哥带我

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6OyYiaN1qHXJMw2iaibg64CpayGHw3RbkwTicgAvAT7wiaibiaa9D100tlGp2ibvUUszTn2Hic2fDXCSoAib4uy1Wf35Uaph1wGougS6avrsQ/640?wx_fmt=webp&animated=1&from=appmsg)

**开源数据库 TiDB 背后的厂商 PingCAP（平凯星辰）的托管云服务 TiDB Cloud 在近日遭勒索组织 FulcrumSec 攻击**，攻击者声称窃取约 10.6TB 数据并公开了首批约 200GB 样本供下载。

TiDB Cloud 是 PingCAP 面向企业客户推出的全托管云数据库服务，用户可以不开源版、直接用它的云端数据库。这次被勒索组织盯上并声称窃取 10.6TB 数据的，正是这个云服务的**控制平面**（租户、集群、密钥等元数据）。

戏剧的是，顶级第三方机构NCC Group在9月1日对 TiDB 的源码安全发布评估为：`没有严重、高危、中危问题`，全部为低危对产品源码的审计结论，但没有覆盖运营区。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzsfMNibHJBUDjR1GQc4rJRX92v8lEu4Bhj9uiaWZO2q3rDGNzxTj1MR2wBvHJvAFzmc7yDj8OsjBez9ibVN5LdHLL8dA7ssbyWzA/640?wx_fmt=webp&from=appmsg)

同一天，公司宣布任命新的首席安全官（CISO）。

**几天后（9月8-9日），攻击开始**。攻击者自称 9 月 8 日搭建控制平面复制通道、开始导出；官方确认的未授权访问从 9 月 9 日开始。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6Owk1Kdqibqqic92yAmFZN2s05aZEGP8s9VcC9b7HG4uZZ8BbPxE1icSOvlcJy1rHgseNV6Zc9m8n3CFVibUDIHxTSQzib71nkLun6n4/640?wx_fmt=webp&from=appmsg)

# 零告警

FulcrumSec在声明中描述，攻击是从 PingCAP 自己托管在 GitHub 的代码仓库中，发现了**已提交进仓库的 GCP 服务账号密钥和 Azure 服务主体凭据**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6Oy38msbAvnrBZ2d9bRkB0ZrGLKW17LUsNQhH28s1tQ5KP8QSRBmUofGicWcD0I4oL2RgLP9CVyy9iclPl6pm0EYVsTp6mwPIAbfg/640?wx_fmt=webp&from=appmsg)

2026 年 9 月 9 日起，攻击者利用这些被盗的服务账号凭据进入 PingCAP 内部系统，接触到云管理、财务、分析、存储系统，并复制数据、取得源代码。

他们利用云环境中过度授权的权限和缺乏分段，横向扩展到 Google Cloud 存储（自称约 50 个 GCP 存储桶）、BigQuery 数据仓库（自称 5.338 亿行）、Jira、CRM 等平台 —— 全程使用合法云凭据和云原生 API，无恶意软件、无外部 C2 基础设施，传统基于 IOC 的检测基本失效。

9 月 8 日至 30 日连续 22 天、**88 次导出、零告警**，最后一次运行于 9 月 30 日 06:02 UTC。初期拖走约 8TB，之后持续 "补货" 到 10.6TB。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UA4ABKCY6Owo6vuibOCxoAVReibqibibeNibC8oh3ZnhQ3Q564wuFxovwicbPVTgsgicaRRz0P03XLxzNIkSwltJic0ebqNI5sMxYEic05eoyNURMsfM/640?wx_fmt=webp&from=appmsg)

# 疑似被拖走的核心资产

被黑客点名的企业名单相当庞大，包括 Booking、Shopee、CAPCOM、Mercari、PayPay、富士通、软银、Square Enix、BANDAI NAMCO、Airbnb、Pinterest、Databricks 等公司，也包括 Bitget、Pionex、DigiPlus、NFTscan 和 Chainbase 等加密货币相关企业

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6Oz5utZDBFKm2BNnicodlChRt83ibskahqxD86JMzMOhqcSRZXkaiaCIKDbPP77Uibk4dxufS7hLnM4ic4CFZkITK1lgK8YYXK6V0CMM/640?wx_fmt=webp&from=appmsg)

· 控制平面 metadb 全量：18 万租户、40 万邮箱、11.5 万明文 API Key

· 客户 SQL：2064 万条 SQL 编辑器/查询语句

· 网关日志：4 年 1.02 亿连接、503 万客户服务器 IP

· 财务/商业资料、37.7 万 Jira 工单、413 个私有代码仓库

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzPnFpGc8kFluhtggibafL7oHNzxR4MZPgl1gJ19sGibTtVvv4hPAJlwmvDgCtloUrVhlVibMwHAjqsggzkt63N0ddjbT5YSngEjc/640?wx_fmt=webp&from=appmsg)

# 云厂商被打成筛子

云数据库资深从业者在事件评论中直接断言`几乎所有联网的云服务器和云虚拟机，都可能被打成筛子`，因为攻击者现在只需要盯住开源项目的公开 commit log 就能反向分析利用条件，而云厂商的补丁落地存在几周到几个月的 "致命时间差"；

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6Oyy0bBgsbFW9u2ezz0WGEN012CXqVqyHQibhCmHy3IQUsAEj6DhSLxlZjQKN0ClEQubLIKp7WvAdDoia3CiaaznOZAJ0rgdUSNgoo/640?wx_fmt=webp&from=appmsg)

同期国际同行也密集爆雷：`PaaS 平台 Zeabur 两度被入侵并于 12 月底关停`、`日本 IDCF Cloud 遭勒索 3.6PB 被加密`、`Hetzner 控制台遭攻击`、`Supabase 1.6 万个数据库因配置裸奔`。

# 运营面疏漏高发

某网于2026年5月披露的一起案例与本次事件根因完全同构：某3万+企业客户提供云存储和数据处理服务的服务商，因一名运维工程师把云服务器管理员密钥遗留在了GitHub公开仓库，导致存储数万客户数据、API密钥和业务配置的核心数据库被外部IP频繁访问。

国家网信办于2026年9月发布的典型案例，安徽某数据公司因ES源版本存在未授权访问漏洞、且开发测试完成后未删除测试数据，导致400余份企业内部文件被窃取。

# AI漏洞挖掘工业化

**PostgreSQL 8 月 13 日一次性披露修复 28 个 CVE，其中 14 个是 CVSS 8.8 的高危 RCE**，创历史纪录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OxNthic1VlSNq3kPmOc6BPdiavwFdBY7ksW5GK6fcgstfWt0a7caxgDa6PlCAdc6nKoa5114GWJgX5PQFdxqiaMUuiaVHTSSftWibH8/640?wx_fmt=webp&from=appmsg)

AI的发展让攻击成本断崖式下降，攻击从`稀缺资源`变`工业品`裸奔的惩罚被放大：**配置错误、泄露密钥**从`隐患`变`定时炸弹`。

对此`你怎么看`在评论区发表你的意见吧

![](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzcdibYcpTfc1rO9NJ2ND8IibicqN34hTt9SgJmFXgI4jJoicVmQ9icsuhDSONA193KOicSAG3jlUBuCmvdtfa82I56plOIhJRmj25OE/640?wx_fmt=webp&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

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