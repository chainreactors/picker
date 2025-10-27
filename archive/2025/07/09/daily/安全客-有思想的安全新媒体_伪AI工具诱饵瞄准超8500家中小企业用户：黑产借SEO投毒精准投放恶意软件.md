---
title: 伪AI工具诱饵瞄准超8500家中小企业用户：黑产借SEO投毒精准投放恶意软件
url: https://www.anquanke.com/post/id/309528
source: 安全客-有思想的安全新媒体
date: 2025-07-09
fetch_date: 2025-10-06T23:16:33.838106
---

# 伪AI工具诱饵瞄准超8500家中小企业用户：黑产借SEO投毒精准投放恶意软件

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

# 伪AI工具诱饵瞄准超8500家中小企业用户：黑产借SEO投毒精准投放恶意软件

阅读量**51395**

发布时间 : 2025-07-08 16:22:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/07/seo-poisoning-campaign-targets-8500.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员披露，一起利用**搜索引擎优化（SEO）投毒技术**传播恶意软件的新型攻击活动正在活跃进行，相关恶意软件载荷为已知的**Oyster木马（又名Broomstick或CleanUpLoader）**。

据 Arctic Wolf 披露，这轮恶意广告活动通过伪装成如 **PuTTY、WinSCP** 等合法工具的仿冒网站，诱骗正在寻找这些工具的软件技术人员下载安装恶意版本。

**“一旦执行，后门程序 Oyster/Broomstick 将被植入系统。”** Arctic Wolf 在上周发布的简报中指出，
**“木马通过创建计划任务，每三分钟运行一次恶意 DLL 文件（twain\_96.dll），利用 rundll32.exe 调用 DllRegisterServer 实现持久化驻留。”**

部分已发现的恶意网站包括：

* `updaterputty[.]com`
* `zephyrhype[.]com`
* `putty[.]run`
* `putty[.]bet`
* `puttyy[.]org`

安全人员推测，攻击者可能还在使用类似方式**瞄准其他IT工具**进行恶意软件投放，提醒用户务必**通过可信渠道和官方站点下载软件**。

此次披露正值大量黑帽SEO攻击利用AI相关关键词优化搜索排名，以推广 **Vidar、Lumma、Legion Loader** 等恶意载荷。

这些钓鱼网站内嵌 **JavaScript 代码**，用于检测广告拦截器并收集浏览器信息，随后发起重定向跳转，将受害者导向包含恶意 ZIP 文件的钓鱼页面。

**“最终的下载页面会提供 Vidar Stealer 和 Lumma Stealer 的密码保护 ZIP 文件，”** Zscaler ThreatLabz 表示，
**“ZIP 文件中包含一个800MB的大型NSIS安装包，目的是伪装成合法软件，以绕过对文件大小有限制的检测机制。”**

NSIS 安装包会运行 AutoIt 脚本，用于加载窃密木马。而针对 Legion Loader 的投递机制则改为使用 **MSI 安装包 + 批处理脚本** 组合完成感染。

还有一类类似攻击通过 SEO 操作提升钓鱼页面在搜索引擎中的排名，尤其是当用户搜索**热门网页应用名称**时，将其重定向至伪造的 **Cloudflare CAPTCHA 页面**，通过名为 **ClickFix** 的策略加载 RedLine Stealer 并借助 Hijack Loader 执行。

### **AI伪装恶意软件瞄准中小企业用户**

根据卡巴斯基（Kaspersky）统计数据，越来越多的**中小型企业（SMBs）成为恶意软件投递的目标**，攻击者将恶意载荷伪装成热门AI和协作工具，如：

* **OpenAI ChatGPT**
* **DeepSeek**
* **Cisco AnyConnect**
* **Google Drive**
* **Microsoft Office、Teams、Outlook**
* **Salesforce**
* **Zoom**

**“仅在2025年1月至4月期间，全球已有约8,500名中小企业用户成为这类伪装软件攻击的目标。”** 卡巴斯基指出。

