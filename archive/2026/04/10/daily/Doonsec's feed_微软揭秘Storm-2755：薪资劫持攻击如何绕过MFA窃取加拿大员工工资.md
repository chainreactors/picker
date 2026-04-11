---
title: 微软揭秘Storm-2755：薪资劫持攻击如何绕过MFA窃取加拿大员工工资
url: https://mp.weixin.qq.com/s/1ynixm5XbudT6m8ljCT-jA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:17:02.475291
---

# 微软揭秘Storm-2755：薪资劫持攻击如何绕过MFA窃取加拿大员工工资

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYAdYHHmGDdo215s5wouiaA5tq3ew3VOh0HOuYYecb8gc5XL3z2VIthEC7VJ9ic8A2PicNV4J8nmZWBpib77VTnF8pgIVojxz2QHNwU/0?wx_fmt=jpeg)

# 微软揭秘Storm-2755：薪资劫持攻击如何绕过MFA窃取加拿大员工工资

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Storm-2755 攻击流程示意图

微软事件响应团队（DART）近期发现一个新兴的经济动机威胁组织——**Storm-2755**，正针对加拿大员工发动"薪资劫持"（Payroll Pirate）攻击。该组织通过入侵用户账户，未经授权访问员工个人资料，将工资直接转入攻击者控制的银行账户，给受害者和组织造成直接经济损失。

与此前针对美国高校的类似攻击不同，Storm-2755 的活动具有独特的投递和定向方式。该组织不聚焦于特定行业或组织，而是**纯粹依赖加拿大用户的地理位置定向**，通过恶意广告（Malvertising）和 SEO 投毒来锁定受害者。攻击全程使用中间人（AiTM）技术劫持已认证会话，从而绕过多因素认证（MFA），将恶意行为隐藏在合法用户活动之中。

────────────────

攻击链路深度拆解

Storm-2755 的活动是一套围绕**会话劫持和企业合法工作流滥用**构建的经济动机攻击链。该组织将初始凭据/令牌窃取与会话持久化、定向侦察相结合，识别受影响加拿大组织中的薪资和人力资源（HR）流程。通过已认证用户会话进行操作并融入正常业务活动，攻击者在实施财务窃取的同时最大限度降低被检测的风险。

01 初始访问

在观测到的活动中，Storm-2755 很可能通过**SEO 投毒或恶意广告**获得初始访问权限。攻击者控制的域名 bluegraintours[.]com 被置于"Office 365"等常见搜索词或"Office 265"等拼写错误的搜索结果顶部。点击这些链接的用户被引导至仿冒 Microsoft 365 登录页面的恶意网站，输入凭据后即导致令牌和凭据窃取。

当用户在恶意页面输入凭据后，登录日志显示受害账户先触发了 50199 登录中断错误，紧接着 Storm-2755 成功入侵账户。更关键的是，**会话的 User-Agent 切换为 Axios（通常为 1.7.9 版本），但会话 ID 保持不变**——这表明令牌已被重放（Token Replay）。

**AiTM 攻击原理：**与传统凭据钓鱼不同，AiTM 框架在受害者与合法认证服务之间插入恶意基础设施，**实时代理整个认证流程**。攻击者不仅能获取用户名和密码，还能捕获认证成功后颁发的会话 Cookie 和 OAuth 访问令牌。这些令牌代表完整的已认证会话，攻击者可直接重用以访问 Microsoft 服务，**无需再次输入凭据或 MFA**，从而有效绕过非防钓鱼 MFA 保护。值得注意的是，该攻击路径还利用了 Axios 开源软件的已知漏洞 CVE-2025-27152，可导致服务端请求伪造（SSRF）。

02 持久化

Storm-2755 利用 axios/1.7.9 客户端中继认证令牌到客户基础设施，有效绕过非防钓鱼 MFA 并在无需重复登录的情况下保持访问权限。微软一致观测到**每约 30 分钟一次的非交互式登录**（针对 OfficeHome 应用），直到修复操作吊销活动令牌。

在约 30 天后，被盗令牌会因刷新令牌过期、轮换或策略执行而失效。在此期间，受损会话主要记录了对 OfficeHome 的非交互式登录，以及对 Outlook、My Sign-Ins 和 My Profile 的登录。对于部分身份，还观测到密码和 MFA 变更操作，以在令牌过期后维持更持久的访问。

