---
title: 微软发布安全预警：攻击者正利用 M365 服务中断事件发起“邮件恢复”钓鱼攻击
url: https://mp.weixin.qq.com/s/qCmK_H0gMCSF9vZmfvy6Vw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:51:33.842585
---

# 微软发布安全预警：攻击者正利用 M365 服务中断事件发起“邮件恢复”钓鱼攻击

# 微软发布安全预警：攻击者正利用 M365 服务中断事件发起“邮件恢复”钓鱼攻击

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnt9XC00LoJHZy2Z5dweUNib5KTaI4LsyEUwiaicV6Th1W93eqtcOEf4ncL8c79WibZfDhZa5p3etFYDfiaoUZX57BNGpZh0xOLd4snQ/640?wx_fmt=png&from=appmsg)

微软发布警告，称有攻击者正利用 11 月 12 日发生的 Microsoft 365 服务中断事件，发起一场活跃的钓鱼攻击活动。

攻击者伪装成服务健康状况通知，并引用了真实存在的 Exchange Online 事件编号 EX1550543。借助这一真实的运营故障，攻击者使伪造的邮件恢复请求对企业用户而言显得极具可信度。

### 利用 Microsoft 365 服务中断的钓鱼攻击

根据微软威胁情报（Microsoft Threat Intelligence）的检测，11 月 13 日发现的钓鱼邮件谎称：相关邮件在服务中断期间被暂存（held），收件人若不在 24 小时内点击恢复链接，这些邮件将被删除。此举针对可能错失重要业务通讯的担忧，刻意制造了紧迫感。

这种诱饵策略将用户对服务可用性的焦虑，转化为立即行动的紧迫压力。攻击者将真实的事件标识符与捏造的删除期限相结合，为收件人编造出一个看似合理的"邮件丢失"理由。与此同时，他们却将用户引导至与微软官方服务健康状况报告渠道毫无关联的链接。

此次伪装手法与更广泛的 Microsoft 365 通知类钓鱼战术如出一辙，均利用了用户熟悉的管理语言。在本次活动中，观察到的邮件主题行遵循"Outage – [六位字符代码]"的格式。发件人显示名称则采用"组织专属前缀 + Outage Notification（中断通知）"或"Service Health（服务健康状况）"的组合，进一步强化了"量身定制的内部通告"这一假象。

微软识别出三个与该活动相关的发件域名：`moments-notice[.]com`、`planetmaison[.]com` 和 `newbooker[.]com`。邮件中嵌入的链接会先经过针对每位收件人生成的 SendGrid 点击跟踪（click tracking），随后重定向至 `reallifeaccounting[.]com`。其中一个已观察到的落地页包含路径 `/themelist0.html`。类似的钓鱼邮件针对的是美国多个行业的组织，而非某一家孤立的企业。

这一警告补充了此前关于 Microsoft 365 账户钓鱼的报道，但相关证据需要审慎界定。微软评估认为，该活动的特征与凭据钓鱼（credential phishing）相符；但官方尚未确认存在实际的凭据收集行为或恶意软件投递。因此，观察到的重定向行为不应被直接等同于账户已被成功入侵的证据。

在调查取证方面，微软建议使用 Microsoft Defender for Office 365 的威胁浏览器（Threat Explorer）以及 Microsoft Defender XDR 的高级狩猎（advanced hunting）功能。安全团队可查询 `EmailEvents`、`EmailUrlInfo` 和 `UrlClickEvents` 等数据表，以识别可疑邮件、审查嵌入的落地目标，并调查用户的点击行为。这些记录有助于在评估活动影响范围时，将"邮件投递"与"用户实际交互"区分开来。

各组织还应全面审查其环境中的恶意链接防护设置。在正确配置的前提下，Microsoft Defender for Office 365 的 Safe Links（安全链接）功能可提供点击时防护（time-of-click protection），拦截恶意 URL。管理员应核实相关策略是否生效，并调查潜在的攻击交互，而不应想当然地认为只要启用了安全产品，就能自动保护每一位收件人。

通过 Microsoft 365 管理中心（admin center）核实服务中断情况，切勿轻信邮件中未经请求的恢复指引。对于防御方而言，当务之急是将"中断主题"的邮件、发件基础设施、重定向落地地址以及点击遥测数据（click telemetry）进行关联分析。在事件响应过程中，始终保持"钓鱼尝试"与"已确认入侵"之间的界限，才能确保响应措施与实际掌握的证据相匹配、不过度升级。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过