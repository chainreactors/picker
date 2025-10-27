---
title: PyPI Python Library "aiocpa" Found Exfiltrating Crypto Keys via Telegram Bot
url: https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html
source: The Hacker News
date: 2024-11-26
fetch_date: 2025-10-06T19:26:22.446212
---

# PyPI Python Library "aiocpa" Found Exfiltrating Crypto Keys via Telegram Bot

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

# [PyPI Python Library "aiocpa" Found Exfiltrating Crypto Keys via Telegram Bot](https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html)

**Nov 25, 2024**Ravie LakshmananSoftware Supply Chain / Malware

[![Crypto Keys via Telegram Bot](data:image/png;base64... "Crypto Keys via Telegram Bot")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeJ5oQ86l0j222iIVUITZZT3yAHUBhpToQdOJiQxsxzwZ-nBzNBqMXJUa6V2yb8F-xUtbC0WecIrMT2LmXq6HDz96ALmv2IEfWZER1LdENzPIAhn8PJPR1gxRInjrD62wX2i-GMNTroA71nbAmcWC7LrAwxvwcnxbAjoBWKGAohZ29uVMCkNqWNZkofrH5/s790-rw-e365/python.png)

The administrators of the Python Package Index (PyPI) repository have quarantined the package "**aiocpa**" following a new update that included malicious code to exfiltrate private keys via Telegram.

The package in question is [described](https://pypi.org/project/aiocpa/) as a synchronous and asynchronous [Crypto Pay API](https://help.crypt.bot/crypto-pay-api) client. The package, originally released in September 2024, has been [downloaded 12,100 times](https://clickpy.clickhouse.com/dashboard/aiocpa) to date.

By putting the Python library in quarantine, it prevents further installation by clients and cannot be modified by its maintainers.

Cybersecurity outfit Phylum, which [shared](https://blog.phylum.io/python-crypto-library-updated-to-steal-private-keys/) details of the software supply chain attack last week, said the author of the package published the malicious update to PyPI, while keeping the library's [GitHub repository](https://github.com/vovchic17/aiocpa) clean in an attempt to evade detection.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's currently not clear if the original developer was behind the rogue update or if their credentials were compromised by a different threat actor.

Signs of malicious activity were first spotted in version 0.1.13 of the library, which included a change to the Python script "sync.py" that's designed to decode and run an obfuscated blob of code immediately after the package is installed.

[![Crypto Keys via Telegram Bot](data:image/png;base64... "Crypto Keys via Telegram Bot")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEin6LSHS5JcWhJZhVnpOnxhJK1ExcOMpqZ5Yhb9ESJ3hyphenhyphen43Bu7pQ1dAXQZ6K8ahtAVHluWs2FesR_zE6w-jttDA_gc23WOl7Vn17VgvovxeJlMOMUsTOyfqaqIfdM5Ufv6_k3Q5_6Eb9_QFNfMYxWS3QKXBLhbnS-8U2Qp7566wPUW1WXc_1ssb6VS0hyUb/s790-rw-e365/code.png)

"This particular blob is recursively encoded and compressed 50 times," Phylum said, adding it's used to capture and transmit the victim's Crypto Pay API token using a Telegram bot.

It's worth noting that Crypto Pay is advertised as a payment system based on [Crypto Bot](https://t.me/CryptoBot) (@CryptoBot) that allows users to accept payments in crypto and transfer coins to users using the API.

The incident is significant, not least because it highlights the importance of scanning the package's source code prior to downloading them, as opposed to just checking their associated repositories.

"As evidenced here, attackers can deliberately maintain clean source repos while distributing malicious packages to the ecosystems," the company said, adding the attack "serves as a reminder that a package's previous safety record doesn't guarantee its continued security."

### Update

[PyPI administrators](https://blog.pypi.org/posts/2024-11-25-aiocpa-attack-analysis/) and cybersecurity firm [ReversingLabs](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code) have also published their own analyses of the campaign, in addition to highlighting the malware author's [unsuccessful attempts to transfer ownership](https://github.com/pypi/support/issues/4682) of what they claimed was an abandoned package. The package aiocpa has since been formally removed from the PyPI repository.

"Unlike the majority of the attacks targeting open source repositories like npm and PyPI, the malicious actors behind aiocpa were not impersonating or typosquatting legitimate looking packages," ReversingLabs researcher Karlo Zanki said.

"Instead, they published their own crypto client tool in order to steadily attract a user base that would later be compromised through a malicious version update."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Phylum](https://thehackernews.com/search/label/Phylum)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[Telegram](https://thehackernews.com/search/label/Telegram)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com...