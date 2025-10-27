---
title: Microsoft Exchange Server多个0Day漏洞安全风险通告第六次更新
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497064&idx=2&sn=a9ce5bbf48d86e3c3ba5ea46d2ccd079&chksm=fe79d1f0c90e58e6f317cbe32759a4a97ed60854ac6746fbb40d4f0f207404a7c88c6c836093&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2022-11-10
fetch_date: 2025-10-03T22:15:39.988031
---

# Microsoft Exchange Server多个0Day漏洞安全风险通告第六次更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icQNBdiacyfljINTcicOd2k1qHw6up502Xo1JylzgfzmHmDfsGtjPBksph3pEaibrbhFpd0BGgaDHnGA/0?wx_fmt=jpeg)

# Microsoft Exchange Server多个0Day漏洞安全风险通告第六次更新

原创

QAX CERT

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

近日，奇安信CERT监测到GTSC SOC 团队发布博客，披露了Microsoft Exchange Server中的两个0Day漏洞，包括：Microsoft Exchange Server权限提升漏洞(CVE-2022-41040)和Microsoft Exchange Server远程代码执行漏洞(CVE-2022-41082)。经过身份验证的远程攻击者可使用相关漏洞利用链在目标系统上执行任意代码。**目前，这两个漏洞已被检测到在野利用。鉴于这些漏洞影响较大，微软官方已发布安全补丁，奇安信CERT强烈建议客户尽快修复漏洞。**

**本次更新内容：**

**监测到微软发布安全补丁，更新处置建议。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Microsoft Exchange Server****权限提升漏洞** | | |
| **公开时间** | 2022-09-30 | **更新时间** | 2022-10-01 |
| **CVE****编号** | CVE-2022-41040 | **其他编号** | QVD-2022-26556 |
| **威胁类型** | 权限提升 | **技术类型** | 服务端请求伪造 |
| **厂商** | Microsoft | **产品** | Exchange Server |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | **已发现** | 未公开 |
| **漏洞描述** | Microsoft Exchange Server 存在权限提升漏洞，经过身份认证的远程攻击者可利用此漏洞绕过相关安全特性，获得在系统上下文中运行 PowerShell 的权限。配合其他漏洞可对目标发起进一步利用，实现任意代码执行。 | | |
| **影响版本** | Microsoft Exchange Server 2016 Cumulative Update 23  Microsoft Exchange Server 2019 Cumulative Update 12  Microsoft Exchange Server 2019 Cumulative Update 11  Microsoft Exchange Server 2016 Cumulative Update 22  Microsoft Exchange Server 2013 Cumulative Update 23 | | |
| **其他受影响组件** | 无 | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Microsoft Exchange Server****远程代码执行漏洞** | | |
| **公开时间** | 2022-09-30 | **更新时间** | 2022-10-01 |
| **CVE****编号** | CVE-2022-41082 | **其他编号** | QVD-2022-26557 |
| **威胁类型** | 代码执行 | **技术类型** | 数据验证不恰当 |
| **厂商** | Microsoft | **产品** | Exchange Server |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | **已发现** | 未公开 |
| **漏洞描述** | Microsoft Exchange Server 存在远程代码执行漏洞，经过身份验证的攻击者可利用此漏洞在目标系统上执行任意代码。 | | |
| **影响版本** | Microsoft Exchange Server 2016 Cumulative Update 23  Microsoft Exchange Server 2019 Cumulative Update 12  Microsoft Exchange Server 2019 Cumulative Update 11  Microsoft Exchange Server 2016 Cumulative Update 22  Microsoft Exchange Server 2013 Cumulative Update 23 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft   Exchange Server权限提升漏洞 | | | |
| **CVE****编号** | CVE-2022-41040 | **其他编号** | | QVD-2022-26556 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 8.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 低 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 未改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 经过身份认证的远程攻击者可利用此漏洞绕过相关安全特性，配合其他漏洞可对目标发起进一步利用，实现任意代码执行。 | | | |
|  |  |  |  |  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft   Exchange Server远程代码执行漏洞 | | | |
| **CVE****编号** | CVE-2022-41082 | **其他编号** | | QVD-2022-26557 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 8.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 低 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 未改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 具有执行PowerShell权限的远程攻击者可利用此漏洞在目标系统上执行任意代码。此漏洞可配合CVE-2022-41040 Microsoft Exchange Server权限提升漏洞使用。 | | | |
|  |  |  |  |  |

处置建议

**微软已于11月发布此漏洞受影响版本的安全补丁，强烈建议受影响的用户尽快安装安全补丁进行防护。建议受影响用户通过以下链接进行手动更新：**

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082

**检测方案：**

**一、使用PowerShell命令**

```
Get-ChildItem -Recurse -Path <Path_IIS_Logs> -Filter "*.log" | Select-String -Pattern 'powershell.*autodiscover\.json.*\@.*200'
```

**二、使用 NCSE0Scanner 检测工具**

GTSC 基于exploit签名开发了扫描 IIS 日志文件的工具，相比 PowerShell，该工具搜索时间更短。以下为工具下载链接：

