---
title: 城市侧网络安保中的高频事件案例分析
url: https://www.4hou.com/posts/NGRv
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-17
fetch_date: 2025-10-06T22:03:27.371062
---

# 城市侧网络安保中的高频事件案例分析

城市侧网络安保中的高频事件案例分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 城市侧网络安保中的高频事件案例分析

安天
[技术](https://www.4hou.com/category/technology)
2025-04-16 15:06:27

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)95431

收藏

导语：黑龙江省重大活动期间，安天作为城市侧网络安全保障的总体技术支撑单位，支撑省市两级主管部门，部署流量、蜜罐探针数百套、终端和服务器安全防护数万套，开放垂直响应、在线威胁分析、安全DNS多种服务。

**1 概述**

黑龙江省重大活动期间，安天作为城市侧网络安全保障的总体技术支撑单位，支撑省市两级主管部门，部署流量、蜜罐探针数百套、终端和服务器安全防护数万套，开放垂直响应、在线威胁分析、安全DNS多种服务。

现代城市是数字化的城市，大量政企机构和公民个人与家庭的设备连接于城域网之上。保障目标复杂多元，有海量的资产暴露面和可攻击点。攻击活动暗流汹涌。仅活动期间，安天网安护卫队在城市侧累计监测发现各类境外网络攻击事件达5076万次。其中主要的高频事件包括网络扫描探测、暴力破解登录凭证、漏洞利用攻击、远控木马植入、挖矿木马感染及僵尸网络控制等，这些攻击活动如果不及时发现、阻断和处置，有可能对城市运行造成严重影响。本报告对相关工作中的六类高频网络攻击事件各摘取一例案例进行解析，以期为安全防护和运营工作提供参考与借鉴。

**2 城市侧安保网络攻击典型案例**

**2.1网络扫描案例**

网络扫描是指攻击者通过主动探测目标网络或系统，收集关键信息（如开放端口、运行服务、操作系统版本等）的行为，目的是发现被扫描目标的资产暴露面，寻找可利用的的攻击入口点，为后续攻击做准备，其处在网络攻击活动中的“侦察”环节。

2025年2月13日2时，安天监测并阻断了一起攻击源IP地址位于美国的端口扫描攻击事件。对攻击IP进行威胁情报查询，安天威胁情报中心显示该攻击IP地理位置为美国，带有多个历史威胁活动标签。通过溯源分析发现CENSYS-ARIN-01网段归属于美国Censys, Inc.公司所有，Censys, Inc.公司是一家注册于美国的主营攻击面管理和威胁搜寻解决方案的网络安全公司。

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783290177330.png "1744783290177330.png")

图 2‑1 安天网络威胁监测预警系统告警信息

安天威胁情报中心显示，该攻击IP归属地为美国，依托历史行为活动标注了“恶意”、“扫描”、“爆破”、“DDoS”等活动标签。

![2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783273400030.png "1744783273400030.png")

图 2‑2 安天威胁情报显示攻击IP行为标签为扫描

对攻击IP进行ASN查询，发现属于AS 398324（CENSYS-ARIN-01），而CENSYS-ARIN-01网段归属于美国Censys, Inc.公司所有。

![2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783262411645.png "1744783262411645.png")

图 2‑3 ASN查询显示IP属于CENSYS

值得特别关注的是，2024年10月，美国国家情报总监办公室 (ODNI)下属的网络威胁情报整合中心（CTIIC）授予Censys一份多年合同，代号“Sentinel Horizon”（哨兵地平线）。根据这一合同，Censys将为美国情报界各机构提供其互联网情报平台服务。Censys利用其全球互联网连续扫描与监测能力，为美情报机构提供对全球所有互联网暴露资产的实时覆盖和访问。

**2.2 暴力破解案例**

暴力破解攻击是通过在攻击者不掌握目标系统的登录凭证的情况下，通过反复尝试系统登录获取受保护系统的访问权限。基本原理是通过尝试空口令、弱口令、设备出场预设口令或历史已破解（泄露）口令，或基于用户相关信息及数字或字母的组合等，来反复登录并找出正确的密码，其处在网络攻击活动中的“初始访问”、“凭证访问”等环节。

