---
title: More_eggs MaaS Expands Operations with RevC2 Backdoor and Venom Loader
url: https://thehackernews.com/2024/12/moreeggs-maas-expands-operations-with.html
source: The Hacker News
date: 2024-12-07
fetch_date: 2025-10-06T19:59:31.885459
---

# More_eggs MaaS Expands Operations with RevC2 Backdoor and Venom Loader

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

# [More\_eggs MaaS Expands Operations with RevC2 Backdoor and Venom Loader](https://thehackernews.com/2024/12/moreeggs-maas-expands-operations-with.html)

**Dec 06, 2024**Ravie LakshmananMalware / Cybercrime

[![RevC2 Backdoor and Venom Loader](data:image/png;base64... "RevC2 Backdoor and Venom Loader")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiVqdu6jTCFeMHiye1NOKu0vzrHFHPoYyaUyNOvLoEjIXTmhyDbQoI9gLUhKbjrSkfHUCyzE353OshnBWb8DG6Axx_gUdHISTfrfaTUOEz2xlD2GdAvvxDqGjzoP4pi7k0tVDc78TirT4vGrUojzRaHmZJBUlbPpU3hwVFJb6w0nsKzOqJOBXCCT5Tma5v/s790-rw-e365/malware-attack.png)

The threat actors behind the [More\_eggs malware](https://thehackernews.com/2024/06/moreeggs-malware-disguised-as-resumes.html) have been linked to two new malware families, indicating an expansion of its malware-as-a-service (MaaS) operation.

This includes a novel information-stealing backdoor called RevC2 and a loader codenamed Venom Loader, both of which are deployed using [VenomLNK](https://quointelligence.eu/2020/07/golden-chickens-evolution-of-the-maas/), a staple tool that serves as an initial access vector for the deployment of follow-on payloads.

"RevC2 uses WebSockets to communicate with its command-and-control (C2) server. The malware is capable of stealing cookies and passwords, proxies network traffic, and enables remote code execution (RCE)," Zscaler ThreatLabz researcher Muhammed Irfan V A [said](https://www.zscaler.com/blogs/security-research/unveiling-revc2-and-venom-loader).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Venom Loader is a new malware loader that is customized for each victim, using the victim's computer name to encode the payload."

Both the malware families have been distributed as part of campaigns observed by the cybersecurity company between August and October 2024. The threat actor behind the e-crime offerings is tracked as Venom Spider (aka Golden Chickens).

The exact distribution mechanism is currently not known, but the starting point of one of the campaigns is VenomLNK, which, besides displaying a PNG decoy image, executes RevC2. The backdoor is equipped to steal passwords and cookies from Chromium browsers, execute shell commands, take screenshots, proxy traffic using SOCKS5, and run commands as a different user.

[![RevC2 Backdoor and Venom Loader](data:image/png;base64... "RevC2 Backdoor and Venom Loader")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4VJFJ2n16NYBKvIB8ELSlz8HZfRIKJw0jXBvUokASPe4lOUn121IjXAZXcb_EfMWcg6Bx3KHd4eCSwrROJK7H45GohzeuVIKBsBF1KOiEZKBzXY92KVtL7fUV5lS1bj2Zwwa8F18DL0MosdabFz2YcM5Wk3bhU_J3JydFQQqu61QCfrgc0jPkrcVKGgjK/s790-rw-e365/lnk.png)

The second campaign also begins with VenomLNK to deliver a lure image, while also stealthily executing Venom Loader. The loader is responsible for launching More\_eggs lite, a lightweight variant of the [JavaScript backdoor](https://thehackernews.com/2024/10/fake-job-applications-deliver-dangerous.html) that only provides RCE capabilities.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The new findings are a sign that the malware authors are continuing to refresh and refine their custom toolset with new malicious programs despite the fact that two individuals from [Canada](https://thehackernews.com/2023/01/experts-uncover-identity-of-mastermind.html) and [Romania](https://thehackernews.com/2023/05/meet-jack-from-romania-mastermind.html) were outed last year as running the MaaS platform.

The disclosure comes as ANY.RUN detailed a previously undocumented fileless loader malware dubbed PSLoramyra, which has been used to deliver the open-source Quasar RAT malware.

"This advanced malware leverages PowerShell, VBS, and BAT scripts to inject malicious payloads into a system, execute them directly in memory, and establish persistent access," it [said](https://any.run/cybersecurity-blog/psloramyra-malware-technical-analysis/).

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

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[More\_eggs](https://thehackernews.com/search/label/More_eggs)[Venom Spider](https://thehackernews.com/search/label/Venom%20Spider)[Zscaler](https://thehackernews.com/search/label/Zscaler)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:im...