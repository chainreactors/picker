---
title: Researchers Uncover Python Package Targeting Crypto Wallets with Malicious Code
url: https://thehackernews.com/2024/10/researchers-uncover-python-package.html
source: The Hacker News
date: 2024-10-31
fetch_date: 2025-10-06T18:58:12.630927
---

# Researchers Uncover Python Package Targeting Crypto Wallets with Malicious Code

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

# [Researchers Uncover Python Package Targeting Crypto Wallets with Malicious Code](https://thehackernews.com/2024/10/researchers-uncover-python-package.html)

**Oct 30, 2024**Ravie LakshmananCybercrim / Cryptocurrency

[![Python Package](data:image/png;base64... "Python Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqyNGfwG8y-bN2mGRe0dRlWQk77HWdEAiAqzPxJy0RxO0f_3i-dirfPcBDIlehgM6AUsA_LA2JAKuZTMgvlMNt290G5yJc9Wy_bKso4XOkpG4smVopDaRj4xbmLacVYhJh4gjRTrjtlcSfQvHG8vhfMFtF_nlOo0yMcno-cQuq_e33dLCVlWmxmQt6D3wY/s790-rw-e365/python.png)

Cybersecurity researchers have discovered a new malicious Python package that masquerades as a cryptocurrency trading tool but harbors functionality designed to steal sensitive data and drain assets from victims' crypto wallets.

The package, named "CryptoAITools," is said to have been distributed via both Python Package Index (PyPI) and bogus GitHub repositories. It was [downloaded](https://secure.software/pypi/packages/CryptoAiTools) over 1,300 times before being taken down from PyPI.

"The malware activated automatically upon installation, targeting both Windows and macOS operating systems," Checkmarx [said](https://checkmarx.com/blog/cryptocurrency-enthusiasts-targeted-in-multi-vector-supply-chain-attack/) in a new report shared with The Hacker News. "A deceptive graphical user interface (GUI) was used to distract vic4ms while the malware performed its malicious ac4vi4es in the background."

The package is designed to unleash its malicious behavior immediately after installation through code injected into its "\_\_init\_\_.py" file that first determines if the target system is Windows or macOS in order to execute the appropriate version of the malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Present within the code is a helper functionality that's responsible for downloading and executing additional payloads, thereby kicking-off a multi-stage infection process.

Specifically, the payloads are downloaded from a fake website ("[coinsw[.]app](https://urlscan.io/result/073a83b8-c7c6-497b-bc4a-472533845194/)") that advertises a cryptocurrency trading bot service, but is in fact an attempt to give the domain a veneer of legitimacy should a developer decide to navigate to it directly on a web browser.

This approach not only helps the threat actor evade detection, but also allows them to expand the malware's capabilities at will by simply modifying the payloads hosted on the legitimate-looking website.

A notable aspect of the infection process is the incorporation of a GUI component that serves to distract the victims by means of a fake setup process while the malware is covertly harvesting sensitive data from the systems.

[![Python Package](data:image/png;base64... "Python Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiU4vbJ1QcGOR-sdTJx0FJziFES3wxhjGwFpOSN8SFro1Ygq334xVs8x63oCoX2SdD8pE52ITUXxpUBVT6FQbwdFXO4t8N5reE_S-2lu4bmjfzFPoUIKShtvblX48mB0Q-bJgl-qQcPcnSBC1G0flslYwPw0AUNFzdBQACH5Ks4KBJEKfF0euwBQrmlUzjx/s790-rw-e365/package.png)

"The CryptoAITools malware conducts an extensive data theft operation, targeting a wide range of sensitive information on the infected system," Checkmarx said. "The primary goal is to gather any data that could aid the attacker in stealing cryptocurrency assets."

This includes data from cryptocurrency wallets (Bitcoin, Ethereum, Exodus, Atomic, Electrum, etc.), saved passwords, cookies, browsing history, cryptocurrency extensions, SSH keys, files stored in Downloads, Documents, Desktop directories that reference cryptocurrencies, passwords, and financial information, and Telegram.

On Apple macOS machines, the stealer also takes the step of collecting data from Apple Notes and Stickies apps. The gathered information is ultimately uploaded to the gofile[.]io file transfer service, after which the local copy is deleted.

Checkmarx said it also discovered the threat actor distributing the same stealer malware through a GitHub repository named [Meme Token Hunter Bot](https://github.com/CryptoAiBots/Meme-Token-Hunter-Bot) that claims to be "an AI-powered trading bot that lists all meme tokens on the Solana network and performs real-time trades once they are deemed safe."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This indicates that the campaign is also targeting cryptocurrency users who opt to clone and run the code directly from GitHub. The repository, which is still active as of writing, has been forked once and starred 10 times.

Also managed by the operators is a Telegram channel that promotes the aforementioned GitHub repository, as well as offers monthly subscriptions and technical support.

"This multi-platform approach allows the attacker to cast a wide net, potentially reaching victims who might be cautious about one platform but trust another," Checkmarx said.

"The CryptoAITools malware campaign has severe consequences for victims and the broader cryptocurrency community. Users who starred or forked the malicious 'Meme-Token-Hunter-Bot' repository are potential victims, significantly expanding the attack's reach."

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
[*...