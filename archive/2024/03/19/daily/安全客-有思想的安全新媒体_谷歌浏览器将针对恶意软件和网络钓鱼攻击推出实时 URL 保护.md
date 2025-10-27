---
title: 谷歌浏览器将针对恶意软件和网络钓鱼攻击推出实时 URL 保护
url: https://www.anquanke.com/post/id/294045
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:43.509115
---

# 谷歌浏览器将针对恶意软件和网络钓鱼攻击推出实时 URL 保护

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

# 谷歌浏览器将针对恶意软件和网络钓鱼攻击推出实时 URL 保护

阅读量**128753**

发布时间 : 2024-03-18 11:14:57

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybersecuritynews.com/google-chrome-real-time-phishing-protection/>

译文仅供参考，具体内容表达以及含义原文为准。

Google Chrome 一直通过安全浏览功能保护用户免受恶意网站和文件的侵害，该功能会维护每 30-60 分钟更新一次的本地存储列表。

由于不安全网站可能在 10 分钟内出现并消失，因此它变得不够。为了解决这个问题，Chrome 推出了新版本的安全浏览，可在不损害用户隐私的情况下提供实时 URL 保护。

这可以通过一个新的 API 来实现，该 API 根据实时列表检查 URL，而不向 Google 透露实际 URL，提高对短期威胁的防护，并更好地应对不断增长的恶意网站。

![]()

![]()

## 实时且保护隐私的安全浏览

Chrome 利用实时安全浏览来识别不安全的网站。访问 URL 时，它首先检查本地缓存中是否有已知的安全地址；如果未找到，则对该 URL 进行实时检查。

为了保护用户隐私，它会在将 URL 发送到安全浏览服务器之前通过散列和加密来混淆 URL。服务器解密，将哈希值与其不安全 URL 数据库进行比较，然后返回匹配的完整哈希值。

Chrome 最终会根据访问的 URL 的哈希值检查收到的总哈希值，如果匹配则显示警告，并针对新出现的威胁启用实时保护。

根据 Google Chrome**[博客文章](https://security.googleblog.com/2024/03/blog-post.html)**，为了保护用户身份，Fastly 的 Oblivious HTTP ( [OHTTP](https://datatracker.ietf.org/doc/rfc9458/) ) 服务器充当自身和安全浏览之间的中介，在将 URL 哈希前缀（混淆的网站地址）发送到安全浏览进行安全检查之前，先屏蔽 IP 地址。

[Chrome](https://cybersecuritynews.com/chrome-use-after-free-flaw-crash/)使用安全浏览的公钥对这些前缀进行加密，确保中间服务器无法解密它们。

匿名前缀到达安全浏览，安全浏览使用其私钥对其恶意站点数据库进行解密和验证。

它在没有 IP 的情况下中继加密的前缀，并且中间服务器在不查看实际 URL 数据的情况下处理 IP 地址。同时，双方都不拥有用户身份和浏览信息，保护您的隐私。

![]()

![]()

为了平衡安全性和浏览速度，Chrome 采用了两层缓存系统以及实时检查网站安全性。它首先查阅先前验证的 URL 的本地缓存和已知安全的 URL 哈希值的全局列表。

如果存在匹配，则使用更快的基于哈希的检查而不是实时请求；如果失败，Chrome 会尝试进行实时检查。

如果不成功或缓慢，它会实现回退机制，暂时恢复到基于哈希的检查并探索异步加载以防止页面延迟。

## Chrome 的安全浏览通过增强的隐私获得实时保护

Chrome 的安全浏览得到了升级，因为标准保护现在利用实时 URL 检查，而不会向 Google 泄露用户从已知恶意网站的浏览历史记录。

![]()

![]()

仍然建议增强保护以实现额外的安全层，包括针对尚未识别的威胁以及可疑扩展和文件的保护。

实时功能默认使用隐私服务器（快速）进行检查。相比之下，开发人员可以期待安全浏览 API 很快就能在其应用程序中提供类似的隐私保护。

本文翻译自 [原文链接](https://cybersecuritynews.com/google-chrome-real-time-phishing-protection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294045](/post/id/294045)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybersecuritynews.com/google-chrome-real-time-phishing-protection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**3赞

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

### 热门推荐

文章目录

* [实时且保护隐私的安全浏览](#h2-0)
* [Chrome 的安全浏览通过增强的隐私获得实时保护](#h2-1)

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