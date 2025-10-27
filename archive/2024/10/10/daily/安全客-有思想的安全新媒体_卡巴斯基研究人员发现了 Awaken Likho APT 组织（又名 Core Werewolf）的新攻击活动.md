---
title: 卡巴斯基研究人员发现了 Awaken Likho APT 组织（又名 Core Werewolf）的新攻击活动
url: https://www.anquanke.com/post/id/300661
source: 安全客-有思想的安全新媒体
date: 2024-10-10
fetch_date: 2025-10-06T18:51:44.672279
---

# 卡巴斯基研究人员发现了 Awaken Likho APT 组织（又名 Core Werewolf）的新攻击活动

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

# 卡巴斯基研究人员发现了 Awaken Likho APT 组织（又名 Core Werewolf）的新攻击活动

阅读量**64663**

发布时间 : 2024-10-09 11:27:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/new-campaign-by-awaken-likho-apt-group-changes-in-software-and-techniques/>

译文仅供参考，具体内容表达以及含义原文为准。

卡巴斯基研究人员发现了 Awaken Likho APT 组织（又称 Core Werewolf）的新活动，该组织至少从 2021 年 7 月起就开始活跃。据了解，该组织以俄罗斯政府机构和工业企业为目标。最新的攻击活动始于 2024 年 6 月，这表明攻击者改变了他们的软件和技术。

以前，Awaken Likho 利用 UltraVNC 模块进行远程访问，但他们最近的行动表明，他们已转向使用 MeshAgent（合法 MeshCentral 平台的代理）。MeshCentral 是一个开源解决方案，设计用于远程设备管理，但在这些攻击者手中，它却成了未经授权控制被入侵系统的有力武器。

卡巴斯基称，”攻击者在攻击中使用的软件发生了很大变化。攻击者现在更喜欢使用合法的 MeshCentral 平台代理，而不是 UltraVNC 模块”。这一转变标志着 APT 组织的运作方式发生了重大变化，使他们的攻击更难被发现和缓解。

在调查过程中，卡巴斯基团队发现了通过钓鱼邮件发送的新植入程序，这是 Awaken Likho 的标志性技术。虽然他们无法检索到原始的钓鱼邮件，但之前的攻击表明该病毒使用了自解压压缩文件（SFX）和恶意模块来传输有效载荷。

![]()
以 “#”模式打开的压缩包内容 | 图片： 卡巴斯基

所分析的植入程序是通过使用 7-Zip 创建的 SFX 发布的。卡巴斯基解释说，“该压缩包包含五个文件，其中四个伪装成合法的系统服务和命令文件”。这些诱饵文件用于误导受害者，而真正的有效载荷则在后台悄无声息地运行。

解压缩后，植入程序会运行 MicrosoftStores.exe，这是一个包含编译 AutoIt 脚本的文件。卡巴斯基专家在对该脚本进行解密后发现，它可以启动两个关键组件： NetworkDrivers.exe是MeshAgent，而nKka9a82kjn8KJHA9.cmd是一个严重混淆的命令文件。

植入的最终目的是持久性。通过创建名为 MicrosoftEdgeUpdateTaskMachineMS 的计划任务，攻击者可确保 MeshAgent 重新连接到命令与控制 (C2) 服务器。服务器连接是使用 WebSocket 协议建立的，“通过 HTTPS 打开该地址时，会显示 MeshCentral 平台的登录表单”，这一点得到了证实。

唤醒 Likho APT
MeshCentral 平台登录界面 | 图片： 卡巴斯基

此次活动的主要目标与 Awaken Likho 之前的活动保持一致–俄罗斯政府机构、承包商和工业企业。根据所采用的战术、技术和程序（TTPs），卡巴斯基非常有把握地将此次活动归因于 Awaken Likho 组织。

这些攻击开始于俄乌冲突开始后不久，其时机突出表明了该组织的政治动机。“卡巴斯基指出：”Awaken Likho 是在俄乌冲突开始后加紧活动的威胁行为体之一。

随着该 APT 组织不断完善其武器库，各组织，尤其是俄罗斯政府和工业部门的组织，必须保持警惕。

通过www.DeepL.com/Translator（免费版）翻译

本文翻译自securityonline [原文链接](https://securityonline.info/new-campaign-by-awaken-likho-apt-group-changes-in-software-and-techniques/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300661](/post/id/300661)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-campaign-by-awaken-likho-apt-group-changes-in-software-and-techniques/)

如若转载,请注明出处： <https://securityonline.info/new-campaign-by-awaken-likho-apt-group-changes-in-software-and-techniques/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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