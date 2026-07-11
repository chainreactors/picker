---
title: 伊朗黑客组织亮出"秘密武器"：Cavern C2框架如何绕过所有安全检测
url: https://www.anquanke.com/post/id/315763
source: 安全客-有思想的安全新媒体
date: 2026-07-10
fetch_date: 2026-07-11T04:56:10.739678
---

# 伊朗黑客组织亮出"秘密武器"：Cavern C2框架如何绕过所有安全检测

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

# 伊朗黑客组织亮出"秘密武器"：Cavern C2框架如何绕过所有安全检测

阅读量**24942**

发布时间 : 2026-07-10 11:03:32

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

一个存在16年的漏洞利用链，一套让安全研究人员”无从下手”的反分析架构——当国家级APT开始把编译格式本身当作武器，传统的防御思路还管用吗？

# 1 发生了什么

2026年7月初，以色列网络安全公司Check Point Research披露了一份重磅报告：一个隶属于伊朗情报与安全部（MOIS）的黑客组织，正在使用一套全新模块化C2框架——**Cavern**（又名Cav3rn），持续攻击以色列的IT服务商和政府机构。

![]()

这个被Check Point追踪为”Cavern Manticore”的威胁组织，从2026年初就开始活跃。不同于以往伊朗系APT组织（如MuddyWater、OilRig）大量使用公开工具的做法，Cavern Manticore展现出了截然不同的技术路线：**整套框架完全基于.NET构建，但被刻意编译成三种不同的二进制格式**，迫使安全研究人员必须切换不同的工具链才能分析——而这，正是他们设计的核心。

更值得警惕的是，这套框架在VirusTotal上的检测率”几乎为零或极低”。换句话说，绝大多数主流安全产品拿它没什么办法。

# 2 技术解析：把”编译格式”变成反分析武器

Cavern框架最引人注目的地方，不在于它做了什么，而在于它**怎么隐藏自己做了什么**。

传统恶意软件的反分析手段，安全从业者已经很熟悉了：加壳、控制流平坦化、字符串加密。Cavern一个都没用。它的思路完全不同——**让每一种模块以不同的编译格式存在**，每种格式需要完全不同的逆向工具和工作流：

**第一种：.NET Framework（纯IL）**——包含mhm.dll（文件操作、DPAPI解密）、db.dll（SQL数据库操控）、ode.dll（Active Directory侦察）三个后渗透模块。用常规的.NET反编译工具就能看，但攻击者根本不在乎你看不看，因为每个模块运行在独立的AppDomain中，执行完毕就卸载，磁盘上不留可分析的组件。

**第二种：混合模式C++/CLI（IL+原生代码）**——这是Agent本体uxtheme.dll，伪装成Windows主题库，83个导出函数中82个是空壳（反沙箱陷阱），只有一个真正工作。

**第三种：.NET 8 Native AOT（纯原生）**——通信模块n-HTCommp.dll、网络侦察模块n-ten.dll、SOCKS5代理模块n-sws.dll。整个.NET运行时被静态编译进去，字符串只有在运行时才会”解冻”。Check Point不得不专门开发了一个IDA Pro插件，才能从这些二进制文件中恢复出元数据。

这种设计的实际效果是：**即使你发现了其中一个模块，分析它的经验无法复用到另一个模块上**。安全团队要同时维护三套分析能力，成本呈几何级增长。

Check Point在报告中写道：”框架的编译格式本身就成为了反分析层。”

# 3 攻击链条：从信任的IT服务商渗透进去

Cavern Manticore的入侵起点，不是什么高精尖的0day，而是一个更接地气的目标——**企业已经部署的远程监控和管理（RMM）软件**。

攻击链条大致如下：

