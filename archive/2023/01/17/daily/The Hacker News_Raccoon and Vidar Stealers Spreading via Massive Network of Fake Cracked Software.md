---
title: Raccoon and Vidar Stealers Spreading via Massive Network of Fake Cracked Software
url: https://thehackernews.com/2023/01/raccoon-and-vidar-stealers-spreading.html
source: The Hacker News
date: 2023-01-17
fetch_date: 2025-10-04T04:05:28.029043
---

# Raccoon and Vidar Stealers Spreading via Massive Network of Fake Cracked Software

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

# [Raccoon and Vidar Stealers Spreading via Massive Network of Fake Cracked Software](https://thehackernews.com/2023/01/raccoon-and-vidar-stealers-spreading.html)

**Jan 16, 2023**Ravie LakshmananData Security / Cyber Threat

[![Fake Cracked Software](data:image/png;base64... "Fake Cracked Software")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqGHm2tKVqe1ygvC80UDqIRgjK8bT4henHVZbuLc4-u9FVP9kR8H2kfBAcb9xImph5q4sKSPqlrWW0hiTTWLzdaPPt6OFBUHw7JnZloHJ_M1SahpRx2mxnCloqVdOczbG7NETUqoAfluE3avm3-EDmrkc1xh9n8nTc9kjd0bM12DETyMHsWkBJf2WZ/s790-rw-e365/cracked-software.png)

A "large and resilient infrastructure" comprising over 250 domains is being used to distribute information-stealing malware such as [Raccoon](https://thehackernews.com/2022/12/new-malvertising-campaign-via-google.html) and [Vidar](https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html) since early 2020.

The infection chain "uses about a hundred of fake cracked software catalogue websites that redirect to several links before downloading the payload hosted on file share platforms, such as GitHub," cybersecurity firm SEKOIA [said](https://blog.sekoia.io/unveiling-of-a-large-resilient-infrastructure-distributing-information-stealers/) in an analysis published earlier this month.

The French cybersecurity company assessed the domains to be operated by a threat actor running a traffic direction system ([TDS](https://thehackernews.com/2022/04/over-16500-sites-hacked-to-distribute.html)), which allows other cybercriminals to rent the service to distribute their malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attacks target users searching for cracked versions of software and games on search engines like Google, surfacing fraudulent websites on top by leveraging a technique called search engine optimization (SEO) poisoning to lure victims into downloading and executing the malicious payloads.

The poisoned result comes with a download link to the promised software that, upon clicking, triggers a five-stage URL redirection sequence to take the user to a web page displaying a shortened link, which points to a password-protected RAR archive file hosted on GitHub, along with its password.

"Using several redirections complicates automated analysis by security solutions," the researchers said. "Carving the infrastructure as such is almost certainly designed to ensure resilience, making it easier and quicker to update or change a step."

[![Fake Cracked Software](data:image/png;base64... "Fake Cracked Software")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtYP1pWUx10U-odta1lTfRB_Wd9xDPOwbZKmtN2YEMW8HcaFosijzzuxH9ZkKmtbvFl8QfdOBSER-_rhBJUVkDPB331QxS73z5zU60wn06VrN0o7SKpcKW4lWRJIBWO6kx3arwr8Uuja_-jdQPAIQPGeO94XMzqnfrktYqaExySxCxzmULIHn2-Gtn/s790-rw-e365/chart.png)

Should the victim uncompress the RAR archive and run the purported setup executable contained within it, either of the two malware families, Raccoon or Vidar, are installed on the system.

The development comes as Cyble [detailed](https://blog.cyble.com/2023/01/12/rhadamanthys-new-stealer-spreading-through-google-ads/) a rogue Google Ads campaign that employs widely-used software such as AnyDesk, Bluestacks, Notepad++, and Zoom as lures to deliver a feature-rich stealer known as Rhadamanthys Stealer.

An alternate variant of the attack chain has been observed taking advantage of phishing emails masquerading as bank statements to dupe unwitting users into clicking on booby-trapped links.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Fabricated websites impersonating the popular remote desktop solution have also been put to use in the past to propagate a Python-based information stealer dubbed [Mitsu Stealer](https://blog.cyble.com/2022/10/13/mitsu-stealer-distributed-via-anydesk-phishing-site/).

Both pieces of malware are equipped to siphon a wide range of personal information from compromised machines, harvest credentials from web browsers, and steal data from various cryptocurrency wallets.

Users are advised to refrain from downloading pirated software and enforce multi-factor authentication wherever possible to harden accounts.

"It is crucial for users to exercise caution when receiving spam emails or to visit phishing websites and to verify the source before downloading any applications," the researchers said.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Raccoon](https://thehackernews.com/search/label/Raccoon)[Vidar](https://thehackernews.com/search/label/Vidar)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/0...