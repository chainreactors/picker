---
title: 泰国财政部遭AI智能体攻陷！攻击基础设施全曝光
url: https://mp.weixin.qq.com/s/-A7T6HfmNac7FMmcqY0Gzg
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:01:41.982840
---

# 泰国财政部遭AI智能体攻陷！攻击基础设施全曝光

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hxdb7gjfn9nDP1ALLSDpaeunvgibmKAuVhZoajEHvHKS5lQqaOUqZRhe5hDrR6jd2HSrPHoicDrkEjEl8xLAibhl0wVPuOzlk33ibmdddRnLMaM/0?wx_fmt=jpeg)

# 泰国财政部遭AI智能体攻陷！攻击基础设施全曝光

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9m2poM9YgUAlThkkrbfb158I1dnian822OQCdGUziaREzBpD6yGwFsdS8sRnrib0MN9pT5j1LH32AMxDKjTztyUhfQBbEoGgF26Pk/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mhGZMIZZbpQ3Hds9QDM81ToGjaDCEXXj9icSGQV9IMFCBMJI4O0RBAzxHUNhw4YYia69OsDd6XoU449F5wXCn5QySYgVmIM5mtQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kBfNpd4sYUyVQGCzEPeKVKqv4m2o0xjiabhBoERymmic0p0hb9bboWk3lR2pJrvX1ibWBNRxcEFyRAk9qWcgIhYUjtJfWF33KAOs/640?wx_fmt=png&from=appmsg)

**安全厂商Hunt.io披露了一起针对泰国财政部的网络攻击行动，攻击者使用Hermes AI智能体和Hades恶意软件实施侦察并建立持久化控制；**

**由于攻击者的部分基础设施未设置权限暴露在公网，使得我们可以从中观察攻击者如何利用AI，此次攻击大量环节由Hermes自主完成，包括环境侦查、提权分析、工具利用、数据检索等。**

美国威胁情报厂商Hunt.io的研究人员发现一起针对泰国财政部的入侵事件，罕见地揭开了一场正在发生的网络行动的内幕。

研究团队并非像以往那样在事后恢复恶意软件，而是发现了暴露在公网上的攻击中转服务器，其中存放着攻击工具、被盗凭据、活动会话资料、AI智能体日志，以及一种此前未被公开记录、被命名为“Hades”的植入程序。

**研究结果表明，在相关基础设施被发现时，这场攻击行动仍在持续进行。**

**Hermes Agent自主攻击
泰国财政部多个系统沦陷**

此次调查由Hunt.io与安全研究员Bob Diachenko联合开展。他们追踪发现，攻击活动涉及一台托管于中国香港的服务器，其上有3个可公开访问的目录，于7月9日至7月13日期间暴露在公网上。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9mAicZ72EKDHcN8rH2CUywnH7jZyRNoROSKKHc8lMacmhqRleehLWviajfvDan0ib6dkFrL8FibWZpibICJK3u3ALVxwPr0zNsW2FcY/640?wx_fmt=png&from=appmsg)

**这些目录共包含近600个文件，包括漏洞利用代码、Web Shell、自定义脚本、编译后的植入程序，以及针对泰国财政部的凭据。**

调查人员还发现证据表明，攻击者已经成功访问了多个内部系统，不过最初的入侵路径目前仍不清楚。

此次行动最值得关注的一个方面，是攻击者使用了Hermes开源AI智能体。Hermes并非作为聊天机器人运行，而是充当攻击者的助手，能够在无需等待人工批准的情况下执行命令。

Hunt.io在发布的报告中写道：“此次针对泰国财政部的攻击，主要由运行于‘YOLO’模式下的AI智能体Hermes驱动。**活动会话Cookie文件、已部署的Web Shell以及内部网络访问记录均表明，攻击者已经成功攻陷了泰国财政部网络中的多个系统。**从我们审查的文档来看，其最初获得访问权限的方式尚无法立即确定。”

从暴露目录中恢复的日志来看，该框架运行于所谓的YOLO模式，即允许具有潜在危险的命令自动执行。恢复的日志显示，该AI智能体执行了权限提升检查、文件枚举、服务发现以及针对财政部系统的侦察任务。

这早已不是什么科幻场景，而是实实在在的攻击自动化。整件事唯一的破绽，就是有人忘了关闭目录列表。对防守方而言，这无疑是幸运的。

**从暴露基础设施分析攻击技战术**

暴露的基础设施中托管着一种Go语言恶意软件家族，研究人员将其命名为Hades。Windows版和Linux版共享同一套代码库，支持加密的命令与控制通信、持久化、交互式Shell、文件传输和SOCKS代理功能，Windows版本还额外支持傀儡进程和屏幕截图。运行时变量进一步暴露了其操作安全机制，例如可配置的工作时间和终止日期，用于降低植入程序被发现的概率。

