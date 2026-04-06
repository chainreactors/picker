---
title: 黑客对Node.js关键维护者发起社会工程攻击
url: https://mp.weixin.qq.com/s/3iD-od-osx0VEQc0Od3SAA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:41:48.559077
---

# 黑客对Node.js关键维护者发起社会工程攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NDDibwicv4jczibHwmmbD4IHnP4lAn7KoMI4RKnSsXYbEkNa8elyuZuB3I3LCBmOefAJxMgQPDue266XrrQTEz3mjxvJXwQ76h7w/0?wx_fmt=jpeg)

# 黑客对Node.js关键维护者发起社会工程攻击

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

继广泛使用的 Axios 软件包发生备受瞩目的供应链泄露事件后，一场针对顶级 Node.js 和 npm 维护者的高度协调的社会工程攻击活动被揭露出来。

安全研究人员证实，Axios 数据泄露事件是旨在渗透全球软件供应链的大规模行动的一部分。

威胁行为者正在积极寻找拥有基础开源软件包写入权限的开发者，将受信任的维护者变成恶意软件的分发渠道。

目标人员管理着对现代软件基础设施至关重要的工具，每月累计下载量达数十亿次。

攻击者最近试图入侵 Socket 首席执行官 Feross Aboukhadijeh、Lodash 创建者 John-David Dalton 和 Fastify 首席维护者 Matteo Collina 的账户。

其他被列入名单的知名人士包括 dotenv 包的 Scott Motte、Node.js 核心合作者 Jean Burellier 以及 Wes Todd 和 Pelle Wessman 等生态系统贡献者。

Aboukhadijeh 警告社区，这种针对个人维护者的持续性、有针对性的骚扰已经成为新的常态。

威胁行为者不会依赖简单的网络钓鱼链接，而是会耐心地执行长达数周的计划，旨在建立真正的信任关系。

攻击者通常通过 LinkedIn 或 Slack 发起联系，冒充合法的招聘人员、营销机构或播客主持人，并使用“Openfort”等虚假公司名称。

他们以专业的企业行为举止行事，精心安排和重新安排视频会议，以解除目标对象的戒备，并建立虚假的信任感。

一旦维护者同意开会，他们就会被引导到一个仿冒的视频会议平台，该平台旨在模仿 Microsoft Teams或 Streamyard。

受害者加入通话后不久，就会看到一条技术上合理的音频或视频错误信息。

为了解决这个人为制造的问题，该网站会提示开发者下载一个本地应用程序或执行一个终端命令。如果受害者照做，恶意程序就会在其计算机上静默安装一个持久性远程访问木马。

这种恶意软件部署具有毁灭性的效果，因为它完全绕过了双因素身份验证等标准安全措施。

Socket 的安全研究员 Tay 解释说，该木马程序会立即捕获受害者身份验证后的状态。

通过窃取活动浏览器会话 cookie、AWS 凭证和发布令牌，攻击者可以立即获得对 npm 注册表的写入权限。

开发者 Wes Todd 警告说，虽然基于 OIDC 的发布提高了安全意识，但它会给人一种虚假的安全感，使人无法抵御完全被攻破的本地计算机。

网络安全专家和组织已将这些复杂的行动与疑似朝鲜威胁组织 UNC1069 联系起来。

从历史上看，UNC1069 曾花费数年时间，利用高级恶意软件攻击加密货币创始人及风险投资家，以榨干他们的数字钱包。

然而，他们转向开源维护者的战略举措标志着事态的严重升级。攻击者通过劫持开发者的npm 发布权限，可以分发恶意更新，这些更新会被全球数百万个持续集成管道自动接收。

网络安全界敦促开发人员保持高度警惕，并分享他们的经验，不要害怕尴尬。

随着威胁行为者不断改进其策略，包括利用 Slack 群组等平台以及部署人工智能生成的视频角色，集体意识仍然是最强大的防御手段。

开发人员的计算机一旦被攻破，就等于直接攻击了数百万个默默依赖于其代码的企业服务。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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