---
title: Hackers Spied on a Stock Exchange Executive's Outlook Mailbox for Five Months
url: https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html
source: The Hacker News
date: 2026-06-04
fetch_date: 2026-06-05T06:14:27.181442
---

# Hackers Spied on a Stock Exchange Executive's Outlook Mailbox for Five Months

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

# [Hackers Spied on a Stock Exchange Executive's Outlook Mailbox for Five Months](https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html)

**Swati Khandelwal**Jun 04, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpg8pBdHkENT_CKClsSR7f4Rb7BQpM27ynGrkRdJg-bbUfI2NIHQ_rFmkOVHjK8RggTD-XMvVdGGI_qrYyIx-Ml1sfwbRkbjaNo8Fz40cWg8wFWK8h5-f-FaB58HryMM5AYlUHI2uO7x12VFvAB6N3w1gobWmzGgp8xXqHfWMERFh7hVS9lBHxfdu71Xs/s1700-e365/stock-emails.jpg)

Unknown attackers spent at least five months inside the Outlook mailbox of a senior executive at a major global stock exchange, copying the inbox out in small, repeated batches and routing it through Dropbox and OneDrive so the traffic blended into normal cloud activity.

Symantec and Carbon Black's Threat Hunter Team [reported the campaign](https://www.security.com/threat-intelligence/stock-exchange-espionage) this week. This points to espionage, not a money grab: Symantec said the commands indicate intelligence collection, not theft for profit.

Neither the executive nor the exchange was named. The value is plain enough: an exchange executive's inbox can hold non-public listing details, enforcement matters, deal terms, market-moving plans, plus the executive's calendar and contacts.

Five months of quiet access handed the attacker a detailed read on the executive's dealings and where the organization was heading, without needing broad access to other business systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The first malicious activity showed up on October 10, 2025. By then, the attacker was already running two binaries as SYSTEM, the highest Windows privilege level, one faking Adobe's updater and the other faking OneDrive. By the time defenders noticed anything, the intruder had full control of the machine, and how they first got in is still unknown.

However, Symantec confirmed that the first signs likely came from lateral movement off a previously compromised device. The operation kicked into gear on November 12. The attacker pulled a Dropbox API token, started uploading data with curl, and deployed the main tool: a mailbox stealer built on Aspose, a legitimate .NET library that reads Outlook OST and PST files. Wrapped in an executable, it converted the mailbox to PST and wrote it to disk, run each time with a password and a date-range flag.

The first run grabbed everything from August 2025 on. After that the attacker came back every two to four weeks, each run taking only the days since the last one, eight more pulls through February 17, 2026. The result is a near-continuous copy of the mailbox, sliced thin enough not to draw attention from security software.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhInePiuhvcYvN3R5EQ7oSXksOnPKC_WDXuPKSAcV1TZVzzzP8itnACG-M51q4VSBTRoXik9R4uuDIFk9h-Qv8avEqkXufs_Ef_F0c3Rn-TA_DnVqX7dTIu_HlDoPDgOitSid3KzeJLjMV9UEL_ssaSL6wLYePJTfG4B-f8gNIbXzf8RQCBup1EMI8VFuY/s1700-e365/ss.jpg)

The stealth came from making the work look ordinary. Scheduled tasks posed as Adobe, Lenovo and OneDrive system services. For exfiltration the attacker used Dropbox and OneDrive Personal, and for OneDrive they connected to hard-coded Microsoft IP addresses instead of the onedrive.live.com hostname, so there were no DNS lookups for a perimeter tool to catch or block.

The attacker also tested the public file host temp.sh once in November, then dropped it. The last observed activity, on March 19, 2026, was a new backdoor that was staged but never run, which Elias said may mean the attacker lost access soon after.

Symantec's published indicators point to a wider intrusion kit, not just a mailbox grabber: FRPC for tunneling traffic out, Secretsdump for pulling Windows credentials, SharpDecryptPwd for recovering saved app passwords, and a tool to bypass Windows User Account Control. The report does not say how each was used here, and none of them point to a specific group.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

There is no CVE in this story. It was an intrusion against a person's mailbox, not the exploitation of a freshly disclosed flaw, which is part of why it is worth reading: no patch closes this, and the burden shifts to monitoring and response.

Attribution is unresolved too. The mix of public tooling and consumer cloud services left little to tie the activity to a known actor, and that stays open until a stronger source says otherwise. Routing exfiltration through Dropbox and OneDrive to blend in is a well-worn play, and one [Microsoft has flagged](https://thehackernews.com/2024/10/microsoft-detects-growing-use-of-file.html) as a deliberate way to slip past perimeter defenses and muddy attribution.

If you defend an exchange, a regulator, or any firm sitting on market-moving information, feed the hashes in now and watch for the behavior behind them: unusual mailbox export activity, odd Outlook access, uploads to personal Dropbox or OneDrive accounts, unexpected tunneling, and credential-dumping on systems tied to privileged users.

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
...