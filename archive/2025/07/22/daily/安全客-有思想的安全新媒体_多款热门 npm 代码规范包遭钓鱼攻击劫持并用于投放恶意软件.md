---
title: 多款热门 npm 代码规范包遭钓鱼攻击劫持并用于投放恶意软件
url: https://www.anquanke.com/post/id/310334
source: 安全客-有思想的安全新媒体
date: 2025-07-22
fetch_date: 2025-10-06T23:16:42.093556
---

# 多款热门 npm 代码规范包遭钓鱼攻击劫持并用于投放恶意软件

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

# 多款热门 npm 代码规范包遭钓鱼攻击劫持并用于投放恶意软件

阅读量**80260**

发布时间 : 2025-07-21 17:37:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ax Sharma，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/popular-npm-linter-packages-hijacked-via-phishing-to-drop-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

本周，多款流行的 JavaScript 库遭劫持并被用于投放恶意软件，这是一场通过精准钓鱼攻击和凭证窃取实施的软件供应链攻击事件。

其中最受欢迎的 npm 包 `eslint-config-prettier` 每周下载量超过 3000 万次，在其维护者遭遇钓鱼攻击后被攻破。攻击者还针对该维护者名下的其他包发起攻击，包括 `eslint-plugin-prettier`、`synckit`、`@pkgr/core` 和 `napi-postinstall`。

威胁者利用窃取的访问凭证，向 npm 发布了多个包含恶意代码的未授权版本，目标是在 Windows 系统中植入恶意程序。

### 维护者遭钓鱼攻击，多个库被篡改

7 月 18 日，开发者在安装 `eslint-config-prettier` 的 8.10.1、9.1.1、10.1.6 和 10.1.7 版本后发现异常行为。这些版本虽然已经发布至 npm 官方仓库，但在对应的 GitHub 仓库中并未发现任何与之匹配的代码更改记录，引发了开源社区的高度警惕。

像 `eslint-config-prettier` 和 `eslint-plugin-prettier` 这样的库可帮助开发者更便捷地在项目中结合使用 Prettier 与 ESLint，使代码格式化规则一致，避免冲突或重复的 lint 校验。这一事件突显出开源生态系统在依赖链维护方面面临的重大安全挑战。

开发者 Dasa Paddock 最早在该项目的 GitHub 仓库中提出了相关问题，引发了社区成员的广泛关注和迅速响应。

不久之后，该包的维护者 JounQin 证实自己确实遭遇了钓鱼攻击。攻击者由此获取了他的 npm 令牌，从而得以发布被植入恶意代码的版本。

“就是这封钓鱼邮件，”JounQin 写道，并分享了一张他收到的钓鱼邮件截图，内容是一封看似来自官方的“验证您的账户”邮件，伪装程度极高。

该邮件通过伪造手段，伪装成来自“support@npmjs.com”的官方地址，但其中的链接却指向一个非法域名“npnjs[.]com”。

JounQin 表示：“我已删除该 npm 令牌，并将尽快发布新版本。”

这位维护者在同一讨论中继续写道：“感谢大家的提醒，对我的疏忽深感抱歉。”

![]()

### 恶意 postinstall 脚本执行 Windows DLL

在这些恶意版本中，npm 包含一个名为 “install.js” 的 postinstall 脚本，该脚本会在包安装后立即运行。

这个 “install.js” 脚本中包含一个名为 logDiskSpace() 的可疑函数，尽管名字与磁盘空间监控相关，实际上它并不执行监控功能。相反，该函数试图通过 Windows 系统进程 rundll32 执行包内捆绑的 DLL 文件 “node-gyp.dll”。

截至目前，该 DLL 已被确认是一个木马病毒，在 VirusTotal 的检测评分为 19/72，说明大多数杀毒软件尚未能检测到该恶意程序。

### 你应该怎么做？

* **避免安装以下受影响版本的包：**

  + eslint-config-prettier 版本：8.10.1、9.1.1、10.1.6 和 10.1.7
  + eslint-plugin-prettier 版本：4.2.2 和 4.2.3
  + synckit 版本：0.11.9
  + @pkgr/core 版本：0.2.8
  + napi-postinstall 版本：0.3.1
* **检查锁文件**，如 package-lock.json、pnpm-lock.yaml、bun.lock 或 yarn.lock，确认是否引用了上述版本。
* 如果你在7月18日之后部署了构建版本，请检查持续集成（CI）日志和运行环境，特别是 Windows 机器，是否有被入侵的迹象。
* 考虑更换在受影响构建过程中可能暴露的任何密钥或凭证。
* 维护者已在 npmjs 注册表中将受影响版本标记为“弃用”。
* 另外，一位 GitHub 用户提醒，应检查该维护者发布的其他包是否存在被篡改的迹象。

![]()

此次事件是近期一系列针对热门库开发者的社会工程攻击的延续。

今年三月，十多个广泛使用的 npm 库遭到入侵，被植入信息窃取程序。上个月，又有17个 Gluestack 包被劫持，这些包每周下载量超过一百万，被用来部署远程访问木马（RAT）。

开源生态系统在很大程度上依赖信任，因此此类事件凸显了供应链安全的脆弱性以及维护者安全防护的重要性。一次错误的点击，就足以让数百万用户面临风险。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/popular-npm-linter-packages-hijacked-via-phishing-to-drop-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310334](/post/id/310334)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/popular-npm-linter-packages-hijacked-via-phishing-to-drop-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/popular-npm-linter-packages-hijacked-via-phishing-to-drop-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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