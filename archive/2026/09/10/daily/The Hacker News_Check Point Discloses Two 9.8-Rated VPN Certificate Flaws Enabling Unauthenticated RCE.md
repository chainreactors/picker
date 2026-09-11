---
title: Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE
url: https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html
source: The Hacker News
date: 2026-09-10
fetch_date: 2026-09-11T06:53:19.873638
---

# Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE

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

# [Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE](https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html)

**Swati Khandelwal**Sep 10, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyc0Kqar7_6N4y9ymGxw8ukQCQbqQ_pGCfnoXYMBZoNZK1w3ljkO26S_rhVhJaIVcx8rcEK95njKyaYj5g63VByKh8ncf_s84nUBWoyEbWZH6uaLYjnu5fNt_TC9wz-r6P_RTJgZ83Z5wmurzSb9_lHVfV1t9STts4WCZr18AH-3XRHTn5pj15uURIM-0/s1700-nu-rw-lo-l85-e365/checkpoint.jpg)

Check Point has patched two critical vulnerabilities in the way its firewall and management products handle VPN certificates. The company says both could allow an unauthenticated remote attacker to run code, but only "under specific conditions" that it has not described.

One flaw affects Check Point's Security Gateways, its firewall appliances. The other affects those gateways and the Security Management Server, the console used to configure them.

Check Point disclosed the flaws on September 9 in a [notice to its customer community](https://community.checkpoint.com/t5/General-Topics/Action-Required-Critical-Security-Advisory-VPN-Vulnerabilities/td-p/281995), and began delivering fixes the same day. The company says it found both itself and has no indication that either has been used in an attack.

The first flaw, [CVE-2026-85102](https://support.checkpoint.com/results/sk/sk1000117), is a failure to properly validate certificate trust during VPN negotiation. Its CVE record says an unauthenticated remote attacker may be able to run code on the Security Gateway.

The second, [CVE-2026-85103](https://support.checkpoint.com/results/sk/sk1000118), is a heap-based buffer overflow that happens while the product decodes the ASN.1 structure of a VPN certificate. Its record says an unauthenticated remote attacker may be able to run code on Quantum Security Management and Quantum Security Gateway systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Both records carry a CVSS score of 9.8. Check Point assigned the identifiers and the scores itself.

The two records give the same affected list:

* R82.10 with Jumbo Hotfix Take 43 or below
* R82 with Jumbo Hotfix Take 125 or below
* R81.20 with Jumbo Hotfix Take 165 or below

Those are the versions the records mark as affected, not the versions that contain the fix. The list covers three Quantum branches and gives no version information for anything else.

An [advisory from the Canadian Center for Cyber Security](https://www.cyber.gc.ca/en/alerts-advisories/check-point-security-advisory-av26-902), published the same evening, lists a broader set of products but no versions at all. It lists Security Gateway, Security Management Server, and Spark Firewall, Check Point's small-business line.

Spark appears twice, once for deployments using Site-to-Site or Remote Access VPN and once without that condition.

In the same community thread, a Check Point staff member was asked whether gateways with the VPN software blade turned off are affected by CVE-2026-85103. The staff member replied that the issue is about certificate processing, so it could, in theory, be triggered in an environment without a VPN but with VPN certificates present.

Check Point gave customers two routes to the fix.

The first is Check Point Live Patch. The company says customers using it are protected automatically as the rollout begins, which started on September 9. A Check Point employee said in the thread that it can be installed on top of any Jumbo Hotfix level in R81.20, R82.00 and R82.10, and named only those three versions.

The second is the Jumbo Hotfix. Check Point told customers to install the latest one for their deployed version once it became available.

### If You Cannot Patch Yet

Two customers said in the thread that they are running R81.10 and will not be moving off it for weeks. One of them said no Jumbo Hotfix and no Live Patch was available for that branch, leaving mitigation as the only option.

The same customer described the advisory's mitigation as turning off implied rules for VPN, called it too vague to act on, and asked which configuration lines to comment out. The other asked how to apply the mitigation without affecting remote users. Neither question had an answer in the thread.

Several customers also said the automatic rollout had not reached them. Five separate accounts reported gateways were still on Take 18 or Take 17 of the urgent security update package on the day of the announcement; one of them posted an update log showing Take 18 installed on September 1 and nothing since.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

Several customers reported that download links in the two advisories did not work for them, and a Check Point staff member replied that the links had been checked and were working. One customer said afterward that the advisory links still failed in two browsers, while the link in the [Live Patch article](https://support.checkpoint.com/results/sk/sk185114) worked.

In June and July, Check Point patched critical flaws in these products that it said were already being exploited when it announced them. June's was [CVE-2026-50751](https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html), an authentication bypass in Remote Access VPN and Mobile Access certificate validation. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added it to its Known Exploited Vulnerabilities catalog on June 8.

July's was CVE-2026-16232, a SmartConsole authentication bypass, which CISA added to the same catalog on the day it was disclosed. It was [one of three flaws Check Point patched that month](https://thehackernews.com/2026/07/check-point-patches-exploited.html), two of which affected the Security Management Server, the same component CVE-2026-85103 reaches.

Check Po...