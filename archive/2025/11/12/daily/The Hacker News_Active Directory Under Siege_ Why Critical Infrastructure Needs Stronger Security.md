---
title: Active Directory Under Siege: Why Critical Infrastructure Needs Stronger Security
url: https://thehackernews.com/2025/11/active-directory-under-siege-why.html
source: The Hacker News
date: 2025-11-12
fetch_date: 2025-11-13T03:16:06.277198
---

# Active Directory Under Siege: Why Critical Infrastructure Needs Stronger Security

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Active Directory Under Siege: Why Critical Infrastructure Needs Stronger Security](https://thehackernews.com/2025/11/active-directory-under-siege-why.html)

**Nov 12, 2025**The Hacker NewsPassword Security / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzohgVmJwL0IMF6xUDk-7UKhnswaBtnht8YAdjmMgnPeft_d_PwFL5ZFvm9zfO_pKg-RkmHgwEM9Uyj6lr5GnUB_Y4IM2oDsroi0pC1yYS6-zdbpiGX-gIlpFQwmBgy-4TcXvQ3NtTXheeqFVh6DL9RUjug2QhaFGFZJOtiJdPOkC1jkZWBuJIJsIHwS0/s790-rw-e365/MAIN.jpg)

Active Directory remains the authentication backbone for [over 90%](https://cybersecuritynews.com/active-directory-security/) of Fortune 1000 companies. AD's importance has grown as companies adopt hybrid and cloud infrastructure, but so has its complexity. Every application, user, and device traces back to AD for authentication and authorization, making it the ultimate target. For attackers, it represents the holy grail: [compromise Active Directory](https://specopssoft.com/blog/active-directory-attack-paths/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article), and you can access the entire network.

## Why attackers target Active Directory

AD serves as the gatekeeper for everything in your enterprise. So, when adversaries compromise AD, they gain privileged access that lets them create accounts, modify permissions, disable security controls, and move laterally, all without triggering most alerts.

The [2024 Change Healthcare breach](https://www.hipaajournal.com/change-healthcare-responding-to-cyberattack/) showed what can happen when AD is compromised. In this attack, hackers exploited a server lacking multifactor authentication, pivoted to AD, escalated privileges, and then executed a highly costly cyberattack. Patient care came to a screeching halt. Health records were exposed. The organization paid millions in ransom.

Once attackers control AD, they control your entire network. And standard security tools often struggle to detect these attacks because they look like legitimate AD operations.

### Common attack techniques

* [Golden ticket attacks](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/golden-ticket-attack/) generate counterfeit authentication tickets granting full domain access for months.
* [DCSync attacks](https://specopssoft.com/blog/active-directory-attack-paths/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) exploit replication permissions to extract password hashes directly from domain controllers.
* [Kerberoasting](https://specopssoft.com/blog/kerberoasting-attacks-in-active-directory/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) gains elevated rights by targeting service accounts with weak passwords.

## How hybrid environments expand the attack surface

Organizations running [hybrid Active Directory](https://specopssoft.com/blog/cloud-password-security-best-practices/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) face challenges that didn't exist five years ago. Your identity infrastructure now spans on-premises domain controllers, Azure AD Connect synchronization, cloud identity services, and multiple authentication protocols.

Attackers exploit this complexity, abusing synchronization mechanisms to pivot between environments. [OAuth token compromises](https://outpost24.com/blog/common-oauth-vulnerabilities-mitigations/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) in cloud services provide backdoor access to on-premises resources. And legacy protocols like [NTLM](https://specopssoft.com/blog/microsoft-phases-out-ntlm-with-kerberos/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) remain enabled for backward compatibility, giving intruders easy relay attack opportunities.

The fragmented security posture makes things worse. On-premises security teams use different tools than cloud security teams, allowing visibility gaps to emerge at the boundaries. Threat actors operate in these blind spots while security teams struggle to correlate events across platforms.

## Common vulnerabilities that attackers exploit

[Verizon's Data Breach Investigation Report](https://www.verizon.com/business/resources/reports/dbir/) found that compromised credentials are involved in 88% of breaches. [Cybercriminals harvest credentials](https://specopssoft.com/blog/credential-harvesting-explained/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) through phishing, malware, brute force, and purchasing breach databases.

### Frequent vulnerabilities in Active Directory

* **Weak passwords:** Users [reuse the same passwords](https://specopssoft.com/blog/password-reuse-hidden-danger/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) across personal and work accounts, so one breach exposes multiple systems. Standard eight-character complexity rules seem secure, but hackers can crack them in seconds.
* **Service account problems:** [Service accounts](https://specopssoft.com/blog/service-account-security-best-practices/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) often use passwords that never expire or change, and they typically have excessive permissions that allow lateral movement once compromised.
* **Cached credentials:** Workstations store administrative credentials in memory, where attackers can extract them with standard tools.
* **Poor visibility:** Teams lack insight into who uses [privileged accounts](https://specopssoft.com/blog/secure-privileged-accounts-keep-business-secrets-belong/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article), what level of access they ha...