---
title: Claude Code推出远程控制功能 实现移动端全自主开发
url: https://www.anquanke.com/post/id/314902
source: 安全客-有思想的安全新媒体
date: 2026-02-27
fetch_date: 2026-02-28T03:50:04.298938
---

# Claude Code推出远程控制功能 实现移动端全自主开发

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

# Claude Code推出远程控制功能 实现移动端全自主开发

阅读量**17746**

发布时间 : 2026-02-27 10:28:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/workstation-in-your-pocket-claude-code-unveils-remote-control-for-total-mobile-dev-autonomy/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

AI 编程工具 **Claude Code** 正式推出全新**远程控制（Remote Control）功能，目前面向 Claude Pro 与 Claude Max 用户开放研究预览版。**

**这项创新将 Claude Code 升级为跨设备 AI 开发助手**，为开发者提供了目前极为流畅的**本地工作站 → 移动端**开发体验。

与此前的网页版 Claude Code 不同，**Remote Control 核心设计理念为完全本地计算**。

在该架构下，远程设备仅作为**显示与操作入口**，**所有数据均保留在本地环境中，不会上传至云端**。

Claude Code 可完整管理本地文件系统、终端命令、MCP 服务器与自定义工具，而手机、平板或浏览器客户端仅负责输入、输出与对话同步。

该功能的架构安全依赖**纯出站连接模型**。

本地进程通过 API 注册、HTTPS 轮询与流式传输实现通信，并采用多层短期有效、作用域受限的凭证及**完整 TLS 加密**进行保护。

由于系统**无需开放任何入站端口**，用户无需复杂的防火墙配置。

同时，会话具备极强的稳定性，在网络中断、设备休眠或切换 Wi‑Fi 后可**自动重连**。

对于重视安全的开发者，可使用 `--sandbox` 参数实现**文件系统与网络的严格隔离**，进一步降低安全风险。

---

### 使用前提与运行方式

**订阅要求**

需为有效 **Claude Pro / Claude Max** 订阅用户，**暂不支持企业与团队版本**。

**初始化**

用户需在项目目录中运行 Claude Code，并完成**工作空间信任授权**。

**启动方式**

* 命令行直接启动：

  `claude remote-control`

  （可附加 `--sandbox` 或 `--verbose` 参数）
* 已有会话内使用命令：

  `/remote-control` 或 `/rc`

**自动启用**

可通过 `/config` 菜单开启 “**为所有会话启用远程控制**”，实现持久化远程访问。

---

功能成功启动后，终端会显示**二维码**或**唯一访问 URL**，可直接通过 Claude 移动端 App 快速连接。

用户可在移动设备上**实时执行命令**、继续长时间任务（如复杂函数生成），甚至**多设备同时输入**。

根据当前安全策略，**每个实例仅限单个远程会话**，且终端进程必须保持运行：关闭设备或合盖会断开连接。

若网络中断，系统会在**10 分钟内持续尝试重连**，超时则会话自动失效。

Anthropic 表示将根据实验阶段的遥测数据持续优化这些限制。

本文翻译自securityonline [原文链接](https://securityonline.info/workstation-in-your-pocket-claude-code-unveils-remote-control-for-total-mobile-dev-autonomy/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314902](/post/id/314902)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/workstation-in-your-pocket-claude-code-unveils-remote-control-for-total-mobile-dev-autonomy/)

如若转载,请注明出处： <https://securityonline.info/workstation-in-your-pocket-claude-code-unveils-remote-control-for-total-mobile-dev-autonomy/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用](/post/id/314880)

  2026-02-27 10:28:35

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