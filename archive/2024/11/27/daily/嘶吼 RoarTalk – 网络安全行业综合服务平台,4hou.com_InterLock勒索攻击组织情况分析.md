---
title: InterLock勒索攻击组织情况分析
url: https://www.4hou.com/posts/424g
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-27
fetch_date: 2025-10-06T19:12:13.013952
---

# InterLock勒索攻击组织情况分析

InterLock勒索攻击组织情况分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# InterLock勒索攻击组织情况分析

安天
[技术](https://www.4hou.com/category/technology)
2024-11-26 16:20:16

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)80896

收藏

导语：暂未发现该组织通过勒索软件即服务（RaaS）模式招募附属成员以扩大非法收益的情况。目前，已监测到该组织开发了针对Windows、Linux和FreeBSD系统的加密载荷。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604823131701.jpg "1732604823131701.jpg")

**1 概述**

InterLock勒索攻击组织被发现于2024年9月，该组织通过网络钓鱼、漏洞利用、搭载于其他恶意软件和非法获取凭证等多种手段渗透受害者网络，窃取敏感信息并加密数据，实施双重勒索，以此对受害者施加压力。暂未发现该组织通过勒索软件即服务（RaaS）模式招募附属成员以扩大非法收益的情况。目前，已监测到该组织开发了针对Windows、Linux和FreeBSD系统的加密载荷。在Windows系统中，InterLock勒索软件采用“AES+RSA”算法对文件进行加密。感染的迹象包括文件名后添加“.interlock”扩展名，以及出现名为“!README!.txt”的勒索信。截至目前，尚未发现任何工具能够有效解密由InterLock勒索软件加密的数据。

InterLock组织在暗网中运营一个名为“InterLock Worldwide Secrets Blog”的网站，公开受害者信息。该网站包含组织介绍、联系方式、受害者资料以及从受害者系统中窃取的数据等。对于每位受害者，攻击者创建独立的信息板块，列出受害者名称、官网链接、信息概览、被盗文件类型和数量。攻击者利用公开受害者信息和部分被盗文件作为要挟，迫使受害者为防数据被出售或公开而支付赎金或满足其他非法要求。截至2024年11月21日，该网站已公布7名受害者的信息，但实际受害数量可能更多。攻击者可能基于多种原因选择不公开或删除某些信息，例如在与受害者达成协议，或受害者支付赎金换取了信息的移除。

InterLock组织所使用的勒索加密载荷和攻击技战术等特征揭示了其与Rhysida组织[1]之间可能的联系。自2023年5月被发现以来，Rhysida组织一直以RaaS和双重勒索模式进行运营，但自2024年10月以来，其攻击活跃度有所下降。在当前复杂的网络犯罪生态和全球执法机构对勒索攻击组织的持续打击下，InterLock与Rhysida之间的关系引发了多种推测：InterLock可能是Rhysida的一个分支或附属机构，继承了其技术和战术；或者Rhysida组织的部分成员因内部分歧或其他原因而另立门户，成立了InterLock；还有一种可能是Rhysida组织为了规避执法机构的打击，以InterLock的新名义继续其非法活动。这些推测基于两个组织在勒索软件操作和战术上的相似性，以及网络犯罪组织内部常见的动态和逃避策略。相关勒索软件及其组织信息可见计算机病毒百科（https://www.virusview.net/RansomwareAttack）。

经验证，安天智甲终端防御系统（简称IEP）可实现对InterLock勒索软件的有效查杀。

**2 组织情况**

表 2‑1 组织概览

|  |  |
| --- | --- |
| 组织名称 | InterLock |
| 出现时间 | 2024年9月 |
| 入侵方式 | 网络钓鱼、漏洞利用、搭载于其他恶意软件和非法获取凭证 |
| 典型加密后缀 | .interlock |
| 解密工具 | 暂未发现公开的解密工具 |
| 加密系统 | Windows、Linux、FreeBSD |
| 攻击模式 | 非定向与定向攻击模式 |
| 常见行业 | 医疗、金融、教育、制造、公共管理 |
| 是否双重勒索 | 是 |
| 勒索信 | ![表2-1里的勒索信.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604765120731.jpg "1732604703436301.jpg") |

InterLock勒索软件于2024年9月被MOXFIVE发现[2]，根据勒索信中预留的信息判定该勒索软件是由InterLock勒索攻击组织使用。

![2-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604766242270.jpg "1732604694183414.jpg")

图 2‑1 组织暗网页面

在暗网中网站页面设置了“自我介绍”信息栏，表明自己的身份和发起勒索攻击的原因等内容。

![2-2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604766201359.jpg "1732604680140521.jpg")

图 2‑2 组织“自我介绍”内容

InterLock组织自2024年10月13日发布第一名受害者信息以来，截至11月21日已陆续发布7名受害者信息，实际受害数量可能更多。

![2-3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604767593708.jpg "1732604654802603.jpg")

图 2‑3 受害者信息栏

**3 样本功能与技术梳理**

**3.1样本标签**

