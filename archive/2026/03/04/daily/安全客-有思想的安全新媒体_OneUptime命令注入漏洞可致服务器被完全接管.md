---
title: OneUptime命令注入漏洞可致服务器被完全接管
url: https://www.anquanke.com/post/id/314962
source: 安全客-有思想的安全新媒体
date: 2026-03-04
fetch_date: 2026-03-05T04:05:28.624556
---

# OneUptime命令注入漏洞可致服务器被完全接管

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

# OneUptime命令注入漏洞可致服务器被完全接管

阅读量**26995**

发布时间 : 2026-03-04 10:37:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/oneuptime-command-injection-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在线服务监控与管理平台 OneUptime 被曝出一处**高危命令注入漏洞**，编号为 **CVE-2026-27728**。

该漏洞可使已认证用户在 Probe 服务器上执行**任意系统命令**，存在**服务器被完全接管**的重大风险。

使用 **10.0.7 之前版本**的机构建议立即安装补丁。

### 命令注入漏洞详情

网络安全厂商 SentinelOne 通报，该漏洞存在于 OneUptime Probe Server 组件中的 **NetworkPathMonitor.performTraceroute () 函数**。

该函数负责网络路由追踪（traceroute）操作，并接收用户可控输入，具体为监控配置中的**目标地址（destination）字段**。

漏洞根源在于应用对该输入的处理方式：**存在风险的代码直接使用 Node.js child\_process 模块中的 exec () 函数启动 Shell 命令**。

由于 exec () 会在 Shell 环境中执行命令，**可被；、|、&、$()、反引号等 Shell 元字符解析利用**。

攻击者借此可脱离原本仅执行 traceroute 的正常逻辑，**注入并执行恶意命令**。

尽管产品设计仅允许用户配置监控端点，但该漏洞可导致**任意已认证项目用户**（即便权限受限），都能在底层 Probe 服务器上实现**完整远程代码执行（RCE）**。

利用该漏洞仅需**项目用户级别的低权限认证**。

攻击者可构造恶意监控配置，在目标地址字段中填入 **Shell 元字符拼接任意命令**。

例如注入 `example.com; cat /etc/passwd` 或 `$(恶意命令)`，即可在执行路由追踪的同时运行注入指令。

Probe 服务器处理该监控任务时，**注入命令将以与 Probe 服务进程相同的权限运行**。

这会直接导致**服务器被完全攻陷**，攻击者可窃取敏感数据，并在机构内网中进行横向移动。

OneUptime 已在 **10.0.7 版本**中修复该问题。安全补丁将存在风险的 **exec () 替换为 execFile ()**。

与 exec () 不同，**execFile () 会直接执行指定文件，并以数组形式传递参数，不会启动 Shell 环境**。

此举可阻止 Shell 元字符被解析，**从根源上消除命令注入攻击面**。

### 缓解与防护建议

为防范 CVE-2026-27728 漏洞，机构可采取以下措施：

* **立即升级**：将 OneUptime 更新至 **10.0.7 及以上版本**，启用安全的 execFile () 函数并开启目标地址校验。
* **配置审计**：检查现有监控配置，排查目标地址中是否存在包含特殊字符的可疑值。
* **系统监控**：关注 Probe 服务器上**异常进程创建、非预期网络连接、未授权文件系统修改**等行为。
* **临时规避**：若无法立即升级，可隔离 Probe 服务器、仅向可信人员开放项目用户权限，并严格限制服务器网络访问。

本文翻译自gbhackers [原文链接](https://gbhackers.com/oneuptime-command-injection-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314962](/post/id/314962)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/oneuptime-command-injection-vulnerability/)

如若转载,请注明出处： <https://gbhackers.com/oneuptime-command-injection-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28
* ##### [AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户](/post/id/314998)

  2026-03-04 10:33:55

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