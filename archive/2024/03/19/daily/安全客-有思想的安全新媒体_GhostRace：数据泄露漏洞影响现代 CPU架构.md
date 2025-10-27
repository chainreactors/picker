---
title: GhostRace：数据泄露漏洞影响现代 CPU架构
url: https://www.anquanke.com/post/id/294035
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:48.705852
---

# GhostRace：数据泄露漏洞影响现代 CPU架构

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

# GhostRace：数据泄露漏洞影响现代 CPU架构

阅读量**82638**

发布时间 : 2024-03-18 11:02:13

**x**

##### 译文声明

本文是翻译文章，文章来源：https://thehackernews.com/2024/03/ghostrace-new-data-leak-vulnerability.html

译文仅供参考，具体内容表达以及含义原文为准。

一组研究人员发现了一种新的数据泄漏攻击，该攻击会影响支持推测执行的现代 CPU 架构。

它被称为GhostRace ( CVE-2024-2193 )，是称为 Spectre v1 (CVE-2017-5753) 的瞬时执行 CPU 漏洞的变体。该方法结合了推测执行和竞争条件。

“使用条件分支实现的所有常见同步原语都可以使用分支误预测攻击在推测路径上从微架构上绕过，将所有架构上无竞争的关键区域转变为推测竞争条件（SRC），从而允许攻击者从目标泄漏信息，”研究人员表示。

IBM 欧洲研究院系统安全研究小组和 VUSec 的调查结果，后者于 2023 年 12 月披露了另一种名为SLAM的旁道攻击，针对现代处理器。

Spectre 是指一类旁道攻击，它利用现代 CPU 上的分支预测和推测执行来读取内存中的特权数据，绕过应用程序之间的隔离保护。

虽然推测执行是大多数 CPU 使用的性能优化技术，但 Spectre 攻击利用了错误预测在处理器缓存中留下内存访问或计算痕迹的事实。

Spectre 攻击背后的研究人员在一月份指出：“Spectre 攻击会诱使受害者推测性地执行在严格序列化的程序指令处理过程中不会发生的操作，并通过隐蔽通道将受害者的机密信息泄露给对手。 ” 2018.

这些漏洞的发现以及 Meltdown 导致多年来对微处理器架构进行了更广泛的审查，甚至促使 MITRE 常见弱点枚举 (CWE) 计划添加了四个与瞬时执行（从CWE-1420 至 CWE-1423）上个月末。

GhostRace 值得注意的是，它使未经身份验证的攻击者能够利用竞争条件从处理器中提取任意数据，从而通过所谓的推测并发释放后使用 (SCUAF) 攻击来访问推测的可执行代码路径。

竞争条件是一种不良情况，当两个或多个进程在没有适当同步的情况下尝试访问相同的共享资源时，会发生这种情况，从而导致结果不一致，并为攻击者执行恶意操作打开了机会之窗。

“在特征和利用策略方面，SRC 漏洞与经典的竞争条件类似，”CERT 协调中心 (CERT/CC)在一份公告中解释道。

“然而，不同之处在于，攻击者在源自错误推测的分支（类似于 Spectre v1）的瞬时执行路径上利用所述竞争条件，以最终向攻击者泄露信息的恶意代码片段或小工具为目标。”

最终结果是，它允许有权访问 CPU 资源的攻击者从主机内存中访问任意敏感数据。

“任何软件，例如操作系统、虚拟机管理程序等，通过条件分支实现同步原语，而该路径上没有任何序列化指令，并且在任何微体系结构（例如，x86、ARM、RISC-V 等）上运行，这允许条件分支投机执行的分支很容易受到 SRC 的影响，”VUSec说。

在负责任地披露后，AMD表示其针对 Spectre 的现有指南“仍然适用于缓解此漏洞”。Xen 开源虚拟机管理程序的维护者承认所有版本都会受到影响，尽管他们表示这不太可能构成严重的安全威胁。

Xen表示：“出于谨慎考虑，Xen 安全团队提供了强化补丁，包括在 x86 上添加新的 LOCK\_HARDEN 机制，类似于现有的 BRANCH\_HARDEN 。 ”

“由于 Xen 下存在漏洞的不确定性以及性能影响的不确定性，LOCK\_HARDEN 默认处于关闭状态。但是，我们预计在该领域会进行更多研究，并认为采取缓解措施是谨慎的做法。 ”

本文翻译自https://thehackernews.com/2024/03/ghostrace-new-data-leak-vulnerability.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294035](/post/id/294035)

安全KER - 有思想的安全新媒体

本文转载自: https://thehackernews.com/2024/03/ghostrace-new-data-leak-vulnerability.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**6赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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