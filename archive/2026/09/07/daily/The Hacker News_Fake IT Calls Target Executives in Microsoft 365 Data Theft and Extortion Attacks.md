---
title: Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks
url: https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
source: The Hacker News
date: 2026-09-07
fetch_date: 2026-09-08T06:42:26.486831
---

# Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks

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

# [Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks](https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html)

**Ravie Lakshmanan**Sep 07, 2026Phishing / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg-Zo4zgxCrVcz6-00WV2qAPHSD-av2Ed5hgRmR-2vUzkr9jVeph0NNb6gGsQfwSkFyuRfRcSsaISSpfysl_Xx5F48IM7HdBpO4F3CaVuLhk1v0a4vcH5xK_bxX6BxIjkfAjhDaNGcLG7_R9IcTjVGlFcW7y1ZV64imACHi9528LOjH1Flhk-cy9LFgrMv/s1700-nu-rw-lo-l85-e365/phish-ms.jpg)

Threat hunters have disclosed details of a widespread data theft and extortion threat cluster that's targeting Microsoft 365 and other software-as-a-service (SaaS) offerings through information technology (IT) help desk vishing, adversary-in-the-middle (AitM) token theft, and residential-proxy sign-ins.

The activity, which mainly singles out directors, vice presidents, and other executive staff, is being [tracked](https://github.com/rtkwlf/wolf-tools/tree/main/pack_alerts/202609-cloud-data-theft-extortion-vishing-proxies) by Arctic Wolf under the moniker **PREY-0058**, adding it shares significant tradecraft similarities with a data extortion group that Google-owned Mandiant calls [UNC6671](https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html).

It also said that the data extortion threat actor known as Cinder likely represents yet another rebrand or a possible continuation of Pink operations, citing overlaps between organizations listed on the Cinder leak site and those connected to Pink.

It's worth noting that the ever-evolving labels do not correspond to a single proven actor identity, but rather an amorphous set of affiliates, splinter crews, or groups using the same underlying phishing infrastructure, as indicated by Google early last month.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Attack chains begin with the threat actors impersonating internal IT or help desk personnel in phone calls and directing prospective targets to an authentication-themed URL that follows the pattern: <victim organization>.<lure domain>. Some of the lure domains flagged by Arctic Wolf are listed below -

* assignpasskey[.]com
* mfaregister[.]com
* nowsso[.]com
* oskeysetup[.]com
* oursso[.]com
* passkey-mfa[.]com
* passkeydeploy[.]com
* registermymfa[.]com
* setpasskey[.]com

The attacks lead to an operator-controlled AitM Microsoft 365 login flow that's designed to harvest credentials and multi-factor authentication (MFA) approvals to obtain access to authenticated session tokens. The captured tokens are subsequently leveraged in session replay attacks originating from proxy infrastructure, such as NodeMaven, and from IP addresses that resolve to the same geographical location and ASN as the victim.

"Initial sign-in activity involves applications such as 'My Signins,' 'My Profile,' 'My Apps,' which reveal account details and the applications available to the victim," researchers Steven Campbell, Trevor Daher, Stefan Hostetler, and Joshua Riccio said in an analysis.

"After initial access, the threat actors perform discovery techniques against SharePoint and Entra ID. SharePoint discovery includes SearchQueryPerformed events with contentclass:STS\_Site, contentclass:STS\_Web, and wildcard searches using indexdocid for pagination."

In the final step, the threat actors perform en masse collection and exfiltration from SharePoint, OneDrive, Exchange, and Box, after which extortion demands are sent to victims.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

What's notable about PREY-0058 is the absence of endpoint malware deployment or network-based lateral movement. Further analysis of subdomains across the lure infrastructure has uncovered hundreds of entries impersonating real companies.

The targets are spread across the U.S., primarily in construction and engineering, healthcare and pharmaceuticals, real estate and property management, finance, and professional services.

To counter the threat, organizations are advised to implement Conditional Access policies, deploy phishing-resistant MFA, restrict the scope of data that users have access to in SharePoint, and educate employees and help desk staff about vishing risks.

"Defenders can disrupt this activity by detecting anomalous residential-proxy token replay, SharePoint discovery and bulk access, mailbox harvesting, and newly registered authentication-themed lure infrastructure," Arctic Wolf said.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cybercrime](https://thehackernews.com/search/label/Cybercrime), [data breach](https://thehackernews.com/search/label/data%20breach), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Phishing](https://thehackernews.com/search/label/Phishing)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Exploit Critical Langflow and Rails Flaws in Credential...