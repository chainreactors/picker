---
title: PyPI拼写劫持投递多层Python木马，利用异或加密绕过扫描器
url: https://www.anquanke.com/post/id/313372
source: 安全客-有思想的安全新媒体
date: 2025-11-25
fetch_date: 2025-11-26T03:15:33.481807
---

# PyPI拼写劫持投递多层Python木马，利用异或加密绕过扫描器

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

# PyPI拼写劫持投递多层Python木马，利用异或加密绕过扫描器

阅读量**14054**

发布时间 : 2025-11-25 17:41:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pypi-typosquat-delivers-multi-layer-python-rat-bypassing-scanners-with-xor-encryption/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

HelixGuard 研究人员发现了一个上传到 PyPI 的恶意 Python 包，它伪装成广泛使用的“pyspellchecker”库——这次隐藏了一个多层加密后门，旨在为攻击者提供远程执行能力。该包名为 spellcheckers，已经下载超过 950 次，扩大了一个与假招聘人员社会工程攻击有关的威胁活动，目标是加密货币持有者。

恶意包试图通过复制 pyspellchecker（一个合法包，拥有超过 1800 万次下载）的名称来融入 Python 生态系统。但其看似无害的功能之下隐藏着一个狡猾的、多阶段的远程访问后门。

根据报告，“该组件伪装成一个拼写检查工具，实际上隐藏了一个多层加密后门。”

HelixGuard 强调了几个为逃避检测而设计的特性：

1. **隐蔽性**：恶意代码隐藏在功能模块中
2. Base64 编码的索引文件，以绕过静态检测
3. 自定义的 XOR 加密网络协议
4. 双层解密和异常抑制

感染始于 ma\_IN.index ，这是一个 Base64 编码的文件，在导入时自动执行。

分析详细描述了这种行为：“恶意代码首先通过一个 Base64 编码的隐藏索引文件（ma\_IN.index ）执行，触发初始恶意行为。”

解码后，payload 会连接到攻击者控制的 C2 服务器（dothebest.store ），并下载第二阶段恶意代码。“第一阶段 payload 连接到攻击者控制的 C2 服务器（dothebest.store ）并下载第二阶段恶意代码。”

解码后的第一阶段代码使用 Python 的 subprocess.Popen() 在后台执行恶意 Python 指令——对用户来说完全无声无息。

第二阶段 payload 显著更先进，具有以下功能：

1. 操作系统指纹识别
2. 计算机名称收集
3. 自定义数据包构建
4. XOR 加密的 C2 通信
5. 持续命令轮询

HelixGuard 写道：“第二阶段 payload 解密并执行一个远程访问木马（RAT）。该 RAT 可以接收远程命令并通过 exec() 执行攻击者控制的 Python 代码，从而对受害者的主机实现完全远程控制。”

与 C2 端点保持持久连接：

1. dothebest.store/allow/inform.php
2. dothebest.store/refresh.php

解密的 Python 后门能够接收各种命令，通过自定义协议进行编码。当 C2 发出命令 ID 1001 时，恶意软件直接执行远程 Python payload：“如果 nCMDID == 1001: exec(szCode)”，从而执行任意命令。

恶意软件使用多个加密例程：

1. 使用 16 字节密钥的 XOR
2. 使用常数密钥 123 的 XOR 转换
3. 命令数据包的 Base64 包装
4. 基于 Unicode 的数据包重新编码

这些层次有意设计为绕过静态扫描并复杂化分析。正如 HelixGuard 所描述的，“使用 XOR 加密的网络通信和自定义协议格式来增加隐蔽性。”

报告直接将这次 PyPI 供应链攻击与先前的社会工程活动联系起来。

HelixGuard 指出，“C2 地址……与黑客之前冒充招聘人员进行社会工程攻击时使用的地址相匹配。”

这些早期攻击通过伪装成招聘人员提供高薪工作来针对用户的加密货币账户——在 2024-2025 年变得越来越常见。

新的 PyPI 基于分发模型允许相同的威胁者悄悄感染不知情安装恶意库的开发人员和工程师。

本文翻译自securityonline [原文链接](https://securityonline.info/pypi-typosquat-delivers-multi-layer-python-rat-bypassing-scanners-with-xor-encryption/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313372](/post/id/313372)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pypi-typosquat-delivers-multi-layer-python-rat-bypassing-scanners-with-xor-encryption/)

如若转载,请注明出处： <https://securityonline.info/pypi-typosquat-delivers-multi-layer-python-rat-bypassing-scanners-with-xor-encryption/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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