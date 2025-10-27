---
title: Critical Golden dMSA Attack in Windows Server 2025 Enables Cross-Domain Attacks and Persistent Access
url: https://thehackernews.com/2025/07/critical-golden-dmsa-attack-in-windows.html
source: The Hacker News
date: 2025-07-17
fetch_date: 2025-10-06T23:55:37.855748
---

# Critical Golden dMSA Attack in Windows Server 2025 Enables Cross-Domain Attacks and Persistent Access

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Critical Golden dMSA Attack in Windows Server 2025 Enables Cross-Domain Attacks and Persistent Access](https://thehackernews.com/2025/07/critical-golden-dmsa-attack-in-windows.html)

**Jul 16, 2025**Ravie LakshmananWindows Server / Enterprise Security

[![Critical dMSA Flaw in Windows Server 2025](data:image/png;base64... "Critical dMSA Flaw in Windows Server 2025")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlJCm6yLGbBy-Ehi1vPF-58giukStT95x7hb_-XcGMTWq5EmeLsQCYIfhv5j6PVfzA84zWBQUSO_iWSOGt1n2U3eQsMS7g5ObJ6KiCc0s8-WenbQxC9siswGEmSeKlMiv7BSRuBcYM_jfZytOK0uAZ7EYyMelz_WDCI8MmGKOQHtunW69Hkbe8tdQFjFp6/s790-rw-e365/dmsa-exploit.jpg)

Cybersecurity researchers have disclosed what they say is a "critical design flaw" in delegated Managed Service Accounts (dMSAs) introduced in Windows Server 2025.

"The flaw can result in high-impact attacks, enabling cross-domain lateral movement and persistent access to all managed service accounts and their resources across Active Directory indefinitely," Semperis said in a report shared with The Hacker News.

Put differently, successful exploitation could allow adversaries to sidestep authentication guardrails and generate passwords for all Delegated Managed Service Accounts ([dMSAs](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-overview)) and group Managed Service Accounts ([gMSAs](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview)) and their associated service accounts.

The persistence and privilege escalation method has been codenamed **Golden dMSA**, with the cybersecurity company deeming it as low complexity owing to the fact that the vulnerability simplifies brute-force password generation.

However, in order for bad actors to exploit it, they must already be in possession of a Key Distribution Service (KDS) [root key](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key) that's typically only available to privileged accounts, such as root Domain Admins, Enterprise Admins, and SYSTEM.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Described as the crown jewel of Microsoft's gMSA infrastructure, the KDS root key serves as a master key, allowing an attacker to derive the current password for any dMSA or gMSA account without having to connect to the domain controller (DC).

"The attack leverages a critical design flaw: A structure that's used for the password-generation computation contains predictable time-based components with only 1,024 possible combinations, making brute-force password generation computationally trivial," security researcher Adi Malyanker [said](https://www.semperis.com/blog/golden-dmsa-what-is-dmsa-authentication-bypass).

Delegated Managed Service Accounts is a new feature [introduced](https://thehackernews.com/2025/05/critical-windows-server-2025-dmsa.html) by Microsoft that facilitates migration from an existing legacy service account. It was introduced in Windows Server 2025 as a way to counter Kerberoasting attacks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvVJDwufLY2IMhnBEBkY6K47leZRGiCF875G68T06kIXyHx9SDo_tPSj-73hzhQjj0Wv-maOFLrz_M17HspwGsQRE5wagF2IsFOKzF9zfPmWLdLZdtlBvD83pwycHvKq4kS2WgJJ7OpIr-CmbuQKnScfM83AvSvbUEydWXFxMiG4DGXPOuFK-u-fU8frCS/s790-rw-e365/chart.jpg)

The machine accounts bind authentication directly to explicitly authorized machines in Active Directory (AD), thus eliminating the possibility of credential theft. By tying authentication to device identity, only specified machine identities mapped in AD can access the account.

Golden dMSA, similar to [Golden gMSA](https://www.semperis.com/blog/golden-gmsa-attack/) Active Directory [attacks](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/recover-from-golden-gmsa-attack), plays out over four steps once an attacker has obtained elevated privileges within a domain -

* Extracting KDS root key material by elevating to SYSTEM privileges on one of the domain controllers
* Enumerating dMSA accounts using [LsaOpenPolicy](https://learn.microsoft.com/en-us/windows/win32/api/ntsecapi/nf-ntsecapi-lsaopenpolicy) and [LsaLookupSids](https://learn.microsoft.com/en-us/windows/win32/api/ntsecapi/nf-ntsecapi-lsalookupsids) APIs or via a Lightweight Directory Access Protocol ([LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol))-based approach
* Identifying the [ManagedPasswordID](https://learn.microsoft.com/en-us/windows/win32/adschema/a-msds-managedpasswordid) attribute and password hashes through targeted guessing
* Generating valid passwords (i.e., Kerberos tickets) for any gMSA or dMSA associated with the compromised key and testing them via [Pass the Hash](https://www.semperis.com/blog/pass-the-hash-attack-explained/) or [Overpass the Hash](https://www.semperis.com/blog/how-to-defend-against-overpass-the-hash-attack/) techniques

"This process requires no additional privileged access once the KDS root key is obtained, making it a particularly dangerous persistence method," Malyanker said.

"The attack highlights the critical trust boundary of managed service accounts. They rely on domain-level cryptographic keys for security. Although automatic password rotation provides excellent protection against typical credential attacks, Domain Admins, DnsAdmins, and Print Operators can bypass these protections entirely and compromise all of the dMSAs and gMSAs in the forest."

Semperis noted that the Golden dMSA technique turns the breach into a forest-wide persistent backdoor, given that compromising the KDS root key from any single domain within the forest is enough to breach every dMSA account across all doma...