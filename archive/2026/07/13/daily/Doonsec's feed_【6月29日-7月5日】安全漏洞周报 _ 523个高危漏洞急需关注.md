---
title: 【6月29日-7月5日】安全漏洞周报 | 523个高危漏洞急需关注
url: https://mp.weixin.qq.com/s/nDiZgxmuTvQncJH95tlOEw
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:44:05.597860
---

# 【6月29日-7月5日】安全漏洞周报 | 523个高危漏洞急需关注

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HJOl681LKxoSG7dPuc8tnc3ibbYlebSak7bdptxos0ZZVDAIOkpc9Sibz2u1wfxzKNMqO9JLpB376XLprdgfhslVV6SYQ0CqbHtmQCGibF0Dpw/0?wx_fmt=jpeg)

# 【6月29日-7月5日】安全漏洞周报 | 523个高危漏洞急需关注

原创

POP Star安全
POP Star安全

POP Star安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/xibib30LehV0twhDUK41GLianurdvtBEskQdVOqNMjgkkia4pXBqLnyIXiaO7iaFAm3do8R069HUOTAiaogavd89RbUIA/640?wx_fmt=gif&from=appmsg)

**点击关注 获取更多实时安全资讯**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HJOl681LKxozBSsJuKJAZm6HzrFaKeU6POYFEC45XK4ThibyWicA8xLYoVs2VWj4sPaftaDUuoVSsbXibiaxoj2TVak3R4EiaU87ib6icnU8NYTOiaA/640?wx_fmt=png&from=appmsg)

**安全漏洞周报**

523个漏洞需紧急关注

**5分钟掌握一周威胁**

**6月29日~7月5日**

**本期核心提示**

**本周重点**：

高危漏洞**289个**

中危漏洞**180个**

低危漏洞**54个**

**核心政策：**

* 全国网络安全标准化技术委员会秘书处发布《网络安全标准实践指南——智能体部署使用安全指引》。
* 国家能源局发布《能源行业数据分类分级指南（2026年版）》。
* 工业和信息化部等八部门联合印发《关于推动工业互联网高质量发展的实施意见》。
* 中央网络安全和信息化委员会办公室就《政务移动互联网应用程序管理要求》强制性国家标准公开征求意见。
* 美国众议院议员联合提出《云安全法案》。

**1**

**本周关键漏洞速览**

|  |  |  |  |
| --- | --- | --- | --- |
| **排名** | **漏洞编号** | **受影响产品** | **CVSS 3.x Base Score** |
| 1 | CVE-2025-20362 | Cisco Secure ASA & FTD | 6.5 |
| 2 | CVE-2025-5777 | Citrix NetScalerADC | 7.5 |
| 3 | CVE-2025-53364 | Parse Server | 5.3 |
| 4 | CVE-2025-47204 | Bootstrap Multiselect | 6.1 |
| 5 | CVE-2025-30567 | WordPress WP01 | 7.5 |

**本周漏洞小结**

本周，Google产品被披露存在多个漏洞，攻击者可利用漏洞通过恶意外设在受影响系统上执行任意代码，通过特制HTML页面在沙盒内执行任意代码，发送特制RTP文本数据，在目标设备上执行任意代码等。此外，Apple、Fortinet、Mozilla等多款产品被披露存在多个漏洞，攻击者可利用漏洞在处理恶意USD文件时导致应用意外终止，导致应用绕过App隐私报告日志记录，通过诱导用户访问恶意网站导致敏感数据泄露，通过特制的HTTP请求执行未授权命令，实现未授权的访问控制操作，通过特制数据包执行未经授权的代码或命令，窃取受害者基于cookie的身份验证凭据，提升特权，在系统上执行任意代码，导致拒绝服务等。另外，D-Link DIR-513被披露存在堆栈缓冲区溢出漏洞。该漏洞源于formTcpipSetup函数未能正确验证输入数据的长度大小。攻击者可利用该漏洞在系统上执行任意代码或者导致拒绝服务。建议相关用户随时关注上述厂商主页，及时获取修复补丁或解决方案。

