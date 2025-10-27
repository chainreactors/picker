---
title: 研究人员揭露针对100多款戴尔笔记本中ControlVault3固件的ReVault攻击
url: https://www.anquanke.com/post/id/311070
source: 安全客-有思想的安全新媒体
date: 2025-08-12
fetch_date: 2025-10-07T00:16:36.548677
---

# 研究人员揭露针对100多款戴尔笔记本中ControlVault3固件的ReVault攻击

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

# 研究人员揭露针对100多款戴尔笔记本中ControlVault3固件的ReVault攻击

阅读量**70756**

发布时间 : 2025-08-11 17:23:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/08/researchers-reveal-revault-attack.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现，戴尔 ControlVault3 固件及其关联的 Windows API **存在多处安全漏洞**，攻击者可能利用这些漏洞绕过 Windows 登录验证、提取加密密钥，并在固件中植入无法检测的恶意程序，从而在重装操作系统后依然维持访问权限。

这些漏洞由 Cisco Talos 命名为 **ReVault**，受影响的包括 100 多款搭载博通 BCM5820X 系列芯片的戴尔笔记本。目前暂无证据表明这些漏洞已在野外被利用。

对于需要更高安全等级登录（如使用智能卡读卡器或近场通信 NFC 读卡器）的行业，ControlVault 设备通常是重要组成部分。ControlVault 是一种基于硬件的安全解决方案，可在固件内安全存储密码、生物识别模板和安全代码。

研究人员在美国 Black Hat 安全大会上介绍，这些漏洞可以**被“串联”利用**：攻击者在获得初始访问权限后，可提升权限、绕过身份验证控制，并在系统遭入侵后实现持久化，即使系统升级或重装操作系统也无法清除。

![]()

综合来看，这些漏洞为攻击者提供了一种强大的远程“事后”持久化访问手段，尤其适用于渗透高价值目标环境。已确认的漏洞包括：

* **CVE-2025-25050**（CVSS 评分：8.8）：`cv_upgrade_sensor_firmware` 功能存在越界写漏洞，可能导致越界写入
* **CVE-2025-25215**（CVSS 评分：8.8）：`cv_close` 功能存在任意释放漏洞，可能导致任意释放内存
* **CVE-2025-24922**（CVSS 评分：8.8）：`securebio_identify` 功能存在基于栈的缓冲区溢出漏洞，可能导致任意代码执行
* **CVE-2025-24311**（CVSS 评分：8.4）：`cv_send_blockdata` 功能存在越界读取漏洞，可能导致信息泄露
* **CVE-2025-24919**（CVSS 评分：8.1）：`cvhDecapsulateCmd` 功能存在不可信数据反序列化漏洞，可能导致任意代码执行

Cisco Talos 还指出，拥有笔记本物理访问权限的本地攻击者，可以拆开设备并**直接接触到统一安全中心（USH）板卡**，从而无需登录或获得全盘加密密码，就能利用上述任一漏洞发动攻击。

Cisco Talos 研究员 Philippe Laulheret 表示：“ReVault 攻击既可以作为一种**入侵后的持久化技术**，跨越 Windows 重装依然存在；也可以**在物理入侵时被利用**，用来绕过 Windows 登录，或让本地用户直接获得管理员/System 权限。”

为降低风险，研究人员建议用户：

**·** 尽快安装戴尔提供的补丁；

**·** 如果未使用指纹识别、智能卡读卡器、NFC 读卡器等外设，可关闭 ControlVault 服务；

**·** 在高风险环境中禁用指纹登录功能。

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/08/researchers-reveal-revault-attack.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311070](/post/id/311070)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/08/researchers-reveal-revault-attack.html)

如若转载,请注明出处： <https://thehackernews.com/2025/08/researchers-reveal-revault-attack.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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