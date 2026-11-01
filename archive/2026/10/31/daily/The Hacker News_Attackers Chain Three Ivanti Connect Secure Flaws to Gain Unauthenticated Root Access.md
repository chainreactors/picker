---
title: Attackers Chain Three Ivanti Connect Secure Flaws to Gain Unauthenticated Root Access
url: https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html
source: The Hacker News
date: 2026-10-31
fetch_date: 2026-11-01T08:21:37.479118
---

# Attackers Chain Three Ivanti Connect Secure Flaws to Gain Unauthenticated Root Access

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Attackers Chain Three Ivanti Connect Secure Flaws to Gain Unauthenticated Root Access](https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html)

**Ravie Lakshmanan**Oct 31, 2026Vulnerability / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeqP4vPt6j2lLPFj77A_1OthmSKb8mItfBrX_q8sQCAUVgTry1FxKizDI2SCLS4CglfjgbVkaMDN8ainqoOZm2pdaF6xw7sU4STZhwIFPCLSz84YXQTVx2tquPo7YJsZhgOWcD3V_w5td9BA_vVuOu1cFcrgL3SXyLF4E24IyGotrzDcbJ-M1mA85biDuW/s1700-nu-rw-lo-l85-e365/1000120841.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday [added](https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog) two security flaws impacting Ivanti Connect Secure (ICS) to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, following active exploitation in the wild.

The vulnerabilities are listed below -

* **CVE-2026-111357** (CVSS score: 8.8) - A missing authentication for a critical function vulnerability that could allow a local authenticated attacker to escalate their privileges.
* **CVE-2026-118527** (CVSS score: 4.3) - A generation of predictable numbers or identifiers vulnerability that could allow a remote authenticated attacker to upload files with attacker-controlled content to a known location on disk.

It's worth noting that the security bugs are part of an [exploit chain](https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html) that was first documented by Volexity earlier this month as weaponized in conjunction with an authentication bypass flaw (CVE-2026-104935, CVSS score: 8.6) by a previously undocumented threat actor dubbed UTA0576. CVE-2026-104935 was [added](https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html) to the KEV catalog on October 13, 2026.

"This exploit chain combined an authentication bypass, a remote code execution (RCE), and a privilege escalation vulnerability to achieve unauthenticated root-level code execution," Volexity noted.

Unlike other attacks that typically exploit such flaws to deploy web shells or malware, UTA0576 has been observed leveraging the flaws to extract credentials and limited Active Directory metadata; conduct host reconnaissance; and search for administrator passwords and BitLocker recovery keys.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Ivanti said that, around the time the details were published, it was still working on developing fixes for the local privilege escalation (LPE) vulnerability exploited in the attack chain. Patches for both CVE-2026-111357 and CVE-2026-118527 are now available in the following versions of ICS -

* 25.1.1.2 and prior (Fixed in 25.1.1.3)
* 22.8R2.5 and prior (Fixed in 22.8R2.6)

"At the time of discovery of exploitation, Ivanti had a fix developed for CVE-2026-104935 which was already in QA for supported versions, and we made the decision to not delay getting a fix to customers that resolved the primary exploitation path when the LPE was discovered," Ivanti [explained](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US).

"Because of this, our focus was initially centered on the disclosure of CVE-2026-104935 and providing protection for our customers as quickly as possible."

The company also noted that it discovered a portion of this vulnerability as part of its product security program and patched it in the July release 25.1.3.0, adding it had been working to backport the fix to other supported versions when exploitation activity occurred.

The latest release addresses all vulnerabilities which were chained and exploited in the wild. Federal Civilian Executive Branch (FCEB) agencies are required to apply the fixes for CVE-2026-111357 by November 2, 2026, and CVE-2026-118527 by November 13, 2026.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them](https://thehackernews.com/2026/10/teamviewer-flaw-lets-remote-computers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Official Claude Code Extension on Cursor Marketplace Trojanized wi...