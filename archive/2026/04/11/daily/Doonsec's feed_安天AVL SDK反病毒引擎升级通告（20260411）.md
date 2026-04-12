---
title: 安天AVL SDK反病毒引擎升级通告（20260411）
url: https://mp.weixin.qq.com/s/1zCnh-4dVe1tHuZB4-R0Lg
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:46:26.127073
---

# 安天AVL SDK反病毒引擎升级通告（20260411）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicgRK6pPBaUGS30k3eqS4qAia6XQBpGSJ0KRqwkEdHJX5BicOVuvwKHz6bn6Tf6o1LCWqibA1yXk5Jl4pcfl3nVeZHcXw1z3S7n20/0?wx_fmt=jpeg)

# 安天AVL SDK反病毒引擎升级通告（20260411）

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

本着**安全能力透明化，易达、易用、可验、可感**的原则，安天每周对公众公布AVL SDK反病毒引擎周度更新和能力全集情况。

**1**

**周度更新****情况**

统计周期：2026年04月04日~2026年04月10日

安天AVL SDK反病毒引擎本周共发布病毒库更新84次，日均更新12次，新增可检测恶意代码家族27个，新增可检测恶意代码变种5,107个，新增检测规则17,390条。

下表为新增可检的恶意代码家族TOP5清单：

|  |  |  |
| --- | --- | --- |
| **序号** | **病毒名** | **病毒描述** |
| 1 | Trojan/Win32.DeviceDisabler | 该家族是一种木马病毒，主要通过捆绑在看似合法的软件、钓鱼邮件附件或恶意网站链接中传播，主要目的是渗透用户系统，窃取敏感信息（如银行账户、密码、个人身份信息）并建立后门以供远程攻击者控制。 |
| 2 | Trojan/Linux.MikeDor[Backdoor] | 该家族是一种木马病毒，通过欺骗用户或携带其他恶意软件来进入受害者的计算机系统。一旦感染，会在后台运行并以隐藏的方式窃取敏感信息，监视用户的活动并向远程服务器发送数据。 |
| 3 | Trojan/Win64.Shirna[Ransom] | 该家族是一种木马病毒，通常通过钓鱼邮件、恶意下载或漏洞利用等方式传播。一旦感染，该恶意软件会加密用户的文件，并要求支付赎金以获取解密密钥，对计算机系统造成严重威胁。 |
| 4 | Trojan/JS.SilentStealer[PSW] | 该家族是一种木马病毒，主要通过钓鱼邮件、恶意下载链接或软件携带等方式传播，在感染用户计算机后会隐藏自身并窃取用户敏感信息，如账号密码、银行卡信息等，从而危害用户隐私安全。 |
| 5 | Trojan/MacOS.Bezdez | 该家族是一种针对MacOS系统的木马病毒，通过欺骗用户或携带其他恶意软件来进入受害者的计算机系统。一旦感染，会在后台运行并以隐藏的方式窃取敏感信息，监视用户的活动并向远程服务器发送数据。 |

（按照周期内家族样本HASH数统计）

**更多相关内容请访问计算机病毒百科****virusview.net**

