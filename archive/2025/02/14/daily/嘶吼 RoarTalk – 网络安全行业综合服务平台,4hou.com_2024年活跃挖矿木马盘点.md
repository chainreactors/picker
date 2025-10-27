---
title: 2024年活跃挖矿木马盘点
url: https://www.4hou.com/posts/gyyj
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-14
fetch_date: 2025-10-06T20:33:54.614163
---

# 2024年活跃挖矿木马盘点

2024年活跃挖矿木马盘点 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 2024年活跃挖矿木马盘点

安天
[行业](https://www.4hou.com/category/industry)
2025-02-13 11:48:46

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)46003

收藏

导语：2024年，安天CERT捕获了多起挖矿木马的攻击活动，现将2024年典型的挖矿木马梳理形成组织/家族概览，进行分享。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739418472963500.jpg "1739412286119459.jpg")

**1 概述**

挖矿木马通过各种手段将挖矿程序植入受害者的计算机中，在用户不知情的情况下，利用受害者计算机的运算能力进行挖矿，从而获取非法收益。目前已知多个威胁组织（例如，H2Miner、“8220”等）传播挖矿木马，致使用户系统资源被恶意占用和消耗、硬件寿命被缩短，严重影响用户生产生活，妨害国民经济和社会发展。2024年，安天CERT捕获了多起挖矿木马的攻击活动，现将2024年典型的挖矿木马梳理形成组织/家族概览，进行分享。

表 1‑1 2024年活跃挖矿木马组织/家族概览

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250213/1739418474153019.png "1739412245860546.png")

**2 挖矿木马的危害**

**1.加重信息系统基础设施资源消耗与运行风险**：挖矿木马普遍消耗信息系统基础设施的大量资源，使操作系统及其服务、应用软件运行缓慢，甚至造成正常服务崩溃，产生承载业务中断、业务数据丢失等一系列负面影响；

**2.危害信息系统基础设施使用寿命与运行性能**：挖矿木马迫使信息系统基础设施长时间高负载运行，致使其使用寿命缩短，运行性能严重下降；

**3.留置后门，衍生僵尸网络**：挖矿木马普遍具有添加SSH免密登录后门、安装RPC后门，接收远程IRC服务器指令、安装Rootkit后门等恶意行为，致使受害组织网络沦为僵尸网络；

**4.作为攻击跳板，攻击其他目标**：挖矿木马支持攻击者控制受害者服务器进行DDoS攻击，以此服务器为跳板，攻击其他计算机，或者释放勒索软件索要赎金等。

**3 挖矿木马趋势**

**3.1 BYOVD攻击成挖矿木马“新宠”**

在2024年的挖矿木马事件应急响应中，安天CERT发现挖矿木马利用BYOVD（Bring Your Own Vulnerable Driver）攻击结束安全软件进程的案例增多。BYOVD攻击是APT中常见的攻击技术，现在挖矿攻击中也逐渐开始利用这种技术。它利用合法但存在漏洞的驱动程序来执行恶意操作，绕过安全防护措施。驱动程序运行在高权限的内核模式，攻击者可以通过其漏洞实现多种攻击目的。在挖矿攻击中，攻击者通过滥用合法安全厂商签名的驱动程序，绕过操作系统的安全机制，为挖矿活动提供支撑。这种手法不仅提升了攻击的隐蔽性，还利用安全软件的高权限执行能力，大幅增强了恶意挖矿的资源占用效率。在未来，BYOVD攻击可能与零日漏洞利用相结合，进一步提高攻击的复杂性和破坏性。这一趋势对政企安全提出更高的要求，防护重点应包括驱动程序的合法性检测与运行时行为监控等。

**3.2 暗网矿池地址的兴起**

