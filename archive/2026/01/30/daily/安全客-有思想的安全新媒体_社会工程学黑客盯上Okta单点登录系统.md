---
title: 社会工程学黑客盯上Okta单点登录系统
url: https://www.anquanke.com/post/id/314615
source: 安全客-有思想的安全新媒体
date: 2026-01-30
fetch_date: 2026-01-31T04:03:14.839293
---

# 社会工程学黑客盯上Okta单点登录系统

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

# 社会工程学黑客盯上Okta单点登录系统

阅读量**16974**

发布时间 : 2026-01-30 11:26:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mathew J. Schwartz，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/social-engineering-hackers-target-okta-single-sign-on-a-30614>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全专家发出警示：身份认证服务商 Okta 的单点登录（SSO）用户需提高警惕，防范黑客入侵企业网络、窃取数据并实施勒索的行为。

近期针对 Okta 单点登录工具用户的**社会工程学攻击**呈激增态势，受此影响，Okta 上周已直接向用户发布了该攻击活动的预警。据悉，这些攻击行为几乎均由网络犯罪组织**ShinyHunters**实施。

谷歌旗下曼迪昂特咨询集团首席技术官查尔斯・卡马克尔表示：“这是一场持续进行的活跃攻击活动，已有多家企业遭遇数据失窃，而自称 ShinyHunters 的黑客组织已向部分受害企业发出勒索要求。”

这类攻击的特殊之处在于，黑客借助最新一代高度自动化的钓鱼工具包，通过**实时语音对话**实施欺诈，并将用户重定向至仿冒度极高的登录界面，整个攻击流程经过精密策划。

威胁情报公司 Silent Push 指出：“这并非常规的自动化暴力钓鱼攻击，而是由人工主导、高交互性的**语音钓鱼（钓鱼电话）** 操作，即便是加固后的多重身份验证（MFA）体系，也可能被其绕过。”

该公司称，黑客所使用的**实时钓鱼面板工具**，能让人工攻击者介入用户的整个登录流程，**实时截获用户凭证与多重认证令牌**，从而立即获取企业管理后台的长期访问权限。拨打钓鱼电话的黑客会按照固定脚本引导受害者，完成其指定的一系列操作。

一旦黑客成功入侵，往往会开展**横向移动**，利用获取的权限通过 Slack、Teams 等内部通讯工具，对高权限管理员实施社会工程学欺诈。Silent Push 表示，黑客会尝试使用不同身份在企业多重认证系统中完成注册，同时**优先实施快速数据窃取，用于公开勒索**。

赛门铁克威胁情报总监雷夫・皮林称，根据 2025 年 12 月起搭建的恶意基础设施线索判断，**目前已有多达 150 家企业**成为黑客的当前攻击目标或潜在盯上的对象。

他表示：“诈骗者会为每个攻击目标单独注册定制域名，以此窃取用户凭证，并协助自己绕过企业的多重身份验证体系。”

研究人员透露，此次攻击的目标覆盖多个行业，包括大型金融服务机构、医疗健康企业、物流运输公司、制造企业、生物科技与制药公司、科技软件企业以及房地产企业。

皮林指出，截至目前，该攻击活动的目标似乎仅针对使用 Okta 系统的企业，但 ShinyHunters 及同类组织此前曾攻击过各类单点登录服务商，这意味着黑客的攻击目标范围**很可能会进一步扩大**。

针对这类并未利用厂商软件漏洞、由人工主导的实时钓鱼攻击，**最有效的防御手段**仍是搭建完善的多重身份验证体系。

曼迪昂特的卡马克尔表示：“我们强烈建议企业尽可能采用**抗钓鱼多重认证方案**，例如 FIDO2 安全密钥或通行密钥，这类防护手段能有效抵御社会工程学攻击，这是推送式认证或短信认证无法做到的。”

他还称：“管理员还应制定严格的应用授权策略，并对日志进行监控，及时发现异常的 API 操作行为或未授权的设备注册行为。”

