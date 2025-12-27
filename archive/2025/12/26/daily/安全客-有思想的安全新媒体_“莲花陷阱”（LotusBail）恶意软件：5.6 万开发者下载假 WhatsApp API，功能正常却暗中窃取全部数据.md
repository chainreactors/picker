---
title: “莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据
url: https://www.anquanke.com/post/id/314059
source: 安全客-有思想的安全新媒体
date: 2025-12-26
fetch_date: 2025-12-27T03:21:01.514839
---

# “莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据

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

# “莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据

阅读量**15648**

发布时间 : 2025-12-26 14:48:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/lotusbail-trap-56000-developers-downloaded-a-fake-whatsapp-api-that-works-perfectly-while-stealing-everything/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

锦鲤安全（Koi Security）开展的一项最新调查显示，npm 代码仓库中潜藏着一起手法极为高超的**供应链攻击**。一款名为 lotusbail 的恶意包伪装成合规的 WhatsApp 网页版 API 库，长达 6 个月时间里诱骗超 5.6 万名开发者将其集成至自身项目中。

该恶意包是基于合规热门库 @whiskeysockets/baileys 二次开发的分支版本，表面上完全兑现功能承诺：可支持开发者搭建 WhatsApp 机器人及各类集成应用，但在正常功能之下，却隐藏着能造成毁灭性后果的恶意载荷。

lotusbail 的阴险之处在于其**功能完备性**。不同于那些常会导致受感染应用崩溃的低端恶意软件，这款恶意包运行毫无异常。安装该包的开发者会看到自身 WhatsApp 集成功能正常运转，完全不会怀疑其中藏有猫腻。

报告指出：“该恶意包已在 npm 平台上架 6 个月，截至本报告撰写时仍未被下架”，凸显这起攻击事件持续时间之长，令人心惊。

然而，就在应用替用户正常发送消息的同时，该恶意包还在暗中向攻击者传输敏感信息。报告明确，其恶意载荷属于**高级恶意软件**，具体行为包括：窃取用户 WhatsApp 账号凭证、拦截所有消息、盗取联系人列表、植入持久化后门，且所有窃取数据均会加密后发送至攻击者服务器。

lotusbail 的与众不同之处，在于这起攻击背后体现出的**专业级开发素养**。攻击者并非简单编写恶意代码，而是以商业软件厂商的严谨标准对恶意程序进行防护。

分析结果显示，该恶意包内置 27 个无限循环陷阱，专门用于冻结试图调试代码的安全研究人员的设备；这些陷阱会检测进程参数、识别沙箱环境，以此规避安全分析。

更具黑色讽刺意味的是，攻击者还严格遵循编码最佳实践。研究人员发现：“他们甚至在代码中添加注释，清晰标记恶意代码段 —— 将专业开发规范用在了供应链攻击上，恐怕有人还专门用 Jira 看板跟进这项攻击开发进度。”

lotusbail 最危险的特质或许是其**顽固性**：仅卸载受感染的恶意包根本无法彻底清理系统，该恶意软件会植入持久化后门，即便原始恶意文件被删除，后门仍会留存。

正如报告中给出的警示结论：“即便恶意包已被卸载，攻击者依然能持续访问你的系统。”

这起事件暴露出现代开发流程中的**核心漏洞**：信誉评级系统与静态分析工具往往会放行那些看似流行且功能正常的软件包，而 lotusbail 凭借 5.6 万次下载量，成功骗过了各类自动化检测工具。

锦鲤安全最终总结道：“这款恶意软件恰好藏身在‘代码能正常运行’与‘代码只做标称功能’的监管盲区之中。”

本文翻译自securityonline [原文链接](https://securityonline.info/lotusbail-trap-56000-developers-downloaded-a-fake-whatsapp-api-that-works-perfectly-while-stealing-everything/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314059](/post/id/314059)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/lotusbail-trap-56000-developers-downloaded-a-fake-whatsapp-api-that-works-perfectly-while-stealing-everything/)

如若转载,请注明出处： <https://securityonline.info/lotusbail-trap-56000-developers-downloaded-a-fake-whatsapp-api-that-works-perfectly-while-stealing-everything/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **860**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24

### 相关文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24
* ##### [潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击](/post/id/314062)

  2025-12-26 14:49:22
* ##### [英特尔 14A/18A 超级芯片：挑战台积电的 AI “系统代工” 标杆](/post/id/314055)

  2025-12-26 14:47:49

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