---
title: ITDR For the Win | Moving Beyond IAM and PAM to Protect Digital Identities
url: https://buaq.net/go-149211.html
source: unSafe.sh - 不安全
date: 2023-02-14
fetch_date: 2025-10-04T06:29:21.701363
---

# ITDR For the Win | Moving Beyond IAM and PAM to Protect Digital Identities

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

![](https://8aqnet.cdn.bcebos.com/7399f0128a395c804f73b2f79cfc441d.jpg)

ITDR For the Win | Moving Beyond IAM and PAM to Protect Digital Identities

In today’s modern work landscape, digital identities have become a record of trust, access, and rel
*2023-2-13 21:38:32
Author: [www.sentinelone.com(查看原文)](/jump-149211.htm)
阅读量:24
收藏*

---

In today’s modern work landscape, digital identities have become a record of trust, access, and relationship management for businesses. Regardless of their size and industry, organizations rely on digital identities to operate.

With a massive growth in the number of digital identities though, opportunistic threat actors have latched on to this expanding surface as a means for attack. Identity-based cyberattacks have accelerated and conventional identity management tools such as Identity Access Management (IAM), Privileged Access Management (PAM), and Identity Governance and Administration (IGA) are no longer enough on their own to shield organizations from advancing cyber threats on both digital and machine identities.

Identity protection and management has increasingly become a topic of focus for many security leaders who now look towards a combination of identity threat detection and response (ITDR) strategies to reduce risk and protect the enterprise. In this post, we explore how ITDR can help protect against threat actors’ growing interest in attacking identity and set up organizations for long-term success.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/ITDR-For-the-Win-Moving-Beyond-IAM-and-PAM-to-Protect-Digital-Identities-2.jpg)

## What Does the Threat Landscape Look Like for Identity?

Data leaks, [phishing](https://www.sentinelone.com/blog/phishing-revealing-vulnerable-targets/) and social engineering campaigns, [supply chain](https://www.sentinelone.com/blog/defending-the-enterprise-against-digital-supply-chain-risk-in-2022/), and [golden ticket](https://www.sentinelone.com/blog/how-kerberos-golden-ticket-attacks-are-signaling-a-greater-need-for-identity-based-security/) attacks have all made global headlines over the past [few years](https://www.sentinelone.com/blog/endpoint-identity-and-cloud-top-cyber-attacks-of-2022-so-far/) with, seemingly, no end in sight. Threat actors are after sensitive data and the volume of attacks on identity has grown significantly.

At the start of last year, for example, attackers impersonated the U.S. Department of Labor in a phishing campaign aimed at stealing Office 365 credentials. [The emails](https://www.oig.dol.gov/public/Fraud_Alert_Graphic_UI_Phishing.pdf) asked recipients to submit bids and utilized an entire network of phishing sites to target unsuspecting users. This particular attack showed a high level of sophistication in the convincing setup of spoofed pages and the well-crafted, typo-free content found within the emails.

![Fraud alert](https://www.sentinelone.com/wp-content/uploads/2023/02/Screenshot-2023-02-13-at-10.13.26-AM.jpg)

Fraud Alert from the Office of Inspector General at the U.S. Department of Labor ([Source](https://www.oig.dol.gov/public/Fraud_Alert_Graphic_UI_Phishing.pdf)).

Later in 2022, authentication services provider [Okta](https://www.okta.com/blog/2022/03/updated-okta-statement-on-lapsus/) suffered a supply chain attack when a laptop belonging to a subprocessor support engineer was compromised. During the 5-day period of unauthorized access, the threat actors were able to access Okta’s customer support panel and internal Slack server. The compromised account held ‘super admin’ access capable of initiating password resets of Okta’s end customers.

Rounding up the tail end of 2022, multinational fintech company PayPal [notified](https://www.documentcloud.org/documents/23578067-paypal-notice?responsive=1&title=1) thousands of its users after their accounts and personal data were accessed by way of a [credential stuffing attack](https://www.sentinelone.com/blog/detecting-brute-force-password-attacks/). In this type of attack, threat actors rely on bots to pair massive lists of known usernames and passwords together to then ‘stuff’ into login portals. The breach impacted nearly 35,000 account holders with threat actors having accessed their full names, birthdays, mailing addresses, social security numbers, and tax identification numbers.

Identity-based attacks accounted for much of the reported security incidents from 2022. Attackers continue to exploit this attack surface, posing a direct risk to enterprises as they meet a surge in digital identities and remote workers.

## Accelerated Attention on the Identity Attack Surface

The [2022 Trends in Security Digital Identities](https://assets.beyondtrust.com/assets/documents/2022-Trends-in-Securing-Digital-Identities.pdf) report from the Identity Defined Security Alliance (IDSA) noted the following key findings:

* 84% of respondents experienced an identity-related breach in the past year
* 96% reported that said breaches could have been minimized or even prevented by identity-focused solutions
* 78% reported direct business impacts such as reputational damage and the cost of recovery post-breach

The causes for this accelerated attention on identity can be attributed to two main factors.

First, the rising use of third-party technology and services, internet of things (IoT) connections, and cloud-based apps have all increased the number of digital identities – both human and machine. Each identity is another possible attack vector, and with so many in existence, more than a few are bound to be less protected or monitored as they should. Such low hanging fruit is a tantalizing ‘in’ for threat actors.

Second, securing new working spaces has become increasingly complex. The perimeters of work have extended far beyond physical offices or small numbers of off-site workers. Accelerated by a global [pandemic](https://www.sentinelone.com/blog/5-cyber-security-challenges-facing-cisos-in-the-age-of-covid-19/), [work-from-home](https://www.sentinelone.com/blog/covid-19-outbreak-employees-working-from-home-its-time-to-prepare/) policies have settled into many organization’s very infrastructure. These allowances have also allowed vendors, partners, contractors, and third-party service providers to all remotely access network resources as needed.

## Understanding the Growing Digital Identity Crisis

Digital identities for both humans and machines are an integral part of how we operate on a day-to-day basis. Vulnerable to attackers, what’s emerged is a high-stakes digital identity crisis that affects everyone. Top challenges businesses face in securing digital identities include:

* A lack of investment for identity management systems – Cloud-based identity architectures are enjoying a boom in adoption, but many small to medium-sized businesses still show resistance to migrating due to budgetary constraints, concerns about onboarding delays, lack of change management processes, and more.
* Fractured ownership for identity in many organizations – Identity management and security is often a responsibility divided amongst the executive leadership and multiple teams like IT, human resources, or sales, for example.
* Fluctuating data privacy regulations and controls – Digital identity management is made complex by the moving goal posts issued by regulatory bodies. Inevitably, identity and data privacy overlap, so organizational leaders must ensure that the data surrounding digital identities comply with mandates such as the European Union’s [GDPR](https://gdpr-info.eu/), the [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privac...