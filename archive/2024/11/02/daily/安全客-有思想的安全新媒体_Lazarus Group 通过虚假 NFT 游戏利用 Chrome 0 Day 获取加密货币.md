---
title: Lazarus Group 通过虚假 NFT 游戏利用 Chrome 0 Day 获取加密货币
url: https://www.anquanke.com/post/id/301490
source: 安全客-有思想的安全新媒体
date: 2024-11-02
fetch_date: 2025-10-06T19:12:15.720464
---

# Lazarus Group 通过虚假 NFT 游戏利用 Chrome 0 Day 获取加密货币

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

# Lazarus Group 通过虚假 NFT 游戏利用 Chrome 0 Day 获取加密货币

阅读量**67748**

发布时间 : 2024-11-01 10:50:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/north-korean-hackers-crypto-deceptive-game-zero-day-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

**来自 Lazarus Group 的朝鲜黑客利用谷歌 Chrome 浏览器中的零日漏洞，针对加密货币投资者推出了一款具有欺骗性的虚假 NFT 游戏。攻击者利用社交工程和恶意软件窃取敏感数据，并可能部署进一步的恶意软件。**

臭名昭著的朝鲜黑客组织 Lazarus Group 针对加密货币投资者发起了一场复杂的攻击活动。卡巴斯基研究人员发现，这一活动涉及多层攻击链，利用了社交工程、虚假游戏网站和谷歌 Chrome 浏览器中的零日漏洞。

报告称，卡巴斯基全面安全公司在 2024 年 5 月发现了一个新的攻击链，目标是一名使用 Manuscrypt 后门的未具名俄罗斯国民的个人电脑。

卡巴斯基研究人员鲍里斯-拉林（Boris Larin）和瓦西里-别尔德尼科夫（Vasily Berdnikov）估计，该活动始于2024年2月。深入研究后，研究人员发现攻击者创建了一个名为 “detankzonecom ”的网站，该网站似乎是 “DeFiTankZone ”游戏的合法平台。

据称，这款游戏将去中心化金融（DeFi）元素与非可充值代币（NFT）结合在一起，采用多人在线竞技场（MOBA）设置。该网站甚至提供了一个可下载的试用版，进一步强化了其合法性的假象。然而，表面之下隐藏着一个恶意陷阱。

![Lazarus Group Exploits Chrome 0-Day for Crypto with Fake NFT Game]()
假冒的 NFA 游戏网站和隐藏的漏洞加载器（Via Kaspersky）

研究人员写道：“在引擎盖下，这个网站有一个隐藏脚本，可以在用户的谷歌 Chrome 浏览器中运行，启动零日漏洞利用，让攻击者完全控制受害者的电脑。”

该漏洞包含两个漏洞的代码：一个允许攻击者从 JavaScript 访问 Chrome 浏览器进程的整个地址空间（CVE-2024-4947），第二个允许绕过 V8 沙箱访问寄存器数组边界之外的内存。谷歌在 2024 年 3 月修补了 V8 JavaScript 和 WebAssembly 引擎中的 CVE-2024-4947 类型混乱漏洞，但目前还不清楚攻击者是更早发现了该漏洞并将其作为零日漏洞加以利用，还是将其作为 N 日漏洞加以利用。

N-day漏洞指的是已经被发现、公开披露并通常由软件供应商修补或缓解的安全漏洞或弱点。N 天 “一词表示该漏洞已被发现 ”n “天，其中 n 代表自该漏洞首次披露或修补以来的天数。

成功利用漏洞后，攻击者会部署一个自定义脚本（验证器）来收集系统信息，并确定受感染设备是否拥有任何值得进一步利用的有价值资产。这一阶段之后交付的具体有效载荷尚不清楚。

在此次活动中，Lazarus 利用 X（前 Twitter）和 LinkedIn 等社交媒体平台，锁定了加密货币领域有影响力的人物。他们在 X 上建立了一个拥有多个账户的社交媒体，积极推广虚假游戏，并利用生成式人工智能和图形设计师为 DeTankZone 游戏创建高质量的宣传内容。此外，该团伙还向感兴趣的个人发送专门制作的电子邮件，冒充区块链公司或游戏开发商寻求投资机会。

DeTankZone 网站本身似乎是建立在一个名为 DeFiTankLand (DFTL) 的合法区块链游戏被盗源代码的基础上。这款游戏在 2024 年 3 月出现了安全漏洞，导致价值 2 万美元的加密货币被盗。

虽然开发者怀疑是内部人员所为，但卡巴斯基研究人员认为，Lazarus Group 可能对此次盗窃和将被盗源代码用于恶意活动负有责任。

这一活动凸显了 Lazarus 集团不断演变的策略。警惕未经请求的投资机会至关重要，尤其是那些涉及可下载游戏客户端或可疑社交媒体促销的机会。此外，保持 Chrome 浏览器等浏览器软件的更新，打上最新的安全补丁，对于降低零日漏洞的风险至关重要。

本文翻译自hackread [原文链接](https://hackread.com/north-korean-hackers-crypto-deceptive-game-zero-day-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301490](/post/id/301490)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/north-korean-hackers-crypto-deceptive-game-zero-day-exploit/)

如若转载,请注明出处： <https://hackread.com/north-korean-hackers-crypto-deceptive-game-zero-day-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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