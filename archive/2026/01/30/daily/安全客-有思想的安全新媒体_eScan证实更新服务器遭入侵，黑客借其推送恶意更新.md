---
title: eScan证实更新服务器遭入侵，黑客借其推送恶意更新
url: https://www.anquanke.com/post/id/314627
source: 安全客-有思想的安全新媒体
date: 2026-01-30
fetch_date: 2026-01-31T04:03:08.544850
---

# eScan证实更新服务器遭入侵，黑客借其推送恶意更新

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

# eScan证实更新服务器遭入侵，黑客借其推送恶意更新

阅读量**24217**

发布时间 : 2026-01-30 11:27:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/escan-confirms-update-server-breached-to-push-malicious-update/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

eScan 杀毒软件开发商**微世界科技（MicroWorld Technologies）** 已正式证实，其旗下一台更新服务器本月初遭黑客入侵，黑客利用该服务器向一小部分用户推送了未经授权的更新程序，后续分析证实该程序为恶意文件。

2026 年 1 月 20 日，在长达两小时的时间窗口内，从该区域更新服务器集群下载更新的用户均收到了这一恶意文件。

eScan 方面表示，涉事的服务器基础设施已完成隔离与重建，相关身份认证凭证也已完成更换，同时已为受影响用户提供了对应的安全修复方案。

安全厂商**Morphisec**也单独发布了一份技术报告，分析了在客户终端监测到的恶意活动，该机构确认这些活动与同一时间段内从 eScan 更新服务器推送的更新程序直接相关。

Morphisec 称其于 2026 年 1 月 20 日检测到相关恶意活动，随后联系了 eScan。但微世界科技向科技媒体 BleepingComputer 表示，该公司对 Morphisec 宣称**自身为首个发现并上报该事件**的说法存在异议。

eScan 方面给出的说法是，公司已于 1 月 20 日通过系统监控和用户反馈内部发现了该问题，并在数小时内完成了涉事基础设施的隔离，且于 1 月 21 日发布了安全预警公告。eScan 还指出，Morphisec 是在公开发布该事件相关声明后，才联系了公司。

对于 “受影响用户对该事件毫不知情” 的说法，eScan 同样予以否认，称其在安全修复方案敲定期间，已主动向受影响用户发送通知并进行了一对一沟通。

### 更新服务器遭非法入侵

eScan 在其安全预警公告中将该事件定性为**更新基础设施访问入侵事件**，表示黑客通过非法访问某区域更新服务器的配置信息，在更新分发路径中植入了未经授权的文件。

微世界科技向 BleepingComputer 提供的公告中写道：“黑客非法访问了我们某台区域更新服务器的配置，导致一个异常文件（补丁配置二进制文件 / 恶意损坏更新包）被植入更新分发路径。”

“2026 年 1 月 20 日的特定时间段内，从该受影响服务器集群下载更新的用户，均接收到了该文件。”

该公司强调，此次事件**并非因 eScan 杀毒软件自身存在漏洞**所致。

eScan 还明确，仅有从该特定区域服务器集群完成软件更新的用户受到影响，其余所有用户均未波及。

不过 eScan 表示，安装了该恶意更新程序的用户，其设备可能出现以下异常现象：

* 更新服务故障提示
* 系统 hosts 文件被篡改，导致无法连接 eScan 更新服务器
* eScan 更新配置文件被修改
* 无法接收新的病毒库安全定义更新
* 客户端设备弹出更新服务不可用的提示窗口

BleepingComputer 已向 eScan 进一步求证其服务器最初遭入侵的具体时间，若收到回复将第一时间更新相关报道。

### 恶意更新被用于投放恶意软件

Morphisec 在其安全公告中指出，此次黑客推送的恶意更新程序，植入了经篡改的 eScan 更新组件**Reload.exe**。

该公告中写道：“黑客通过 eScan 合法的更新基础设施分发恶意更新程序，导致全球范围内的企业和个人终端设备均被植入了多阶段恶意软件。”