2025年2月8日22时，安天监测并阻断了一起攻击源IP地址位于越南的暴力破解攻击事件。攻击者使用IP地址103.237.\*\*\*.\*\*\*对客户服务器发起SSH暴力破解尝试，企图获取系统访问权限。经深入分析，安天确认此次攻击未成功，并立即启动威胁溯源流程。通过多维度威胁情报分析，显示攻击IP地理位置为越南，威胁标签显示相关地址关联扫描、暴力破解等恶意活动。该攻击IP关联越南某图书馆数字化公司的业务域名（idtvietnam[.]vn）。

![2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783241639228.png "1744783241639228.png")

图 2‑4 安天网络威胁监测预警系统告警信息

安天威胁情报中心显示，该攻击IP归属地为越南，具有“恶意”、“爆破”、“扫描”等标签。

![2-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783224152534.png "1744783224152534.png")

图 2‑5 安天威胁情报显示该IP行为标签为爆破

对攻击IP进行域名反查，发现关联域名(demo[.]idtvietnam[.]vn)，浏览idtvietnam[.]vn网站内容，其是一家专注于图书馆数字化领域的越南公司。初步判断相关主机被攻击者入侵控制，成为攻击肉鸡。

![2-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783211713596.png "1744783211713596.png")

图 2‑6 IP反查域名结果

**2.3 漏洞利用案例**

漏洞利用是指攻击者利用软件、硬件或网络协议中的安全漏洞来执行未授权操作的行为，其处在网络攻击活动中的“初始访问”、“执行”、“权限提升”与“防御绕过”等环节。

2025年2月7日10时，安天监测并阻断了一起攻击源IP地址位于美国的漏洞利用攻击事件，攻击者企图利用漏洞获取系统控制权限。安天网安护卫队迅速响应并完成攻击行为研判，确认攻击未造成实际危害，并立即开始溯源。通过威胁情报查询、域名反查、历史资产测绘、互联网检索等手段进行溯源分析，发现该IP关联瑞士网络安全公司BinaryEdge的域名（binaryedge[.]ninja）。

![2-7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783183150589.png "1744783183150589.png")

图 2‑7 安天网络威胁监测预警系统告警信息

安天威胁情报中心显示，该攻击IP归属地为美国，具有“恶意”、“爆破”、“扫描”等标签。

![2-8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783165295006.png "1744783165295006.png")

图 2‑8 安天威胁情报显示攻击IP行为标签为扫描

对攻击IP进行域名反查，发现关联域名binaryedge[.]ninja与binaryedge[.]io，域名归属于瑞士BinaryEdge公司所有。

BinaryEdge为一家网络安全企业， 提供网络攻击面在内的实时威胁情报。其平台通过扫描互联网上的设备和服务，收集关于开放端口、服务、潜在漏洞以及配置不当的网络共享等信息。通过上述事件判断其并非单纯进行端口服务和指纹探测，也进行了PoC验证行为。

![2-9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783148116421.png "1744783148116421.png")

图 2‑9 反查域名发现其属于瑞士BinaryEdge公司

**2.4 远控攻击案例**

远程控制攻击是指攻击者通过植入带有远程控制功能恶意程序（特洛伊木马等）或利用合法远程管理工具（如VNC、RDP、TeamViewer等）、以及机器自身的开放的管理服务（如远程桌面），来实现可以对目标系统进行操控的行为，其处在网络攻击活动中的“命令与控制”、“持久化”、“执行”与“防御绕过”等环节。

2025年2月14日4时，安天监测并阻断了一起攻击源IP地址位于荷兰的远控攻击事件，安天网安护卫队溯源分析发现，该IP曾传播远控木马家族NanoCore。NanoCore是一种知名的远程控制木马，最初作为合法的远程管理工具开发，但被广泛用于恶意目的。它具备远程控制、键盘记录、屏幕监控、窃取数据和摄像头控制等功能，常通过钓鱼邮件或漏洞传播。感染后可能导致隐私泄露、数据窃取和设备被完全控制。

![2-10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783098118399.png "1744783098118399.png")

图 2‑10 安天网络威胁监测预警系统告警信息

