---
title: SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution
url: https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html
source: The Hacker News
date: 2026-11-10
fetch_date: 2026-11-11T08:35:40.646296
---

# SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution](https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html)

**Swati Khandelwal**Nov 10, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo4snqwJ4uD_sRDyI8zs23mcfFTWfZoSrn9n1hbUrsHbyWy-1VFL8amxqQnLb7LSTPkuSwnsPofUJT6anObg-nU4Q5e01WBb3IixN_PdL-1MJ2nOip4qSTEoVDmePRlOgjSVjvtbH8vFlQgxtGuKuqmuHWLyzIavw2Sj4VtZBlTYhUqeySbQcDMEr4Wns/s1700-nu-rw-lo-l85-e365/sap-flaws.jpg)

Four flaws that attackers could exploit without logging in were fixed today as part of SAP's monthly Security Patch Day—the vendor rates all four 10.0, the maximum CVSS score.

Three are in the SAP NetWeaver application server, the software SAP systems run on, and one is in the Web Dispatcher, which receives web requests from the internet and passes them on to that server.

The flaws in the Web Dispatcher and the Internet Communication Manager (ICM), which handles the server's web traffic, could allow an attacker who can reach the software over the network to run code, the vendor says.

The flaw in the server's SAML 2.0 service provider, which hands off user sign-in to an identity provider, could allow an attacker to log in as any user on some systems that use SAML single sign-on.

The flaw in SAP Gateway, which connects the server to other SAP systems and programs, could allow an attacker to impersonate one of the system's own servers and take unauthorized actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

None of the four require any user action to work.

### Affected Versions and SAP Notes

Each flaw is fixed in its own note, and the affected versions differ by component, according to SAP's November [security bulletin](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/november-2026.html). The notes are in SAP for Me, which requires a sign-in, and the vendor strongly recommends applying them as a priority.

| CVE | Component | SAP Note | Affected versions |
| --- | --- | --- | --- |
| CVE-2026-76964 | Internet Communication Manager (ICM), SAP NetWeaver AS ABAP | [Note 3778530](https://me.sap.com/notes/3778530) | KRNL64UC 7.53, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20 |
| CVE-2026-89126 | SAP Web Dispatcher | [Note 3778556](https://me.sap.com/notes/3778556) | HDB 2.00, KRNL64UC 7.53, WEBDISP 7.53, 7.54, 7.77, 7.93, 9.16, XS\_ADVANCED\_RUNTIME 1.00, SAP\_EXTENDED\_APP\_SERVICES 1, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20 |
| CVE-2026-89103 | SAP Gateway | [Note 3798345](https://me.sap.com/notes/3798345) | KRNL64NUC 7.22, 7.22EXT, KRNL64UC 7.22, 7.22EXT, 7.53, 8.04, KERNEL 7.22, 7.53, 7.54, 7.77, 7.93, 8.04, 9.16, 9.20, 9.21 |
| CVE-2026-120017 | SAML2 service provider, SAP NetWeaver AS ABAP and ABAP Platform | [Note 3849308](https://me.sap.com/notes/3849308) | SAP\_BASIS 702, 731, 740, 750, 751, 752, 753, 754, 755, 756, 757, 758, 816, 920, 921, 922 |

Kernels that are out of maintenance are affected too, according to Onapsis, an SAP security company whose researchers found the ICM, Web Dispatcher and Gateway flaws. Its [ICM2SHELL advisory](https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/) lists kernels 7.40, 7.41, 7.42, 7.45, 7.49, 7.73, 7.81, 7.85 and 7.89 for the ICM and Web Dispatcher flaws, and its [PROXYGATE advisory](https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/) lists the same kernels plus 7.20 and 7.21 for the Gateway flaw. These kernels may not get a fix and need an upgrade to one that is still maintained.

### What Each Flaw Allows

On the affected SAML setups, an attacker could use CVE-2026-120017 to log in as privileged users too, according to the vendor. A full compromise could follow, possibly reaching connected systems.

A [different SAML flaw](https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html) in the same software, CVE-2026-44748, was fixed on June 9 and needed an attacker with a normal user account.

In the ICM flaw (CVE-2026-76964) and the Web Dispatcher flaw (CVE-2026-89126), crafted network traffic could corrupt memory. An attacker who succeeds could then run code and fully compromise the system.

Onapsis says both flaws come from one bug, which it calls ICM2SHELL, in kernel code the ICM and Web Dispatcher share for putting split WebSocket messages back together. It gave the vendor a working exploit that runs operating system commands as <sid>adm, the account that owns the SAP installation.

The same bug can crash either component, and a crashed Web Dispatcher cuts off every SAP system behind it while it restarts. WebSocket support is on by default, so a system is exposed even if nothing uses it, and dual-stack systems are affected through their ABAP stack. The company's researchers have not seen the bug exploited in attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

SAP Gateway uses access control lists to decide which outside programs may connect to it, which programs it may start and which connections it may relay for others. In CVE-2026-89103, the gateway enables its default list with high privileges, allowing an external attacker to be treated as one of the system's own application servers. That attacker could then take unauthorized actions in the application environment.

The researchers who found the flaw call it PROXYGATE. They say exposure depends on the gateway's proxy list, prxyinfo, or on a profile parameter where that list is missing, not on the secinfo and reginfo lists that most hardening guidance covers. Where the proxy settings allow it, crafted requests make the gateway treat an outside attacker as one of its own application servers, and it could then run operating system commands for the attacker as <sid>adm.

The flaw affects any system that runs a gateway, i...