---
title: 思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用
url: https://www.anquanke.com/post/id/314880
source: 安全客-有思想的安全新媒体
date: 2026-02-27
fetch_date: 2026-02-28T03:50:06.059342
---

# 思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用

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

# 思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用

阅读量**20038**

发布时间 : 2026-02-27 10:28:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-three-year-shadow-critical-cvss-10-cisco-sd-wan-zero-day-exploited-by-uat-8616/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

思科 Talos 发布**最高级别安全预警**，针对 **CVE-2026-20127** 漏洞发起主动攻击利用告警。该漏洞影响**思科 Catalyst SD-WAN 控制器**，**CVSS 评分 10.0**，**允许未授权远程攻击者完全绕过身份认证**。

问题核心出在思科 Catalyst SD-WAN 控制器（原 vSmart）与管理器（原 vManage）中**存在缺陷的对等认证机制**。攻击者通过构造精心设计的请求，即可绕过该机制登录受影响系统。

一旦入侵成功，攻击者将获得**内部高权限非 root 管理员权限**。凭借该权限，攻击者可访问 **NETCONF** 接口，**实现对整个 SD-WAN 网络配置的完全操控**。

思科 Talos 将相关攻击活动归类为 **UAT-8616** 团伙，并高度确信其为**高水准的专业网络威胁组织**。

更令人警惕的是，证据显示**此类恶意活动已持续至少三年**，最早可追溯至 2023 年。这也符合当前威胁组织针对**关键基础设施等高价值目标**，长期潜伏网络边界设备的典型趋势。

为将权限提升至 **root**，UAT-8616 使用了一套隐蔽的组合攻击手法：

1. 攻击者在已攻陷设备上**执行软件版本降级**
2. 随后利用旧版漏洞 **CVE-2022-20775**
3. 最后恢复原始软件版本，**隐蔽维持 root 权限**

企业必须重点审计思科 Catalyst SD-WAN 日志中**异常的控制连接对等事件**，这是通过 **CVE-2026-20127** 发起初始入侵的典型特征。此类行为需**人工复核**，才能区分正常操作与潜在入侵行为。

安全团队应重点排查以下 **UAT-8616 入侵高可信度指标**：

1. 生产系统中出现**交互式 root 会话**，包含不明 SSH 密钥与已知主机记录
2. 出现针对 `vmanage-admin` 账户的**未授权 SSH 密钥**
3. 日志被篡改痕迹：如 `syslog`、`wtmp`、`lastlog`、`cli-history`、`bash_history` 等文件异常缩小或被清空
4. 设备出现**未授权的版本升降级并伴随系统重启**

目前**暂无可用的软件级临时缓解方案**。

思科托管云环境（含思科托管版与 FedRAMP 环境）已部署防护措施。

**本地部署环境**的用户必须加固控制器间通信。

思科建议使用**访问控制列表（ACL）** 或防火墙规则，**严格限制 22 端口与 830 端口**，仅允许可信控制器与 IP 地址访问。

思科**强烈建议所有用户升级至已修复版本**以彻底解决该漏洞。目前已有多个补丁可用，更多版本将陆续发布：

### 思科 Catalyst SD-WAN 修复版本对照表

| 发行版本 | 首个修复版本 |
| --- | --- |
| 早于 20.9 | 迁移至修复版本 |
| 20.9 | 20.9.8.2（预计 2026 年 2 月 27 日发布） |
| 20.11、20.12.5、20.12.6 | 20.12.5.3 / 20.12.6.1 |
| 20.13、20.14、20.15 | 20.15.4.2 |
| 20.16、20.18 | 20.18.2.1 |

本文翻译自securityonline [原文链接](https://securityonline.info/the-three-year-shadow-critical-cvss-10-cisco-sd-wan-zero-day-exploited-by-uat-8616/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314880](/post/id/314880)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-three-year-shadow-critical-cvss-10-cisco-sd-wan-zero-day-exploited-by-uat-8616/)

如若转载,请注明出处： <https://securityonline.info/the-three-year-shadow-critical-cvss-10-cisco-sd-wan-zero-day-exploited-by-uat-8616/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

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
* **1030**

* 粉丝
* **6**

### TA的文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42

### 相关文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42
* ##### [未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击](/post/id/314906)

  2026-02-27 10:29:22
* ##### [Claude Code推出远程控制功能 实现移动端全自主开发](/post/id/314902)

  2026-02-27 10:28:57

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