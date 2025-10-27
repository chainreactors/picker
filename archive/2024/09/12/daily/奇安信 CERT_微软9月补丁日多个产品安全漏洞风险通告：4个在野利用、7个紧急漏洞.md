---
title: 微软9月补丁日多个产品安全漏洞风险通告：4个在野利用、7个紧急漏洞
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502059&idx=1&sn=2a4c7dc68382398f1e644be7ef2820e7&chksm=fe79ec73c90e656573c8297ab60ed4699b08361a5cf6fbcf954b080a5f0fb8d7c32f13070418&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-09-12
fetch_date: 2025-10-06T18:28:44.971790
---

# 微软9月补丁日多个产品安全漏洞风险通告：4个在野利用、7个紧急漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icGW7QGibPy1K2LXzM7L68KbATupTtuDiaWy5BQ1p6Bh7MLb1qKESK50WYcGWPACS9qLuq6hHpKSQicQ/0?wx_fmt=jpeg)

# 微软9月补丁日多个产品安全漏洞风险通告：4个在野利用、7个紧急漏洞

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 微软2024年9月补丁日多个产品安全漏洞 | | |
| **影响产品** | Windows Win32k、Windows Installer、Microsoft SharePoint Server 和 Microsoft Publisher等。 | | |
| ****公开时间**** | 2024-09-11 | ****影响对象数量级**** | 千万级 |
| **奇安信评级** | **高危** | **利用可能性** | **高** |
| **POC状态** | 未公开 | **在野利用状态** | **部分发现** |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**攻击者利用这些漏洞，可造成权限提升、远程代码执行等。 | | | |

**0****1**

**漏洞详情**

本月，微软共发布了79个漏洞的补丁程序，修复了Windows Win32k、Windows Installer、Microsoft SharePoint Server 和 Microsoft Publisher等产品中的漏洞。经研判，以下27个重要漏洞值得关注（包括7个紧急漏洞、19个重要漏洞、1个中等），如下表所示：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **编号** | **漏洞名称** | **风险等级** | **公开状态** | **利用可能** |
| CVE-2024-43491 | Microsoft Windows 更新远程代码执行漏洞 | 紧急 | 未公开 | **在野利用** |
| CVE-2024-38217 | Windows Web 查询标记安全功能绕过漏洞 | 重要 | **已公开** | **在野利用** |
| CVE-2024-38226 | Microsoft Publisher 安全功能绕过漏洞 | 重要 | 未公开 | **在野利用** |
| CVE-2024-38014 | Windows Installer 权限提升漏洞 | 重要 | 未公开 | ****在野利用**** |
| CVE-2024-43464 | Microsoft SharePoint Server 远程代码执行漏洞 | 紧急 | 未公开 | **较大** |
| CVE-2024-38018 | Microsoft SharePoint Server 远程代码执行漏洞 | 紧急 | 未公开 | ****较大**** |
| CVE-2024-38119 | Windows 网络地址转换 (NAT) 远程代码执行漏洞 | 紧急 | 未公开 | **较小** |
| CVE-2024-38194 | Azure Web 应用权限提升漏洞 | 紧急 | 未公开 | ****较小**** |
| CVE-2024-38220 | Azure Stack Hub 权限提升漏洞 | 紧急 | 未公开 | ****较小**** |
| CVE-2024-38216 | Azure Stack Hub 权限提升漏洞 | 紧急 | 未公开 | ****较小**** |
| CVE-2024-38246 | Win32k 权限提升漏洞 | 重要 | 未公开 | ****较大**** |
| CVE-2024-38243 | 内核流式处理服务驱动程序权限提升漏洞 | 重要 | 未公开 | ****较大**** |
| CVE-2024-38237 | Kernel Streaming WOW Thunk 服务驱动程序权限提升漏洞 | 重要 | 未公开 | ****较大**** |
| CVE-2024-38249 | Windows 图形组件权限提升漏洞 | 重要 | 未公开 | ****较大**** |
| CVE-2024-43461 | Windows MSHTML Platform 欺骗漏洞 | 重要 | 未公开 | ****较大**** |
| CVE-2024-43457 | Windows 安装和部署权限提升漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38247 | Windows 图形组件权限提升漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38245  CVE-2024-38244  CVE-2024-38238 | 内核流式处理服务驱动程序权限提升漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38228 | Microsoft SharePoint Server 远程代码执行漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38227 | Microsoft SharePoint Server 远程代码执行漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38253 | Windows Win32 内核子系统权限提升漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38252 | Windows Win32 内核子系统权限提升漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38242 | 内核流式处理服务驱动程序代码执行漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-38241 | 内核流式处理服务驱动程序权限提升漏洞 | 重要 | 未公开 | **较大** |
| CVE-2024-43487 | Windows Web 查询标记安全功能绕过漏洞 | 中 | 未公开 | **较大** |

**02**

**重点关注漏洞**

**>****>****>****>**

**更容易被利用漏洞**

以下23个漏洞被微软标记为 “Exploitation Detected”或“Exploitation More Likely”，这代表这些漏洞已遭利用或更容易被利用：

