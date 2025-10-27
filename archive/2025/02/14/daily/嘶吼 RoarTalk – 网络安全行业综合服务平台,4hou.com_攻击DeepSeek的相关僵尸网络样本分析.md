---
title: 攻击DeepSeek的相关僵尸网络样本分析
url: https://www.4hou.com/posts/7MMB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-14
fetch_date: 2025-10-06T20:33:55.745660
---

# 攻击DeepSeek的相关僵尸网络样本分析

攻击DeepSeek的相关僵尸网络样本分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击DeepSeek的相关僵尸网络样本分析

安天
[技术](https://www.4hou.com/category/technology)
2025-02-13 11:26:05

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)73863

收藏

导语：为了更有效地研判风险，支撑对相关攻击的防范，安天CERT从“赛博超脑”平台样本库中提取了上述两个僵尸网络所使用的僵尸木马样本，进行了进一步分析工作。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739417080191662.jpg "1739353826124120.jpg")

**1.概览**

近日，国产AI大模型DeepSeek（深度求索）线上服务受到大规模网络攻击，多次出现服务中断等情况。引发了国内安全业界的关注。根据奇安信XLab实验室监测报告，发现僵尸网络RapperBot和HailBot[1]针对DeepSeek发动了DDoS攻击。为了更有效地研判风险，支撑对相关攻击的防范，安天CERT从“赛博超脑”平台样本库中提取了上述两个僵尸网络所使用的僵尸木马样本，进行了进一步分析工作。

**2.样本分析**

**2.1 RapperBot与HailBot的前世——Mirai**

RapperBot与HailBot两个僵尸网络都是僵尸网络Mirai的源码泄露的产物。Mirai僵尸网络在2016年首次被发现，迅速引发了广泛关注。其命名源自日语中的“未来”。与传统以Windows系统肉鸡为主的僵尸网络不同，Mirai感染控制网络摄像头、家用路由器和其他物联网设备，用于构建僵尸网络体系[2]。在2016年，因其引发的“DYN事件”[3]而浮出水面，Mirai的三名作者Paras Jha，Josiah White和Dalton Norman，均为美国人。三人经营了一家名为Protraf Solutions LLC的公司，对外宣称提供DDoS攻击防护，实际上则利用僵尸网络发动DDoS攻击，进行敲诈等牟利活动。三名人员在2018年，被美国阿拉斯加法院判处5年缓刑、2500小时社区服务，赔偿12.7万美元，并需自愿放弃犯罪期间获取的加密货币。

Mirai专门针对物联网（IoT）设备实施自动化渗透植入，如路由器、网络摄像头和数字视频录像机（DVR），这些设备往往在安全运营视角之外，或者为家庭设备，普遍存在未修改默认密码或采取简易密码、固件版本陈旧等问题。通过密码破解、漏洞攻击，Mirai获取设备的访问权限，并将恶意代码上传至设备中运行，将其转变为受控的僵尸节点[4]。该僵尸网络的一个突出特点是其模块化设计和自更新能力，这使得它能够迅速适应不断变化的安全环境，并增加新的攻击手段。设备被Mirai感染后会自动执行扫描探测任务，并尝试将恶意软件传播至其他设备中，进而构建起一个个庞大的僵尸网络[5]。

2016年9月30日，Mirai僵尸网络源代码在GitHub平台公开泄露。攻击者已基于源码进行定制化改造，衍生出多个变种家族，其中包括RapperBot、HailBot，攻击者改造手段包括但不限于主控域名替换（规避安全厂商封禁）、登录认证机制伪装（仿冒合法设备流量）、通信协议字段混淆（如修改上线心跳包结构以绕过检测规则）等。由于源代码的高度可复用性，全球黑产团伙得以低成本构建“同源异构”的僵尸网络集群——这些变种虽在表层功能上呈现差异，但其核心感染逻辑、C2指令体系与攻击模块均继承自Mirai原始架构，导致其背后操控组织的关联性溯源较为困难。

**2.2 RapperBot僵尸网络**

RapperBot是一种基于Mirai源代码二次开发的僵尸网络，具有多种版本，可在ARM、MIPS、SPARC和x86等不同架构处理器下运行。由于其早期样本中嵌有一个指向说唱视频的链接，因此被命名为“RapperBot”。

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739417081578668.png "1739353776174297.png")

图2‑1 RapperBot早期样本中嵌有一个指向说唱视频的链接

