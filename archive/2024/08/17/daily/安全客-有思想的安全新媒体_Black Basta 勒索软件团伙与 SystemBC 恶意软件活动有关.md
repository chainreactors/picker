---
title: Black Basta 勒索软件团伙与 SystemBC 恶意软件活动有关
url: https://www.anquanke.com/post/id/299205
source: 安全客-有思想的安全新媒体
date: 2024-08-17
fetch_date: 2025-10-06T18:02:14.059491
---

# Black Basta 勒索软件团伙与 SystemBC 恶意软件活动有关

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

# Black Basta 勒索软件团伙与 SystemBC 恶意软件活动有关

阅读量**48063**

发布时间 : 2024-08-16 14:43:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167079/cyber-crime/black-basta-ransomware-systembc-campaign.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 专家们将正在进行的旨在部署恶意软件 SystemBC 的社会工程活动与 Black Basta 勒索软件组织联系起来。

Rapid7 研究人员发现了一项新的社会工程活动，该活动将 SystemBC 滴管分发到 Black Basta 勒索软件操作中。

2024 年 6 月 20 日，Rapid7 研究人员检测到多次攻击，这与 Rapid7 正在跟踪的持续社会工程活动一致。专家们注意到，在最近的事件中，威胁行为者使用的工具发生了重要转变。

攻击链以相同的方式开始，威胁行为者发送电子邮件炸弹，然后尝试致电目标用户，通常通过 Microsoft Teams，以提供虚假解决方案。他们诱骗用户安装AnyDesk，允许远程控制他们的计算机。

在攻击过程中，攻击者部署了一个名为 AntiSpam.exe 的凭据收集工具，该工具伪装成垃圾邮件过滤器更新程序。此工具会提示用户输入其凭据，然后保存或记录这些凭据以供以后使用。

![]()

攻击者使用了各种名为与其初始诱饵对齐的有效载荷，包括 SystemBC 恶意软件、Golang HTTP 信标和 Socks 代理信标。

研究人员注意到使用了一个名为旨在利用漏洞 CVE-2022-26923 进行权限提升的可执行文件，并使用反向 SSH 隧道和级别远程监控和管理 （RMM） 工具进行横向移动和维护访问。`update6.exe`

*Rapid7 发布的报告中写道：“执行时，如果环境中使用的域控制器易受攻击，`update6.exe`将尝试利用 CVE-2022-26923 添加计算机帐户。“调试符号数据库路径保持不变，并指示以下内容：`C：\Users\lfkmf\source\repos\AddMachineAccount\x64\Release\AddMachineAccount.pdb`。原始源代码可能是从 Outflank 创建的公开可用的 Cobalt Strike 模块复制而来的。*

中的 SystemBC 有效负载是从加密资源中动态检索的，并直接注入到同名的子进程中。原始 SystemBC 文件使用 XOR 密钥进行加密，由于 PE 部分之间的填充 null 字节的加密，此密钥会公开。`update8.exe`

研究人员建议通过阻止所有未经批准的远程监控和管理解决方案来减轻威胁。AppLocker 或 Microsoft Defender 应用程序控制可以阻止所有未经批准的 RMM 解决方案在环境中执行。

Rapid7 还建议：

* 对用户进行有关 IT 通信渠道的教育，以发现并避免社会工程攻击。
* 鼓励用户举报声称来自IT人员的可疑电话和短信。
* 保持软件更新以防范已知漏洞，包括应用 CVE-2022-26923 补丁以防止易受攻击的域控制器上的权限提升。

该报告还包括此活动的妥协指标。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167079/cyber-crime/black-basta-ransomware-systembc-campaign.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299205](/post/id/299205)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167079/cyber-crime/black-basta-ransomware-systembc-campaign.html)

如若转载,请注明出处： <https://securityaffairs.com/167079/cyber-crime/black-basta-ransomware-systembc-campaign.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

### 热门推荐

文章目录

* [专家们将正在进行的旨在部署恶意软件 SystemBC 的社会工程活动与 Black Basta 勒索软件组织联系起来。](#h2-0)

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