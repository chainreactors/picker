---
title: 标价6000美元的新型恶意软件工具包Stanley：借Chrome应用商店实现页面仿冒攻击
url: https://www.anquanke.com/post/id/314560
source: 安全客-有思想的安全新媒体
date: 2026-01-28
fetch_date: 2026-01-29T04:03:56.142444
---

# 标价6000美元的新型恶意软件工具包Stanley：借Chrome应用商店实现页面仿冒攻击

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

# 标价6000美元的新型恶意软件工具包Stanley：借Chrome应用商店实现页面仿冒攻击

阅读量**17379**

发布时间 : 2026-01-28 10:07:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Amar Ćemanović，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/new-6000-malware-toolkit-stanley-delivers-page-spoofing-via-chrome-web-store/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款名为**Stanley**、标价 6000 美元的恶意软件工具包现身俄罗斯网络犯罪论坛，该工具包搭载一款恶意 Chrome 扩展程序，可仿冒整个网站页面，且能让浏览器地址栏保持显示真实域名，开发者还承诺该扩展可通过 Chrome 应用商店的审核。

2026 年 1 月中旬，瓦罗尼斯实验室的研究人员发现了这款工具包，Stanley 的出现，也印证了浏览器恶意软件商业化的趋势正不断加剧。1 月 12 日，一名化名为**Стэнли**的卖家首次发布该工具包的广告，还附带演示视频，展示其针对币安、美国加密货币交易所等加密货币平台的攻击效果。1 月 21 日，瓦罗尼斯已将该恶意攻击活动上报谷歌及该扩展的托管服务商；次日，相关**命令与控制（C2）基础设施**被下线，但这款恶意扩展程序仍在 Chrome 应用商店中正常可用。

![]()

据瓦罗尼斯实验室披露，2026 年 1 月 12 日 Stanley 在地下网络论坛首次出现，由化名为**Стэнли**的卖家发布广告。该工具包并非定制开发版本，而是以标准化打包服务的形式售卖，卖家还附带演示视频，展示其对币安、美国加密货币交易所等知名加密货币平台发起的实时攻击过程。该工具包的高级版本支持定制开发，可访问基于网页端的**命令与控制（C2）面板**，且卖家承诺能将配套的恶意扩展成功上架谷歌应用商店。

这款工具包的核心设计，是将恶意程序伪装成正规的 Chrome 扩展程序。瓦罗尼斯实验室对一款名为**Notely**的样本扩展进行了分析，该扩展对外宣称是轻量级的笔记记录与书签管理工具。尽管它确实能实现宣传中的基础功能，但这些正常功能仅为伪装，目的是获取浏览器的多项高权限，包括**访问所有网址、执行脚本、获取网页导航数据、读取存储文件、发送通知**等。其恶意代码会在**document\_start**阶段执行，能在网页的合法内容加载前就获得页面的控制权。

该扩展程序一旦安装，会每 10 秒向其命令与控制基础设施发送一次心跳请求，且并非通过随机生成的标识，而是将**受害者的 IP 地址**作为唯一识别符。这一设计让攻击者能跨会话追踪用户、开展地域定向攻击，还可选择性触发攻击行为。卖家演示视频中的管理面板显示，攻击者可针对单个受害者配置**URL 劫持规则**，指定需要拦截的正规网站，以及替换展示的钓鱼页面。

![]()

该工具包的核心攻击手段，是在正规网站页面上叠加一个由攻击者控制的**全屏 iframe 框架**，加载钓鱼内容。关键在于，受害者浏览器的地址栏会始终显示正确的域名（如币安官网[binance.com](https://binance.com)），但用户的所有操作实际都在钓鱼页面上完成。Stanley 还支持调用**Chrome 原生推送通知**功能，攻击者可通过该渠道发送诱导信息，相比普通网页弹窗，这类通知更具迷惑性。同时，该工具包还配备**备用域名轮换机制**，即便主命令与控制服务器被下线，恶意程序仍能正常运行。

![]()

2026 年 1 月 21 日，瓦罗尼斯实验室已将该恶意基础设施情况上报 Chrome 应用商店及相关托管服务商。尽管主命令与控制服务器在次日被下线，但截至本文撰写时，这款恶意扩展程序仍未被下架，可正常获取。

安全机构建议，用户应定期检查已安装的浏览器扩展程序，卸载闲置的扩展，同时提高警惕，**切勿授权请求 “访问所有网站” 等大范围权限的扩展程序**。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/new-6000-malware-toolkit-stanley-delivers-page-spoofing-via-chrome-web-store/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314560](/post/id/314560)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/new-6000-malware-toolkit-stanley-delivers-page-spoofing-via-chrome-web-store/)

如若转载,请注明出处： <https://cyberinsider.com/new-6000-malware-toolkit-stanley-delivers-page-spoofing-via-chrome-web-store/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **970**

* 粉丝
* **6**

### TA的文章

* ##### [反制黑客：研究人员对“哈萨克远控木马”间谍攻击活动实施黑洞诱捕](/post/id/314594)

  2026-01-28 10:10:00
* ##### [人机验证陷阱：ClearFake恶意软件诱导用户自我入侵](/post/id/314580)

  2026-01-28 10:09:09
* ##### [“G\_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥](/post/id/314577)

  2026-01-28 10:09:08
* ##### [CVE-2026-0994：谷歌Protocol Buffers曝出高严重性拒绝服务漏洞](/post/id/314571)

  2026-01-28 10:08:23
* ##### [法国将弃用Zoom和Teams，改用本土自主研发平台Visio](/post/id/314576)

  2026-01-28 10:08:22

### 相关文章

* ##### [反制黑客：研究人员对“哈萨克远控木马”间谍攻击活动实施黑洞诱捕](/post/id/314594)

  2026-01-28 10:10:00
* ##### [人机验证陷阱：ClearFake恶意软件诱导用户自我入侵](/post/id/314580)

  2026-01-28 10:09:09
* ##### [“G\_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥](/post/id/314577)

  2026-01-28 10:09:08
* ##### [CVE-2026-0994：谷歌Protocol Buffers曝出高严重性拒绝服务漏洞](/post/id/314571)

  2026-01-28 10:08:23
* ##### [法国将弃用Zoom和Teams，改用本土自主研发平台Visio](/post/id/314576)

  2026-01-28 10:08:22
* ##### [布鲁塞尔对马斯克旗下人工智能企业展开深度伪造调查，科技对峙局势升级](/post/id/314572)

  2026-01-28 10:07:52
* ##### [遭攻击：微软紧急修复Office零日漏洞（CVE-2026-21509），漏洞已在野被利用](/post/id/314561)

  2026-01-28 10:07:36

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