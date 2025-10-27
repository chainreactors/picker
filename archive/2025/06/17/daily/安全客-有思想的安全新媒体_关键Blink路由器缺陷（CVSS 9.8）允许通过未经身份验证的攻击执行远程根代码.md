---
title: 关键Blink路由器缺陷（CVSS 9.8）允许通过未经身份验证的攻击执行远程根代码
url: https://www.anquanke.com/post/id/308486
source: 安全客-有思想的安全新媒体
date: 2025-06-17
fetch_date: 2025-10-06T22:47:56.254671
---

# 关键Blink路由器缺陷（CVSS 9.8）允许通过未经身份验证的攻击执行远程根代码

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

# 关键Blink路由器缺陷（CVSS 9.8）允许通过未经身份验证的攻击执行远程根代码

阅读量**50749**

发布时间 : 2025-06-16 15:54:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-blink-router-flaws-cvss-9-8-allow-remote-root-code-execution-via-unauthenticated-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Blink 路由器，关键漏洞]()

在多种型号的 Blink 路由器 BL 中披露了五个关键漏洞，每个漏洞的 CVSS 为 9.8，使用户通过未经身份验证的 HTTP 请求面临未经授权的命令注入攻击。这些漏洞被跟踪为 CVE-2025-45984 到 CVE-2025-45988，影响消费者和企业级网络设备中使用的各种固件版本。

这些漏洞存在于 /bin/goahead Web 服务器组件和相关共享库中，允许攻击者以 root 权限执行任意系统命令，从而有效地完全控制受影响的设备。

* **CVE-2025-45984：通过密码纵路由到 root –**此漏洞源于 sub\_45B238 函数，其中对 routepwd 参数的不当过滤会导致未经清理的输入被传递给 sprintf，并最终通过 bl\_do\_system 函数执行。对 /goform/set\_manpwd构建的 POST 请求允许攻击者链接 shell 命令并创建系统级工件，例如文件夹。
* **CVE-2025-45985：SSID Stealth 漏洞 –**sub\_44D9F4 函数通过 enable 参数容易受到攻击，该参数在作时会将命令从 libshare-0.0.26.so 注入 bs\_SetSSIDHide 函数。通过滥用 /goform/set\_hidessid\_cfg 端点，攻击者可以执行任意 shell 命令。
* **CVE-2025-45986：MAC 过滤变成了恶意软件网关 –**共享库中的 sub\_45BD1C 函数和 bs\_SetMacBlack 也受到相同的监督。恶意行为者可以利用 mac 参数通过 /goform/set\_blacklist 插入命令序列。
* **CVE-2025-45987：用作命令代理的 DNS 字段 –**该漏洞会影响 DNS 配置功能sub\_44E628。通过纵传递给 dns1 和 dns2 的值bs\_SetDNSInfo攻击者可以通过以 /goform/set\_AdvDns\_cfg 为目标来执行系统命令。
* **CVE-2025-45988：通过通用接口执行命令 –**最后一个漏洞存在于 sub\_44D18C 函数中，该函数调用 bs\_SetCmd — 一个通用的命令执行处理程序。攻击者提供的 cmd 值直接传递给 popen，从而允许执行任意 shell。

**是什么使这些漏洞变得危险？**

* 未经身份验证的访问：所有漏洞都不需要事先登录或会话令牌。
* 零点击潜力：通过远程访问，攻击者可以悄无声息地植入恶意软件、发起持续威胁或更改网络配置。
* 共享受影响的代码库：每个缺陷都针对相同的 goahead 二进制文件和关联的共享对象，从而放大了不同型号和固件版本的影响。

受影响的产品包括 BL-WR9000、BL-AC1900、BL-AC2100\_AZ3、BL-X10\_AC8、BL-X26\_AC8、BL-LTE300、BL-F1200\_AT1、BLAC450M\_AE4 和 BL-X26\_DA3，固件版本可追溯至 2023 年。

**缓解建议**

* **立即固件更新**：所有受影响的用户都应在最新固件版本可用时立即修补。
* **限制管理员面板访问**：确保路由器的管理界面只能从本地网络或通过安全的 VPN 连接访问。
* **启用输入过滤**：网络管理员应实施 Web 应用程序防火墙 （WAF） 和流量检查工具，以检测针对路由器端点的恶意负载。
* **监控异常**：查找可疑目录（例如 、 ）作为入侵迹象。`hacker``sub_44D9F4`

本文翻译自securityonline [原文链接](https://securityonline.info/critical-blink-router-flaws-cvss-9-8-allow-remote-root-code-execution-via-unauthenticated-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308486](/post/id/308486)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-blink-router-flaws-cvss-9-8-allow-remote-root-code-execution-via-unauthenticated-attacks/)

如若转载,请注明出处： <https://securityonline.info/critical-blink-router-flaws-cvss-9-8-allow-remote-root-code-execution-via-unauthenticated-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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