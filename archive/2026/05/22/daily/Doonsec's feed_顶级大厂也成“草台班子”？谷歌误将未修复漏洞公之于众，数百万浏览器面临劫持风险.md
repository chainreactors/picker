---
title: 顶级大厂也成“草台班子”？谷歌误将未修复漏洞公之于众，数百万浏览器面临劫持风险
url: https://mp.weixin.qq.com/s/70EqPfIriYX_z36CvaplOQ
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:38:06.613595
---

# 顶级大厂也成“草台班子”？谷歌误将未修复漏洞公之于众，数百万浏览器面临劫持风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lQ1jXOMq3d15v8XtUKfGECrcVURicglqp1UscxjcHBj1BylpNFVIokGT6Q3yWFx5v2YVFDqNsD1lzSzy2baGlnVbYxxjrYVZLx7dyVYs37D4/0?wx_fmt=jpeg)

# 顶级大厂也成“草台班子”？谷歌误将未修复漏洞公之于众，数百万浏览器面临劫持风险

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年5月20日，谷歌Chromium项目在问题追踪器上意外公开发布了一个严重漏洞的完整细节与概念验证（PoC）攻击代码。该漏洞由独立安全研究员Lyra Rebane于2022年12月私下报告并获确认，至泄露时已长达近三年半未修复。在泄露当天，Rebane测试后发现该漏洞在最新的Chrome Dev 150和Edge 148中仍然有效，所谓的“修复”根本不存在。她在社交平台上惊呼：“哦不，我刚刚意识到这个问题实际上并没有得到彻底修复，它仍然可以运行！”更令人不安的是，Rebane进一步发现，在最新版Edge浏览器中，此前可能出现的下载弹窗提示已完全消失，使漏洞利用变得完全静默。她写道：“这是完全静默的JS远程代码执行攻击，即使关闭浏览器后也会继续运行！！而这一切仅仅是因为你访问了一个网站！”谷歌代表在事后声明中表示，公司已知晓代码发布一事，正在开发补丁。但此时，攻击代码已被归档站留存并可能已在暗网扩散。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lQ1jXOMq3d1a4oxfJmnVHbJLJy6FaMRWwbAwibkLyLKRZ69hGsyOTZeWTtRgnS8iarKnmG7X8OZ6TU8JkxeOyiby05pvuJXd8Rxwp4WBwHiblt0/640?wx_fmt=jpeg&from=appmsg)

#### 浏览器如何变成“永不熄灯”的僵尸节点

该漏洞的核心在于对Browser Fetch API的滥用。这项技术标准本用于在后台静默下载大型文件，但攻击者可利用其创建一个恶意的Service Worker，从而在用户设备上建立持久化的控制通道。具体技术链条如下：

**触发之简单，令人咋舌。** 用户仅需访问一个恶意网站，该网站运行的JavaScript代码即可触发漏洞，无需点击任何链接、确认任何弹窗或执行任何下载操作。正如Rebane所说：“无需用户交互，就能将任何基于Chromium的浏览器变成永久性的JS僵尸网络成员。”

**驻留之顽固，超乎想象。** 漏洞利用代码会注册一个Service Worker，使其保持持久活跃。最危险的是，在Edge浏览器中，即使用户完全关闭浏览器，该连接仍会保持。Rebane强调，在Edge上“你甚至不会注意到任何异常，即使关闭浏览器，也会保持与C2的连接”。这意味着攻击者获得了一个随设备启动而自动复活的永久后门。