Storm-2755 直接存款变更钓鱼邮件示例

03 侦察与社工

账户成功入侵后，攻击者立即启动侦察活动，搜索与薪资和 HR 相关的内部流程和邮箱。在多个客户环境中，受损会话的内部搜索关键词包括：**"payroll"、"HR"、"human resources"、"support"、"finance"、"account"、"admin"** 等。

攻击者的钓鱼邮件主题在所有受损用户中保持一致：**"Question about direct deposit"**（关于直接存款的问题）。目的是对 HR 或财务人员进行社会工程，诱导其手动更改薪资指令，从而无需进一步的手动操作。

在无法通过用户冒充和 HR 人员社工成功更改薪资信息的情况下，攻击者会**转向直接操作 HR SaaS 平台（如 Workday）**，手动登录受害者账户更新银行信息。

04 防御规避

侦察活动之后、邮件冒充之前，Storm-2755 创建了邮箱收件箱规则，将包含 **"direct deposit" 或 "bank"** 关键词的邮件移至受损用户的会话历史中，并阻止进一步的规则处理。这一技术极为有效——受害者根本看不到 HR 团队关于银行账户变更的回复邮件，因为邮件被立即转入隐藏文件夹。

**时间窗口规避：**为降低受害者正常重新认证导致访问失效的风险，Storm-2755 将被盗会话的续期时间安排在**受害者所在时区的凌晨 5:00**，即正常工作时间之外。

05 影响

在一个案例中，攻击者成功入侵用户账户后：创建收件箱规则抑制 HR 发来的"direct deposit"和"bank"相关通知 → 使用被盗会话冒充受害者给 HR 发邮件请求更改直接存款信息 → HR 回复更改流程 → 攻击者手动登录 Workday 更新银行信息 → **受害者的工资支票被转入攻击者控制的银行账户**，造成直接经济损失。

────────────────

检测与猎杀指南（KQL 查询）

微软提供了多项 KQL 猎杀查询，帮助安全团队检测此类攻击：

**1. 审查针对 Workday 的隐藏收件箱规则：**

CloudAppEvents | where Timestamp >= ago(1d)
| where Application == "Microsoft Exchange Online" and ActionType in ("New-InboxRule", "Set-InboxRule")
| where Parameters has "From" and Parameters has "@myworkday.com"
| where Parameters has "DeleteMessage" or Parameters has "MoveToFolder"

**2. 审查 Workday 支付信息变更：**

CloudAppEvents | where Timestamp >= ago(1d)
| where Application == "Workday"
| where ActionType == "Change My Account" or ActionType == "Manage Payment Elections"

────────────────

IoC 情报

|  |  |  |
| --- | --- | --- |
| 类型 | 值 | 说明 |
| 恶意 URL | bluegraintours[.]com | 用于窃取用户令牌的恶意网站 |
| User-Agent | axios/1.7.9 | AiTM 攻击中使用的 User-Agent 字符串 |
| CVE | CVE-2025-27152 | Axios SSRF 漏洞，攻击链利用点 |
| Entra 错误码 | 50199 | 登录中断错误，AiTM 活动的标志性特征 |

────────────────

缓解建议

微软建议组织采取以下防御措施：

**1.** 实施**防钓鱼 MFA**（FIDO2/WebAuthN），替代短信验证码和推送通知等传统 MFA 方式

**2.** 使用 **Conditional Access 策略**配置自适应会话生命周期策略，限制长期会话

**3.** 启用**持续访问评估（CAE）**，确保在风险条件变化时近实时吊销访问令牌

**4.** 创建可疑收件箱规则告警，快速识别和分类商业邮件入侵（BEC）和钓鱼活动迹象

**5.** 通过 **Microsoft Intune 合规策略**强化资源访问控制，确保只有合规设备才能访问企业资源

**6.** 对受损令牌和会话立即执行撤销，移除恶意收件箱规则，并重置受影响账户的凭据和 MFA 方法

────────────────

**来源：**Microsoft Threat Intelligence Blog
**原文链接：**Investigating Storm-2755: "Payroll pirate" attacks targeting Canadian employees
**发布日期：**2026-04-09

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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