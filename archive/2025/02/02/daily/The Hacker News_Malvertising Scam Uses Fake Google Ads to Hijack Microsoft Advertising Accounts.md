---
title: Malvertising Scam Uses Fake Google Ads to Hijack Microsoft Advertising Accounts
url: https://thehackernews.com/2025/02/malvertising-scam-uses-fake-google-ads.html
source: The Hacker News
date: 2025-02-02
fetch_date: 2025-10-06T20:38:25.108342
---

# Malvertising Scam Uses Fake Google Ads to Hijack Microsoft Advertising Accounts

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

# [Malvertising Scam Uses Fake Google Ads to Hijack Microsoft Advertising Accounts](https://thehackernews.com/2025/02/malvertising-scam-uses-fake-google-ads.html)

**Feb 01, 2025**Ravie LakshmananMalvertising / Mobile Security

[![Malvertising Scam](data:image/png;base64... "Malvertising Scam")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSmjvusalOsx5BY80bTBTB8ucS2cwAaDYYnT1DtwWLWesKVUVnyIr9zF9UQXHo3aew3wDOT03DoaDdTKHZ8TXol-sCUFS5D2O6iDI7hA6v5npXqF7IugbTYpAi-I5Ck3szRFVwZsaSLN8oKQz2KwngxTCcG1bK6Dmg1qNfrirvZJrtpclVVqETcLkMYjW5/s790-rw-e365/malware-ads.png)

Cybersecurity researchers have discovered a malvertising campaign that's targeting Microsoft advertisers with bogus Google ads that aim to take them to phishing pages that are capable of harvesting their credentials.

"These malicious ads, appearing on Google Search, are designed to steal the login information of users trying to access Microsoft's advertising platform," Jérôme Segura, senior director of research at Malwarebytes, [said](https://www.malwarebytes.com/blog/news/2025/01/microsoft-advertisers-phished-via-malicious-google-ads) in a Thursday report.

The findings came a few weeks after the cybersecurity company [exposed](https://thehackernews.com/2025/01/google-ads-users-targeted-in.html) a similar campaign that leveraged sponsored Google Ads to target individuals and businesses advertising via the search giant's advertising platform.

The latest set of attacks targets users who search for terms like "Microsoft Ads" on Google Search, hoping to trick them into clicking on malicious links served in the form of sponsored ads in the search results pages.

At the same time, the threat actors behind the campaign employ several techniques to evade detection by security tools. This includes redirecting traffic originating from VPNs to a phony marketing website. Site visitors are also served Cloudflare challenges in an attempt to filter out bots.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Last but not least, users who attempt to directly visit the final landing page ("ads.mcrosoftt[.]com") are [rickrolled](https://en.wikipedia.org/wiki/Rickrolling) by redirecting them to a YouTube video linked to the famous internet meme.

The phishing page is a lookalike version of its legitimate counterpart ("ads.microsoft[.]com") that's designed to capture the victim's login credentials and two-factor authentication (2FA) codes, granting the attackers the ability to hijack their accounts.

Malwarebytes said it identified additional phishing infrastructure targeting Microsoft accounts going back to a couple of years, suggesting that the campaign has been ongoing for some time and that it may have also targeted other advertising platforms like Meta.

Another notable aspect is that a majority of the phishing domains are either hosted in Brazil or have the ".com.br" Brazilian top-level domain, drawing parallels to the campaign aimed at Google Ads users, which was predominantly hosted on the ".pt" TLD.

Google previously told The Hacker News that it takes steps to prohibit ads that seek to dupe users with the goal of stealing their information, and that it has been actively working to enforce countermeasures against such efforts.

"We expressly prohibit ads that aim to deceive people and we suspend advertisers' accounts if they are found to engage in this practice, as we have done here," a Google spokesperson told the publication when reached for comment.

[![Microsoft Advertising Accounts](data:image/png;base64... "Microsoft Advertising Accounts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdGyZGQRkLSacwe4skLKgRu1Zi5dCxiOUa2D1LX5IAHxoUFA3UfMEgUOJRkNmbHbjogsSwRnB9L0-CFugQK9STDWYKkZBUI2DUEAU707V3c4VyZak9TS8e_zH1nBb7xavbVhbYTr8dczq81vGNSdjwSqUHNRzT7r1jubS50diJkHTCJVAyw_-a0wrHRZ1j/s790-rw-e365/ads.png)

### Smishing Attacks Impersonate USPS

The disclosure follows the emergence of an SMS phishing campaign that employs failed package delivery lures to exclusively target mobile device users by impersonating the United States Postal Service (USPS).

"This campaign employs sophisticated social engineering tactics and a never-before-seen means of obfuscation to deliver malicious PDF files designed to steal credentials and compromise sensitive data," Zimperium zLabs researcher Fernando Ortega [said](https://www.zimperium.com/blog/hidden-in-plain-sight-pdf-mishing-attack/) in a report published this week.

The messages urge recipients to open an accompanying PDF file to update their address to complete the delivery. Present within the PDF document is a "Click Update" button that directs the victim to a USPS phishing web page, where they are asked to enter their mailing address, email address, and phone number.

The phishing page is also equipped to capture their payment card details under the guise of a service charge for redelivery. The entered data is then encrypted and transmitted to a remote server under the attacker's control. As many as [20 malicious PDFs and 630 phishing pages](https://github.com/Zimperium/IOC/tree/master/2025-01-PDF-Phishing) have been detected as part of the campaign, indicating a large-scale operation.

"The PDFs used in this campaign embed clickable links without utilizing the standard /URI tag, making it more challenging to extract URLs during analysis," Ortega noted. "This method enabled known malicious URLs within PDF files to bypass detection by several endpoint security solutions."

The activity is a sign that cybercriminals are exploiting security gaps in mobile devices to pull off social engineering attacks that capitalize on users' trust in popular brands and official-looking communications.

Similar USPS-themed smishing attacks have also utilized Apple's iMessage to deliver the phishing pages, a technique known to be adopted by a Chinese-speaking threat actor known as [Smishing Triad](https://thehackernews.com/2023/09/chinese-speaking-cybercriminals-launch.html).

[![CIS Build Kits...