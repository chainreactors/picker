---
title: GitHub API遭滥用，企业代码库面临隐秘侦查威胁
url: https://mp.weixin.qq.com/s/Q10yqNKHZNTfVVLeg-buZg
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:44.687620
---

# GitHub API遭滥用，企业代码库面临隐秘侦查威胁

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3uFszLNC8CEVWkUQGGfeXxFiacEpbVwW98NmTA2ufRHUGqxteTCnI7JKNAgoYzvI7ljSpqEWHGBRt2f6ibU45tzMbO24e0TB7lw/0?wx_fmt=jpeg)

# GitHub API遭滥用，企业代码库面临隐秘侦查威胁

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX11ZribZiaggDiaVTsul5jfTeQfoYdZgcoVVACQtY4nTeryRibkSnlqKUbw9PXMhn9icnjFmBZk1ZAHIqvicibRKicO3gibR5CPqWRKLX8w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1XdnM5VteVuxKMzPhoNDIWKO11Gicgc3daicnCIvfYoCQLWH74KpLTk7XPesiaLKLicpxfBle2LGryZHrSFnGlW1fGlVib7YGh2LhA/640?wx_fmt=png&from=appmsg)

Part01

隐蔽的侦查行动

研究人员发现一项持续进行的攻击活动，攻击者利用 GitHub公共API和幽灵账户对企业软件环境进行画像，同时完美融入正常开发者活动之中。

GitHub始终是攻击者觊觎的目标，因其处于软件供应链核心位置，能提供威胁行为者最渴望的三样东西：源代码、密钥以及可肆意操纵的自动化流水线。

Datadog安全研究团队过去数月持续追踪GitHub API滥用行为，发现其呈现"持续性模式"。这些请求看似单独出现时"平淡无奇"，但当它们跨环境持续数周运作，尤其是发展为完整克隆时，危险性便急剧上升。最大挑战在于这些行为与正常API使用模式高度相似。

Beauceron Security的David Shipley指出，由于多数开发生命周期存在安全隐患，GitHub已成为攻击者突破企业防线的金矿，威胁行为者通常瞄准API密钥和云环境密钥。

"随着AI Agent编程推动开发效率提升，密钥宝库的规模可能更加庞大。"他比喻道，"用模拟时代淘金热的名言来说——'群山之中藏着黄金'。"

安全合规公司DataBee的CTO Scott Miserendino对此表示认同："GitHub是开源和企业项目最受欢迎的源代码仓库，其海量项目资源加上托管着众多流行软件，自然成为攻击目标。"他特别指出，未经授权克隆私有仓库等知识产权盗窃行为，可能被用于盗用专有软件或发掘可利用漏洞。

Part02

自动化侦查技术

Datadog高级安全工程师Julie Agnes Sparks在博客中披露："这些活动并非单一行为体所为，而是融合了定制化自动扫描工具、凭据泄露的投机性滥用，以及经过协调的幽灵账户网络。"

Sparks解释道，GitHub大部分API接口无需认证即可访问——这是其设计特性。API请求通常返回标准HTTP 200响应，这意味着威胁行为者能构建包含组织架构、公共仓库、成员关系、关注列表、星标仓库及互动项目的完整图谱。此类流量与正常API使用无异，因此难以察觉。

值得注意的是，GitHub仅在与私有仓库交互时收集地理位置数据，记录用户身份及所用访问令牌，而对外部资源交互则不做记录，这限制了基于地理位置和VPN/代理的溯源能力。

攻击者通常使用定制化或看似合法的用户代理（User Agent），利用注册于2-5年前且长期休眠的GitHub"幽灵账户"实施自动化爬取。Sparks强调："拥有多年历史的账户比新注册账户更具可信度。"研究发现，这些账户通常在1-3周内对多家企业发起"爆发式"扫描后便停止活动，已识别出超过50个幽灵账户，其命名呈现user432023、user412023或kobalt\*等规律性特征。

部分攻击活动确实使用了真实GitHub账户——这些账户或因用户意外泄露OAuth令牌、个人访问令牌（PAT），或因终端设备遭入侵而暴露。攻击工具采用GitHub-Company-Scraper、GitHub-Scraper-Tool/1.0等名称伪装成正常数据分析流量，主要针对适合批量查询的graphql接口，同时使用常规REST端点进行组织架构测绘。

Part03

企业防护建议

Sparks指出，通过监控用户代理、令牌类型、自治系统编号（ASN）等关键字段可有效发现异常行为。"用户代理、事件活动和操作者名称是识别未授权行为的重要线索，"她建议企业审查GitHub审计日志中的异常用户代理行为，特别是涉及私有仓库的访问——此时平台会记录IP地址、操作者名称和程序化访问类型。

企业应启用GitHub审计日志流式传输，建立用户代理基线并开展主动威胁狩猎。Sparks特别强调："关键在于掌握自身环境的正常行为特征。"Miserendino补充道，企业须遵循基础安全实践：为所有账户启用多因素认证（MFA）、定期审查用户访问权限、清理闲置账户，以及扫描仓库中明文存储的凭据。

参考来源：

GitHub’s public APIs are becoming an enterprise reconnaissance tool

https://www.csoonline.com/article/4194665/githubs-public-apis-are-becoming-an-enterprise-reconnaissance-tool-2.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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