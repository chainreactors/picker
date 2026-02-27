---
title: 让OpenClaw安全上岗，火山引擎发布首个AI助手安全方案
url: https://www.anquanke.com/post/id/314871
source: 安全客-有思想的安全新媒体
date: 2026-02-26
fetch_date: 2026-02-27T04:06:52.329911
---

# 让OpenClaw安全上岗，火山引擎发布首个AI助手安全方案

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

# 让OpenClaw安全上岗，火山引擎发布首个AI助手安全方案

阅读量**24522**

发布时间 : 2026-02-26 12:35:26

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

作为现象级的开源 AI Agent 项目，OpenClaw 凭借强大的自主执行能力，正迅速成为能够操作文件、调用系统命令、控制浏览器的“数字员工”。同时，这种能力也带来了一系列的安全风险。例如**本地敏感信息外发，执行破坏性高危操作或被远程控制，引发数据泄露、系统损毁、业务中断**等严重问题。

针对这些问题，火山引擎重磅推出**三层纵深安全防护方案**，助力企业构建“安全可控”的数字员工。

* **·** 第一层：平台安全，通过访问控制、指令过滤、执行沙箱、技能准入扫描，确保默认安全。
* **·** 第二层：AI 助手安全 **（AI Assistant Security）** ，防范提示词注入、高危操作、敏感信息泄露等导致的风险。
* **·** 第三层：供应链安全，提供 **Skills 的深度安全检测**，避免供应链攻击风险。

**平台安全**
**打造“免疫级”底层环境**

火山引擎为通过 ECS 和 Agentkit 部署的 OpenClaw 提供基础安全保障方案，从**访问控制、指令过滤、执行环境、安全准入**四个维度，构建相应的底层防御能力。

* **·** 入口层：默认仅绑定本地端口，减少公网暴露面，强制 token/密码认证及网关鉴权，确保每次访问真实可靠。
* **·** 决策层：镜像预置提示词加固策略，自动识别并过滤恶意注入指令，防止 Agent 被“洗脑”或指令篡改。
* **·** 执行层：默认在 veFaaS 沙箱中运行，通过容器和网络双隔离机制及非 Root 权限运行，将风险锁定在沙箱内。
* **·** 生态层：对镜像和预置 Skills 进行深度扫描检查，持续追踪恶意 Skills 并推动修复。

**AI助手安全**
**打造安全可控的“数字员工”**

火山引擎全新发布 AI Assistant Security ，在 OpenClaw 等 AI 助手类智能体的交互环节（如调用大模型、Skills 及工具等），提供针对高危操作、敏感信息泄露、提示词注入等风险的防护和管控。

![picture.image]()

**// 三大典型场景，感受安全价值**

**个人隐私的脱敏和保护**：识别身份证号、手机号等敏感信息，严控敏感数据出域，确保个人隐私不被泄露。

**高危操作的拦截**：在调用工具和技能前，识别如“资金转账、敏感数据外发、文件恶意删除”等高危操作，实现默认阻断或降级为人工确认，避免模糊指令带来不可逆的损失。

**提示词攻击的防护**：当 AI 数字员工联网访问到恶意网页，其中暗藏的恶意提示词导致 AI 数字员工被远程控制并带来不可控的后果，AI Assistant Security 会提前识别异常并给出安全提示，确保 AI 只执行用户的真实意图。

