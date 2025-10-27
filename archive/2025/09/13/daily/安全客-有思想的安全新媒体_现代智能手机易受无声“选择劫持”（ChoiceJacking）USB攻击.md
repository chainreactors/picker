---
title: 现代智能手机易受无声“选择劫持”（ChoiceJacking）USB攻击
url: https://www.anquanke.com/post/id/312088
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:23.035282
---

# 现代智能手机易受无声“选择劫持”（ChoiceJacking）USB攻击

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

# 现代智能手机易受无声“选择劫持”（ChoiceJacking）USB攻击

阅读量**71487**

发布时间 : 2025-09-12 17:35:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Mann ，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/modern-smartphones-vulnerable-to-silent-choicejacking-usb-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为“选择劫持”（ChoiceJacking）的USB攻击通过恶意充电器伪造用户授权弹窗，静默访问敏感数据，从而绕过Android和iOS设备的防护机制。

该攻击突破了针对“果汁劫持”（JuiceJacking）的长期防御措施，导致当前几乎所有USB数据保护机制失效。

ChoiceJacking由格拉茨理工大学研究人员开发，其通过在单一攻击链中融合USB主机与外设功能，使曾被缓解的恶意充电 station 威胁死灰复燃。

早期JuiceJacking依赖默认信任USB连接，而现代系统需用户交互授权数据访问。ChoiceJacking则通过注入伪造输入事件模拟用户批准，实现无需合法交互即可完成攻击。

![]()

### **三种攻击技术**

研究人员发现三种攻击手法，均通过制造成本低于100美元的特制充电器发起：

1. **AOAP漏洞利用**：滥用Android开放配件协议（AOAP），在USB数据协商阶段注入输入事件，使充电器在用户不知情的情况下确认文件访问或调试提示。
2. **输入队列竞争条件**：向Android输入事件队列填充伪造序列，在用户授权弹窗出现时精准执行，自动确认弹窗。
3. **蓝牙HID spoofing**：通过充电器配对隐藏蓝牙键盘，操控UI界面批准USB连接——此方法对iOS同样有效。

这三种技术均利用USB信任模型的系统性缺陷，使充电器可通过USB电力传输（USB Power Delivery）切换主机与外设角色，实现此前缓解措施未覆盖的混合攻击。

![]()

为提升隐蔽性，研究人员引入**电力线侧信道（PLSC）**，通过检测手机通话、屏幕关闭或用户分心等时机发起攻击。充电器监控电力波动以推断用户活动状态，并在检测风险最低时启动攻击。

该机制通过机器学习模型训练，能基于充电器的实时电流数据区分通话活动和屏幕状态。

### **受影响设备与攻击效果**

移动操作系统当前虽要求用户交互批准USB主机连接（如文件传输或调试），但默认信任输入设备和配件。ChoiceJacking通过模拟输入设备自动化批准流程，正是利用了这一信任缺口。

研究人员认为，随着USB-C双角色端口普及，这种信任模型存在根本性缺陷：恶意硬件可灵活切换主机与设备模式，实施传统缓解措施无法阻断的组合攻击。

团队测试了11款主流厂商设备，结果如下：

1. **三星**：所有测试设备在**300毫秒内**被攻陷。
2. **小米**：即便未开启开发者模式，仍能获取完整ADB访问权限。
3. **OPPO & 荣耀**：**屏幕锁定状态下**攻击依然成功。
4. **谷歌Pixel & vivo**：对AOSP原生系统稍作修改即可成功攻击。
5. **苹果（iPad Pro）**：可通过PTP协议提取照片，但因认证要求无法执行代码。

![]()

Android设备平均**333毫秒**内实现文件访问；未锁屏且开启开发者模式的设备中，完整代码执行耗时不到**316毫秒**。

### **漏洞披露与缓解建议**

团队已向厂商披露16个特定漏洞，并向谷歌、苹果报告上游问题。除一家厂商外，所有厂商均确认了问题。谷歌和三星已分配CVE编号（**CVE-2024-43085**、**CVE-2024-20900**），缓解工作正在进行中。

在安全补丁推送前，建议用户避免连接公共USB充电 station，并启用iOS“锁定模式”或Android“高级安全模式”以阻断USB攻击。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/modern-smartphones-vulnerable-to-silent-choicejacking-usb-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312088](/post/id/312088)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/modern-smartphones-vulnerable-to-silent-choicejacking-usb-attacks/)

如若转载,请注明出处： <https://cyberinsider.com/modern-smartphones-vulnerable-to-silent-choicejacking-usb-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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