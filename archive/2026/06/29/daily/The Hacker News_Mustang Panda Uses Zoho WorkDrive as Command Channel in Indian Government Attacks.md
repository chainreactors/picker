---
title: Mustang Panda Uses Zoho WorkDrive as Command Channel in Indian Government Attacks
url: https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html
source: The Hacker News
date: 2026-06-29
fetch_date: 2026-06-30T06:10:13.020755
---

# Mustang Panda Uses Zoho WorkDrive as Command Channel in Indian Government Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Mustang Panda Uses Zoho WorkDrive as Command Channel in Indian Government Attacks](https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html)

**Ravie Lakshmanan**Jun 29, 2026Threat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4479X60pqma2HNkNzrVQuQlGImd-48w4eYTTW-wylTLfK7XfLPtmNOMi79oy48LNiFg-4a_vqF378ZobR2Dy6VTO38VxbsFc_l8xQypwe-V43txSB7f73JS142E4uBXjrLKx0lcS-UOUMZ45kLeYgaqCjg2Je2TElLosoBvARIQpzam5q3ckk5CVXsoAF/s1700-e365/india-china.jpg)

The China-aligned espionage group [Mustang Panda](https://attack.mitre.org/groups/G0129/) is running two campaigns against the Indian government and hydropower targets, deploying new malware and turning a legitimate cloud service into its command channel.

[Acronis Threat Research Unit](https://www.acronis.com/en/tru/posts/mustang-panda-targets-indias-government-and-energy-sectors/) found active compromises inside Indian government networks, including machines used by senior administrative staff, and worked with [CERT-In](https://www.cert-in.org.in/) on notification and cleanup.

The malware abuses [Zoho WorkDrive](https://www.zoho.com/workdrive/), a cloud storage platform common in India's government sector, to pass commands and exfiltrate data. That is the whole idea: the traffic looks like ordinary cloud activity, so it hides inside the network it is stealing from.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Acronis names three new tools.

* **SHARDLOADER** is a loader that runs by sideloading a malicious DLL through a legitimately signed binary, a Solid PDF Creator executable in one campaign, and a Citrix Receiver binary in the other. It deploys one of two implants.
* **MINIRECON** is a reworked variant of the Toneshell backdoor [documented by IBM X-Force](https://www.ibm.com/think/x-force/hive0154-drops-updated-toneshell-backdoor), now beaconing over a WebSocket connection on HTTPS.
* **ZOHOMURK** is the novel piece: it carries hardcoded Zoho OAuth credentials and uses them to run an attacker-controlled WorkDrive account as a dead drop, reading commands from an inbox folder and writing stolen output to an outbox.

Both campaigns arrive as ZIP archives with the malicious DLL marked hidden. Acronis believes they were delivered by spear-phishing. The lures fit the targets: one themed around a hydropower cooperation proposal, the other around a memorandum of understanding between Indian and Taiwanese institutions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQmk98KFrFYERbtI3uXGfmrEPyCrJgHUtublqZJ0UaP7Wilvi1jw5pk3wluzz-2n0wk0fqXsaZULjjKOb4NjyUQ8NhnMQUTMp5rU_dHZue4hNSV3Ue-kCswz6-SiDmF4p8A1oDf09VgzcqL21U25ZDS-i-z67gOjgyV16s6r0soA5TBZgZeM2jSevlkDMG/s1700-e365/camp.png)

Per Acronis, the goal is intelligence on India's hydropower plans and its defense ties with Taiwan. Acronis attributes the activity to Mustang Panda with high confidence.

The report includes the reused Solid PDF Creator sideloading chain, code overlap with Toneshell, command servers sitting in the same network block as infrastructure IBM X-Force tied to the group, and a recurring typo, RunOnece, carried across multiple implants.

Operational security was thin. Hardcoded tokens, plaintext identifiers, and reused infrastructure all helped analysts pin it down. Active beaconing ran from June 12 to June 22, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

This continues a steady push against Indian targets. In April, Acronis tied the group's [LOTUSLITE backdoor](https://thehackernews.com/2026/04/mustang-pandas-new-lotuslite-variant.html) to attacks on India's banking sector and South Korean policy circles, also staged through a legitimate cloud service. The broader China-linked interest in India's power sector goes back further: the 2021 [RedEcho campaign](https://www.recordedfuture.com/research/redecho-targeting-indian-power-sector) [targeted the country's electricity grid](https://thehackernews.com/2021/03/chinese-hackers-targeted-indias-power.html) with ShadowPad.

There is no patch to apply. The defense is catching the delivery and the cloud abuse. Acronis published indicators and hunting tips, including the persistence Run keys, a scheduled task named SolidPDFPcl2Bmp, the C2 domain couldinstallup[.]com, and the Zoho user agents that turn up on non-browser processes.

Government and energy organizations, especially those tied to cross-border deals likely to interest Beijing, should watch for geopolitical lures and sideloading from signed binaries. And flag any endpoint process calling cloud APIs that it has no reason to touch.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [DLL Sideloading](https://thehackernews.com/search/label/DLL%20Sideloading), [Malware](https://thehackernews.com/search/label/Malware), [Mustang Panda](https://thehackernews.com/search/label/Mustang%20Panda), [Spear Phishing](https://thehackernews.com/searc...