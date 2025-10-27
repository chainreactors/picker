---
title: Neglected Domains Used in Malspam to Evade SPF and DMARC Security Protections
url: https://thehackernews.com/2025/01/neglected-domains-used-in-malspam-to.html
source: The Hacker News
date: 2025-01-09
fetch_date: 2025-10-06T20:14:49.945510
---

# Neglected Domains Used in Malspam to Evade SPF and DMARC Security Protections

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

# [Neglected Domains Used in Malspam to Evade SPF and DMARC Security Protections](https://thehackernews.com/2025/01/neglected-domains-used-in-malspam-to.html)

**Jan 08, 2025**Ravie LakshmananEmail Security / Cybercrime

[![Neglected Domains](data:image/png;base64... "Neglected Domains")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCXs_wTz3FRVBTZBk-v-qswiTqiODpdqZaTrSV_3o3YuwjcmkQCubWf4fDrqazt2LiWEz34xvyembq-18Gj9zZk85hgq-3lj4xZjpP8Oht79FpD4EJcoLQGA86vgXv72YtjSUcULQqk7zUGqlw_kTETvcpk2XckIWGeC5OcGWQDMRJKHyqGSeUGDYXJawj/s790-rw-e365/phishing.png)

Cybersecurity researchers have found that bad actors are continuing to have success by spoofing sender email addresses as part of various malspam campaigns.

Faking the sender address of an email is widely seen as an attempt to make the digital missive more legitimate and get past security mechanisms that could otherwise flag it as malicious.

While there are [safeguards](https://thehackernews.com/2024/02/8000-subdomains-of-trusted-brands.html) such as DomainKeys Identified Mail (DKIM), Domain-based Message Authentication, Reporting and Conformance (DMARC), and Sender Policy Framework (SPF) that can be used to prevent spammers from spoofing well-known domains, such measures have increasingly led them to leverage old, neglected domains in their operations.

In doing so, the email messages are likely to bypass security checks that rely on the domain age as a means to identify spam.

DNS threat intelligence firm Infoblox, in a [new analysis](https://blogs.infoblox.com/threat-intelligence/muddling-malspam-the-use-of-spoofed-domains-in-malicious-spam/) shared with The Hacker News, discovered that threat actors, including [Muddling Meerkat](https://thehackernews.com/2024/04/china-linked-muddling-meerkat-hijacks.html) and others, have abused some of its own old, disused top-level domains (TLDs) that haven't been used to host content for nearly 20 years.

"They lack most DNS records, including those that are typically used to check the authenticity of a sender domain, e.g., Sender Policy Framework (SPF) records," the company said. "The domains are short and in highly reputable TLDs."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

One such campaign, active since at least December 2022, involves distributing email messages with attachments containing QR codes that lead to phishing sites. It also instructs recipients to open the attachment and use the AliPay or WeChat apps on their phones to scan the QR code.

The emails employ tax-related lures written in Mandarin, while also locking the QR code documents behind a four-digit password included in the email body in different ways. The phishing site, in one case, urged users to enter their identification and card details, and then make a fraudulent payment to the attacker.

"Although the campaigns do use the neglected domains we see with Muddling Meerkat, they appear to broadly spoof random domains, even ones that do not exist," Infoblox explained. "The actor may use this technique to avoid repeated emails from the same sender."

The company said it also observed phishing campaigns that impersonate popular brands like Amazon, Mastercard, and SMBC to redirect victims to fake login pages using traffic distribution systems (TDSes) with an aim to steal their credentials. Some of the email addresses that have been identified as using spoofed sender domains are listed below -

* ak@fdd.xpv[.]org
* mh@thq.cyxfyxrv[.]com
* mfhez@shp.bzmb[.]com
* gcini@vjw.mosf[.]com
* iipnf@gvy.zxdvrdbtb[.]com
* zmrbcj@bce.xnity[.]net
* nxohlq@vzy.dpyj[.]com

A third category of spam relates to extortion, wherein email recipients are asked to make a $1,800 payment in Bitcoin to deleteembarrassing videos of themselves that were recorded using a purported remote access trojan installed on their systems.

"The actor spoofs the user's own email address and challenges them to check it and see," Infoblox The email tells the user that their device has been compromised, and as proof, the actor alleges that the message was sent from the user's own account."

The disclosure comes as legal, government and construction sectors have been targeted by a new phishing campaign dubbed Butcher Shop that aims to steal Microsoft 365 credentials since early September 2024.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgH_fdluiYbUtj9s7xWh9A_SrF-zkpqFNZsO0RbaU4ITmbWzS3S1DBSKk9bTOTfQT5iQzE3wZrJhhgJf2YPzaICMTG1xgQ9H-37fXFo_QLuuqhrFb6s1Erd4ugxtGwGPmRsnu2Ya4vJadYlu3a320Z3xt4HHyNy0kLvkSS7nonR8S2sQ3SRoq95G9u64jnR/s790-rw-e365/cf.png)

The attacks, per Obsidian Security, abuse trusted platforms like Canva, Dropbox DocSend, and Google Accelerated Mobile Pages (AMPs) to redirect users to the malicious sites. Some of the other channels include emails and compromised WordPress sites.

"Before displaying the phishing page, a custom page with a Cloudflare Turnstile is shown to verify that the user is, in fact, human," the company [said](https://www.obsidiansecurity.com/blog/butcher-shop-phishing-campaign-targets-organizations/). "These turnstiles make it harder for email protection systems, like URL scanners, to detect phishing sites."

In recent months, SMS phishing campaigns have been observed impersonating law enforcement authorities in the U.A.E. to send fake payment requests for non-existent traffic violations, parking violations, and license renewals. Some of the bogus sites set up for this purpose have been [attributed](https://www.resecurity.com/blog/article/cybercriminals-impersonate-dubai-police-to-defraud-consumers-in-the-uae-smishing-triad-in-action) to a known threat actor called [Smishing Triad](https://thehackernews.com/2024/06/grandoreiro-banking-trojan-hits-brazil.html).

Banking customers in the Middle East have also been targeted by a sophisticated social engineering scheme that impersonates government officials in phone calls and employs remote access software to steal credit ca...