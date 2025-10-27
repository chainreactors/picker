---
title: Microsoft 要求 Windows Insiders 试用有争议的 Recall 功能
url: https://www.anquanke.com/post/id/302186
source: 安全客-有思想的安全新媒体
date: 2024-11-27
fetch_date: 2025-10-06T19:12:20.435284
---

# Microsoft 要求 Windows Insiders 试用有争议的 Recall 功能

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

# Microsoft 要求 Windows Insiders 试用有争议的 Recall 功能

阅读量**50004**

发布时间 : 2024-11-26 11:17:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/11/25/microsoft-windows-insiders-try-out-windows-recall/>

译文仅供参考，具体内容表达以及含义原文为准。

Windows Insider 计划的参与者，只要拥有一台搭载高通骁龙处理器的 Copilot+ PC，现在就可以试用 Recall，这项声名狼藉的快照拍摄和人工智能功能在今年早些时候推出时曾饱受批评。

“我们听到了你们的反馈，认为在组织中使用 Recall 需要安全、可控的体验。”Windows 市场营销高级总监梅丽莎-格兰特（Melissa Grant）上周表示：“默认情况下，Recall 将被禁用，IT 部门可以通过新策略启用该功能，然后再由个人选择是否使用。”

**回应投诉**

在最初的批评有理有据之后，微软暂时放弃了发布该功能，并表示将使该功能成为选择性启用（而不是默认 “开启”），并通过加密屏幕快照中存储的数据和通过可信平台模块保护加密密钥来加强对这些数据的保护，可信平台模块与用户的 Windows Hello 增强登录安全身份绑定。

微软还：

* 实施速率限制和反骚扰措施，保护 Recall 存储的数据免受暴力破解攻击
* 使 Recall 不保存私人浏览会话的信息
* 默认启用敏感内容过滤

**针对 Windows Insiders 的 Windows Recall 又回来了**

上周五，公司终于呼吁 Windows Insiders 试用该功能。

首先，他们必须选择保存快照，要做到这一点，他们必须启用 BitLocker 和安全启动，并注册 Windows Hello（即通过面部识别、指纹或 PIN 登录）。

用户可以暂停/恢复快照的拍摄；从快照中排除应用程序、网站和敏感信息；删除快照–所有这些都可以通过 “调用 ”的特定设置来实现。

![try Windows Recall]()

Windows 11 Recall 隐私和安全设置（来源：微软）

但最重要的是，微软已经解决了安全研究人员和隐私倡导者提出的一些痛点。

首先，Recall 会检测敏感信息–信用卡信息、密码和个人身份号码–并不会保存或存储包含这些信息的快照。

其次，保存的快照不会离开用户的电脑，不会被微软用于培训目的，微软也无法获取查看加密数据所需的密钥。

该公司表示：“我们不会将你的快照从你的电脑发送给微软或第三方，也不会将它们用于培训目的。”

最后，由 IT 管理员管理的工作、学校和企业版 Windows 11 PC 将默认删除 Recall 功能。

微软补充说：“IT 管理员可以完全控制其组织内 Recall 的可用性。”

“员工必须选择保存快照，并使用 Windows Hello 注册脸部或指纹才能保存快照。只有已登录的用户才能访问和解密 Recall 数据，因此尽管企业无法访问员工的 Recall 数据，但可以完全阻止 Recall 的使用，并阻止对特定应用程序或网站的任何保存。”

微软在另一份关于如何使用该功能的指南中进一步解释说，该功能默认情况下将适用于不受组织或学校管理的设备，用户需要选择保存快照。

用户还可以通过以下方式移除/关闭该功能：

* 在任务栏的搜索框中输入打开或关闭Windows功能
* 从对话框中取消选中 “调用”，然后重新启动电脑。

**查找安全漏洞**

Windows Insiders 现在可以试用 Windows Recall，并敦促他们将遇到的问题报告给微软，而安全研究人员则有望从中发现安全漏洞。

“我被告知，作为 Insider 计划的一部分，Recall 有资格获得漏洞赏金。我认为这个过程应该是沙箱式的，所以理论上（我的理解），奖金限额应该是 2 万美元，”安全研究人员凯文-博蒙特（Kevin Beaumont）说。

微软没有透露何时向公众提供Recall。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/11/25/microsoft-windows-insiders-try-out-windows-recall/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302186](/post/id/302186)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/11/25/microsoft-windows-insiders-try-out-windows-recall/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/11/25/microsoft-windows-insiders-try-out-windows-recall/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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