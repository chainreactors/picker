---
title: Ultralytics 人工智能库遭受供应链攻击： 6000 万次下载遭到破坏
url: https://www.anquanke.com/post/id/302523
source: 安全客-有思想的安全新媒体
date: 2024-12-10
fetch_date: 2025-10-06T19:33:14.797785
---

# Ultralytics 人工智能库遭受供应链攻击： 6000 万次下载遭到破坏

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

# Ultralytics 人工智能库遭受供应链攻击： 6000 万次下载遭到破坏

阅读量**46579**

发布时间 : 2024-12-09 10:44:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/ultralytics-ai-library-hit-by-supply-chain-attack-60-million-downloads-compromised/>

译文仅供参考，具体内容表达以及含义原文为准。

![Ultralytics Supply Chain Attack]()

ReversingLabs 的网络安全研究人员详细介绍了针对流行人工智能库 Ultralytics 的供应链攻击，该库在 PyPI 上的下载量已超过 6000 万次。12 月 4 日披露的这次攻击涉及恶意版本（8.3.41）的库，该库被伪装成部署了 XMRig 加密货币矿机。这次入侵是通过针对 GitHub Actions 脚本的复杂漏洞精心策划的。

报告称，攻击者利用了一个已知的 GitHub Actions 脚本注入漏洞，使他们能够在 Ultralytics 的构建环境中执行任意代码。ReversingLabs 详细描述道：“恶意行为者成功入侵了与上述项目相关的构建环境，并在代码审查部分结束后注入了恶意代码。”

攻击者使用 GitHub 用户账户 openimbot 创建了恶意拉取请求，并在分支名称中嵌入了有效载荷代码。这触发了对被入侵环境的后门访问，导致 XMRig 挖币机下载器代码的注入。

此次事件中最令人担忧的问题之一是缓解过程处理不当。12 月 5 日作为 “安全 ”更新发布的 8.3.42 版无意中包含了与 8.3.41 版相同的恶意代码。直到当天晚些时候，8.3.43 版才发布，解决了这一问题。

该恶意软件嵌入了downloads.py和model.py等关键文件，展示了特定平台行为，以根据目标系统调整有效载荷的交付。报告指出：“下载特定平台有效载荷的代码是可见的。”

行为分析还揭示了与文件系统相关的变化，以及旨在利用受害者的计算资源挖掘加密货币的有效载荷。虽然这次的影响仅限于加密货币挖矿，但专家警告说，这有可能部署更具破坏性的恶意软件，如后门或远程访问木马。

本文翻译自securityonline [原文链接](https://securityonline.info/ultralytics-ai-library-hit-by-supply-chain-attack-60-million-downloads-compromised/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302523](/post/id/302523)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ultralytics-ai-library-hit-by-supply-chain-attack-60-million-downloads-compromised/)

如若转载,请注明出处： <https://securityonline.info/ultralytics-ai-library-hit-by-supply-chain-attack-60-million-downloads-compromised/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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