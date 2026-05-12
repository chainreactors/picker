---
title: 今日（2026年5月11日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/vk5fU91FeZy9wnfnQUCEYA
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:36:44.233670
---

# 今日（2026年5月11日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uiaROkU1HLSJXUe1BFxPQphRDb8hjuzD4zgayibibc8csiaW6via7CDPbJfR2tOn6ibtF0Kj5RicYcMgK7iccLlDMibMtEQDurMbOJstIU/0?wx_fmt=jpeg)

# 今日（2026年5月11日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

日期: 2026-05-11  |  威胁等级: **High**  |  来源: securityonline.info · NVD · thehackernews

## 一、概要

2026年5月11日，集中披露多条高危漏洞：**cPanel & WHM Perl代码注入**补丁刚出即被重点追踪；**Android ADB 认证绕过**公开 PoC 实现零点击远程代码执行；**Grav CMS 利用链**可零基础实现完全主机控制；MAD Bugs 项目披露**PHP unserialize 21年历史 UAF 漏洞**，AI 辅助发现并附完整 exploit，安全社区今日热度极高。

## 二、高危漏洞详情

### CVE-2026-29202：cPanel & WHM Perl代码注入漏洞

CVSS 8.8Root访问风险活跃讨论补丁刚出

**受影响产品：**cPanel & WHM（11.136.0.9 及以下等未修补版本，WP Squared 也受影响）。

**影响：**已认证用户通过 create\_user API 的 plugin 参数实现 **Perl 代码注入**，可执行任意 Perl 代码（以系统用户身份）；结合 symlink 等 flaw 可权限提升、文件读写、DoS。

**热度原因：**securityonline.info 今日突出报道"Root Access at Risk"，补丁刚发布（5月8日），cPanel 广泛用于共享主机，大量实例未及时更新，活跃讨论和检测签名已出现。

**修复建议：**立即更新至 11.136.0.9+ 等修补版本；限制 API 访问来源；监控异常 create\_user 调用日志；优先处置面向互联网的共享主机环境。

### CVE-2026-0073：Android ADB 认证绕过漏洞

零点击RCE邻近网络PoC已公开Android多版本

**受影响产品：**Android 系统（特定版本，adbd 组件，Android 14/15/16 等）。

**影响：**无线 ADB 互认证绕过，邻近网络攻击者可**零点击实现远程代码执行**（shell 用户权限），无需用户交互，公开 PoC 已披露。

**热度原因：**securityonline.info 今日重点报道"Zero-Click Shell: Public Exploit and PoC"；移动端覆盖面极广，邻近攻击场景对企业内网和公共场所充电站等环境威胁突出。

**修复建议：**更新至 2026-05-01 或更高安全补丁级别；**禁用不必要 ADB 调试**（尤其是无线 ADB）；监控 ADB 端口（5555等）异常连接；企业移动设备管理（MDM）策略审查。

### CVE-2026-42613 等：Grav CMS 关键利用链漏洞

未认证RCE链式利用路径遍历文件写入

**受影响产品：**Grav CMS（v1.7.49.5 及类似未修补版本，FormFlash 等组件）。

**影响：**未认证路径遍历 + 任意文件写入 + 权限提升，链式组合实现 **unauthenticated RCE（零登录完全主机控制）**。

**热度原因：**securityonline.info 今日报道"Zero Installation, Total Compromise"；公开利用链，CMS 用户基数大，攻击门槛极低，适合批量扫描利用。

**修复建议：**升级至 2.0.0-beta.2+ 或最新版本；禁用公开注册；加强输入验证和文件操作限制；Web 应用防火墙（WAF）规则覆盖路径遍历特征。

### PHP unserialize() Use-After-Free 漏洞（MAD Bugs 项目）21年历史MAD BugsAI辅助发现

**受影响产品：**PHP（自 5.1 以来所有版本，至最新 8.5.5；Serializable 接口相关路径）。

**影响：**unserialize() 中缺少 BG(serialize\_lock)++ 导致 UAF，本地可绕过 disable\_functions 实现 RCE（无需 /proc 或硬编码偏移）；远程需特定类（实现 Serializable 并递归 unserialize），约 **2000 HTTP 请求**可达成 RCE。公开 PoC 和完整 exploit 已发布。

**热度原因：**MAD Bugs（AI 辅助发现）系列技术博客，5月初发布后今日持续传播；PHP 生态极广泛，证明 AI 系统可发现古老高危 bug 并编写可用 exploit，引发对历史代码安全性的广泛讨论。

**修复建议：**升级至官方包含修复的最新 PHP 版本；**永远不要将不受信任输入传入 unserialize()**（使用 json\_decode() 等安全替代）；对相关代码进行沙箱隔离；监控异常反序列化调用日志。

### 其他值得关注的漏洞

LLM安全**Spring AI 数据破坏和内存投毒漏洞**——威胁 LLM 应用完整性，使用 Spring AI 框架的应用需关注官方安全通告。

## 三、总体修复提醒

**最高优先（立即处理）：**

* cPanel & WHM（CVE-2026-29202）——立即更新至 11.136.0.9+；共享主机环境优先处置；监控 create\_user API 调用。
* PHP unserialize UAF（MAD Bugs）——尽快升级 PHP；全面替换 unserialize() 为 json\_decode()；检测反序列化异常日志。

**高优先级（48小时内处理）：**

* Android ADB 认证绕过（CVE-2026-0073）——更新安全补丁；禁用无线 ADB；企业 MDM 策略审查。
* Grav CMS 利用链（CVE-2026-42613等）——升级至 2.0.0-beta.2+；禁用公开注册；WAF 规则覆盖。

**通用防护建议：**

* 启用上述产品的**自动更新**机制，确保安全补丁及时生效。
* 监控异常网络流量和 API 调用日志，配置告警阈值。
* 访问 securityonline.info 持续跟踪最新漏洞披露与官方补丁动态。
* 建立漏洞响应 SOP，快递验证、测试与生产部署全流程闭环。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过