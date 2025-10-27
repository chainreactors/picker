---
title: Malicious PyPI Package "automslc" Enables 104K+ Unauthorized Deezer Music Downloads
url: https://thehackernews.com/2025/02/malicious-pypi-package-automslc-enables.html
source: The Hacker News
date: 2025-02-27
fetch_date: 2025-10-06T21:55:37.031819
---

# Malicious PyPI Package "automslc" Enables 104K+ Unauthorized Deezer Music Downloads

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

# [Malicious PyPI Package "automslc" Enables 104K+ Unauthorized Deezer Music Downloads](https://thehackernews.com/2025/02/malicious-pypi-package-automslc-enables.html)

**Feb 26, 2025**Ravie LakshmananMalware / Cryptocurrency

[![Deezer Music Downloads](data:image/png;base64... "Deezer Music Downloads")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRKtiUS0GzSS_JsBkS89D1avV_OtQ891_OquTs0uqNMExpvKKcKT7easvadhvJHLIbBhGFpNhasIJNt3wz7rIoN1fkDYaWHSJ9yuBBrJdPaMe3T7NTaQcCvxbT7UOKkVm0W_QRsDEiW7jqh-QTNRKPhbhNCk8YPpPdjbkNZ4aFNdMWOS4o2Kj258KCO_Wp/s790-rw-e365/malware.png)

Cybersecurity researchers have flagged a malicious Python library on the Python Package Index (PyPI) repository that facilitates unauthorized music downloads from music streaming service Deezer.

The package in question is automslc, which has been downloaded over 104,000 times to date. First published in May 2019, it [remains available](https://pypi.org/project/automslc/) on PyPI as of writing.

"Although automslc, which has been [downloaded](https://pepy.tech/projects/automslc) over 100,000 times, purports to offer music automation and metadata retrieval, it covertly bypasses Deezer's access restrictions by embedding hardcoded credentials and communicating with an external command-and-control (C2) server," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-pypi-package-exploits-deezer-api-for-coordinated-music-piracy) in a report published today.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Specifically, the package is designed to log into the French music streaming platform via user-supplied and hard-coded credentials, gather track-related metadata, and download full audio files in violation of Deezer's API terms.

The package also periodically communicates with a remote server located at "54.39.49[.]17:8031" to provide updates on the download status, thereby giving the threat actor centralized control over the coordinated music piracy operation.

Put differently, automslc effectively turns the systems of the package users into an illicit network for facilitating bulk music downloads in an unauthorized manner. The IP address is associated with a domain named "automusic[.]win," which is said to be used by the threat actor to oversee the distributed downloading operation.

[![Deezer Music Downloads](data:image/png;base64... "Deezer Music Downloads")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7Trs7VUtWhGZ1s_uh9QrHLj4HzdkdiM3CzDr50vP179IWfB91jqN8ZJJ2k7yc8POZL_uiqcbs78c-NnGswjGzoeqigUulA66ibU_TWPOub6XyofA2phCrY8EiMaNZG7JlXxDd1bd-A7u_u5DdQqXrmK_tbuEdtfy0cUv8IhKd4lA_1AH0fUBw4JfXpBM_/s790-rw-e365/malware.png)

"Deezer's API terms forbid the local or offline storage of complete audio content, but by downloading and decrypting entire tracks, automslc bypasses this limitation, potentially placing users at risk of legal repercussions," Boychenko said.

The disclosure comes as the software supply chain security company detailed a rogue npm package called @ton-wallet/create that has been found stealing [mnemonic phrases](https://thehackernews.com/2024/03/watch-out-these-pypi-python-packages.html) from unsuspecting users and developers in the TON ecosystem, while impersonating the legitimate @ton/ton package.

The package, [first published](https://www.npmjs.com/package/%40ton-wallet/create) to the npm registry in August 2024, has attracted [584 downloads](https://npm-stat.com/charts.html?package=%40ton-wallet%2Fcreate) to date. It remains available for download.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The malicious functionality embedded into the library is capable of extracting the process.env.MNEMONIC environment variable, thereby giving threat actors complete access to a cryptocurrency wallet and potentially drain a victim's digital assets. The information is transmitted to an attacker-controlled Telegram bot.

"This attack poses severe supply chain security risks, targeting developers and users integrating TON wallets into their applications," Socket [said](https://socket.dev/blog/ton-wallet-security-threat-malicious-npm-package-steals-cryptocurrency-wallet-keys). "Regular dependency audits and automated scanning tools should be employed to detect anomalous or malicious behaviors in third-party packages before they are integrated into production environments."

### Update

The Python package "automslc" is no longer available for download from PyPI.

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Digital Piracy](https://thehackernews.com/search/label/Digital%20Piracy)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Python)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[Threat Intelligence](https://t...