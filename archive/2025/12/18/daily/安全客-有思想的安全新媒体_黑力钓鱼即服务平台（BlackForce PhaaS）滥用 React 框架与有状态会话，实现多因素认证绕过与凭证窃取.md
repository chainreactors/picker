---
title: 黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取
url: https://www.anquanke.com/post/id/313827
source: 安全客-有思想的安全新媒体
date: 2025-12-18
fetch_date: 2025-12-19T03:21:21.285465
---

# 黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取

阅读量**24558**

发布时间 : 2025-12-18 09:51:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/blackforce-phaas-weaponizes-react-and-stateful-sessions-to-bypass-mfa-steal-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

钓鱼即服务（PhaaS）市场迎来一个技术成熟的全新威胁角色 —— 一款名为**黑力（BlackForce）** 的钓鱼工具包，它能让网络犯罪分子以惊人的便捷性绕过现代安全防护体系。这款工具包正快速迭代升级，已被发现针对迪士尼、网飞以及敦豪速递等全球知名品牌发起攻击，其利用看似合规的代码库，实现用户凭证窃取与多因素认证（MFA）绕过。

瞻博网络威胁实验室（Zscaler ThreatLabz）发布的一份全新报告详细披露了黑力工具包的崛起过程，该工具包最早于 2025 年 8 月被监测到。它在电报（Telegram）论坛上公开售卖，售价仅为 200 至 300 欧元，却已快速迭代多个版本，从一款简单的凭证窃取工具，蜕变为具备高抗检测能力的有状态攻击平台。

黑力工具包的巨大危险性，在于它能够支持攻击者发起实时攻击，突破传统安全防护层。报告指出：“黑力能够窃取用户凭证，并实施浏览器中间人（MitB）攻击，以此盗取一次性令牌，实现多因素认证的绕过。”

![]()

该工具包的攻击链运行需要人工操作者实时介入。当受害者在钓鱼伪造页面输入初始账号密码后，攻击者会收到提醒通知，随即通过命令与控制（C2）面板，向受害者的浏览器中动态注入伪造的多因素认证验证弹窗。当毫无防备的用户输入短信验证码或认证应用生成的验证码时，攻击者会立即捕获该信息，实时劫持用户会话。

为规避安全检测，黑力通过模仿现代 Web 开发标准来伪装其恶意本质。分析人员发现，这款工具包采用了 React 与 React Router 的生产环境构建版本，这两款框架均为正规企业广泛使用的前端开发工具。

研究人员强调：“黑力钓鱼工具包采用的最高效伪装手段，就是其‘看似合规的代码库’。事实上，恶意 JavaScript 文件中 99% 以上的内容，都由 React 和 React Router 的生产环境构建代码构成，这使其具备了高度合法的外观特征。”

此外，该工具包还借助 \*\*“缓存清除” 技术 \*\* 强化伪装效果 —— 它会使用诸如`index-[hash].js`这类带哈希值的文件名，强制浏览器加载新的脚本文件。这种技术本是专业 Web 开发中的标准做法，却被攻击者滥用，以此规避基于静态特征的安全检测。

最值得警惕的一点，是这款工具包的迭代速度。短短数月内，其开发者就发布了 3.x、4.x 和 5.x 多个版本，并通过重大架构调整提升工具的抗检测能力。

早期的 3.x 版本属于 \*\*“无状态” 架构 \*\*，受害者只需简单刷新页面，就能清除浏览器内存中已被窃取的数据，导致攻击流程中断。而更新的 4.x 与 5.x 版本则进化为 \*\*“有状态” 架构 \*\*。

通过利用浏览器的`sessionStorage`（会话存储）功能，该恶意工具现在可以 “在整个用户会话周期内持久化保存窃取到的凭证，构建起流畅且抗干扰的多阶段攻击流程，即使用户刷新页面也不会失效”。这意味着，即便出现网络错误，攻击者也不会丢失已窃取的用户数据。

黑力工具包还设置了严格的过滤机制，确保只有真实受害目标才能进入钓鱼着陆页。它通过服务端黑名单，过滤掉安全厂商、网络爬虫以及安全研究人员的访问流量。后续版本甚至强制开启 “仅限移动设备访问” 策略，直接拒绝桌面端用户访问，以此规避通常运行在工作站上的安全分析工具。

瞻博网络威胁实验室在报告结论中指出：“黑力工具包的开发者正在积极对其进行修改与优化，短期内快速推出多个版本就是直接证据。” 同时，实验室警告各组织机构应尽快部署零信任架构，以降低此类账号劫持攻击带来的危害范围。

本文翻译自securityonline [原文链接](https://securityonline.info/blackforce-phaas-weaponizes-react-and-stateful-sessions-to-bypass-mfa-steal-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313827](/post/id/313827)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/blackforce-phaas-weaponizes-react-and-stateful-sessions-to-bypass-mfa-steal-credentials/)

如若转载,请注明出处： <https://securityonline.info/blackforce-phaas-weaponizes-react-and-stateful-sessions-to-bypass-mfa-steal-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **820**

* 粉丝
* **6**

### TA的文章

* ##### [惠普预测：2026 年人工智能驱动型网络威胁与 Cookie 窃取攻击将激增](/post/id/313832)

  2025-12-18 09:52:40
* ##### [黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取](/post/id/313827)

  2025-12-18 09:51:49
* ##### [新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击](/post/id/313823)

  2025-12-18 09:51:11
* ##### [“幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取](/post/id/313818)

  2025-12-18 09:50:33
* ##### [青少年体育赛事及全美大学体育协会保险理赔数据或遭黑客窃取](/post/id/313816)

  2025-12-18 09:49:40

### 相关文章

* ##### [惠普预测：2026 年人工智能驱动型网络威胁与 Cookie 窃取攻击将激增](/post/id/313832)

  2025-12-18 09:52:40
* ##### [新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击](/post/id/313823)

  2025-12-18 09:51:11
* ##### [“幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取](/post/id/313818)

  2025-12-18 09:50:33
* ##### [青少年体育赛事及全美大学体育协会保险理赔数据或遭黑客窃取](/post/id/313816)

  2025-12-18 09:49:40
* ##### [飞塔防火墙单点登录高危漏洞遭在野利用：攻击者绕过认证并窃取配置文件](/post/id/313811)

  2025-12-18 09:48:51
* ##### [ScreenConnect 高危漏洞（CVE-2025-14265）存在配置泄露与恶意扩展安装风险](/post/id/313807)

  2025-12-18 09:48:07
* ##### [OpenShift GitOps 高危漏洞可致集群沦陷（CVE-2025-13888）—— 低权限用户可提权至 root 权限](/post/id/313803)

  2025-12-18 09:47:20

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)