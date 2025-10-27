---
title: APT 组织 StormBamboo 通过 DNS 欺骗攻击 ISP 客户
url: https://www.anquanke.com/post/id/298835
source: 安全客-有思想的安全新媒体
date: 2024-08-07
fetch_date: 2025-10-06T18:02:18.345202
---

# APT 组织 StormBamboo 通过 DNS 欺骗攻击 ISP 客户

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

# APT 组织 StormBamboo 通过 DNS 欺骗攻击 ISP 客户

阅读量**87154**

发布时间 : 2024-08-06 11:32:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Phil Muncaster，文章来源：infosecurity magazine

原文地址：<https://www.infosecurity-magazine.com/news/apt-stormbamboo-isp-dns-poisoning/>

译文仅供参考，具体内容表达以及含义原文为准。

安全研究人员揭露了一起复杂的供应链攻击活动，该活动源自一家未具名互联网服务提供商（ISP）的遭入侵事件。

Volexity公司指出，StormBamboo组织（又称为Evasive Panda、Daggerfly、StormCloud）利用其在该ISP中的立足点，对选定的客户发起了DNS毒化攻击。

Volexity确定，StormBamboo组织篡改了特定域的DNS查询响应，这些域与自动软件更新机制相关。StormBamboo似乎针对的是那些使用不安全更新机制的软件，例如HTTP，这些软件没有正确验证安装程序的数字签名，”它解释道。

“因此，当这些应用程序去获取它们的更新时，它们安装的不是预期的更新，而是包括但不限于MACMA和POCOSTICK（又称为MGBot）在内的恶意软件。”

MACMA是针对macOS的后门恶意软件，而MGBot则作用于Windows系统。

该组织以这种方式针对了多个使用不安全更新流程的供应商，其中包括媒体播放软件5KPlayer。它会将应用程序发出的合法HTTP更新请求重定向至其控制下的命令与控制服务器，该服务器托管着伪造的文本文件和恶意安装程序，Volexity解释道。

有一次，研究人员观察到StormBamboo在一个已被入侵的受害者的机器上部署了一个恶意Chrome扩展。该扩展程序旨在将浏览器cookies数据泄露至由该组织控制的Google云端硬盘账户。

幸运的是，Volexity通知了涉事的ISP，后者对其网络中提供流量路由服务的设备进行了调查。

Volexity表示：“随着ISP重启并将其网络的各个组件下线，DNS毒化立即停止了。”“在此期间，无法确定具体哪台设备被入侵，但基础设施的各部分被更新或保持离线状态，相关活动也就停止了。”

本文翻译自infosecurity magazine [原文链接](https://www.infosecurity-magazine.com/news/apt-stormbamboo-isp-dns-poisoning/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298835](/post/id/298835)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity magazine](https://www.infosecurity-magazine.com/news/apt-stormbamboo-isp-dns-poisoning/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/apt-stormbamboo-isp-dns-poisoning/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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