调查结果描绘出一名攻击者投入大量精力研究财政部内部环境的画像。攻击者编写的自定义脚本专门针对Apache Hadoop基础设施中的HiveServer2，通过滥用默认身份验证机制以及恶意Hive用户自定义函数，执行操作系统命令。

报告继续写道：“专门编写的脚本针对泰国财政部的Hadoop基础设施，利用内置硬编码凭据的HiveServer2客户端以及恶意Hive UDF，通过WebHDFS执行命令并返回执行结果。”

另一套独立工具则针对Apache Ambari管理服务器、GlassFish管理控制台、内部Web应用、财政部邮件服务以及文档管理平台。研究人员还恢复了伪装成合法系统文件的Web Shell，以及用于验证邮箱凭据并复用活动Web会话的脚本。

攻击者还在基础设施中预先部署了权限提升能力。相关目录中包含多个知名漏洞的利用代码，包括PwnKit（CVE-2021-4034）、sudo堆溢出漏洞（CVE-2021-3156）以及长期存在的IIS WebDAV漏洞（CVE-2017-7269）。恢复的载荷表明，攻击者针对目标网络被攻陷后可能遇到的不同操作系统，准备了多种攻击方案。

研究人员还通过分析TLS证书特征以及嵌入在Hades中的命令与控制配置，进一步关联出更多攻击基础设施。分析发现了多台位于中国香港和马来西亚的相关服务器，这进一步证明，暴露出来的服务器只是整个攻击基础设施中的一个组成部分。

**AI如何重塑网络攻击行动**

Hermes日志或许提供了目前最清晰的证据，说明AI正在如何重塑攻击行动。攻击者不再需要手动执行每一条命令，而是将日常侦察任务交给AI智能体来完成。该智能体运行LinPEAS，搜索权限提升机会，遍历财政部目录，并整理财政部常务秘书办公室所属的文件。

Hunt.io指出，没有发现证据表明这些文件已经被窃取，但日志显示，攻击者正在系统性地扩大其在目标环境中的可见范围。

报告继续写道：“该智能体使用了开源项目LinPEAS，即Linux权限提升脚本，进一步在网络中横向移动。其他日志还显示，攻击者指示该智能体枚举一个内容目录，其中包含PDF、DOC、XLS文件以及与财政部常务秘书办公室相关的人事记录。目前没有证据表明这些文件已被窃取。”

除了具体的受害目标，这起事件还表明，AI智能体正在从实验性项目演变为切实可用的攻击工具。Hermes并没有编写钓鱼邮件，也没有生成恶意软件样本，而是承担了那些通常需要攻击者耗费大量时间完成的重复性工作，使键盘背后的操作者能够专注于价值更高的决策，而AI智能体则默默完成目标环境的测绘。这种能力将越来越多地出现在未来的入侵事件中，防御者应对此做好准备。

报告最后总结道：“这里的大多数工具我们此前都见过。真正不同的地方在于它们的组合方式：由AI智能体协调整个攻击流程，由跨平台植入程序维持访问权限，并针对这一特定目标编写了专用脚本。这些共同勾勒出一名为攻破单个政府目标而投入大量前期准备的攻击者形象。目前，其最初的入侵方式仍然未知。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9ns6ticOOnoFPdoffCq43GuicSzV7FkPNBKVicbrHdTdtV9ZSK6YLX0qjfhMRbbvYEich7teyYH7ibEkMrWXqRbPtDw1dg9ImLkvDrw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9k5ibQDx4Tus2vibd1pKeUcl4GbYk3T2nEshUib6icex4EatrBhhQqt9Lh45yyroyQEVIFtZupCiaibf6mywp1nvwj8kYv1pSf55Yf7Y/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：安全内参

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9licyPrcibWLRgTJt81oWvNTIppyUe7TIYIHomq1Kye7pAcGXosYAvdDibQKSVw4nGsPFvJ0ic3PhtEOI3oz6PtibWBghPlCqbVC9Sw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9lia3YGKngicQsSdCyrvHqxKtaxF4ib0r7ricHuopJ7DnlfD2IiaOUvbHicZjNEHtX56rDT2icrWywyLV8YubGHQ0hHt0MibNjAWwSnIQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9nRaicLMAP2lWIpHAzjbeYPYMf3MLfqk3rEkH2rMcIZ5wcMiaxIBn6Y0hmm6ZCwLWweicdiaXibLsciaw1vHhyDhPhm2iafgdByEoHvPk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1Y08O57sHWiaro9eC87veL2BfoUwAjnOfbTbGQwSaaunoz9m7KFdFkib1pMyMoNY4tVtskNSHickKmn7Nza8WGTeA/0?wx_fmt=png)

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