2024年，安天CERT在监测挖矿攻击中发现个别挖矿木马采用了暗网地址进行挖矿的事件，如Perfctl恶意软件利用TOR进行挖矿，Outlaw挖矿僵尸网络在配置文件中添加了暗网地址，但还未开发出tor进行连接。这一趋势表明，攻击者正在加速向更隐秘、更难追踪的挖矿方式转型，以逃避传统安全防护和执法行动的打击。通过Tor网络或其他匿名通信协议，矿池运营者能够有效隐藏其真实位置和身份，难以被执法部门定位和取缔。暗网矿池普遍采用加密货币作为支付手段，结合匿名钱包技术，实现了攻击收益的完全匿名化。随着暗网矿池技术的不断成熟，传统基于互联网的挖矿威胁检测手段将变得无效。政企需调整防护策略，关注挖矿通信的特征分析和暗网流量的异常检测。

**3.3合理资源分配致用户难以感知**

2024年，挖矿木马在资源利用上更加智能化，表现为更合理的资源分配策略。如app Miner挖矿木马会检查系统环境是否有curl、Python、Perl等工具，如果没有会进行下载适配，在不同的系统上动态的调整CPU的功率或资源使用参数。Outlaw挖矿僵尸网络会获取目标主机的系统架构，根据系统架构调整默认线程数，arm架构线程数设置为75，i686架构线程数设置为325，其他架构默认线程数为475。这种趋势不仅提升了挖矿效率，还极大地增强了挖矿木马被发现感知的风险。智能化资源分配根据系统负载动态调整CPU和GPU的使用率，避免引起设备异常或用户注意。挖矿进程被设计为低优先级任务，在设备闲置时充分利用资源，而在用户活跃时降低消耗，从而延长挖矿周期。这种智能化资源分配的趋势使挖矿木马更具隐蔽性和持续性，成为网络威胁防护的难点。

**4 活跃挖矿木马介绍**

**4.1“8220”**

“8220”是一个长期活跃并且擅长使用漏洞进行攻击并部署挖矿程序的组织，该组织早期使用Docker镜像传播挖矿木马，后来逐步利用多个漏洞进行攻击，如WebLogic漏洞、Redis未授权访问漏洞、Hadoop Yarn未授权访问漏洞和Apache Struts漏洞等。在2020年发现该组织开始使用SSH暴力破解进行横向攻击传播。自Apache Log4j 2远程代码执行漏洞曝光后，该组织利用该漏洞制作漏洞利用脚本进行传播，影响范围广。

**4.1.1组织概览**

表 4‑1 “8220”挖矿组织介绍

|  |  |
| --- | --- |
| 组织名称 | “8220” |
| 出现时间 | 2017年 |
| 针对平台 | Windows、Linux |
| 传播方式 | SSH暴力破解、Docker镜像和漏洞利用 |
| 利用的漏洞 | Apache Log4j 2远程代码执行漏洞  Oracle WebLogic漏洞  Atlassian Confluence漏洞  Redis未授权访问漏洞  Hadoop Yarn未授权访问漏洞  Apache Struts漏洞 |
| 挖矿币种 | 门罗币（XMR） |

**4.1.2典型案例**

**·针对Oracle WebLogic漏洞的攻击活动分析**

Water Sigbin(8220 Gang)是一个专注于部署加密货币挖矿恶意软件的威胁行为者，它积极针对Oracle WebLogic服务器。该威胁行为者利用Oracle WebLogic Server中的漏洞（特别是CVE-2017-3506和CVE-2023-21839）通过PowerShell脚本部署加密货币挖矿程序。研究人员分析了用于传递PureCrypter加载器和XMRIG加密挖掘器的多阶段加载技术。此活动期间使用的所有有效载荷均使用.Net Reactor（一种.NET代码保护软件）进行保护，以防止逆向工程。此保护会混淆代码，使防御者难以理解和复制。此外，它还采用了反调试技术。有效载荷是通过利用CVE-2017-3506来传递的[1]。

**·8220挖矿团伙的新玩具：k4spreader**

