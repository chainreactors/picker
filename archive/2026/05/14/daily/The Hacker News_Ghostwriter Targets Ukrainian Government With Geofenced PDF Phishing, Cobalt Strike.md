---
title: Ghostwriter Targets Ukrainian Government With Geofenced PDF Phishing, Cobalt Strike
url: https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html
source: The Hacker News
date: 2026-05-14
fetch_date: 2026-05-15T05:53:27.900040
---

# Ghostwriter Targets Ukrainian Government With Geofenced PDF Phishing, Cobalt Strike

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Ghostwriter Targets Ukrainian Government With Geofenced PDF Phishing, Cobalt Strike](https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html)

**Ravie Lakshmanan**May 14, 2026Hacktivism / Data Theft

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEld5BcqD9rYWVjx7o_XlV5pN_9djvilow0iIYP-LlFEzGReX8fTPZ0gKi9zMGVLTT8qddHu5FyBMaZpQroEzYFpsoPWf96hD7JeTdqsROemmavXW2pDxNwc9kjvpJdhahmXA5Ng88tN1lyO5rqzC3K6JNwPFPWBo7OzSsaiQIN8JJsXvMrGhewMfzpouF/s1700-e365/uk.jpg)

The Belarus-aligned threat group known as **[Ghostwriter](https://thehackernews.com/2025/09/noisy-bear-targets-kazakhstan-energy.html)** has been attributed to a fresh set of attacks targeting governmental organizations in Ukraine.

Active since at least 2016, Ghostwriter has been linked to both cyber espionage and influence operations targeting neighboring countries, particularly Ukraine. It's also tracked under the monikers FrostyNeighbor, PUSHCHA, Storm-0257, TA445, UAC‑0057, Umbral Bison (formerly RepeatingUmbra), UNC1151, and White Lynx.

"FrostyNeighbor has been running continual cyber operations, changing and updating its toolset regularly, updating its compromise chain and methods to evade detection – targeting victims located in Eastern Europe," ESET [said](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/) in a report shared with The Hacker News.

Previous attacks mounted by the hacking crew have leveraged a malware family known as [PicassoLoader](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html), which then acts as a conduit for Cobalt Strike Beacon and njRAT. In late 2023, the threat actor was also [observed](https://thehackernews.com/2023/11/experts-uncover-darkcasino-new-emerging.html) weaponizing a vulnerability in WinRAR ([CVE-2023-38831](https://thehackernews.com/2023/09/ukraines-cert-thwarts-apt28s.html), CVSS score: 7.8) to deploy PicassoLoader and Cobalt Strike.

As recently as last year, Polish entities were at the receiving end of a phishing campaign orchestrated by Ghostwriter that [exploited](https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q2-2025-q3-2025/) a cross-site flaw in Roundcube ([CVE-2024-42009](https://thehackernews.com/2025/06/cisa-adds-erlang-ssh-and-roundcube.html), CVSS score: 9.3) to run malicious JavaScript responsible for capturing email login credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

In at least some cases, the threat actors are said to have leveraged the harvested credentials to analyze mailbox contents, download the contact list, and abuse the compromised account to propagate more phishing messages, per a [report](https://cert.pl/en/posts/2025/06/unc1151-campaign-roundcube/) from CERT Polska in June 2025. Towards the end of 2025, the group also [began to incorporate](https://strikeready.com/blog/captch-ya-if-you-can/) an anti-analysis technique where lure documents relied on dynamic CAPTCHA checks to trigger the attack chain.

"FrostyNeighbor remains a persistent and adaptive threat actor, demonstrating a high level of operational maturity with the use of diverse lure documents, evolving lure and downloader variants, and new delivery mechanisms," ESET researcher Damien Schaeffer said. "This newest compromise chain that we detected is a continuation of the group's willingness to update and renew its arsenal, trying to evade detection to compromise its targets."

The latest set of activities, observed since March 2026, involves using links in malicious PDFs sent via spear-phishing attachments to target government entities in Ukraine, ultimately resulting in the deployment of a JavaScript version of PicassoLoader to drop Cobalt Strike. The PDF decoy documents have been found to impersonate the Ukrainian telecommunications company Ukrtelecom.

The infection sequence incorporates a geofencing check, serving a benign PDF file to victims whose IP address does not correspond to Ukraine. The embedded link in the PDF document is used to deliver a RAR archive containing a JavaScript payload that displays a lure document to keep up the ruse, while simultaneously launching PicassoLoader in the background.

The downloader is also designed to profile and fingerprint the compromised host, based on which the operators may manually decide to send a third-stage JavaScript dropper for Cobalt Strike Beacon. The system fingerprint is transmitted to attacker-controlled infrastructure every 10 minutes, allowing the threat actor to assess whether the victim is of interest.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkqrpTHue2yirSzSVSa9Io2fzK0VSX6lVS4TZolFtqDIpY0VOw4AMlxlRULLZvjuFTD5R7G6G8ilb93YUB_kT5X4A07JgW7ct7XZFdeDXDCW5Nu3eXDjg5W3kXlf_miVqk9Du5CqEJVxLto8qSoDEdZZGWSuXPmiEDJjMIHJznT5H7EmEyT-RAwmHzI8oI/s1700-e365/eset-1.png)

The activity primarily appears to center around military, defense sector, and governmental organizations in Ukraine, whereas the victimology in Poland and Lithuania is much broader, targeting industrial and manufacturing, healthcare and pharmaceuticals, logistics, and government sectors.

"FrostyNeighbor remains a persistent and adaptive threat actor, demonstrating a high level of operational maturity with the use of diverse lure documents, evolving lure and downloader variants, and new delivery mechanisms," ESET said. "The payload is only delivered after server-side victim validation, combining automated checks of the requesting user agent and IP address with the manual validation by the operators."

### Gamaredon Delivers GammaDrop and GammaLoad in Ukraine Attacks

The disclosure comes as the Russia-affiliated [Gamaredon](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html) hacking group has been tied to a spear-phishing campaign targeting Ukrainian state institutions since September 2025, with an aim to deliver [Gam...