---
title: Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root
url: https://thehackernews.com/2026/09/critical-check-point-management-server.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:38.470775
---

# Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root

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

# [Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html)

**Swati Khandelwal**Sep 17, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuFSb4LQQ7e_Iz1RS0JfQEDY9G9LcQZ23RM0h6ladr56GJ6nN3kPwVoZPpNVJUyJEBmLVEyMaIxytF2XqyQs8fGjIdd_ymPjwaZA8Q8R7JiXC-srMFj0_YBd-a94juv46HZm4ie72j7PTj45veyTgOBaeuN53HvktSH3JTgasvV_Mo-RwjsTPnRLlHFVk/s1700-nu-rw-lo-l85-e365/cp-main.jpg)

A critical vulnerability in Check Point's Security Management and Log Servers could allow an attacker without login credentials to run code as root on those servers over the network.

The Security Management Server is the system that controls firewall policy and administrator access. Check Point has released a fix through its LivePatch update channel and says it has no indication that the flaw has been exploited.

Check Point told The Hacker News that the vulnerable path runs only through the Trusted Clients setting, which controls which hosts may connect to the management server through SmartConsole.

The flaw, tracked as **CVE-2026-91843** and rated 9.8 out of 10 on the CVSS scale by Check Point, is a stack overflow in the login process, which handles requests before a user is authenticated. Internet scanning company Censys said the overflow is triggered by a login request that carries a very long username.

Check Point said in a notice on its [CheckMates community](https://community.checkpoint.com/t5/General-Topics/Important-Notification-Action-required-Critical-Security-Update/m-p/282409) on September 16, 2026, that customers with automatic updates enabled are already protected, and that everyone else should apply the LivePatch fix described in advisory [sk1000155](https://support.checkpoint.com/results/sk/sk1000155). It urged customers to take immediate action because of the flaw's severity and potential impact.

"At this time, there is no indication that this vulnerability has been exploited in the wild," the notice said. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) recorded exploitation as "none" in its assessment attached to the [CVE record](https://www.cve.org/CVERecord?id=CVE-2026-91843) on September 17.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The flaw was not in CISA's Known Exploited Vulnerabilities catalog as of the catalog's September 16 release, which The Hacker News checked on September 17. Censys said no public proof-of-concept exploit existed as of September 16. **Aviv Abramovich**, vice president of product management for network security at Check Point, told The Hacker News that the company had not received any reports of exploitation.

### Affected Versions

Check Point's CVE record lists the following branches as affected, by Jumbo Hotfix Take, the numbered level of the update package that collects the fixes for a release.

A server on a listed branch at the listed Take or an older one is affected.

* R82.10 with Jumbo Hotfix Take 44 or below
* R82 with Jumbo Hotfix Take 126 or below
* R81.20 with Jumbo Hotfix Take 166 or below
* R81.10 with Jumbo Hotfix Take 190 or below, and R81, R80.40, R80.30, R80.20, R80.10 and R80, all of which are end of support

The record does not list R82.20, but Abramovich said R82.20 is also vulnerable. Censys said in its [advisory](https://censys.com/advisory/cve-2026-91843/) that every R82.20 build is affected and that no Jumbo Hotfix yet protects that branch.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiec_JG9HhUiWjcgnKnEgXcJFZYF4Nkk7whhgmxfKT1r13snRZuBcNEkRGvHXGKef3B1HqTWMmx7oB85emQTHFTDY2UVF9DN5rdqwerBE-w5xGWRkDss84c2gtP_KREYKa_IrpCq9p85G3VRWO48k5hjJTAA_JiwPF1FXP9Qj1E04oA1kaQgrYh6RtKDcU/s1700-nu-rw-lo-l85-e365/cen.jpg)

Standalone deployments, which run management and gateway on one system, Log Servers and Multi-Domain servers are also vulnerable, Abramovich said. An [alert from NHS England Digital](https://digital.nhs.uk/cyber-alerts/2026/cc-4854), citing sk1000155, says the hosted Smart-1 Cloud service is not affected because the fix is already in place there.

The CVE record marks R81.10 and the older branches as end-of-support. Check Point has a fix ready for those out-of-support versions, Abramovich said, and customers who need it should log a ticket with Check Point support.

### What Administrators Should Do

1. Apply the LivePatch fix described in sk1000155 to every Security Management Server and Log Server.
2. If automatic updates are enabled, confirm the fix has been installed rather than assume it. The cplp list command shows which LivePatches are installed and their status.
3. Whether or not the fix is installed, check that management Trusted Clients access is limited to known, trusted hosts and is not set to any IP address, and do not expose management access directly to the internet.

"Automatic updates" means the setting described in sk175504, according to Check Point's [hardening guide](https://sc1.checkpoint.com/documents/Check_Point_Gateway_and_Management_Hardening/CP_Check_Point_Gateway_and_Management_Hardening.pdf). It is the checkbox in SmartConsole, under Global Properties and Data Access Control, labeled "Automatically download and install Software Blade Contracts, security updates, and other important data (highly recommended)," followed by the installation of the Access Control policy. LivePatch is the channel Check Point uses to push urgent security fixes to systems where that option is turned on.

Delivery is not always immediate. When Check Point pushed fixes for [two VPN certificate flaws](https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html) last week, several customers wrote in its community that the automatic package had not reached their systems on the day of the announcement, and a Check Point community ...