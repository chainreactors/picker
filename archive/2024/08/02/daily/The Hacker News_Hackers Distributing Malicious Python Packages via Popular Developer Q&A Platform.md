---
title: Hackers Distributing Malicious Python Packages via Popular Developer Q&A Platform
url: https://thehackernews.com/2024/08/hackers-distributing-malicious-python.html
source: The Hacker News
date: 2024-08-02
fetch_date: 2025-10-06T18:07:26.084326
---

# Hackers Distributing Malicious Python Packages via Popular Developer Q&A Platform

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

# [Hackers Distributing Malicious Python Packages via Popular Developer Q&A Platform](https://thehackernews.com/2024/08/hackers-distributing-malicious-python.html)

**Aug 01, 2024**Ravie LakshmananMalware / Developer Security

[![Python Packages](data:image/png;base64... "Python Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTWOhYPMK5s_mOHnqsux82Yn3yBGcMq9oLB_KjkrP3lnJBmz6YsDKtnOP1lQw9DJtf0g9ufeTXtMoZIBfIyb2lnYPAS7ptIoeflOeFt7vcTjs7RDVriB18cK7KbV5Ps8yl3RxiK63sTW0ITtd8KTmiv-tmcbJ3F8S_koaAOjbUrvWNAcEC-vzYAUwyXm0t/s790-rw-e365/stack.png)

In yet another sign that threat actors are always looking out for new ways to trick users into downloading malware, it has come to light that the question-and-answer (Q&A) platform known as Stack Exchange has been abused to direct unsuspecting developers to bogus Python packages capable of draining their cryptocurrency wallets.

"Upon installation, this code would execute automatically, setting in motion a chain of events designed to compromise and control the victim's systems, while also exfiltrating their data and draining their crypto wallets," Checkmarx researchers Yehuda Gelb and Tzachi Zornstain said in a [report](https://checkmarx.com/blog/stackexchange-abused-to-spread-malicious-python-package-that-drains-victims-crypto-wallets/) shared with The Hacker News.

The campaign, which began on June 25, 2024, specifically singled out cryptocurrency users involved with Raydium and Solana. The list of rogue packages uncovered as part of the activity is listed below -

* [raydium](https://www.pepy.tech/projects/raydium) (762 downloads)
* [raydium-sdk](https://www.pepy.tech/projects/raydium-sdk) (137 downloads)
* [sol-instruct](https://www.pepy.tech/projects/sol-instruct) (115 downloads)
* [sol-structs](https://www.pepy.tech/projects/sol-structs) (292 downloads)
* [spl-types](https://www.pepy.tech/projects/spl-types) (776 downloads)

The packages have been collectively downloaded 2,082 times. They are no longer available for download from the Python Package Index (PyPI) repository.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware concealed within the package served a full-fledged information stealer, casting a wide net of data, including web browser passwords, cookies, and credit card details, cryptocurrency wallets, and information associated with messaging apps like Telegram, Signal, and Session.

It also packed in capabilities to capture screenshots of the system, and search for files containing GitHub recovery codes and BitLocker keys. The gathered information was then compressed and exfiltrated to two different Telegram bots maintained by the threat actor.

Separately, a backdoor component present in the malware granted the attacker persistent remote access to victims' machines, enabling potential future exploits and long-term compromise.

The attack chain spans multiple stages, with the "raydium" package listing "spl-types" as a dependency in an attempt to conceal the malicious behavior and give users the impression that it was legitimate.

A notable aspect of the campaign is the use of Stack Exchange as a vector to drive adoption by posting ostensibly helpful answers referencing the package in question to [developer questions](https://solana.stackexchange.com/questions/8647/how-to-perform-a-swap-transaction-in-raydium-with-python) related to performing swap transactions in Raydium using Python.

[![Python Packages](data:image/png;base64... "Python Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK2dEHZH4ttyuT33IDpxMZR65gcqEPPqH0haOyH21fMzmCclkYcoJ_hyphenhyphenhjz_mhHy3xV6QjQT0xebJ6lTUprK5XvggPwZk_PlxgSvGgHAstNUUd0gB7qkiLmZeQAs8_MbRG3D-_MxchyphenhyphenU7Eu8inuW1xhW2_QgIEdEz5cnU9UP0MkSoci9MhFAy51fS_FAQW/s790-rw-e365/aa.png)

"By choosing a thread with high visibility — garnering thousands of views—the attacker maximized their potential reach," the researchers said, adding it was done so to "lend credibility to this package and ensure its widespread adoption."

While the answer no longer exists on Stack Exchange, The Hacker News found references to "raydium" in another [unanswered question](https://solana.stackexchange.com/questions/15305/how-can-i-swap-solana-token-in-python) posted on the Q&A site dated July 9, 2024: "I have been struggling for nights to get a swap on solana network running in python 3.10.2 installed solana, solders and Raydium but I can't get it to work," a user said.

References to "raydium-sdk" have also [surfaced](https://medium.com/%40SolScribe/how-to-buy-and-sell-tokens-on-raydium-using-python-a-step-by-step-solana-guide-5fa2a2196ce5) in a post titled "How to Buy and Sell Tokens on Raydium using Python: A Step-by-Step Solana Guide" that was shared by a user named SolanaScribe on the social publishing platform Medium on June 29, 2024.

It's currently not clear when the packages were removed from PyPI, as two other users have responded to the Medium post seeking help from the author about installing "raydium-sdk" as recently as July 27, 2024. Checkmarx told The Hacker News that the post is not the work of the threat actor.

This is not the first time bad actors have resorted to such a malware distribution method. Earlier this May, Sonatype [revealed](https://thehackernews.com/2024/05/cybercriminals-abuse-stackoverflow-to.html) how a package named pytoileur was promoted via another Q&A service called Stack Overflow to facilitate cryptocurrency theft.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

If anything, the development is evidence that attackers are leveraging trust in these community-driven platforms to push malware, leading to large-scale supply chain attacks.

"A single compromised developer can inadvertently introduce vulnerabilities into an entire company's software ecosystem, potentially affecting the whole corporate network," the researchers said. "This attack serves as a wake-up call for both individuals and...