Silent Push 建议，企业需向员工发出预警，告知其该活跃攻击活动可能会直接针对个人，并为员工举例说明黑客的攻击手段，同时建立**线下验证渠道**，让员工能够确认与其沟通的是否为企业真实的 IT 部门。

该公司表示：“若员工在此期间收到任何可疑信息、来电或邮件，应立即上报给管理人员与安全团队进行核查。”

ShinyHunters 组织诞生于西方以青少年为主的网络犯罪社群**The Com**，该组织成员多为英语母语者，常通过拨打钓鱼电话伪装成 IT 技术支持人员实施攻击，且会随意使用不同的组织旗号，近期使用的旗号包括**Scattered Lapsus$ ShinyHunters**。

威胁情报机构 Unit 221B 首席研究官艾莉森・尼克松表示，从 ShinyHunters 及 Scattered Lapsus$ ShinyHunters 此前的攻击行径来看，任何遭遇此次攻击的受害企业，都可能面临**黑客的反复勒索**、黑客利用已窃取数据实施的虚假欺诈，即便支付赎金，也会遭遇多次二次勒索。

她直言：“毫无疑问，向 The Com 社群旗下的勒索软件组织支付赎金毫无意义。这些组织根本不理解俄罗斯勒索软件的商业模式为何能运作，受害者也无法得到其承诺的结果，因此这些勒索者一分钱都不配得到。”

尼克松表示：“无论是否支付赎金，最终结果都是一样的。企业不如省下这笔钱，专注于开展事件响应工作，以及处理后续必须完成的法律相关文书工作。”

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/social-engineering-hackers-target-okta-single-sign-on-a-30614)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314615](/post/id/314615)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/social-engineering-hackers-target-okta-single-sign-on-a-30614)

如若转载,请注明出处： <https://www.govinfosecurity.com/social-engineering-hackers-target-okta-single-sign-on-a-30614>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **980**

* 粉丝
* **6**

### TA的文章

* ##### [筑牢聊天安全防线：WhatsApp推出 “严格模式” 抵御飞马间谍软件](/post/id/314636)

  2026-01-30 11:28:04
* ##### [CVE-2026-24765：PHPUnit漏洞致CI/CD流水线面临远程代码执行风险](/post/id/314611)

  2026-01-30 11:27:56
* ##### [假意网恋设局，实为安卓间谍软件植入](/post/id/314629)

  2026-01-30 11:27:37
* ##### [重登AI存储王座？三星新一代HBM4即将通过英伟达关键认证，行业格局或将改写](/post/id/314606)

  2026-01-30 11:27:26
* ##### [eScan证实更新服务器遭入侵，黑客借其推送恶意更新](/post/id/314627)

  2026-01-30 11:27:07

### 相关文章

* ##### [筑牢聊天安全防线：WhatsApp推出 “严格模式” 抵御飞马间谍软件](/post/id/314636)

  2026-01-30 11:28:04
* ##### [CVE-2026-24765：PHPUnit漏洞致CI/CD流水线面临远程代码执行风险](/post/id/314611)

  2026-01-30 11:27:56
* ##### [假意网恋设局，实为安卓间谍软件植入](/post/id/314629)

  2026-01-30 11:27:37
* ##### [重登AI存储王座？三星新一代HBM4即将通过英伟达关键认证，行业格局或将改写](/post/id/314606)

  2026-01-30 11:27:26
* ##### [eScan证实更新服务器遭入侵，黑客借其推送恶意更新](/post/id/314627)

  2026-01-30 11:27:07
* ##### [仿冒AI助手：恶意程序ClawdBot以插件形式藏身VS Code，实为特洛伊木马](/post/id/314625)

  2026-01-30 11:26:48
* ##### [信号基金会总裁警示：人工智能代理正让加密技术丧失实际效用](/post/id/314609)

  2026-01-30 11:26:44

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