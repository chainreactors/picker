---
title: “NordDragonScan”窃密木马曝光：精准瞄准Windows用户，窃取凭据并横向扫描网络
url: https://www.anquanke.com/post/id/309614
source: 安全客-有思想的安全新媒体
date: 2025-07-10
fetch_date: 2025-10-06T23:16:56.715096
---

# “NordDragonScan”窃密木马曝光：精准瞄准Windows用户，窃取凭据并横向扫描网络

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

# “NordDragonScan”窃密木马曝光：精准瞄准Windows用户，窃取凭据并横向扫描网络

阅读量**53106**

发布时间 : 2025-07-09 14:22:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/norddragonscan-attacking-windows-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员近期揭露了一起高危网络攻击活动，攻击者通过名为 **“NordDragonScan”** 的高级信息窃取型木马（infostealer），专门针对 **Microsoft Windows 用户**展开攻击，目标包括浏览器数据、登录凭据以及敏感文档。

### **利用信任机制传播：HTA投递链精心伪装**

据 FortiGuard Labs 报告，攻击活动使用精密的 HTA（HTML Application）脚本投递机制，背后的基础设施已处于活跃运行状态。

攻击流程起始于短链接服务，诱导用户跳转至伪装成文件共享平台的恶意网站，随后自动触发下载名为乌克兰语文件名的 RAR 压缩包，制造“官方文件”假象。

压缩包内包含一个精心构造的 LNK 快捷方式文件，双击后会**调用 Windows 原生命令行工具 mshta.exe 执行嵌入的 HTA 脚本**，有效绕过多种安全检测机制。

该 HTA 脚本会将 **PowerShell.exe 复制到公共目录**，并伪装为“install.exe”以逃避杀软检测。

### **全面数据窃取：浏览器凭据、截图、文档一网打尽**

NordDragonScan 木马安装后，具备强大的信息收集能力，严重威胁用户隐私和数据安全：

* **截屏监控**：定期截取主机屏幕图像；
* **浏览器数据窃取**：完整提取 Chrome 和 Firefox 的浏览器配置，包括：保存的密码、浏览历史、Cookie 等敏感信息；
* **敏感文件扫描**：在桌面、文档、下载等关键目录中搜索特定文件类型（如 `.docx`、`.doc`、`.xls`、`.ovpn`、`.rdp`、`.txt`、`.pdf`）；
* **持久化机制**：通过修改注册表实现系统重启后仍可自动启动；
* **隐秘通信**：通过自定义 HTTP 头与 C2 服务器 **“kpuszkiev.com”** 建立加密 TLS 连接，用于数据回传和持续通信；
* **远程控制能力**：C2 同时作为心跳检查与指令响应节点，确保持续操控被感染主机。

### **横向扫描：从单点入侵扩展至内网风险**

更值得警惕的是，NordDragonScan 不仅危害单一主机，还具备 **内网扫描与横向渗透**能力。

它会自动识别主机网络适配器、计算 CIDR 网段，并对本地局域网内其他设备进行轻量级探测，尝试识别存在安全缺口的邻近主机，可能引发 **连锁式感染**。

### **安全建议：警惕压缩包与快捷方式文件**

安全专家建议：

* **谨慎处理来自不明来源的 .LNK 快捷方式和压缩包**；
* **部署邮件网关过滤机制**，阻断含恶意附件或钓鱼链接的邮件；
* **保持杀软、操作系统和终端防护软件的及时更新**；
* **加强用户安全意识培训**，重点识别“假文件共享”“冒充官方文档”等社交工程手法

NordDragonScan 代表了一种典型的 **“高级持续性威胁”（APT）** 风格窃密木马，其精巧的传播链条、绕过检测的手段以及强大的数据窃取与横向渗透能力，**对个人用户和企业网络均构成重大风险**。

当前威胁形势下，常态化的安全教育与端点防护已成为防御此类攻击的**关键基石**。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/norddragonscan-attacking-windows-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309614](/post/id/309614)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/norddragonscan-attacking-windows-users/)

如若转载,请注明出处： <https://cybersecuritynews.com/norddragonscan-attacking-windows-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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