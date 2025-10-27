---
title: 无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户
url: https://www.anquanke.com/post/id/308562
source: 安全客-有思想的安全新媒体
date: 2025-06-19
fetch_date: 2025-10-06T22:47:55.493998
---

# 无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户

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

# 无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户

阅读量**1209329**

发布时间 : 2025-06-18 15:22:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/fileless-asyncrat-campaign-targets-german-users-with-stealthy-powershell-payload/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在最近的一项调查中，威胁情报公司 CloudSEK 发现了一个隐蔽的无文件恶意软件活动，该活动利用社会工程和本机系统工具来提供远程访问木马 AsyncRAT。该活动被称为“Clickfix”攻击，旨在引诱讲德语的用户自行执行混淆的 PowerShell 有效负载——所有这些都不会将任何文件放入磁盘。

“*恶意软件是通过虚假的验证提示传递的，引诱用户执行恶意命令*，”CloudSEK 指出。

该活动从一个模拟 CAPTCHA 验证屏幕的网页开始。当用户单击“I’m not a robot”（我不是机器人）时，PowerShell 命令将复制到他们的剪贴板。然后，他们被指示以验证身份为幌子在他们的终端中粘贴并执行此作。根据 CloudSEK 的归因工作，此本地化文本非常可信地表明“*该活动针对讲德语的用户*”。

![无文件恶意软件 AsyncRAT]()

网络杀伤链 |图片来源： CloudSEK

执行后，PowerShell 有效负载会触发多阶段感染链：

* 第 1 步：使用 conhost.exe 在无头模式下调用 PowerShell。
* 第 2 步：从 namoet[.] 下载混淆的有效负载de：80/x.
* 第 3 步：使用 PowerShell 的 Add-Type 功能完全在内存中解码和执行有效负载。

“*该恶意软件通过注册表项建立持久性，并连接到端口 4444 上的远程 TCP C2 服务器*，”报告证实。

这种无文件方法不仅可以减少取证伪像，还可以实现深度系统访问。解密的有效负载在内存中编译和加载 C# 代码，从而建立反向 TCP shell 以 namoet[.]de：4444，让攻击者可以完全控制受害者的机器。

威胁行为者采用了一种巧妙的技术：他们反转 base64 编码的 C# 代码，使用 PowerShell 编译它，并使用静态方法调用它。一个例子：

```
Add-Type -TypeDefinition $($l -join '');
[B]::ma($y.Trim())
```

此方法与 AsyncRAT 的已知 TTP 匹配：

* T1059.001：PowerShell 执行
* T1127.001：交付后的内存中编译
* T1547.001：使用 HKCU：\RunOnce 的注册表持久性
* T1071.001 / T1571：具有非标准端口的应用层协议 （TCP 4444）

“*有效负载包括典型的 byte[] 处理、进程注入和反向格式的嵌入式 base64 C#*”，这与 AsyncRAT 暂存行为直接一致。

该恶意软件通过在以下位置添加注册表项来确保在下次登录时重新执行：

* HKCU：\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
* HKCU：\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows

此外，CloudSEK 还观察到以下规避技术：

* 没有文件写入磁盘
* 通过混淆命令进行反调试
* 禁用 Windows Defender
* 使用 conhost.exe 和 powershell.exe 等 LOLBin

鉴于其复杂性和隐蔽性，Clickfix AsyncRAT 活动需要多层防御策略：

* 阻止可疑的 PowerShell 执行，尤其是无头或隐藏的实例。
* 监控注册表修改，尤其是 Run 和 RunOnce 键。
* 实施内存扫描工具以检测内存中的 C# 编译和模糊处理的有效负载。
* 使用威胁情报源阻止已知的 IOC，例如 和 port 。`namoet[.]de``4444`

本文翻译自securityonline [原文链接](https://securityonline.info/fileless-asyncrat-campaign-targets-german-users-with-stealthy-powershell-payload/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308562](/post/id/308562)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/fileless-asyncrat-campaign-targets-german-users-with-stealthy-powershell-payload/)

如若转载,请注明出处： <https://securityonline.info/fileless-asyncrat-campaign-targets-german-users-with-stealthy-powershell-payload/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**11赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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