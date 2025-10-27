---
title: Styx Stealer Creator's OPSEC Fail Leaks Client List and Profit Details
url: https://thehackernews.com/2024/08/styx-stealer-creators-opsec-fail-leaks.html
source: The Hacker News
date: 2024-08-22
fetch_date: 2025-10-06T18:06:19.202479
---

# Styx Stealer Creator's OPSEC Fail Leaks Client List and Profit Details

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

# [Styx Stealer Creator's OPSEC Fail Leaks Client List and Profit Details](https://thehackernews.com/2024/08/styx-stealer-creators-opsec-fail-leaks.html)

**Aug 21, 2024**Ravie LakshmananCyber Espionage / Threat Intelligence

[![OPSEC Fail](data:image/png;base64... "OPSEC Fail")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7ye1Nq5DpfzUb6eUUtkmqPTPzN-J6D6d3_V3LFRcSfexJs7iBqJRAqQw16g-g3T5vcLDNKSR_PjsG9WP4dpUZAXdKpxQIkB_8S-M0sTWFCWS8r7OL8EUPf9Lr0GSPYOjLQMVUjT8gkkiM7_mvDhx70TUYBlzBdc0lGQONMXA73IwxA3i96SHqSf3CIuh7/s790-rw-e365/code.png)

In what's a case of an operational security (OPSEC) lapse, the operator behind a new information stealer called Styx Stealer leaked data from their own computer, including details related to the clients, profit information, nicknames, phone numbers, and email addresses.

Styx Stealer, a derivative of the [Phemedrone Stealer](https://thehackernews.com/2024/01/hackers-weaponize-windows-flaw-to.html), is capable of stealing browser data, instant messenger sessions from Telegram and Discord, and cryptocurrency wallet information, cybersecurity company Check Point said in an analysis. It first emerged in April 2024.

"Styx Stealer is most likely based on the source code of an old version of Phemedrone Stealer, which lacks some features found in newer versions such as sending reports to Telegram, report encryption, and more," the company [noted](https://research.checkpoint.com/2024/unmasking-styx-stealer-how-a-hackers-slip-led-to-an-intelligence-treasure-trove/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"However, the creator of Styx Stealer added some new features: auto-start, clipboard monitor and crypto-clipper, additional sandbox evasion, and anti-analysis techniques, and re-implemented sending data to Telegram."

Advertised for $75 a month (or $230 for three months or $350 for a lifetime subscription) on a dedicated website ("styxcrypter[.]com"), licenses for the malware requires prospective buyers to reach out to a Telegram account (@styxencode). It's linked to a Turkey-based threat actor who goes by the alias STY1X on cybercrime forums.

Check Point said it was able to unearth connections between STY1X and a March 2024 spam campaign distributing Agent Tesla malware that targeted various sectors across China, India, the Philippines, and the U.A.E. The Agent Tesla activity has been attired to a threat actor named Fucosreal, whose approximate location is in Nigeria.

This was made possible owing to the fact that STY1X debugged the stealer on their own machine using a Telegram bot token provided by Fucosreal. This fatal error allowed the cybersecurity company to identify as many as 54 customers and 8 cryptocurrency wallets, likely belonging to STY1X, that are said to have been used to receive the payments.

"This campaign was notable for its use of the Telegram Bot API for data exfiltration, leveraging Telegram's infrastructure instead of traditional command-and-control (C&C) servers, which are more easily detectable and blockable," Check Point noted.

"However, this method has a significant flaw: each malware sample must contain a bot token for authentication. Decrypting the malware to extract this token provides access to all data sent via the bot, exposing the recipient account."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes amid the emergence of new stealer malware strains such as [Ailurophile](https://www.gdatasoftware.com/blog/2024/08/38005-ailurophile-infostealer), [Banshee Stealer](https://thehackernews.com/2024/08/new-banshee-stealer-targets-100-browser.html), and [QWERTY](https://www.cyfirma.com/research/qwerty-information-stealer/), even as well-known stealers like RedLine are being used in phishing attacks targeting Vietnamese oil and gas, industrial, electrical and HVAC manufacturers, paint, chemical, and hotel industries.

"RedLine is a well-known stealer that targets login credentials, credit card details, browser history, and even cryptocurrency wallets," Broadcom-owned Symantec [said](https://www.broadcom.com/support/security-center/protection-bulletin/redline-stealer-impersonates-oil-and-gas-company-targets-key-sectors-in-vietnam). "It is actively used by multiple groups and individuals around the world."

"Once installed, it collects data from the victim's computer and sends it to a remote server or Telegram channel controlled by the attackers."

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[data theft](https://thehackernews.com/search/label/data%20theft)[digital forensics](https://thehackernews.com/search/label/digital%20forensics)[Information security](https://thehackernews.com/search/label/Information%20security)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https:...