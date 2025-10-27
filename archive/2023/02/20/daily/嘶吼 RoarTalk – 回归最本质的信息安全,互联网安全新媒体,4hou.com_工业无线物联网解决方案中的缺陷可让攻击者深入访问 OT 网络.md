---
title: 工业无线物联网解决方案中的缺陷可让攻击者深入访问 OT 网络
url: https://www.4hou.com/posts/ykqP
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-20
fetch_date: 2025-10-04T07:31:46.660015
---

# 工业无线物联网解决方案中的缺陷可让攻击者深入访问 OT 网络

工业无线物联网解决方案中的缺陷可让攻击者深入访问 OT 网络 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 工业无线物联网解决方案中的缺陷可让攻击者深入访问 OT 网络

丝绸之路
[新闻](https://www.4hou.com/category/news)
2023-02-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)157904

收藏

导语：更多地使用工业蜂窝网关和路由器会使 IIoT 设备暴露给攻击者并增加 OT 网络的攻击面。

![20230211123217.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230217/1676616790693547.jpeg "1676090032121551.jpeg")

![]()

运营技术 (OT) 团队通常通过无线和蜂窝解决方案将工业控制系统 (ICS) 连接到远程控制和监控中心，这些解决方案有时带有供应商运行的基于云的管理界面。这些连接解决方案，也称为工业无线物联网设备，增加了 OT 网络的攻击面，并且可以为远程攻击者提供进入包含关键控制器的先前分段网络段的捷径。

工业网络安全公司 Otorio 最近发布了一份报告，强调了这些设备容易受到的攻击向量以及该公司的研究人员在几种此类产品中发现的漏洞。Otorio 研究人员在他们的报告中说：“工业无线物联网设备及其基于云的管理平台是攻击者在工业环境中寻找初步立足点的有吸引力的目标。” “这是由于对漏洞利用和潜在影响的最低要求。”

**传统 OT 网络架构的转变**

OT 安全通常遵循 Purdue 企业参考架构 (PERA)模型来决定在何处放置强大的访问控制层并进行分段。该模型可追溯到 1990 年代，将企业 IT 和 OT 网络分为六个功能级别。

0 级是直接影响物理过程的设备，包括阀门、电机、执行器和传感器等。

第 1 层或基本控制层包括现场控制器，例如可编程逻辑控制器 (PLC) 和远程终端单元 (RTU)，它们根据工程师上传的逻辑（程序）控制这些传感器、阀门和执行器。

第 2 层是监督控制层，包括监督控制和数据采集 (SCADA) 系统，这些系统收集从第 1 层控制器接收到的数据并根据这些数据采取行动。

第 3 层是现场控制层，包括直接支持工厂运营的系统，例如数据库服务器、应用程序服务器、人机界面、用于对现场控制器进行编程的工程工作站等。这通常称为控制中心，并通过非军事区 (DMZ) 连接到组织的通用 IT 企业网络（第 4 级）。

正是在这个 DMZ 中，组织将他们的边界安全工作集中在其网络的 IT 和 OT 部分之间。额外的控制通常放在 3 级和 2 级之间，以保护现场设备免受入侵控制中心。

然而，一些组织可能有远程工业装置，他们需要连接到他们的中央控制中心。这在天然气和石油等行业更为常见，运营商在不同地点拥有多个油田和气井，但它在其他行业也很普遍。远程 0-2 级设备和 3 级控制系统之间的这些链接通常由工业蜂窝网关或工业 Wi-Fi 接入点提供。

这些工业无线物联网设备可以通过多种协议（如 Modbus 和 DNP3）与现场设备通信，然后使用各种安全通信机制（如 VPN）通过互联网连接回组织的控制中心。许多设备制造商还为工业资产所有者提供基于云的管理界面，以远程管理他们的设备。

**工业无线物联网设备中的漏洞**

这些与连接到互联网的任何其他设备一样，增加了 OT 网络的攻击面并削弱了组织传统上实施的安全控制，为攻击者提供了进入 OT 网络较低级别的旁路。Otorio 研究人员在他们的报告中说：“利用 Shodan 等搜索引擎，我们观察到工业蜂窝网关和路由器的广泛暴露，使它们很容易被发现并且可能容易受到威胁行为者的利用。” 他们关于具有可访问互联网的 Web 服务器和接口的设备的一些发现包括：

|  |  |  |
| --- | --- | --- |
| 攻击向量 | 数量 | 过滤器 |
| Sierra Wireless | 96,715 | http.title:ACEmanager |
| Teltonika Networks | 37,100 | http.title:Teltonika |
| InHand Networks | 13,990 | http.html:"Login failed! Check  your username & password" |
| Moxa | 1,782 | http.html:"MOXA OnCell" |
| ETIC Telecom | 1,538 | http.html:"ETIC TELECOM" |

研究人员声称，他们在来自其中三个供应商（Sierra、InHand 和 ETIC）的设备的基于 Web 的界面中发现了 24 个漏洞，并设法在所有这三个供应商上实现了远程代码执行。

虽然其中许多漏洞仍在负责任地披露过程中，但已经修补的漏洞影响了 Sierra Wireless AirLink 路由器，并被跟踪为 CVE-2022-46649。这是路由器基于 Web 的管理界面 ACEManager 的 IP 日志记录功能中的一个命令注入漏洞，是 Talos 研究人员在 2018 年发现的另一个漏洞的变体，该漏洞被追踪为 CVE-2018-4061。

