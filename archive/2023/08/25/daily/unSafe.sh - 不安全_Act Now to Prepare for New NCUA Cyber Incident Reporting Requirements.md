---
title: Act Now to Prepare for New NCUA Cyber Incident Reporting Requirements
url: https://buaq.net/go-175314.html
source: unSafe.sh - 不安全
date: 2023-08-25
fetch_date: 2025-10-04T11:59:28.434488
---

# Act Now to Prepare for New NCUA Cyber Incident Reporting Requirements

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

![]()

Act Now to Prepare for New NCUA Cyber Incident Reporting Requirements

We recently discussed the new SEC rule requiring all registered companies to report material
*2023-8-24 22:55:18
Author: [lab.wallarm.com(查看原文)](/jump-175314.htm)
阅读量:21
收藏*

---

We recently [discussed the new SEC rule](https://lab.wallarm.com/impact-of-the-new-sec-cyber-incident-reporting-rules-on-the-c-suite-and-beyond/) requiring all registered companies to report material cyber incidents within four (4) days.

Now the [**National Credit Union Administration**](https://ncua.gov/) (NCUA)[1](#b1414acb-d39c-41ce-90d7-989edddf9913) has updated their Cyber Incident Notification Rule, requiring all federally insured Credit Unions to notify the NCUA of any cyber incident **no more than 72 hours after detection**.[2](#f7906cfe-b48a-4244-be9f-9623124045f8)

In this post, we’ll provide a quick summary of the new requirements and how it impacts not only US Credit Unions, but also third parties supporting the move towards open banking.

## **Who Is Impacted?**

There are over 4,700 federally insured Credit Unions in the US, with almost 137 million members (over 40% of the entire US population) and over $2.2 trillion in total assets.

Also impacted are third-party service providers which handle sensitive data or business operations for these Credit Unions. There is a specific carve out for contracted pentesting.

## **What’s a Cyber Incident?**

The new rule is focused on actual or “imminent” harm to the confidentiality, integrity or availability (aka [the CIA triad](https://www.csoonline.com/article/568917/the-cia-triad-definition-components-and-examples.html)) of Credit Union information or information systems.

> The Cyber Incident Notification Requirements rule defines a cyber incident as an occurrence that actually or imminently jeopardizes, without lawful authority, the integrity, confidentiality, or availability of information on an information system or actually or imminently jeopardizes, without lawful authority, an information system.
>
> NCUA Letter regarding [Cyber Incident Notification Requirements](https://ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/cyber-incident-notification-requirements)

The rule defines reportable cyber incidents are any one or more of the following outcomes:

1. *“A substantial loss of confidentiality, integrity, or availability of a network or member information system that results from the unauthorized access to or exposure of sensitive data, disrupts vital member services, or has a serious impact on the safety and resiliency of operational systems and processes.”*
2. “*A disruption of business operations, vital member services, or a member information system resulting from a cyberattack or exploitation of vulnerabilities.”*
3. *“A disruption of business operations or unauthorized access to sensitive data facilitated through, or caused by, a compromise of a credit union service organization, cloud service provider, or other third-party data hosting provider or by a supply chain compromise.”*

## **When Does This Take Effect?**

The new NCUA Cyber Incident Notification requirements come into effect **beginning on September 1, 2023**.

## **How Are APIs Involved?**

In a couple of ways.

First, it’s no secret that attacks against APIs are not only increasing but getting increasingly more sophisticated. We see it in our sensor data – in fact, in our [Q2-2023 API ThreatStatsTM report](https://lab.wallarm.com/api-exploits-are-everywhere-from-nvidia-to-reddit-and-more/) we saw 32.1M unique API attacks (40% of all attacks) against our customer base worldwide, including an astonishing 514% YoY increase in API attacks against US-based customers.

And this is borne out by the continuing attacks by the Cl0p ransomware group which exploit [several API vulnerabilities in MOVEit](https://lab.wallarm.com/the-moveit-ransomware-attacks-now-impacting-government-agencies-and-large-organizations/), a Managed File Transfer (MFT) solution used by many organizations. It was recently reported that [15 banks and credit unions have confirmed MOVEit-related data breaches](https://www.americanbanker.com/creditunions/news/15-banks-credit-unions-confirm-moveit-data-breaches), including at least one case which arose because of a third party.

Second, the Open Banking movement, which is heavily dependent on information and data sharing via APIs, is accelerating worldwide and in the US. In fact, the Consumer Financial Protection Bureau (CFPB) [recently announced](https://www.consumerfinance.gov/about-us/blog/laying-the-foundation-for-open-banking-in-the-united-states/) that new rules will be proposed later this year with the expectation they will be finalized in 2024. This will only further the impact of the new NCUA reporting requirements.

## **Any Implementation Guidance?**

The NCUA has provided some guidance to Credit Unions when implementing this rule, including:

* **Update Response Plan**, to provide clear guidelines on what constitutes reportable incidents and associated escalation & reporting procedures.
* **Review Contracts**, to confirm critical service providers are required to provide timely incident notification.
* **Train Employees**, to ensure they understand the importance of reporting cyber incidents and are properly supported to avoid the consequences of noncompliance.
* **Monitor and Review**, to validate the reporting process is effective; they also recommend periodic tests and exercises to evaluate its effectiveness.
* **Document All Incidents**, without regard to reportability, to serve as an audit trail to support reporting decisions and as a resource for future incident response.

Of course, if you find you need real-time integrated web app and API protection to extend security across your entire portfolio, we invite you to [schedule a call](https://www.wallarm.com/request-demo) with one of our security experts to learn how Wallarm can help you.

## **NCUA Resources**

* Letter to Credit Unions: [**Cyber Incident Notification Requirements**](https://ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/cyber-incident-notification-requirements) (23-CU-07 / August 2023)
* Quick Reference Guide: [**Cyber Incident Reporting**](https://ncua.gov/files/letters-credit-unions/cyber-incident-reporting-quick-reference-guide.pdf) (updated July 2023)
* [**Cybersecurity Resources**](https://ncua.gov/regulation-supervision/regulatory-compliance-resources/cybersecurity-resources), including assessment programs & tools, regulations & guidance, and more

---

文章来源: https://lab.wallarm.com/act-now-to-prepare-for-new-ncua-cyber-incident-reporting-requirements/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)