**0****2**

**本周高危漏洞清单**

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | WordPress plugin Masteriyo LMS PRO 安全漏洞 | 厂商 | WordPress |
| 漏洞编号 | CNNVD202606-553 | 危害等级 | **超危** |
| CVE ID | CVE-2025-53209 | 漏洞类型 | 其他 |

**漏洞简介**

WordPress和WordPress plugin都是WordPress基金会的产品。WordPress是一套使用PHP语言开发的博客平台。该平台具有在基于PHP和MySQL的服务器上架设个人博客网站的功能。WordPress plugin是一个应用插件。

WordPress plugin Masteriyo LMS PRO 2.20.0及之前版本存在安全漏洞，该漏洞源于权限分配不当，可能导致权限提升。

**官方补丁****：**

https://wordpress.org/plugins/

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | pache ActiveMQ 安全漏洞 | 影响产品 | Apache |
| 漏洞编号 | CNNVD-202606-293 | 危害等级 | **高危** |
| CVE ID | CVE-2026-45505 | 漏洞类型 | 其他 |

**漏洞简介**

Apache ActiveMQ是美国阿帕奇（Apache）基金会的一套开源的消息中间件，它支持Java消息服务、集群、Spring Framework等。

Apache ActiveMQ存在安全漏洞，该漏洞源于输入验证不当和代码生成控制不当，可能导致已认证攻击者通过特制发现URI触发VM传输的brokerConfig参数加载远程Spring XML应用上下文，从而在代理JVM上执行任意代码。以下版本受到影响：Apache ActiveMQ Broker 5.19.7之前版本和6.0.0版本至6.2.6之前版本、Apache ActiveMQ All 5.19.7之前版本和6.0.0版本至6.2.6之前版本以及Apache ActiveMQ 5.19.7之前版本和6.0.0版本至6.2.6之前版本。

**官方补丁**：

https://lists.apache.org/thread/7n97nddyw96w6ykldjv1h40 jx86xdo0w

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | Google Chrome 资源管理错误漏洞 | 厂商 | Google |
| 漏洞编号 | CNNVD-202606-900 | 危害等级 | **高危** |
| CVE ID | CVE-2026-11164 | 漏洞类型 | 资源管理错误 |

**漏洞简介**

Google Chrome是美国谷歌（Google）公司的一款Web浏览器。Google Chrome 149.0.7827.53之前版本存在资源管理错误漏洞，该漏洞源于内存释放后重用，攻击者利用该漏洞可以通过特制HTML页面在沙箱内执行任意代码。

**官方补丁****：**

https://chromereleases.googleblog.com/2026/06/stablechannel-update-for-desktop.html

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | Linux kernel内存破坏漏洞 | 影响产品 | Linux Kernel |
| 漏洞编号 | CNVD-2026-26372 | 危害等级 | **高危** |
| CVE ID | CVE-2026-53284 | 漏洞类型 | 通用型漏洞 |

**漏洞简介**

Linux kernel是Linux操作系统的内核，负责管理系统资源、进程调度、文件系统等功能。
Linux kernel存在内存破坏漏洞。该漏洞产生的原因是btrfs模块在写入未成功时提前释放脏页面IO树，导致extent buffer状态错误。攻击者可利用该漏洞通过触发特定文件系统操作导致内核内存破坏。

**官方****补丁：**https://git.kernel.org/stable/c/9ebb7eba1237dc198768b9c76506a79f924c82bb

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | 多款Mozilla产品处理逻辑错误漏洞 | 厂商 | Mozilla |
| 漏洞编号 | CNVD-2026-26387 | 危害等级 | **高危** |
| CVE ID | CVE-2026-12296 | 漏洞类型 | 通用型漏洞 |

**漏洞简介**

