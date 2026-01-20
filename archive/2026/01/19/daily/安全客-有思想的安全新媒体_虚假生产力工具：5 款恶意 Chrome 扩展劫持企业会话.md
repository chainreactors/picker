---
title: 虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话
url: https://www.anquanke.com/post/id/314370
source: 安全客-有思想的安全新媒体
date: 2026-01-19
fetch_date: 2026-01-20T03:30:17.563911
---

# 虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话

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

# 虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话

阅读量**22513**

发布时间 : 2026-01-19 16:53:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Socket 威胁研究团队揭露了一场针对企业环境的新型、高度复杂的攻击活动。五款伪装成生产力工具的恶意 Google Chrome 扩展被发现正在**窃取身份验证令牌并劫持用户会话**，目标涵盖 Workday、NetSuite、SAP SuccessFactors 等主流企业平台。

这些恶意扩展包括 **DataByCloud Access、Data By Cloud 1、Data By Cloud 2、Tool Access 11 和 Software Access**，累计安装量已超过 **2,300 名用户**。它们表面上承诺简化工作流程、提供 “高级工具”，实则用于渗透企业网络并削弱安全响应能力。

攻击者为恶意软件披上了专业、合法的外衣。这些扩展拥有精致的控制面板，并请求看似正常的权限，不会立即引起怀疑。![]()

“这些扩展将自己伪装成生产力工具，声称能简化企业平台的访问流程…… 主要针对需要在多个账号间切换或追求更快工作流的用户。”

然而，在这层伪装之下，是一个协调一致的恶意软件运营。Socket 的分析显示，这些工具共享**完全相同的代码结构、API 端点和安全工具检测列表**，表明它们来自同一威胁 actor。

### 攻击链：三大恶意技术协同入侵

该攻击活动采用三种核心技术来攻陷账号并维持长期控制：

#### 1. Cookie 窃取（Cookie Exfiltration）

这些扩展会持续收集会话令牌。例如，**DataByCloud Access** 会提取名为 **\_session** 的 Cookie，并每隔 **60 秒** 将其发送到攻击者的 **C2 服务器**。

“这确保即使用户在正常工作流程中登出并重新登录，威胁 actor 仍能保持对最新令牌的掌控。”

#### 2. 会话劫持（Session Hijacking）

**Software Access** 扩展更进一步，实现了**双向 Cookie 注入**。它会从攻击者服务器获取被盗的凭证，并将其直接注入受害者浏览器，从而**绕过多因素认证（MFA）**。

“Software Access 的双向 Cookie 注入完全绕过了身份验证要求，使攻击者无需密码即可访问被攻陷的账号。”

#### 3. 阻断安全响应（Blocking Incident Response）

最阴险的功能是它们能够让安全团队 “失明”。例如 **Data By Cloud 2** 和 **Tool Access 11** 会主动监控并阻止访问关键管理页面。

“这些阻断型扩展会造成‘遏制失效’场景。安全团队即使发现了可疑活动…… 但所有标准的补救措施都会被阻断。”

被阻断的页面包括：

* 密码修改表单
* 双因素认证设备管理
* 安全审计日志

当管理员试图访问这些页面时，扩展会立即清空内容并进行重定向，使安全人员无法进入自己的管理界面。

### 反检测机制（Anti-Detection）

恶意软件作者还加入了多种反研究机制。部分变体使用 **DisableDevtool** 库阻止代码检查，并通过 **“RegExp toString 篡改”** 检测调试器是否处于激活状态。

“没有任何合法扩展会阻止用户查看自己的密码字段，也不会阻止开发者工具打开。这些功能的存在只有一个目的：隐藏恶意行为。”

### 影响与建议

通过攻陷员工日常使用的工具，攻击者可以绕过边界防护，直接访问敏感的 **HR 与 ERP 数据**。企业被建议立即：

* 审查浏览器扩展策略
* 调查是否安装了上述恶意插件
* 限制员工随意安装扩展
* 加强对会话令牌和 Cookie 的监控

本文翻译自securityonline 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314370](/post/id/314370)

安全KER - 有思想的安全新媒体

本文转载自: securityonline

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **930**

* 粉丝
* **6**

### TA的文章

* ##### [1340 亿美元豪赌：马斯克起诉 OpenAI，加州监管重拳同时砸向 xAI](/post/id/314365)

  2026-01-19 16:54:15
* ##### [CVE-2026-0695：ConnectWise PSA 2026.1 修复高危跨站脚本（XSS）漏洞](/post/id/314368)

  2026-01-19 16:53:36
* ##### [虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话](/post/id/314370)

  2026-01-19 16:53:09
* ##### [未修补的远程代码执行漏洞：Livewire Filemanager 文件上传缺陷（CVE-2025-14894）影响 Laravel 应用](/post/id/314374)

  2026-01-19 16:52:22
* ##### [Deno 高危漏洞可导致密钥泄露（CVE-2026-22863）与代码执行（CVE-2026-22864）](/post/id/314377)

  2026-01-19 16:51:31

### 相关文章

* ##### [1340 亿美元豪赌：马斯克起诉 OpenAI，加州监管重拳同时砸向 xAI](/post/id/314365)

  2026-01-19 16:54:15
* ##### [CVE-2026-0695：ConnectWise PSA 2026.1 修复高危跨站脚本（XSS）漏洞](/post/id/314368)

  2026-01-19 16:53:36
* ##### [未修补的远程代码执行漏洞：Livewire Filemanager 文件上传缺陷（CVE-2025-14894）影响 Laravel 应用](/post/id/314374)

  2026-01-19 16:52:22
* ##### [Deno 高危漏洞可导致密钥泄露（CVE-2026-22863）与代码执行（CVE-2026-22864）](/post/id/314377)

  2026-01-19 16:51:31
* ##### [2026 年会迎来微芯片植入的 “ChatGPT 时刻” 吗？](/post/id/314380)

  2026-01-19 16:51:12
* ##### [大规模清理行动：X 平台禁用 “信息金融”，彻底打击 AI 生成的加密垃圾帖](/post/id/314383)

  2026-01-19 16:50:29
* ##### [五款恶意 Chrome 扩展程序伪装成 Workday 与 NetSuite 以劫持账户](/post/id/314386)

  2026-01-19 16:49:57

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