---
title: Grandoreiro Banking Trojan Resurfaces, Targeting Over 1,500 Banks Worldwide
url: https://thehackernews.com/2024/05/grandoreiro-banking-trojan-resurfaces.html
source: The Hacker News
date: 2024-05-20
fetch_date: 2025-10-06T16:49:41.501147
---

# Grandoreiro Banking Trojan Resurfaces, Targeting Over 1,500 Banks Worldwide

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

# [Grandoreiro Banking Trojan Resurfaces, Targeting Over 1,500 Banks Worldwide](https://thehackernews.com/2024/05/grandoreiro-banking-trojan-resurfaces.html)

**May 19, 2024**Ravie LakshmananBanking Troja / Email Security

[![Grandoreiro Banking Trojan](data:image/png;base64... "Grandoreiro Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5-kZvOVxoh88ywy2pxjyTedNazjZeTetG15AeVqaK0dpeege9CD6e2nGix7xcLI8J5RtixTt0_ADwR6weDe_DL8Zpy5P0W8PgKn5lk0SFi421tllqDPbFLTqy03f-EBXdNDL2FEoIBeqLQcEtMwUf9AH2XFER0KHuzr7EgmKXZEM-6P8C7gydaNIbRKgm/s790-rw-e365/bank.png)

The threat actors behind the Windows-based **Grandoreiro** banking trojan have returned in a global campaign since March 2024 following a law enforcement takedown in January.

The large-scale phishing attacks, likely facilitated by other cybercriminals via a malware-as-a-service (MaaS) model, target over 1,500 banks across the world, spanning more than 60 countries in Central and South America, Africa, Europe, and the Indo-Pacific, IBM X-Force said.

While [Grandoreiro](https://thehackernews.com/2022/08/new-grandoreiro-banking-malware.html) is known primarily for its focus in Latin America, Spain, and Portugal, the expansion is likely a shift in strategy after attempts to [shut down its infrastructure](https://thehackernews.com/2024/01/brazilian-feds-dismantle-grandoreiro.html) by Brazilian authorities.

Going hand-in-hand with the broader targeting footprint are significant improvements to the malware itself, which indicates active development.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Analysis of the malware revealed major updates within the string decryption and domain generating algorithm (DGA), as well as the ability to use Microsoft Outlook clients on infected hosts to spread further phishing emails," security researchers Golo Mühr and Melissa Frydrych [said](https://securityintelligence.com/x-force/grandoreiro-banking-trojan-unleashed/).

The attacks commence with phishing emails that instruct recipients to click on a link to view an invoice or make a payment depending on the nature of the lure and the government entity impersonated in the messages.

[![Grandoreiro Banking Trojan](data:image/png;base64... "Grandoreiro Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOn09YDLVaTyEh7cAZzUng_55NN8vPDLwbQYOluNqnzbkeo1VDr9NMcgY-JUw3YQSSDAY9XTjy6_X6dorgYcBum47CYh13l84h5c_UBVHFR0WeqlhLX9HvhbksfCjLcP94uPhcsU2Z7ZlF6Gh_5eWkxQLwedDec5UV8mZoi8a0oPALqQNXcz5Odv4Zrvb2/s790-rw-e365/dga.png)

Users who end up clicking on the link are redirected to an image of a PDF icon, ultimately leading to the download of a ZIP archive with the Grandoreiro loader executable.

The custom loader is artificially inflated to more than 100 MB to bypass anti-malware scanning software. It's also responsible for ensuring that the compromised host is not in a sandboxed environment, gathering basic victim data to a command-and-control (C2) server, and downloading and executing the main banking trojan.

It's worth pointing out that the verification step is also done to skip systems geolocated to Russia, Czechia, Poland, and the Netherlands, as well as Windows 7 machines based in the U.S. with no antivirus installed.

The trojan component begins its execution by establishing persistence via the Windows Registry, after which it employs a reworked DGA to establish connections with a C2 server to receive further instructions.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Grandoreiro supports a variety of commands that allow the threat actors to remotely commandeer the system, carry out file operations, and enable special modes, including a new module that gathers Microsoft Outlook data and abuses the victim's email account to blast spam messages to other targets.

"In order to interact with the local Outlook client, Grandoreiro uses the [Outlook Security Manager tool](https://www.add-in-express.com/outlook-security/), a software used to develop Outlook add-ins," the researchers said. "The main reason behind this is that the Outlook Object Model Guard triggers security alerts if it detects access on protected objects."

[![Grandoreiro Banking Trojan](data:image/png;base64... "Grandoreiro Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0fv5ncKjqwVGPBkhMQzzfwec9kmaotggrAfxOrrW-2KSsW183508dYIzY4n2f1DzRwbVnz9pzGQiSFxhbLbV_I-pnxcGx5zo-ZsxKbplOqtFYHS88VIBNelSgnpJhWb0H6TDVpWEAO8tTESK92iNBpeD6aYizXHsWWcaBeZ-OQlVlAwK2Q-OUgBMXD0K4/s790-rw-e365/banking.png)

"By using the local Outlook client for spamming, Grandoreiro can spread through infected victim inboxes via email, which likely contributes to the large amount of spam volume observed from Grandoreiro."

### Update

ESET, in a series of posts shared on X (formerly Twitter) on May 28, 2024, noted that the "disrupted Grandoreiro is different from the currently active Grandoreiro strain," giving it the moniker NewGrandoreiro. The new fork is said to have been active since at least December 2023, although it's currently not clear if it's operated by the same group.

"It is a major rewrite of the long-established Grandoreiro," the Slovakian cybersecurity company [said](https://x.com/ESETresearch/status/1795437280016154955). "And, most importantly, it appeared \*before\* the disruption."

"'NewGrandoreiro' employs a new custom downloader, a completely reworked DGA algorithm and has a significantly modified codebase. It uses slightly different binary padding. While command logic changed, the [command-and-control] protocol remained the same."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[*...