---
title: PyPI遭遇攻击：新型恶意软件“SilentSync”窃取凭证
url: https://www.anquanke.com/post/id/312305
source: 安全客-有思想的安全新媒体
date: 2025-09-23
fetch_date: 2025-10-02T20:30:59.735240
---

# PyPI遭遇攻击：新型恶意软件“SilentSync”窃取凭证

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

# PyPI遭遇攻击：新型恶意软件“SilentSync”窃取凭证

阅读量**58611**

发布时间 : 2025-09-22 18:10:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pypi-under-attack-new-malware-silentsync-is-stealing-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Zscaler ThreatLabz发现Python Package Index（PyPI）再次遭遇供应链攻击。2025年8月，研究人员识别出两个恶意包——sisaws和secmeasure，它们伪装成合法库，实则分发名为**SilentSync**的Python远程访问木马（RAT）。

ThreatLabz解释：“2025年7月已发现名为termncolor的恶意Python包。几周后的8月4日，我们又发现了sisaws和secmeasure两个恶意包。”这两个包由同一攻击者发布，均通过PyPI传播。

其中，sisaws模仿阿根廷官方医疗集成包sisa，secmeasure则伪装成安全工具。两者均包含隐藏函数，调用时会从Pastebin下载并执行SilentSync。

### **SilentSync功能：多平台窃密与持久化**

据Zscaler分析，“SilentSync具备远程命令执行、文件窃取和屏幕捕获能力，还会提取Web浏览器数据，包括Chrome、Brave、Edge和Firefox的凭证、历史记录、自动填充数据及Cookie。”

![]()

SilentSync支持**跨平台持久化**（尽管当前恶意PyPI包仅感染Windows系统）：

1. **Windows**：创建注册表项实现开机自启；
2. **Linux**：使用crontab @reboot指令；
3. **macOS**：利用LaunchAgents。

该RAT通过HTTP与命令控制（C2）服务器通信，采用**定期心跳和任务轮询**机制。

### **核心命令与数据窃取流程**

支持的命令包括：

1. **`cmd`：执行任意shell命令；**
2. **`get`：窃取文件或整个目录（先压缩为ZIP再上传）；**
3. **`screenshot`：捕获桌面截图；**
4. **`browserdata`：窃取浏览器敏感数据。**

### **恶意包伪装技巧**

sisaws包精准模仿阿根廷医疗API集成功能。ThreatLabz报告：“sisaws表面上模拟合法模块（puco和renaper）的行为……乍看之下，它像是对接阿根廷医疗服务的合法Python库。”

但其\_\_init\_\_.py文件包含恶意函数`gen_token`：当提供硬编码令牌时，会返回伪造的类API响应，同时将十六进制字符串解码为curl命令，用于获取并执行SilentSync。

secmeasure包则伪装成简单的字符串清理库，提供`strip_whitespace`和`escape_html`等看似合法的函数。但ThreatLabz指出：“与sisaws类似，secmeasure的初始化脚本包含名为`sanitize_input`的恶意函数，调用时会执行与sisaws相同的十六进制编码curl命令，分发SilentSync RAT。”

本文翻译自securityonline [原文链接](https://securityonline.info/pypi-under-attack-new-malware-silentsync-is-stealing-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312305](/post/id/312305)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pypi-under-attack-new-malware-silentsync-is-stealing-credentials/)

如若转载,请注明出处： <https://securityonline.info/pypi-under-attack-new-malware-silentsync-is-stealing-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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