---
title: The Top 5 Largest Scale Intrusions in 2023
url: https://www.paloaltonetworks.com/blog/2024/10/top-5-largest-scale-intrusions-in-2023/
source: Palo Alto Networks Blog
date: 2024-10-03
fetch_date: 2025-10-06T18:57:01.882479
---

# The Top 5 Largest Scale Intrusions in 2023

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Points of View](https://www.paloaltonetworks.com/blog/category/points-of-view/)
* The Top 5 Largest Scale I...

# The Top 5 Largest Scale Intrusions in 2023

Link copied

By [Michael J Graven](/blog/author/michael-j-graven/ "Posts by Michael J Graven")

Oct 02, 2024

9 minutes

[Points of View](/blog/category/points-of-view/)

[Predictions](/blog/category/predictions/)

[Unit 42](/blog/category/unit42/)

[incident response report](/blog/tag/incident-response-report/)

[Unit 42 Incident Response](/blog/tag/unit-42-incident-response/)

# What Powered Them?

Large-scale cyber intrusions increased during 2023, exploiting vulnerabilities in web applications and internet-facing software. Attackers favored this attack vector even more than phishing and other social engineering tactics. But why?

Attackers are using new technologies and tactics that take advantage of shortcomings in patch and vulnerability management processes. These tools allow them to find, initiate and execute intrusions at greater speed.

The Unit 42 Incident Response Report analyzed thousands of incidents to learn what tools and vulnerabilities attackers are focusing on. Read on to unpack the concerning trends of large-scale intrusions and empower your organization to fight back.

## Notable Intrusion Campaigns

#### MOVEit: CVE-2023-34362

In one of the most infamous attacks of 2023, a [critical zero-day vulnerability](https://unit42.paloaltonetworks.com/threat-brief-moveit-cve-2023-34362/) (CVE-2023-34362) was found in a widely used file transfer service for secure data exchange. This system is popular across highly regulated industries and government agencies, such as critical infrastructure providers, healthcare institutions and even government bodies. The impact was far-reaching, affecting over 2,600 organizations, and spread even to organizations whose *vendors* used the file transfer service.

A large number of systems containing this vulnerability were exposed to the internet. Researchers identified more than 3,000 before the vulnerability was disclosed and patched. The vulnerability was rated a critical [9.8 out of 10](https://nvd.nist.gov/vuln/detail/CVE-2023-34362) on the Common Vulnerability Scoring System (CVSS) because it was easy to exploit and the data involved was often sensitive. [Analysts attributed this attack](https://unit42.paloaltonetworks.com/threat-brief-moveit-cve-2023-34362/) to the CL0P ransom group, which indicates these file sharing services are targets for large cybergangs.

But, file services aren’t the only ones affected by software vulnerabilities.

#### Citrix Bleed: CVE-2023-4966

Another major attack vector in 2023 exploited a critical vulnerability in widely deployed remote access and virtual desktop appliances. This flaw allowed attackers, such as the ransomware group [LockBit](https://www.helpnetsecurity.com/2023/11/22/lockbit-citrix-bleed/), to gain a foothold from which they could execute malicious tactics.

Our Incident Response (IR) and Managed Threat Hunting (MTH) teams [observed ransomware groups exploiting Citrix Bleed](https://unit42.paloaltonetworks.com/threat-brief-cve-2023-4966-netscaler-citrix-bleed/). The MTH team has also observed remote executions from Netscaler gateways in association with the exploitation of this vulnerability.

Using this vulnerability, attackers bypassed security controls to hijack legitimate user sessions, gain unauthorized access to systems and steal credentials and other sensitive information. And with the widespread use of the remote access system across various industries (aerospace, banking, shipping logistics, etc.), the potential victim pool is vast.

Even with patches available from the manufacturer, this remote access tool is so widely used that many organizations are *still* suffering the results of the vulnerability.

#### SugarCRM: CVE-2023-22952

A third [zero-day vulnerability](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/) exploited in 2023 was exposed in a popular customer relationship management (CRM) system. This vulnerability allowed attackers to bypass authentication altogether and execute malicious code directly on vulnerable servers. Not only that, the exploited code itself was publicly posted online, complete with instructions for finding similar vulnerable servers.

The potential impact of an exploited CRM isn’t limited to the servers. CRM systems often house sensitive data, such as customer information, financial records and internal communications. In the wrong hands, it’s easy to see how attackers could use this data for extortion attempts, sell on the dark web, or simply use it to damage an organization’s reputation.

Palo Alto’s investigations into this exploit reveal a troubling trend. In many cases, attackers used the initial breach to gain access to cloud service accounts with far-reaching permissions. This demonstrates how one weak link in the security chain puts the entire environment at risk, leaving it open to cascading attacks.

#### Apache Log4j: CVE-2021-44228

One of the most [widespread vulnerabilities](/resources/webcasts/understanding-log4j-vulnerability) in recent years was discovered in the Apache Log4j logging library, a common logging framework developed by a well-known open-source organization. This library plays a vital role over a wide range of industries. It records important information, like error messages and user actions, within various software programs and creates an audit trail of the program’s activity.

A critical vulnerability, first discovered in 2021, gave attackers a way to leverage this library for their gain by essentially granting attackers complete control of any system running an unpatched version of the logging library. Hackers need only inject malicious code into seemingly harmless places, like chat boxes and login forms to gain access using this vulnerability, with no special permissions or authentication required.

Logging libraries often interact with various services within a system, making it easy to distribute malware rapidly and potentially compromise entire networks in a short time frame.

So why is a 2021 vulnerability on the 2023 top-five list? Because the library was embedded in so much software, the number of affected systems is so large that the [U.S. Department of Homeland Security](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf) estimates it will take at least a decade to find and fix every vulnerable instance.

#### Oracle WebLogic: CVE-2020-14882

A Java-based enterprise application, used by more than 7,000 organizations globally, suffered similar attack campaigns in 2023. This time, the platform vulnerability resided in the administrative console – a fast track to significant impact, with the flaw allowing remote attackers access to the inner workings of the platform itself.

Due to the high level of privilege, attackers could seize complete control of applications running on the platform with ease. With one click, a hacker could gain unrestricted access to financial data, customer records and internal systems. This presented a scenario ripe for disruptions, data breaches and financial losses.

The situation was complicated because there were multiple vulnerable versions of the platform and the sheer number of deployments around the globe was daunting. While the company released patches as early as October 2020, the platform’s widespread adoption meant many organizations were still working with unpatched systems by 2023. Moreover, the vulnerability was relatively [easy to exploit](https://unit42.paloaltonetworks.com/network-attack-trends-internet-threats/), requiring minimal technical expertise on the part of the attacker.

## How Did This Happen?

Widespread impact is the goal of these exploitations. Attackers are looking for th...