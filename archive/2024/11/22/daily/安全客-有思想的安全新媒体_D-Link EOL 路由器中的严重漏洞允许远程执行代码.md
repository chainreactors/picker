---
title: D-Link EOL 路由器中的严重漏洞允许远程执行代码
url: https://www.anquanke.com/post/id/302053
source: 安全客-有思想的安全新媒体
date: 2024-11-22
fetch_date: 2025-10-06T19:13:19.736926
---

# D-Link EOL 路由器中的严重漏洞允许远程执行代码

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

# D-Link EOL 路由器中的严重漏洞允许远程执行代码

阅读量**61457**

发布时间 : 2024-11-21 10:55:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-vulnerability-in-d-link-eol-routers-allows-remote-code-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

![D-Link Vulnerability]()

D-Link 发布了一则安全公告，涉及多款报废 (EOL) 和服务终止 (EOS) 路由器型号，包括 DSR-150、DSR-150N、DSR-250 和 DSR-250N。该公告强调了一个堆栈缓冲区溢出漏洞，该漏洞可能允许未经认证的用户执行远程代码。此关键问题影响运行固件版本 3.13 至 3.17B901C 的这些传统路由器的所有硬件版本。

自 2024 年 5 月 1 日起，D-Link 不再支持或修补这些型号。根据公告，“达到 EOL/EOS 的产品不再接收设备软件更新和安全补丁，D-Link 美国公司也不再提供支持”。

报告的漏洞是堆栈缓冲区溢出，这是一个常见但严重的漏洞，可导致远程代码执行（RCE）。这使得攻击者有可能在没有验证的情况下完全控制设备。受影响的型号包括

* **DSR-150**： 所有硬件版本，固件版本 3.13 至 3.17B901C。
* **DSR-150N**：所有硬件版本，固件版本 3.13 至 3.17B901C。
* **DSR-250**： 所有硬件版本，固件版本 3.13 至 3.17B901C。
* **DSR-250N**：所有硬件版本，固件版本 3.13 至 3.17B901C。

鉴于漏洞的严重性，D-Link 已声明不会为这些型号提供固件更新或补丁，因为它们的支持生命周期已经结束。

D-Link 强烈建议用户淘汰和更换这些路由器。该公司强调：“D-Link 美国公司建议退役和更换已达到 EOL/EOS 的 D-Link 设备。”继续使用不支持的设备会使网络暴露于关键漏洞，增加数据泄露的风险。

对于不确定其设备是否受影响的用户，D-Link 建议通过公告中提供的旧版网站链接检查其型号和固件版本。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-vulnerability-in-d-link-eol-routers-allows-remote-code-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302053](/post/id/302053)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-vulnerability-in-d-link-eol-routers-allows-remote-code-execution/)

如若转载,请注明出处： <https://securityonline.info/critical-vulnerability-in-d-link-eol-routers-allows-remote-code-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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