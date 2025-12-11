---
title: Fortinet, Ivanti, and SAP Issue Urgent Patches for Authentication and Code Execution Flaws
url: https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html
source: The Hacker News
date: 2025-12-10
fetch_date: 2025-12-11T03:25:11.906097
---

# Fortinet, Ivanti, and SAP Issue Urgent Patches for Authentication and Code Execution Flaws

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Fortinet, Ivanti, and SAP Issue Urgent Patches for Authentication and Code Execution Flaws](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html)

**Dec 10, 2025**Ravie LakshmananVulnerability / Endpoint Security

[![Fortinet, Ivanti, and SAP Issue Urgent Patches](data:image/png;base64... "Fortinet, Ivanti, and SAP Issue Urgent Patches")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK0R-QzlGdiLRGA3gSZBJ0bMFvDgCeIgaL7lrq_FTLjhBMQUG6WN0Br_556xWrtqsM1U3814t28KYCkYXcp9CJS4P_jaFPJrLkcku0G1w2N44ocsawmjWgwqog3Uz3ef4kfG6z7F9J56F-O9ReNGWJlVnizYgI-i9PC_GTo2FCnajwj9CBc_-zoaEWwaz-/s790-rw-e365/sap.jpg)

Fortinet, Ivanti, and SAP have moved to address critical security flaws in their products that, if successfully exploited, could result in an authentication bypass and code execution.

The Fortinet vulnerabilities affect FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager and relate to a case of improper verification of a cryptographic signature. They are tracked as **CVE-2025-59718** and **CVE-2025-59719** (CVSS scores: 9.8).

"An Improper Verification of Cryptographic Signature vulnerability [CWE-347] in FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication via a crafted SAML message, if that feature is enabled on the device," Fortinet [said](https://fortiguard.fortinet.com/psirt/FG-IR-25-647) in an advisory.

The company, however, noted that the FortiCloud SSO login feature is not enabled in the default factory settings. FortiCloud SSO login is enabled when an administrator registers the device to FortiCare and has not disabled the toggle "Allow administrative login using FortiCloud SSO" in the registration page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

To temporarily protect their systems against attacks exploiting these vulnerabilities, organizations are advised to disable the FortiCloud login feature (if enabled) until it can be updated. This can be done in two ways -

* Go to System -> Settings -> Switch "Allow administrative login using FortiCloud SSO" to Off
* Run the below command in the CLI -

```
config system global
set admin-forticloud-sso-login disable
end
```

### Ivanti Releases Fix for Critical EPM Flaw

Ivanti has also shipped updates to address four security flaws in Endpoint Manager (EPM), one of which is a critical severity bug in the EPM core and remote consoles. The vulnerability, assigned the CVE identifier **CVE-2025-10573**, carries a CVSS score of 9.6.

"Stored XSS in Ivanti Endpoint Manager prior to version 2024 SU4 SR1 allows a remote unauthenticated attacker to execute arbitrary JavaScript in the context of an administrator session," Ivanti [said](https://forums.ivanti.com/s/article/Security-Advisory-EPM-December-2025-for-EPM-2024?language=en_US).

Rapid7 security researcher Ryan Emmons, who discovered and reported the shortcoming on August 15, 2025, said it allows an attacker with unauthenticated access to the primary EPM web service to join fake managed endpoints to the EPM server so as to poison the administrator web dashboard with malicious JavaScript.

"When an Ivanti EPM administrator views one of the poisoned dashboard interfaces during normal usage, that passive user interaction will trigger client-side JavaScript execution, resulting in the attacker gaining control of the administrator's session," Emmons [said](https://www.rapid7.com/blog/post/cve-2025-10573-ivanti-epm-unauthenticated-stored-cross-site-scripting-fixed/).

Douglas McKee, director of vulnerability intelligence at Rapid7, said in a statement that CVE-2025-10573 represents a serious risk as it's trivial to exploit and can be done so by sending a fake device report to the server using a basic file format.

"While the attack only fully executes when an administrator views the dashboard, this is a routine and necessary task for IT staff; consequently, the likelihood of triggering the exploit during normal operations is high, ultimately allowing the attacker to take control of the administrator's session," McKee added.

Ensar Seker, CISO at threat intelligence company SOCRadar, also emphasized that the user interaction requirement doesn't reduce the vulnerability's threat level and that it has a "significant" exploitation potential when combined with social engineering.

"Remote code execution via JavaScript injection is no longer theoretical in supply chain attacks; it’s become operationally viable," Seker said. "Organizations must act swiftly to patch, and more importantly, implement rigorous user interface sanitization and privilege segmentation."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The company [noted](https://www.ivanti.com/blog/december-2025-security-update) that user interaction is required to exploit the flaw and that it's not aware of any attacks in the wild. It has been patched in EPM version 2024 SU4 SR1.

Also patched in the same version are three other high-severity vulnerabilities (CVE-2025-13659, CVE-2025-13661, and CVE-2025-13662) that could allow a remote, unauthenticated attacker to achieve arbitrary code execution. CVE-2025-13662, like in the case of CVE-2025-59718 and CVE-2025-59719, stems from improper verification of cryptographic signatures in the patch management component.

### SAP Fixes Three Critical Flaws

Lastly, SAP has [pushed](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/december-2025.html) December security updates to address 14 vulnerabilities across multiple products, including three critical-severity flaws. They are listed below -

* **CVE-2025-42880** (CVSS score: 9.9) - A code injection vulnerability in SAP Solution Manager
* **CVE-2025-55754** (CVSS score: 9.6) - Multiple vulnerabilities in Apache Tomcat within SAP Commerce Cloud
* **CVE-2025-42928** (CVSS score: 9.1) - A deserialization vulnerability in SAP jConnect SDK for Sybase Adaptive Server Enterprise (ASE)

Boston-based...