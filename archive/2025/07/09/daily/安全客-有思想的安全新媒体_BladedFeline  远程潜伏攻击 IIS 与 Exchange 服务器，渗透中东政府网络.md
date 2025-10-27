---
title: BladedFeline  远程潜伏攻击 IIS 与 Exchange 服务器，渗透中东政府网络
url: https://www.anquanke.com/post/id/309532
source: 安全客-有思想的安全新媒体
date: 2025-07-09
fetch_date: 2025-10-06T23:16:29.300361
---

# BladedFeline  远程潜伏攻击 IIS 与 Exchange 服务器，渗透中东政府网络

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

# BladedFeline 远程潜伏攻击 IIS 与 Exchange 服务器，渗透中东政府网络

阅读量**48345**

发布时间 : 2025-07-08 16:30:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/bladedfeline-malware-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

### **伊朗背景APT持续渗透中东政府网络**

BladedFeline 最早于 **2023年**因对库尔德外交官部署 **Shahmaran 后门**而被安全研究人员注意。但后续分析显示，其攻击活动至少从 **2017年**就已开始，最初目标为库尔德自治区政府（KRG）官员。

该组织名称反映其对地区政府目标的持续关注与伊朗国家战略之间的关联。

ESET 研究人员基于 **工具代码相似性**（与 OilRig 的 RDAT 后门高度重合）、**攻击目标重叠**、以及 **攻击基础设施一致性**，中等置信度认为 BladedFeline 是著名伊朗 APT 组织 OilRig（APT34 / Hazel Sandstorm）的子组。

### **Whisper：基于邮件的隐蔽后门通信机制**

Whisper 后门的最大特点是其 **非传统 C2 通信方式**——不通过常规网络协议，而是通过登录被攻陷的 **Exchange Webmail 账户**，利用 **邮件附件实现命令控制**。

> **恶意程序会设置收件箱规则自动处理含命令的邮件，执行后再通过加密附件将结果发回。**

整个通信过程涉及以下七个步骤：

1. 获取目标邮箱访问权限；
2. 设置自动处理规则；
3. 定期发送检查邮件；
4. 从附件中提取并解密攻击者下发的命令；
5. 执行命令（包括 PowerShell 脚本、文件传输、主机探测等）；
6. 加密执行结果；
7. 通过邮件附件返回结果。

该后门具备 **强持久性** 和 **极高隐蔽性**，对基于流量分析的检测机制构成挑战。

### **PrimeCache：伪装成IIS模块的被动后门**

PrimeCache 是一种以 **本地IIS模块形式实现的被动后门**，允许攻击者持续访问被控服务器，而无需主动发送流量指令。

> **它仅处理包含特定 Cookie 的 HTTP 请求，利用该机制进行“身份识别”。**

与传统后门一次性命令-响应方式不同，PrimeCache 采用 **参数分包 + 触发执行** 的分布式命令策略：

1. 攻击者首先以多个 HTTP 请求分别提交命令参数，缓存在服务器内存中；
2. 最后通过单独请求触发命令执行；
3. 利用 **RSA + AES 混合加密**保障通信安全；
4. 指令通过 Cookie 发送，结果嵌入 HTTP 响应体返回。

**此方式有效规避了异常流量检测规则，具备极强的规避能力。**

该模块支持：**远程命令执行、****文件上传与下载、****系统侦察与信息搜集。**

### **攻击时间线与受害者概况**

BladedFeline 的活动时间跨度覆盖 **2017至2024年**，显示出其攻击工具链不断演化。

早期使用简单的反弹 Shell，后期发展为复杂的邮件与 Web 后门，始终保持对多个受害者网络的持续控制。

> **受害目标包括：**库尔德自治区政府高层官员、伊拉克政府机构、乌兹别克斯坦某地区电信服务商攻击目标高度集中于外交与政府部门，表明其行动目的以**情报收集**为主，服务于**伊朗国家战略利益**。

### **趋势研判：APT攻击趋向合法基础设施隐藏C2**

此次行动体现出伊朗国家支持的网络攻击组织正在朝着 **更加隐蔽、结构复杂、通信手段合法化** 的方向演化。

特别是对 **Microsoft Exchange 的合法邮件功能用于 C2 通信** 的创新应用，使得传统检测手段难以察觉此类隐蔽通道。**这类以“合法外壳”包裹攻击内核的 APT 战术，已成为当前最具挑战性的威胁演进方向之一。**

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/bladedfeline-malware-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309532](/post/id/309532)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/bladedfeline-malware-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/bladedfeline-malware-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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