[AI助手安全演示视频](https://bytedance.larkoffice.com/file/RBrLbo9Q4odrXlxcwmkcvv1EnHd)

**// 快速上手，限时免费试用**

目前，火山引擎 AI Assistant Security for OpenClaw 的安全防护方案，面向所有用户开启限时免费试用。

**👉** **火山引擎客户**

* **已购客户**：已购买 OpenClaw ECS 的客户，在云服务器-运维编排-应用更新中点击创建任务，选择安全加固和需要加固的实例，下发任务即可完成防护。

![picture.image]()

* **新购客户**：火山引擎 ECS 标准镜像已自带该防护插件，初始化即拥有安全能力。

![picture.image]()

**👉** **非火山引擎客户**

通过简单的命令自动完成安装。

1. 1.登入到您部署 OpenClaw 的服务器上执行下方命令，安装插件的命令行工具。

```
npm i -g @omni-shield/openclaw-cli
```

1. 2.安装完成，执行下方命令启动配置流程。

```
omni-shield-openclaw
```

1. 3.安装过程会自动检测环境并生成一个有时效性的登录 URL，通过浏览器访问 URL 跳转登录火山引擎账号，登录完成后，命令行工具自动检测登录状态，自动执行插件的安装和配置流程。

1. 4.安装完成后，按 **Y** **\*\*重启 OpenClaw 以使配置生效，或执行** openclaw gateway restart\*\* 重启正在运行的 OpenClaw 服务，重启后正式生效。

**供应链安全**
**让Skills安全调用**

Skills 作为 OpenClaw 的“手”，通过封装特定能力供 OpenClaw 调用以完成复杂任务。然而，随着 Skills 的权限过大及恶意 Skills 的涌现，导致账户凭证外泄、执行木马病毒等安全事件频发。

针对此痛点，火山引擎智能体安全管理平台的扫描功能全面升级，支持对 MCP/Skills 的深度扫描。用户可以自行上传任意 Skills 文件，平台提供预置的扫描规则可对上传的 Skills 进行深度扫描，并输出详细的风险详情，实现了覆盖事前检测、定期巡检、事中拦截的全生命周期安全防护：

* **风险检测**：依托平台预置扫描规则，对 OpenClaw 本地部署的 Skills 进行深度扫描
* **定期巡检**：基于 OpenClaw 的 Cron 机制，支持定期对更新的 Skills 进行自动扫描
* **动态拦截**：当 OpenClaw 的 Skills 被加载时，平台会判断其是否经过扫描。若未经过扫描，平台将即时发起检测，并根据风险评估情况决定是否继续执行

![picture.image]()
（预置扫描规则、上传Skills文件、Skills风险详情）

**// 使用教程**

目前，火山引擎智能体安全管理平台私有化版本已上线扫描方案，面向所有用户开启限时免费试用。同时，公有云版本将在2月底对外上线，届时欢迎大家体验。

在私有化版本中，对接 OpenClaw 和智能体安全管理平台对 Skills 进行安全扫描，具体操作步骤如下：

* **·** 下载智能体安全管理平台的 Skills 扫描安装包； [Skills-Security-Scanner](https://bytedance.larkoffice.com/file/Rbm0bNBViowSNqxB0Ltc9qBAnNe)
* **·** 将上方压缩包解压至 OpenClaw 目录下 ~/.openclaw/workspace/skills/；

* **·** 通过 OpenClaw 的对话 Agent 查询 Skills 列表，查看上方 Skills 是否已经被加载；

* **·** 通过 OpenClaw 提示词用 Skills-Security-Scanner 对1password（OpenClaw平台自带的Skills）进行扫描；

* **·** 通过 OpenClaw 的控制台展现扫描结果，识别潜在威胁。

[Skills深度安全扫描演示视频](https://bytedance.larkoffice.com/file/EmZMb1UzSoeaZ6xkBCbch2npnZc)

安全是 AI 真正成为生产力的底线。火山引擎通过三层纵深安全防护方案，助力开发者在享受 AI 效率的同时，无需担心隐私外泄与操作风险。现在，上火山引擎一键安全防护，让你的 AI 助手安全上岗。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**火山引擎云安全**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314871](/post/id/314871)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [AI安全](/tag/AI%E5%AE%89%E5%85%A8)
* [Agent安全](/tag/Agent%E5%AE%89%E5%85%A8)
* [OpenClaw](/tag/OpenClaw)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t01d7c5cb6fdb04a6cc.png)火山引擎云安全

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t01d7c5cb6fdb04a6cc.png)](/member.html?memberId=165382)

[火山引擎云安全](/member.html?memberId=165382)

火山引擎云安全产品是字节跳动旗下的企业级安全技术服务产品

* 文章
* **43**

* 粉丝
* **5**

### TA的文章

* ##### [让OpenClaw安全上岗，火山引擎发布首个AI助手安全方案](/post/id/314871)

  2026-02-26 12:35:26
* ##### [开源！可信MCP，AICC机密计算新升级！](/post/id/312944)

  2025-10-31 11:27:13
* ##### [打造可信AI Agent：如何让智能体不跑偏、不越界，安全又靠谱](/post/id/312818)

  2025-10-23 18:25:38
* ##### [MCP 安全“体检” | 基于 AI 驱动的 MCP 安全扫描系统](/post/id/312465)

  2025-10-10 09:35:34
* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32

### 相关文章

* ##### [利润仅$200？Anthropic 最新研究揭示 AI 自动挖掘 0-day 的真实经济账](/post/id/313896)

  2025-12-19 14:36:30
* ##### [打造可信AI Agent：如何让智能体不跑偏、不越界，安全又靠谱](/post/id/312818)

  2025-10-23 18:25:38
* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50
* ##### [360 MCP 生态安全风险治理实践与思考](/post/id/307934)

  2025-05-29 11:07:56
* ##### [SAST｜UtopianCode从检测到治理：AI 助力代码漏洞修复](/post/id/298966)

  2024-09-03 16:29:38
* ##### [AI时代的安全护航者：F5的全方位安全防护与创新](/post/id/297340)

  2024-06-17 17:58:12

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