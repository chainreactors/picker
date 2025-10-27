---
title: 活跃的RansomHub勒索攻击组织情况分析
url: https://www.4hou.com/posts/Ey0N
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-14
fetch_date: 2025-10-06T18:24:28.763095
---

# 活跃的RansomHub勒索攻击组织情况分析

活跃的RansomHub勒索攻击组织情况分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 活跃的RansomHub勒索攻击组织情况分析

安天
[技术](https://www.4hou.com/category/technology)
2024-09-13 15:41:07

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)89720

收藏

导语：目前，尚未发现能够成功解密其加密数据的有效工具。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211984167846.jpg "1726211984167846.jpg")

**1 概述**

RansomHub勒索攻击组织被发现于2024年2月，自出现以来持续活跃，采用勒索软件即服务（RaaS）模式运营，通过“窃取文件+加密数据”双重勒索策略对受害者实施侵害。目前，尚未发现能够成功解密其加密数据的有效工具。该组织利用特定方式公开受害者的敏感信息，并以此为要挟，迫使受害者支付赎金或满足其他非法要求，以避免其数据被进一步泄露或出售。截至2024年9月12日，该组织所使用的信息发布站点共有227名受害者信息，实际受害者数量会更多，因为攻击者出于某些原因可能选择不公开或删除信息，例如在与受害者进行协商谈判并达成一致后，或者受害者支付了赎金以换取信息的删除。

**RansomHub勒索攻击组织使用的攻击技战术与Knight勒索攻击组织有着显著的相似之处**。此外，**它与曾经在勒索攻击领域活跃但现已退出的BlackCat（又名ALPHV）组织似乎存在某种联系**。在最近发现的攻击事件中，**RansomHub组织表现出了利用高级持续性威胁（Advanced Persistent Threat,APT）组织常用的技战术来执行勒索攻击的能力**。因此，RansomHub组织的背景错综复杂，究竟是“集万恶于一身”还是“另立山头”，目前尚未明确，这些推测指向了一个复杂的网络犯罪生态系统，其中攻击者之间的界限可能远比表面看起来的要模糊。

**2 组织背景**

2024年2月，暗网监控云服务商ParanoidLab发现名为“koley”的用户在黑客论坛发布关于RansomHub勒索攻击组织RaaS的相关计划[1]，用于招揽附属成员，包括勒索赎金分赃比例、加密工具特性和部分规则等内容。

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211921154428.png "1726211921154428.png")

图 2‑1 RansomHub组织RaaS计划

2023年5月，Cyclops勒索攻击组织首次出现在公众视野中，同年7月更名为Knight。2024年2月，有关该组织成员在黑客论坛上公开销售其核心源代码的消息被披露[2]。与此同时，RansomHub勒索攻击组织在同一月份被发现，其使用的勒索软件载荷和技战术与Knight有着显著的相似之处[3]，而且这两个组织的成员在论坛中注册时间点相同。这种相似性不难引发猜测，包括以下几种可能性：RansomHub可能采用了Knight的源代码；或者，Knight的一部分原成员可能已经转投RansomHub；又或者，Knight可能进行了一次品牌重塑，以RansomHub的新身份继续其网络犯罪行为。

![2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211907951022.png "1726211907951022.png")

图 2‑2 Knight组织出售代码

2024年2月，美国医疗保健行业的巨头Change Healthcare不幸成为BlackCat勒索攻击组织成员“Notchy”所发动攻击的目标[4]。这次攻击导致公司的部分业务系统遭到加密，还使得数以TB计的敏感数据被窃。面对这种情况，Change Healthcare在3月初做出了支付赎金的决定，总额约2200万美元，这是为了确保公司的数据能够恢复，并且防止被盗数据被进一步泄露或在黑市上出售。但成员“Notchy”表示受害者支付赎金后并未收到自己应得的分成部分，全额赎金都被BlackCat管理人员扣押。随后，BlackCat管理人员在黑客论坛中表示BlackCat这一品牌退出勒索市场[5]，其代码已出售。4月，“Notchy”将窃取到的数据转移到RansomHub勒索攻击组织并继续勒索Change Healthcare。种种行径不禁让人心生疑窦，是否是其自导自演的一出戏，以此来误导公众，让外界相信BlackCat真的退出了勒索软件市场，抑或是换了个名头，继续为非作歹。

**·勒索软件样本部分**

RansomHub勒索软件样本通过C++和Go语言进行编写，为干扰安全人员分析，代码段利用特定方式进行混淆。勒索软件样本执行前提需读取特定json文件，若读取失败则无法执行样本。这一技术手段与BlackCat勒索软件存在相似点[6]。

勒索载荷执行时需读取前置json文件，根据json文件中预设的字段信息实现不同功能。

![2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211887858835.png "1726211887858835.png")

图 2‑3 json文件中的功能字段

根据json文件内的字段设定，结合勒索软件部分特性猜测其对应功能，具体信息见下表：

表 2‑1 json内字段及对应功能信息表

|  |  |  |  |
| --- | --- | --- | --- |
| 字段 | 对应功能 | 字段 | 对应功能 |
| extension | 被加密文件的后缀名 | net spread | 网络传播 |
| local disks | 本地磁盘加密 | running one | 只执行一次 |
| self delete | 自删除 | white files | 不加密的文件 |
| white hosts | 不加密的主机 | credentials | 用于访问的凭证信息 |
| kill services | 结束特定服务 | set wallpaper | 设置桌面背景 |
| white folders | 不加密的目录 | note file name | 勒索信名称 |
| note full text | 完整勒索信内容 | kill processes | 结束特定进程 |
| network shares | 网络共享加密 | note short text | 简短勒索信内容 |
| master public key | 用于加密的主公钥 |  |  |