![](https://mmbiz.qpic.cn/mmbiz_jpg/krU5D4C1q6Q7oIpWcyiaZsj6MYu7l3pTtLZGR8fJ0krvTjbD0WpG4IlXS4Hv4p6ibC4G1b1Ej6aLh7E5LjTjWpvA/640?wx_fmt=jpeg&from=appmsg)

（长按识别二维码查看更多病毒信息）

**2**

**检测能力全集情况**

截至2026年04月10日24:00，AVL SDK反病毒引擎可检出分布在8个基础分类，57,692个恶意代码家族的18,538,008个恶意代码变种、总检测规则数41,787,279条。

按照恶意代码分类统计检测能力和规则条数如下：

|  |  |  |
| --- | --- | --- |
| 恶意代码分类 | **可检测恶意代码（种）** | **检测规则（条）** |
| 感染式病毒 | 59,598 | 6,806,427 |
| 蠕虫 | 314,636 | 3,938,468 |
| 木马 | 13,486,873 | 25,467,742 |
| 黑客工具 | 457,125 | 362,224 |
| 风险工具 | 1,205,582 | 2,213,064 |
| 流氓软件 | 3,014,157 | 2,998,177 |
| 垃圾文件 | 11 | 1,078 |
| 测试程序（自检用） | 26 | 99 |
| 合计 | 18,538,008 | 41,787,279 |

**预处理能力（部分）：**

可脱壳种类数31种（精确到种类），可拆解包裹数132个，含全部常见包裹和自解压包。

**配套知识输出能力：**

针对恶意代码载荷，配套使用AVL SDK配套恶意代码知识库，具备533种ATT&CK关键行为范式，覆盖ATT&CK技术标签171个，覆盖度64.29%，基本上覆盖了ATT&CK框架中的全部可静态检测的标签数量。

**3**

**本周需重点防范病毒家族**

本周需重点关注开源AI生态仿冒投毒风险攻击。近段时间，开源AI生态仿冒投毒风险呈现剧烈增长趋势，OpenClaw（龙虾）成为攻击者重点狙击目标，短期内已出现多起仿冒事件，下载载荷为游蛇木马。攻击者注册与官方高度近似的域名，搭建界面、Logo以及功能介绍完全复刻的被仿冒站点，并利用搜索引擎SEO技术精准诱导用户点击下载，下载后的安装包内嵌游蛇家族变种后门。近期钓鱼的游蛇家族手法主要为利用伪装成图片文件的加密载荷执行Shellcode并最终执行远控木马与C2服务器建立连接。

视频：SwimSnake木马视频形象
（安天AMPS网安文化工作室利用大模型创作）

防护建议

针对该病毒，安天建议采取如下防护措施:

（1）安装终端反病毒软件：推荐使用[安天智甲终端防护系统](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650205228&idx=3&sn=72473850250f89f2d1b2896b6e5fa702&scene=21#wechat_redirect)等使用AVL SDK引擎的主机杀毒和防护产品。推荐安天智甲用户开启勒索病毒防御工具模块（默认开启）；

（2）加强口令强度：避免使用弱口令，建议使用16位或更长的密码，包括大小写字母、数字和符号在内的组合，同时避免多个服务器使用相同口令；

（3）定期更改口令：定期更改系统口令，避免出现口令泄露导致系统遭到入侵；

（4）及时更新补丁：建议开启自动更新功能安装系统补丁，服务器、数据库、中间件等易受攻击部分应及时更新系统补丁；

（5）关闭高危端口：对外服务采取最小化原则，关闭3389、445、139、135等不用的高危端口；

（6）邮件安全：谨慎处理可疑邮件，避免下载不明附件或点击陌生链接；

（7）关闭PowerShell：如不使用PowerShell命令行工具，建议将其关闭；

（8）定期数据备份：定期对重要文件进行数据备份，备份数据应与主机隔离。

**安天应急响应服务**

安天持续赋能用户构筑有效勒索攻击安全防护体系，达成有效安全价值。

全国服务热线：400-840-9234

服务支持邮箱：support@antiy.cn

**警惕新型威胁，筑牢数据防线！**

**安天AVL SDK反病毒引擎简介**

安天AVL SDK反病毒引擎是安天面向全体系结构和系统平台所研发的威胁检测能力中间件。安天产品和使用生态伙伴产品通过嵌入AVL SDK获得病毒和恶意代码检测能力，并通过病毒库获得持续更新。

针对感染式病毒、蠕虫、木马、黑客工具、灰色软件、风险软件、垃圾文件、测试文件八个恶意代码分类，超过5万个家族和1800万个恶意代码变种进行精准识别检测，检测能力完整覆盖全量已知恶意代码，严格遵守CARO公约，输出由分类、环境、家族组成结构化分节命名，并基于恶意样本的行为能力输出并针对加密勒索、窃密、远控、僵尸程序、挖矿等典型恶意行为输出近百种恶意行为标签。安天引擎可识别超过300种文件格式，并对PE、ELF等编译可执行格式进行深度预处理，对各种包裹（含自解压包裹进行递归解压）、对OFFICE、ACAD等可嵌入脚本或有溢出风险格式的复合文档进行结构解析。从而确保对恶意代码对抗具有较高的鲁棒性，安天引擎同时带有可信文件签名库，支持产品基于黑白双控的方式实现安全策略，全面提升攻击者的难度。

安天检测能力可以全量本地部署，安天每日平均自动化分析处理超过200万新增文件对象，每两小时发布一次病毒库更新。同时也开放云查杀、云分析和计算机病毒百科等支撑服务。

安天AVL SDK有传统PC主机、智能终端、网络流量、信创系统、工业系统、无人系统等版本，面向主机系统和工作负载安全、网络流量安全、业务流转安全、邮件和文件服务安全等场景提供威胁检测能力。全面支持X86、ARM、MIPS（含Cavium）、RISC、PowerPC等各种体系架构，支持包括国产操作系统、Linux、Windows等多种主流操作系统和Vxwork等实时工业操作系统，支持骨干网场景的高速检测。

安天AVL SDK引擎为超过100家业内伙伴提供引擎赋能，除安天自身产品部署外，安天引擎已经累计覆盖超过40亿个节点（包括手机终端、信创PC终端、云原生节点、网络设备、网络安全设备等），为手机和智能终端提供内生安全检测能力。使用安天引擎的主要合作伙伴包括华为、小米、荣耀、VIVO、OPPO等手机企业，蚂蚁金服等大型互联网企业和多家网络安全上市企业。使用安天引擎的合作伙伴产品曾获得AV-TEST和NSS Labs等国际知名评测奖项。AVL SDK的 “L战斧”标志，已经成为可靠杀毒能力的象征。

安天全线产品包括但不限于[智甲系统安全防护系统](http://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650179641&idx=1&sn=bdcea68a6fd0fca0f0be4b4f48431499&chksm=beb92b0b89cea21d3a8661e0007a7bd5c7901086fa96b39b420532eedd67e8b98e787ad57a3a&scene=21#wechat_redirect)产品家族、[睿甲主机安全检测响应系统](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650205220&idx=2&sn=200c1a6d585126d346b58bf4541611cd&scene=21#wechat_redirect)、[探海威胁检测系统](http://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650179614&idx=1&sn=f23da1aa858aa4ed11c56717b739fbc7&chksm=beb92b2c89cea23a7a6ac6d1249633d57c37e13bd7914191e03f394f3a150ccaf617f6a80b88&scene=21#wechat_redirect)、[追影威胁分析系统](http://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650179603&idx=1&sn=7c5059ec431f5a88db2bf6edf937a881&chksm=beb92b2189cea23753ad8fabcce5bf5c8c5adac2798df764a8ebf0aa3faa63a151d5c6832105&scene=21#wechat_redirect)、[捕风蜜罐系统](http://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650179615&idx=1&sn=6b7cce69f5d660ade852493b9bfe5061&chksm=beb92b2d89cea23bb27a6b35d81f8bb59ff52b2e6eb68a1deccd03c280085379d51347c37c8d&scene=21#wechat_redirect)、青竹智语WAF等均使用安天反病毒引擎。

AVL SDK反病毒引擎从2001年开始研发，历经多个重大版本迭代升级。先后获得科技部中小企业创新基金（2004）、科技部863（2006）、发改委信息安全专项（2008）、工信部工程专项（2019）支持，AVL SDK移动版曾获得[2014年度AV-TEST移动设备最佳保护奖](http://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=200018171&idx=1&sn=2397d3f8434ad55e6393e267619c18a7&chksm=28a3abc91fd422df67b5105fa2862c611941ab722c2656192af14a79d715cf09ff97a6545e27&scene=21#wechat_redirect)，使用AVL SDK的安天探海、追影产品曾蝉联国家网络安全应急技术处理协调中心主办的第一届、第二届[网络安全技术对抗赛第一名](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650174170&idx=1&sn=261153d1b5ca46329e4b5594c63dad7b&scene=21#wechat_redirect)。

**往期推荐:**

[安天AVL SDK反病毒引擎升级通告（20260404）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214438&idx=1&sn=e7aa23f29bade3c90c876c85b7af15cc&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260328）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214338&idx=1&sn=8421f04239da5258a77685616139a955&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260321）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214249&idx=1&sn=1791774f5fb08c32d2a3dede9c2f092b&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260314）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214070&idx=1&sn=d83145209bd60d7f3b058b7191446a85&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260307）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650213955&idx=1&sn=448a2fd990fd2080a4c3cffafee367a5&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

安天集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

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