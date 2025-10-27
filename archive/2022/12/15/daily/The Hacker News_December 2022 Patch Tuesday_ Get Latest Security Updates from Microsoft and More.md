---
title: December 2022 Patch Tuesday: Get Latest Security Updates from Microsoft and More
url: https://thehackernews.com/2022/12/december-2022-patch-tuesday-get-latest.html
source: The Hacker News
date: 2022-12-15
fetch_date: 2025-10-04T01:34:48.669667
---

# December 2022 Patch Tuesday: Get Latest Security Updates from Microsoft and More

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

# [December 2022 Patch Tuesday: Get Latest Security Updates from Microsoft and More](https://thehackernews.com/2022/12/december-2022-patch-tuesday-get-latest.html)

**Dec 14, 2022**Ravie LakshmananPatch Management / Vulnerability

[![Patch Tuesday Security Updates](data:image/png;base64... "Patch Tuesday Security Updates")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRbgwLqZwKl8WbC_KGx4gxaKO_xw8xLb0wcK55QizXmNg8y6iC4DH_Mu-WSdIdlHvzlEyNkMYzMj_rb-_Ff_Mz_Na0blyUjLDxvg_8pTNCGF5b7w2WrdmJjE_S4OiO12SQfDRB2vTTwHNAGk5dfTtJw5hn9KgZxBQzz-mHJ-AfLhccacvrp9tYFcwm/s790-rw-e365/patch-tuesday.png)

Tech giant Microsoft released its last set of monthly security updates for 2022 with [fixes for 49 vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2022-Dec) across its software products.

Of the 49 bugs, six are rated Critical, 40 are rated Important, and three are rated Moderate in severity. The updates are in addition to [24 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) that have been addressed in the Chromium-based Edge browser since the start of the month.

December's Patch Tuesday plugs two zero-day vulnerabilities, one that's actively exploited and another issue that's listed as publicly disclosed at the time of release.

The former relates to [CVE-2022-44698](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-44698) (CVSS score: 5.4), one of the [three security bypass issues](https://twitter.com/wdormann/status/1582466468968792064) in Windows SmartScreen that could be exploited by a malicious actor to evade mark of the web (MotW) protections.

It's worth noting that this issue, in conjunction with [CVE-2022-41091](https://thehackernews.com/2022/11/install-latest-windows-update-asap.html) (CVSS score: 5.4), has been observed being exploited by Magniber ransomware actors to deliver rogue JavaScript files within ZIP archives.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"It allows attackers to craft documents that won't get tagged with Microsoft's 'Mark of the Web' despite being downloaded from untrusted sites," Rapid7's Greg Wiseman said. "This means no Protected View for Microsoft Office documents, making it easier to get users to do sketchy things like execute malicious macros."

Publicly disclosed, but not seen actively exploited, is [CVE-2022-44710](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44710) (CVSS score: 7.8), an elevation of privilege flaw in DirectX Graphics Kernel that could enable an adversary to gain SYSTEM privileges.

"Successful exploitation of this vulnerability requires an attacker to win a race condition," Microsoft pointed out in an advisory.

Also patched by Microsoft are multiple remote code execution bugs in Microsoft Dynamics NAV, Microsoft SharePoint Server, PowerShell, Windows Secure Socket Tunneling Protocol (SSTP), .NET Framework, Contacts, and Terminal.

Furthermore, the update also resolves 11 remote code execution vulnerabilities in Microsoft Office Graphics, OneNote, and Visio, all of which are rated 7.8 in the CVSS scoring system.

Two of the 19 elevation of privilege flaws remediated this month comprises fixes for the Windows Print Spooler component ([CVE-2022-44678](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-44678) and [CVE-2022-44681](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-44681), CVSS scores: 7.8), continuing a steady stream of patches released by the company over the past year.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Last but not least, Microsoft has assigned the "Exploitation More Likely" tag to the PowerShell remote code execution vulnerability ([CVE-2022-41076](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41076), CVSS score: 8.5) and Windows Sysmon privilege escalation flaw ([CVE-2022-44704](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-44704), CVSS score: 7.8), making it essential that users apply updates to mitigate potential threats.

### Software Patches from Other Vendors

In addition to Microsoft, security updates have also been released by other vendors over the past two weeks to rectify several vulnerabilities, including —

* [Adobe](https://helpx.adobe.com/security/security-bulletin.html)
* [Android](https://source.android.com/docs/security/bulletin/2022-12-01)
* [Apple](https://thehackernews.com/2022/12/new-actively-exploited-zero-day.html)
* [Cisco](https://tools.cisco.com/security/center/publicationListing.x)
* [Citrix](https://thehackernews.com/2022/12/hackers-actively-exploiting-citrix-adc.html)
* [CODESYS](https://www.codesys.com/security/security-reports.html)
* [Dell](https://www.dell.com/support/security/)
* [F5](https://support.f5.com/csp/new-updated-articles)
* [Fortinet](https://www.fortiguard.com/psirt?date=12-2022)
* [GitLab](https://about.gitlab.com/releases/2022/11/30/security-release-gitlab-15-6-1-released/)
* [Google Chrome](https://chromereleases.googleblog.com/2022/12/stable-channel-update-for-desktop_13.html)
* [HP](https://support.hp.com/us-en/security-bulletins)
* [IBM](https://www.ibm.com/support/pages/bulletin/)
* [Intel](https://www.intel.com/content/www/us/en/security-center/default.html)
* [Lenovo](https://support.lenovo.com/us/en/product_security/ps500001-lenovo-product-security-advisories)
* Linux distributions [Debian](https://www.debian.org/security/2022/), [Oracle Linux](https://linux.oracle.com/ords/f?p=105:21::::RP::), [Red Hat](https://access.redhat.com/security/security-updates/#/security-advisories?q=&p=1&sort=portal_publication_date%20desc&rows=10&portal_advisory_type=Security%20Advisory&documentKind=PortalProduct), [SUSE](https://www.suse.com/support/update/), and [Ubuntu](https://ubuntu.com/security/notices)
* [MediaTek](https://corp.mediatek.com/product-security-bulletin/December-2022)
* [Mozilla Firefox, Firefox ESR, and Th...