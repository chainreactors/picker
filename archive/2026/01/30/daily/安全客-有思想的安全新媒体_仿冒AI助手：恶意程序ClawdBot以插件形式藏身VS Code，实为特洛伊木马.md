---
title: 仿冒AI助手：恶意程序ClawdBot以插件形式藏身VS Code，实为特洛伊木马
url: https://www.anquanke.com/post/id/314625
source: 安全客-有思想的安全新媒体
date: 2026-01-30
fetch_date: 2026-01-31T04:03:11.019256
---

# 仿冒AI助手：恶意程序ClawdBot以插件形式藏身VS Code，实为特洛伊木马

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

# 仿冒AI助手：恶意程序ClawdBot以插件形式藏身VS Code，实为特洛伊木马

阅读量**16412**

发布时间 : 2026-01-30 11:26:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/fake-ai-assistant-malicious-clawdbot-extension-hides-trojan-in-vs-code/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

AI 代码助手的火爆出圈，也引来全新的网络恶意攻击者。2026 年 1 月 27 日，Aikido Security 的安全研究员查理・埃里克森发现一款伪装成热门工具**ClawdBot**的恶意 Visual Studio Code 插件，这款被命名为**ClawdBot Agent**的插件打着实用 AI 工具的幌子，在开发者的设备上悄悄植入恶意软件。

这一事件凸显出一个日益显著的趋势：攻击者正利用新型 AI 工具的热度，诱骗本具备一定安全意识的开发者。研究报告指出：“近期只要接触过 AI 编程相关领域，大概率随处能看到 ClawdBot 的相关提及，这自然让它成为仿冒攻击的首要目标。”

此次攻击的高危险性，还体现在攻击者为实施欺骗所付出的精心设计上。与那些制作粗糙、要么无法运行要么毫无实际功能的低级诈骗插件不同，这款恶意插件**能正常实现宣称的功能**。

报告中提到：“这款仿冒插件的伪装程度极高，配有专业的图标、打磨精致的操作界面，还能对接七家不同的 AI 服务商…… 甚至完全按照宣传的效果正常工作，而这一点恰恰是它最危险的地方。”

该恶意软件依托 OpenAI、Anthropic、谷歌的正版 API，让插件表面上成为一款功能完备的代码助手，让受害者放下戒心，而它则在后台悄然执行恶意操作。

研究报告明确表示：“我们已证实该插件是一款功能完整的特洛伊木马：表面上是正常可用的 AI 代码助手，实则会在 VS Code 启动的瞬间，向 Windows 设备悄悄植入恶意程序。”

该插件的攻击链为：下载伪装成常用截图工具**Lightshot.exe**的恶意载荷，或是名为**Code.exe**的 Electron 程序包。但对其攻击基础设施的分析显示，这些文件名只是高级下载器的伪装而已。

埃里克森在分析中写道：“发现一个有意思的细节？其硬编码的备用执行程序仍指向 Lightshot.exe 和 Lightshot.dll…… 这说明攻击者的恶意载荷大概率经过了多次迭代升级。”

研究人员追踪发现，这款恶意软件的命令与控制（C2）通信流量指向一个可疑域名：**darkgptprivate[.]com**。该域名由奥米加科技有限公司托管在塞舌尔，且注册时间就在此次攻击发生前几周。

攻击者为此次攻击操作搭建了多重冗余机制：利用 Cloudflare 隐藏其主服务器（**clawdbot.getintwopc[.]site**），还设置了各类备用执行方案。“主 C2 服务器瘫痪，他们有备用节点；Node.js 执行失败，还有 PowerShell 方案兜底…… 可见这群攻击者做足了准备工作。”

所幸这款恶意插件被及时发现。研究报告证实：“我们第一时间向微软进行了举报，微软也迅速下架了该插件。”

插件下架时的安装量仅为 21 次，其影响范围得以控制。但这一事件也为开发者敲响了警钟：在 AI 工具的淘金热潮中，安装插件前务必核实开发者的真实身份。正如报告最后所强调的：**正版 ClawdBot 开发团队从未发布过官方的 VS Code 插件，只是攻击者抢先盗用了这个名称而已。**

本文翻译自securityonline [原文链接](https://securityonline.info/fake-ai-assistant-malicious-clawdbot-extension-hides-trojan-in-vs-code/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314625](/post/id/314625)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/fake-ai-assistant-malicious-clawdbot-extension-hides-trojan-in-vs-code/)

如若转载,请注明出处： <https://securityonline.info/fake-ai-assistant-malicious-clawdbot-extension-hides-trojan-in-vs-code/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **980**

* 粉丝
* **6**

### TA的文章

* ##### [筑牢聊天安全防线：WhatsApp推出 “严格模式” 抵御飞马间谍软件](/post/id/314636)

  2026-01-30 11:28:04
* ##### [CVE-2026-24765：PHPUnit漏洞致CI/CD流水线面临远程代码执行风险](/post/id/314611)

  2026-01-30 11:27:56
* ##### [假意网恋设局，实为安卓间谍软件植入](/post/id/314629)

  2026-01-30 11:27:37
* ##### [重登AI存储王座？三星新一代HBM4即将通过英伟达关键认证，行业格局或将改写](/post/id/314606)

  2026-01-30 11:27:26
* ##### [eScan证实更新服务器遭入侵，黑客借其推送恶意更新](/post/id/314627)

  2026-01-30 11:27:07

### 相关文章

* ##### [筑牢聊天安全防线：WhatsApp推出 “严格模式” 抵御飞马间谍软件](/post/id/314636)

  2026-01-30 11:28:04
* ##### [CVE-2026-24765：PHPUnit漏洞致CI/CD流水线面临远程代码执行风险](/post/id/314611)

  2026-01-30 11:27:56
* ##### [假意网恋设局，实为安卓间谍软件植入](/post/id/314629)

  2026-01-30 11:27:37
* ##### [重登AI存储王座？三星新一代HBM4即将通过英伟达关键认证，行业格局或将改写](/post/id/314606)

  2026-01-30 11:27:26
* ##### [eScan证实更新服务器遭入侵，黑客借其推送恶意更新](/post/id/314627)

  2026-01-30 11:27:07
* ##### [信号基金会总裁警示：人工智能代理正让加密技术丧失实际效用](/post/id/314609)

  2026-01-30 11:26:44
* ##### [社会工程学黑客盯上Okta单点登录系统](/post/id/314615)

  2026-01-30 11:26:00

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