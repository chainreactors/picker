---
title: 安天AVL SDK反病毒引擎升级通告（20260627）
url: https://mp.weixin.qq.com/s/sRCmkjBZiFEPFfZOS6VfOw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:11:31.878358
---

# 安天AVL SDK反病毒引擎升级通告（20260627）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk9wVPJLBzt0IibJZK4RAuLwhsrPAN9S5wJNLcpGz5B3q0MTibnlyQycwtoDz8WiaHSibXhOPQBoKMvib465I3qWEe4ziaIcSswPTbicMg/0?wx_fmt=jpeg)

# 安天AVL SDK反病毒引擎升级通告（20260627）

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

统计周期：2026年06月20日~2026年06月26日

安天AVL SDK反病毒引擎本周共发布病毒库更新84次，日均更新12次，新增可检测恶意代码家族25个，新增可检测恶意代码变种5,992个，新增检测规则39,894条。

下表为新增可检的恶意代码家族TOP5清单：

|  |  |  |
| --- | --- | --- |
| **序号** | **病毒名** | **病毒描述** |
| 1 | Trojan/MSIL.BlankPage[Backdoor] | 该家族是一种木马病毒，通过欺骗用户或携带其他恶意软件来进入受害者的计算机系统。一旦感染，会在后台运行并以隐藏的方式窃取敏感信息，监视用户的活动并向远程服务器发送数据。 |
| 2 | Trojan/Win64.Redicab[Exploit] | 该家族是一种木马病毒，通过网络传播，具有隐蔽性和破坏力强的特点, 借用系统漏洞、社会工程等方式侵入目标主机，然后在后台潜伏，进行恶意操作。 |
| 3 | Trojan/MSIL.ScreenCapture | 该家族是一种木马病毒，主要利用系统漏洞进行传播和感染，该病毒通过伪装成正常软件或隐藏在破解程序、盗版软件中诱骗用户下载执行，窃取用户的敏感信息，包括银行账户、密码、个人身份信息等重要数据。 |
| 4 | Trojan/Win32.DarkIcon | 该家族是一种木马病毒，主要通过木马程序的方式潜伏在计算机系统中，监视用户的键盘输入和屏幕操作，记录敏感信息如账号、密码等。 |
| 5 | Trojan/JS.NpmSteal[PSW] | 该家族是一种木马病毒，恶意程序会绕过证书校验连接攻击者 C2 服务器，窃取各类研发密钥、账号凭证、加密货币钱包数据，并在 Windows、macOS、Linux 全平台建立持久化后门。 |

（按照周期内家族样本HASH数统计）

**更多相关内容请访问计算机病毒百科****virusview.net**

![](https://mmbiz.qpic.cn/mmbiz_jpg/krU5D4C1q6Q7oIpWcyiaZsj6MYu7l3pTtLZGR8fJ0krvTjbD0WpG4IlXS4Hv4p6ibC4G1b1Ej6aLh7E5LjTjWpvA/640?wx_fmt=jpeg&from=appmsg)

（长按识别二维码查看更多病毒信息）

**2**

**检测能力全集情况**

截至2026年06月26日24:00，AVL SDK反病毒引擎可检出分布在8个基础分类，58,020个恶意代码家族的18,609,487个恶意代码变种、总检测规则数42,133,900条。

按照恶意代码分类统计检测能力和规则条数如下：

|  |  |  |
| --- | --- | --- |
| 恶意代码分类 | **可检测恶意代码（种）** | **检测规则（条）** |
| 感染式病毒 | 59,667 | 6,823,419 |
| 蠕虫 | 315,512 | 3,949,291 |
| 木马 | 13,552,754 | 25,732,543 |
| 黑客工具 | 458,670 | 366,254 |
| 风险工具 | 1,206,932 | 2,241,325 |
| 流氓软件 | 3,015,914 | 3,019,882 |
| 垃圾文件 | 11 | 1,081 |
| 测试程序（自检用） | 27 | 105 |
| 合计 | 18,609,487 | 42,133,900 |

**预处理能力（部分）：**

可脱壳种类数31种（精确到种类），可拆解包裹数132个，含全部常见包裹和自解压包。

**配套知识输出能力：**

针对恶意代码载荷，配套使用AVL SDK恶意代码知识库，具备533种ATT&CK关键行为范式，覆盖ATT&CK技术标签171个，覆盖度64.29%，基本上覆盖了ATT&CK框架中的可静态检测的标签数量。

**3**

**本周需重点防范病毒家族**

本周持续警惕AI 开源供应链投毒安全风险。近期 Mastra AI 生态爆发大规模 npm 供应链投毒攻击，威胁全面覆盖企业本地开发终端、项目依赖库管理、自动化 CI/CD 构建流水线全环节。攻击者盗用项目维护账号，仿冒知名 dayjs 库投放恶意依赖包，用户执行 npm 安装操作时会自动触发 postinstall 钩子执行窃密恶意载荷（Trojan/JS.NpmSteal[PSW]）；恶意程序会绕过证书校验连接攻击者 C2 服务器，窃取各类研发密钥、账号凭证、加密货币钱包数据，并在 Windows、macOS、Linux 全平台建立持久化后门，极易造成企业源码、核心业务数据泄露。请相关用户排查项目依赖、落实安全加固。

视频：Trojan/JS.NpmSteal[PSW]木马视频形象

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

[安天AVL SDK反病毒引擎升级通告（20260620）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214982&idx=1&sn=27b7b4b89626e1ec228c6e21cd08991b&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260613）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214901&idx=1&sn=a0897e60f6ba77999d2a77987c700713&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260606）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214872&idx=2&sn=619a01948ed8b3376dd5ac65935d5f45&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260530）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214831&idx=1&sn=56c1b33a6511f32b2d0703df9aa86536&scene=21#wechat_redirect)

[安天AVL SDK反病毒引擎升级通告（20260523）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214768&idx=1&sn=48d5c7d08f8436b80b62a33d6f141600&scene=21#wechat_redirect)

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