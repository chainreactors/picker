---
title: 微软7月补丁日多个产品安全漏洞风险通告：2个在野利用、5个紧急漏洞
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501618&idx=1&sn=9593ae978490bf55a9dbc632d4d83c6f&chksm=fe79e3aac90e6abce546a96abd8076691994f6ba44c7ae02a1177dfd09e9407f27e37d6403d7&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-11
fetch_date: 2025-10-06T17:44:35.152865
---

# 微软7月补丁日多个产品安全漏洞风险通告：2个在野利用、5个紧急漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs49NyUHsAHhWFMYoTwtuE29UuhOzD5yL6o2z2syhR9oRfkUO12nAmEMX5TFbNwp4uRLic1hJCWkhmLg/0?wx_fmt=jpeg)

# 微软7月补丁日多个产品安全漏洞风险通告：2个在野利用、5个紧急漏洞

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 微软2024年7月补丁日多个产品安全漏洞 | | |
| **影响产品** | Microsoft Office、Windows Hyper-V、Windows Imaging Component 和 Windows Win32K等。 | | |
| ****公开时间**** | 2024-7-10 | ****影响对象数量级**** | 千万级 |
| **奇安信评级** | **高危** | **利用可能性** | ****高**** |
| **POC状态** | 未公开 | **在野利用状态** | **部分发现** |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**攻击者利用这些漏洞，可造成权限提升、远程代码执行等。 | | | |

**0****1**

**漏洞详情**

本月，微软共发布了139个漏洞的补丁程序，修复了Microsoft Office、Windows Hyper-V、Windows Imaging Component 和 Windows Win32K等产品中的漏洞。经研判，以下19个重要漏洞值得关注（包括5个紧急漏洞、13个重要漏洞、1个中等），如下表所示：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **编号** | **漏洞名称** | **风险等级** | **公开状态** | **利用可能** |
| CVE-2024-38112 | Windows MSHTML Platform 欺骗漏洞 | 重要 | 未公开 | **在野利用** |
| CVE-2024-38080 | Windows Hyper-V 权限提升漏洞 | 重要 | 未公开 | **在野利用** |
| CVE-2024-38060 | Windows Imaging Component 远程代码执行漏洞 | **紧急** | 未公开 | 较大 |
| CVE-2024-38023 | Microsoft SharePoint Server 远程代码执行漏洞 | **紧急** | 未公开 | 较大 |
| CVE-2024-38077 | Windows 远程桌面授权服务远程代码执行漏洞 | **紧急** | 未公开 | 较小 |
| CVE-2024-38076 | Windows 远程桌面授权服务远程代码执行漏洞 | **紧急** | 未公开 | 较小 |
| CVE-2024-38074 | Windows 远程桌面授权服务远程代码执行漏洞 | **紧急** | 未公开 | 较小 |
| CVE-2024-38099 | Windows 远程桌面授权服务拒绝服务漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38094 | Microsoft SharePoint 远程代码执行漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38052 | Kernel Streaming WOW Thunk 服务驱动程序权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38021‍ | Microsoft Office 远程代码执行漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38085 | Windows 图形组件权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38079 | Windows 图形组件权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38066 | Windows Win32k 权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38100 | Windows 文件资源管理器权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38059 | Win32k 权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38054 | Kernel Streaming WOW Thunk 服务驱动程序权限提升漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-38024 | Microsoft SharePoint Server 远程代码执行漏洞 | 重要 | 未公开 | 较大 |
| CVE-2024-39684 | Github：TenCent RapidJSON 权限提升漏洞 | 中 | 未公开 | 较大 |

**02**

**重点关注漏洞**

**>****>****>****>**

**更容易被利用漏洞**

以下16个漏洞被微软标记为 “Exploitation Detected”或“Exploitation More Likely”，这代表这些漏洞已遭利用或更容易被利用：

* CVE-2024-39684 Github：TenCent RapidJSON 权限提升漏洞
* CVE-2024-38052 Kernel Streaming WOW Thunk 服务驱动程序权限提升漏洞
* CVE-2024-38054 Kernel Streaming WOW Thunk 服务驱动程序权限提升漏洞
* CVE-2024-38021 Microsoft Office 远程代码执行漏洞
* CVE-2024-38023 Microsoft SharePoint Server 远程代码执行漏洞
* CVE-2024-38024 Microsoft SharePoint Server 远程代码执行漏洞
* CVE-2024-38094 Microsoft SharePoint 远程代码执行漏洞
* CVE-2024-38059 Win32k 权限提升漏洞
* CVE-2024-38080 Windows Hyper-V 权限提升漏洞
* CVE-2024-38060 Windows Imaging Component 远程代码执行漏洞
* CVE-2024-38112 Windows MSHTML Platform 欺骗漏洞
* CVE-2024-38066 Windows Win32k 权限提升漏洞
* CVE-2024-38085 Windows 图形组件权限提升漏洞
* CVE-2024-38079 Windows 图形组件权限提升漏洞
* CVE-2024-38100 Windows 文件资源管理器权限提升漏洞
* CVE-2024-38099 Windows 远程桌面授权服务拒绝服务漏洞

CVE-2024-38104 Windows 传真服务远程代码执行漏洞由奇安信天工实验室安全研究员发现并提交。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs49NyUHsAHhWFMYoTwtuE29U5plLY9x0JYemm233f3RnY00gZ7iaKFiajUA6QkCIxA5QLL4FP2gSF0rA/640?wx_fmt=png&from=appmsg)

