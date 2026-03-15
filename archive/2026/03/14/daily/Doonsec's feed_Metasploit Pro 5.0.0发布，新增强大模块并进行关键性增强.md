---
title: Metasploit Pro 5.0.0发布，新增强大模块并进行关键性增强
url: https://mp.weixin.qq.com/s/rQ5wOyoMOR63u6f0-C4CFA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:29:01.770736
---

# Metasploit Pro 5.0.0发布，新增强大模块并进行关键性增强

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hfjKPyxBDjpMSDliaWENktPIznLwBicK22KzicepHr4NgTqgM8Ud2KoH2iaicoDRjTIJF4DpWfGbV6RU5iau7Emw1x4CYLVJkibmkjuNcAW0l7Q3dU/0?wx_fmt=jpeg)

# Metasploit Pro 5.0.0发布，新增强大模块并进行关键性增强

原创

铸盾安全
铸盾安全

河南等级保护测评

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/hfjKPyxBDjpcWYMuIeIuJ77r7ZfIe8EsphapVEansIScibbKkrxmrJvy1mzsorNG5uN64Z5697jIxuclJbTsZSt7qDn6IltvCU8hLAp7uQTk/640?wx_fmt=png&from=appmsg)

随着网络犯罪分子不断利用新的漏洞，对持续的红队演练和主动安全评估的需求也达到了前所未有的高度。

年度渗透测试已不足以保障现代复杂环境的安全。为了帮助安全团队领先于高级威胁攻击者，Metasploit Pro 5.0.0 已正式发布。

此次重大更新带来了一种全新的红队演练方法，其特点是直观的测试工作流程、高级 Active Directory 功能以及一套强大的新模块。

Metasploit Pro 5.0.0 通过彻底改进的测试工作流程简化了接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjrj0gciapojzC7cMeY0icPab8y1JqHpZqDrgdDhiaoUWIs9TUBr3Lq91vYL3Ye3YI6nicXkjZia9eMDiaVDz0djwQnNoI4bZGoECdWWQ/640?wx_fmt=png&from=appmsg)

直观的测试工作流程（来源：Rapid7）

更新后的用户界面使渗透测试人员能够专注于高价值漏洞验证，而不是配置工具。

此次重新设计的一大亮点是新增了网络拓扑支持功能，可即时直观地显示受损主机、破解凭证和捕获的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/hfjKPyxBDjoSVGCCv3XibMVx3aX2vqTDPLZm0JATnBn2GNfWicHyIJtoEOwozvJyDGp3HGpAms2NZ0WQAntox13ibDtSLUC9XyEibDJKreG9icVk/640?wx_fmt=png&from=appmsg)

网络拓扑支持将数据转化为可视化防御（来源：Rapid7）

该映射功能专为处理大型企业环境而设计，使安全团队能够零延迟地浏览数百台主机，将复杂的数据转化为可操作的防御策略。

# 更智能的漏洞检测和 AD CS 漏洞利用

在发起漏洞利用之前，安全团队需要确保该操作有效且安全。Metasploit Pro 现在会在执行过程中记录有关漏洞检测的关键细节。

配备预检逻辑的模块可以在尝试任何利用之前评估目标并提供完整的情报图景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjo4OxvOkXRCibS9YxodbdfuKtAdFxIVdiaOOMeFvyXJibDaRlWAASr3QKxYgOOTgFRZhLyOX3JdCIKcMgbSCePeI8cojfLCh1BSXA/640?wx_fmt=png&from=appmsg)

漏洞检测改进（来源：Rapid7）

这种透明度有助于用户更快地做出决策，节省时间，并最大限度地降低不良副作用或模块运行失败的风险。

此次更新还解决了现代企业网络中最关键的攻击途径之一：Active Directory 证书服务 (AD CS)。

AD CS 工作流元模块已升级，提供了一种自动化、全面的方法来识别九种常见的 AD CS 漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/hfjKPyxBDjrvzHdcCwjr8abp3QxEZbiaeN19ZVTEugQwSy8malMB12XX4e6kcPNgEWgI5x59t6nORfP16nN4K7whoGU6NiceKRsslhOyXYd2M/640?wx_fmt=png&from=appmsg)

AD CS 工作流元模块（来源：Rapid7）

现在它积极支持最新的、最危险的升级漏洞，特别是 ESC9、ESC10 和 ESC16，使专业人员能够以外科手术般的精准度消除这些威胁。

# 先进的控制和技术改进

Metasploit Pro 5.0.0 为高级用户提供了前所未有的控制权，将复杂的操作简化为几次简单的点击。

用户现在无需手动配置每个选项，系统会针对适用的值提供智能建议，例如网络目标和Kerberos 凭据缓存。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjrODu01xqXSjib55b56tnwt0upzEF8VZBmzxicdbkgesLjjjCO3lW4y6nFEFYCTrKQJFSZ5NOia9dtnde7QVPZCJwAHMJy103R1qk/640?wx_fmt=png&from=appmsg)

随着新会话的开始和分析师切换任务，上下文可能会迅速消失（来源：Rapid7）。

本次版本的主要技术改进包括：

手动有效载荷配置：安全专业人员现在可以手动选择和配置单个有效载荷，以实现精细控制，但为了方便起见，系统仍将默认使用最常用的选项。

会话标签：为了提升团队协作，分析师可以为打开的会话添加自定义标签，例如优先级、角色或环境。这可以防止在快速操作过程中丢失上下文信息，并使在多人协作中跟踪高价值目标变得更加容易。

SAML 单点登录 (SSO)：企业现在可以将 Metasploit Pro 与其集中式身份提供商集成。这实现了无缝的无密码登录体验，并可利用现有的多因素身份验证 (MFA) 服务。

一键重放：验证修复比以往任何时候都更加简单。现在，重放模块运行以重新利用目标变得无缝衔接，不再需要重新配置整个模块。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoERdyt2icMobIJOJ7gZ6EE7A5Lu91AicvWMVsCUpMGUVic1PkJD8nJULlZG3XyRDzTNpQbVsfyFBLYeg/0?wx_fmt=png)

河南等级保护测评

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoERdyt2icMobIJOJ7gZ6EE7A5Lu91AicvWMVsCUpMGUVic1PkJD8nJULlZG3XyRDzTNpQbVsfyFBLYeg/0?wx_fmt=png)

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