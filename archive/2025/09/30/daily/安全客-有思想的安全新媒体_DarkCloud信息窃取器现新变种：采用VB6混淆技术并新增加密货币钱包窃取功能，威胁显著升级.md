---
title: DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级
url: https://www.anquanke.com/post/id/312435
source: 安全客-有思想的安全新媒体
date: 2025-09-30
fetch_date: 2025-10-02T12:03:38.999648
---

# DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级

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

# DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级

阅读量**44968**

|评论**1**

发布时间 : 2025-09-29 18:02:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/darkcloud-stealer-evolves-new-vb6-obfuscation-and-crypto-wallet-theft-make-malware-more-dangerous-than-ever/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Sentire威胁响应团队（TRU）发现一场针对制造业客户的鱼叉式钓鱼活动，试图投递**DarkCloud信息窃取恶意软件**。诱饵以银行业务为主题，包含恶意ZIP归档文件，发送至公司Zendesk支持邮箱，伪装成合法财务 correspondence。

攻击者使用了极具说服力的社会工程学手段。TRU表示：“钓鱼诱饵由procure@bmuxitq[.]shop发送，主题为‘Swift Message MT103 Addiko Bank ad: FT2521935SVT’，邮件正文设计成看似合法的财务 correspondence。”附件中包含**DarkCloud 3.2版本**，伪装成Swift交易文件。

![]()

DarkCloud曾在现已关闭的XSS.is 论坛上售卖，此后经历了重大开发。报告指出：“DarkCloud最初基于.NET构建，现已多次更新，包括使用VB6完全重写加载器、字符串加密和规避技术升级。”

最新版本（4.2）采用**VB6驱动的凯撒密码**进行字符串加密，增加了分析难度。研究人员需从msvbvm60.dll 中逆向工程VB6的随机数生成器，才能解密存储的字符串。

DarkCloud旨在跨多个类别最大化窃取数据：

1. **凭证与财务数据**：浏览器存储的密码、Cookie、信用卡信息、FTP凭证和邮件客户端数据；
2. **文件窃取**：从桌面、文档、收藏夹等目录抓取.txt、.docx、.pdf、.xls[x]文件；
3. **加密货币钱包**：针对Electrum、Exodus、Zcash、Atomic、Guarda和MetaMask等钱包。报告强调：“已观察到DarkCloud针对Chrome和Edge中的MetaMask目录。”
4. **系统侦察**：通过WMI查询收集操作系统详情、用户名和硬件信息。

DarkCloud集成了**广泛的沙箱和虚拟机（VM）检测**。TRU详细说明：“如果运行的进程不超过50个，检测将失败……变体通过WMI查询系统型号，并与VMware、VirtualBox和微软虚拟环境进行比对。”它还会检查Wireshark、Procmon、IDA Pro、Joe Sandbox等分析工具的特征。

此外，恶意软件会检测其可执行文件名是否完全由十六进制字符组成——这是自动化沙箱测试的典型特征。

窃取的数据通过多种渠道渗出：

1. **SMTP**：“DarkCloud将窃取的Cookie和其他数据以JSON格式作为multipart/mixed消息发送……最近已更新为支持SSL加密的SMTP。”
2. **Telegram**：使用窃取的机器人令牌渗出凭证和文件；
3. **FTP**：通过明文FTP上传浏览器Cookie和文件；
4. **Web面板**：发送至攻击者使用的PHP控制面板。

eSentire捕获的PCAP文件显示，数据被渗出至攻击者控制的邮件服务器和Telegram端点。

目前，DarkCloud通过darkcloud.onlinewebshop[.]net 和Telegram账号@BluCoder进行销售。尽管被宣传为“密码恢复工具”，但网站列出的恶意功能包括击键记录、剪贴板窃取和加密货币剪贴劫持。

DarkCloud体现了信息窃取恶意软件的**持续专业化**。通过结合新型VB6混淆、多渠道渗出和反分析技术，它不断进化为持久威胁。鉴于钓鱼活动仍在活跃，防御者必须加强邮件安全、端点检测，并监控SMTP/Telegram出站流量，以尽早发现入侵。

本文翻译自securityonline [原文链接](https://securityonline.info/darkcloud-stealer-evolves-new-vb6-obfuscation-and-crypto-wallet-theft-make-malware-more-dangerous-than-ever/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312435](/post/id/312435)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/darkcloud-stealer-evolves-new-vb6-obfuscation-and-crypto-wallet-theft-make-malware-more-dangerous-than-ever/)

如若转载,请注明出处： <https://securityonline.info/darkcloud-stealer-evolves-new-vb6-obfuscation-and-crypto-wallet-theft-make-malware-more-dangerous-than-ever/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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