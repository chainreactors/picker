---
title: 新型Linux恶意软件利用文件名武器化实现"隐形"攻击
url: https://www.anquanke.com/post/id/311438
source: 安全客-有思想的安全新媒体
date: 2025-08-26
fetch_date: 2025-10-07T00:18:04.705397
---

# 新型Linux恶意软件利用文件名武器化实现"隐形"攻击

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

# 新型Linux恶意软件利用文件名武器化实现"隐形"攻击

阅读量**45541**

发布时间 : 2025-08-25 17:47:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/a-new-linux-malware-hides-in-plain-sight-by-weaponizing-file-names/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Linux系统长期以来被视为安全堡垒——全球开发者、系统管理员和安全专家的首选平台。但根据Trellix高级研究中心的最新报告，攻击者正在利用其被忽视的弱点：操作系统和shell脚本处理文件名的机制。

正如研究人员所言：”攻击者不再单纯利用软件漏洞，而是通过武器化系统行为、脚本模式甚至文件名等文件元数据，以隐蔽且出人意料的方式突破系统防线。”

攻击活动始于伪装成美容产品调查邀请的垃圾邮件，以小额奖金诱骗收件人。邮件包含一个.rar压缩包（yy.rar），其中的**文件名本身即携带恶意载荷**。

Trellix解释道：”有效载荷并非隐藏于文件内容或宏中，而是直接编码在文件名内。”解压后文件看似普通文档，实则嵌入了Bash命令。当系统管理员或脚本使用`eval "echo $f"`或`ls | while read f; do eval "echo $f"; done`等命令处理文件名时，隐藏的有效载荷将自动执行——无需用户双击或主动运行文件。

![]()

该恶意软件通过精密的四阶段攻击链实现渗透：

1. **武器化文件名** – 恶意文件名内嵌Base64解码命令并通过管道传输至Bash，无声触发攻击
2. **下载器脚本** – 第二阶段Bash脚本识别系统架构（x86/x64/ARM/ARM64），从攻击者服务器获取定制ELF二进制文件
3. **内存加载器** – ELF二进制文件在内存中解密XOR加密载荷（密钥：0x99），以伪装内核线程（[kworker/0:2]）形式启动
4. **最终载荷（VShell）** – 提供远程访问、文件操作、进程管理、端口转发和加密C2通信的全功能后门

这种隐蔽攻击方式使恶意软件实现**无文件化运作**，直接在内存中运行的同时伪装成合法系统进程。

该攻击链的隐蔽性体现在：

1. **无需可执行权限** – 仅解压或在脚本中列出压缩包内容即可触发感染
2. **跨平台覆盖** – 支持x86/x64/ARM架构，针对服务器、IoT设备和云环境
3. **纯内存执行** – 无磁盘痕迹大幅增加检测难度
4. **备用持久化** – 下载器脚本尝试多个可写路径并使用nohup确保执行

通过将基于文件名的注入与Bash脚本弱点结合，攻击者成功绕过传统安全防护。杀毒引擎很少扫描文件名，静态分析工具对畸形压缩包头也无能为力。

采用Go语言编写且被中国APT组织广泛使用的VShell恶意软件具备强大远程控制与间谍功能，包括：

1. 反向shell访问
2. 文件上传/下载/删除
3. 进程管理
4. TCP/UDP端口转发
5. 内存隐蔽执行
6. 自定义加密C2通信

Trellix警告称：”此分析凸显了Linux恶意软件投递的危险进化——隐藏在RAR压缩包中的普通文件名竟可被武器化执行任意命令。”

VShell攻击活动表明，攻击者正将低复杂度技术转化为高影响威胁。通过利用Linux宽松的执行环境和被忽视的脚本行为，威胁分子甚至能渗透加固系统。

研究人员总结道：”攻击者正日益利用脚本环境、nohup等系统工具和文件名解析行为来绕过传统安全防护层。”

本文翻译自securityonline [原文链接](https://securityonline.info/a-new-linux-malware-hides-in-plain-sight-by-weaponizing-file-names/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311438](/post/id/311438)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/a-new-linux-malware-hides-in-plain-sight-by-weaponizing-file-names/)

如若转载,请注明出处： <https://securityonline.info/a-new-linux-malware-hides-in-plain-sight-by-weaponizing-file-names/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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