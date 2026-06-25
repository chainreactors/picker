---
title: LastPass 这次不是密码库被攻破：真正该警惕的是 SaaS OAuth 供应链
url: https://mp.weixin.qq.com/s/ND6kuxpbOAMXSLvzA_cwHQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:03.719131
---

# LastPass 这次不是密码库被攻破：真正该警惕的是 SaaS OAuth 供应链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nOo5YmK1PHzRRqCHxc9CfyVjZ4ZKo0qFBMYFVO2zfXMlliaicp1MYA4wSJmMCortdBZicnSDaiaTcicsTZ8620hWACVcbJL7lH8j9sZeqmoeibSyE/0?wx_fmt=jpeg)

# LastPass 这次不是密码库被攻破：真正该警惕的是 SaaS OAuth 供应链

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

摘要：LastPass 披露，攻击者通过第三方市场情报平台 Klue 被盗的 OAuth token，访问了其 Salesforce 环境中的客户联系和 CRM 数据。LastPass 强调产品、服务、基础设施和客户密码库未受影响。对企业来说，这起事件的重点不是恐慌，而是重新审视第三方 SaaS 集成、OAuth 授权和 CRM 数据暴露面。

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHxZPYJYXqicEC6yKK2xiaYQoZRpvibC0uT6Mic7U5WN2fNmRvSfO8TdPRBsicBbyFTvlicPewPB25ic2a0dFCOvMz7ZSU1cSo1UXEnCAY/640?wx_fmt=png&from=appmsg)

事件概述
    过去 24 小时内，BleepingComputer 报道了 LastPass 在 Klue 供应链事件中的数据暴露情况。LastPass 官方说明称，6 月 12 日获悉第三方供应商 Klue 发生安全事件。Klue 是其市场进入团队使用的市场情报平台，并与 LastPass 的 Salesforce 和 Gong 系统集成。
    LastPass 表示，攻击者获取了 Klue 为多个客户保存的 OAuth token，其中包括 LastPass 的 token，并用这些凭据访问了 LastPass Salesforce 环境中的客户数据。LastPass 同时强调，本次范围仅限与 Klue 应用集成的系统，LastPass 产品、服务、基础设施未受影响，客户密码库仍然安全，也没有证据显示 Gong 相关数据被访问。
    这类事件的传播点很明显：用户看到 “LastPass” 和 “data breach” 容易联想到密码库风险。但从公开信息看，本次更准确的关键词是：第三方 SaaS、OAuth token、CRM 数据和供应链权限治理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nOo5YmK1PHyyZZ41Eic2QynStYgF1Eg8Xt5cibootrFGzo7weeiaIfxunE8NKVIXUX8aMt4ZCCtfkcqlt9HawAqoxXysCm3Ps3VHM2oMwkJye8/640?wx_fmt=png&from=appmsg)

核心事实
    第一，事件入口是第三方供应商 Klue 持有的 OAuth token，而不是 LastPass 密码库系统被攻破。
    第二，被访问的信息限于标准商业联系信息和客户关系管理数据，包括客户姓名、电话、邮箱、地址、支持工单数据和销售相关数据。
    第三，LastPass 称相关 Klue OAuth token 已完成轮换，补救已完成；BleepingComputer 于 2026 年 6 月 23 日报道了该事件。
    第四，即便密码库未受影响，CRM 和支持数据仍然有价值。攻击者可利用这些信息做精准钓鱼、冒充客服、供应商诈骗或后续社工。
影响分析
    对普通用户来说，最重要的是不要误判风险。公开信息没有显示 LastPass 密码库泄露，因此不应把这次事件简单理解为“密码全部被偷”。但如果你曾经与 LastPass 销售或支持有过互动，后续收到自称 LastPass、Klue、客服、续费、企业支持的邮件或电话时，应提高警惕。
    对企业来说，SaaS 集成风险正在从“账号密码”转向“授权 token”。OAuth 的便利性在于用户不用反复登录，第三方应用也能访问业务系统；风险在于，一旦第三方应用或其 token 管理失守，攻击者可能绕过传统登录流程访问已授权的数据。
    对安全团队来说，CRM 不应被看成低风险系统。客户名单、联系人、支持工单、销售备注、合同线索、客户痛点和历史沟通记录，都是攻击者做定向社工的材料。
应对建议

1. 盘点第三方 SaaS 集成。列出哪些外部应用连接了 Salesforce、Gong、HubSpot、Slack、Google Workspace、Microsoft 365、工单系统和代码平台。
2. 检查 OAuth 授权范围。外部应用只应获得完成业务所需的最小权限，避免长期持有过宽的数据访问权。
3. 建立 token 轮换和撤销流程。供应商发生事件后，不能只等供应商通知，应能快速撤销授权、重建连接并验证访问日志。
4. 审计 CRM 异常访问。关注异常时间、异常地理位置、异常 API 调用、批量导出、陌生应用授权和历史 token 使用情况。
5. 对客户沟通做反钓鱼提醒。若客户联系数据可能被访问，应提醒客户识别冒充客服、续费、合同和支持工单的社工邮件。
6. 把 go-to-market 工具纳入安全基线。市场、销售、客服常用 SaaS 同样处理敏感数据，不应低于研发和财务系统的安全要求。
7. 对供应商做集成分级。凡是能读写客户数据、工单、邮件或会议记录的供应商，都应进入高风险第三方管理清单。
   事实、推测与观点区分
       事实：LastPass 官方称攻击者通过 Klue 持有的 OAuth token 访问了其 Salesforce 环境中的客户联系和 CRM 数据；LastPass 产品、服务、基础设施和客户密码库未受影响。
       合理推测：被访问的 CRM 数据可能被用于后续精准钓鱼、冒充支持人员或供应商诈骗，但是否已发生需以官方后续通报为准。
       本文观点：企业安全治理不能只盯核心生产系统，销售、市场和客服 SaaS 的 OAuth 授权同样可能成为数据暴露入口。
   结语
       这次事件不是“密码库沦陷”的故事，而是一个更常见也更容易被忽视的问题：第三方 SaaS 拿着长期有效的授权，连接着高价值客户数据。真正的改进，不是少接一个工具，而是让每一个授权都可见、可控、可撤销。
   关键来源
   • LastPass, “Klue Supply Chain Incident & LastPass Response”, 2026-06-23: https://blog.lastpass.com/posts/klue-supply-chain-incident-and-lastpass-response
   • BleepingComputer, “LastPass confirms data breach in Klue supply chain attack”, 2026-06-23 09:58 AM: https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia3Is12pQKnIPvX43Bm5RTfn38gGrVIvGtiaMrLfFqknYBzOd4wmQb1Ra7InwkMM5Ru09FTZ6ibhcLiagpiannxZdlA/0?wx_fmt=png)

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