安天威胁情报中心显示，该攻击IP归属地为荷兰，具有“恶意”、“远控”、“NanoCore”等标签。

![2-11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783065404170.png "1744783065404170.png")

图 2‑11 安天威胁情报显示攻击IP传NanoCore远控木马

**2.5 挖矿攻击案例**

挖矿攻击是指攻击者未授权利用受害者的计算资源（如CPU、GPU等）进行加密货币挖矿（如比特币、门罗币等）的行为，目的是通过窃取资源牟利，其处在网络攻击活动中的“执行”、“持久化”与“防御绕过”等环节。

重大活动期间，安天网安护卫队应急响应了多起服务器挖矿攻击事件。基于网络侧感知到相关服务器到达矿池地址连接，由于该服务器未安装防护软件，护卫队员指导用户进行了工具处置。发现的挖矿木马样本（样本hash：B4A802912838ADD056FB0ACA7EE3A835，病毒名：Trojan/Win64.CoinMiner）。该木马执行后首先复制自身到C:\ProgramData\WinMngr\目录下，并命名为winmngrsa.exe，同时在C:\Windows\TEMP\下创建名为yoygdjmdclhw.sys的驱动文件。该木马通过一系列精心设计的服务操作来隐藏自身行为，包括删除原有“WinMngr”服务，重新创建同名服务并设置为自启动，以及停止系统日志服务以逃避检测。该挖矿木马启动后，会通过dwm.exe进程连接恶意IP地址185.215.\*\*\*.\*\*\*。安天通过流量分析确认，这些连接均为挖矿通信流量，钱包地址为47fEQ5mTN8MCL91SaDm6ooigyfKddGfTchFTudHDQLoyZ4Kps7jG19n1UA8eSwuzomEtjQqKkkZr6NmcbUWa3HtuA2dEe6e。该木马会大量消耗系统算力资源，导致服务器性能严重下降，影响正常业务运行，以及造成电力资源浪费和硬件设备寿命缩短。

表 2‑1 样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Win64.CoinMiner |
| 原始文件名 | winmngrsa.exe |
| MD5 | B4A802912838ADD056FB0ACA7EE3A835 |
| 处理器架构 | Intel   386 or later processors and compatible processors |
| 文件大小 | 2.50   MB(2,620,416字节) |
| 文件格式 | BinExecute/Microsoft.EXE[:X86] |
| 时间戳 | 2024-12-26   17:17:10 |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| 编译语言 | Microsoft   Visual C++ |

木马运行后会将自身复制到C:\ProgramData\WinMngr\目录下，并命名为winmngrsa.exe，且以winmngrsa.exe为进程名驻留在系统中。

![2-12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744783016201367.png "1744783016201367.png")

图 2‑12 复制自身到当前目录下

该木马使用了驱动技术，使用安天系统安全内核分析工具ATool发现木马同时在C:\Windows\TEMP\下创建名为yoygdjmdclhw.sys的驱动文件，开启ATool的云查功能后，该驱动文件被ATool的信誉分析带有恶意内容和恶意行为两个标签，但带有合法数字签名。

![2-13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744782997220523.png "1744782997220523.png")

图 2‑13 TEMP目录下创建名为yoygdjmdclhw.sys的驱动文件

删除系统原有“WinMngr”服务，重新创建同名服务并设置为自启动，便于受害机器重启后重新执行。下图为使用ATool的云查功能发现病毒创建的服务，橙色表示恶意。

![2-14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744782984166908.png "1744782984166908.png")

图 2‑14 创建“WinMngr”服务

该挖矿病毒启动后，会通过dwm.exe进程连接恶意IP地址185.215.\*\*\*.\*\*\*。![2-15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744782943196534.png "1744782943196534.png")

图 2‑15 连接恶意IP地址

病毒内置XMRig挖矿程序进行挖矿，版本为6.21.3，钱包地址为47fEQ5mTN8MCL91SaDm6ooigyfKddGfTchFTudHDQLoyZ4Kps7jG19n1UA8eSwuzomEtjQqKkkZr6NmcbUWa3HtuA2dEe6e。

![2-16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744782925100098.png "...