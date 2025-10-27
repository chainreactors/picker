---
title: 警告：HotPage广告软件伪装成广告拦截安装恶意内核驱动程序
url: https://www.anquanke.com/post/id/298095
source: 安全客-有思想的安全新媒体
date: 2024-07-20
fetch_date: 2025-10-06T17:42:25.108317
---

# 警告：HotPage广告软件伪装成广告拦截安装恶意内核驱动程序

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

# 警告：HotPage广告软件伪装成广告拦截安装恶意内核驱动程序

阅读量**97256**

发布时间 : 2024-07-19 11:42:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员揭示了一个广告软件模块，该模块旨在阻止广告和恶意网站，同时秘密卸载内核驱动程序组件，该组件使攻击者能够在 Windows 主机上以提升的权限运行任意代码。

根据 ESET 的新发现，该恶意软件被称为 HotPage，其名称来自同名安装程序（“HotPage.exe”）。

ESET研究员Romain Dumont在今天发表的技术分析中表示，安装程序“部署了一个能够将代码注入远程进程的驱动程序，以及两个能够拦截和篡改浏览器网络流量的库。

“恶意软件可以修改或替换请求页面的内容，将用户重定向到另一个页面，或根据某些条件在新选项卡中打开新页面。”

除了利用其浏览器流量拦截和过滤功能来显示与游戏相关的广告外，它还旨在收集系统信息并将其泄露到与一家名为湖北盾网网络科技有限公司的中国公司相关的远程服务器。

这是通过驱动程序实现的，其主要目标是将库注入浏览器应用程序并更改其执行流程以更改正在访问的 URL，或确保将新 Web 浏览器实例的主页重定向到配置中指定的特定 URL。

这还不是全部。驱动程序没有任何访问控制列表 （ACL） 意味着具有非特权帐户的攻击者可以利用它来获取提升的权限，并以 NT AUTHORITY\System 帐户的身份运行代码。

“这个内核组件无意中为其他威胁打开了大门，让他们以 Windows 操作系统中可用的最高权限级别运行代码：系统帐户，”Dumont 说。由于对这个内核组件的访问限制不当，任何进程都可以与它通信，并利用其代码注入功能来定位任何不受保护的进程。

尽管尚不清楚安装程序的确切分发方法，但斯洛伐克网络安全公司收集的证据表明，它已被宣传为网吧的安全解决方案，旨在通过停止广告来改善用户的浏览体验。

嵌入式驱动程序值得注意的是，它是由 Microsoft 签名的。据信，这家中国公司已经通过了Microsoft的驾驶员代码签名要求，并设法获得了扩展验证（EV）证书。自 2024 年 5 月 1 日起，它已从 Windows Server 目录中删除。

内核模式驱动程序需要经过数字签名才能由 Windows 操作系统加载，这是 Microsoft 建立的重要防御层，用于防止可能被武器化以破坏安全控制并干扰系统进程的恶意驱动程序。

也就是说，思科Talos去年7月透露了母语为中文的威胁行为者如何利用Microsoft Windows策略漏洞在内核模式驱动程序上伪造签名。

“对这种看起来相当通用的恶意软件的分析再次证明，广告软件开发人员仍然愿意加倍努力来实现他们的目标，”Dumont说。

“不仅如此，他们还开发了一个内核组件，其中包含大量操作进程的技术，而且还通过了Microsoft施加的要求，以获取其驱动程序组件的代码签名证书。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298095](/post/id/298095)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [Gunra Ransomware集团声称从美国医院泄露了40 TB数据](/post/id/308534)

  2025-06-17 16:00:49
* ##### [新黑客组织利用 LockBit 勒索软件变种攻击俄罗斯公司](/post/id/308300)

  2025-06-10 13:29:14
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险](/post/id/308238)

  2025-06-09 17:01:38
* ##### [阿联酋中央银行要求金融机构放弃短信和 OTP 身份验证](/post/id/308132)

  2025-06-05 12:29:10
* ##### [警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据](/post/id/308092)

  2025-06-04 15:31:41

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