CVE-2024-38044 DHCP 服务器服务远程代码执行漏洞和CVE-2024-38049 Windows 分布式事务处理协调器远程代码执行漏洞由奇安信代码安全实验室安全研究员发现并提交。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs49NyUHsAHhWFMYoTwtuE29UufiagrhnTX4QGicWwpmoC99cqHw8UibjcrzE3Yy699durm5tjFdTdT6tg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs49NyUHsAHhWFMYoTwtuE29UkFxDNdSiadphg0G9vAf4wtUOO2QWMzrfXlqpxZbCCCbAnDK4FpTPVxw/640?wx_fmt=png&from=appmsg)

**鉴于这些漏洞危害较大，建议客户尽快安装更新补丁。**

**>****>****>****>**

**重点关注漏洞详情**

经研判，以下19个漏洞值得关注，漏洞的详细信息如下：

**1、CVE-2024-38112 Windows MSHTML Platform 欺骗漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows MSHTML Platform 欺骗漏洞 | | | | |
| **漏洞类型** | 欺骗 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-38112 |
| **公开状态** | 未公开 | **在野利用** | **已发现** | | |
| **漏洞描述** | 该漏洞允许远程攻击者破坏受影响的系统。该漏洞是由于输入验证不当而存在的。远程攻击者可以进行欺骗攻击并诱骗受害者执行特制文件。**请注意，该漏洞存在在野利用。** | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38112 | | | | | |

**2、CVE-2024-38080 Windows Hyper-V 权限提升漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows Hyper-V 权限提升漏洞 | | | | |
| **漏洞类型** | 权限提升 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-30091 |
| **公开状态** | 未公开 | **在野利用** | **已发现** | | |
| **漏洞描述** | 该漏洞允许本地用户提升系统权限。该漏洞是由于 Windows Hyper-V 组件中的整数溢出而导致的。本地用户可以触发整数溢出并以 SYSTEM 权限执行任意代码。**请注意，该漏洞存在在野利用。** | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38080 | | | | | |

**3、CVE-2024-38060 Windows Imaging Component 远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows Imaging Component 远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-38060 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程攻击者在目标系统上执行任意代码。该漏洞是由于 Windows Imaging 组件中的边界错误而存在的。远程用户可以将特制数据传递给应用程序，触发基于堆的缓冲区溢出并在目标系统上执行任意代码。成功利用此漏洞可能会导致易受攻击的系统完全被攻陷。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38060 | | | | | |

**4、CVE-2024-38023 Microsoft SharePoint Server 远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft SharePoint Server 远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-38023 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程用户在目标系统上执行任意代码。该漏洞是由于在 Microsoft SharePoint Server 中处理序列化数据时输入验证不安全而导致的。远程管理员可以将特制数据传递给应用程序并在目标系统上执行任意代码。成功利用此漏洞可能导致易受攻击的系统完全被攻陷。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38023 | | | | | |

**5、Windows 远程桌面授权服务远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows 远程桌面授权服务远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-38077  CVE-2024-38076 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 这些漏洞允许未经身份验证的远程攻击者在受影响的系统上执行任意代码。这个漏洞是由 Windows 远程桌面授权服务中的基于堆的缓冲区溢出引起的。攻击者可以通过发送特制的请求到受影响的服务来利用此漏洞完全控制系统。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38077  https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38076 | | | | | |

**6、CVE-2024-38074 Windows 远程桌面授权服务远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows 远程桌面授权服务远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 紧急 | **漏洞ID** | CVE-2024-38074 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程攻击者在目标系统上执行任意代码。该漏洞是由于 Windows 远程桌面授权服务中的整数下溢而存在的。远程攻击者可以向受影响的应用程序发送特制的数据包，触发整数下溢并在目标系统上执行任意代码。成功利用此漏洞可能导致易受攻击的系统完全被攻陷。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38074 | | | | | |

**7、CVE-2024-38099 Windows 远程桌面授权服务拒绝服务漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Windows 远程桌面授权服务拒绝服务漏洞 | | | | |
| **漏洞类型** | 拒绝服务 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-38099 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程攻击者绕过身份验证过程。该漏洞是由于 Windows 远程桌面授权服务在处理身份验证请求时出现错误而导致的。远程攻击者可以绕过身份验证过程并执行拒绝服务 (DoS) 攻击。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38099 | | | | | |

**8、CVE-2024-38094 Microsoft SharePoint 远程代码执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft SharePoint 远程代码执行漏洞 | | | | |
| **漏洞类型** | 远程代码执行 | **风险等级** | 重要 | **漏洞ID** | CVE-2024-38094 |
| **公开状态** | 未公开 | **在野利用** | 未发现 | | |
| **漏洞描述** | 该漏洞允许远程用户在目标系统上执行任意代码。该漏洞是由于在 Microsoft SharePoint 中处理序列化数据时输入验证不安全而导致的。远程管理员可以将特制数据传递给应用程序并在目标系统上执行任意代码。成功利用此漏洞可能导致易受攻击的系统完全被攻陷。 | | | | |
| **参考链接** | | | | | |
| https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38094 | | | | | |

**9、CVE-2024-38052 Kernel Stre...