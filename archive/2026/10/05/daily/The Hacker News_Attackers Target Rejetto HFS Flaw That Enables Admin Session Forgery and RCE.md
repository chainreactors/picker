---
title: Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE
url: https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
source: The Hacker News
date: 2026-10-05
fetch_date: 2026-10-06T08:25:26.758151
---

# Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE](https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html)

**Ravie Lakshmanan**Oct 05, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTCvFj7lVSH1eLS0oYdxqBa4wQkNQvuemuCAL5XqwKueywAUl8Fg6zY-5UT9cdx3fZZ81DHX_emE9JXthW_OfH-axyWn3bE5CpCp4CDs4HREWjv_1uBtt5iJE947S-Bkn-4Mn1Shwt1kV9FF4RO9Wa7_4jmUtvbWrx2zs4-cdSg-FkUtxW-erVx2CXKhU3/s1700-nu-rw-lo-l85-e365/hfs-rce-main.jpg)

A critical security flaw impacting Rejetto HTTP File Server (HFS) is witnessing active exploitation attempts, according to VulnCheck.

The vulnerability in question is **CVE-2026-61500** (CVSS score: 9.3), a case of session forgery stemming from the use of a weak pseudo-random number generator (PRNG) that can lead to a predictable key, which an attacker can then use to gain unauthorized access and seize control of affected systems.

"Rejetto HFS 3.0.0 through 3.2.0 derives its session-cookie signing key from the non-cryptographic Math.random() generator and discloses outputs of the same generator to unauthenticated clients during login," according to an [advisory](https://github.com/advisories/GHSA-xxrm-3f86-v97j) for the flaw.

"A remote attacker can collect a small number of login responses, reconstruct the generator's state, recover the signing key, and forge a valid administrator session cookie, leading to full administrative access and remote code execution via the server\_code configuration feature."

Horizon3.ai researcher Zach Hanley, in a post [published](https://horizon3.ai/attack-research/disclosures/anthropic-mythos-rejetto-hfs-rce/) on September 30, 2026, said Anthropic's Mythos model was used to discover the vulnerability, describing it as an authentication bypass that facilitates arbitrary remote code execution on Rejetto HFS.

"Rejetto HFS's administrative API allows for custom endpoints that can execute arbitrary JavaScript," Hanley said. "Combined, this presented a clear path from unauthenticated access to administrative control, and ultimately, remote code execution."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

A patch for the vulnerability was released in July 2026 in [version 3.2.1](https://github.com/rejetto/hfs/releases/tag/v3.2.1). However, it was not until late September that a Python-based proof-of-concept (PoC) exploit was publicly released by a security researcher named Alejandro Ramos (aka aramosf).

"HFS generated its Koa session-cookie signing key with JavaScript Math.random() and exposed outputs from the same V8 PRNG in the unauthenticated SRP login handshake," Ramos [noted](https://github.com/aramosf/CVE-2026-61500). "An attacker can reconstruct the PRNG state, recover the signing key, forge an administrator session, and use the documented server\_code configuration feature to execute server-side JavaScript."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1eMxJU556yUr7jgiw-78vXKiKTMMttH4lCNaGVx324B1P0t8PxG7AR4__T8eWsy1fWASyXXxuEyGQ9yuQ3n0Mqqr45iQttoAlnb8Bx3P6yU0aPcE_i3JEqJQvcbp55qT8FGdysWCuvBNOwBYCBlczmuT88mJahJlYMLjNEso_h6tl29R6GfxG4OTo8EAw/s1700-nu-rw-lo-l85-e365/shift.jpg)

According to VulnCheck's Patrick Garrity, exploitation attempts were [detected](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7511590230232256513/) on October 1, 2026, a day after Horizon3.ai published additional details of the flaw. The cybersecurity company said it identified an unnamed threat actor in China targeting real vulnerable hosts in the U.S.

"Activity so far looks to be small-scale reconnaissance only, with a single China Telecom IP probing Canary deployments in Japan and the United States," Caitlin Condon, vice president of research at VulnCheck, [said](https://www.linkedin.com/posts/ccondon_new-kev-earlier-today-vulnchecks-canary-share-7511574376446590976-NNh3/) in a LinkedIn post.

CVE-2026-61500 is the second vulnerability in Rejetto HTTP File Server after [CVE-2024-23692](https://www.vicarius.io/vsociety/posts/unauthenticated-rce-flaw-in-rejetto-http-file-server-cve-2024-23692) (CVSS score: 9.8) to come under active exploitation in the wild. In July 2024, multiple threat actors were observed weaponizing the flaw to deliver [cryptocurrency miners, trojans](https://thehackernews.com/2024/07/microsoft-uncovers-critical-flaws-in.html), and a malware named [HATVIBE](https://thehackernews.com/2024/07/ukrainian-institutions-targeted-using.html).

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats](https://thehackernews.com/2026/09/weekly-reca...