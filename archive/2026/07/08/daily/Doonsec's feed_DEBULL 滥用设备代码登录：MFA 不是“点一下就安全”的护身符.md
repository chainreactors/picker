---
title: DEBULL 滥用设备代码登录：MFA 不是“点一下就安全”的护身符
url: https://mp.weixin.qq.com/s/CgsH27DS6RK5XNiAmkuc4A
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:57:32.006356
---

# DEBULL 滥用设备代码登录：MFA 不是“点一下就安全”的护身符

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nOo5YmK1PHxiah5Zm5TUibUVoVKkmJXflpvib8he5HKialKhVaakaarjuZ8d1G6tPyrv4UiaYQJ2xTg5py7h64zIEZKeoX5sU10RNsPqMoQEnY7o/0?wx_fmt=jpeg)

# DEBULL 滥用设备代码登录：MFA 不是“点一下就安全”的护身符

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHzranK809peX0KymCcVU85mNzZ80vomOibYriauB55ZEcAYY2qyAszweCm9j5DibDsPd2E2kE9Yvh2iam2su5GzTgHdTpk1mlUeUZc/640?wx_fmt=png&from=appmsg)

    很多企业已经启用了 MFA，于是默认认为“账号安全基本稳了”。

    但现实中的钓鱼已经不只是在假页面上骗密码。更棘手的一类攻击，是诱导用户在真实的登录流程里完成授权，让攻击者拿到令牌或会话能力。用户看到的页面可能是真的，流程也可能是真的，危险点在于：这次登录并不是用户自己发起的。

    7 月 7 日，The Hacker News 报道的 DEBULL 工具链滥用 Microsoft 365 设备代码流程，就是这类身份攻击的最新提醒。

事件概述

    The Hacker News 报道称，ZeroBEC 观察到一类 Microsoft 365 设备代码钓鱼活动，使用协作文档、共享文件夹、付款等诱饵，引导受害者进入合法的 Microsoft 设备登录体验。攻击者不一定需要伪造 Microsoft 密码页，而是利用设备代码授权流程的特性，让用户在真实登录页面中输入攻击者提供的代码，从而把会话授权给攻击者控制的流程。

    Cisco Talos 7 月 1 日发布的 ARToken/EvilTokens 分析，也展示了类似生态正在从单点钓鱼页面发展为更完整的 PhaaS 和 BEC 操作平台，能力覆盖令牌管理、邮箱访问、业务邮件诈骗和文件访问等环节。

核心事实

    事实：Microsoft 设备代码流程本身是合法 OAuth 机制，常用于不方便直接输入账号密码的设备，例如电视、IoT 设备或打印机等。Microsoft Learn 文档明确说明，该流程允许用户在另一台设备的浏览器中完成登录，从而让原设备获得访问令牌。

    事实：The Hacker News 2026 年 7 月 7 日报道称，DEBULL 相关活动使用协作类诱饵滥用设备代码流程，目标是 Microsoft 365 账号。

    事实：Cisco Talos 2026 年 7 月 1 日发布研究，分析了 ARToken/EvilTokens 相关面板和生态，显示设备代码钓鱼已与邮箱访问、BEC 和持久化会话能力结合。

    推测：未来一段时间，面向财务、人事、采购、法务、销售等高邮件价值岗位的设备代码钓鱼会继续增加。原因是这些岗位对共享文档、付款、合同和供应商沟通更敏感。

    观点：MFA 是必要基础，但不能被当成终点。身份安全的重点正在从“验证一次登录”转向“持续判断这次授权是否合理”。

影响分析

    设备代码钓鱼的欺骗性在于，它绕开了很多人对传统钓鱼的判断习惯。

    用户没有看到粗糙的假登录页，甚至可能确实在官方登录页面完成操作；安全团队也可能只看到一次看似正常的授权流程。如果缺少设备代码登录、OAuth 授权、异常地理位置、异常客户端和邮箱行为的关联分析，攻击可能在较长时间内不被发现。

    对企业而言，成功的账号接管可能带来四类后果：读取邮件、搜索合同和发票、利用真实邮箱发起 BEC、访问 SharePoint 或 OneDrive 中的敏感文件。对普通用户而言，风险则集中在账号被接管、通讯录被滥用、云盘文件外泄和二次诈骗。

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHyLBRO8Rr7NDxNFkDKddJLx8CmlcIEmPFiaQDtde4ib7CEufdDasibsJAslIw1xQJ1o3RNX8fic2Y1k2BfvBFMKGCjqwsb66WJ9rd8/640?wx_fmt=png&from=appmsg)

企业和普通用户应对建议

    1. 强化用户提醒：任何人都不应输入别人通过邮件、聊天、二维码或网页转发来的设备代码。设备代码只应来自自己正在登录的可信设备。

    2. 审计设备代码登录：在 Microsoft Entra ID / Microsoft 365 审计中关注设备代码流程、异常 OAuth 授权、非常见客户端、异常地理位置和异常登录时间。

    3. 调整条件访问：按业务需要限制或加强设备代码流程的使用条件，对高风险用户、高价值岗位和非托管设备增加额外约束。

    4. 监控邮箱后续行为：发现可疑登录后，不要只改密码。还要检查转发规则、隐藏规则、OAuth 应用授权、异常发送、异常 SharePoint/OneDrive 访问和会话令牌。

    5. 快速撤销会话：对确认或高度怀疑的账号，应撤销活动会话和刷新令牌，重置凭据，复核 MFA 方式，检查是否新增了设备或应用授权。

    6. 对财务流程加一道人工校验：涉及付款账户变更、紧急转账、供应商发票重发等场景，应建立电话或独立渠道确认机制，不能只依赖邮件链路。

结语

    设备代码钓鱼最值得警惕的一点，是它把“真实登录页面”变成了攻击链的一部分。

    所以，防守不能停留在“别点假链接”“看域名对不对”。更有效的做法是：限制不必要的授权流程，监控异常授权行为，并让员工知道一个简单规则：不要替别人完成任何登录代码输入。

    MFA 仍然重要，但今天的身份安全需要比 MFA 更进一步。

关键来源

• The Hacker News，2026-07-07，DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts：https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html

• Cisco Talos，2026-07-01 06:00，ARToken: Inside an EvilTokens affiliate panel targeting Microsoft 365：https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/

• Microsoft Security Blog，2026-04-06，Inside an AI-enabled device code phishing campaign：https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/

• Microsoft Learn，OAuth 2.0 device authorization grant：https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code

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