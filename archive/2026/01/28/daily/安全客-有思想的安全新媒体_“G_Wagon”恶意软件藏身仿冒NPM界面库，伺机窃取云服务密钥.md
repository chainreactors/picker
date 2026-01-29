---
title: “G_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥
url: https://www.anquanke.com/post/id/314577
source: 安全客-有思想的安全新媒体
date: 2026-01-28
fetch_date: 2026-01-29T04:03:41.886266
---

# “G_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥

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

# “G\_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥

阅读量**28243**

发布时间 : 2026-01-28 10:09:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/g_wagon-malware-hides-in-fake-npm-ui-library-to-steal-cloud-keys/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

这看起来只是又一个普通的 UI 库。名为 **ansi-universal-ui** 的包声称是 “适用于现代 Web 应用的轻量型模块化 UI 组件系统”，但在专业的描述和版本历史背后，隐藏着一个复杂的信息窃取恶意软件 —— 安全研究机构 Aikido 将其命名为 **“G\_Wagon”**。

该恶意包于 **2026 年 1 月 23 日** 被发现，它并非简单脚本，而是一个多阶段攻击平台，目标直指开发者环境中最有价值的机密信息。

攻击始于这个具有欺骗性的 npm 包。在普通开发者眼中，ansi-universal-ui 看似合法无害，但一旦安装，它就会执行一段 “高度混淆的载荷”，并下载专属的 Python 运行时，以此绕过本地环境限制。

这款恶意软件的数据窃取胃口极大。报告显示，它会**窃取浏览器凭据、加密货币钱包、云服务密钥（AWS/Azure/GCP 等）以及 Discord 令牌**，并将这些数据上传至一个 Appwrite 存储桶。

报告梳理了其攻击演进时间线：仅两天内，攻击者就发布了 10 个版本，可见其通过 “试错迭代” 完善攻击功能的过程：

* **第一天**：攻击者测试基础功能。1.0.0 版本为 “使用 npm 的 tar 模块搭建的初始框架”，随后迅速发布多个版本修复依赖项和重定向问题。
* **第二天**：攻击者全面激活恶意功能。1.3.5 版本新增了**命令与控制（C2）服务器 URL**；到 1.3.8 版本时，该恶意软件已集成 “完整的 Python 载荷及浏览器注入功能”。

研究人员指出：“这个恶意软件的特别之处在于，我们能完整看到它的开发过程。攻击者两天内发布 10 个版本，每个版本都揭示了攻击构建的一部分。”

“G\_Wagon” 的技术复杂度远超普通脚本小子编写的恶意软件。其 Python 代码中嵌入了一个 “大型 Base64 编码数据块”，解码后发现是经过 XOR 加密的 Windows 动态链接库（DLL）。

这款恶意软件并非简单运行，而是深度植入系统：它利用 **NtAllocateVirtualMemory** 和 **NtCreateThreadEx** 等高级原生 API，将该 DLL 注入浏览器进程。“恶意软件内置了完整的 PE 文件解析器，会遍历导出表查找名为‘Initialize’的函数 —— 这是注入后执行的入口点。”

攻击者显然瞄准了高价值目标。针对大型文件，恶意软件会 “将数据分割为 5MB 的分片”，确保即使是海量窃取的数据也能可靠上传。“开发者显然为拥有大量敏感数据的受害者做好了准备。”

对于可能已安装 ansi-universal-ui 包的开发者，研究人员敦促立即采取彻底的应急措施：

1. 删除 node\_modules 目录并卸载该恶意包；
2. 检查用户主目录中是否存在 **.gwagon\_status 文件**—— 这是感染的直接证据；
3. 轮换所有凭据，重点包括浏览器保存的密码、云服务密钥（AWS/Azure/GCP）及 SSH 密钥。

本文翻译自securityonline [原文链接](https://securityonline.info/g_wagon-malware-hides-in-fake-npm-ui-library-to-steal-cloud-keys/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314577](/post/id/314577)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/g_wagon-malware-hides-in-fake-npm-ui-library-to-steal-cloud-keys/)

如若转载,请注明出处： <https://securityonline.info/g_wagon-malware-hides-in-fake-npm-ui-library-to-steal-cloud-keys/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

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
* ##### [CVE-2026-0994：谷歌Protocol Buffers曝出高严重性拒绝服务漏洞](/post/id/314571)

  2026-01-28 10:08:23
* ##### [法国将弃用Zoom和Teams，改用本土自主研发平台Visio](/post/id/314576)

  2026-01-28 10:08:22
* ##### [布鲁塞尔对马斯克旗下人工智能企业展开深度伪造调查，科技对峙局势升级](/post/id/314572)

  2026-01-28 10:07:52
* ##### [遭攻击：微软紧急修复Office零日漏洞（CVE-2026-21509），漏洞已在野被利用](/post/id/314561)

  2026-01-28 10:07:36
* ##### [标价6000美元的新型恶意软件工具包Stanley：借Chrome应用商店实现页面仿冒攻击](/post/id/314560)

  2026-01-28 10:07:17

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