Mozilla Firefox是一款开源Web浏览器。Mozilla Firefox ESR是Firefox（Web浏览器）的一个延长支持版本。Mozilla Thunderbird是一套从Mozilla Application Suite独立出来的电子邮件客户端软件。

多款Mozilla产品存在处理逻辑错误漏洞，攻击者可利用该漏洞导致沙箱逃逸。

**官****方补丁：**

https://www.mozilla.org/security/advisories/mfsa2026-57/

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | Fortinet FortiSandbox OS命令注入漏洞 | 厂商 | Fortinet |
| 漏洞编号 | CNVD-2026-25587 | 危害等级 | **高危** |
| CVE ID | CVE-2026-25089 | 漏洞类型 | 通用型漏洞 |

**漏洞简介**

FortiSandbox是一款由Fortinet提供的安全沙箱产品，主要用于检测和分析恶意软件。

Fortinet FortiSandbox存在OS命令注入漏洞。该漏洞源于未能正确中和OS命令中使用的特殊元素，攻击者可利用该漏洞通过特制的HTTP请求执行未授权命令。

**官方补丁：**

https://fortiguard.fortinet.com/psirt/FG-IR-26-141

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | Oracle WebCenter Sites权限许可和访问控制问题漏洞 | 厂商 | Oracle Fusion Middleware |
| 漏洞编号 | CNVD-2026-26210 | 危害等级 | **高危** |
| CVE ID | CVE-2026-35318 | 漏洞类型 | 通用型漏洞 |

**漏洞简介**

Oracle WebCenter Sites是Oracle Fusion Middleware中的一个内容管理系统组件，主要用于网站内容管理和发布。

Oracle WebCenter Sites存在安全漏洞。该漏洞源于未能正确处理用户权限验证，攻击者可利用该漏洞通过HTTP入侵系统，导致完全接管Oracle WebCenter Sites，影响机密性、完整性和可用性。

**官方补丁：**

https://www.oracle.com/security-alerts/cspujun2026.html

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | Google Chrome Bluetooth内存错误引用漏洞 | 厂商 | Google |
| 漏洞编号 | CNVD-2026-25581 | 危害等级 | **高危** |
| CVE ID | CVE-2026-13035 | 漏洞类型 | 通用型漏洞 |

**漏洞简介**

Google Chrome是一款由Google开发的跨平台网页浏览器，主要提供网页浏览、扩展支持及多平台同步功能。
Google Chrome存在内存错误引用漏洞，该漏洞源于Bluetooth组件未能正确管理内存生命周期，攻击者可利用该漏洞通过恶意外设在受影响系统上执行任意代码。

**官方补丁：**

https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop\_0482630350.html

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | MLflow 安全漏洞 | 厂商 | MLflow |
| 漏洞编号 | CNNVD-202606-737 | 危害等级 | **高危** |
| CVE ID | CVE-2026-4035 | 漏洞类型 | 其他 |

**漏洞简介**

MLflow是MLflow开源的一个简化机器学习开发的平台，包括跟踪实验、将代码打包成可重复的运行以及共享和部署模型。

MLflow 3.11.0之前版本存在安全漏洞，该漏洞源于AI Gateway secrets中环境变量解析问题，可能导致敏感凭据泄露。

**官****方补丁：**

https://mlflow.org/

**0****3**

**本周****漏洞威胁情报**

##

## **Microsoft SharePoint Server 反序列化漏洞**

## **(CVE-2026-45659)**

**事件概述:**

7月1日，美国网络安全和基础设施安全局(CISA)将微软SharePoint Server反序列化漏洞CVE-2026-45659（有证据表明该漏洞已被利用）添加到其“已知已利用漏洞目录”中，这迫使有关机构和暴露SharePoint系统的私营团队加快修复速度。该漏洞条目数量虽少，但影响巨大。它再次提醒我们，最危险的Windows相关企业风险往往并非存在于桌面，而是存在于每个人都默默信任的协作服务器中。SharePoint再次成为补丁管理演变为事件响应的典型案例。