![](https://mmbiz.qpic.cn/mmbiz_png/lQ1jXOMq3d1n1SnYS0TgW2LiafB9kRhgEWQc7AHyEogLO2VI7YA8KG74R7usXbdjqsv750slHgIKSXdoIMtBZb7CPeoGomE48U7YlcSI9HjU/640?wx_fmt=png&from=appmsg)

**隐蔽之深，难以察觉。** 该漏洞在不同浏览器上表现各异。在最新Edge浏览器上，已完全静默——下载菜单不再弹出，用户毫无感知。在Chrome上，JavaScript“可能”会打开一个下载下拉窗口，但不会添加任何下载项，且后续启动浏览器时窗口不再出现。普通用户极易将这种异常视为浏览器的小故障，根本不会意识到设备已被控制。

**能力之广，不容小觑。** 成功利用后，攻击者可对受害者浏览器实施以下操控：监控用户浏览活动、将浏览器作为代理跳板匿名访问其他网站、发起分布式拒绝服务攻击（DDoS）、或组建一个由成千上万受感染浏览器构成的僵尸网络，为未来的大规模攻击储备“弹药”。Rebane在最初的漏洞报告中就警告：“创建一个‘僵尸网络’，获得数万次的页面浏览量是完全有可能的，而且人们不会意识到JavaScript可以在他们的设备上远程执行。”

值得注意的是，该漏洞并没有绕过浏览器的安全沙箱边界。正如Rebane所澄清的，它无法让攻击者直接访问用户的电子邮件、文件系统或主机操作系统。但也正是因为这一“局限性”，导致该漏洞在谷歌内部未被充分重视，从而被拖延处理。

#### 42个月的拖延与一次致命的“乌龙”

仔细梳理事件时间线，谷歌漏洞管理流程的疏失清晰可见：

**2022年12月**：Lyra Rebane发现漏洞并私下报告给谷歌。谷歌确认其有效性，并将其列为**P1优先级（第二高）和S2严重性（第三高）**。在内部讨论中，两位开发者分别回应称这是一个“严重的漏洞”。

**2024年10月26日**：在漏洞报告近两年后，一位谷歌开发人员注意到问题仍未解决，再次将其描述为“严重的漏洞”，并请求状态更新“以确保取得进展”。

**2026年2月10日**：该问题首次被标记为“已解决”，但仅几分钟后就因存在问题被重新开启。

**2026年2月12日**：问题再次被标记为“已修复”，但实际补丁并未推出。系统自动向Rebane发放了**1000美元**的漏洞赏金。在旁观的同行看来，这笔微不足道的赏金与漏洞的严重性和等待时间形成了刺眼对比。

**2026年5月20日**：根据Chromium问题追踪器规则，标记为“已修复”超过14周的问题会自动解除访问限制。漏洞细节与PoC代码因此对全世界公开。Rebane在公开当天测试后，发现漏洞在最新版本中依然有效，随即将这一荒谬的局面公之于众。谷歌随后将帖子重新设为私密，但为时已晚。

#### 影响范围与应对措施

该漏洞影响所有基于Chromium的浏览器。Rebane确认受影响的有Chrome、Edge、Brave、Opera、Vivaldi和Arc。**Firefox和Safari不受影响**，因为它们不支持Background Fetch API。

一位开发者曾在内部讨论中指出，后台获取功能在Chrome上的使用率极低，平均每位用户每天仅完成“约17个文件”，以此推断“没有什么可怕的大规模事件发生”。但这一数据仅反映Chrome的情况，且无法排除小规模、高针对性的攻击正在发生。

在官方补丁发布前，用户可采取以下临时防御措施：对无故出现的下载弹窗保持高度警惕；高级用户可通过uBlock Origin等内容拦截器注入内容安全策略（CSP），使用规则如`||$csp=worker-src ‘none’`来禁用Service Worker，但可能影响部分扩展的正常功能。最根本的解决方案仍是及时安装谷歌即将发布的浏览器更新。

网友评论

1. 嘲讽谷歌的双重标准与拖延：主流声音指责谷歌对自身产品拖延42个月，却以90天期限约束第三方，凸显其虚伪，被讽“终于对自己开火”。

2. 调侃“自爆”的荒谬性：大量评论戏谑谷歌发布自家产品零日漏洞的离奇场面，质疑“难道指望谷歌给谷歌施压来修复谷歌代码？”

3. 猜测内部政治或蓄意泄露：不少人认为非单纯失误，可能是内斗或员工故意公开以逼修复，称为“内部政变”或“辞职宣言”。

4. 震惊于持久后门的隐蔽性：用户对重启后仍维持连接表示“太离谱”，担忧Service Worker沦为“超级Cookie”和无感知肉鸡，已有人报告可疑空弹窗。

5. 呼吁转向Firefox及强化防护：众多网友借此推荐逃离Chromium，转向Firefox，并建议用NoScript等插件禁用Service Worker以防患未然。

---

### 【闲话简评】

Chromium不仅是浏览器，更是无数桌面应用、电子框架的核心，单一底层漏洞足以引发多米诺骨牌式的崩塌风险。更值得深思的是漏洞管理机制本身：一个因“未跨过安全边界”而被轻视的漏洞，竟拖延42个月，最终因自动化流程失控而走向公开。这暴露了大型科技公司在漏洞修复优先级上的认知偏差——不被重视的“受限”能力，在攻击者手中经沙盒化组合后，完全可能成为基础设施级别的威胁。对于用户而言，此役亦敲响警钟：必须建立“浏览器即战场”的认知，及时更新、最小化扩展权限、警惕一切异常，方能在危机四伏的数字环境中保住一隅净土。

### 参考文献

[1] Goodin, D. *Google publishes exploit code threatening millions of Chromium users* [EB/OL]. Ars Technica, 2026-05-21. https://arstechnica.com/security/2026/05/google-publishes-exploit-code-threatening-millions-of-chromium-users/.

[2] Toulas, B. *Google accidentally exposed details of unfixed Chromium flaw* [EB/OL]. BleepingComputer, 2026-05-21. https://www.bleepingcomputer.com/news/security/google-accidentally-exposed-details-of-unfixed-chromium-flaw/.

[3] Rebane, L. [@rebane2001]. \*back in 2022 i found a bug that would let me, with no user interaction, turn any chromium-based browser into a permanent js botnet member...\* [EB/OL]. Infosec Exchange, 2026-05-20. https://infosec.exchange/@rebane2001/116606719764376414.

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

网空闲话plus

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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