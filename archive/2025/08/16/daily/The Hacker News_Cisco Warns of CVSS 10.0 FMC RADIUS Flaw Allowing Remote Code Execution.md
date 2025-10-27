---
title: Cisco Warns of CVSS 10.0 FMC RADIUS Flaw Allowing Remote Code Execution
url: https://thehackernews.com/2025/08/cisco-warns-of-cvss-100-fmc-radius-flaw.html
source: The Hacker News
date: 2025-08-16
fetch_date: 2025-10-07T00:49:54.812588
---

# Cisco Warns of CVSS 10.0 FMC RADIUS Flaw Allowing Remote Code Execution

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

# [Cisco Warns of CVSS 10.0 FMC RADIUS Flaw Allowing Remote Code Execution](https://thehackernews.com/2025/08/cisco-warns-of-cvss-100-fmc-radius-flaw.html)

**Aug 15, 2025**Ravie LakshmananVulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikiELTSHyWHi7CSFi6tYtpffVVvHCmkPhCmPVocvkSuRS54UnTJ9IZUpKS88W021yRHJrtjQw24uS_6-zkLCcxJHT959CPDLmMm27WCb98N3lBJl1rMl5fwzXNE0E52W9ASt_jTJPxBZmC_xpX7S6UqiOgmAnF5ZkyBv9QYqzOei7t6zyrh4T59G01i_bg/s790-rw-e365/cisco-flaw.jpg)

Cisco has released security updates to address a maximum-severity security flaw in Secure Firewall Management Center (FMC) Software that could allow an attacker to execute arbitrary code on affected systems.

The vulnerability, assigned the CVE identifier **CVE-2025-20265** (CVSS score: 10.0), affects the RADIUS subsystem implementation that could permit an unauthenticated, remote attacker to inject arbitrary shell commands that are executed by the device.

The networking equipment major said the issue stems from a lack of proper handling of user input during the authentication phase, as a result of which an attacker could send specially crafted input when entering credentials that get authenticated at the configured RADIUS server.

"A successful exploit could allow the attacker to execute commands at a high privilege level," the company [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-radius-rce-TNBKf79) in a Thursday advisory. "For this vulnerability to be exploited, Cisco Secure FMC Software must be configured for RADIUS authentication for the web-based management interface, SSH management, or both."

The shortcoming impacts Cisco Secure FMC Software releases 7.0.7 and 7.7.0 if they have RADIUS authentication enabled. There are no workarounds other than applying the patches provided by the company. Brandon Sakai of Cisco has been credited with discovering the issue during internal security testing.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Besides CVE-2025-20265, Cisco has also resolved a number of high-severity bugs -

* **[CVE-2025-20217](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-dos-SvKhtjgt)** (CVSS score: 8.6) - Cisco Secure Firewall Threat Defense Software Snort 3 Denial-of-Service Vulnerability
* **[CVE-2025-20222](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fp2k-IPsec-dos-tjwgdZCO)** (CVSS score: 8.6) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Firepower 2100 Series IPv6 over IPsec Denial-of-Service Vulnerability
* **[CVE-2025-20224, CVE-2025-20225, CVE-2025-20239](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-ios-dos-DOESHWHy)** (CVSS scores: 8.6) - Cisco IOS, IOS XE, Secure Firewall Adaptive Security Appliance, and Secure Firewall Threat Defense Software IKEv2 Denial-of-Service Vulnerabilities
* **[CVE-2025-20133, CVE-2025-20243](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-mfPekA6e)** (CVSS scores: 8.6) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access SSL VPN Denial-of-Service Vulnerabilities
* **[CVE-2025-20134](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ssltls-dos-eHw76vZe)** (CVSS score: 8.6) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software SSL/TLS Certificate Denial-of-Service Vulnerability
* **[CVE-2025-20136](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-nat-dns-dos-bqhynHTM)** (CVSS score: 8.6) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Network Address Translation DNS Inspection Denial-of-Service Vulnerability
* **[CVE-2025-20263](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-buffer-overflow-PyRUhWBC)** (CVSS score: 8.6) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Web Services Denial-of-Service Vulnerability
* **[CVE-2025-20148](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-html-inj-MqjrZrny)** (CVSS score: 8.5) - Cisco Secure Firewall Management Center Software HTML Injection Vulnerability
* **[CVE-2025-20251](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-http-file-hUyX2jL4)** (CVSS score: 8.5) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software VPN Web Server Denial-of-Service Vulnerability
* **[CVE-2025-20127](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-3100_4200_tlsdos-2yNSCd54)** (CVSS score: 7.7) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Firepower 3100 and 4200 Series TLS 1.3 Cipher Denial-of-Service Vulnerability
* **[CVE-2025-20244](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpnwebs-dos-hjBhmBsX)** (CVSS score: 7.7) - Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access VPN Web Server Denial-of-Service Vulnerability

While none of the flaws have come under active exploitation in the wild, with network appliances repeatedly getting caught in the attackers' crosshairs, it's essential that users move quickly to update their instances to the latest version.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read mo...