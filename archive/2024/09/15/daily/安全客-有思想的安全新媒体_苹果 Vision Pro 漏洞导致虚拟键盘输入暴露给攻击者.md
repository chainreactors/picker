---
title: 苹果 Vision Pro 漏洞导致虚拟键盘输入暴露给攻击者
url: https://www.anquanke.com/post/id/300109
source: 安全客-有思想的安全新媒体
date: 2024-09-15
fetch_date: 2025-10-06T18:20:11.416576
---

# 苹果 Vision Pro 漏洞导致虚拟键盘输入暴露给攻击者

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

# 苹果 Vision Pro 漏洞导致虚拟键盘输入暴露给攻击者

阅读量**111026**

发布时间 : 2024-09-14 14:57:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/apple-vision-pro-vulnerability-exposed.html>

译文仅供参考，具体内容表达以及含义原文为准。

有关影响 Apple Vision Pro 混合现实耳机的现已修补的安全漏洞的详细信息已经浮出水面，如果成功利用该漏洞，可能会允许恶意攻击者推断在设备的虚拟键盘上输入的数据。

这次名为 **GAZEploit** 的攻击已被分配 CVE 标识符 CVE-2024-40865。

“一种新颖的攻击，可以从头像图像中推断出与眼睛相关的生物识别技术，以重建通过凝视控制打字输入的文本，”来自佛罗里达大学、CertiK Skyfall 团队和德克萨斯理工大学的一组学者说。

“GAZEploit 攻击利用了用户共享虚拟形象时凝视控制文本输入中固有的漏洞。”

在负责任地披露后，Apple 在 2024 年 7 月 29 日发布的 visionOS 1.3 中解决了该问题。它将该漏洞描述为影响名为 Presence 的组件。

“虚拟键盘的输入可以从 Persona 推断出来，”它在安全公告中说，并补充说它通过“当虚拟键盘处于活动状态时暂停 Persona”来解决问题。

简而言之，研究人员发现，可以分析虚拟形象的眼球运动（或“凝视”）以确定佩戴耳机的用户在虚拟键盘上输入的内容，从而有效地损害了他们的隐私。

因此，假设威胁行为者可以分析通过视频通话、在线会议应用程序或直播平台共享的虚拟形象，并远程执行击键推理。然后，可以利用它来提取敏感信息，例如密码。

反过来，攻击是通过在 Persona 记录、眼睛纵横比 （EAR） 和眼睛凝视估计上训练的监督学习模型来实现的，以区分打字会话和其他与 VR 相关的活动（例如，看电影或玩游戏）。

在后续步骤中，将虚拟键盘上的视线估计方向映射到特定键，以便确定可能的击键，使其也考虑到键盘在虚拟空间中的位置。

“通过远程捕获和分析虚拟形象视频，攻击者可以重建键入的键，”研究人员说。“值得注意的是，GAZEploit 攻击是该领域已知的第一次攻击，它利用泄露的凝视信息远程执行击键推理。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/apple-vision-pro-vulnerability-exposed.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300109](/post/id/300109)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/apple-vision-pro-vulnerability-exposed.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/apple-vision-pro-vulnerability-exposed.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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