---
title: Malicious PyPI Package Targets MEXC Trading API to Steal Credentials and Redirect Orders
url: https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html
source: The Hacker News
date: 2025-04-16
fetch_date: 2025-10-06T22:09:57.055007
---

# Malicious PyPI Package Targets MEXC Trading API to Steal Credentials and Redirect Orders

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

# [Malicious PyPI Package Targets MEXC Trading API to Steal Credentials and Redirect Orders](https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html)

**Apr 15, 2025**Ravie LakshmananSupply Chain Attack / Malware

[![Malicious PyPI Package Targets](data:image/png;base64... "Malicious PyPI Package Targets")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJdXtd9Ylo6f1P7QljTiXFMQtpcro40XhEWP2qY_g_VXEW01JS6F4wUxcv49JRFFA1P8M2goWV3TIifA1y9TPFp8HEfYWb2SJawYrDFvPFQTYw3KTfJhZE-F3PaeTDxwOUWxCcwkHprd24UL_wsMjDDolLdOJ1XfthyphenhyphenV34-NMDq7b615BsRzFtwuYoKv-b/s790-rw-e365/python-malware.jpg)

Cybersecurity researchers have disclosed a malicious package uploaded to the Python Package Index (PyPI) repository that's designed to reroute trading orders placed on the [MEXC](https://www.mexc.co/) cryptocurrency exchange to a malicious server and steal tokens.

The package, ccxt-mexc-futures, purports to be an extension built on top of a popular Python library named [ccxt](https://pypi.org/project/ccxt/) (short for CryptoCurrency eXchange Trading), which is used to connect and trade with several cryptocurrency exchanges and facilitate payment processing services.

The malicious package is no longer available on PyPI, but statistics on pepy.tech shows that it has been downloaded at least [1,065 times](https://pepy.tech/projects/ccxt-mexc-futures).

"The authors of the malicious ccxt-mexc-futures package, claim in its README file that it extends the CCXT package to [support 'futures' trade](https://www.investopedia.com/terms/f/futures.asp) on MEXC," JFrog researcher Guy Korolevski [said](https://jfrog.com/blog/malicious-pypi-package-hijacks-mexc-orders-steals-crypto-tokens/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

However, a deeper examination of the library has revealed that it specifically overrides two APIs associated with the MEXC interface -- contract\_private\_post\_order\_submit and contract\_private\_post\_order\_cancel -- and introduces a new one named spot4\_private\_post\_order\_place.

In doing so, the idea is to trick developers into calling these API endpoints to create, cancel, or place a trading order on the MEXC exchange and stealthily perform malicious actions in the background.

The malicious modifications particularly target three different MEXC-related functions present in the original ccxt library, viz. ֵdescribe, sign, and prepare\_request\_headers.

This makes it possible to execute arbitrary code on the local machine on which the package is installed, effectively retrieving a JSON payload from a bogus domain impersonating MEXC ("v3.mexc.workers[.]dev"), which contains a configuration to direct the overridden APIs to a malicious third-party platform ("greentreeone[.]com") as opposed to the actual MEXC website.

"The package creates entries in the API for MEXC integration, using an API that directs requests to the domain greentreeone[.]com, and not the MEXC site mexc.com," Korolevski said.

"All requests are redirected to the domain set up by the attackers, allowing them to hijack all of the victim's crypto tokens and sensitive information transferred in the request, including API keys and secrets."

What's more, the fraudulent package is engineered to send the MEXC API key and secret key to the attacker-controlled domain whenever a request is sent to create, cancel, or place an order.

Users who have installed ccxt-mexc-futures are recommended to revoke any potentially compromised tokens and remove the package with immediate effect.

The development comes as Socket [revealed](https://socket.dev/blog/shell-usage) that threat actors are making use of counterfeit packages across npm, PyPI, Go, and Maven ecosystems to launch a reverse shell to maintain persistence and exfiltrate data.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Unsuspecting developers or organizations might inadvertently be including vulnerabilities or malicious dependencies in their code base, which could allow for sensitive data or system sabotage if undetected," the software supply chain security company said.

It also follows new research that delves into how large language models (LLMs) powering generative artificial intelligence (AI) tools could [endanger](https://vulcan.io/blog/ai-hallucinations-package-risk/) the [software supply chain](https://thehackernews.com/2024/04/ai-as-service-providers-vulnerable-to.html) by hallucinating non-existent packages and recommending them to developers.

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpstSlfO0l5Ysplva8A8DMlPf9feu2tqZgzx4puxQNJBcimYG0odZgHCUBnXjt_bJ-g3jbMY_zjqS48AA87Bitd-skc-PCBvCAQicQIOad1wcrdW0E5yadjGQ7p0dSnlsaIapMdCnQTUJVujfIFnkWYTrOSobBgMOAG0qh2aFgnmL1EWgMSY9t0-YhyaiV/s790-rw-e365/ai.png)

The [supply chain threat](https://thehackernews.com/2024/10/researchers-reveal-deceptive-delight.html) comes into play when malicious actors register and publish malware-laced packages with the hallucinated names to open-source repositories, infecting developer systems in the process – a technique referred to as [slopsquatting](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks).

The academic study [found](https://arxiv.org/abs/2406.10279) that "the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read mor...