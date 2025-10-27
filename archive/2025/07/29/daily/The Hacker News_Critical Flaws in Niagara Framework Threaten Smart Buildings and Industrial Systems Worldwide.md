---
title: Critical Flaws in Niagara Framework Threaten Smart Buildings and Industrial Systems Worldwide
url: https://thehackernews.com/2025/07/critical-flaws-in-niagara-framework.html
source: The Hacker News
date: 2025-07-29
fetch_date: 2025-10-06T23:58:29.839814
---

# Critical Flaws in Niagara Framework Threaten Smart Buildings and Industrial Systems Worldwide

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

# [Critical Flaws in Niagara Framework Threaten Smart Buildings and Industrial Systems Worldwide](https://thehackernews.com/2025/07/critical-flaws-in-niagara-framework.html)

**Jul 28, 2025**Ravie LakshmananVulnerability / Critical Infrastructure

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf1_6YYkQ-zZ6XYMDfViWj1UXcPc8IAU97a_M-aS6Y4v4XnA_II0iT6NQv3dz8gJvDnBQTKfTQhwZQPn4wD2nwQJ3Zu_1PPet21oqsnl0x5RdC9viPJ5pC25mz6rYAghDKwchSOHPdqrcIhl46Qrf-run82RVUfDILM1X8OAs6JYn5x5OQHWTaI0D7dqwM/s790-rw-e365/exploit.jpg)

Cybersecurity researchers have discovered over a dozen security vulnerabilities impacting [Tridium's Niagara Framework](https://www.tridium.com/us/en/Products/niagara) that could allow an attacker on the same network to compromise the system under certain circumstances.

"These vulnerabilities are fully exploitable if a Niagara system is misconfigured, thereby disabling encryption on a specific network device," Nozomi Networks Labs [said](https://www.nozominetworks.com/blog/critical-vulnerabilities-found-in-tridium-niagara-framework) in a report published last week. "If chained together, they could allow an attacker with access to the same network — such as through a Man-in-the-Middle (MiTM) position — to compromise the Niagara system."

Developed by Tridium, an independent business entity of Honeywell, the Niagara Framework is a vendor-neutral platform used to manage and control a wide range of devices from different manufacturers, such as HVAC, lighting, energy management, and security, making it a valuable solution in building management, industrial automation, and smart infrastructure environments.

It consists of two key components: Station, which communicates with and controls connected devices and systems, and Platform, which is the underlying software environment that provides the necessary services to create, manage, and run Stations.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The vulnerabilities identified by Nozomi Networks are exploitable should a Niagara system be misconfigured, causing encryption to be disabled on a network device and opening the door to lateral movement and broader operational disruptions, impacting safety, productivity, and service continuity.

The most severe of the issues are listed below -

* **CVE-2025-3936** (CVSS score: 9.8) - Incorrect Permission Assignment for Critical Resource
* **CVE-2025-3937** (CVSS score: 9.8) - Use of Password Hash With Insufficient Computational Effort
* **CVE-2025-3938** (CVSS score: 9.8) - Missing Cryptographic Step
* **CVE-2025-3941** (CVSS score: 9.8) - Improper Handling of Windows: DATA Alternate Data Stream
* **CVE-2025-3944** (CVSS score: 9.8) - Incorrect Permission Assignment for Critical Resource
* **CVE-2025-3945** (CVSS score: 9.8) - Improper Neutralization of Argument Delimiters in a Command
* **CVE-2025-3943** (CVSS score: 7.3) - Use of GET Request Method With Sensitive Query Strings

Nozomi Networks said it was able to craft an exploit chain combining CVE-2025-3943 and CVE-2025-3944 that could enable an adjacent attacker with access to the network to breach a Niagara-based target device, ultimately facilitating root-level remote code execution.

Specifically, the attacker could weaponize CVE-2025-3943 to intercept the anti-CSRF (cross-site request forgery) refresh token in scenarios where the Syslog service is enabled, causing the logs containing the token to be transmitted potentially over an unencrypted channel.

Armed with the token, the threat actor can trigger a CSRF attack and lure an administrator into visiting a specially crafted link that causes the content of all incoming HTTP requests and responses to be fully logged. The attacker then proceeds to extract the administrator's JSESSIONID session token and use it to connect to the Niagara Station with full elevated permissions and creates a new backdoor administrator user for persistent access.

In the next stage of the attack, the administrative access is abused to download the private key associated with the device's TLS certificate and conduct adversary-in-the-middle (AitM) attacks by taking advantage of the fact that both the Station and Platform share the same certificate and key infrastructure.

With control of the Platform, the attacker could leverage CVE-2025-3944 to facilitate root-level remote code execution on the device, achieving complete takeover. Following responsible disclosure, the issues have been [addressed](https://www.honeywell.com/content/dam/honeywellbt/en/documents/downloads/product-security/security-notification/hon-corp-niagara-software-vulnerabilities-2025-05-22-01.pdf) in Niagara Framework and Enterprise Security versions 4.14.2u2, 4.15.u1, or 4.10u.11.

"Because Niagara often connects critical systems and sometimes bridges IoT technology and information technology (IT) networks, it could represent a high-value target," the company said.

"Given the critical functions that can be controlled by Niagara-powered systems, these vulnerabilities may pose a high risk to operational resilience and security provided the instance has not been configured per Tridium's hardening guidelines and best practices."

The disclosure comes as several memory corruption flaws have been discovered in the [P-Net C library](https://github.com/rtlabs-com/p-net), an open-source implementation of the PROFINET protocol for IO devices, that, if successfully exploited, could allow unauthenticated attackers with network access to the targeted device to trigger denial-of-service (DoS) conditions.

"Practically speaking, exploiting CVE-2025-32399, an attacker can force the CPU running the P-Net library into an infinite loop, consuming 100% CPU resources," Nozomi Networks [said](https://www.nozominetworks.com/blog/fuzzing-the-p-net-profinet-implementation). "Another vulnerability, tracked as CVE-2025-32405, allows an attacker to write beyond the boundaries of a connection buffer, corrupting memory ...