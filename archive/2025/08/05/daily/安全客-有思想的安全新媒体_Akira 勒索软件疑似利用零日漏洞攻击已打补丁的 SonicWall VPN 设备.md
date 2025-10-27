---
title: Akira 勒索软件疑似利用零日漏洞攻击已打补丁的 SonicWall VPN 设备
url: https://www.anquanke.com/post/id/310863
source: 安全客-有思想的安全新媒体
date: 2025-08-05
fetch_date: 2025-10-07T00:17:42.414807
---

# Akira 勒索软件疑似利用零日漏洞攻击已打补丁的 SonicWall VPN 设备

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

# Akira 勒索软件疑似利用零日漏洞攻击已打补丁的 SonicWall VPN 设备

阅读量**95520**

发布时间 : 2025-08-04 17:17:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/08/akira-ransomware-exploits-sonicwall.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

SonicWall SSL VPN 设备近日成为 Akira 勒索软件攻击的目标。安全研究人员指出，这轮攻击活动自 2025 年 7 月下旬起明显增多。

Arctic Wolf Labs 的研究员 Julian Tuin 在报告中表示：“我们观察到多起勒索软件攻击前的入侵行为都涉及 **SonicWall SSL VPN 的远程访问**，并且这些入侵在短时间内频繁发生。”

报告指出，攻击者可能利用了 SonicWall 设备中一个尚未公开的安全漏洞（零日漏洞），因为部分受害设备已经打上了所有官方补丁。不过，研究人员也未排除攻击者是通过凭证获取实现初始访问的可能性。

此次针对 SonicWall VPN 的攻击**最早记录于 2025 年 7 月 15 日**，但 Arctic Wolf 表示，早在 2024 年 10 月就已发现类似的恶意 VPN 登录行为，说明攻击者长期关注并持续利用该类设备。

“从首次通过 SSL VPN 获取账户访问权限到勒索加密执行之间的时间非常短。”报告补充道，“与正常 VPN 登录通常来自宽带运营商网络不同，勒索软件团伙更常通过**虚拟私人服务器（VPS）**进行 VPN 认证，以隐藏真实来源。”

截至本文发布，SonicWall 官方尚未就相关攻击作出回应。鉴于可能涉及零日漏洞，Arctic Wolf 建议企业在补丁发布并应用之前，可考虑**暂时禁用 SonicWall SSL VPN 服务**。

同时，研究人员还建议采取以下防护措施：

* **为远程访问强制启用多因素认证（MFA）；**
* **删除不再使用或长期未登录的本地防火墙账户；**
* **严格执行密码管理规范。**

Akira 勒索软件自 2023 年 3 月首次现身以来，至 2024 年初估计已通过攻击超过 250 个目标勒索了约 **4200 万美元**的非法收益。

根据 Check Point 发布的数据，Akira 是 2025 年第二季度攻击活跃度排名第二的勒索团伙，仅次于 Qilin，在该季度中声称攻击了 143 名受害者。

此外，报告指出 Akira 此次瞄准的受害者中有 **10% 来自意大利公司**，远高于整体平均的 3%。

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/08/akira-ransomware-exploits-sonicwall.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310863](/post/id/310863)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/08/akira-ransomware-exploits-sonicwall.html)

如若转载,请注明出处： <https://thehackernews.com/2025/08/akira-ransomware-exploits-sonicwall.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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