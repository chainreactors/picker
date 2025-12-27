---
title: 潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击
url: https://www.anquanke.com/post/id/314062
source: 安全客-有思想的安全新媒体
date: 2025-12-26
fetch_date: 2025-12-27T03:20:59.041142
---

# 潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击

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

# 潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击

阅读量**16191**

发布时间 : 2025-12-26 14:49:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/evasive-panda-apt-hijacks-dictionary-com-and-app-updates-in-two-year-spree/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一个臭名昭著的网络间谍组织在过去两年间持续开展高精准监视行动，通过劫持网络流量、篡改 DNS 响应的方式，借助伪装成合法软件更新的载体投放恶意软件。卡巴斯基实验室发布最新报告，详细披露了**潜伏熊猫（Evasive Panda）** 组织（又名竹风暴 StormBamboo、匕首蝇 Daggerfly）的近期活动，该组织在 2022 年 11 月至 2024 年 11 月期间，针对中国、印度及土耳其境内目标发动了一场手法高超的攻击行动。

该组织自 2012 年起便活跃于网络空间，目前已升级攻击武器库，新增**混合加密技术**与一款新型隐身加载器，专门用于绕过现代安全防护体系。

此类攻击通常以经典木马策略开启：将恶意软件伪装成可信应用的更新程序。研究人员发现，该组织曾仿冒中国互联网巨头旗下热门流媒体应用搜狐影音（SohuVA）实施攻击。

报告明确指出：“这款名为 sohuva\_update\_10.2.29.1-lup-s-tp.exe 的恶意安装包，刻意仿冒正版搜狐影音更新程序，以此投放恶意软件。”

而其欺诈手段远不止于此。该组织还攻陷了多款主流软件的更新机制，涉及爱奇艺视频、IObit 智能磁盘整理工具及腾讯 QQ 等应用。攻击者将伪造更新程序植入软件合法安装目录，确保恶意代码能依托受信任的系统服务执行。

此次发现的最令人警惕的攻击手法，当属利用**中间人（AitM）攻击劫持网络流量**。其中一个典型案例显示，恶意软件会从看似无害的[Dictionary.com](https://dictionary.com/)词典网获取第二阶段恶意载荷。

分析表明，攻击者通过篡改 DNS 响应，将原本发往正版词典网的流量重定向至自身控制的服务器。研究人员解释：“我们的监测数据显示，攻击者成功将加密的第二阶段外壳代码伪装成 PNG 文件，从[Dictionary.com](https://dictionary.com/)这个合法网站下发至目标设备。”

这一手法让攻击者可根据受害者所在地区、互联网服务提供商（ISP）定制恶意载荷，既实现高精准打击，又让攻击难以在实验室环境中复现。

为确保植入的恶意程序持久驻留且不被检测，潜伏熊猫采用了复杂的**混合加密方案**。恶意软件整合微软数据保护接口（DPAPI）与 RC5 加密算法，对存储在受害者磁盘中的恶意载荷进行加密处理。

报告指出：“攻击者采用该方案，可确保攻击链核心环节的安全性，且加密数据仅能在最初执行加密操作的特定设备上解密。”

这项技术将恶意软件与受感染的目标设备深度绑定，即便窃取的文件被拿到研究人员的设备中分析，也会完全失效。

尽管投放手段不断翻新，该组织的最终目标始终是部署其标志性后门程序**MgBot**。新型加载器会将 “二级加载器” 伪装成合法 Windows 系统库文件（libpython2.4.dll），借此向 svchost.exe 等核心系统进程注入 MgBot 后门。

值得注意的是，攻击者研发了全新加载器，可在感染目标时规避检测，其运用的关键技术包括：借助一个已签名十年的合法可执行文件（evteng.exe）实施**DLL 侧载攻击**，全程保持隐身状态。

报告总结道：“潜伏熊猫威胁组织再次展现其高超攻击能力，依托新型技术与工具规避安全防护，同时实现对目标系统的长期持久化控制。”

目前该组织仍在持续优化其中间人攻击能力，甚至可能攻陷互联网服务提供商或边缘路由器，安全防护人员面临的对手正变得愈发难以追踪。

本文翻译自securityonline [原文链接](https://securityonline.info/evasive-panda-apt-hijacks-dictionary-com-and-app-updates-in-two-year-spree/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314062](/post/id/314062)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/evasive-panda-apt-hijacks-dictionary-com-and-app-updates-in-two-year-spree/)

如若转载,请注明出处： <https://securityonline.info/evasive-panda-apt-hijacks-dictionary-com-and-app-updates-in-two-year-spree/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [“莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据](/post/id/314059)

  2025-12-26 14:48:34
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