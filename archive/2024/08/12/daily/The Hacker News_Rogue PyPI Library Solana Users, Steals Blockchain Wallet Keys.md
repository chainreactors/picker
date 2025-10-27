---
title: Rogue PyPI Library Solana Users, Steals Blockchain Wallet Keys
url: https://thehackernews.com/2024/08/rogue-pypi-library-solana-users-steals.html
source: The Hacker News
date: 2024-08-12
fetch_date: 2025-10-06T18:02:28.071606
---

# Rogue PyPI Library Solana Users, Steals Blockchain Wallet Keys

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

# [Rogue PyPI Library Solana Users, Steals Blockchain Wallet Keys](https://thehackernews.com/2024/08/rogue-pypi-library-solana-users-steals.html)

**Aug 11, 2024**Ravie LakshmananSupply Chain / Software Security

[![Rogue PyPI Library](data:image/png;base64... "Rogue PyPI Library")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4sIhXPWrGL5LwJ7k9403Pl-nGF2zc4NLGLfzFi1QKvr5ENy7TCQt2tnmmSGNSQIqgSlQ4a4w3Ylhd5qAnChwowEhBtVOUjeVVvJHSUfXGNIOHQ2EnGmwXvEWmgUwhPZ7h16neVvax5aSfdpj6GL_Ipk3g3kQE_VVVAr4Wnie8gls2DAdWP25bvrSXYkIH/s790-rw-e365/python.jpg)

Cybersecurity researchers have discovered a new malicious package on the Python Package Index (PyPI) repository that masquerades as a library from the Solana blockchain platform but is actually designed to steal victims' secrets.

"The legitimate Solana Python API project is known as 'solana-py' on GitHub, but simply '[solana](https://pypi.org/project/solana/)' on the Python software registry, PyPI," Sonatype researcher Ax Sharma [said](https://www.sonatype.com/blog/an-ideal-pypi-typosquat-solana-py-is-here-to-steal-your-crypto-keys) in a report published last week. "This slight naming discrepancy has been leveraged by a threat actor who published a 'solana-py' project on PyPI."

The malicious "solana-py" package attracted a total of [1,122 downloads](https://www.pepy.tech/projects/solana-py) since it was published on August 4, 2024. It's no longer available for download from PyPI.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The most striking aspect of the library is that it carried the version numbers 0.34.3, 0.34.4, and 0.34.5. The latest version of the legitimate "solana" package is 0.34.3. This clearly indicates an attempt on the part of the threat actor to trick users looking for "solana" into inadvertently downloading "solana-py" instead.

What's more, the rogue package borrows the real code from its counterpart, but injects additional code in the "\_\_init\_\_.py" script that's responsible for harvesting Solana blockchain wallet keys from the system.

This information is then exfiltrated to a [Hugging Face Spaces domain](https://thehackernews.com/2024/06/ai-company-hugging-face-notifies-users.html) operated by the threat actor ("treeprime-gen.hf[.]space"), once again underscoring how threat actors are abusing [legitimate services](https://www.sonatype.com/blog/open-source-ml/ai-models-attackers-next-potential-target) for malicious purposes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYVckpkhjE6s-r87Z25YpwxPBUFkY-wYcQL3mbLMzk_3KIWuPe2TACJQwNR7PlX6MqAxYo0UEM8r1wHm2MzCirn2eX1Y5LYRTAnC9fXMPlMkJ8C2NESHoLcaX0BRsxVw6biaA0nDJdfUennWwoRKB6BBWEPVqUi7iGlqIslN2rlXD4MLqWApuh4FpKtT7G/s790-rw-e365/pip.png)

The attack campaign poses a supply chain risk in that Sonatype's investigation found that legitimate libraries like "solders" make references to "solana-py" in their [PyPI documentation](https://pypi.org/project/solders/#description), leading to a scenario where developers could have mistakenly downloaded "solana-py" from PyPI and broadened the attack surface.

"In other words, if a developer using the legitimate 'solders' PyPI package in their application is mislead (by solders' documentation) to fall for the typosquatted 'solana-py' project, they'd inadvertently introduce a crypto stealer into their application," Sharma explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This would not only steal their secrets, but those of any user running the developer's application."

The disclosure comes as Phylum said it identified hundreds of thousands of spam npm packages on the registry containing markers of Tea protocol abuse, a campaign that [first came to light](https://thehackernews.com/2024/04/beware-githubs-fake-popularity-scam.html) in April 2024.

"The Tea protocol project is [taking steps](https://tea.xyz/blog/proof-of-contribution) to remediate this problem," the supply chain security firm [said](https://blog.phylum.io/the-great-npm-garbage-patch/). "It would be unfair to legitimate participants in the Tea protocol to have their remuneration reduced because others are scamming the system. Also, npm has begun to [take down some of these spammers](https://github.com/advisories?query=type%3Amalware+zitterorg), but the takedown rate does not match the new publication rate."

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

[Blockchain Security](https://thehackernews.com/search/label/Blockchain%20Security)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Developer Tools](https://thehackernews.com/search/label/Developer%20Tools)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Python)[software development](https://thehackernews.com/search/label/software%20development)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20In...