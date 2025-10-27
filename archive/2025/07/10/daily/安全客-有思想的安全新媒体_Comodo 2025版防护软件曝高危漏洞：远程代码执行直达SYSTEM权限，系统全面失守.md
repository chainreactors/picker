---
title: Comodo 2025版防护软件曝高危漏洞：远程代码执行直达SYSTEM权限，系统全面失守
url: https://www.anquanke.com/post/id/309600
source: 安全客-有思想的安全新媒体
date: 2025-07-10
fetch_date: 2025-10-06T23:16:51.370470
---

# Comodo 2025版防护软件曝高危漏洞：远程代码执行直达SYSTEM权限，系统全面失守

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

# Comodo 2025版防护软件曝高危漏洞：远程代码执行直达SYSTEM权限，系统全面失守

阅读量**55308**

发布时间 : 2025-07-09 14:24:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/comodo-internet-security-2025-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近日，安全研究人员披露**Comodo Internet Security Premium 2025（版本 12.3.4.8162）** 存在**多个关键级别安全漏洞**，攻击者可通过伪造更新包实现**远程代码执行（RCE）并获取SYSTEM权限**，最终完全控制受害者系统。

本次漏洞已被归为统一编号 **CVE-2025-7095**，由 **FPT IS Security** 团队发现。

### **关键风险概览：**

1. **CVE-2025-7095**：远程攻击者可通过软件更新机制实现**SYSTEM权限的代码执行**。
2. **证书校验不当（CWE-295）**：攻击者可利用DNS欺骗将更新请求重定向至恶意服务器。
3. **更新清单伪造（CWE-345）**：可嵌入恶意命令，执行持久化后门并窃取凭据。
4. **路径遍历漏洞（CWE-22）**：恶意文件可被写入Windows启动目录，实现跨重启持久驻留。

### **漏洞细节解析：**

**证书校验缺陷（CWE-295）**

Comodo 虽然通过 HTTPS 连接 `https://download.comodo.com/` 进行更新，但其并未正确校验证书有效性，导致攻击者可通过 **DNS Spoofing** 重定向更新流量至恶意服务器。

研究人员使用 **Scapy** 工具构造了Python脚本完成DNS欺骗。
攻击流程包括：

* 拦截目标机器的 DNS 请求；
* 将 `download.comodo.com` 定向至攻击者服务器（如 `192.168.58.192`）；
* 利用如 `sudo arpspoof -i eth0 -t 10.10.14.4 -r 10.10.14.1` 实现网络中间人定位；
* 伪造更新响应，投送恶意代码。

**更新清单验证不足（CWE-345）**

Comodo 的更新系统会处理名为 `cis_update_x64.xml` 的清单文件，该文件中 `<exec>` 标签的命令将以 **SYSTEM权限** 被执行。

攻击者可通过 PowerShell 语句植入 **Metasploit Payload**，并使用 `hashdump` 与 `mimikatz` 等模块提取系统中的**敏感账号密码**。

**路径遍历漏洞（CWE-22）**

Comodo 的文件更新机制未正确处理路径参数，攻击者可使用 `../../../` 等目录穿越技巧，将**恶意脚本写入Windows启动目录**（如 `Start Menu\Programs\Startup\`）。

研究人员在此路径投放Base64编码的反弹Shell脚本，确保**每次系统启动时自动执行**。攻击者初期获得用户权限后，可进一步利用 UAC绕过工具（如 `bypassuac_sdclt` 模块）提升至SYSTEM权限。

### **风险评级与影响**

| 风险项 | 内容说明 |
| --- | --- |
| 影响产品 | Comodo Internet Security Premium v12.3.4.8162 |
| 核心危害 | 远程代码执行（RCE）+ SYSTEM权限控制 |
| 漏洞评分 | CVSS v4.0 分数：6.3（中危，但实际危害极高） |
| 利用前提 | 攻击者需具备网络位置控制能力（如DNS欺骗） |

尽管评分为中等，但由于该漏洞链一旦被利用可实现**完整系统接管**，危害程度实质已达高危级别。

### **官方响应与安全建议**

截至目前，Comodo 官方**尚未对漏洞披露作出回应**。
在补丁发布前，建议用户采取以下防护措施：

* **在网络层面封锁**对 `download.comodo.com` 的DNS可疑重定向；
* **加强网络边界监测**，尤其关注更新流量中的异常请求；
* 禁用或限制自动更新功能，等待官方确认补丁；
* 使用IPS/IDS监控DNS和ARP欺骗行为。

该漏洞再次提醒用户，**安全软件自身更新机制的完整性与信任链构建**，同样是企业防护体系中不可忽视的一环。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/comodo-internet-security-2025-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309600](/post/id/309600)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/comodo-internet-security-2025-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/comodo-internet-security-2025-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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