---
title: PumaBot恶意软件瞄准Linux物联网设备
url: https://www.anquanke.com/post/id/307974
source: 安全客-有思想的安全新媒体
date: 2025-05-30
fetch_date: 2025-10-06T22:23:26.071178
---

# PumaBot恶意软件瞄准Linux物联网设备

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

# PumaBot恶意软件瞄准Linux物联网设备

阅读量**85925**

发布时间 : 2025-05-29 15:21:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Prajeet Nair，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/pumabot-malware-targets-linux-iot-devices-a-28526>

译文仅供参考，具体内容表达以及含义原文为准。

![PumaBot 恶意软件以 Linux IoT 设备为目标]()

在巴西戈亚斯圈养的美洲狮。（图片：Leonardo Mercon/Shutterstock）

针对在 Linux作系统上运行的物联网设备的僵尸网络通过暴力破解凭据和下载加密挖矿软件来工作。

**另请参阅：**破解密码：保护机器身份

Darktrace 的研究人员将僵尸网络命名为“PumaBot”，因为它的恶意软件会检查字符串“Pumatronix”。这是巴西一家监控和交通摄像头系统制造商的名字，“暗示潜在的 IoT 目标或试图规避特定设备。该机器人还会对环境进行指纹识别，以避免出现蜜罐或受限 shell。

与僵尸网络不同，该恶意软件不会扫描互联网以查找机会主义目标。相反，它连接到命令和控制服务器，该服务器提供可能具有开放 SSH 端口的设备的 IP 地址列表。在进行 Darktrace 分析时，与服务器关联的域未解析为 Internet 地址。`ssh.ddos-cc.org`

一个关键的恶意用途是劫持受感染的设备进行加密货币挖掘。通过在受感染的系统上运行加密挖矿软件，僵尸网络会耗尽设备的处理能力和能源资源。分析师认为，PumaBot 可能成为在智慧城市或工业监控网络中建立隐蔽、长期立足点的更大规模活动的一部分。

PumaBot 主要通过编写自定义 ，一个封装了有关系统服务和侦听套接字信息的配置文件，专注于隐蔽渗透和长期控制。它还将自己的 SSH 密钥添加到文件中，确保即使有人删除了流氓文件也能保持持久性。`systemmd service unit``authorized_keys``systemmd service unit`

该恶意软件将自身安装在隐藏目录中，并创建欺骗性的 systemd 服务，例如 和 。`/lib/redis``redis.service``mysqI.service`

该恶意软件使用自定义 HTTP 标头与其 C2 通信，包括不常见的 X-API-KEY、.它发回系统指纹，包括架构、内核版本和用户凭证。这些数据可帮助运营商维护受感染基础设施的实时地图，并在需要时部署定制的有效负载。`jieruidashabi`

作为更广泛的 PumaBot 活动的一部分，Darktrace 还观察到了相关的二进制文件，包括一个名为持久性后门和一个名为 的组件，该组件通过 MD5 哈希检查执行 SSH 暴力破解和自我更新。`ddaemon``networkxm`

另一个关键部分是 bash 脚本，它使用恶意文件修改 Linux 可插拔身份验证模块身份验证堆栈，以在本地和远程登录中收集凭据。`installx.sh``pam_unix.so`

为了泄露数据，仅命名为“1”的文件观察器二进制文件会监视存储在隐藏文件中的被盗凭据，然后将它们发送到远程服务器。此数据包括 SSH 凭据、系统 IP 地址和端口扫描结果。`con.txt`

研究人员说：“虽然它似乎不像传统蠕虫那样自动传播，但它确实通过暴力攻击目标保持了类似蠕虫的行为，这表明这是一个专注于设备入侵和长期访问的半自动化僵尸网络活动。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/pumabot-malware-targets-linux-iot-devices-a-28526)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307974](/post/id/307974)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/pumabot-malware-targets-linux-iot-devices-a-28526)

如若转载,请注明出处： <https://www.govinfosecurity.com/pumabot-malware-targets-linux-iot-devices-a-28526>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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