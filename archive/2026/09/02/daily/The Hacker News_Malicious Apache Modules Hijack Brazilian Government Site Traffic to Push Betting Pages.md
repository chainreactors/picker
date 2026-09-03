---
title: Malicious Apache Modules Hijack Brazilian Government Site Traffic to Push Betting Pages
url: https://thehackernews.com/2026/09/malicious-apache-modules-hijack.html
source: The Hacker News
date: 2026-09-02
fetch_date: 2026-09-03T07:02:41.921549
---

# Malicious Apache Modules Hijack Brazilian Government Site Traffic to Push Betting Pages

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

# [Malicious Apache Modules Hijack Brazilian Government Site Traffic to Push Betting Pages](https://thehackernews.com/2026/09/malicious-apache-modules-hijack.html)

**Swati Khandelwal**Sep 02, 2026Web Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixn-0jJvMDlL85UUyW0E5PUDeUnMbGMxZJEnJMOAXXAuiqD-e1D9IoZdYsNwwDY16NA7x7GFHzVrx6LqJU7u7ywR50UWP4DGybNAhTlLPeAiBcVwVUJPgV1KbD1u0aUNy_468Y6gMQJ8FlnfGFlz_iCJcAeOeTiPViV1195lHwovULdtSBlsvPWOGpNU8/s1700-nu-rw-lo-l85-e365/check.jpg)

A Chinese-speaking cybercrime cluster known as **Gambling Goblin** has been observed installing malicious Apache modules on compromised web servers run by Brazilian government and educational institutions, and using them to divert visitors to attacker-controlled pages promoting online gambling and sports betting.

Check Point Research said it has tracked the campaign since mid-2025.

The modules reverse-proxy visitors to a set of phishing pages while the traffic still appears to originate from the legitimate domain. The site's own security headers are stripped, allowing the injected content to run freely.

Those pages pose as trusted app stores including Google Play, Microsoft Store, and Amazon, and push online gambling and sports betting behind that facade.

Check Point said the likely goal is search engine optimization (SEO) manipulation at scale, with compromised high-reputation domains, many of them Brazilian government sites, chained together to inflate search rankings.

ANY.RUN reported in July that [at least 20 .gov.br portals](https://thehackernews.com/2026/07/20-hijacked-government-websites.html) belonging to Brazilian municipalities and police forces had been used to distribute malware in a campaign it tracks as **PhantomEnigma**.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"These government systems are part of the delivery chain, not confirmed campaign targets," ANY.RUN said in a report published July 16.

Compromised .gov.br and .jus.br hosts should be handled separately from attacker-controlled infrastructure, ANY.RUN said, because blocking them broadly would disrupt access to government resources.

Brazil began licensing fixed-odds betting on January 1, 2025, under Law 14,790/2023, and authorized operators to run on .bet.br domains issued through Registro.br, Brazil's domain registry.

Check Point did not say whether the betting sites promoted through the compromised servers hold that authorization.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHewWyk3XJllurk7qzIMg542kGUOT0bMsiXXVOf6SMQ55C6CPPxQH-0JTCvzwxweCeG744ytU4SjpoNNYvLkC8_-U25ptEzPdp7R0wlz9YRmqM7FRidWoj0ZZYelBprgZMylPssCNVXUvoHoeJ3-gjkcO7ku2sKfVJXkAdbeV4P6u1K8GzljuCz-vI5YI/s1700-nu-rw-lo-l85-e365/betting.png)

Once on a host, [Check Point said](https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/) the group deploys the following tools -

* **DownPro**, a custom downloader
* **AlphaAgent**, a modular backdoor
* **oRAT**, a remote access trojan (RAT)
* **A 3snake-based credential stealer**
* An SSH brute-forcer
* A plugin-driven reconnaissance agent

The public version of 3snake attaches ptrace to newly spawned sshd and sudo processes and extracts strings related to password-based authentication. Its documentation states that the tool targets rooted servers.

The Hacker News reviewed [the 3snake source on GitHub](https://github.com/blendin/3snake) on September 2, 2026, and confirmed both. The credentials used to administer a compromised server are therefore read by a component the operators control.

Check Point said it hasn't directly observed how the group obtains initial access. An exposed open directory on one of the actor's servers held an ELF binary written in Go that bundles reconnaissance and scanning plugins.

The material published so far includes no count of compromised servers and no module filenames, paths, or hashes that would let administrators check the modules loaded into their own Apache instances.

Parallel phishing networks localized in Vietnamese, Spanish, and English were also identified, along with infrastructure that generates new domains daily. Because the pages already mimic app-download destinations, Check Point said the operators sit "one step from pushing malware straight to victims."

The published summary names no affected organization and does not say whether the compromised servers have been cleaned.

Check Point tied the cluster to Earth Berberoka, an actor Trend Micro documented in 2022 as targeting gambling websites across Asia using malware families historically attributed to Chinese-speaking individuals.

[Xnote, a Linux backdoor](https://thehackernews.com/2026/03/web-server-exploits-and-mimikatz-used.html) tied to the group, was reported in March during attacks on critical infrastructure in Asia.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

oRAT, one of the Linux tools in that arsenal, was documented by Trend Micro [in April 2022](https://www.trendmicro.com/en_us/research/22/d/new-apt-group-earth-berberoka-targets-gambling-websites-with-old.html) as Earth Berberoka malware, in Windows and macOS samples both flagged as version 0.5.1. The Hacker News confirmed that provenance against Trend Micro's research on September 2, 2026.

ESET documented [at least 65 Windows servers](https://thehackernews.com/2025/09/ghostredirector-hacks-65-windows.html) , mainly in Brazil, Thailand, and Vietnam, compromised in June 2025 by GhostRedirector, an actor it assessed with medium confidence as China-aligned, which installed a native Internet Information Services (IIS) module called Gamshen.

"GhostRedirector has developed a malicious native IIS module, Gamshen, that can perform SEO fraud; we believe its purpose is to artificially promo...