---
title: n8n供应链攻击：滥用社区节点窃取OAuth令牌
url: https://www.anquanke.com/post/id/314316
source: 安全客-有思想的安全新媒体
date: 2026-01-14
fetch_date: 2026-01-15T03:28:04.008124
---

# n8n供应链攻击：滥用社区节点窃取OAuth令牌

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

# n8n供应链攻击：滥用社区节点窃取OAuth令牌

阅读量**24427**

发布时间 : 2026-01-14 13:00:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

有监测显示，威胁攻击者在 npm 软件包仓库中上传了八个恶意软件包。这些软件包伪装成面向 n8n 工作流自动化平台的集成插件，其真实目的是窃取开发者的 OAuth 身份凭证。

其中一款名为`n8n-nodes-hfgjf-irtuinvcm-lasdqewriit`的软件包，仿冒了谷歌广告的集成功能。它会诱导用户通过一个看似正规的表单绑定广告账户，随后将用户的 OAuth 凭证窃取并传输至攻击者控制的服务器中。

恩多尔实验室在其上周发布的一份报告中指出：**“此次攻击标志着供应链威胁进入了全新的升级阶段。”** 与传统的 npm 恶意软件不同 —— 这类软件往往以窃取开发者个人凭证为目标，而此次攻击则直接针对工作流自动化平台。这类平台本身相当于一个集中式凭证存储库，会将谷歌广告、Stripe 支付、Salesforce 客户管理等数十种集成服务的 OAuth 令牌、API 密钥以及敏感凭证统一存储。

目前已被确认并下架的恶意软件包完整名单如下：

* `n8n-nodes-hfgjf-irtuinvcm-lasdqewriit`（下载量 4241 次，作者：kakashi-hatake）
* `n8n-nodes-ggdv-hdfvcnnje-uyrokvbkl`（下载量 1657 次，作者：kakashi-hatake）
* `n8n-nodes-vbmkajdsa-uehfitvv-ueqjhhhksdlkkmz`（下载量 1493 次，作者：kakashi-hatake）
* `n8n-nodes-performance-metrics`（下载量 752 次，作者：hezi109）
* `n8n-nodes-gasdhgfuy-rejerw-ytjsadx`（下载量 8385 次，作者：zabuza-momochi）
* `n8n-nodes-danev`（下载量 5525 次，作者：dan\_even\_segler）
* `n8n-nodes-rooyai-model`（下载量 1731 次，作者：haggags）
* `n8n-nodes-zalo-vietts`（下载量 4241 次，作者：vietts\_code、diendh）

截至本文撰写时，npm 用户`zabuza-momochi`、`dan_even_segler`和`diendh`还被列为另外四款仍可下载的软件包的作者，具体如下：

* `n8n-nodes-gg-udhasudsh-hgjkhg-official`（下载量 2863 次）
* `n8n-nodes-danev-test-project`（下载量 1259 次）
* `@diendh/n8n-nodes-tiktok-v2`（下载量 218 次）
* `n8n-nodes-zl-vietts`（下载量 6357 次）

目前尚无法确认这四款软件包是否包含类似的恶意功能。不过，逆向实验室通过 Spectra Assure 工具对前三款软件包进行的安全评估显示，其暂未发现安全隐患；而针对`n8n-nodes-zl-vietts`的分析结果则显示，该软件包中包含一个曾被标记为恶意软件的组件。

**![]()**

值得警惕的是，软件包`n8n-nodes-gg-udhasudsh-hgjkhg-official`的更新版本在三小时前刚刚发布至 npm 仓库，这一迹象表明，**攻击者的此次攻击活动可能仍在持续**。

这类恶意软件包一旦作为社区节点完成安装，其外在表现与其他任何一款 n8n 集成插件无异 —— 会正常显示配置界面，并将谷歌广告账户的 OAuth 令牌以加密形式保存至 n8n 的凭证存储库。但当工作流开始执行时，它会运行恶意代码，利用 n8n 的主密钥对存储的令牌进行解密，随后将这些凭证窃取并外传至远程服务器。

这一攻击事件的出现，标志着供应链威胁首次明确将 n8n 生态系统作为攻击目标。攻击者正是利用了用户对社区集成插件的信任，进而实现其窃取凭证的目的。

此次事件也凸显出一个核心安全隐患：**集成来源不可信的工作流，会大幅扩大企业的攻击面**。研究人员建议，开发者在安装任何软件包前都应进行安全审计，仔细核查软件包的元数据是否存在异常，并优先使用 n8n 官方提供的集成插件。

n8n 官方同样发出警告，提醒用户警惕来自 npm 仓库的社区节点所带来的安全风险。这类节点可能会引入破坏性更新，或在服务运行的主机上执行恶意操作。官方建议，对于自托管的 n8n 实例，可通过将环境变量`N8N_COMMUNITY_PACKAGES_ENABLED`设置为`false`的方式，禁用社区节点功能。

研究人员基兰・拉吉与亨里克・普拉特指出：“**社区节点拥有与 n8n 主程序完全等同的访问权限**。它们可以读取环境变量、访问文件系统、发起对外网络请求，而最关键的一点是，它们能在工作流执行过程中获取到已解密的 API 密钥与 OAuth 令牌。节点代码与 n8n 运行时环境之间，不存在任何沙箱隔离机制。”

“正因如此，一款恶意 npm 软件包就足以让攻击者深度窥探目标系统的工作流、窃取各类凭证，并且在不触发即时警报的情况下实现对外通信。对于攻击者而言，npm 供应链已成为他们潜入 n8n 环境的一条隐蔽且高效的入侵通道。”

**更新补充**

在接受《黑客新闻》采访时，恩多尔实验室证实，npm 软件包`n8n-nodes-gg-udhasudsh-hgjkhg-official`确实为恶意软件，且属于此次攻击活动的一部分；其余三款软件包则被判定为良性。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314316](/post/id/314316)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

如若转载,请注明出处： <https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **920**

* 粉丝
* **6**

### TA的文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22

### 相关文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [高危警报：Moxa交换机存在OpenSSH远程代码执行漏洞（CVSS 9.8）](/post/id/314327)

  2026-01-14 12:59:46
* ##### [ValleyRAT\_S2病毒攻击组织：投放隐匿恶意软件，窃取金融敏感信息](/post/id/314334)

  2026-01-14 12:59:44
* ##### [苹果确认谷歌 Gemini 将为 Siri 提供技术支持，强调隐私仍是核心优先级](/post/id/314310)

  2026-01-14 12:58:29

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