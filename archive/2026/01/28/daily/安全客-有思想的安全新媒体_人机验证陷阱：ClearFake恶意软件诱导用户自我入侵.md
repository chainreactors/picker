---
title: 人机验证陷阱：ClearFake恶意软件诱导用户自我入侵
url: https://www.anquanke.com/post/id/314580
source: 安全客-有思想的安全新媒体
date: 2026-01-28
fetch_date: 2026-01-29T04:03:39.429969
---

# 人机验证陷阱：ClearFake恶意软件诱导用户自我入侵

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

# 人机验证陷阱：ClearFake恶意软件诱导用户自我入侵

阅读量**27852**

发布时间 : 2026-01-28 10:09:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-captcha-trap-clearfake-malware-tricks-users-into-hacking-themselves/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款设计缜密的恶意软件攻击活动，正将常规的安全验证步骤变为入侵陷阱。Expel 安全研究团队发布分析报告指出，名为**ClearFake**的恶意软件框架通过伪造人机验证验证挑战，诱导用户亲手攻陷自身设备。该恶意软件结合 \*\*“就地取材” 攻击手法 \*\* 与区块链技术的不可篡改特性，已进化为一款极具规避性的网络威胁。

攻击始于遭遇入侵的恶意网站，访问者会看到伪造的人机验证弹窗，要求完成真人验证。但与常规点击交通信号灯等验证操作不同，用户会收到一系列诡异的操作指令：按下**Win+R**组合键，接着按下**Ctrl+V**，最后按下回车键。

![]()

对于不了解网络安全的普通用户而言，这看似是一套复杂的验证流程，实则是名为**ClickFix**的社会工程学诱骗手段。

报告中解释道：“伪造的人机验证挑战借助社会工程学手段，诱导访问者安装恶意软件。” 当用户按下 Win+R 时，Windows 系统的运行对话框会被打开；按下 Ctrl+V 则会将网站悄悄复制到剪贴板中的恶意 PowerShell 命令粘贴至对话框，按下回车后命令便会执行。

最新版本 ClearFake 的高明与危险之处，核心在于其恶意代码的执行方式。攻击者并未直接运行易触发杀毒软件警报的脚本，而是采用了一种名为**代理执行**的技术手段。

他们利用 Windows 系统目录**C:\Windows\System32**下的一款合法系统文件**SyncAppvPublishingServer.vbs**实施攻击。该文件原本用于同步 App-V 应用环境，却存在命令注入漏洞。

分析报告指出：“近期，该攻击活动采用了更具规避性的手段，例如借助代理执行技术，通过 Windows 系统的可信功能运行 PowerShell 命令。”

通过滥用这款受信任的系统组件，攻击者能以 \*\*“隐藏模式”\*\* 启动 PowerShell，让整个感染过程对用户完全不可见。且由于相关操作均源自 Windows 可信系统文件，多数安全产品无法第一时间将其标记为恶意行为。

ClearFake 最难以根除的特点，当属其传播分发方式。该攻击活动采用**以太隐藏**技术，将恶意载荷直接托管在**币安智能链（BSC）** 上。

报告称：“由于区块链具有不可篡改的特性，这些恶意智能合约根本无法被删除。”

攻击者利用原本用于非同质化代币等 Web3 技术的智能合约，存储经 Base64 编码的恶意 JavaScript 代码。受害者设备中的恶意软件会通过公共应用程序编程接口端点查询智能合约，以此获取恶意载荷。这一方式为攻击者提供了 \*\*“难以被下架的恶意软件托管渠道”\*\*，因为只有加密钱包的所有者才能对合约进行修改。

为进一步规避检测，该攻击活动还转而使用主流内容分发网络**jsDelivr**托管部分恶意代码。报告表示，这一做法 \*\*“大幅限制了依赖标记恶意域名和 IP 地址开展防护的安全产品的作用”\*\*，因为封禁这一主流内容分发网络，会导致无数合法网站的访问受到影响。

此次攻击活动的影响规模十分庞大。研究人员通过分析涉事智能合约的交易记录估算，自 2025 年 8 月以来，已有近**15 万台设备**遭到感染。

正如 Expel 的分析报告所总结的：“该攻击活动设计极为缜密，规避性极强”，它将社会工程学诱骗与高级技术漏洞利用相结合，成功绕过了各类现代网络防护体系。

本文翻译自securityonline [原文链接](https://securityonline.info/the-captcha-trap-clearfake-malware-tricks-users-into-hacking-themselves/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314580](/post/id/314580)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-captcha-trap-clearfake-malware-tricks-users-into-hacking-themselves/)

如若转载,请注明出处： <https://securityonline.info/the-captcha-trap-clearfake-malware-tricks-users-into-hacking-themselves/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [“G\_Wagon”恶意软件藏身仿冒NPM界面库，伺机窃取云服务密钥](/post/id/314577)

  2026-01-28 10:09:08
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