在勒索软件功能这部分，RansomHub与Knight均支持通过命令行模式选择不同选项，从而实现不同功能，且部分模式与对应字段均相同。

![2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211865146678.png "1726211865146678.png")

图 2‑4 RansomHub与Knight部分功能对比

RansomHub勒索攻击组织近期利用自带易受攻击的驱动程序（Bring Your Own Vulnerable Driver,BYOVD）技术开展勒索攻击。攻击者利用此类技术将存在安全漏洞的合法驱动程序植入目标系统，这些驱动程序由于拥有合法的数字签名，往往能够逃避安全软件的审查，从而不被标记或阻止。这些驱动程序，尤其是内核模式的驱动程序，一旦被成功利用，便能为攻击者提供一种手段，以实现对目标系统的内核级权限提升。这种权限提升不仅赋予攻击者对系统资源的全面访问权，还使他们能够对端点安全软件进行禁用或规避其检测，从而在目标系统中肆意进行各种恶意活动。

值得注意的是，这种策略并非RansomHub的独创，包括Lazarus和Lamberts在内的一些APT组织，也曾使用过类似的技术开展攻击活动。此外，BlackCat、Cuba和LockBit[7]等勒索攻击组织也纷纷效仿，利用这种手段实施勒索攻击。正如安天在2021年发布的《网络安全威胁的回顾与展望》[8]中所提到的，部分勒索攻击能力已经达到“APT”水平。

**3 受害者信息发布平台**

RansomHub组织将其受害者的信息发布在特定的Tor网络地址上。每个受害者都有自己独立的信息展示区。该组织根据是否已经公开了窃取的数据，将受害者的状态分为两种：“未公开”（倒计时状态）和“已公开”（PUBLISHED）。在每个受害者的状态信息下方，还详细列出了包括被浏览次数（Visits）、窃取数据的总量（Data Size）、最后更新时间（Last View）以及受害者信息首次发布的时间等关键信息。

![3-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211846679747.png "1726211846679747.png")

图 3‑1 发布受害者信息的Tor页面

如下图所示，该受害者信息栏表示当前从受害者窃取到的数据已公开，已被浏览2585次，窃取数据50 GB，上次更新时间：8月26日03:30:27 UTC，最初发布时间为8月21日12:03:03 UTC。

![3-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211833106546.png "1726211833106546.png")

图 3‑2 受害者信息状态

进入信息栏中可以看到对受害者的简介，部分窃取到的数据示例和用于下载已公开数据的地址等信息。

![3-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211816648951.png "1726211816648951.png")

图 3‑3  受害者信息及数据下载地址

该组织还采用拍卖的方式出售窃取到的数据。

![3-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211806138525.png "1726211806138525.png")

图 3‑4 采用拍卖的形式出售数据

关于页面的内容为该组织相关介绍和一些条例。

![3-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211788304843.png "1726211788304843.png")

图 3‑5 Tor网站中组织介绍

联系页面的内容为该组织对受害者和想成为附属成员预留的内容。

![3-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211748157902.png "1726211748157902.png")

图 3‑6 Tor网站中联系信息

**4 防护建议**

建议企业用户部署专业的终端安全防护产品，对本地新增和启动文件进行实时检测，并周期性进行网内病毒扫描。安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀本次发现病毒样本。

智甲具备内核级防护能力，基于内核驱动持续监控进程等内存对象操作行为动作，研判是否存在持久化、提权、信息窃取等攻击动作，并且结合勒索行为特征库检测，可分析进程行为是否疑似勒索攻击行为，对发现的勒索攻击可在第一时间进行阻断。

![4-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211719477057.png "1726211719477057.png")

图 4‑1 发现病毒时，智甲第一时间拦截并发送告警

智甲还为用户提供统一管理平台，管理员可通过平台集中查看网内威胁事件详情，并批量进行处置，提高终端安全运维效率。

![4-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726211705595671.png "1726211705595671.png")

图 4‑2通过智甲管理中心查看并完成威胁事件处置

**5 参考链接**

[1] ParanoidLab.ParanoidLab spotted RansomHub, a new Ransomware as a Service (RaaS) on the Dark Web.(2024-02-02)

https://www.linkedin.com/feed/update/urn:li:activity:7159288343535484928/

[2] BleepingComputer.Knight ransomware source code for sale after leak site shuts down [R/OL].(2024-02-20)

https://www.bleepingcomputer.com/news/security/knight-ransomware-source-code-for-sale-after-leak-site-shuts-down/

[3] Symantec.RansomHub: New Ransomware has Origins in Older Knight [R/OL].(2024-06-05)

https://symantec-enterprise-blogs.security.com/threat-intelligence/ransomhub-knight-ransomware

[4] Forescout.Analysis: A new ransomware group emerges from the Change Healthcare cyber attack [R/OL].(2024-05-09)

https://www.forescout.com/blog/analysis-a-new-ransomware-group-emerges-from-the-change-healthcare-cyber-attack/

[5] BleepingComputer.BlackCat ransomware shuts down in exit scam, blames the "feds"[R/OL].(2024-03-05)

https://www.bleepingcomputer.com/news/security/blackcat-ransomware-shuts-down-in-exit-scam-blames-the-feds/

[6] 安天.警惕因BlackCat勒索软件造成的数据泄露[R/OL].(2023-07-03)

https://www.antiy.cn/research/notice&report...