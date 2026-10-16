---
title: Outside the Monitored Perimeter, Inside the Attack Surface
url: https://labs.yarix.com/2026/10/outside-the-monitored-perimeter-inside-the-attack-surface/
source: Over Security
date: 2026-10-15
fetch_date: 2026-10-16T06:37:42.784323
---

# Outside the Monitored Perimeter, Inside the Attack Surface

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Visit Yarix Website](https://www.yarix.com/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Outside the Monitored Perimeter, Inside the Attack Surface

* [Home](https://labs.yarix.com "Go to Home Page")
* Outside the Monitored Perimeter, Inside the Attack Surface

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2026/10/cover1.jpg)

15Oct15/10/2026

## Outside the Monitored Perimeter, Inside the Attack Surface

[Ylabs](https://labs.yarix.com/author/ylabs/)2026-10-15T09:36:30+02:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/)

Reading Time:   14 minutes

*Personal Websites as an Indirect Corporate Exposure*

**Key Takeaways**

* Personal websites can represent an additional point of exposure for high-profile individuals, even when they are not directly connected to the corporate infrastructure.
* In some cases, compromising infrastructure associated with a VIP may allow a threat actor to indirectly target the company by abusing the individual’s trusted identity and resources, without directly interacting with the corporate infrastructure.
* An ad-hoc DNS fuzzing activity identified active personal websites associated with monitored VIPs, including assets that were not part of the monitoring perimeter communicated to the YCTI Team.
* The relevance of these findings does not necessarily come from a single element, but from the correlation of different information and technical exposure around the same identity and, in some cases, the same asset.

# Introduction: One Identity, Many Points of Exposure

Personal websites represent an important window for individuals to promote their business, research, studies, hobbies, and professional profile. For self-employed workers and independent professionals, they are often also a direct channel to reach future clients, partners, and new business opportunities. However, like any other exposed asset, **personal websites are part of the attack surface** and can become an interesting target for malicious actors.

A threat actor interested in targeting a company may also consider **targeting the individuals behind it** rather than directly aiming at the company itself. Executives, board members, founders, public-facing professionals, or other high-profile individuals may represent an alternative point of exposure. Their personal websites may be easier to identify, less monitored, and often receive less security attention than official corporate domains. In this sense, compromising an asset associated with a VIP may also provide a threat actor with **an indirect way to target the organization**, by abusing the individual’s trusted identity and resources without directly targeting the corporate infrastructure itself.

From an attacker perspective, gaining control of a website associated with a known individual means gaining control of a domain that customers, employees, partners, or other users may already associate with a trusted identity. Such access could be used for phishing and social engineering operations, impersonation, malicious redirects, scam content, reputational damage, or fraudulent communications with customers and partners.

For this reason, personal websites linked to high-profile individuals should also be considered when evaluating external exposure, **even when these assets are not formally part of the corporate infrastructure**.

This article focuses on personal websites associated with VIPs monitored by the Yarix Cyber Threat Intelligence Team (YCTI), with the aim of understanding whether some of these assets fall outside the monitoring perimeter normally provided by customers and what risks their exposure could introduce for the individuals and organizations involved.

To do so, the YCTI Team adopted a simple idea, conducting an ad-hoc R&D activity based on DNS fuzzing, using the names of VIPs included in its monitored pool and combining them with a set of common top-level domains (TLDs), with the aim of identifying possible personal websites related to the individuals and not already included in the monitored perimeter communicated by customers.

The objective of the article is not to dive into a mere technical overview of the discovered assets, but to raise awareness around how assets associated with a high-profile individual, even when they are outside the corporate monitoring perimeter, may still provide information or additional points of exposure that could be useful to a threat actor.

**NOTE:** The analysis was conducted through non-intrusive research techniques. No exploitation attempts or invasive activities were performed against the identified websites.

# Business Email Compromise, credential exposure, and personal information

Before diving into the technical aspects of the research, it is useful to provide a brief context on the wider identity-related threat landscape.

The priorities expressed by CEOs in the World Economic Forum Global Cybersecurity Outlook 2026[[1]](#fn1) see **cyber-enabled fraud and phishing as their top concern for 2026**[[2]](#fn2), marking a shift from 2025, when ransomware attacks were occupying the CEOs’ first spot in the ranking[[3]](#fn3). This means that threats related to Business Email Compromise (BECs) such as CEO Fraud and Account Compromise[[4]](#fn4) are becoming increasingly relevant, also supported by the use of AI to create more credible stories and by the fact that these attacks can be tricky and subtle to detect. Threat actors rely on established relationships, processes and requests coming from trusted contacts (such as colleagues, relatives, CEOs or, in this case, a VIP), to make their fraudulent activity more convincing.

The emergence of this trend has been already identified and shown throughout the latest Yarix annual reports. In fact, according to the Yarix 2025 Y-REPORT and 2026 Y-REPORT, **Business Email Compromise remained a significant threat category**, with 38 BEC cases managed in 2024[[5]](#fn5) and 37 cases managed in 2025[[6]](#fn6). A dedicated analysis included in the Yarix 2025 Y-REPORT, covering 27 BEC incidents managed in 2024, also showed that these attacks do not necessarily rely only on simple email spoofing. In the sample analyzed, in approximately 60% of cases, the threat actor was able to bypass multi-factor authentication and maintain persistence inside the compromised account[[7]](#fn7).

The relevance of this threat can also be observed in law enforcement reporting. According to the FBI Internet Crime Complaint Center (IC3) 2025 Annual Report, Business Email Compromise was the second-highest cyber-enabled fraud category by reported losses, generating 24,768 complaints and **more than USD 3 billion in reported losses during 2025**[[8]](#fn8).

A further element is represented by the large amount of compromised credentials circulating in criminal ecosystems. Yarix identified an increase from more than 193 million infostealer-compromised credentials in 2023[[9]](#fn9) to over 920 million in 2024[[10]](#fn10) and **more than 1.2 billion in 2025**[[11]](#fn11). As is known, the role of infostealers does not only stop at credential harvesting, but extends to the collection of browser cookies, session tokens, and other authentication material that may later be used to access accounts and further expand the exposure associated with the same identity.

These figures and cases do not establish a direct relationship between personal websites and BEC incidents, credential theft, or account takeover. However, they provide useful context to understand why **information and exposure...