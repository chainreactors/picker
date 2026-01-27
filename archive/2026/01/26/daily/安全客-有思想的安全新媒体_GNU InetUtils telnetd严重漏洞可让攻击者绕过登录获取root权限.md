---
title: GNU InetUtils telnetd严重漏洞可让攻击者绕过登录获取root权限
url: https://www.anquanke.com/post/id/314536
source: 安全客-有思想的安全新媒体
date: 2026-01-26
fetch_date: 2026-01-27T03:37:09.427206
---

# GNU InetUtils telnetd严重漏洞可让攻击者绕过登录获取root权限

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

# GNU InetUtils telnetd严重漏洞可让攻击者绕过登录获取root权限

阅读量**18605**

发布时间 : 2026-01-26 14:05:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

GNU InetUtils 的 telnet 守护进程（telnetd）中被披露存在一个严重安全漏洞，该漏洞已隐藏近 11 年未被发现。

此漏洞的 CVE 编号为 **CVE-2026-24061**，在 CVSS 评分系统中得分为 **9.8/10.0（严重级别）**，影响 GNU InetUtils 从 1.9.3 版本到 2.7 版本（含 2.7 版本）的所有版本。

美国国家标准与技术研究院（NIST）国家漏洞数据库（NVD）对该漏洞的描述为：“GNU Inetutils 2.7 及以下版本中的 telnetd 存在远程身份验证绕过漏洞，攻击者可通过将 USER 环境变量设置为 ‘-f root’ 实现绕过。”

GNU 贡献者 Simon Josefsson 在 oss-security 邮件列表中发文指出，攻击者可利用该漏洞获取目标系统的 **root 权限**，具体利用方式如下：

* telnetd 服务器会调用 `/usr/bin/login`（通常以 root 权限运行），并将从客户端接收的 USER 环境变量值作为最后一个参数传入。
* 若客户端构造特殊的 USER 环境变量值（即字符串 **“-f root”**），并通过 telnet (1) 的 `-a` 或 `--login` 参数将该 USER 环境变量发送至服务器，即可绕过正常身份验证流程，直接以 root 用户身份自动登录系统。

漏洞成因在于：**telnetd 服务器在将 USER 环境变量传递给 login (1) 之前未进行任何净化处理**，而 login (1) 工具本身支持通过 `-f` 参数绕过正常身份验证流程。

Josefsson 还提到，该漏洞源于 2015 年 3 月 19 日的一次源代码提交，并随 2015 年 5 月 12 日发布的 1.9.3 版本正式引入。安全研究员 Kyu Neushwaistein（又名 Carlos Cortes Alvarez）于 2026 年 1 月 19 日发现并报告了该漏洞。

### 漏洞缓解措施

Josefsson 建议采取以下缓解措施：

1. **安装最新补丁**：及时应用官方发布的修复补丁（优先推荐）；
2. **限制端口访问**：仅允许可信客户端访问 telnet 端口（默认 23 端口）；
3. **临时规避方案**：
   * 直接禁用 telnetd 服务器；
   * 让 InetUtils telnetd 使用自定义的 login (1) 工具，且该工具需禁止使用 `-f` 参数。

### 攻击态势监测

威胁情报公司 GreyNoise 收集的数据显示，**过去 24 小时内已监测到 21 个独立 IP 地址** 尝试利用该漏洞发起远程身份验证绕过攻击。这些 IP 地址分别来自中国香港、美国、日本、荷兰、中国内地、德国、新加坡和泰国，且均已被标记为恶意 IP。

觉得这篇文章有价值？关注我们的 Google 新闻、Twitter 和 LinkedIn 账号，获取更多独家内容。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314536](/post/id/314536)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html)

如若转载,请注明出处： <https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **960**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30

### 相关文章

* ##### [CVE-2026-23594：HPE Alletra和Nimble中存在高严重性漏洞可被利用获取管理员权限](/post/id/314515)

  2026-01-26 14:16:01
* ##### [OpenAI发力TOB市场，瞄准企业客户与高价值商业场景](/post/id/314513)

  2026-01-26 14:15:35
* ##### [“SymPy”仿冒品：域名抢注式攻击将数学库沦为加密货币挖矿工具](/post/id/314518)

  2026-01-26 14:14:43
* ##### [破坏与野外利用：LA-Studio Element Kit中发现严重后门](/post/id/314510)

  2026-01-26 14:13:55
* ##### [黑客利用“rn”拼写欺诈手段，在新型钓鱼攻击中仿冒微软与万豪](/post/id/314543)

  2026-01-26 14:12:30
* ##### [Mac 用户警惕：“MacSync”恶意软件诱导你“亲手”入侵自己的设备](/post/id/314522)

  2026-01-26 14:12:18
* ##### [CVE-2026-22822：External Secrets Operator严重漏洞破坏命名空间隔离机制](/post/id/314529)

  2026-01-26 14:11:37

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