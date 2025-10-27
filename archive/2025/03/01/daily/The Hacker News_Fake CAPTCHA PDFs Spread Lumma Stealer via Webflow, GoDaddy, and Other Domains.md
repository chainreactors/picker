---
title: Fake CAPTCHA PDFs Spread Lumma Stealer via Webflow, GoDaddy, and Other Domains
url: https://thehackernews.com/2025/02/5000-phishing-pdfs-on-260-domains.html
source: The Hacker News
date: 2025-03-01
fetch_date: 2025-10-06T22:01:48.398186
---

# Fake CAPTCHA PDFs Spread Lumma Stealer via Webflow, GoDaddy, and Other Domains

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

# [Fake CAPTCHA PDFs Spread Lumma Stealer via Webflow, GoDaddy, and Other Domains](https://thehackernews.com/2025/02/5000-phishing-pdfs-on-260-domains.html)

**Feb 28, 2025**Ravie LakshmananNetwork Security / Malware

[![Phishing PDFs](data:image/png;base64... "Phishing PDFs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8wponAwogFPLdER3yW6L-XbukZl3Wn1x9LlHrDj1sXPokvzLExCy55utTczDiOvQ4eKz9l2_FoE0-cF7GIt3jJHdqr1am9nZl3SjW4-di2fcYhNQQ7p7AdFQLVm4MpcOwj11XxbnKrXwxFS4bucICXFfTGbUZJ6L_SNcANWfkfAtegTzns0shpauhswPe/s790-rw-e365/pdf.png)

Cybersecurity researchers have uncovered a widespread phishing campaign that uses fake CAPTCHA images shared via PDF documents hosted on Webflow's content delivery network (CDN) to deliver the Lumma stealer malware.

Netskope Threat Labs said it discovered 260 unique domains hosting 5,000 phishing PDF files that redirect victims to malicious websites.

"The attacker uses SEO to trick victims into visiting the pages by clicking on malicious search engine results," security researcher Jan Michael Alcantara [said](https://www.netskope.com/blog/fake-captchas-malicious-pdfs-seo-traps-leveraged-for-user-manual-searches) in a report shared with The Hacker News.

"While most phishing pages focus on stealing credit card information, some PDF files contain fake CAPTCHAs that trick victims into executing malicious PowerShell commands, ultimately leading to the Lumma Stealer malware."

The phishing campaign is estimated to have affected more than 1,150 organizations and more than 7,000 users since the second half of 2024, with the attacks primarily singling out victims in North America, Asia, and Southern Europe across technology, financial services, and manufacturing sectors.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Of the 260 domains identified to host the fake PDFs, a majority of them are [related to Webflow](https://thehackernews.com/2025/02/hackers-use-captcha-trick-on-webflow.html), followed by those related to GoDaddy, Strikingly, Wix, and Fastly.

Attackers have also been observed uploading some of the PDF files to legitimate online libraries and PDF repositories like PDFCOFFEE, PDF4PRO, PDFBean, and Internet Archive, such that users searching for PDF documents on search engines are directed to them.

The PDFs contain fraudulent CAPTCHA images that act as a conduit to steal credit card information. Alternatively, those distributing Lumma Stealer contain images to download the document that, when clicked, takes the victim to a malicious site.

For its part, the site masquerades as a fake CAPTCHA verification page that employs the [ClickFix technique](https://thehackernews.com/2025/02/threat-actors-exploit-clickfix-to.html) to deceive the victim into running an MSHTA command that executes the stealer malware by means of a PowerShell script.

In recent weeks, Lumma Stealer has also been [disguised](https://asec.ahnlab.com/en/86435/) as Roblox games and a cracked version of the Total Commander tool for Windows, highlighting the myriad delivery mechanisms adopted by various threat actors. Users are redirected to these websites through YouTube videos likely uploaded from previously compromised accounts.

"Malicious links and infected files are often disguised in [YouTube] videos, comments, or descriptions," Silent Push [said](https://www.silentpush.com/blog/lumma-stealer/). "Exercising caution and being skeptical of unverified sources when interacting with YouTube content, especially when prompted to download or click on links, can help protect against these growing threats."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxfvOYDijN9HPf7ST5NhPhysDLXF4eW44Pefk_feCXtzWKeIyMCJG3MlyGJONTmFupvPn8AvT5aFcb1gZKg7YP39O6UbcTd3uA2RvVraG7CKv6aI3D35GK0Iz2hY43E1yq6J-mXn1CbwmiZRX6DlB1p7OOGYuSqIGLqkqwzBnq5bdpiqvKmaw67-ifAvUm/s790-rw-e365/pdfs.png)

The cybersecurity company further found that Lumma Stealer logs are being shared for free on a relatively new hacking forum called Leaky[.]pro that went operational in late December 2024.

Lumma Stealer is a [fully-featured crimeware solution](https://thehackernews.com/2025/02/sticky-werewolf-uses-undocumented.html) that's offered for sale under the malware-as-a-service (MaaS) model, giving a way for cybercriminals to harvest a wide range of information from compromised Windows hosts. In early 2024, the malware operators announced an integration with a Golang-based proxy malware named GhostSocks.

"The addition of a SOCKS5 backconnect feature to existing Lumma infections, or any malware for that matter, is highly lucrative for threat actors," Infrawatch [said](https://infrawatch.app/blog/ghostsocks-lummas-partner-in-proxy).

"By leveraging victims' internet connections, attackers can bypass geographic restrictions and IP-based integrity checks, particularly those enforced by financial institutions and other high-value targets. This capability significantly increases the probability of success for unauthorized access attempts using credentials harvested via infostealer logs, further enhancing the post-exploitation value of Lumma infections."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosures come as stealer malware like [Vidar](https://thehackernews.com/2023/06/vidar-malware-using-new-tactics-to.html) and Atomic macOS Stealer ([AMOS](https://thehackernews.com/2025/02/crazy-evil-gang-targets-crypto-with.html)) are being distributed using the ClickFix method via lures for the DeepSeek artificial intelligence (AI) chatbot, according to [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/deepseek-lure-using-captchas-spread-malware) and [eSentire](https://www.esentire.com/blog/fake-deepseek-site-infects-mac-users-with-atomic-stealer).

Phishing attacks have also been spotted abusing a JavaScript obfuscation method that uses invisible Unicode characters to represent binary values, a technique that was...