2024年6月17号研究人员发现了一个VT 0检测的使用c语言编写的ELF样本，这个样本使用变形的upx加壳，脱壳后得到了另一个变形的upx加壳的elf文件，使用cgo的方式编写。经过分析发现这是来自“8220”挖矿团伙的新工具，用来安装其他恶意软件执行，主要是构建Tsunami DDoS僵尸网络和安装PwnRig挖矿程序。根据样本中的函数名称将其命名为“k4spreader”，进一步分析了VT的和蜜罐的数据后，发现k4spreader尚处于开发阶段，但已经出现3个变种[2]

**4.2 Outlaw**

Outlaw挖矿僵尸网络最早于2018年被发现，主要针对云服务器实施挖矿攻击，持续活跃。疑似来自罗马尼亚，最早由趋势科技将其命名为Outlaw，中文译文为“亡命徒”。该挖矿僵尸网络首次被发现时，攻击者使用Perl脚本语言的后门程序构建机器人，因此被命名为“Shellbot”。其主要传播途径是SSH暴力破解攻击目标系统并写入SSH公钥，以达到长期控制目标系统的目的，同时下载基于Perl脚本语言编写的后门和开源门罗币挖矿木马。

**4.2.1 组织概览**

表 4‑2 Outlaw挖矿僵尸网络介绍

|  |  |
| --- | --- |
| 组织名称 | Outlaw |
| 组织介绍 | 一个通过漏洞利用和SSH暴力破解传播基于Perl语言编写的Shellbot而组建的僵尸网络，后期开始投放挖矿木马获利 |
| 首次披露时间 | 2018年11月1日 |
| 首次披露厂商 | 趋势科技 |
| 归属国家 | 疑似罗马尼亚 |
| 命名原因 | 源自罗马尼亚语haiduc的翻译，该组织主要使用的黑客工具Haiduc |
| 威胁类型 | 僵尸网络、挖矿木马 |
| 针对目标 | Linux、IoT |
| 传播途径 | Shellshock(CVE-2014-7169)漏洞、Drupalgeddon2漏洞（CVE-2018-7600）漏洞和SSH暴力破解，主要采用后者，漏洞利用只在初期使用过 |
| 组织组件 | 隐藏进程工具（XHide）、SSH暴力破解工具（Haiduc、ps、tsm）、Shellbot程序、挖矿木马（XMRig） |
| 版本迭代 | 该僵尸网络样本共有5个版本迭代，主要区别在于功能的新增，破解工具替换，破解工具功能的变化上 |

**4.2.2典型案例**

**·Outlaw挖矿僵尸网络近期活动分析**

安天CERT监测到多起Outlaw挖矿僵尸网络攻击事件，该挖矿僵尸网络最早于2018年被发现，主要针对云服务器从事挖矿活动，持续活跃。安天CERT在分析近期的攻击事件中发现，该挖矿僵尸网络样本在第三版本基础上有了重要更新，其功能更加多样、隐匿性更高、清除更加困难。主要传播途径和功能依旧是SSH暴力破解攻击目标系统，植入SSH公钥，以达到长期控制目标系统的目的，同时下载执行基于Perl脚本语言编写的后门和开源门罗币挖矿木马，使用扫描和暴力破解工具对其他主机进行相应攻击[3]。

**4.3 TeamTNT**

TeamTNT挖矿组织最早于2019年被发现，主要针对Docker Remote API未授权访问漏洞、配置错误的Kubernetes集群和Redis服务暴力破解进行攻击。入侵成功后，窃取各类登录凭证并留下后门，主要利用目标系统资源进行挖矿并组建僵尸网络。经过近几年发展，该组织控制的僵尸网络规模庞大，所使用的攻击组件更新频繁，是目前针对Linux服务器进行挖矿的主要攻击组织之一。该组织疑似来自德国，其命名方式依据该组织最早使用teamtnt.red域名进行命名。

**4.3.1组织概览**

表 4‑3 TeamTNT挖矿组织介绍

