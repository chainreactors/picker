---
title: Fortinet Issues Patches for 40 Flaws Affecting FortiWeb, FortiOS, FortiNAC, and FortiProxy
url: https://thehackernews.com/2023/02/fortinet-issues-patches-for-40-flaws.html
source: The Hacker News
date: 2023-02-20
fetch_date: 2025-10-04T07:34:29.797995
---

# Fortinet Issues Patches for 40 Flaws Affecting FortiWeb, FortiOS, FortiNAC, and FortiProxy

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

# [Fortinet Issues Patches for 40 Flaws Affecting FortiWeb, FortiOS, FortiNAC, and FortiProxy](https://thehackernews.com/2023/02/fortinet-issues-patches-for-40-flaws.html)

**Feb 19, 2023**Ravie LakshmananNetwork Security / Firewall

[![Fortinet](data:image/png;base64... "Fortinet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6k4J3SVc4t6-_mwgAsuml14Tbzq3jCnJrPd7QcLrCBsmk9DEu2x7DNq8bLgl-xcbA9oRpGC5RcY0xLlO6CkPp8YWN-MRhTF_ml10B_XAejPe5venB4OwgRYMA213vBEyr2DU8lKN9cfpxyH190G4Eg8UJtgA5rrd_KY4dBiOwKRhfhxT8idWPlP0Z/s790-rw-e365/fortnet.png)

Fortinet has released security updates to [address 40 vulnerabilities](https://www.fortiguard.com/psirt?date=02-2023) in its software lineup, including FortiWeb, FortiOS, FortiNAC, and FortiProxy, among others.

Two of the 40 flaws are rated Critical, 15 are rated High, 22 are rated Medium, and one is rated Low in severity.

Top of the list is a severe bug residing in the FortiNAC network access control solution (CVE-2022-39952, CVSS score: 9.8) that could lead to arbitrary code execution.

"An external control of file name or path vulnerability [CWE-73] in FortiNAC web server may allow an unauthenticated attacker to perform arbitrary write on the system," Fortinet [said](https://www.fortiguard.com/psirt/FG-IR-22-300) in an advisory earlier this week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The products impacted by the vulnerability are as follows -

* FortiNAC version 9.4.0
* FortiNAC version 9.2.0 through 9.2.5
* FortiNAC version 9.1.0 through 9.1.7
* FortiNAC 8.8 all versions
* FortiNAC 8.7 all versions
* FortiNAC 8.6 all versions
* FortiNAC 8.5 all versions, and
* FortiNAC 8.3 all versions

Patches have been released in FortiNAC versions 7.2.0, 9.1.8, 9.1.8, and 9.1.8. Penetration testing firm Horizon3.ai [said](https://twitter.com/Horizon3Attack/status/1626692778062237713) it plans to release a proof-of-concept (PoC) code for the flaw "soon," making it imperative that users move quickly to apply the updates.

The second flaw of note is a set of stack-based buffer overflow in FortiWeb's proxy daemon ([CVE-2021-42756](https://www.fortiguard.com/psirt/FG-IR-21-186), CVSS score: 9.3) that could enable an unauthenticated remote attacker to achieve arbitrary code execution via specifically crafted HTTP requests.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

CVE-2021-42756 affects the below versions of FortiWeb, with fixes available in versions FortiWeb 6.0.8, 6.1.3, 6.2.7, 6.3.17, and 7.0.0 -

* FortiWeb versions 6.4 all versions
* FortiWeb versions 6.3.16 and below
* FortiWeb versions 6.2.6 and below
* FortiWeb versions 6.1.2 and below
* FortiWeb versions 6.0.7 and below, and
* FortiWeb versions 5.x all versions

Both the flaws were internally discovered and reported by its product security team, Fortinet said. Interestingly, CVE-2021-42756 also appears to have been identified in 2021 but not publicly disclosed until now.

## UPDATE: FortiNAC CVE-2022-39952 PoC Released

Horizon3.ai on February 21, 2023, [published](https://www.horizon3.ai/fortinet-fortinac-cve-2022-39952-deep-dive-and-iocs/) a deep-dive on a critical security flaw impacting FortiNAC that enables an unauthenticated attacker to write arbitrary files on the system and as a result obtain remote code execution in the context of the root user. The proof-of-concept (PoC) is available [here](https://github.com/horizon3ai/CVE-2022-39952).

[GreyNoise](https://twitter.com/GreyNoiseIO/status/1628440450183962627) and the [Shadowserver Foundation](https://twitter.com/Shadowserver/status/1628140029322362880) on February 22, 2023, [warned](https://twitter.com/Shadowserver/status/1628140029322362880) of active exploitation attempts from [multiple IP addresses](https://viz.greynoise.io/tag/fortinac-rce-attempt?days=10) that weaponize the Fortinet FortiNAC flaw, a day after the release of the PoC.

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

[Fortinet](https://thehackernews.com/search/label/Fortinet)[FortiOS](https://thehackernews.com/search/label/FortiOS)[FortiProxy](https://thehackernews.com/search/label/FortiProxy)[FortiWeb](https://thehackernews.com/search/label/FortiWeb)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... ...