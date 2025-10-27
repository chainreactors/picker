---
title: Microsoft Teams used in phishing campaign to bypass multi-factor authentication
url: https://buaq.net/go-173731.html
source: unSafe.sh - 不安全
date: 2023-08-05
fetch_date: 2025-10-04T12:00:11.867784
---

# Microsoft Teams used in phishing campaign to bypass multi-factor authentication

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/54eb79df1f5047cde90cff1202cff75d.jpg)

Microsoft Teams used in phishing campaign to bypass multi-factor authentication

Attackers believed to have ties to Russia's Foreign Intelligence Servic
*2023-8-4 21:45:0
Author: [www.malwarebytes.com(查看原文)](/jump-173731.htm)
阅读量:23
收藏*

---

Attackers believed to have ties to Russia's Foreign Intelligence Service (SVR) are using Microsoft Teams chats as credential theft phishing lures. Microsoft Threat Intelligence has [posted details about the perceived attacks](https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/) targeted at fewer than 40 unique global organizations. The targeted organizations are mostly found among government, non-government organizations (NGOs), IT services, technology, discrete manufacturing, and media sectors.

According to Microsoft the attackers are part of the same group that was behind the attacks against [SolarWinds](https://www.malwarebytes.com/blog/threat-analysis/2020/12/advanced-cyber-attack-hits-private-and-public-sector-via-supply-chain-software-update/), the [Sunburst](https://www.malwarebytes.com/blog/detections/backdoor-sunburst/)[backdoor](https://www.malwarebytes.com/blog/detections/backdoor-sunburst/), TEARDROP malware, GoldMax malware, and other [related components](https://www.malwarebytes.com/blog/malwarebytes-news/2021/01/malwarebytes-targeted-by-nation-state-actor-implicated-in-solarwinds-breach-evidence-suggests-abuse-of-privileged-access-to-microsoft-office-365-and-azure-environments/). Malwarebytes tracks that group as [APT29/Cozy Bear](https://www.malwarebytes.com/blog/business/2023/05/apt-attacks-exploring-advanced-persistent-threats-and-their-evasive-techniques). A group well-known for finding and deploying novel tactics, techniques, and procedures (TTPs).

In the phishing attacks the group leverages previously compromised Microsoft 365 instances, mostly owned by small businesses, to create new domains that look like technical support accounts. From these instances the group reaches out through Teams messages and persuades targets to approve multi-factor authentication (MFA) prompts initiated by the attacker.

The compromised instances are renamed and used to set up a new onmicrosoft.com subdomain. Onmicrosoft.com domains are legitimate Microsoft domains which are automatically used by Microsoft 365 for fallback purposes in case a custom domain is not created.

The attackers often use security terms or product-specific names in these subdomain names to give credibility to the technical support themed messages which are sent out as a lure.

![example of a compromised omicrosoft account initiating a chat](https://www.malwarebytes.com/blog/news/2023/08/easset_upload_file10639_275819_e.png)

The objective is to target users with passwordless authentication configured on their account, or accounts for which they have obtained credentials previously. In both cases they require the user to enter a code that is displayed during the authentication flow into the prompt on the Microsoft Authenticator app on their mobile device.

Once the target has done this, the attacker can use the gained access to further compromise the account. Typically, this involves information theft from the now compromised Microsoft 365 tenant. In some cases, the actor attempts to add a device to the organization as a managed device via Microsoft Entra ID (formerly Azure Active Directory), likely an attempt to circumvent conditional access policies configured to restrict access to specific resources to managed devices only.

Microsoft says it has successfully blocked the Russian threat group from utilizing the compromised instances in other attacks and is now actively working to address and limit the impact of the campaign.

## How to avoid tech support scammers

In the blog Microsoft provides a very important ground rule to remember: Authentication requests not initiated by the user should be treated as malicious.

As a security provider with a good reputation, we do get a lot of impersonators. Maybe we should be flattered, but frankly we are annoyed. So here are a few tell-tale signs that you are dealing with an impersonator:

* The company gives you any name at all other than Malwarebytes. Malwarebytes does not outsource support. We have our own [Support team](https://support.malwarebytes.com/hc/en-us). There are no third parties “authorized” to provide support. Nobody is “licensed” to use our name, logo, or any other intellectual property.
* The company can’t or won't take your credit card the first time you ask. Reputable organizations don’t do this. Period. Malwarebytes has a credit card processor that takes payments for all transactions. Credit card processors do things like vet clients for risk, fraud, and abuse. So any company having trouble doing business with one, probably fits into one of those three categories. Credit cards also have reasonably robust consumer fraud protection, so if you’re being steered away from using one, that is also a red flag that the company is about to do something they probably shouldn’t.
* The company makes outbound support calls. Malwarebytes, and Microsoft, do not do this. Tech support companies that make outbound unsolicited calls tend to do so because they bought your personal information from a data broker who classified you as a vulnerable target. How would they know you have a problem with your computer? How would they even know you own a computer? Generally speaking, if someone calls you out of the blue claiming your computer has a problem, hang up.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/08/microsoft-teams-used-in-phishing-campaign-to-bypass-multi-factor-authentication
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)