代码中字符串“follow me on instant gram @2tallforfood, pause it. Fuck Bosco.”翻译为“在Instgram上找到我@2tallforfood,暂停，FuckBosco”而@2tallforfood 是在Youtube频道ALL URBAN CENTRAL (城市中心）的一个歌手的账户，该账户在Youtube只有2个2021年前的视频：@2TallForFood - Diamonds Is Lit (Official Video) [6]（钻石闪亮）和 @2tallforfood - I Am Da Bag (Official Video) （我是一个大包）。而Fuckbosco[7]是该歌手的另外一首歌曲的名字。该歌手为小众歌手，其的视频观看人数到报告发布时点不超过500次。

Youtube频道ALL URBAN CENTRAL (城市中心）是2014年成立的美国音乐娱乐频道，主要类型有音乐Rap和Hip HOP 以及名人新闻。订阅用户大约3百万，该频道的视频大都在6分钟以内，频道总视频被浏览次数为20亿次以上。靠订阅收取费用。在美国音乐类排名4000名左右。

![2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739417085368975.png "1739353747178381.png")

图2‑2 RapperBot早期样本中嵌入链接指向的视频

**2.2.1 样本标签**

表2‑1 RapperBot早期版本样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Linux.Mirai[Backdoor] |
| MD5 | 9E331675D780AF4585857B1F95B40CBB |
| 处理器架构 | i386 |
| 文件大小 | 66.47  KB（68068字节） |
| 文件格式 | ELF |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| VT首次上传时间 | 2022-06-17  08:10:19 |
| VT检测结果 | 38/64 |

表2‑2 RapperBot新变种样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Linux.Mirai[Backdoor] |
| MD5 | BEC7596CFB1225900673398ABB24FFA8 |
| 处理器架构 | i386 |
| 文件大小 | 80.47  KB（82400字节） |
| 文件格式 | ELF |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| VT首次上传时间 | 2024-07-02  02:21:30 |
| VT检测结果 | 37/63 |

说明：由于安天AVL SDK反病毒引擎有较强预处理能力，能以较少高质量规则检测变形后的衍生样本，截至本文撰写时RapperBot样本检测结果均为Mirai，特此说明。

**2.2.2 传播方式**

**2.2.2.1 SSH暴力破解**

RapperBot僵尸网络家族中的一些变种通过SSH暴力破解的方式进行传播，在早期样本中，其凭据列表被硬编码在文件中，其后的新变种变更为从C2服务器中获取凭据列表。成功暴力破解SSH服务器后，RapperBot执行Shell命令替换该服务器中的~/.ssh/authorized\_keys文件，从而保持对受害服务器的远程访问。

![2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739417087709067.png "1739353719926240.png")

图2‑3 硬编码在文件中的部分SSH暴力破解凭据列表

**2.2.2.2 Telnet默认口令探测**

部分RapperBot僵尸网络变种会通过Telnet基于设备默认口令的方式进行探测，目标设备关键词、默认用户名称以及密码被硬编码在文件中。

![2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739417088166986.png "1739353308952451.png")

图2‑4 硬编码在样本文件中的Telnet用户名/口令表

从相关样本尝试暴力破解的硬编码信息可知，此类RapperBot变种的目标大多为常见的网络设备和IoT物联网设备等。

表2‑3 RapperBot内置用户探测登录的服务、用户名、口令和可能的关联设备表（表格内容基于DeepSeek整理输出，并做人工修订，特此说明）

|  |  |  |  |
| --- | --- | --- | --- |
| 服务/模块 | 用户名 | 密码 | 可能关联的服务/品牌/设备类型 |
| tc login | dnsekakf2$$ | ""（空） | DASAN定制网络设备 |
| tc login | dnsekakf2$$ | dnsekakf2$$ | DASAN 定制网络设备 |
| tc login | user | 1234 | DASAN 定制网络设备 |
| tc login | admin | TeleCom\_1234 | 中国电信定制设备 |
| tc login | admin | TJ2100Npassword | Tejas Networks TJ2100N光猫或网关 |
| tc login | admin | admin | 多种主流网络设备 |
| tc login | &unk\_19130 | 1234 | 可能为部分摄像头等物联网 |
| soc1 | default | Default | 多种工业产品和软件 |
| soc1 | default | password | 多种工业产品和软件 |
| TAG | default | password | 疑似物联网设备 |
| PXICPU | default | password | 部分工业嵌入式控制器设备 |
| TX25 | default | password | 疑似某种无线设备 |
| PK | admin\_404A03Tel | zyad5001 | ZyXEL(合勤)路由器 |
| PK | admin\_404A03Tel | Centurylink | ZyXEL(合勤)路由器 |
| PK | admin\_404A03Tel | QwestM0dem | ZyXEL(合勤)路由器 |
| PK | admin | Centurylink | ZyXEL(合勤)路由器 |
| PK | admin | QwestM0dem | ZyXEL(合勤)路由器 |
| PK | admin | zyad5001 | ZyXEL(合勤)路由器 |
| abloom | nobody | ""（空） | Abloom品牌物联网设备 |
| abloom | admin | Abloom | Abloom品牌物联网设备 |
| abloom | root | Abloom | Abloom品牌物联网设备 |
| SAP | nobody | ""（空） | SAP系统测试环境或物联网设备 |
| SAP | admin | Admin | SAP NetWeaver应用服务器 |
| RG- | ftp | Video | 网络录像机（NVR）或IP摄像头 |
| buildroot login | default | Default | 多种嵌入式Linux系统 |
| mico | root | ""（空） | 嵌入式系统 |

**2.2.3 行为分析**

RapperBot早期版本支持执行的DoS攻击方式较少，包括TCP STOMP攻击以及UDP泛洪攻击等。RapperBot新变种支持接收的指令与早期样本相似，但能够支持执行更多种类的DoS攻击。

表2‑4 早期版本及新变种指令功能对比

|  |  |  |
| --- | --- | --- |
| 指令码 | RapperBot早期版本功能 | RapperBot新变种功能 |
| 1 | 保持连接状态 | 上线包 |
| 2 | 停止DoS攻击并终止运行 | 响应包 |
| 3 | 执行DoS攻击 | 心跳包 |
| 4 | 停止DoS攻击 | 执行DoS攻击 |
| 5 | 无 | 停止DoS攻击并终止运行 |
| 6 | 无 | 关闭C2连接 |

当攻击者进行DoS攻击时，通过选择预先设定的序号执行对应的功能函数，从而执行具体的DoS攻击。由此可以看出，RapperBot相关样本支持接收的指令功能以发起DoS攻击为主，并且从其早期至今的发展过程中，其开发者对RapperBot的DoS攻击功能进行了逐步完善，从而支持完成大范围的DDoS攻击活动。

表2‑5 RapperBot新变种支持多种DoS攻击

|  |  |  |
| --- | --- | --- |
| 攻击指令 | DoS攻击类型 | 攻击说明介绍 |
| 0 | UDP泛洪攻击 | 通过发送大量UDP数据包消耗受害者网络带宽。 |
| 1 | UDP数据包伪造 | 攻击者向目标服务器发送大量伪造的UDP数据包，欺骗服务器进行响应，消耗受害者网络带宽。 |
| 2 | GRE-IP泛洪攻击 | 通过大量封装有IP网络数据包的GRE协议数据消耗受害者网络带宽。 |
| 3 | GRE-Eth泛洪攻击 | 通过大量封装有Eth网络数据包的GRE协议数据消耗受害者网络带宽。 |
| 4 | SYN泛洪攻击 | 通过发送大量SYN数据包，使服务器创建具有大量处于半连接状态的请求，消耗系统内存和CPU资源。 |
| 5 | ACK泛洪攻击 | 通过发送具有随机源端口、目的端口及数据等信息的ACK数据包消耗受害者网络带宽。 |
| 6 | ACK-PSH泛洪攻击 | 通过带有PSH标记的ACK响应与服务器建立连接，发送大量请求消耗受害者的网络带宽。 |
| 7 | TCP泛洪攻击 | 通过发送大量TCP数据包消耗受害者网络带宽。 |
| 8 | HTTP泛洪攻击 | 攻击者向目标服务器发送大量的HTTP报文，消耗受害者网络带宽和服务器资源。 |

**2.3 HailBot僵尸网络**

HailBot是一种基于Mirai源代码二次开发的僵尸网络，可在ARM、x86、x64、MIPS等不同架构处理器下运行。由于其运行时向控制台输出“hail china mainland”，故命名为HailBot僵尸网络。

**2.3.1 样本标签**

表2‑6 HailBot早期版本样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Linux.Mirai[Backdoor] |
| MD5 | C4526600A90D4E1EC581D1D905AA6593 |
| 处理器架构 | x64 |
| 文件大小 | 68.6  KB (70,295 字节) |
| 文件格式 | BinExecute/Linux.ELF[:X64] |
| 数字签名...