---
title: 深度隐藏：Python恶意软件藏身PNG伪装的RAR文件，向cvtres.exe 注入载荷
url: https://www.anquanke.com/post/id/313375
source: 安全客-有思想的安全新媒体
date: 2025-11-25
fetch_date: 2025-11-26T03:15:35.243963
---

# 深度隐藏：Python恶意软件藏身PNG伪装的RAR文件，向cvtres.exe 注入载荷

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

# 深度隐藏：Python恶意软件藏身PNG伪装的RAR文件，向cvtres.exe 注入载荷

阅读量**14234**

发布时间 : 2025-11-25 17:40:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/extreme-stealth-python-malware-hides-inside-png-disguised-rar-injects-payload-into-cvtres-exe/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

K7 Labs 研究人员发现了一种高度混淆的 Python 恶意软件，它使用 **多层编码**、**伪装的压缩包格式** 和 **隐蔽的进程注入** 技术，在受感染系统上建立持久的命令与控制（C2）通信。该活动经过精心设计，通过将看似合法的组件与深度嵌套的 payload 转换相结合，以逃避用户怀疑和传统安全控制。

### 攻击链解析

攻击链始于一个 PE 投放器，它在运行时解密嵌入的 payload，重建恶意批处理脚本（config.bat ）并写入磁盘。恶意软件遵循多步骤解压流程，最终执行 Python 代码。

K7 Labs 解释：“感染链始于包含运行时解密例程的 PE 投放器……通过 WriteFile 将重建的 payload 写入磁盘。”

批处理脚本随后下载一个看似无害的 PNG 文件——但这个“图像”实际上是伪装成 .png 扩展名的 **RAR 压缩包**：

“尽管下载的文件具有 .png 扩展名，但它实际上是一个 RAR 压缩包——这是一种简单且常用的技巧，因为用户和安全过滤器通常将 .png 文件视为无害。”

### 解压与伪装机制

解压后，恶意软件展现更多欺骗手段：

1. **AsusMouseDriver.sys** ：实为受密码保护的 RAR 压缩包
2. **Interput.json** ：运行时重命名为 Install.bat
3. **Inx**：合法的 WinRAR 辅助可执行文件，用于解压隐藏压缩包

解压完成后，脚本会构建一个伪造的 Windows 目录：

“名为 WindowsSecurityA 的目录现在包含：一个名为 ntoskrnl.exe 的文件（伪装成 Windows 内核文件，实为捆绑的 Python 运行时）……[以及] 主要的混淆 Python payload。”

### 多层解密与内存执行

加载器随后使用两个参数（dcconsbot 和 dcaat）执行这个伪造的 ntoskrnl.exe ，这些参数作为触发恶意软件 **多层去混淆序列** 的密钥，并直接传递给 Python 解释器。

K7 Labs 指出，实际恶意逻辑隐藏在多个解码和 decompression 层之下：“解压过程使用分层转换：Base64 → BZ2 → Zlib → marshal.loads 。”

生成的 65 MB 数据块中，大部分是无意义的填充内容：“只有末尾附近的一小部分包含有效的编组 Python 字节码。” 这个最终的 .pyc payload 直接在内存中执行。

### 进程注入与持久化

解压完成后，payload 立即向 **cvtres.exe （微软合法工具）** 执行进程注入。这为恶意软件带来两大优势：

1. **隐蔽性**：安全工具通常信任签名的微软二进制文件……使恶意活动看似来自合法进程。
2. **持久化**：即使加载器进程终止，被注入的进程仍保持活跃并继续 C2 通信。

### RAT 功能与网络特征

网络分析显示，运行时从攻击者服务器下载的注入式 .NET 模块，会与 C2 基础设施建立加密 TCP 通信。

K7 Labs 指出：“这种持续的双向加密流量模式是远程访问木马（RAT）的典型特征。”

RAT 功能包括：

1. 命令执行
2. 文件传输
3. 信息侦察
4. 持久化远程控制

K7 Labs 对整个操作总结如下：“该样本具有多项特征：多层编码、压缩包类型伪装，以及将 Python 运行时与看似签名/合法的可执行文件名捆绑。”

本文翻译自securityonline [原文链接](https://securityonline.info/extreme-stealth-python-malware-hides-inside-png-disguised-rar-injects-payload-into-cvtres-exe/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313375](/post/id/313375)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/extreme-stealth-python-malware-hides-inside-png-disguised-rar-injects-payload-into-cvtres-exe/)

如若转载,请注明出处： <https://securityonline.info/extreme-stealth-python-malware-hides-inside-png-disguised-rar-injects-payload-into-cvtres-exe/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **728**

* 粉丝
* **6**

### TA的文章

* ##### [微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役](/post/id/313348)

  2025-11-25 17:46:05
* ##### [美国CISA发布警告：Oracle身份管理器中的远程代码执行漏洞正遭攻击者积极利用](/post/id/313352)

  2025-11-25 17:45:43
* ##### [美国司法部诉谷歌广告技术反垄断案进入最终阶段，预计将迎来快速裁决](/post/id/313356)

  2025-11-25 17:44:55
* ##### [NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁](/post/id/313359)

  2025-11-25 17:44:33
* ##### [TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身](/post/id/313362)

  2025-11-25 17:43:43

### 相关文章

* ##### [微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役](/post/id/313348)

  2025-11-25 17:46:05
* ##### [美国CISA发布警告：Oracle身份管理器中的远程代码执行漏洞正遭攻击者积极利用](/post/id/313352)

  2025-11-25 17:45:43
* ##### [美国司法部诉谷歌广告技术反垄断案进入最终阶段，预计将迎来快速裁决](/post/id/313356)

  2025-11-25 17:44:55
* ##### [NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁](/post/id/313359)

  2025-11-25 17:44:33
* ##### [TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身](/post/id/313362)

  2025-11-25 17:43:43
* ##### [vLLM框架存在漏洞（CVE-2025-62164），通过恶意提示嵌入可导致远程代码执行](/post/id/313366)

  2025-11-25 17:43:02
* ##### [复杂WhatsApp蠕虫攻击通过伪造“阅后即焚”诱饵实施会话劫持，并投放Astaroth银行木马](/post/id/313369)

  2025-11-25 17:42:46

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