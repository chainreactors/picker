---
title: 新型 WordPress 钓鱼骗局现身 借 Telegram 盗取信用卡信息
url: https://www.anquanke.com/post/id/314129
source: 安全客-有思想的安全新媒体
date: 2026-01-06
fetch_date: 2026-01-07T03:26:31.563973
---

# 新型 WordPress 钓鱼骗局现身 借 Telegram 盗取信用卡信息

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

# 新型 WordPress 钓鱼骗局现身 借 Telegram 盗取信用卡信息

阅读量**15473**

发布时间 : 2026-01-06 14:31:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源： securityonline

原文地址：<https://securityonline.info/new-wordpress-phishing-scam-steals-credit-cards-via-telegram/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款手法隐蔽的新型钓鱼攻击正针对 WordPress 站点所有者发起攻击，攻击者以伪造的 “域名续费通知” 为诱饵，**诱骗受害者提交信用卡信息及 3D 安全验证一次性密码（OTP）**。威胁研究员阿努拉格揭露了这一攻击活动，该活动摒弃了传统的命令控制服务器模式，**直接通过 Telegram 将窃取的数据传输给攻击者**。

诈骗流程由一封主题为 “续费即将到期 —— 需立即处理” 的邮件开启。尽管邮件刻意营造出紧迫感，但阿努拉格的分析指出了其中的关键破绽：**“这封邮件的致命疑点在于未提及任何具体域名信息，这在正规的续费通知中极为反常”**。

点击邮件中 “立即续费” 按钮的受害者，会被重定向至搭建在 `soyfix[.]com` 域名下的虚假支付页面。该页面几乎完美复刻了 WordPress 官方支付流程的界面。

阿努拉格指出：“这个钓鱼页面在视觉设计上刻意模仿正规 WordPress 支付流程，以此骗取受害者的信任。” 页面不仅设有 “安全订单验证” 的醒目横幅、各大信用卡品牌的标识，还展示了逼真的价格明细（例如：订单小计 13 美元，增值税 2.73 美元）。

但实际上，整个 “订单” 都是伪造的幌子。页面的后台逻辑会收集受害者填写的持卡人姓名、卡号、有效期及安全码（CVV），并**实时将这些信息传输给攻击者**。

更阴险的是，攻击者的目标不只是窃取信用卡信息，还试图绕过 3D 安全验证机制。当受害者提交信用卡信息后，页面会弹出伪造的 “3D 安全验证” 窗口，**诱导受害者输入手机收到的短信验证码**。

随后，页面脚本会启动一系列 “心理信任诱导操作”—— 比如设置 7 秒的加载界面、4 秒的 “验证处理中” 延迟，**让整个窃取流程看起来与真实的银行交易无异**。

尤为关键的是，该页面被预先设定为验证失败的结果。“页面始终会显示‘验证失败’，迫使受害者反复输入一次性密码，从而让攻击者能够获取多组有效的验证码”。

该钓鱼攻击的基础设施有一个显著特点 ——**依托正规的即时通讯应用运作**。后台脚本文件（`send_payment.php` 和 `send_sms.php`）并未将窃取的信息发送至可疑服务器，而是直接转发给一个 Telegram 机器人。

“尽管脚本文件名十分普通，但控制台输出信息及代码注释明确显示，数据会被转发至 Telegram。这表明攻击者正将 Telegram 机器人或频道，用作命令控制（C2）的数据窃取传输通道”。

这种攻击方式正日益流行，原因在于其 “所需的基础设施成本极低”，且 “与传统的受控命令控制面板相比，更难被阻断或摧毁”。

最初的钓鱼邮件均从 `admin@theyounginevitables.com` 邮箱发出，该域名伪造了 WordPress 官方支持的名义。对邮件头的分析结果显示，**该域名的 DMARC 策略配置极为宽松（p=NONE）**，使得攻击者可以不受限制地伪造发件人身份。

安全人员建议 WordPress 用户：**对任何未注明具体域名的续费通知保持高度警惕**，务必通过 [WordPress.com](https://WordPress.com) 官方后台直接核实账户状态。

本文翻译自 securityonline [原文链接](https://securityonline.info/new-wordpress-phishing-scam-steals-credit-cards-via-telegram/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314129](/post/id/314129)

安全KER - 有思想的安全新媒体

本文转载自:  [securityonline](https://securityonline.info/new-wordpress-phishing-scam-steals-credit-cards-via-telegram/)

如若转载,请注明出处： <https://securityonline.info/new-wordpress-phishing-scam-steals-credit-cards-via-telegram/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **880**

* 粉丝
* **6**

### TA的文章

* ##### [伊顿 UPS 管理软件曝漏洞 致系统面临高危代码执行风险](/post/id/314132)

  2026-01-06 14:44:21
* ##### [工作流集成赋能谷歌 Gemini AI，市场份额攀升至 18.2%](/post/id/314154)

  2026-01-06 14:43:18
* ##### [Trust Wallet浏览器扩展遭入侵，700 万美元资产被盗](/post/id/314161)

  2026-01-06 14:39:28
* ##### [黑客宣称窃取欧洲空间局 200GB 数据](/post/id/314157)

  2026-01-06 14:38:44
* ##### [信息窃取恶意软件助攻击者劫持合法商业基础设施，用于托管恶意程序](/post/id/314146)

  2026-01-06 14:37:52

### 相关文章

* ##### [伊顿 UPS 管理软件曝漏洞 致系统面临高危代码执行风险](/post/id/314132)

  2026-01-06 14:44:21
* ##### [工作流集成赋能谷歌 Gemini AI，市场份额攀升至 18.2%](/post/id/314154)

  2026-01-06 14:43:18
* ##### [Trust Wallet浏览器扩展遭入侵，700 万美元资产被盗](/post/id/314161)

  2026-01-06 14:39:28
* ##### [黑客宣称窃取欧洲空间局 200GB 数据](/post/id/314157)

  2026-01-06 14:38:44
* ##### [信息窃取恶意软件助攻击者劫持合法商业基础设施，用于托管恶意程序](/post/id/314146)

  2026-01-06 14:37:52
* ##### [人工智能与云计算热潮推动下，2026 年软件工程岗位需求激增至 10.5 万个](/post/id/314143)

  2026-01-06 14:36:37
* ##### [金狼（Kimwolf）僵尸网络感染 180 万台安卓设备，发起DDoS攻击](/post/id/314138)

  2026-01-06 14:35:37

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