|  |  |
| --- | --- |
| 组织名称 | TeamTNT |
| 首次披露时间 | 2019年10月 |
| 归属国家 | 德国 |
| 命名原因 | 最早使用teamtnt.red域名 |
| 威胁类型 | 挖矿木马、后门 |
| 针对目标 | JupyterLab、Docker、Kubernetes和Redis |
| 传播途径 | 错误的配置和SSH凭证等 |
| 组织武器库 | Tsunami、Rathole、Ezuri、Punk.py、libprocesshider、tmate、masscan、pnscan、ZGrab、Tiny Shell、Mimipy、BotB、Diamorphine、Docker   Escape Tool等 |
| 组织擅长技术 | 扫描局域网端口、添加防火墙规则、删除其他竞争对手进程、创建持久性计划任务、窃取服务凭证、收集机器信息、Rootkit隐藏进程、部署挖矿程序和横向移动等 |
| 推特账户 | HildeGard@TeamTNT@HildeTNT |
| GitHub账户 | hilde@TeamTNT  HildeTeamTNT |
| 托管网站 | teamtnt.red |

**4.3.2典型案例**

**·TeamTNT组织发起新一轮攻击活动**

研究人员发现了TeamTNT正在策划一场新的攻击活动。在这次攻击活动中，TeamTNT似乎回归本源，准备对云环境进行大规模攻击。该组织目前以暴露的Docker守护进程为目标，部署Sliver恶意软件、网络蠕虫和加密矿工，使用受感染的服务器和Docker Hub作为传播恶意软件的基础设施。在此次活动中，TeamTNT通过将受感染的Docker实例附加到Docker Swarm并利用Docker Hub存储和分发恶意软件。他们还将受害者的计算能力出租给第三方，有效地通过加密货币挖矿间接赚钱，而无需自己管理。此外，他们还采用了新的黑客工具，用更隐蔽的Sliver恶意软件取代了传统的Tsunami后门[4]。

**·地平线上的乌云：TeamTNT的复苏？**

研究人员发现了TeamTNT新的活动影响基于CentOS操作系统的VPS云基础设施的明确证据。调查显示，初始访问是通过对受害者资产进行安全外壳(SSH)暴力破解实现的，在此期间威胁行为者上传了恶意脚本。恶意脚本在搜索现有矿工时会禁用安全功能、删除日志并修改系统文件。还会终止加密货币挖掘过程、删除Docker容器并更新Google服务器的DNS设置。安装Diamorphine工具包以实现隐藏和root权限，并使用自定义工具来维持持久性和控制。通过修改文件属性、创建具有root访问权限的后门用户以及删除命令历史记录来锁定系统，以隐藏其活动[5]。

**4.4 H2Miner**

H2Miner挖矿木马最早出现于2019年12月，爆发初期及此后一段时间该挖矿木马都是针对Linux平台，直到2020年11月后，开始利用WebLogic漏洞针对Windows平台进行入侵并植入对应挖矿程序。此外，该挖矿木马频繁利用其他常见Web组件漏洞，入侵相关服务器并植入挖矿程序。例如，2021年12月，攻击者利用Log4j漏洞实施了H2Miner挖矿木马的投放。

**4.4.1组织概览**

表 4‑4 H2Miner挖矿组织介绍

|  |  |
| --- | --- |
| 组织名称 | H2Miner/Kinsing |
| 出现时间 | 2019年12月 |
| 针对平台 | Windows、Linux |
| 传播方式 | 漏洞利用 |
| 利用的漏洞 | Looney Tunables特权升级漏洞  Apache ActiveMQ RCE漏洞（CVE-2023-46604）  Apache Solr’s   DataImportHandler (CVE-2019-0193)  Redis未授权RCE  Confluence未授权RCE(CVE-2019-3396)  WebLogic RCE漏洞(CVE-2020-14882/14883)  Log4j漏洞(CVE-2021-44228)  …… |
| 挖矿币种 | 门罗币（XMR） |

**4.4.2典型案例**

·Kinsing组织将新披露的漏洞集成到漏洞利用库中并扩展其僵尸网络

Kinsing组织将新披露的漏洞集成到漏洞利用库中并扩展其僵尸网络。该组织自2019年以来积极策划非法加密货币挖矿活动。近年来，涉及基于Golan...