该漏洞被描述为Microsoft Office SharePoint中不受信任数据的反序列化，允许授权攻击者通过网络执行代码。简而言之，SharePoint可能被诱骗重建数据，使其比服务器原本应该接受的数据更加危险。攻击者需要一定程度的授权，但网络可达性、攻击复杂度低以及无需用户交互等特点，正是令防御者警惕的典型特征。

“授权攻击者”这一表述不应让人掉以轻心。在企业环境中，有效的凭据并非稀缺资源；这些漏洞通常是网络钓鱼、令牌窃取、密码重用、权限过高的服务帐户以及无人愿意禁用的休眠帐户（因为禁用帐户可能会导致工作流程中断）等攻击的副产品。即使 SharePoint 漏洞发生在身份验证之后，它仍然可以加速初始访问或入侵后的攻击。

受影响的产品系列是常见的本地部署SharePoint Server环境：SharePoint Server 订阅版、SharePoint Server 2019和SharePoint Enterprise Server 2016。它不包括 SharePoint Online（因为SharePoint Online的补丁问题由客户自行管理），但它明确地指向了那些组织选择或被迫将协作基础架构保留在自身内部的环境。

对于管理员而言，建议尽快识别受影响的SharePoint服务器实例并应用相关的 Microsoft安全更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/xibib30LehV0twhDUK41GLianurdvtBEskQFjnHoxdzWWibibHKHq9oBaVoHo38AHfqevjj80HmPTDRbaQZU45yXtkA/640?wx_fmt=gif&from=appmsg)

## **SimpleHelp OIDC 身份验证绕过漏洞**

## **(CVE-2026-48558)**

**事件概述:**

6月30日，黑客正在利用最近披露的SimpleHelp中的严重漏洞(CVE-2026-48558)部署 Djinn Stealer，这是一个此前未记录的跨平台信息窃取程序，目标包括Windows、macOS和Linux。

SimpleHelp平台主要由托管服务提供商(MSP)、IT部门、服务台和系统管理员用于远程监控和管理(RMM)。本月初，攻击性安全公司Horizon3.ai公布了CVE-2026-48558的详细信息，称该漏洞可被利用来创建无需身份验证的高权限技术人员帐户。使用OpenID Connect(OIDC)身份验证协议的服务器可能存在被利用的漏洞。研究人员表示，在漏洞披露时，约有1000台暴露在外的SimpleHelp服务器运行着存在漏洞的配置。

在托管检测和响应(MDR)提供商Blackpoint调查的一起事件中，威胁行为者利用关键的身份验证绕过漏洞，在面向互联网的SimpleHelp服务器上建立了经过身份验证的技术人员会话，然后部署了TaskWeaver恶意软件加载器和Djinn Stealer。

Blackpoint表示，被攻破的RMM平台为操作员提供了一个可信的管理通道，能够传输文件并在通过服务器管理的系统上执行命令。调查显示，TaskWeaver是以名为“jquery.js”的混淆JavaScript文件的形式从临时Cloudflare域名下载的。TaskWeaver是一个通用的恶意软件加载器，它能够识别受感染的设备，并与命令与控制 (C2)基础设施通信，以接收新的JavaScript模块来执行。然后，加载器会安装Djinn Stealer，以便一次性收集开发者机器（无论是 Windows、macOS 还是 Linux）上能找到的所有敏感数据。

Djinn Stealer尤其专注于AI开发工具，但其目标用户群体广泛，涵盖开发者和基础设施凭证。在Linux系统上，该恶意软件还会尝试读取/proc/<pid>/cmdline和 /proc/<pid>/environ虚拟文件，其中包含有关正在运行的进程的信息，包括密钥（例如API密钥、凭据、会话令牌、文件路径、URL）。Blackpoint 的研究人员警告说，窃取广泛用于编码和软件开发的AI开发工具的凭证，可能会使攻击者获得AI助手对存储库、云资源、数据库和API的授权访问权限。

在将敏感数据泄露到C2服务器之前，D...