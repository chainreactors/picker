---
title: 黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内
url: https://www.anquanke.com/post/id/314815
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:46.485073
---

# 黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内

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

# 黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内

阅读量**26587**

发布时间 : 2026-02-25 14:19:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/hackers-pulsar-rat-png-images-npm-supply-chain-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员发现一类全新网络攻击手法，其利用普通图片藏匿高危恶意程序。Veracode 威胁研究团队在**NPM**平台上检出一款恶意软件包 ——NPM 是全球数百万开发者共享工具的大型代码仓库。该恶意包外观与正常软件无异，真实目的却是**完全控制受害者计算机**。

该恶意包命名为**buildrunner-dev**。攻击核心陷阱在于：黑客采用**typosquatting（拼写抢注）** 手段，将包名仿冒成与正规安全工具`buildrunner`高度近似的名称，诱使用户因拼写失误误下载。这意味着，攻击在软件安装的瞬间便已启动。

![]()

### 海量干扰代码，掩盖真实恶意逻辑

恶意软件包植入计算机后，会自动执行脚本并下载名为`packageloader.bat`的文件。

Veracode 研究人员在独家提供给[Hackread.com](https://Hackread.com)的博客文章中指出：该文件体积庞大、结构极度混乱，**代码行数超 1600 行**，但绝大多数内容都是用于迷惑安全扫描器的 “垃圾噪声”。

研究人员表示，文件充斥`raven`、`glacier`、`monsoon`等无意义随机字符串，**真正有效指令仅约 21 行**。进一步分析显示，该恶意程序具备较强的反检测能力：会主动检查系统中是否存在 ESET、Malwarebytes、F-Secure 等主流杀毒软件。

一旦检测到杀软，便会通过多种手段**静默绕过**，不触发任何告警。

它首先将自身复制到隐蔽目录，命名为`protect.bat`实现持久化驻留，随后检查自身是否拥有**管理员权限**。

若权限不足，则利用 Windows 系统工具**fodhelper.exe**绕过安全提示，用户全程不会收到任何权限申请弹窗。

### 恶意代码藏身图片，利用隐写术躲避检测

本次攻击最具特点的环节，是将核心木马**隐匿在图片中**，该技术被称为**隐写术（steganography）**。

恶意程序会从免费图床下载一张 PNG 图片，在普通用户眼中，这只是一张模糊、充满杂色的无效图片；但恶意代码可解析图片中的 RGB 像素值，从中提取并还原出藏匿的指令。

此外，研究人员还发现该恶意程序使用**进程空心化（process hollowing）** 技术：将正常程序的内存空间替换为恶意代码，使其在系统中看似合法进程。

完成一系列隐蔽动作后，它最终释放并安装**Pulsar RAT**远控木马。

Pulsar 是一款**远程访问木马**，可让黑客**完全控制受感染主机**。

攻击者还使用`CheaperMyanmarCaribbean.exe`这类怪异文件名，让木马在系统内存中持续隐蔽。

尽管该攻击仅出现在 NPM 平台的开发者工具中，却揭示一个严峻事实：**一张看似普通的图片，即可成为藏匿重大威胁的载体**。

本文翻译自hackread [原文链接](https://hackread.com/hackers-pulsar-rat-png-images-npm-supply-chain-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314815](/post/id/314815)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-pulsar-rat-png-images-npm-supply-chain-attack/)

如若转载,请注明出处： <https://hackread.com/hackers-pulsar-rat-png-images-npm-supply-chain-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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