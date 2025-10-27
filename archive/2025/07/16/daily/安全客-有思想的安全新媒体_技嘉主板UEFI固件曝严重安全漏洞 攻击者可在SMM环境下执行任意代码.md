---
title: 技嘉主板UEFI固件曝严重安全漏洞 攻击者可在SMM环境下执行任意代码
url: https://www.anquanke.com/post/id/310068
source: 安全客-有思想的安全新媒体
date: 2025-07-16
fetch_date: 2025-10-06T23:39:08.791992
---

# 技嘉主板UEFI固件曝严重安全漏洞 攻击者可在SMM环境下执行任意代码

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

# 技嘉主板UEFI固件曝严重安全漏洞 攻击者可在SMM环境下执行任意代码

阅读量**59823**

发布时间 : 2025-07-15 18:18:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/gigabyte-uefi-firmware-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近日，美国软件工程研究院（Software Engineering Institute, SEI）协调中心 CERT/CC 于 2025 年 7 月 11 日发布通告称，在技嘉（Gigabyte）多个系统使用的 **UEFI 固件中发现严重安全漏洞**，攻击者可利用这些漏洞在系统管理模式（System Management Mode，简称 SMM）中执行任意代码。**SMM 是现代处理器中权限最高的执行环境之一**，若遭利用，将对系统安全构成严重威胁。

这些漏洞可**绕过包括 Secure Boot（安全启动）和 Intel BootGuard 在内的核心安全防护机制**，允许持久化的**固件级恶意软件**植入，同时绕过传统杀毒软件的检测，具备**极高隐蔽性**。

##### 主要风险摘要：

1. 技嘉 UEFI 固件中的**四个 CVE 漏洞**可被利用，在特权级别极高的 SMM 环境中执行任意代码；
2. 漏洞利用可**绕过 Secure Boot 与 Intel BootGuard**，实现固件层级的**持久化**攻击，传统杀毒工具**无法检测**；
3. 技嘉系统在**启动、休眠状态或正常运行中**，若存在本地或远程管理员访问权限，均可能被利用；
4. 建议用户**立即访问技嘉官网**，下载安装最新 UEFI 固件**更新补丁**。

##### 漏洞技术细节

本次披露的漏洞主要源于技嘉 UEFI 固件中**系统管理中断处理程序（SMI handlers）**在**数据校验**方面存在缺陷。

四个漏洞已被分配以下 CVE 编号：**CVE-2025-7029、CVE-2025-7028、CVE-2025-7027 和 CVE-2025-7026**。

这些漏洞主要与固件在处理 SMI 请求时对寄存器和指针的使用缺乏有效验证有关，攻击者可利用这些缺陷对**系统管理内存（SMRAM）**进行任意写入。

* **• CVE-2025-7029：**攻击者可通过未检查的 RBX 寄存器控制 OcHeader 和 OcData 指针，在电源和热管理逻辑中实现任意 SMRAM 写入；
  **• CVE-2025-7028：**RBX 和 RCX 寄存器导出的函数指针结构未校验，攻击者可控制 ReadFlash、WriteFlash、EraseFlash 和 GetFlashInfo 等关键闪存操作；
  **• CVE-2025-7027：**存在双重指针解引用漏洞，未校验的 NVRAM 变量 SetupXtuBufferAddress 可被利用执行任意 SMRAM 写入；
  **• CVE-2025-7026：**RBX 寄存器未作检查即作为指针在 CommandRcx0 函数中使用，攻击者可将数据写入指定的 SMRAM 内存地址。

根据 CERT/CC 报告，这些漏洞使**具备本地或远程管理员权限的攻击者**可在 Ring-2 权限级别下执行代码，绕过操作系统的**所有防护机制**。

由于 SMM 位于操作系统内核之下，该类攻击具有**极强的隐蔽性**，可在系统重启后依然存在，传统终端防护工具无法检测。

漏洞可通过**多种路径触发**，包括操作系统内部调用 SMI、系统启动初期、休眠唤醒过程，甚至系统恢复模式等关键时间点，攻击者可在操作系统加载前获得控制权。

攻击成功后，攻击者可关闭关键的 UEFI 安全机制，**在固件层面植入恶意程序**，建立长期隐蔽控制路径。

研究机构 Binarly 团队已负责任地将漏洞报告提交 CERT/CC，并获得技嘉 PSIRT（产品安全响应团队）的积极配合。

##### **漏洞详情表（CVE 评级）**

|  |  |  |  |
| --- | --- | --- | --- |
| CVE编号 | 漏洞描述 | CVSS 3.1分数 | 严重等级 |
| CVE-2025-7029 | 未检查的RBX寄存器导致通过OcHeader/OcData指针写入 SMRAM | 9.8 | Critical |
| CVE-2025-7028 | 函数指针结构未校验，攻击者可控制关键闪存读写操作 | 9.8 | Critical |
| CVE-2025-7027 | 双重指针解引用，SetupXtuBufferAddress可导致任意SMRAM写入 | 9.8 | Critical |
| CVE-2025-7026 | CommandRcx0函数中RBX寄存器未校验，可写入攻击者指定地址 | 9.8 | Critical |

技嘉官方已发布针对上述漏洞的 UEFI 固件更新，强烈建议用户**尽快访问技嘉支持网站，确认自身设备是否受影响**，并及时下载**最新固件版本**进行升级。

据原始固件供应商 AMI 表示，尽管此前已通过私下渠道披露相关漏洞，但**部分 OEM 固件版本中仍存在相关问题**。

安全专家提醒，由于此类漏洞涉及固件层及供应链安全，可能影响的不仅限于技嘉品牌，**其他 PC 原始设备制造商（OEM）亦有可能受到波及**。建议广大用户**密切关注相关安全通告，定期检查并更新系统固件**，切实保障设备安全。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/gigabyte-uefi-firmware-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310068](/post/id/310068)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/gigabyte-uefi-firmware-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/gigabyte-uefi-firmware-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

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