---
title: Chrome网络商店陷入围攻：发现40多个恶意扩展程序窃取数据
url: https://www.anquanke.com/post/id/307749
source: 安全客-有思想的安全新媒体
date: 2025-05-27
fetch_date: 2025-10-06T22:23:27.628566
---

# Chrome网络商店陷入围攻：发现40多个恶意扩展程序窃取数据

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

# Chrome网络商店陷入围攻：发现40多个恶意扩展程序窃取数据

阅读量**78698**

发布时间 : 2025-05-26 13:11:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/chrome-web-store-under-siege-40-malicious-extensions-found-stealing-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![Chrome 网上商店恶意软件,浏览器劫持]()

LayerX已经发现了三个协调的网络钓鱼活动涉及的40多个恶意浏览器扩展程序 – 许多仍然存在于Chrome网上商店中 – 对个人和组织都构成重大风险。

这项研究建立在DomainTools Intelligence(DTI)团队的早期发现的基础，揭示了这些活动的内部运作以及攻击者渗透用户浏览器以窃取数据,冒充身份和破坏公司网络的惊人易用性。

“LayerX已经确定了40多个恶意浏览器扩展,这些扩展程序是三种不同网络钓鱼活动的一部分。

与针对零日漏洞的复杂漏洞漏洞漏洞不同,此活动依赖于欺骗性品牌和可信平台来吸引用户自愿安装恶意工具。这些扩展伪装成:

* Fortinet VPN(英语:FortiVPN)
* Calendly 调度助理
* 加密公用事业,如DeBank和AML部门
* 人工智能生产力工具和YouTube助手

*“这些扩展是经过精心制作的,以模仿知名平台……有效地绕过了用户的怀疑*,”LayerX报道。

安装后,每个扩展程序都会允许威胁行为者持续访问用户会话,允许他们窃取 Cookie、会话令牌、注入恶意脚本,甚至在企业环境中冒充用户。

LayerX研究人员发现,许多扩展着陆页是使用AI工具生成的,导致数十个条目中异常均匀的元数据和格式。

*“恶意扩展页面表现出高度相似的结构……指出它们使用AI工具自动生成的可能性*,”研究人员指出。

此外[,](https://securityonline.info/bitdefender-gravityzone-small-business-security-review-enterprise-grade-protection-without-the-enterprise-headache/)攻击者注册了类似的域名(例如,calendly-daily [.]com,aiwriter[.]expert,crypto-whale[.]top),并使用匹配的电子邮件(如support@domain-name)看起来是合法的。

与从 Chrome Store 中删除的恶意应用程序不同,这些扩展程序可以无限期地在用户浏览器上保持活动状态,如果不是手动删除。

*“从商店中删除不会从用户的浏览器中删除活动安装*,”LayerX警告说。

随着企业员工越来越依赖基于浏览器的工具,这些扩展作为云应用程序、敏感文档和受会话保护数据的静音后门。

LayerX建议针对这种不断上升的浏览器威胁进行几种可操作的防御:

1. **执行扩展卫生:**
   * 阻止来自未知或未经验证的出版商的扩展。
   * 限制最近发布的扩展,具有低评论或可疑权限。
   * 使用欺骗品牌名称或可疑域监控扩展。
2. **按扩展 ID 划分的块:**
   * 使用 MDM 或浏览器策略执行来阻止已知的恶意扩展 ID(在 LayerX 的完整报告中提供)。
3. **持续浏览器安全监控:**
   * 实施持续评估扩展行为、风险和政策合规性的工具。

本文翻译自securityonline [原文链接](https://securityonline.info/chrome-web-store-under-siege-40-malicious-extensions-found-stealing-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307749](/post/id/307749)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/chrome-web-store-under-siege-40-malicious-extensions-found-stealing-data/)

如若转载,请注明出处： <https://securityonline.info/chrome-web-store-under-siege-40-malicious-extensions-found-stealing-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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