---
title: ThreatsDay: AI Secrets Leak, PingCAP Source Theft, Signal Hang-Up Flaw, Laravel Auth Bypass + 21 More
url: https://thehackernews.com/2026/10/threatsday-ai-secrets-leak-pingcap.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:42.910389
---

# ThreatsDay: AI Secrets Leak, PingCAP Source Theft, Signal Hang-Up Flaw, Laravel Auth Bypass + 21 More

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [ThreatsDay: AI Secrets Leak, PingCAP Source Theft, Signal Hang-Up Flaw, Laravel Auth Bypass + 21 More](https://thehackernews.com/2026/10/threatsday-ai-secrets-leak-pingcap.html)

**Ravie Lakshmanan**Oct 22, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt9NuQgzmDAqircHtb2OEO9jXuNXIfpmc6cywt44gLVoKRSyrTtwqh2DaQkZ_BCrux5hLbZ9-uU9fR7Q6oFE7cjYOJB6aF1zqIJrrgT9A5RVRZguNYHZCk7-LBEAY7GxyR9KoCwwdPF9UowRvnZBvSN4X24RJXEQBRg3F1Mi5ktvXfNWWsUXlVnHLUmYd6/s1700-nu-rw-lo-l85-e365/threatsday-oct-main.jpg)

This week has already been rough for cybersecurity. [Critical PHP](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html) and [GitLab RCE](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html) flaws, serious [Linux security bugs](https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html), compromised [eMudhra certificates](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html), a [Node.js RCE flaw](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html), a [hacked LiteLLM](https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html) release, and hundreds of [hijacked Tor relays](https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html). That's a lot to deal with in just a few days. And the week isn't even over yet.

But those big headlines are only half the story. Stolen passwords, exposed databases, broken login checks, and trusted tools being turned against their users are causing trouble too. Some attacks are clever. Others work because someone left a simple security gap open.

This ThreatsDay, we're digging into the stories that didn't make as much noise but still deserve attention. Some are strange, some are serious, and a few might surprise you. Here's everything else you shouldn't miss this week.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. 4,500+ accounts compromised

   [Bluesky Confirms More Than 4,500 Accounts Compromised in Phishing Campaign](https://bsky.app/profile/safety.bsky.app/post/3my3zch7j4225)

   Bluesky has acknowledged it's aware of a phishing attack that has compromised more than 4,500 accounts. "The attack spread through posts promoting a fake offer of a government payment," Bluesky [said](https://bsky.app/profile/safety.bsky.app/post/3my3zch7j4225). "We have temporarily suspended the compromised accounts and are working with their owners to secure them and restore access. If your account was suspended, email moderation@blueskyweb.xyz and we will help to get you back into your account."
2. Android malware scam losses

   [Singapore Police Warn of Android Malware Scams Causing Nearly S$1 Million in Losses](https://www.police.gov.sg/Media-Hub/News/2026/10/20261020_police_advisory_on_malware_from_social_media_advertisements)

   The Singapore Police Force has alerted users of a malware-enabled scam variant involving advertisements on social media platforms promoting senior-focused activities and programmes, water-based fitness activities, and recycling initiatives. The agency said at least 62 cases have been reported since April 2026, leading to S$989,000 in losses. "In this scam, victims would come across the fake advertisements on social media platforms, such as Facebook, and be instructed to download an Android Application Package (APK) file to facilitate programme registration or service arrangements," the Singapore Police Force [said](https://www.police.gov.sg/Media-Hub/News/2026/10/20261020_police_advisory_on_malware_from_social_media_advertisements). "After installing the application, victims would receive unsolicited calls from scammers impersonating government officials or bank representatives, who would falsely claim that the victims' devices or bank accounts had been compromised, or that they were implicated in criminal activities. Victims would then be induced to transfer monies, disclose banking credentials or personal information, or surrender valuables for investigations."
3. Customer credentials exposed

   [Andromeda Confirms Credential Theft Affecting AI Infrastructure Customers](https://andromeda.ai/security-updates/october-2026-security-incident)

   Andromeda said it identified a security incident on October 13, 2026, that involved unauthorized access to credentials in its environment. "We disabled the compromised accounts that day and have observed no further unauthorized activity since," it [said](https://andromeda.ai/security-updates/october-2026-security-incident). "We believe the activity began as part of an industry-wide attack on or about October 9th. It affected a limited number of customer accounts and involved exposure of certain Andromeda and customer credentials. If we believe you were affected, you’ve already heard from us." The company said there is no evidence of unauthorized access to customer models, datasets, or training data.
4. 20 security flaws patched

   [Roundcube Fixes 20 Security Issues Including IMAP Injection and SSRF Bypass](https://roundcube.net/news/2026/10/19/security-updates-1.6.20-and-1.7.5)

   Roundcube has [released](https://roundcube.net/news/2026/10/19/security-updates-1.6.20-and-1.7.5) versions 1.6.20 and 1.7.5, addressing 20 issues including IMAP command injection, SSRF filter bypass, and unsafe attachment handling. There is no evidence any of the patched vulnerabilities have been exploited.
5. Internal business systems breached

   [Genesys Confirms Breach of Internal CRM and Learning Systems](https://www.genesys.com/blog/post/security-update-incident-affecting-certain-genesys-internal-business-systems)

   On October 16, 2026, Genesys [disclosed](https://www.genesys.com/blog/post/security-update-incident-affecting-certain-genesys-internal-business-systems) that it became aware of a cybersecurity incident involving an unauthorized third p...