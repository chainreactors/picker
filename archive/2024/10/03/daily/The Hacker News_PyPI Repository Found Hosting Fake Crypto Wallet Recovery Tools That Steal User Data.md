---
title: PyPI Repository Found Hosting Fake Crypto Wallet Recovery Tools That Steal User Data
url: https://thehackernews.com/2024/10/pypi-repository-found-hosting-fake.html
source: The Hacker News
date: 2024-10-03
fetch_date: 2025-10-06T18:56:15.395797
---

# PyPI Repository Found Hosting Fake Crypto Wallet Recovery Tools That Steal User Data

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

# [PyPI Repository Found Hosting Fake Crypto Wallet Recovery Tools That Steal User Data](https://thehackernews.com/2024/10/pypi-repository-found-hosting-fake.html)

**Oct 02, 2024**The Hacker NewsSupply Chain Attack / Cryptocurrency

[![Fake Crypto Wallet Recovery Tools](data:image/png;base64... "Fake Crypto Wallet Recovery Tools")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQQmlA-GTYop8VEY4RJmHttP8AaVUNCW7RXrdpJedI80Xiv0p-vYAo8xDgdw6M0oh7b6m63d5YkpVbDUOsixLzE71mOPpC85qqi2I-siAFux_FoI3lnsDy3oxnV0n6TLmidx4_LIKrIxlbJrXKRrtMXQnzWvBr-cL9FacwTqHF9jzsp_llFx57KBg3ggk/s790-rw-e365/stealer.png)

A new set of malicious packages has been unearthed in the Python Package Index (PyPI) repository that masqueraded as cryptocurrency wallet recovery and management services, only to siphon sensitive data and facilitate the theft of valuable digital assets.

"The attack targeted users of Atomic, Trust Wallet, Metamask, Ronin, TronLink, Exodus, and other prominent wallets in the crypto ecosystem," Checkmarx researcher Yehuda Gelb [said](https://checkmarx.com/blog/crypto-stealing-code-lurking-in-python-package-dependencies/) in a Tuesday analysis.

"Presenting themselves as utilities for extracting mnemonic phrases and decrypting wallet data, these packages appeared to offer valuable functionality for cryptocurrency users engaged in wallet recovery or management."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

However, they harbor functionality to steal private keys, mnemonic phrases, and other sensitive wallet data, such as transaction histories or wallet balances. Each of the packages attracted hundreds of downloads prior to them being taken down -

* [atomicdecoderss](https://www.pepy.tech/projects/atomicdecoderss) (366 downloads)
* [trondecoderss](https://www.pepy.tech/projects/trondecoderss) (240 downloads)
* [phantomdecoderss](https://www.pepy.tech/projects/phantomdecoderss) (449 downloads)
* [trustdecoderss](https://www.pepy.tech/projects/trustdecoderss) (466 downloads)
* [exodusdecoderss](https://www.pepy.tech/projects/exodusdecoderss) (422 downloads)
* [walletdecoderss](https://www.pepy.tech/projects/walletdecoderss) (232 downloads)
* [ccl-localstoragerss](https://www.pepy.tech/projects/ccl-localstoragerss) (335 downloads)
* [exodushcates](https://www.pepy.tech/projects/exodushcates) (415 downloads)
* [cipherbcryptors](https://www.pepy.tech/projects/cipherbcryptors) (450 downloads)
* [ccl\_leveldbases](https://www.pepy.tech/projects/ccl_leveldbases) (407 downloads)

Checkmarx said the packages were named so in a deliberate attempt to lure developers working in the cryptocurrency ecosystem. In a further attempt to lend legitimacy to the libraries, the package descriptions on PyPI came with installation instructions, usage examples, and in one case, even "best practices" for virtual environments.

[![Fake Crypto Wallet Recovery Tools](data:image/png;base64... "Fake Crypto Wallet Recovery Tools")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKOyjYMH6F_C9W0ysteG3NyDZIYrHyt-8yVaEMFUUmqgcGzwwHjdNX-SNZyKXob8Gy9lZQxaTn2V_-LIqk9lqIuFlR9Wi3J_3bbLWMIOkrLSjwZ8btHrnw4l2NLUMDoYGLluvNOYbsrxre8rD7vbXwR3J5_RSTz1zQThPcnaP64c5myp9XkpKU7JEDTLM/s790-rw-e365/python.png)

The deception didn't stop there, for the threat actor behind the campaign also managed to display fake download statistics, giving users the impression that the packages were popular and trustworthy.

Six of the identified PyPI packages included a dependency called cipherbcryptors to execute the malicious, while a few others relied on an additional package named ccl\_leveldbases in an apparent effort to obfuscate the functionality.

A notable aspect of the packages is that the malicious functionality is triggered only when certain functions are called, marking a denture from the typical pattern where such behavior would be activated automatically upon installation. The captured data is then exfiltrated to a remote server.

"The attacker employed an additional layer of security by not hard-coding the address of their command and control server within any of the packages," Gelb said. "Instead, they used external resources to retrieve this information dynamically."

This technique, called [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/), gives the attackers the flexibility to update the server information without having to push out an update to the packages themselves. It also makes the process of switching to a different infrastructure easy should the servers be taken down.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The attack exploits the trust in open-source communities and the apparent utility of wallet management tools, potentially affecting a broad spectrum of cryptocurrency users," Gelb said.

"The attack's complexity – from its deceptive packaging to its dynamic malicious capabilities and use of malicious dependencies – highlights the importance of comprehensive security measures and continuous monitoring."

The development is just the latest in a series of malicious campaigns targeting the cryptocurrency sector, with threat actors constantly on the lookout for new ways to drain funds from victim wallets.

[![PyPI Repository](data:image/png;base64... "PyPI Repository")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVB2l_0EvetiCNF-ahhm9p1OFJqZpUXPBfSQsgkdAtCzMqARNdzjYDnYz7M6EaukyJWO1skD7Os3bZ6t9Vi1hGlJnOI-1ZxFmlDqlyG7ar28SX9HrAewBArdGbI1JddYBRN6HRdeWNcL6YHKnoEpgO8_Mxa4tLeU0_eIFDIDisdeBCVOzqnKOVo2GsHeQ/s790-rw-e365/scam.png)

In August 2024, details emerged of a sophisticated cryptocurrency scam operation dubbed CryptoCore that involves using fake videos or hijacked accounts on social media platforms like Facebook, Twitch, X, and YouTube to lure users into parting with their cryptocurrency assets under the guise of quick and easy profits.

"This scam group and its giveaway campaigns leverage deepfake technology, hijacked YouTub...