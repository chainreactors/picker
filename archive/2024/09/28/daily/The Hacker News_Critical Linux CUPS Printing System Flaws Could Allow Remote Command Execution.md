---
title: Critical Linux CUPS Printing System Flaws Could Allow Remote Command Execution
url: https://thehackernews.com/2024/09/critical-linux-cups-printing-system.html
source: The Hacker News
date: 2024-09-28
fetch_date: 2025-10-06T18:38:51.704797
---

# Critical Linux CUPS Printing System Flaws Could Allow Remote Command Execution

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

# [Critical Linux CUPS Printing System Flaws Could Allow Remote Command Execution](https://thehackernews.com/2024/09/critical-linux-cups-printing-system.html)

**Sep 27, 2024**Ravie LakshmananLinux / Vulnerability

[![Linux CUPS Printing System](data:image/png;base64... "Linux CUPS Printing System")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfw61OcqJmIxtfVOx_GGXRPn4z5_xvpDi3FhDM6NcPa915RqdOGjpFno7B7DKNRT6QiwIcWgWZg72sidA6r0tuqAsVfnBeLRZ3g0VC8yikw0sGEQLovz21BG4fBqfAc_e9TCZP47MFLloAreLHMsMnfl6P8HYW6g6UhkgGGI19AiBRnv7DWkvw0wc5RrKt/s790-rw-e365/linux-printer.png)

A new set of security vulnerabilities has been disclosed in the OpenPrinting Common Unix Printing System ([CUPS](https://github.com/OpenPrinting/cups)) on Linux systems that could permit remote command execution under certain conditions.

"A remote unauthenticated attacker can silently replace existing printers' (or install new ones) IPP urls with a malicious one, resulting in arbitrary command execution (on the computer) when a print job is started (from that computer)," security researcher Simone Margaritelli [said](https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/).

CUPS is a standards-based, open-source printing system for Linux and other Unix-like operating systems, including ArchLinux, Debian, Fedora, Red Hat Enterprise Linux (RHEL), ChromeOS, FreeBSD, NetBSD, OpenBSD, openSUSE, and SUSE Linux.

The list of [vulnerabilities](https://seclists.org/oss-sec/2024/q3/281) is as follows -

* **[CVE-2024-47176](https://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8)** - cups-browsed <= 2.0.1 binds on UDP INADDR\_ANY:631 trusting any packet from any source to trigger a Get-Printer-Attributes IPP request to an attacker-controlled URL
* **[CVE-2024-47076](https://github.com/OpenPrinting/libcupsfilters/security/advisories/GHSA-w63j-6g73-wmg5)** - libcupsfilters <= 2.1b1 cfGetPrinterAttributes5 does not validate or sanitize the IPP attributes returned from an IPP server, providing attacker-controlled data to the rest of the CUPS system
* **[CVE-2024-47175](https://github.com/OpenPrinting/libppd/security/advisories/GHSA-7xfx-47qg-grp6)** - libppd <= 2.1b1 ppdCreatePPDFromIPP2 does not validate or sanitize the IPP attributes when writing them to a temporary PPD file, allowing the injection of attacker-controlled data in the resulting PPD
* **[CVE-2024-47177](https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47)** - cups-filters <= 2.0.1 foomatic-rip allows arbitrary command execution via the FoomaticRIPCommandLine PPD parameter

A net consequence of these shortcomings is that they could be fashioned into an exploit chain that allows an attacker to create a malicious, fake printing device on a network-exposed Linux system running CUPS and trigger remote code execution upon sending a print job.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The issue arises due to improper handling of 'New Printer Available' announcements in the 'cups-browsed' component, combined with poor validation by 'cups' of the information provided by a malicious printing resource," network security company Ontinue [said](https://www.ontinue.com/resource/new-linux-rce-in-cups-printing-system/).

"The vulnerability stems from inadequate validation of network data, allowing attackers to get the vulnerable system to install a malicious printer driver, and then send a print job to that driver triggering execution of the malicious code. The malicious code is executed with the privileges of the lp user – not the superuser 'root.'"

RHEL, in an advisory, said all versions of the operating system are affected by the four flaws, but noted that they are not vulnerable in their default configuration. It tagged the issues as Important in severity, given that the real-world impact is likely to be low.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhdnycCpJzgw3OhKXzl9VUCGrV6_hCSAbcn1SxKG_Nn2wJV9vFY9RPmnf860_S0N-dY_c_Z5Vg5Cmq7PJg_G6nrTJsn1iJ05837Wpt7NT42a5m8KfSf17RD8n4oNBvvfowsLfN4H2iTYZDJyWlENvbkHACTSe-kfzVYK0fsaCsZ0_Sup3-Cy-hdBsMX1yN/s790-rw-e365/linux.png)

"By chaining this group of vulnerabilities together, an attacker could potentially achieve remote code execution which could then lead to theft of sensitive data and/or damage to critical production systems," it [said](https://www.redhat.com/en/blog/red-hat-response-openprinting-cups-vulnerabilities).

Cybersecurity firm Rapid7 [pointed out](https://www.rapid7.com/blog/post/2024/09/26/etr-multiple-vulnerabilities-in-common-unix-printing-system-cups/) that affected systems are exploitable, either from the public internet or across network segments, only if UDP port 631 is accessible and the vulnerable service is listening.

Palo Alto Networks has [disclosed](https://security.paloaltonetworks.com/CVE-2024-47076) that none of its products and cloud services contain the aforementioned CUPS-related software packages, and therefore are not impacted by the flaws.

Patches for the vulnerabilities are currently being developed and are expected to be released in the coming days. Until then, it's advisable to disable and remove the cups-browsed service if it's not necessary, and block or restrict traffic to UDP port 631.

"It looks like the embargoed Linux unauth RCE vulnerabilities that have been touted as doomsday for Linux systems, may only affect a subset of systems," Benjamin Harris, CEO of WatchTowr, said in a statement shared with The Hacker News.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Given this, while the vulnerabilities in terms of technical impact are serious, it is significantly less likely that desktop machines/workstations running CUPS are exposed to the Internet in the same manner or numbers that typical server editions of Linux would be."

Satnam Narang, senior staff research engineer at Tenable, said these...