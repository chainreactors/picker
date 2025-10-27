---
title: 发现超过70个恶意npm和VS代码包窃取数据和加密货币
url: https://www.anquanke.com/post/id/307800
source: 安全客-有思想的安全新媒体
date: 2025-05-28
fetch_date: 2025-10-06T22:24:30.654763
---

# 发现超过70个恶意npm和VS代码包窃取数据和加密货币

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

# 发现超过70个恶意npm和VS代码包窃取数据和加密货币

阅读量**126844**

发布时间 : 2025-05-27 12:53:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html>

译文仅供参考，具体内容表达以及含义原文为准。

在包注册表中发现了多达60个恶意npm包,具有恶意功能,可以将主机名、IP地址、DNS服务器和用户目录传输到Discord控制的端点。

这些软件包在三个不同的帐户下发布,附带在npm安装期间触发的安装时间脚本,Socket安全研究员Kirill Boychenko在上周发布的一份报告中说。图书馆被集体下载了3000多次。

“该脚本针对Windows,macOS或Linux系统,并包括基本的沙盒规避检查,使每个受感染的工作站或连续集成节点成为有价值的侦察的潜在来源[,”软件供应链安全公司说。](https://socket.dev/blog/60-malicious-npm-packages-leak-network-and-host-data)

下面列出了三个帐户的名称,每个帐户在11天内发布了20个软件包。帐户在npm上不再存在 –

* bbbb335656
* cdsfdfafd1232436437, and
* sdsds656565

根据Socket,恶意代码明确设计用于对安装软件包的每台机器进行指纹识别,同时如果检测到它在与亚马逊,Google和其他相关的虚拟化环境中运行,则也会中止执行。

收集的信息,包括主机详细信息,系统DNS服务器,网络接口卡(NIC)信息以及内部和外部IP地址,然后传输到Discord webhook“通过收集内部和外部IP地址,DNS服务器,用户名和项目路径,它使威胁行为者能够绘制网络并识别未来战役的高价值目标,”Boychenko说。披露之前,另一组8个npm包伪装成广泛使用的JavaScript框架的助手库,包括React,Vue.js,Vite,Node.js和开源Quill编辑器,但安装后会部署破坏性有效载荷。它们已被下载超过6,200次,仍然可以从存储库下载 –

* vite-plugin-vue-extend
* quill-image-downloader
* js-hood
* js-bomb
* vue-plugin-bomb
* vite-plugin-bomb
* vite-plugin-bomb-extend, and
* vite-plugin-react-extend

“伪装成合法的插件和实用程序,同时秘密包含旨在损坏数据,删除关键文件和崩溃系统的破坏性有效载荷,这些软件包仍未被发现,”Socket安全研究员Kush Pandya说。

一些已识别的包一旦开发人员在其项目中调用它们,就会自动执行,从而能够递归删除与Vue.js,React和Vite相关的文件。其他设计用于破坏基本的JavaScript方法或篡改浏览器存储机制,如localStorage,sessionStorage和cookie。

[![恶意 npm 和 VS 代码包](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyFWKUo_jVBPdwxcsEKqqTZQ_CFCe2o7TTQrxl278Z-AhPZB8DwZqrs6qyENZ1jMhSd-WyV_G9S06H16NENmfjC7SE-h6UF_OuuhlP-Pkz76DJNQcYOt2DJ7ZntE6iLFI_zhBlq9laeXBvWcDVyrxIwyZNdmKVnneZpdhGyVJ50_FD0DPMmJDo5L3zdTVR/s728-rw-e365/npm-code.jpg "恶意 npm 和 VS 代码包")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyFWKUo_jVBPdwxcsEKqqTZQ_CFCe2o7TTQrxl278Z-AhPZB8DwZqrs6qyENZ1jMhSd-WyV_G9S06H16NENmfjC7SE-h6UF_OuuhlP-Pkz76DJNQcYOt2DJ7ZntE6iLFI_zhBlq9laeXBvWcDVyrxIwyZNdmKVnneZpdhGyVJ50_FD0DPMmJDo5L3zdTVR/s728-rw-e365/npm-code.jpg)

另一个值得注意的包是js-bomb,它超越了删除Vue.js框架文件,还根据当前执行时间启动系统关闭。

该活动可以追溯到一个名为xuxingfeng的威胁行为者,他还发布了五个合法的,非恶意的软件包,按预期工作。部分流氓软件包于2023年发布。“这种释放有害和有用软件包的双重方法创造了合法性的外墙,使恶意软件包更有可能被信任和安装,”Pandya说。

调查结果还遵循了发现一种新颖的攻击活动,该活动将传统的电子邮件网络钓鱼与JavaScript代码相结合,该代码是伪装成良性开源库的恶意npm包的一部分。

“一旦建立通信,该软件包加载并交付了第二阶段脚本,该脚本使用受害者的电子邮件地址定制了钓鱼链接,导致他们进入一个旨在窃取其凭据的虚假Office 365登录页面,”Fortra研究员Israel Cerda说。

攻击的起点是包含恶意的钓鱼电子邮件。HTM文件,其中包括托管在jsDelivr上的加密JavaScript代码jsDelivr,citiycar8并与现在删除的名为citiycar8的npm包相关联。安装后,嵌入在包中的 JavaScript 有效载荷用于启动 URL 重定向链,最终将用户引导到旨在捕获其凭据的虚假着陆页。

“这种网络钓鱼攻击表现出高度的复杂性,威胁行为者将AES加密,通过CDN交付的npm包等技术以及多个重定向以掩盖其恶意意图,”Cerda说。

[![恶意 npm 和 VS 代码包](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2d5aEyFZ-wjEv7bqYoTLcIYCRnWjjWHgVmDj1LXnzhWnjx7qql4_JkOXTsK1esUFlIr5DR6YdhlL8jqc8Lwlop_Id1he9Z-3yQoeQjfdnHl8MYGIYWv7cw17HwcIFMgVlKZhTdASP2aDubqUqK7BWR68z-p0m-XTQJyyHNHfjIYH8qOF1JRW9Cjg8vkHr/s728-rw-e365/jsdl.png "恶意 npm 和 VS 代码包")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2d5aEyFZ-wjEv7bqYoTLcIYCRnWjjWHgVmDj1LXnzhWnjx7qql4_JkOXTsK1esUFlIr5DR6YdhlL8jqc8Lwlop_Id1he9Z-3yQoeQjfdnHl8MYGIYWv7cw17HwcIFMgVlKZhTdASP2aDubqUqK7BWR68z-p0m-XTQJyyHNHfjIYH8qOF1JRW9Cjg8vkHr/s728-rw-e365/jsdl.png)

“这次袭击不仅说明了攻击者试图逃避检测的创造性方式,而且还强调了在不断变化的网络安全威胁环境中保持警惕的重要性。

滥用开源存储库进行恶意软件分发已成为大规模进行供应链攻击的久经考验的方法。最近几周,微软的Visual Studio Code(VS Code) Marketplace也发现了恶意数据窃取扩展,该扩展旨在通过针对Windows上的Solidity开发人员来窃取加密货币钱包凭据。

Datadog Security Research将该活动归因于其跟踪为MUT-9332的威胁行为者。扩展名如下:

* solaibot
* among-eth, and
* blankebesxstnion

“扩展程序伪装成合法,在真实功能中隐藏有害代码,并使用似乎与Solidity相关的命令和控制域,通常不会被标记为恶意,”Datadog研究人员说。

“所有三个扩展都使用复杂的感染链,涉及混淆恶意软件的多个阶段,包括使用隐藏在互联网存档托管的图像文件中的有效载荷。

具体来说,这些扩展被宣传为为Solidity开发人员提供语法扫描和漏洞检测。虽然它们提供了真正的功能,但扩展也旨在提供恶意有效载荷,从受害者Windows系统窃取加密货币钱包凭据。三个扩展已经被删除。

VS Code扩展的最终目标是滑落基于Chromium的恶意浏览器扩展,该扩展程序能够掠夺以太坊钱包并将其泄漏到命令和控制(C2)端点。

[![恶意 npm 和 VS 代码包](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4J68FJYXvnOPiO4TzUMWJisXj3pMAyOuZmwEBp0ZHi816DRnfd6dGfqfok85zLDkqXkvEBIKSxD0l3lqRxngC6K0cVJ5VUo9ftuenJPPrkSLnGq_1owOzSmx5bfwyOZarWgZwvi9QVeaDIkYCLTKlRj1ajaKVP4WW7yOpe1SxWASY3TFLhcKqmaTFqdvs/s728-rw-e365/target.png "恶意 npm 和 VS 代码包")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4J68FJYXvnOPiO4TzUMWJisXj3pMAyOuZmwEBp0ZHi816DRnfd6dGfqfok85zLDkqXkvEBIKSxD0l3lqRxngC6K0cVJ5VUo9ftuenJPPrkSLnGq_1owOzSmx5bfwyOZarWgZwvi9QVeaDIkYCLTKlRj1ajaKVP4WW7yOpe1SxWASY3TFLhcKqmaTFqdvs/s728-rw-e365/target.png)

它还配备了安装一个单独的可执行文件,禁用Windows Defender扫描,扫描Discord,基于Chromium的浏览器,加密货币钱包和Electron应用程序的应用程序数据目录,并从远程服务器检索和执行额外的有效载荷。

MUT-9332也被评估为最近披露的活动的幕后黑手,该活动涉及使用10个恶意VS Code扩展程序通过传递编码或人工智能(AI)工具来安装XMRig密码矿工。

“这次活动展示了MUT-9332在隐瞒其恶意意图时愿意付出的令人惊讶和创造性的长度,”Datadog说。“这些有效载荷更新表明,此活动可能会继续,并且检测和删除第一批恶意VS Code扩展可能会促使MUT-9332在随后的策略中改变策略。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307800](/post/id/307800)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html)

如若转载,请注明出处： <https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

**X**![安全KER](https://p0.ssl.qh...