https://github.com/ncsgroupvn/NCSE0Scanner

**三、使用Microsoft Defender for Endpoint**

用户可启用 Microsoft Defender 防病毒以检测与此次在野利用漏洞相关的 Web Shell 恶意软件。

详情可参考：https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server

**四、入侵指标 (IOC)**

GTSC 安全研究人员还提供了一些可用于识别感染的入侵指标 (IOC)，如下：

**Webshell:**

```
File Name: pxh4HG1v.ashxHash (SHA256): c838e77afe750d713e67ffeb4ec1b82ee9066cbe21f11181fd34429f70831ec1Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\pxh4HG1v.ashxFile Name: RedirSuiteServiceProxy.aspxHash (SHA256): 65a002fe655dc1751add167cf00adf284c080ab2e97cd386881518d3a31d27f5Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\RedirSuiteServiceProxy.aspxFile Name: RedirSuiteServiceProxy.aspxHash (SHA256): b5038f1912e7253c7747d2f0fa5310ee8319288f818392298fd92009926268ca

Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\RedirSuiteServiceProxy.aspxFile Name: Xml.ashxHash (SHA256): c838e77afe750d713e67ffeb4ec1b82ee9066cbe21f11181fd34429f70831ec1Path: Xml.ashxFilename: errorEE.aspxSHA256: be07bd9310d7a487ca2f49bcdaafb9513c0c8f99921fdf79a05eaba25b52d257Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\errorEE.aspx
```

**DLL:**

```
File name: Dll.dllSHA256:074eb0e75bb2d8f59f1fd571a8c5b76f9c899834893da6f7591b68531f2b5d8245c8233236a69a081ee390d4faa253177180b2bd45d8ed08369e07429ffbe0a99ceca98c2b24ee30d64184d9d2470f6f2509ed914dafb87604123057a14c57c029b75f0db3006440651c6342dc3c0672210cfb339141c75e12f6c84d990931c3c8c907a67955bcdf07dd11d35f2a23498fb5ffe5c6b5d7f36870cf07da47bff2File name: 180000000.dll (Dump từ tiến trình Svchost.exe)SHA256: 76a2f2644cb372f540e179ca2baa110b71de3370bb560aca65dcddbd7da3701e
```

**IP:**

```
125[.]212[.]220[.]485[.]180[.]61[.]1747[.]242[.]39[.]9261[.]244[.]94[.]8586[.]48[.]6[.]6986[.]48[.]12[.]6494[.]140[.]8[.]4894[.]140[.]8[.]113103[.]9[.]76[.]208103[.]9[.]76[.]211104[.]244[.]79[.]6112[.]118[.]48[.]186122[.]155[.]174[.]188125[.]212[.]241[.]134185[.]220[.]101[.]182194[.]150[.]167[.]88212[.]119[.]34[.]11
```

**URL:**

```
hxxp://206[.]188[.]196[.]77:8080/themes.aspx
```

**C2:**

```
137[.]184[.]67[.]33
```

更多细节可参考：https://gteltsc.vn/blog/warning-new-attack-campaign-utilized-a-new-0day-rce-vulnerability-on-microsoft-exchange-server-12715.html。

**缓解方案：**

**一、 在 IIS 服务器中添加新的 URL 重写规则**

**1）启用Exchange 紧急缓解服务 (EEMS)**

对于启用了 Exchange 紧急缓解服务 (EEMS) 的客户，Microsoft 发布了适用于 Exchange Server 2016 和 Exchange Server 2019 的 URL 重写缓解措施。该服务会自动启用缓解措施并更新URL重写规则。有关Exchange 紧急缓解服务详情可参考：

https://techcommunity.microsoft.com/t5/exchange-team-blog/new-security-feature-in-september-2021-cumulative-update-for/ba-p/2783155

**2）使用EOMTv2工具**

Microsoft 为 URL 重写缓解步骤创建了脚本工具 EOMTv2，如果没有安装 IIS URL 重写模块，脚本会自动下载并安装该模块。

工具链接：https://aka.ms/EOMTv2

1．使用方法：.\EOMTv2.ps1

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icQNBdiacyfljINTcicOd2k1qyMWibE2rv3yF1fiaGBy0uLoJhvLS28lficm5x3vMUZQPL4PicdJ40ChbKw/640?wx_fmt=png)

2. 回滚 EOMTv2 缓解措施：.\EOMTv2.ps1 -Rollbackmitigation

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icQNBdiacyfljINTcicOd2k1qb2c2mKSCa5M89LHwtT1uv6Wh7Ir91iajd0feMpaoiaL1cQ2hRGibP0cDA/640?wx_fmt=png)

**3）手动配置**

1. 打开 IIS 管理器

2. 选择Default Web Site（默认网站）

3. 在功能视图中选择 URL 重写

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icQNBdiacyfljINTcicOd2k1qTT7QVvghs7FZLQp9rVU8bBkZgpD69WnvHAYwcxLaicngyCKAEgbhTdA/640?wx_fmt=png)

4. 在右侧的操作窗格中，单击添加规则，或右键选择添加规则

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icQNBdiacyfljINTcicOd2k1qLY93...