尽管这一经篡改的 Reload.exe 文件，表面上带有看似属于 eScan 的代码签名证书，但 Windows 系统和病毒检测平台 VirusTotal 均判定该签名**无效**。

Morphisec 表示，这款恶意 Reload.exe 文件（可在 VirusTotal 查询）被黑客用于实现**恶意程序持久化驻留**、执行恶意命令、篡改 Windows HOSTS 文件以阻止设备进行远程更新，同时连接黑客的**命令与控制（C2）服务器**，下载更多恶意载荷。

研究人员公布了监测到的以下黑客命令与控制服务器地址：

hxxps [://] vhs [.] delrosal [.] net/i

hxxps [://] tumama [.] hns [.] to

hxxps [://] blackice [.] sol-domain [.] org

hxxps [://] codegiant [.] io/dd/dd/dd [.] git/download/main/middleware [.] ts

504e1a42.host.njalla [.] net

185.241.208 [.] 115

研究人员发现，黑客最终向受感染设备投放的恶意载荷为一个名为**CONSCTLX.exe**的文件（可在 VirusTotal 查询），Morphisec 确认该文件是一款**后门程序**，同时具备持久化下载恶意文件的功能。该机构还表示，这些恶意文件会创建计划任务以实现持久化驻留，任务名称伪装为**CorelDefrag**等正常名称。

目前 eScan 已推出一款修复性更新程序，用户运行后可自动完成以下操作：

1. 自动识别并修正被篡改的系统配置
2. 恢复 eScan 更新服务的正常功能
3. 验证系统是否成功恢复
4. 操作完成后需重启系统（常规重启即可）

eScan 与 Morphisec 均建议用户，为提升设备安全性，**屏蔽上述所有黑客命令与控制服务器地址**。

值得注意的是，2024 年曾有相关监测显示，朝鲜黑客组织曾利用 eScan 杀毒软件的更新机制，在企业网络中植入后门程序。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/escan-confirms-update-server-breached-to-push-malicious-update/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314627](/post/id/314627)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/escan-confirms-update-server-breached-to-push-malicious-update/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/escan-confirms-update-server-breached-to-push-malicious-update/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **980**

* 粉丝
* **6**

### TA的文章

* ##### [筑牢聊天安全防线：WhatsApp推出 “严格模式” 抵御飞马间谍软件](/post/id/314636)

  2026-01-30 11:28:04
* ##### [CVE-2026-24765：PHPUnit漏洞致CI/CD流水线面临远程代码执行风险](/post/id/314611)

  2026-01-30 11:27:56
* ##### [假意网恋设局，实为安卓间谍软件植入](/post/id/314629)

  2026-01-30 11:27:37
* ##### [重登AI存储王座？三星新一代HBM4即将通过英伟达关键认证，行业格局或将改写](/post/id/314606)

  2026-01-30 11:27:26
* ##### [eScan证实更新服务器遭入侵，黑客借其推送恶意更新](/post/id/314627)

  2026-01-30 11:27:07

### 相关文章

* ##### [筑牢聊天安全防线：WhatsApp推出 “严格模式” 抵御飞马间谍软件](/post/id/314636)

  2026-01-30 11:28:04
* ##### [CVE-2026-24765：PHPUnit漏洞致CI/CD流水线面临远程代码执行风险](/post/id/314611)

  2026-01-30 11:27:56
* ##### [假意网恋设局，实为安卓间谍软件植入](/post/id/314629)

  2026-01-30 11:27:37
* ##### [重登AI存储王座？三星新一代HBM4即将通过英伟达关键认证，行业格局或将改写](/post/id/314606)

  2026-01-30 11:27:26
* ##### [仿冒AI助手：恶意程序ClawdBot以插件形式藏身VS Code，实为特洛伊木马](/post/id/314625)

  2026-01-30 11:26:48
* ##### [信号基金会总裁警示：人工智能代理正让加密技术丧失实际效用](/post/id/314609)

  2026-01-30 11:26:44
* ##### [社会工程学黑客盯上Okta单点登录系统](/post/id/314615)

  2026-01-30 11:26:00

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