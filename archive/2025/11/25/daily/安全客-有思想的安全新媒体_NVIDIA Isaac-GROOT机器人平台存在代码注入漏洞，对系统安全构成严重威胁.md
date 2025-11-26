---
title: NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁
url: https://www.anquanke.com/post/id/313359
source: 安全客-有思想的安全新媒体
date: 2025-11-25
fetch_date: 2025-11-26T03:15:27.615061
---

# NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁

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

# NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁

阅读量**23244**

发布时间 : 2025-11-25 17:44:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/code-injection-flaws-threaten-nvidias-isaac-groot-robotics-platform/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

英伟达（NVIDIA）已发布安全更新，修复其 **NVIDIA Isaac-GROOT 软件** 中的两个 **高严重性漏洞**。Isaac-GROOT 是用于通用人形机器人推理与技能的开放基础模型，这一安全缺陷引发了快速发展的机器人行业中开发者和研究人员的关注。

这两个漏洞编号为 **CVE-2025-33183** 和 **CVE-2025-33184**，均源于软件 **Python 组件** 中的缺陷。

两者均被评为高严重性，基础评分（Base Score）均为 **7.8**。根本原因是 Python 组件中存在一个弱点，“攻击者可利用该弱点造成代码注入问题”。

成功利用这些漏洞可能导致严重后果，包括：

1. 代码执行
2. 权限提升
3. 信息泄露
4. 数据篡改

公告指出，两个 CVE 的“成功利用均可能导致代码执行、权限提升、信息泄露和数据篡改”。

漏洞影响 **所有平台上的 NVIDIA Isaac-GROOT N1.5**，具体受影响版本为“**所有未包含代码提交 7f53666 的版本**”。

英伟达敦促所有使用 Isaac-GROOT 平台的用户和开发者 **立即更新软件**。修复包含在“**所有包含代码提交 7f53666 的代码分支**”中。鉴于存在未授权代码执行和权限提升风险，打补丁对于保障正在进行的机器人开发和部署项目的安全至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/code-injection-flaws-threaten-nvidias-isaac-groot-robotics-platform/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313359](/post/id/313359)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/code-injection-flaws-threaten-nvidias-isaac-groot-robotics-platform/)

如若转载,请注明出处： <https://securityonline.info/code-injection-flaws-threaten-nvidias-isaac-groot-robotics-platform/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身](/post/id/313362)

  2025-11-25 17:43:43
* ##### [vLLM框架存在漏洞（CVE-2025-62164），通过恶意提示嵌入可导致远程代码执行](/post/id/313366)

  2025-11-25 17:43:02
* ##### [复杂WhatsApp蠕虫攻击通过伪造“阅后即焚”诱饵实施会话劫持，并投放Astaroth银行木马](/post/id/313369)

  2025-11-25 17:42:46
* ##### [PyPI拼写劫持投递多层Python木马，利用异或加密绕过扫描器](/post/id/313372)

  2025-11-25 17:41:58

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