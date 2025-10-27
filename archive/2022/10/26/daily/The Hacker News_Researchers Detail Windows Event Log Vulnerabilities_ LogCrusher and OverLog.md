---
title: Researchers Detail Windows Event Log Vulnerabilities: LogCrusher and OverLog
url: https://thehackernews.com/2022/10/researchers-detail-windows-event-log.html
source: The Hacker News
date: 2022-10-26
fetch_date: 2025-10-03T20:56:23.291322
---

# Researchers Detail Windows Event Log Vulnerabilities: LogCrusher and OverLog

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

# [Researchers Detail Windows Event Log Vulnerabilities: LogCrusher and OverLog](https://thehackernews.com/2022/10/researchers-detail-windows-event-log.html)

**Oct 25, 2022**Ravie Lakshmanan

[![LogCrusher and OverLog](data:image/png;base64... "LogCrusher and OverLog")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgww6d7xW8UptkJ66Pr748PaJHvgXZtOBjpGva4ZFhItjOJflWN2m4cPL1gnI6LW42SxhFXdrvRYQCYxDOLHfVlapOFLPHPULrN_OHWsyXWHpgQ6W2aldWBHEhDe-k-dqULo5QH7NMNPHqhSkcUMrQZIGzfxBXNEnkcv7YWiS7fIhhY3P_qd7p_wGkc/s790-rw-e365/event.jpg)

Cybersecurity researchers have disclosed details about a pair of vulnerabilities in Microsoft Windows, one of which could be exploited to result in a denial-of-service (DoS).

The exploits, dubbed **LogCrusher** and **OverLog** by Varonis, take aim at the EventLog Remoting Protocol ([MS-EVEN](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even/55b13664-f739-4e4e-bd8d-04eeda59d09f)), which enables remote access to event logs.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While the former allows "any domain user to remotely crash the Event Log application of any Windows machine," OverLog causes a DoS by "filling the hard drive space of any Windows machine on the domain," Dolev Taler [said](https://www.varonis.com/blog/the-logging-dead-two-windows-event-log-vulnerabilities) in a report shared with The Hacker News.

OverLog has been assigned the CVE identifier CVE-2022-37981 (CVSS score: 4.3) and was addressed by Microsoft as part of its [October Patch Tuesday](https://thehackernews.com/2022/10/microsoft-patch-tuesday-fixes-new.html) updates. LogCrusher, however, remains unresolved.

[![Windows Event Log Vulnerabilities](data:image/png;base64... "Windows Event Log Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgB67qzpfW-YI5yIy4i-LtGhmiOlAYMi6qqn0qEdqkjD9-Jm-xJ7OT2PNfn8T1dGjJboTX39VaXk-2INIEud9aBV6PNPmBZAAIvSeuNjQKpce8jO43dcO4jJpOlLiDQAmFVPgvJMneuP35Ud3iMUwra8UratLLnCUzLktTs3Nz4H03g5ZsFeKSPPX17/s790-rw-e365/demo1.gif)

"The performance can be interrupted and/or reduced, but the attacker cannot fully deny service," the tech giant said in an advisory for the flaw released earlier this month.

[![Windows Event Log Vulnerabilities](data:image/png;base64... "Windows Event Log Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCkY00aaCzABjapg2XrGydX-rVOVmj-YxFNIU3Es_QRw4vo1H2mY34ZZxGQmlV48If2ceNezSwxUJ8eFHA5DU_J7uLX_aQVqiJ5oxvrvJ53Bzwh5MBA9Mb7GcLMbmOgpGtX6Ja4I31Z_asxeYwlqccqzvSvYC4V7pwzQrRcrNEX76F-gVJ_8R9KyRq/s790-rw-e365/demo2.gif)

The issues, according to Varonis, bank on the fact that an attacker can obtain a handle to the legacy Internet Explorer log, effectively setting the stage for attacks that leverage the handle to crash the Event Log on the victim machine and even induce a DoS condition.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is achieved by combining it with another flaw in a log backup function ([BackupEventLogW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-backupeventlogw)) to repeatedly backup arbitrary logs to a writable folder on the targeted host until the hard drive gets filled.

Microsoft has since remediated the OverLog flaw by restricting access to the Internet Explorer Event Log to local administrators, thereby reducing the potential for misuse.

"While this addresses this particular set of Internet Explorer Event Log exploits, there remains potential for other user-accessible application Event Logs to be similarly leveraged for attacks," Taler said.

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

[Microsoft](https://thehackernews.com/search/label/Microsoft)[Microsoft Windows](https://thehackernews.com/search/label/Microsoft%20Windows)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX...