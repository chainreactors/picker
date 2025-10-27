---
title: CISA Warns of Multiple Critical Vulnerabilities Affecting Mitsubishi Electric PLCs
url: https://thehackernews.com/2022/12/cisa-warns-of-multiple-critical.html
source: The Hacker News
date: 2022-12-03
fetch_date: 2025-10-04T00:26:32.812907
---

# CISA Warns of Multiple Critical Vulnerabilities Affecting Mitsubishi Electric PLCs

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

# [CISA Warns of Multiple Critical Vulnerabilities Affecting Mitsubishi Electric PLCs](https://thehackernews.com/2022/12/cisa-warns-of-multiple-critical.html)

**Dec 02, 2022**Ravie LakshmananICS Security / Encryption

[![Mitsubishi Electric PLCs](data:image/png;base64... "Mitsubishi Electric PLCs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMP40s2GceY2AStw_gk9ngnI3lgH7isnmpOBVXx8pr7_YPC7fxsO1Pyqdo0M0tKWE_Q9jU718owbQdzdfw5QeJXbcIxzUbVijVLicv49yVqIz02H9qfnZeASAJoSxtfNeeePlPIYXUVZ1F1mLEsMpEhI-FWbC8tk064BFU3lhDipAHZv7Fvcw2Yxe5/s790-rw-e365/Mitsubishi.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) this week released an Industrial Control Systems (ICS) advisory warning of multiple vulnerabilities in Mitsubishi Electric GX Works3 engineering software.

"Successful exploitation of these vulnerabilities could allow unauthorized users to gain access to the MELSEC iQ-R/F/L series CPU modules and the MELSEC iQ-R series OPC UA server module or to view and execute programs," the agency [said](https://www.cisa.gov/uscert/ics/advisories/icsa-22-333-05).

[GX Works3](https://www.mitsubishielectric.com/fa/products/cnt/plceng/smerit/gx_works3/index.html) is an [engineering workstation](https://www.cisa.gov/uscert/ics/Control_System_Engineering_Workstation-Definition.html) software used in ICS environments, acting as a mechanism for uploading and downloading programs from/to the controller, troubleshooting software and hardware issues, and performing maintenance operations.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The wide range of functions also makes the platform an attractive target for threat actors looking to compromise such systems to commandeer the [managed PLCs](https://thehackernews.com/2021/08/unpatched-security-flaws-expose.html).

Three of the 10 shortcomings relate to cleartext storage of sensitive data, four relate to the use of a hard-coded cryptographic key, two relate to the use of a hard-coded password, and one concerns a case of insufficiently protected credentials.

The most critical of the bugs, [CVE-2022-25164](https://nvd.nist.gov/vuln/detail/CVE-2022-25164), and [CVE-2022-29830](https://nvd.nist.gov/vuln/detail/CVE-2022-29830), carry a CVSS score of 9.1 and could be abused to gain access to the CPU module and obtain information about project files without requiring any permissions.

Nozomi Networks, which discovered [CVE-2022-29831](https://nvd.nist.gov/vuln/detail/CVE-2022-29831) (CVSS score: 7.5), said an attacker with access to a safety PLC project file could exploit the hard-coded password to directly access the safety CPU module and potentially disrupt industrial processes.

"Engineering software represents a critical component in the security chain of industrial controllers," the company [said](https://www.nozominetworks.com/blog/flaws-in-gx-works3-threaten-mitsubishi-electric-safety-plc-security/). "Should any vulnerabilities arise in them, adversaries may abuse them to ultimately compromise the managed devices and, consequently, the supervised industrial process."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as CISA [revealed](https://www.cisa.gov/uscert/ncas/current-activity/2022/12/01/cisa-releases-three-industrial-control-systems-advisories) details of a denial-of-service (DoS) vulnerability in Mitsubishi Electric MELSEC iQ-R Series that stems from a lack of proper input validation ([CVE-2022-40265](https://nvd.nist.gov/vuln/detail/CVE-2022-40265), CVSS score: 8.6).

"Successful exploitation of this vulnerability could allow a remote unauthenticated attacker to cause a denial-of-service condition on a target product by sending specially crafted packets," CISA noted.

In a related development, the cybersecurity agency further outlined three issues impacting Remote Compact Controller (RCC) 972 from Horner Automation, the most critical of which ([CVE-2022-2641](https://nvd.nist.gov/vuln/detail/CVE-2022-2641), CVSS score: 9.8) could lead to remote code execution or cause a DoS condition.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[CISA](https://thehackernews.com/search/label/CISA)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[encryption](https://thehackernews.com/search/label/encryption)[Mitsubishi](https://thehackernews.com/search/label/Mitsubishi)[password security](https://thehackernews.com/search/label/password%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admi...