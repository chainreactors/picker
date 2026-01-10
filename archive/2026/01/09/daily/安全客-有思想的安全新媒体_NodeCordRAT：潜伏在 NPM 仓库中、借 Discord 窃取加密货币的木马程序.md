---
title: NodeCordRAT：潜伏在 NPM 仓库中、借 Discord 窃取加密货币的木马程序
url: https://www.anquanke.com/post/id/314242
source: 安全客-有思想的安全新媒体
date: 2026-01-09
fetch_date: 2026-01-10T03:31:04.002365
---

# NodeCordRAT：潜伏在 NPM 仓库中、借 Discord 窃取加密货币的木马程序

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

# NodeCordRAT：潜伏在 NPM 仓库中、借 Discord 窃取加密货币的木马程序

阅读量**15163**

发布时间 : 2026-01-09 17:12:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/nodecordrat-the-trojan-hiding-in-npm-to-steal-crypto-via-discord/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

开源生态系统再次被恶意利用，本次攻击的目标直指**使用加密货币开发库的开发者**。网络安全公司 Zscaler ThreatLabz 于本周发布一份新报告称，其在 npm 软件包仓库中发现一款技术成熟的**远程访问木马（RAT）**。该木马以 Discord 平台作为隐秘的命令与控制中心，专门窃取浏览器登录凭证与加密货币钱包信息。

这款被命名为**NodeCordRAT**的恶意软件，通过三个恶意软件包进行传播，分别为`bitcoin-main-lib`、`bitcoin-lib-js`和`bip40`，这三个恶意包于 2025 年 11 月被首次发现。攻击者煞费苦心地将这些恶意包命名为模仿知名项目`bitcoinjs`旗下的正规工具，以此诱导开发者下载使用。

NodeCordRAT 的**独特之处**在于，它依托主流聊天平台 Discord 实现对受感染设备的管控。攻击者并未搭建专用的恶意服务器，而是直接利用 Discord 的自有基础设施发送指令、接收窃取的数据。

报告中指出：“威胁实验室将这款新型恶意软件家族命名为 NodeCordRAT，正是因为它通过 npm 仓库传播，且借助 Discord 服务器完成命令与控制（C2）通信。”

通过调用 Discord 的应用程序编程接口（API），这款恶意软件能够将自身的恶意流量**混入正常的用户交互数据**中，使得传统安全工具难以对其进行识别检测。

NodeCordRAT 通常会借助伪造开发库中的`postinstall`脚本完成安装，一旦植入成功，便会立刻启动大规模的数据窃取行动。它主要瞄准三类高价值数据：

1. **谷歌浏览器凭证**：恶意软件会 “提取并上传谷歌浏览器配置文件中的登录数据 SQLite 数据库文件与本地状态文件（Local State）”。
2. **加密货币钱包数据**：专门搜索 MetaMask 钱包的相关数据，定位包含 “MetaMask 浏览器扩展程序 ID（`nkbihfbeogaeaoehlefnkodbefgpgknn`）” 的文件。
3. **敏感机密信息**：在用户的主目录中**递归搜索**所有文件名包含`.env`的文件，企图从中获取应用程序编程接口（API）密钥与环境变量。

窃取到的数据并不会上传至某台服务器，而是以聊天消息的形式直接发送。报告详细说明，这款恶意软件会使用一个硬编码的机器人令牌（bot token），将窃取的文件上传至一个私密的 Discord 频道。

“被盗文件会通过 Discord 的 REST 接口以消息附件的形式上传…… 在上传数据之前，NodeCordRAT 会先验证每个目标文件是否存在且不为空。”

如果文件传输失败，该恶意软件甚至会向攻击者发送提示性的错误信息，例如 “文件发送失败……”。

威胁实验室的研究人员在报告结论中发出警告：“尽管这三个恶意软件包已被从 npm 仓库中移除，但未来类似的**软件供应链威胁仍会持续出现**。”

研究人员强烈建议开发者，务必严格核查项目中引入的各类开发库的真实性，尤其是那些用于比特币交易等敏感金融操作的工具库。

本文翻译自securityonline [原文链接](https://securityonline.info/nodecordrat-the-trojan-hiding-in-npm-to-steal-crypto-via-discord/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314242](/post/id/314242)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/nodecordrat-the-trojan-hiding-in-npm-to-steal-crypto-via-discord/)

如若转载,请注明出处： <https://securityonline.info/nodecordrat-the-trojan-hiding-in-npm-to-steal-crypto-via-discord/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **900**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2025-60262：H3C无线设备存在严重配置缺陷，攻击者可借此获取设备控制权](/post/id/314220)

  2026-01-09 17:15:06
* ##### [“幽灵刷卡” 来袭：新型安卓恶意软件将手机变为数字扒手](/post/id/314224)

  2026-01-09 17:14:40
* ##### [一招制胜：趋势科技高危漏洞（CVE-2025-15471）可致设备完全沦陷](/post/id/314227)

  2026-01-09 17:14:19
* ##### [疯狂猎手：肆虐医疗领域的“冷酷型”勒索软件](/post/id/314232)

  2026-01-09 17:13:58
* ##### [“虚拟机隔离并非绝对”：研究人员揭露高复杂度VMware ESXi“主控程序”（Maestro）漏洞攻击手段](/post/id/314235)

  2026-01-09 17:13:35

### 相关文章

* ##### [CVE-2025-60262：H3C无线设备存在严重配置缺陷，攻击者可借此获取设备控制权](/post/id/314220)

  2026-01-09 17:15:06
* ##### [“幽灵刷卡” 来袭：新型安卓恶意软件将手机变为数字扒手](/post/id/314224)

  2026-01-09 17:14:40
* ##### [一招制胜：趋势科技高危漏洞（CVE-2025-15471）可致设备完全沦陷](/post/id/314227)

  2026-01-09 17:14:19
* ##### [疯狂猎手：肆虐医疗领域的“冷酷型”勒索软件](/post/id/314232)

  2026-01-09 17:13:58
* ##### [“虚拟机隔离并非绝对”：研究人员揭露高复杂度VMware ESXi“主控程序”（Maestro）漏洞攻击手段](/post/id/314235)

  2026-01-09 17:13:35
* ##### [具备自学习能力的人工智能模型：有望催生超级智能，风险亦如影随形](/post/id/314239)

  2026-01-09 17:13:13
* ##### [欧洲空间局再曝数据泄露事件：500GB 敏感数据遭窃取](/post/id/314245)

  2026-01-09 17:12:22

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