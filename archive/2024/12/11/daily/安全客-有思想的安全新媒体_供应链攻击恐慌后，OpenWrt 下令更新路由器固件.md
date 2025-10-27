---
title: 供应链攻击恐慌后，OpenWrt 下令更新路由器固件
url: https://www.anquanke.com/post/id/302577
source: 安全客-有思想的安全新媒体
date: 2024-12-11
fetch_date: 2025-10-06T19:36:46.126474
---

# 供应链攻击恐慌后，OpenWrt 下令更新路由器固件

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

# 供应链攻击恐慌后，OpenWrt 下令更新路由器固件

阅读量**57836**

发布时间 : 2024-12-10 11:30:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Connor Jones，文章来源：theregister

原文地址：<https://go.theregister.com/feed/www.theregister.com/2024/12/09/openwrt_firmware_vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

OpenWrt用户应将他们的镜像升级到相同的版本，以保护自己免受上周向开源Wi-Fi路由器项目报告的可能的供应链攻击。

OpenWrt的开发者保罗-斯普奥伦（Paul Spooren）上周五给用户发送了一封电子邮件，内容涉及日本安全公司Flatt Security的研究人员Ry0taK两天前报告的该项目出席系统升级服务器（ASU）中的一个安全问题。

Spooren 写道：“由于‘openwrt/imagebuilder’镜像中的命令注入和构建请求哈希中包含的截短 SHA-256 哈希的组合，攻击者可以通过提供导致哈希碰撞的软件包列表来污染合法镜像。”

第一部分是 Imagebuilder 中的命令注入漏洞，其存在的原因是该程序没有正确地对用户提供的软件包名称进行消毒，这使得潜在的攻击者可以生成用合法的构建密钥签名的恶意固件镜像。

第二部分是使用弱散列（CWE-328）漏洞，该漏洞被追踪为 CVE-2024-54143，CVSS 严重性等级暂定为 9.3。

Spooren 说，SHA-256 哈希值被截断为 12 个字符，大大降低了其复杂性，有可能让攻击者产生碰撞。

他说：“利用这一点，先前构建的恶意图片就可以代替合法图片，让攻击者能够‘毒害’人工智能缓存，并向毫无戒心的用户提供受攻击的图片。”

“综合来看，这些漏洞使攻击者能够通过 ASU 服务提供受攻击的固件镜像，从而影响交付的构建的完整性。”

ASU 是一种允许用户更轻松地升级固件，而不触动其软件包和设置的设施。

这些问题影响了所有ASU实例，但由于它们在独立于Buildbot的专用服务器上运行，因此无法访问SSH密钥或签名证书等敏感资源。

OpenWrt表示，其下载页面上的官方镜像和24.10.0-rc2的任何自定义镜像均未受到影响。它检查了其他自定义镜像的构建日志，没有发现任何违规行为；但是，由于自动清理程序的原因，没有检查超过七天的构建。

Spooren 说： “虽然受影响图像的可能性几乎为零，但建议用户就地升级到相同的版本，以消除受此影响的任何可能性。如果你运行的是公共、自托管的 ASU 实例，请立即更新。”

另外，应用 OpenWrt 公告中详述的两个特定提交也能达到同样的效果。

就在该项目宣布与软件自由保护组织（SFC）联合开发首个硬件平台–OpenWrt One–几天后，OpenWrt发布了这一消息。

它被誉为 “维修权运动 ”的一个巨大胜利，SFC称，该设备 “无法被破解”，因为它有一个开关，可以分别闪存NOR和NAND。

本文翻译自theregister [原文链接](https://go.theregister.com/feed/www.theregister.com/2024/12/09/openwrt_firmware_vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302577](/post/id/302577)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://go.theregister.com/feed/www.theregister.com/2024/12/09/openwrt_firmware_vulnerabilities/)

如若转载,请注明出处： <https://go.theregister.com/feed/www.theregister.com/2024/12/09/openwrt_firmware_vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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