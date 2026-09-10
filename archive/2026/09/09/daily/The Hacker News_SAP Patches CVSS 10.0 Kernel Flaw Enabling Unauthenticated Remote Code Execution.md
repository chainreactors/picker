---
title: SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution
url: https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html
source: The Hacker News
date: 2026-09-09
fetch_date: 2026-09-10T06:52:42.161589
---

# SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution](https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html)

**Ravie Lakshmanan**Sep 09, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwUnFS6EAvkjYM7AC_3-k8C6QSAmpatuThkiXaa1WxvtiZU7M-n384kpPN4-VSAQfwL8PCTPUVd3iYeTDn_V5ZoZGEfuizJSZghdAw4Ldq_wFg7rxWyKBbwdMctiiBaykAmL40L6wappUeeyIr58u8SFFSszCP-rszf5ioHsaz0dtKilEpkw1LTEmtaCtZ/s1700-nu-rw-lo-l85-e365/sap-flaws.jpg)

SAP has [released](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/september-2026.html?isu_page=1) security updates to address multiple vulnerabilities, including a maximum-severity flaw in SAP Extended Passport (EPP) Processing that could have a severe impact on the confidentiality, integrity, and availability of the application

The vulnerability, tracked as CVE-2026-44756 (CVSS score: 10.0), has been described as a case of memory corruption. [Discovered and reported](https://onapsis.com/blog/sap-security-patch-day-september-2026/) by SAP security company Onapsis, it has been codenamed [OVERPASS](https://onapsis.com/blog/sap-overpass-remediation/).

The flaw, which resides in the SAP kernel's processing of the Extended Passport (EPP), is exploitable remotely and without authentication, and allows bad actors to run arbitrary operating system commands on the SAP host with SAP administrative privileges, leading to a total compromise of the underlying SAP business data and processes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

CVE-2026-44756 stems from a missing boundary validation during the deserialization of EPP data, leading to a memory safety violation when processing externally supplied length fields. An unauthenticated attacker can exploit this loophole to send crafted network requests containing a malformed EPP header and trigger unintended behavior and abnormal program termination.

"OVERPASS is a flaw in the SAP kernel code that processes this structure. A specially-crafted request sent to an affected system can be abused to take control of the receiving process and, from there, run operating system commands on the host," Onapsis CTO JP Perez-Etchegoyen said.

"Because EPP processing is shared kernel code used by more than one protocol, the flaw is reachable from the internet-facing web layer, from the SAP GUI layer every end user connects to, and from the RFC layer that links SAP systems to one another. It is reachable through several SAP components and several communication protocols, none of them requiring credentials, so no single network control can fully mitigate risk."

Successful exploitation can permit an attacker to read the SAP secure store to recover database credentials, password hashes and all housed business data; read the live session data of logged-in users; extract stored credentials to move laterally into every other SAP system; and modify application data, system configuration and the SAP binaries.

The second critical flaw patched by SAP is CVE-2026-58240 (CVSS score: 9.8), a missing Authentication check in SAP NetWeaver Message Server that unauthenticated attackers with network access can exploit to perform unauthorized actions. Onapsis, which also discovered the vulnerability, has assigned it the name S4GET.

"S4GET is a logic flaw, not a misconfiguration," security researcher Pablo 'Partu' Agustin Artuso [said](https://onapsis.com/blog/s4get-cve-2026-58240-sap-message-server-threat-advisory/). "It is present in SAP's 9.x kernel lines – the kernels that SAP S/4HANA and SAP S/4HANA Cloud Private Edition run on, and potentially other ABAP-based products as well."

"What makes it uniquely dangerous is its reachability: the flaw is triggered through the same public port that every SAP GUI client connects to, so it cannot be firewalled away without breaking the end-user logon. Exploitation requires no credentials, no certificate, and no pre-existing misconfiguration. A successful attack yields full remote code execution as <sid>adm, the OS-level user that runs SAP, on every application server in the cluster."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

Two other critical-rated security flaws patched by SAP are as follows -

* **CVE-2026-76969** (CVSS score: 9.4) - A credential disclosure vulnerability in multi-tenant applications using SAP Cloud Application Programming Model (CAP) that allows an unauthenticated attacker to obtain sensitive credentials by sending specially crafted requests, and then use them to replace or delete tenant data.
* **CVE-2026-66768** (CVSS score: 9.0) - An improper access control vulnerability in SAP NetWeaver SAP GUI for Java that allows execution of arbitrary commands on the underlying host.

Although none of the security vulnerabilities have been exploited to date, the criticality of the flaws requires immediate attention. Onapsis is recommending that users inventory every SAP system, patch internet-facing systems before internal instances, reduce exposure where possible, and monitor for exploitation attempts.

"Ensure you have visibility into your SAP application layer so that attempts to exploit this vulnerability can be detected and investigated while the rollout is in progress," Perez-Etchegoyen said about CVE-2026-44756.

"One point is worth stating plainly: SAP authorizations and Segregation of Duties (SoD) controls will not help. The vulnerable code runs before any authentication step, so locking users, tightening roles, enforcing password policies or restricting transaction access has no effect on this attack path."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedi...