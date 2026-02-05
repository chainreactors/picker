---
title: 微软新版Windows 11更新悄然收紧存储设置权限
url: https://www.anquanke.com/post/id/314713
source: 安全客-有思想的安全新媒体
date: 2026-02-04
fetch_date: 2026-02-05T04:07:44.940968
---

# 微软新版Windows 11更新悄然收紧存储设置权限

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

# 微软新版Windows 11更新悄然收紧存储设置权限

阅读量**28425**

发布时间 : 2026-02-04 11:25:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/admins-only-microsofts-new-windows-11-update-quietly-locks-down-storage-settings/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

上周，微软面向 Windows 11 24H2 和 25H2 版本推送了非安全更新**KB5074105**。尽管该更新最初对外宣传的内容仅包含一系列功能增强与漏洞修复，微软却对补丁中暗藏的多项重要安全强化措施只字未提。

随后微软发布了一份澄清说明，详细介绍了一项用于强化 Windows 11 文件系统的**全新安全功能**。根据这项新规，非管理员用户被严格禁止访问**存储设置**。该设置界面位于系统设置应用的 “系统” 子菜单中，涵盖了存储感知、清理建议、备份方案、存储空间以及磁盘与卷管理等关键功能；同时它也是清理回收站文件、传递优化文件、系统缩略图等临时数据的核心操作入口。

这项经调整的权限规则明确规定，上述所有配置项的访问权限**仅限管理员专属**。普通用户一旦尝试进入存储设置界面，系统会立即弹出**用户账户控制（UAC）** 验证窗口，要求输入管理员凭据才能继续操作。

考虑到普通用户依然可以手动清空回收站或删除特定文件，这项权限限制的具体战略意图目前仍略显费解。将旧版更新碎片等辅助数据的操作权限纳入管理员专属范畴，对普通用户而言，似乎难以带来实质性的安全增益。因此，行业分析人士指出，微软将该调整归类为安全功能，其核心目的实则是**为企业 IT 管理员赋能**。通过限制普通用户的访问权限，企业能够对存储感知功能的配置实施集中管控，确保系统自动化维护与冗余数据清理流程不受未授权操作的干扰。

本文翻译自securityonline [原文链接](https://securityonline.info/admins-only-microsofts-new-windows-11-update-quietly-locks-down-storage-settings/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314713](/post/id/314713)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/admins-only-microsofts-new-windows-11-update-quietly-locks-down-storage-settings/)

如若转载,请注明出处： <https://securityonline.info/admins-only-microsofts-new-windows-11-update-quietly-locks-down-storage-settings/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1000**

* 粉丝
* **6**

### TA的文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58

### 相关文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58
* ##### [Notepad++被劫持国家级攻击者投毒更新包，持续数月作恶](/post/id/314722)

  2026-02-04 11:24:22
* ##### [Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序](/post/id/314725)

  2026-02-04 11:23:54
* ##### [WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞](/post/id/314716)

  2026-02-04 11:23:22

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