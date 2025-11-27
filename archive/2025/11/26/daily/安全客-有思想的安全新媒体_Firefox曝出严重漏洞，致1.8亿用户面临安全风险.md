---
title: Firefox曝出严重漏洞，致1.8亿用户面临安全风险
url: https://www.anquanke.com/post/id/313385
source: 安全客-有思想的安全新媒体
date: 2025-11-26
fetch_date: 2025-11-27T03:10:38.865466
---

# Firefox曝出严重漏洞，致1.8亿用户面临安全风险

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

# Firefox曝出严重漏洞，致1.8亿用户面临安全风险

阅读量**23869**

发布时间 : 2025-11-26 18:30:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ken Underhill，文章来源：techrepublic

原文地址：<https://www.techrepublic.com/article/news-firefox-bug-180m-users-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Firefox 中一个 **隐蔽但危险的内存漏洞** 在被安全研究人员发现前已静默存在六个月，影响超过 1.8 亿用户。

该漏洞允许攻击者通过 **恶意构造的 WebAssembly 负载** 破坏内存，甚至可能执行任意代码。

“Aisle 的自主 AI 系统在我们对 WebAssembly 安全的深入研究中发现了这个微妙的边界条件漏洞，为约 1.8 亿 Firefox 用户揭示了重大的内存安全风险，”AISLE 创始人兼首席科学家 Stanislav Fort 在博客文章中表示。

他补充道：“Mozilla 迅速采取行动部署了修复程序。现代浏览器是现存最安全、设计最严谨的平台之一，这一发现凸显了持续的、AI 驱动的安全研究对于保障全球用户安全的重要性。”

### 暴露 Firefox 用户的隐藏代码错误

该漏洞（CVE-2025-13016）的核心是 Firefox WebAssembly 垃圾回收（GC）实现中的一个 **微妙指针算术错误**，具体位于 `StableWasmArrayObjectElements` 类中，其中不匹配的指针类型导致内联数组数据的错误复制。

易受攻击的代码使用字节寻址指针（`uint8_t*`）来确定要复制的数据量，但将数据复制到类型为 `uint16_t` 的缓冲区中。当模板为 16 位值实例化时，`std::copy()` 将基于字节的范围解释为类型化元素的计数，而非字节数。

结果，一个旨在容纳 N 个 16 位元素的缓冲区接收了 2N 个元素，导致 **堆栈内存溢出** 并破坏相邻数据结构。第二个缺陷加剧了问题：复制操作没有从正确的内存位置读取数据。

代码没有使用数组数据区域的专用指针，而是从 `inlineStorage()` 中提取数据，该位置以内部对象元数据开头。

这意味着复制到缓冲区的前几个字节根本不是数组内容，而是 WebAssembly 对象本身的结构信息。这引入了额外的不可预测性，并增加了在利用过程中将损坏内存武器化的可能性。

### 攻击者利用此 Firefox 漏洞所需的条件

并非 Firefox 中的每条执行路径都会触及有缺陷的例程，这也是该漏洞长期未被发现的原因。

该问题仅在 Firefox 回退到较慢的、支持 GC 的路径处理 WebAssembly 数组时发生——特别是在将这些数组转换为字符串的过程中。

在典型序列中，WebAssembly 代码首先操作一个数组，例如 `char16_t` 数组。Firefox 然后尝试使用旨在避免垃圾回收的快速路径操作将该数组转换为字符串。然而，当某些条件（最常见的是内存压力）导致该快速路径失败时，浏览器会切换到允许 GC 的回退例程。

正是在这个回退过程中，Firefox 调用了易受攻击的 `StableWasmArrayObjectElements` 构造函数，该构造函数执行有缺陷的复制操作，最终导致堆栈溢出，破坏相邻内存。

在实际攻击场景中，攻击者可以故意构造恶意 WebAssembly 模块来操纵此序列以利于他们。

通过创建特定大小的数组、故意使浏览器陷入内存压力以强制垃圾回收，并反复触发数组到字符串的转换过程，攻击者可以可靠地将 Firefox 推入易受攻击的回退路径。

这创建了一个受控环境，在其中，由此产生的内存损坏可以被定向到堆栈上的选定目标。

本文翻译自techrepublic [原文链接](https://www.techrepublic.com/article/news-firefox-bug-180m-users-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313385](/post/id/313385)

安全KER - 有思想的安全新媒体

本文转载自: [techrepublic](https://www.techrepublic.com/article/news-firefox-bug-180m-users-exposed/)

如若转载,请注明出处： <https://www.techrepublic.com/article/news-firefox-bug-180m-users-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **740**

* 粉丝
* **6**

### TA的文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44

### 相关文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44
* ##### [高级威胁组织ToddyCat升级攻击工具库，新型工具专门窃取Outlook邮件并劫持Microsoft 365访问令牌](/post/id/313434)

  2025-11-26 18:27:40
* ##### [威胁行为体利用Blender基金会官方文件作为载体，传播臭名昭著的StealC V2信息窃取木马](/post/id/313427)

  2025-11-26 18:26:53
* ##### [供应链攻击“Sha1-Hulud”已波及超800个npm软件包与数千个GitHub代码库](/post/id/313439)

  2025-11-26 18:26:16

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