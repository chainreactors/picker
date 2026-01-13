---
title: “粉河豚”攻击行动：银行恶意软件Astaroth转战WhatsApp发起新型攻击
url: https://www.anquanke.com/post/id/314279
source: 安全客-有思想的安全新媒体
date: 2026-01-12
fetch_date: 2026-01-13T03:26:23.188222
---

# “粉河豚”攻击行动：银行恶意软件Astaroth转战WhatsApp发起新型攻击

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

# “粉河豚”攻击行动：银行恶意软件Astaroth转战WhatsApp发起新型攻击

阅读量**17706**

发布时间 : 2026-01-12 17:01:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/boto-cor-de-rosa-banking-malware-astaroth-pivots-to-whatsapp-in-new-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

臭名昭著的巴西银行恶意软件**Astaroth**再度完成迭代升级，此次它将目标瞄准全球最主流的即时通讯平台之一，把该平台变成了传播恶意程序的武器。安克诺斯威胁研究团队（Acronis Threat Research Unit）发现，在这场代号为 \*\*“粉河豚（Boto Cor-de-Rosa）”\*\* 的新型攻击活动中，该恶意软件借助网页版 WhatsApp 进行传播，自动向受害者的联系人列表群发恶意消息。

这种攻击路径的转变，标志着银行恶意软件的发展进入了令人担忧的新阶段 —— 其不再局限于传统的邮件钓鱼诱饵，转而利用个人即时通讯场景中天然存在的信任关系实施攻击。

尽管 Astaroth 多年来一直困扰着巴西地区的用户，但此次最新变种新增了一个**基于 Python 语言开发、专为 WhatsApp 定制的蠕虫模块**。攻击的感染流程始于受害者通过即时通讯软件接收到一个恶意 ZIP 压缩包。

![]()

报告指出：“该恶意压缩包的文件名会随每次攻击发生变化，但始终遵循固定命名模式 —— 由数字和十六进制字符组合而成，不同字符段之间用下划线和短横线分隔”，并举例给出样本文件名，例如`552_516107-a9af16a8-552.zip`。

一旦受害者解压该文件，并运行其中经过伪装的 Visual Basic 脚本，这款恶意软件就会在设备中扎根。但与以往仅窃取账号凭证的攻击目的不同，此次变种会将受感染的设备直接变成一台**垃圾消息发送机器人**。

这个新增模块的核心目标是实现恶意软件的大规模传播。它会劫持受害者的网页版 WhatsApp 会话，获取其联系人列表，然后**自动向列表中的每一位联系人发送恶意消息，以此扩大感染范围**。

这款恶意软件的攻击流程极具条理性。它会定期向攻击者的控制端上报攻击数据，统计内容包括**成功发送的恶意消息数量、发送失败的尝试次数，以及以 “每分钟发送消息数” 为指标的传播速率**。

它甚至具备自我效能计算能力。报告提到：“每发送 50 条消息后，该脚本就会自动计算已处理联系人的占比，以及当前的传播吞吐量”，确保攻击者能够实时掌握恶意软件的扩散态势。

此次攻击的危害不止于恶意软件传播，还会造成严重的隐私泄露。报告披露，该恶意软件组件会**将受害者的联系人列表窃取并上传至远程服务器**，让攻击者获得一批有效的手机号码资源，为后续攻击行动储备目标数据。

从技术架构来看，Astaroth 仍然属于 \*\*“多语言模块化”\*\* 的恶意威胁。其核心攻击载荷依旧由 Delphi 语言编写，安装程序则采用 Visual Basic 语言开发，而新增的 WhatsApp 蠕虫模块则完全基于 Python 语言实现。

这种多技术栈融合的特点，凸显出威胁行为体的技术适配能力正在不断增强。研究人员发出警示：“Astaroth 将即时通讯平台传播机制与银行凭证窃取功能相结合，这一特性代表了恶意软件演进过程中一个值得高度警惕的趋势”。攻击者通过将技术创新与 “熟人文件传输带来的心理诱导” 相结合，大幅提升了攻击的成功率。

此次攻击行动也为所有用户敲响警钟：社交平台中的信任关系，完全可能被恶意行为体利用。报告在结尾强调：“该攻击活动凸显了用户保持警惕的重要性，尤其是在通过即时通讯平台接收陌生文件时，更需严加甄别”。

企业与个人都必须突破 “仅关注邮件安全” 的防护局限，要意识到，下一个重大安全威胁很可能就潜藏在来自好友的聊天窗口之中。

本文翻译自securityonline [原文链接](https://securityonline.info/boto-cor-de-rosa-banking-malware-astaroth-pivots-to-whatsapp-in-new-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314279](/post/id/314279)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/boto-cor-de-rosa-banking-malware-astaroth-pivots-to-whatsapp-in-new-campaign/)

如若转载,请注明出处： <https://securityonline.info/boto-cor-de-rosa-banking-malware-astaroth-pivots-to-whatsapp-in-new-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **910**

* 粉丝
* **6**

### TA的文章

* ##### [XML陷阱：Struts 2高危漏洞CVE-2025-68493致数据泄露](/post/id/314266)

  2026-01-12 17:05:06
* ##### [“粉河豚”攻击行动：银行恶意软件Astaroth转战WhatsApp发起新型攻击](/post/id/314279)

  2026-01-12 17:01:39
* ##### [CVE-2026-22184(CVSS 评分 9.3)zlib高危漏洞引发全球性缓冲区溢出风险](/post/id/314276)

  2026-01-12 17:00:43
* ##### [锈水木马崛起：泥水坑组织弃用PowerShell，改用高隐蔽性Rust植入程序](/post/id/314289)

  2026-01-12 17:00:03
* ##### [执法打击力度加大，2025年勒索软件攻击仍激增47%](/post/id/314260)

  2026-01-12 16:58:40

### 相关文章

* ##### [XML陷阱：Struts 2高危漏洞CVE-2025-68493致数据泄露](/post/id/314266)

  2026-01-12 17:05:06
* ##### [CVE-2026-22184(CVSS 评分 9.3)zlib高危漏洞引发全球性缓冲区溢出风险](/post/id/314276)

  2026-01-12 17:00:43
* ##### [锈水木马崛起：泥水坑组织弃用PowerShell，改用高隐蔽性Rust植入程序](/post/id/314289)

  2026-01-12 17:00:03
* ##### [执法打击力度加大，2025年勒索软件攻击仍激增47%](/post/id/314260)

  2026-01-12 16:58:40
* ##### [泥水坑组织借助鱼叉式钓鱼，在中东多行业部署“锈水”远程访问木马](/post/id/314257)

  2026-01-12 16:58:01
* ##### [数据投毒：2026年新兴人工智能安全防护策略](/post/id/314275)

  2026-01-12 16:56:53
* ##### [印度以应对网络威胁为由要求审查智能手机源代码](/post/id/314272)

  2026-01-12 16:56:12

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