攻击者先通过某种方式获得目标组织RMM系统的访问权限，然后滥用SysAid软件的合法更新功能，将恶意代码伪装成正常更新推送。一个WinDirStat的DLL侧加载链被部署到`C:\ProgramData\WinDir\`目录，合法的WinDirStat.exe加载被篡改的uxtheme.dll（Cavern Agent），Agent随即连接C2服务器`hospitalinstallation[.]com`，并通过HTTPS或WebSocket按需拉取后续攻击模块。

C2通信使用XOR密钥0x48加密，外层再套一层Base64编码，User-Agent固定为Edge浏览器，自定义`X-User-token`头部携带Agent ID。整个通信协议的字段用`_;;_`分隔，参数用`_,_`分隔——这种”方言”式的语法设计，也让流量特征检测更加困难。

值得注意的是，Agent具备**热更新能力**：它可以重命名自己的DLL文件，写入新版本，然后加载——整个过程不需要重启。启动后还会执行清理，删除除通信模块、配置和日志以外的所有文件。

攻击者的代码中甚至留下了带”个性”的错误信息：”What is this sh\*t?! where is get\_version?!?!”——Check Point的研究人员据此判断，这是一个具体的开发者，而非自动化代码生成器的产物。

# 4 事件影响：供应链信任正在被系统性武器化

这起事件最深层的信号，不在于某个技术细节有多精巧，而在于**攻击者对”信任关系”的利用方式**。

第一层信任滥用：IT服务商本身就是攻击入口。Cavern Manticore不直接攻击最终目标，而是先拿下目标使用的IT服务商，再通过服务商的RMM工具”合法地”跳转到真正的目标。这种”第二跳”甚至”第三跳”的攻击路径，让基于边界的防御模型几乎失效——你的安全团队很难区分”IT服务商正常推送的更新”和”攻击者伪装的更新”。

第二层信任滥用：合法软件被当作投毒载体。SysAid本身并没有被入侵，攻击者是先拿到了系统权限后，再利用它的更新功能来分发恶意代码。这意味着安全团队不能只盯着软件自身的漏洞，还得关注软件被攻陷后可能扮演的”帮凶”角色。

第三层，也是更宏观的一层：伊朗多个APT组织正在协同行动。与Cavern Manticore同时活跃的，还有同属MOIS体系的MuddyWater组织，后者正在对埃及、以色列、阿联酋的航空、能源和政府部门发起大规模侦察和渗透，已确认在多个受控环境中完成了敏感数据外泄。两个组织的同步活跃，指向伊朗在网络空间正在升级其攻击行动——这与当前以色列和美国对伊朗的军事行动形成了”镜像呼应”。

对于不在中东地区的组织来说，这起事件的启示同样直接：**你的IT服务商、MSP（托管服务提供商）、RMM工具，都可能成为国家级攻击者的跳板**。供应链安全不是一个抽象概念，而是一个需要落实到每一层信任关系中的具体工程。

# 5 防护建议

针对Cavern Manticore的攻击特征，以下是分层次的防护建议：

**1.IT服务商/MSP管理**

对IT服务商的远程管理权限实施最小化原则。RMM工具的更新推送机制需要额外验证——建议引入变更审批流程，关键更新需要双方确认。定期审计服务商对内部系统的访问记录，重点关注非常规时间段的更新推送行为。

**2.终端检测**

关注以下IOC（失陷指标）：

* C2域名：`hospitalinstallation[.]com`（及历史域名`adserviceupdate[.]com`、`hygienehistory[.]com`）
* 文件路径：`C:\ProgramData\WinDir\WinDirStat.exe`
* 互斥量：`MYMUTEX123HELLP02`、`MYMUTEX123HELLP04`
* 网络特征：固定Edge UA（Chrome/146.0.0.0 Edg/146.0.0.0）、自定义`X-User-token`头部、XOR密钥0x48

**3.网络流量监控**

对出站HTTPS和WebSocket连接实施更严格的审计，尤其是到非常见域名的加密连接。Cavern的C2通信虽然使用了加密，但其固定的User-Agent和自定义头部字段仍可作为检测锚点。

**4.DLL侧加载防护**

启用Windows的Code Integrity策略，限制非微软签名DLL的加载。对`ProgramData`等非特权目录中的可执行文件保持高度警觉。

# 6 写在最后

Cavern Manticore不是一个”更厉害的恶意软件”那么简单。它代表了一种趋势：**国家级攻击者正在从”工具对抗”转向”分析成本对抗”**。当一套框架的设计目标不是”让你检测不到”，而是”让你检测到了也分析不过来”时，传统的安全运营模型——依赖少数分析师手动逆向、手动提取规则——就面临根本性的挑战。

同时，这起事件也再次提醒我们：在供应链安全面前，没有” trustworthy “这三个字是绝对的。你信任的IT服务商、你依赖的远程管理工具、你习以为常的自动更新机制——每一环都可能被攻击者重新定义。

安全不是一个产品，是一种持续验证的过程。这句话说了很多年，但在Cavern Manticore面前，它从未如此具体。

---

**参考来源**：

1. Check Point Research, “Cavern Manticore: Exposing Iran-Linked Modular C2 Framework”, 2026年7月
2. The Hacker News, “Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations”, 2026年7月6日
3. OSINTSights / SecurityWeek / Infosecurity Magazine 相关报道

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315763](/post/id/315763)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **20**

* 粉丝
* **0**

### TA的文章

* ##### [智能体面临的十大安全风险问题](/post/id/315781)

  2026-07-10 20:48:53
* ##### [紧急！医疗巨头美敦力遭黑客入侵，患者隐私数据大规模外泄，这些坑普通人千万别踩](/post/id/315767)

  2026-07-10 11:07:46
* ##### [伊朗黑客组织亮出"秘密武器"：Cavern C2框架如何绕过所有安全检测](/post/id/315763)

  2026-07-10 11:03:32
* ##### [630GB机密挂上暗网：苹果二十年供应链铁幕一夜崩塌](/post/id/315760)

  2026-07-10 10:43:47
* ##### [【FDE前沿部署工程师】全国百城上岗计划二期来啦！](/post/id/315682)

  2026-07-07 23:19:12

### 相关文章

* ##### [深度分析Sorry勒索软件的加密实现与行为特征](/post/id/315390)

  2026-04-29 13:32:51
* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [虚假招聘陷阱 微软揭露针对开发者的传染性面试攻击活动](/post/id/315168)

  2026-03-13 10:31:36
* ##### [可变标签陷阱Xygeni GitHub Action高危漏洞危及CI/CD流水线](/post/id/315171)

  2026-03-13 10:31:09
* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37

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