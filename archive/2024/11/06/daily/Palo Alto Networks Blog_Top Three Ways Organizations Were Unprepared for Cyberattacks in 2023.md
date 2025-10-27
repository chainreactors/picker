---
title: Top Three Ways Organizations Were Unprepared for Cyberattacks in 2023
url: https://www.paloaltonetworks.com/blog/2024/11/top-three-ways-organizations-were-unprepared-for-cyberattacks-in-2023/
source: Palo Alto Networks Blog
date: 2024-11-06
fetch_date: 2025-10-06T19:21:45.596587
---

# Top Three Ways Organizations Were Unprepared for Cyberattacks in 2023

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Cybersecurity](https://www.paloaltonetworks.com/blog/category/cybersecurity-2/)
* Top Three Ways Organizati...

# Top Three Ways Organizations Were Unprepared for Cyberattacks in 2023

Link copied

By [Michael J Graven](/blog/author/michael-j-graven/ "Posts by Michael J Graven")

Nov 05, 2024

8 minutes

[Cybersecurity](/blog/category/cybersecurity-2/)

[Products and Services](/blog/category/products-and-services/)

[Reports](/blog/category/reports/)

[Threat Prevention](/blog/category/threat-prevention-2/)

[Threat Research](/blog/category/threat-research/)

[Unit 42](/blog/category/unit42/)

[2024 incident response report](/blog/tag/2024-incident-response-report/)

[incident response report](/blog/tag/incident-response-report/)

# Back to Basics

With attackers moving at greater speed and scale than ever before, the fundamentals of cybersecurity have become even more important. Unit 42 has gathered data from hundreds of incidents across the globe to identify the soft spots in security postures that made cyberattacks in 2023 more risky and painful than they needed to be.

Effective patch and vulnerability management, complete visibility and comprehensive identity management practices often feel out of reach. Our 2024 Incident Response report reveals the need for defenders to prioritize these security fundamentals more than ever.

## Ineffective Patch and Vulnerability Management

Software and API vulnerabilities are a prime target for bad actors. According to the Unit 42 [Incident Response Report](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report), 38% of breaches exploited these flaws last year, dethroning phishing and social engineering as the top attack vector for the previous two years.

Vulnerabilities in software, like the MOVEit file sharing service, allowed attackers to mount large-scale intrusion campaigns. We found that over 85% of organizations had Remote Desktop Protocol internet-accessible for at least 25% of a month, significantly increasing the risk of a ransomware attack.

Organizations must get their arms around their internet-facing attack surface, which is more easily said than done.

* Zero-day vulnerabilities kick off a race between the threat actors and the defenders (including developers, vendors and customers) to exploit or remediate the impacted systems. Unfortunately, attackers have speed on their side. Defenders must wait for developers to release a patch, then test that patch before applying it to live systems, making sure the patch won’t break anything mission-critical.
* Vulnerabilities are discovered at a far greater rate than even the most efficient team’s ability to patch them. [According to NIST](https://nvd.nist.gov/vuln/search/statistics?form_type=Basic&results_type=statistics&search_type=all&isCpeNameSearch=false), over 28,000 vulnerabilities were reported in 2023. When a major vulnerability is announced, attackers can scan the entire internet for exposed instances and exploit them [within hours](https://www.paloaltonetworks.ca/resources/research/2023-unit-42-attack-surface-threat-report). Meanwhile, it takes enterprises [an average of three weeks](https://www.paloaltonetworks.com/cortex/cortex-xpanse) to fix them.
* [Patches aren’t the only vulnerabilities](https://www.paloaltonetworks.com/cyberpedia/vulnerability-management) affording attackers an entry point. Insecure configurations in cloud services, infrastructure and other resources can provide a foothold. They can’t be patched in the conventional sense, and they deserve equal priority.

While vulnerabilities themselves are inevitable, your organization’s response is not. Establishing a system for vulnerability awareness and remediation is critical for good security hygiene. This system starts with a complete and maintained inventory of assets, coupled with ongoing monitoring of CVE databases.

However, discovering all the vulnerabilities in your purview isn’t enough. Teams need processes and tools that allow them to score and prioritize the vulnerabilities that present the most risk. Other controls that hinder attackers, like segmenting systems and subnets, can make some vulnerabilities less critical by imposing speed bumps and dead ends on attackers’ progress.

## Gaps in Monitoring and Coverage

Organizations with partial or incomplete deployment of security controls allowed attackers to operate from parts of the network that weren’t defended. Imagine a fortified castle with shadowy corners that are never patrolled; that’s the risk of partial security control deployment.

The modern IT landscape is only growing in complexity. Organizations juggle a mix of on-premises infrastructure, cloud deployments, hybrid environments and even multicloud architectures. This diversity makes consistent eXtended detection and response (XDR) deployment across all endpoints a challenge. This challenge is compounded by the sheer variety of devices (desktops, laptops, mobile devices and even IoT products) connecting to the network.

This complexity is further amplified in bring-your-own-device (BYOD) situations, where endpoints regularly move inside and outside the corporate network. Additionally, integrating XDR tools with existing security infrastructure (i.e., firewalls, security information and event management (SIEM) systems, and other endpoint solutions) can be difficult, creating gaps in overall coverage. Achieving full coverage often requires a complex tool stack, leading to increased costs, redundancy and a greater maintenance burden.

Fortunately, organizations can consolidate tools into unified security platforms, like [extended security intelligence and automation management (XSIAM) solutions](https://www.paloaltonetworks.com/cortex/cortex-xsiam). These platforms offer a centralized view of security events across the entire network, simplifying management and reducing tool sprawl.

Leveraging strong relationships with those who can help you defend is vital to success. These partners can identify potential uncertainties through tailor-made strategies and services, like vulnerability scanning, to ensure comprehensive security coverage across the entire IT environment. By adopting these strategies, organizations can move from a partially secured castle to a fully fortified stronghold.

## Overprivileged Identity and Access Management

Credential theft is still rising, accounting for 20% of attacks last year, which is up 4% from 2021 and 13% from 2022. With privileged credentials in hand, attackers can penetrate systems, move laterally and escalate privileges to reach more sensitive assets.

Identity is a fundamental of strong security — knowing who’s doing what, and whether they should be doing it.

Fortifying defenses against credential-based attacks goes beyond implementing multifactor authentication (MFA) and other table-stakes controls. Teams must cultivate the ability to stitch together data points from disparate sources, painting a bigger picture of behavior that may indicate an attack pattern. As it stands, security teams universally struggle with the sheer volume of data generated by their tools, and they cannot analyze audit logs and maintain correlation rules.

Though forensics following a breach may suggest these patterns are obvious, that’s simply not the case.

A tension between security and productivity prevents security teams from effectively leveraging this data. Personnel are commonly granted excessive privileges for the sake of convenience and productivity. However, they don’t always have a deeper security training to safeguard these privileges, which can create low-hanging fruit for attackers.

To effectively combat these challenges, organizations can deploy a streamlined detection strategy focused on identifying unusual activity within their systems:

* **Unusual Tool Usage:** Monitor the ...