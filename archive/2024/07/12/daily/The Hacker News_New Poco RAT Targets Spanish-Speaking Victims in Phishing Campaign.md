---
title: New Poco RAT Targets Spanish-Speaking Victims in Phishing Campaign
url: https://thehackernews.com/2024/07/new-poco-rat-targets-spanish-speaking.html
source: The Hacker News
date: 2024-07-12
fetch_date: 2025-10-06T17:46:33.697458
---

# New Poco RAT Targets Spanish-Speaking Victims in Phishing Campaign

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

# [New Poco RAT Targets Spanish-Speaking Victims in Phishing Campaign](https://thehackernews.com/2024/07/new-poco-rat-targets-spanish-speaking.html)

**Jul 11, 2024**Ravie LakshmananMalware / Threat Intelligence

[![Phishing Campaign](data:image/png;base64... "Phishing Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj8LNcwmw4vq8SCQBtv0NpgGBZ8g_CrX7-ST2zE7JT_9wAu6TpmypPXtABiWYJvpDfgzQJf4wD3OCiB3KENkqusLzhyphenhyphenpUU-8z59dU2xT3JdgwYTUfyUvoa1i2Rmp2bQjT5dwqFh2n_SqdzDxad2cRDQ2qugqW_Surlw8BJLnM_N7HOPVSEx9fIKWbBxzv3/s790-rw-e365/phishing.png)

Spanish language victims are the target of an email phishing campaign that delivers a new remote access trojan (RAT) called **Poco RAT** since at least February 2024.

The attacks primarily single out mining, manufacturing, hospitality, and utilities sectors, according to cybersecurity company Cofense.

"The majority of the custom code in the malware appears to be focused on anti-analysis, communicating with its command-and-control center (C2), and downloading and running files with a limited focus on monitoring or harvesting credentials," it [said](https://cofense.com/blog/new-malware-campaign-targeting-spanish-language-victims/).

Infection chains begin with phishing messages bearing finance-themed lures that trick recipients into clicking on an embedded URL pointing to a 7-Zip archive file hosted on Google Drive.

Other methods observed include the use of HTML or PDF files directly attached to the emails or downloaded via another embedded Google Drive link. The abuse of legitimate services by threat actors is not a new phenomenon as it allows them to bypass secure email gateways (SEGs).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The HTML files propagating Poco RAT, in turn, contain a link that, upon clicking, leads to the download of the archive containing the malware executable.

"This tactic would likely be more effective than simply providing a URL to directly download the malware as any SEGs that would explore the embedded URL would only download and check the HTML file, which would appear to be legitimate," Cofense noted.

The PDF files are no different in that they also contain a Google Drive link that harbors Poco RAT.

Once launched, the Delphi-based malware establishes persistence on the compromised Windows host and contacts a C2 server in order to deliver additional payloads. It's so named owing to its use of the [POCO C++ Libraries](https://pocoproject.org/).

The use of Delphi is a sign that the unidentified threat actors behind the campaign are focusing on Latin America, which is [known](https://thehackernews.com/2024/03/new-banking-trojan-chavecloak-targets.html) to be targeted by banking trojans written in the programming language.

[![Phishing Campaign](data:image/png;base64... "Phishing Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVsDLPY953vWwbW36Ufr2vhLt5Ti6Z3cEGxI0t4CbrPozqO987MVE7QBNCi3wnLrmGxRsv3x7GF0qfoi3AumN1vPzZFXH6u1hBm9HNsVEGY8mo4gVNdvWZpfw9pN9qE0SpISidhM7DES7KE8LMRZ9vWVf7pVSiVfQwBAouJ1BOexL6_QEYIZsC4y43B7kt/s790-rw-e365/cofense.png)

This connection is strengthened by the fact that the C2 server does not respond to requests originating from infected computers that are not geolocated to the region.

The development comes as malware authors are [increasingly using](https://blog.sonicwall.com/en-us/2024/07/the-hidden-danger-of-pdf-files-with-embedded-qr-codes/) QR codes embedded with PDF files to trick users into visiting phishing pages that are designed to harvest Microsoft 365 login credentials.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It also follows social engineering campaigns that use deceptive sites advertising popular software to deliver malware such as RATs and information stealers like [AsyncRAT](https://www.esentire.com/blog/exploring-the-infection-chain-screenconnects-link-to-asyncrat-deployment) and [RisePro](https://blogs.blackberry.com/en/2024/06/threat-analysis-insight-risepro-information-stealer).

Similar data theft attacks have also targeted internet users in India with bogus SMS messages falsely claiming of package delivery failures and instructing them to click on a provided link to update their details.

The SMS phishing campaign has been attributed to a Chinese-speaking threat actor called [Smishing Triad](https://thehackernews.com/2024/06/grandoreiro-banking-trojan-hits-brazil.html), which has a history of using compromised or purposefully registered Apple iCloud accounts (e.g., "fredyma514@hlh-web.de") to send smishing messages for carrying out financial fraud.

"The actors registered domain names impersonating the India Post around June, but were not actively using them, likely preparing for a large-scale activity, which became visible by July," Resecurity [said](https://www.resecurity.com/blog/article/smishing-triad-is-targeting-india-to-steal-personal-and-payment-data-at-scale). "The goal of this campaign is to steal massive amounts of personal identifiable information (PII) and payment data."

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

[Cybercrime](https://thehackernews.com/search/...