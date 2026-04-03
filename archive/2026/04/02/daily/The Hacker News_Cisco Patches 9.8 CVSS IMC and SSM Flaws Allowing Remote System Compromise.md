---
title: Cisco Patches 9.8 CVSS IMC and SSM Flaws Allowing Remote System Compromise
url: https://thehackernews.com/2026/04/cisco-patches-98-cvss-imc-and-ssm-flaws.html
source: The Hacker News
date: 2026-04-02
fetch_date: 2026-04-03T04:29:26.550615
---

# Cisco Patches 9.8 CVSS IMC and SSM Flaws Allowing Remote System Compromise

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Cisco Patches 9.8 CVSS IMC and SSM Flaws Allowing Remote System Compromise](https://thehackernews.com/2026/04/cisco-patches-98-cvss-imc-and-ssm-flaws.html)

**Ravie Lakshmanan**Apr 02, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH6wuST9R8voZTpCC-v5LSwd4O7vlbuRDhXMzcSw9iu0k2JvFOao-3Jr2o9iCs0jqX3pIqHvcYo_n-5Ad80WXeQXKV_DTgJUN0A6nl9f73BA1U0wRoZBqgySfDR6Uk7KD8jXzw2BFLGvusf-96qsINw9jT4PnglZohYM2VhSsdHcpw-cl6vwAekfE-KD_H/s1700-e365/cisco-exploit.jpg)

Cisco has released updates to address a critical security flaw in the Integrated Management Controller (IMC) that, if successfully exploited, could allow an unauthenticated, remote attacker to bypass authentication and gain access to the system with elevated privileges.

The vulnerability, tracked as CVE-2026-20093, carries a CVSS score of 9.8 out of a maximum of 10.0.

"This vulnerability is due to incorrect handling of password change requests," Cisco [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-auth-bypass-AgG2BxTn) in an advisory released Wednesday. "An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device."

"A successful exploit could allow the attacker to bypass authentication, alter the passwords of any user on the system, including an Admin user, and gain access to the system as that user."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Security researcher "jyh" has been credited with discovering and reporting the vulnerability. The shortcoming affects the following products regardless of the device configuration -

* 5000 Series Enterprise Network Compute Systems (ENCS) - Fixed in 4.15.5
* Catalyst 8300 Series Edge uCPE - Fixed in 4.18.3
* UCS C-Series M5 and M6 Rack Servers in standalone mode - Fixed in 4.3(2.260007), 4.3(6.260017), and 6.0(1.250174)
* UCS E-Series Servers M3 - Fixed in 3.2.17
* UCS E-Series Servers M6 - Fixed in 4.15.3

Another critical vulnerability patched by Cisco impacts Smart Software Manager On-Prem (SSM On-Prem), which could enable an unauthenticated, remote attacker to execute arbitrary commands on the underlying operating system. The vulnerability, CVE-2026-20160 (CVSS score: 9.8), stems from an unintentional exposure of an internal service.

"An attacker could exploit this vulnerability by sending a crafted request to the API of the exposed service," Cisco [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ssm-cli-execution-cHUcWuNr). "A successful exploit could allow the attacker to execute commands on the underlying operating system with root-level privileges."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Patches for the flaw have been released in Cisco SSM On-Prem version 9-202601. Cisco said the vulnerability was discovered internally during the resolution of a Cisco Technical Assistance Center (TAC) support case.

While neither of the vulnerabilities has been exploited in the wild, a number of[recently](https://thehackernews.com/2026/02/cisco-sd-wan-zero-day-cve-2026-20127.html)[disclosed](https://thehackernews.com/2026/03/cisco-confirms-active-exploitation-of.html) security flaws in Cisco products have been weaponized by threat actors. In the absence of a workaround, customers are recommended to update to the fixed version for optimal protection.

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

[cisco](https://thehackernews.com/search/label/cisco), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [network security](https://thehackernews.com/search/label/network%20security), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Citrix NetScaler Under Active Recon for CVE-2026-3055 (CVSS 9.3) Memory Overread Bug](data:image/svg+xml;base64... "Citrix NetScaler Under Active Recon for CVE-2026-3055 (CVSS 9.3) Memory Overread Bug")

Citrix NetScaler Under Active Recon for CVE-2026-3055 (CVSS 9.3) Memory Overread Bug](https://thehackernews.com/2026/03/citrix-netscaler-under-active-recon-for.html)

[![CISA Adds CVE-2025-53521 to KEV After Active F5 BIG-IP APM Exploitation](data:image/svg+xml;base64... "CISA Adds CVE-2025-53521 to KEV After Active F5 BIG-IP APM Exploitation")

CISA Adds CVE-2025-53521 to KEV After Active F5 BIG-IP APM Exploitation](https://thehackernews.com/2026/03/cisa-adds-cve-2025-53521-to-kev-after.html)

[![TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files](data:image/svg+xml;base64... "TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files")

TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files](https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html)

[![China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks](data...