具体而言，Zoom 占总恶意文件样本的 **41%**，Outlook 和 PowerPoint 各占 **16%**，Excel 为 **12%**，Word 为 **9%**，Teams 为 **5%**。
伪装成 ChatGPT 的恶意样本数量在2025年初暴增 **115%**，达到 **177个样本**。

### **钓鱼手法不断演化：搜索结果劫持、广告平台注入、跨平台传播并举**

攻击者不止利用 Google 搜索广告，也在 **Facebook 上发布虚假广告**，诱骗用户提供加密钱包助记词，或通过 Pi2Day 活动传播伪造的 Pi Network 桌面客户端。

这些恶意软件具备：

* **窃取保存的凭据和加密钱包私钥**
* **键盘记录与屏幕监控**
* **后续载荷下载能力**
* **具备躲避检测机制**

比特梵德（Bitdefender）认为该活动可能由 **单一攻击组织操控**，在 Meta 平台上并行运行多个诈骗链条，以最大化覆盖面和经济收益。

不仅如此，伪装成 AI、VPN 服务等知名品牌的钓鱼网站也被发现传播 macOS 平台的 **Poseidon Stealer**，以及 Windows 平台的 **PayDay Loader**，后者会进一步下载 **Lumma Stealer** 木马。

安全研究员 g0njxa 将该系列攻击活动命名为 **Dark Partners**。其中 PayDay Loader 使用 **Google Calendar 链接作为隐蔽的中继点**，获取 C2 地址并加载混淆 JavaScript 代码，最终执行木马并窃取敏感数据。

PayDay Loader 依靠 Google 日历链接作为死点解析器来提取命令和控制 （C2） 服务器并获取混淆的 JavaScript 代码，这些代码旨在加载 Lumma Stealer 有效负载并窃取敏感数据。

有趣的是，用于创建 Google 日历事件的电子邮件地址 （“echeverridelfin@gmail[.]com“） 还被发现与名为”os-info-checker-es6“的恶意 npm 包有关。这表明 Dark Partners 参与者可能已经尝试了不同的交付机制。

“PayDay Loader 有一个Node.js窃取模块，可以将加密货币钱包数据泄露到外部 C2，”g0njxa 表示。“使用Node.js的 ADM-ZIP 库，PayDay Loader 能够查找、打包钱包信息并将其发送到硬编码的 C2 主机。”

这些活动与一种持续的现象齐头并进，即诈骗者和网络犯罪分子建立了由数千个网站组成的庞大网络，以欺骗流行品牌，并通过宣传从未交付的真实产品来实施金融欺诈。其中一个被 Silent Push 称为 GhostVendors 的网络购买了 Facebook 广告空间来推广 4,000 多个粗略的网站。

恶意的 Facebook Marketplace 广告会运行几天，之后它们就会停止，从而有效地从 Meta 广告库中删除它们的所有痕迹。值得指出的是，Meta 在过去七年中只保留了有关社会问题、选举和政治的广告。

“这有助于确认已知的 Meta 广告库策略的存在，并强调这些威胁行为者可能正在利用这一点，在不同页面上快速启动和停止类似产品的广告，”Silent Push 研究人员说表示。

该公司发现的另一个网络以英语和西班牙语购物者为目标，投放虚假市场广告，被评估为中国威胁行为者所为。这些网站主要旨在窃取在支付页面上输入的信用卡信息，同时声称可以处理订单。一些虚假网站还包括 Google Pay 购买小部件以启用付款。

“这个虚假的市场活动主要针对消费者的网络钓鱼威胁，该威胁利用主要品牌、知名组织和一些政治人物的名气，”Silent Push 表示。

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/07/seo-poisoning-campaign-targets-8500.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309528](/post/id/309528)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/07/seo-poisoning-campaign-targets-8500.html)

如若转载,请注明出处： <https://thehackernews.com/2025/07/seo-poisoning-campaign-targets-8500.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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