表 3‑1 InterLock勒索软件样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Win32.InterLock[Ransom] |
| 原始文件名 | matrix |
| MD5 | F7F679420671B7E18677831D4D276277 |
| 文件大小 | 1.89 MB (1,982,464字节) |
| 文件格式 | BinExecute/Microsoft.EXE[:X86] |
| 时间戳 | 2024-10-11 04:47:13 UTC |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| 编译语言 | Visual C/C++ |
| VT首次上传时间 | 2024-10-13 17:10:43 UTC |
| VT检测结果 | 57/73 |

**3.2样本分析**

样本执行支持4种执行参数，具体功能如下表所示：

表 3‑2 功能参数

|  |  |
| --- | --- |
| 参数 | 功能 |
| --directory | 加密指定文件夹 |
| --file | 加密指定文件 |
| --delete | 自删除 |
| --system | 创建系统计划任务 |

样本包含大量混淆代码，并通过代码自解密恢复正常代码执行，以此增加分析难度，减少代码静态特征。![3-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604768205855.jpg "1732604627412974.jpg")

图 3‑1 样本代码混淆

如果指定了自删除参数，则在加密结束后，释放文件%Temp%\tmp

若指定了计划任务参数，则会创建名为TaskSystem的计划任务。

![3-3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604769124000.jpg "1732604596118380.jpg")

图 3‑2 创建计划任务

避免因加密导致系统崩溃或加密到杀毒软件文件，不对特定文件夹进行加密。

![3-4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604770730027.jpg "1732604587394180.jpg")

图 3‑3 绕过加密的文件夹

具体绕过加密的文件夹信息如下表所示：

表 3‑3 绕过加密的文件夹

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 绕过加密的文件夹 | | | | |
| $Recycle.Bin | Boot | Documents and Settings | PerfLogs | ProgramData |
| Recovery | Windows | System Volume Information | AppData | WindowsApps |
| Windows Defender | WindowsPowerShell | Windows Defender Advanced Threat   Protection |  |  |

避免因加密导致系统崩溃，不对特定后缀名和特定文件名的文件进行加密。

![3-5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604771517411.jpg "1732604573913921.jpg")

图 3‑4 绕过加密的后缀名及文件名

具体绕过加密的后缀名及文件名信息如下表所示：

表 3‑4 绕过加密的后缀及文件名

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 绕过加密的后缀及文件名 | | | | |
| .bin | .diagcab | .hta | .scr | .dll |
| .cab | .diagcfg | .ico | .sys | .exe |
| .cmd | .diagpkg | .msi | .ini | .ps1 |
| .com | .drv | .ocx | .url | .psm1 |
| .cur | .hlp | Thumbs.db |  |  |

样本使用LibTomCrypt加密库。

![3-6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604771842574.jpg "1732604488390951.jpg")

图 3‑5 LibTomCrypt加密库

在要加密的目标文件末尾填充字节，直至文件大小为16字节的倍数，对齐AES加密分组大小。

![3-7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604772731916.jpg "1732604475134210.jpg")

图 3‑6 填充目标文件末尾

样本采用AES-CBC和RSA加密算法，样本会为每个文件生成独立的48个字节长度的随机数，将其前32字节作为AES密钥对整个文件进行加密。同时将这48个字节的随机数使用RSA非对称加密后附加在加密的文件的末尾。总体加密逻辑如下所示。

![3-8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604773193366.jpg "1732604463851973.jpg")

图 3‑7 加密逻辑

使用AES加密文件的代码如下，文件所有内容均会被加密。

![3-9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604774187556.jpg "1732604323956387.jpg")

图 3‑8 采用AES加密算法

勒索信相关内容。

![3-10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604775888784.jpg "1732604312302427.jpg")

图 3‑9创建勒索信相关代码

清除入侵痕迹，在样本执行结束后调用API清除相关日志。

![3-11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604776163511.jpg "1732604299603960.jpg")

图 3‑10 清除相关日志

**4 防护建议**

建议企业用户部署专业的终端安全防护产品，对本地新增和启动文件进行实时检测，并周期性进行网内病毒扫描。安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀本次发现病毒样本。

智甲具备内核级防护能力，基于内核驱动持续监控进程等内存对象操作行为动作，研判是否存在持久化、提权、信息窃取等攻击动作，并且结合勒索行为特征库检测，可分析进程行为是否疑似勒索攻击行为，对发现的勒索攻击可在第一时间进行阻断。

![4-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604776631540.jpg "1732604279201335.jpg")

图 4‑1 发现病毒时，智甲第一时间拦截并发送告警

智甲提供统一安全管理中心，管理员可通过管理中心快速完成对网内安全事件的查看、分析、处置等操作，提升安全管理效率。

![4-2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241126/1732604777154624.jpg "1732604261153401.jpg")

图 4‑2 可通过智甲统一管理平台对威胁进行一键处置

**参考链接**

**[1]**2023年活跃勒索攻击组织盘点 [R/OL].(2024-01-25)

https://www.antiy.cn/research/notice&report/research\_report/RansomwareInventory.html

**[2]**MOXFIVE Threat Actor Alert - INTERLOCK Ransomware [R/OL].(2024-09-30)

https://www.moxfive.com/resources/moxfive-threat-actor-spotlight-interlock-ransomware

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/ca...