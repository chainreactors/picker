---
title: FreePBX 服务器遭零日漏洞攻击，官方紧急发布修复方案
url: https://www.anquanke.com/post/id/311725
source: 安全客-有思想的安全新媒体
date: 2025-08-30
fetch_date: 2025-10-07T00:17:57.630578
---

# FreePBX 服务器遭零日漏洞攻击，官方紧急发布修复方案

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

# FreePBX 服务器遭零日漏洞攻击，官方紧急发布修复方案

阅读量**72864**

发布时间 : 2025-08-29 16:00:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/freepbx-servers-hacked-via-zero-day-emergency-fix-released/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Sangoma FreePBX 安全团队近日发布紧急通告，警告一个正在被 **积极利用的零日漏洞**，该漏洞影响所有 **直接将管理员控制面板（ACP）暴露在互联网上的 FreePBX 系统**。

FreePBX 是一款基于 Asterisk 的开源 PBX（专用交换机）平台，被广泛用于企业、呼叫中心和服务提供商，以管理语音通信、分机、SIP 中继和呼叫路由。

## 官方警告与临时修复

在 FreePBX 论坛的公告中，安全团队表示：

> “我们注意到一个可能影响部分 FreePBX 系统的漏洞，尤其是那些将管理员控制面板直接暴露在公网的实例。攻击行为自 8 月 21 日起已被观测到。团队正在开发修复补丁，预计将在 36 小时内发布。”

安全团队建议用户立即采取措施，通过 **Firewall 模块限制 ACP 访问，仅允许可信主机**。

目前，Sangoma 已发布了一个 **EDGE 模块修复补丁**供测试使用，标准的安全更新预计将在当天晚些时候正式发布。

需要注意的是，该 EDGE 模块修复仅能 **保护未来的新安装系统**，**无法修复已被入侵的现有系统**。

官方警告称：

* FreePBX **16 和 17** 版本可能已受影响，前提是：
  1. 安装了 Endpoint 模块；
  2. 管理员登录页面直接暴露在公网等不可信网络。

## 紧急安装方法

* FreePBX v16 / v17 用户：

```
fwconsole ma downloadinstall endpoint --edge
```

* PBXAct v16 用户：

```
fwconsole ma downloadinstall endpoint --tag 16.0.88.19
```

* PBXAct v17 用户：

```
fwconsole ma downloadinstall endpoint --tag 17.0.2.31
```

但有部分用户反馈，如果支持合同已过期，可能无法安装 EDGE 补丁，从而导致设备依然处于风险之中。对于无法安装的用户，官方建议 **立即阻止 ACP 访问**，直到正式补丁发布。

## 攻击已导致大规模入侵

自公告发布以来，已有大量 FreePBX 用户报告服务器遭入侵。

有客户在论坛发帖称：

> “我们报告称，基础设施中多台服务器遭到攻陷，约 3,000 个 SIP 分机与 500 条中继受影响。我们已紧急锁定所有管理员访问，并将系统恢复至攻击前的状态。但我们必须强调确定入侵范围的重要性。”

在 Reddit 上，另一位用户表示：

> “我的个人 PBX 以及我协助管理的一台 PBX 都被攻陷了。该漏洞基本允许攻击者以 Asterisk 用户权限执行任意命令。”

## 入侵迹象（IOC）

尽管 Sangoma 尚未披露漏洞的具体技术细节，但已知的一些入侵迹象包括：

* **缺失或被篡改**的 `/etc/freepbx.conf` 配置文件
* `/var/www/html/` 目录下出现可疑脚本 `.clean.sh`
* Apache 日志中存在异常的 **modular.php** 请求
* Asterisk 日志中出现异常的 **分机 9998** 呼叫记录，时间可追溯至 8 月 21 日
* MariaDB/MySQL 数据库 **ampusers 表**中新增可疑账号，尤其是名为 **“ampuser”** 的条目

## 官方处置建议

若确认服务器已被入侵，Sangoma 建议：

1. **恢复至 8 月 21 日前的备份**
2. 在全新系统上部署修复补丁
3. **重置所有系统与 SIP 相关凭据**
4. 检查通话记录与账单，关注是否有未经授权的国际呼叫

Sangoma 强调：所有 **直接暴露 ACP 界面的 FreePBX 系统** 都可能已经被攻陷。管理员应立即排查环境并采取防护措施，直到安全补丁全面部署。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/freepbx-servers-hacked-via-zero-day-emergency-fix-released/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311725](/post/id/311725)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/freepbx-servers-hacked-via-zero-day-emergency-fix-released/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/freepbx-servers-hacked-via-zero-day-emergency-fix-released/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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

* [官方警告与临时修复](#h2-0)
* [紧急安装方法](#h2-1)
* [攻击已导致大规模入侵](#h2-2)
* [入侵迹象（IOC）](#h2-3)
* [官方处置建议](#h2-4)

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