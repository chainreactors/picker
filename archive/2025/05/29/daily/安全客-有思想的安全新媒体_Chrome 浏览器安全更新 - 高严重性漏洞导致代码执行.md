---
title: Chrome 浏览器安全更新 - 高严重性漏洞导致代码执行
url: https://www.anquanke.com/post/id/307922
source: 安全客-有思想的安全新媒体
date: 2025-05-29
fetch_date: 2025-10-06T22:25:25.490320
---

# Chrome 浏览器安全更新 - 高严重性漏洞导致代码执行

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

# Chrome 浏览器安全更新 - 高严重性漏洞导致代码执行

阅读量**146222**

发布时间 : 2025-05-28 14:25:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 古鲁 巴兰，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/chrome-security-update-code-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

谷歌已经正式将Chrome 137推广到Windows、Mac和Linux平台的稳定渠道,标志着浏览器安全和人工智能集成的一个重要里程碑。Chrome团队于2025年5月27日宣布发布,该更新将在未来几天和几周内在全球范围内推出。

适用于 Linux 的 Chrome 137.0.7151.55 和适用于 Windows 和 Mac 的 137.0.7151.55/56 提供了实质性的安全改进,解决了外部研究人员和内部安全团队识别的 11 个漏洞。

该更新解决了几个高严重性问题,包括CVE-2025-5063,[一个匿名研究人员于2025年4月18日报告的Compositing中的无使用漏洞](https://cybersecuritynews.com/tag/use-after-free-vulnerability/),以及CVE-2025-5280,这是安全研究员pwn2car于2025年5月12日发现的V8中一个出界的写问题。

谷歌已经实施了一项全面的漏洞赏金计划,奖励安全研究人员的贡献。值得注意的付款包括莫里斯·道尔(Maurice Dauer)在后台获取API中发现不适当实现的4,000美元,用于NDevTK的FileSystemAccess API发现2,000美元,以及Mohit Raj识别消息漏洞的1,000美元。

该公司继续致力于透明度,同时保持负责任的披露做法,限制对错误详细信息的访问,直到大多数用户收到安全补丁。

| CVE ID 系统 | 严重性 | 类型 | 描述 | 举报 By | 赏金 |
| --- | --- | --- | --- | --- | --- |
| CVE-2025-5063年 | 高 | 在合成中使用后免费 | 在渲染管道中通过精心制作的 HTML 页面堆损坏漏洞 | 匿名(2025-04-18) | TBD |
| CVE-2025-5280年 | 高 | Out-of-bounds 写在V8 | JavaScript引擎中的内存损坏允许潜在的远程代码执行 | pwn2car(2025-05-12) | TBD |
| CVE-2025-5064年 | 中等 | 背景 获取 API 缺陷 | 通过不正确实现后台获取操作的跨源数据泄露 | 莫里斯·道尔(2021-11-29) | 4000元 |
| CVE-2025-5065年 | 中等 | FileSystemAccess API 问题 | UI欺骗攻击,通过精心制作的对话操作实现恶意文件操作 | NDevTK(2022-03-11) | 2000元 |
| CVE-2025-5066年 | 中等 | 消息实现缺陷 | 影响Android Chrome用户的基于UI手势的欺骗漏洞 | 莫希特·拉杰(Mohit Raj)(2024-07- | 1000元 |
| CVE-2025-5281年 | 中等 | BFCache 漏洞 | 通过不适当的后/前端缓存处理潜在的跨源信息泄漏 | 杰斯珀·范登德恩德(Jesper van den Ende) (2025-05-12) | TBD |
| CVE-2025-5283年 | 中等 | libvpx 使用后免费 | 通过恶意媒体内容处理 VP8/VP9 视频处理中的堆腐败 | Mozilla(2025-05-22) | TBD |
| CVE-2025-5067年 | 低 | Tab Strip 实施 | 通过精心制作的标签条传输交互的 UI 欺骗 | 哈利勒·扎尼(2023-10-17) | 500元 |

Chrome 137中最具开创性的功能是集成了谷歌的Gemini Nano大型语言模型,该模型提供了设备内人工智能功能,以对抗复杂的网络威胁。这种创新明确针对技术支持骗局,这些骗局在欺骗用户的方法上变得越来越普遍和复杂。

人工智能系统完全在用户设备上运行,[确保隐私](https://cybersecuritynews.com/tag/privacy/),同时实时分析网页内容。当Chrome检测到特征性诈骗触发器(例如滥用键盘锁定API)时,Gemini Nano通过处理文本、布局和行为线索来评估页面的意图。

这种方法使Chrome能够检测欺骗模式,并为Google的安全浏览服务生成安全信号,提供针对平均平均存在不到10分钟的威胁的保护。

除了安全改进之外,Chrome 137还为Web平台引入了几项重大增强功能。更新包括支持画布渲染上下文中的浮点颜色类型,这对于医疗可视化和高动态范围内容等高精度应用至关重要。

此外,浏览器现在支持SVG`<use>`可以引用外部文档的根元素,而无需显式片段标识符的元素,简化 Web 开发工作流。

该版本还实现了Document-Isolation-Policy,[使文档能够在不部署复杂安全标头的情况下实现跨源隔离](https://cybersecuritynews.com/chrome-134-released-fixes-14-vulnerabilities/),并将Ed25519加密算法支持添加到Web加密API中。

Chrome在浏览器市场的主导地位,截至2024年,在所有平台上拥有约65%的全球市场份额,这意味着这些安全增强将影响全球数十亿用户。

设备上AI的集成代表了浏览器安全性的范式转变,从基于响应式块状防御的防御转向主动的智能威胁检测。

该版本表明谷歌致力于利用人工智能进行网络安全,同时通过设备处理维护用户隐私,在日益复杂的网络威胁时代为浏览器安全设定了新标准。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/chrome-security-update-code-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307922](/post/id/307922)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/chrome-security-update-code-execution/)

如若转载,请注明出处： <https://cybersecuritynews.com/chrome-security-update-code-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53

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