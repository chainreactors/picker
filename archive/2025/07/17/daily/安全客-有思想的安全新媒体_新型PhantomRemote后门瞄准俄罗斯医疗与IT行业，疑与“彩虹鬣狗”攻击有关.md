---
title: 新型PhantomRemote后门瞄准俄罗斯医疗与IT行业，疑与“彩虹鬣狗”攻击有关
url: https://www.anquanke.com/post/id/310157
source: 安全客-有思想的安全新媒体
date: 2025-07-17
fetch_date: 2025-10-06T23:27:43.468930
---

# 新型PhantomRemote后门瞄准俄罗斯医疗与IT行业，疑与“彩虹鬣狗”攻击有关

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

# 新型PhantomRemote后门瞄准俄罗斯医疗与IT行业，疑与“彩虹鬣狗”攻击有关

阅读量**79331**

发布时间 : 2025-07-16 18:18:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/new-phantomremote-backdoor-targets-russian-healthcare-it-linked-to-rainbow-hyena-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**俄罗斯医疗和 IT 行业正遭遇新一轮钓鱼攻击**，幕后黑手被认定为行踪诡秘的 **“彩虹鬣狗”（Rainbow Hyena）威胁团伙**。据 BI.ZONE 威胁情报团队透露，该团伙部署了一款**此前未被记录**的后门程序**PhantomRemote**，展现出较高的技术成熟度和不断升级的攻击策略。

攻击者利用合法机构的 compromised 电子邮件账户发送邮件，主题包括：

* 《运输单 TTN 第 391-44 号（2025 年 6 月 26 日）》
* 《合同 RN83-371》

每封邮件均附带一个 “多语言” ZIP 附件，**表面看似合法压缩包**，实则包含 **PE32 + 格式的 DLL 文件**，内部还藏有一个**.LNK 文件**，用于启动**隐蔽的感染链**。

该.LNK 文件的**设计功能**包括：

1. 在用户目录中**搜索**上述 “多语言” ZIP 文件
2. 通过 rundll32.exe **执行**嵌入的 DLL 文件
3. 将诱饵文档**解压**至 TEMP 文件夹以降低用户怀疑
4. 通过隐蔽的 PowerShell 命令**打开**诱饵文件

BI.ZONE 解释道：“这些邮件包含‘多语言’ZIP 附件…… 其中隐藏了一个诱饵文档和一个含.LNK 文件的 ZIP 压缩包。”

从.LNK 文件中的一个示例命令可见，此次攻击链**嵌入极深且经过混淆处理**，融合了 **PowerShell、ZIP 解压和 DLL 注入**等多种技术。

BI.ZONE 最重要的发现是一个**全新的恶意软件家族** ——**PhantomRemote**，这是一款用 **C++** 编写的 **PE32 + 格式 DLL** 文件。

PhantomRemote 一旦执行，会进行以下操作：

1. **收集系统元数据**，包括 GUID、计算机名和域名
2. 在 % PROGRAMDATA% 目录下**创建隐藏工作目录**，如 “YandexCloud” 或 “MicrosoftAppStore”
3. **与命令控制（C2）服务器建立通信**，服务器地址为 http://91.239.148 [.] 21/poll?id=&hostname=&domain=
4. 通过 cmd.exe **执行命令、下载文件**，并通过 HTTP POST **请求发送结果**

值得注意的是，其通信流量使用 **“YandexCloud/1.0”“MicrosoftAppStore/2001.0”** 等自定义 User-Agent 头部，以**伪装成合法软件流量**。

PhantomRemote至少支持**两种命令类型**：

1. **cmd:<命令>：**执行系统命令并捕获输出结果
2. **download:<URL>：**从指定 URL 获取文件并存储至工作目录

执行命令后，PhantomRemote 会等待 10 秒；若命令执行失败，则等待 1 秒。这一机制表明其具备**基础但有效的延迟控制功能**。

报告指出：“该后门程序收集受 compromise 系统的信息，从命令控制服务器加载其他可执行文件，并通过 cmd.exe 解释器运行命令。”

BI.ZONE 提到，“彩虹鬣狗” 最初被认为是一个黑客激进组织，如今已逐渐转向**间谍活动和以经济利益为目的的网络犯罪**。

报告总结道：“黑客激进组织正越来越多地转向间谍活动、敛财等更常规的非法活动，同时采用**更复杂的方法和工具**。”

本文翻译自securityonline [原文链接](https://securityonline.info/new-phantomremote-backdoor-targets-russian-healthcare-it-linked-to-rainbow-hyena-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310157](/post/id/310157)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-phantomremote-backdoor-targets-russian-healthcare-it-linked-to-rainbow-hyena-attacks/)

如若转载,请注明出处： <https://securityonline.info/new-phantomremote-backdoor-targets-russian-healthcare-it-linked-to-rainbow-hyena-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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