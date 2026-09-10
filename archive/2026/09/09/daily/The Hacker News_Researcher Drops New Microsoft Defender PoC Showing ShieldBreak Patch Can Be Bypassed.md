---
title: Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed
url: https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
source: The Hacker News
date: 2026-09-09
fetch_date: 2026-09-10T06:52:42.032647
---

# Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed

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

# [Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed](https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html)

**Ravie Lakshmanan**Sep 09, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZtPq88H-iuD1vEn_DT-1UgFvWXy-P5eKMUm280xVsPt3_Dja1q22icfvF49OduVCGmazXmVmi51Oj58t-2H6JMA4e89X_-obRVRVORjeAZoQzNnw3Io6ad_LofQ1kfum9XeiHC9cijCgAiRL-RsRYjECDVPD_ZT3w61CFj1lkwe2sSZ_1_eSn6Oruh9MJ/s1700-nu-rw-lo-l85-e365/windows-poc.jpg)

The security researcher known as Chaotic Eclipse has dropped a proof-of-concept (PoC) for yet another zero-day in Microsoft Defender.

The vulnerability, codenamed **[ShieldCrash](https://github.com/MSNightmare/ShieldCrash)**, is assessed to be a patch bypass for CVE-2026-69414 (CVSS score: 7.8), also called [ShieldBreak](https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html), which the researcher reported last month.

"Microsoft has failed to properly patch ShieldBreak CVE-2026-69414," Chaotic Eclipse said. "Under specific conditions it is still possible to trigger the exact same problem that was caused by ShieldBreak. While Microsoft fixed several things to prevent re-exploiting the issue, they missed a spot where ShieldBreak can still be exploited."

The PoC demonstrates an arbitrary file read as SYSTEM with the latest version of Windows installed. All supported versions of the desktop operating system are said to be impacted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

The development comes days after Redmond shipped an update to the Microsoft Malware Protection Engine to plug CVE-2026-69414. The issue has been patched in Malware Protection Engine version 1.1.26080.3. It does not require any customer action and does not affect systems that have disabled Microsoft Defender.

"In response to a constantly changing threat landscape, Microsoft frequently updates malware definitions and the Microsoft Malware Protection Engine," the tech giant [said](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-69414). "In order to be effective in helping protect against new and prevalent threats, antimalware software must be kept up to date with these updates in a timely manner."

"For enterprise deployments as well as end users, the default configuration in Microsoft antimalware software helps ensure that malware definitions and the Microsoft Malware Protection Engine are kept up to date automatically. Product documentation also recommends that products are configured for automatic updating."

In recent weeks, Chaotic Eclipse has also [released](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html) PoC exploits for four vulnerabilities impacting CrowdStrike Falcon Sensor (FalconFlank), Kaspersky (HardBreacher), Avast Antivirus (PrettyPrague), and NVIDIA (GreenSection). Both HardBreacher and PrettyPrague have since been patched by the respective security vendors, while CrowdStrike told The Hacker News that it's investigating the report.

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

[endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows](https://thehackernews.com/search/label/Windows)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity](https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html)

[![The Hacker News](data:image/svg+xml;base64...)

Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests](https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More](https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html)

[![The Hacker News](data:image/svg+xml;base64...)

N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores](https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials](https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html)

[![The Hacker News](data:image/svg+xml;base64...)

Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code](https://thehackernews.com/2026/09/critical-vmware-workstation-and-fusion...