* CVE-2024-38237 Kernel Streaming WOW Thunk 服务驱动程序权限提升漏洞
* CVE-2024-38226 Microsoft Publisher 安全功能绕过漏洞
* CVE-2024-43464 Microsoft SharePoint Server 远程代码执行漏洞
* CVE-2024-38018 Microsoft SharePoint Server 远程代码执行漏洞
* CVE-2024-38228 Microsoft SharePoint Server 远程代码执行漏洞
* CVE-2024-38227 Microsoft SharePoint Server 远程代码执行漏洞
* CVE-2024-43491 Microsoft Windows 更新远程代码执行漏洞
* CVE-2024-38246 Win32k 权限提升漏洞
* CVE-2024-38014 Windows Installer 权限提升漏洞
* CVE-2024-43461 Windows MSHTML Platform 欺骗漏洞
* CVE-2024-38217 Windows Web 查询标记安全功能绕过漏洞
* CVE-2024-43487 Windows Web 查询标记安全功能绕过漏洞
* CVE-2024-38253 Windows Win32 内核子系统权限提升漏洞
* CVE-2024-38252 Windows Win32 内核子系统权限提升漏洞
* CVE-2024-38249 Windows 图形组件权限提升漏洞
* CVE-2024-38247 Windows 图形组件权限提升漏洞
* CVE-2024-43457 Windows 安装和部署权限提升漏洞
* CVE-2024-38243 内核流式处理服务驱动程序权限提升漏洞
* CVE-2024-38245 内核流式处理服务驱动程序权限提升漏洞
* CVE-2024-38244 内核流式处理服务驱动程序权限提升漏洞
* CVE-2024-38238 内核流式处理服务驱动程序权限提升漏洞
* CVE-2024-38242 内核流式处理服务驱动程序代码执行漏洞
* CVE-2024-38241 内核流式处理服务驱动程序权限提升漏洞

CVE-2024-38248 Windows 存储特权提升漏洞由奇安信天工实验室安全研究员发现并提交。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icAgzicLAYAejGPQa4HzNZuZ4zDeY1y4wibS5pwWql1icwYszSQR4KqsAcsiadmFKbAQJNeT8eibWvWoYw/640?wx_fmt=png&from=appmsg)

**鉴于这些漏洞危害较大，建议客户尽快安装更新补丁。**

**>****>****>****>**

**重点关注漏洞详情**

经研判，以下27个漏洞值得关注，漏洞的详细信息如下：

**1、CVE-2024-43491 Microsoft Windows 更新远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft Windows 更新远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-43491 |
| **公开状态** | 未公开 | **在野利用** | **已发现** | | |
| **漏洞描述** | 该漏洞允许远程攻击者入侵易受攻击的系统。该漏洞是由于 Microsoft Windows 更新服务中的释放后使用错误而产生的。远程攻击者可以向系统发送特制的流量，触发释放后使用错误并执行任意代码。成功利用该漏洞可能允许攻击者入侵易受攻击的系统。**该漏洞已存在在野利用。** | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-43491 | | | | | |

**2、CVE-2024-38217 Windows Web 查询标记安全功能绕过漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows Web 查询标记安全功能绕过漏洞 | | | | |
| **漏洞类型** | 安全特性绕过 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-38217 |
| **公开状态** | **公开** | **在野利用** | **已发现** | | |
| **漏洞描述** | 该漏洞允许远程攻击者绕过已实施的安全限制。该漏洞是由于安全措施实施不足而存在的。攻击者可以诱骗受害者下载特制文件，逃避 Web 标记 (MOTW) 防御并绕过安全功能，例如 SmartScreen 应用程序信誉安全检查和/或旧版 Windows 附件服务安全提示。**该漏洞已存在在野利用。** | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38217 | | | | | |

**3、CVE-2024-38226 Microsoft Publisher 安全功能绕过漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft Publisher 安全功能绕过漏洞 | | | | |
| **漏洞类型** | 安全特性绕过 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-38226 |
| **公开状态** | 未公开 | **在野利用** | **已发现** | | |
| **漏洞描述** | 该漏洞允许远程攻击者绕过已实施的安全限制。该漏洞是由于安全措施实施不足而导致的。攻击者可以诱骗受害者打开特制文件，绕过 Office 宏策略限制并在系统上执行任意代码。**该漏洞已存在在野利用。** | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38226 | | | | | |

**4、CVE-2024-38014 Windows Installer 权限提升漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows Installer 权限提升漏洞 | | | | |
| **漏洞类型** | 权限提升 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-38014 |
| **公开状态** | 未公开 | **在野利用** | **已发现** | | |
| **漏洞描述** | 该漏洞允许本地用户提升系统权限。该漏洞是由于 Windows Installer 中的权限管理不当而导致的。本地用户可以使用 SYSTEM 权限执行任意代码。**该漏洞已存在在野利用。** | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38014 | | | | | |

**5、Microsoft SharePoint Server 远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft SharePoint Server 远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-43464  CVE-2024-38018 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程用户在目标系统上执行任意代码。该漏洞是由于在 Microsoft SharePoint Server 中处理序列化数据时输入验证不安全而导致的。远程管理员可以将特制数据传递给应用程序并在目标系统上执行任意代码。成功利用此漏洞可能导致易受攻击的系统完全被攻陷。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-43464  https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38018 | | | | | |

**6、CVE-2024-38119 Windows 网络地址转换 (NAT) 远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows 网络地址转换 (NAT) 远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-38119 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程攻击者破坏易受攻击的系统。该漏洞是由于 Windows 网络地址转换 (NAT) 中的释放后使用错误而存在的。本地网络上的远程攻击者可以在目标系统上执行任意代码。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38119 | | | | | |

**7、CVE-2024-38194 Azure Web 应用权限提升漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Azure Web 应用权限提升漏洞 | | | | |
| **漏洞类型** | 权限提升 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-38194 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程攻击者提升系统权限。该漏洞是由于 Azure Web Apps 对用户提供的输入验证不足而导致的。远程用户可以将特制的输入传递给应用程序，并在目标系统上获得提升的权限。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38194 | | | | | |

**8、CVE-2024-38220 Azure Stack Hub 权限提升漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Azure Stack Hub 权限提升漏洞 | | | | |
| **漏洞类型** | 权限提升 | **风险等级...