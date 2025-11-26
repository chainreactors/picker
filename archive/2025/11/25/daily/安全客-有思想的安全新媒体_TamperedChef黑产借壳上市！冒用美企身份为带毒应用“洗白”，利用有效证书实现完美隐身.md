---
title: TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身
url: https://www.anquanke.com/post/id/313362
source: 安全客-有思想的安全新媒体
date: 2025-11-25
fetch_date: 2025-11-26T03:15:29.193681
---

# TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身

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

# TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身

阅读量**23797**

发布时间 : 2025-11-25 17:43:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/tamperedchef-malvertising-uses-us-shell-companies-to-sign-trojanized-apps-with-valid-certificates-deploying-stealth-backdoor/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Acronis 威胁研究部门（TRU）发现了一场名为 **TamperedChef** 的全球性大规模恶意广告与 SEO 投毒活动。该活动通过美国空壳公司购买的证书签名，分发 **功能完整但植入恶意代码的应用程序**。安装后，这些伪造应用会部署计划任务和 **高度混淆的 JavaScript 后门**，以在多个行业实现持久化控制、远程访问和长期系统操控。

TRU 的调查始于 2025 年 6 月，但发现该活动在被检测前已活跃许久。

### 传播途径与受害者分布

恶意安装程序通过以下渠道传播：

* 必应和谷歌恶意广告
* 伪造下载站点
* 针对产品手册、PDF 阅读器、浏览器甚至简单游戏的 **SEO 优化页面**

Acronis 遥测数据显示，该活动已全球蔓延：“大多数受害者位于美洲，约 80% 在美国。”

受影响最严重的行业包括：

* 医疗保健
* 建筑
* 制造业

正如报告所指出：“这些行业的用户可能经常在线搜索产品手册——这正是 TamperedChef 活动利用的行为之一。”

### 伪造应用与签名机制

Acronis 识别出多个 **功能完整且看似合法的伪造应用**，均使用有效代码签名证书签名。已发现的示例包括：

* All Manuals Reader
* Manual Reader Pro
* Any Product Manual
* JustAskJacky
* Master Chess

这些应用模仿真实软件行为：

* 显示安装向导
* 展示许可协议
* 弹出“感谢安装”页面
* 提供实际功能

Acronis 表示：“每个伪造应用都伪装成功能齐全的程序，并带有有效签名……增加可信度并帮助逃避检测。”

### 工业化运营与基础设施

TamperedChef 以 **高度组织化、企业级流水线** 运作。研究发现威胁行为者：“依赖美国注册空壳公司网络获取和轮换代码签名证书，运营工业化基础设施。”

这些空壳公司包括：

* App Interplace LLC
* Pixel Catalyst Media LLC
* Performance Peak Media LLC
* Unified Market Group LLC

均通过 Northwest Registered Agent Service, Inc. 等代理服务注册。

大多数证书已被吊销，仅最新证书仍活跃：“Unified Market Group LLC——有效（截至撰写时）。”这种快速轮换机制确保旧证书被标记后，恶意软件能持续重新签名。

### 持久化与后门功能

伪造安装程序启动后，会投放恶意 task.xml 文件并创建计划任务，该任务：

* 立即执行
* 每 24 小时重复一次
* 增加最多 30 分钟的随机延迟
* 错过触发时仍会运行
* 阻止同时执行

报告解释：“此变体仅使用计划任务实现持久化……配置为每 24 小时运行一次 JavaScript，并带有随机延迟。”这确保高度混淆的 JavaScript payload 能 **隐蔽且可靠地执行**。

### 后门技术细节

TRU 发现两种 JavaScript 后门变体，均使用 obfuscator.io 进行混淆，应用：

* 控制流平坦化
* 死代码注入
* 函数重命名
* 字符串混淆

部分反混淆后，核心功能包括：

* 注册表操作
* 机器指纹生成
* 与 C2 服务器的加密通信
* 远程代码执行

通信采用加密方式，所有样本均支持远程执行。

### C2 服务器演变

早期 C2 域名类似算法生成字符串：

* api.78kwijczjz0mcig0f0[.]com
* api.zxg4jy1ssoynji24po[.]com

后期域名刻意伪装得更合法：

* get.latest-manuals[.]com
* app.catalogreference[.]com

Acronis 指出这种演变：“早期 C2 服务器使用看似随机的字符串……到 2025 年中后期，C2 服务器改为人类可读名称。”

通过新发现的 C2 服务器进一步调查，发现更多与新空壳公司关联的签名恶意软件，显示其运营规模正快速扩张。

本文翻译自securityonline [原文链接](https://securityonline.info/tamperedchef-malvertising-uses-us-shell-companies-to-sign-trojanized-apps-with-valid-certificates-deploying-stealth-backdoor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313362](/post/id/313362)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/tamperedchef-malvertising-uses-us-shell-companies-to-sign-trojanized-apps-with-valid-certificates-deploying-stealth-backdoor/)

如若转载,请注明出处： <https://securityonline.info/tamperedchef-malvertising-uses-us-shell-companies-to-sign-trojanized-apps-with-valid-certificates-deploying-stealth-backdoor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **728**

* 粉丝
* **6**

### TA的文章

* ##### [微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役](/post/id/313348)

  2025-11-25 17:46:05
* ##### [美国CISA发布警告：Oracle身份管理器中的远程代码执行漏洞正遭攻击者积极利用](/post/id/313352)

  2025-11-25 17:45:43
* ##### [美国司法部诉谷歌广告技术反垄断案进入最终阶段，预计将迎来快速裁决](/post/id/313356)

  2025-11-25 17:44:55
* ##### [NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁](/post/id/313359)

  2025-11-25 17:44:33
* ##### [TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身](/post/id/313362)

  2025-11-25 17:43:43

### 相关文章

* ##### [微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役](/post/id/313348)

  2025-11-25 17:46:05
* ##### [美国CISA发布警告：Oracle身份管理器中的远程代码执行漏洞正遭攻击者积极利用](/post/id/313352)

  2025-11-25 17:45:43
* ##### [美国司法部诉谷歌广告技术反垄断案进入最终阶段，预计将迎来快速裁决](/post/id/313356)

  2025-11-25 17:44:55
* ##### [NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁](/post/id/313359)

  2025-11-25 17:44:33
* ##### [vLLM框架存在漏洞（CVE-2025-62164），通过恶意提示嵌入可导致远程代码执行](/post/id/313366)

  2025-11-25 17:43:02
* ##### [复杂WhatsApp蠕虫攻击通过伪造“阅后即焚”诱饵实施会话劫持，并投放Astaroth银行木马](/post/id/313369)

  2025-11-25 17:42:46
* ##### [PyPI拼写劫持投递多层Python木马，利用异或加密绕过扫描器](/post/id/313372)

  2025-11-25 17:41:58

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