事实证明，Sierra 为解决 CVE-2018-4061 而实施的过滤并未涵盖所有漏洞利用场景，Otorio 的研究人员能够绕过它。在 CVE-2018-4061 中，攻击者可以使用 -z 标志将额外的 shell 命令附加到由 ACEManager iplogging.cgi 脚本执行的 tcpdump 命令。此标志由命令行 tcpdump 实用程序支持，用于传递所谓的 postrotate 命令。Sierra 通过执行一个过滤器来修复它，该过滤器从传递给 iplogging 脚本的命令中删除任何 -z 标志，如果它后面跟着空格，制表符，换页符或垂直制表符，这将阻止，例如，“tcpdump -z reboot ”。

根据 Otorio 的说法，他们错过的是 -z 标志后面不需要任何这些字符，并且像“tcpdump -zreboot”这样的命令可以很好地执行并绕过过滤。单靠这种绕过仍然会限制攻击者执行设备上已经存在的二进制文件，因此研究人员开发了一种方法，将他们的有效负载隐藏在通过另一个名为 iplogging\_upload.cgi 的 ACEManager 功能上传到设备的 PCAP（包捕获）文件中。这个特制的 PCAP 文件在被 sh（shell 解释器）解析时也可以充当 shell 脚本，并且可以通过使用 iplogging.cgi 中的 -z 漏洞触发其解析和执行。

**云管理风险**

即使这些设备不将其基于 Web 的管理界面直接暴露给互联网（这不是一种安全的部署做法），远程攻击者也不会完全无法访问它们。这是因为大多数供应商都提供基于云的管理平台，允许设备所有者执行配置更改、固件更新、设备重启、设备上的隧道流量等。

这些设备通常使用 MQTT 等机器对机器 (M2M) 协议与这些云管理服务进行通信，它们的实现可能存在弱点。Otorio 研究人员在三个供应商的云平台中发现了严重漏洞，允许攻击者在无需身份验证的情况下远程破坏任何云管理设备。

“通过针对单一供应商基于云的管理平台，远程攻击者可能会暴露位于不同网络和部门的数千台设备，”研究人员说。“云管理平台的攻击面很广。它包括利用 Web 应用程序（云用户界面）、滥用 M2M 协议、薄弱的访问控制策略或滥用薄弱的注册过程。”

研究人员通过他们在 InHand Networks 的“设备管理器”云平台及其 InRouter 设备的固件中发现的一系列三个漏洞来举例说明这些风险，这些漏洞可能导致在所有云管理的 InRouter 设备上以 root 权限远程执行代码。

首先，他们研究了设备通过 MQTT 与平台对话的方式以及实现身份验证或“注册”的方式，他们发现注册使用的随机值不够充分，并且可能被强制执行。换句话说，其中两个漏洞允许研究人员通过模拟经过身份验证的连接并向路由器写入任务（例如更改其主机名）来强制路由器提供其配置文件。

第三个漏洞是路由器通过 MQTT 解析配置文件的方式，特别是在用于解析名为 auto\_ping 的功能参数的函数中。研究人员发现他们可以启用 auto\_ping，然后将反向 shell 命令行连接到 auto\_ping\_dst 函数，这将在设备上以 root 权限执行。

**对 OT 网络的无线攻击**

除了互联网上可用的远程攻击媒介之外，这些设备还在本地暴露 Wi-Fi 和蜂窝信号，因此可以利用这些技术对它们进行任何攻击。“可以对 Wi-Fi 和蜂窝通信通道使用不同类型的本地攻击，从对 WEP 等弱加密的攻击和对易受攻击的 GPRS 的降级攻击开始，一直到可能需要时间修补的复杂芯片组漏洞，”研究人员说。

虽然研究人员没有调查 Wi-Fi 或蜂窝基带调制解调器漏洞，但他们使用 WiGLE 进行了侦察，WiGLE 是一种公共无线网络映射服务，可收集全球无线接入点的信息。“利用高级过滤选项，我们编写了一个 Python 脚本扫描潜在的高价值工业或关键基础设施环境，突出显示配置了弱加密的环境，”研究人员说。“我们的扫描发现了数千个与工业和关键基础设施相关的无线设备，其中数百个配置了众所周知的弱加密。”

使用这种技术，研究人员设法在现实世界中的制造厂、油田、变电站和水处理设施中找到部署了弱无线加密的设备。攻击者可以使用这种侦察来识别薄弱的设备，然后前往现场利用它们。

**缓解无线物联网设备漏洞**

由于此类设备在 OT 网络中的特权地位和对关键控制器的直接访问权限，因此在发现此类设备中的漏洞时对其进行修补非常重要，因此应采取额外的预防措施来降低风险。Otorio 研究人员有以下建议：

禁用并避免任何不安全的加密（WEP、WAP），并且在可能的情况下，不允许使用 GPRS 等旧协议。

隐藏您的网络名称 (SSID)。

对连接的设备使用基于 MAC 的白名单，或使用证书。

验证管理服务仅限于 LAN 接口或 IP 白名单。

确保没有使用默认凭据。

警惕您设备的新安全更新。

确认这些服务在未使用时被禁用（在许多情况下默认启用）。

单独实施安全解决方案（VPN、防火墙），将来自 IIoT 的流量视为不受信任。

本文翻译自：https://www.csoonline.com/article/3687735/flaws-in-industrial-wireless-iot-solutions-can-give-attackers-deep-access-into-ot-networks.html#tk.rss\_all如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?X7zzdJkf)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/wp-content/uploads/2017/06/7d0f41b6202b24cb61e4.jpg)

# [丝绸之路](https://www.4hou.com/member/dwVJ)

这个家伙什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/dwVJ)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?t...