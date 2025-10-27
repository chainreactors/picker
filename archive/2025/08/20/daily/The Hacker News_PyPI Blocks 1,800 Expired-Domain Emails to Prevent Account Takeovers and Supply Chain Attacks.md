---
title: PyPI Blocks 1,800 Expired-Domain Emails to Prevent Account Takeovers and Supply Chain Attacks
url: https://thehackernews.com/2025/08/pypi-blocks-1800-expired-domain-emails.html
source: The Hacker News
date: 2025-08-20
fetch_date: 2025-10-07T00:50:38.500299
---

# PyPI Blocks 1,800 Expired-Domain Emails to Prevent Account Takeovers and Supply Chain Attacks

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

# [PyPI Blocks 1,800 Expired-Domain Emails to Prevent Account Takeovers and Supply Chain Attacks](https://thehackernews.com/2025/08/pypi-blocks-1800-expired-domain-emails.html)

**Aug 19, 2025**Ravie LakshmananSupply Chain Security

[![Expired-Domain Emails](data:image/png;base64... "Expired-Domain Emails")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTEoI3KmKmfXUu9hlkrCmfO0uo4AoCmomDPVSCYVEitWAqZzFRWcTYgodijTVen7NLHkgxjXyK3YMBqkgoV9c86OmmVUZ2682Fbr8MkBl28dPDvD6Cx_Fels_7UGa9l9Zw-I_ZTHTmo_HIjgDCSDSynsq3sqkgUJ3civRTHzP5R4oiSArTcTw_wOXzohxK/s790-rw-e365/pypi.jpg)

The maintainers of the Python Package Index (PyPI) repository have announced that the package manager now checks for expired domains to prevent supply chain attacks.

"These changes improve PyPI's overall account security posture, making it harder for attackers to exploit expired domain names to gain unauthorized access to accounts," Mike Fiedler, PyPI safety and security engineer at the Python Software Foundation (PSF), [said](https://blog.pypi.org/posts/2025-08-18-preventing-domain-resurrections/).

With the latest update, the intention is to tackle domain resurrection attacks, which occur when bad actors purchase an expired domain and use it to take control of PyPI accounts through password resets.

PyPI said it has unverified over 1,800 email addresses since early June 2025, as soon as their associated domains entered expiration phases. While this is not a foolproof solution, it helps plug a significant supply chain attack vector that would otherwise appear legitimate and hard to detect, it added.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Email addresses are tied to domain names that, in turn, can lapse, if left unpaid – a critical risk for packages distributed via open-source registries. The threat is magnified if those packages have long been abandoned by their respective maintainers, but still enjoy a fair amount of use by downstream developers.

PyPI users are required to verify their email addresses during the account registration phase, thus ensuring that the provided addresses are valid and accessible to them. But this layer of defense is effectively neutralized should the domain expire, thus allowing an attacker to purchase the same domain and initiate a password reset request, which would land in their inbox (as opposed to the actual owner of the package).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYLaDz6mYnCgsNUdYBacsNGrQWw01-ImvWY3wBaRuaVZw-Y7A4hmABc05JvwAHYr2k-QmacIPxDY1BIlNqsrWlmCZiJWHjNPWX8OUauzenVLZPdsSsaTcVPyUygpJSI7V5XpmupzoO0TMXKdiyN2QKocElU6bJcwfVxllrF0KaoVWqaB_1b8Ww8JJ14YAm/s790-rw-e365/python-chart.jpg)

From there, all the threat actor has to do is follow through the steps to gain access to the account with that domain name. The threat posed by expired domains [arose in 2022](https://thehackernews.com/2022/05/pypi-package-ctx-and-php-library-phpass.html), when an unknown attacker acquired the domain used by the maintainer of the ctx PyPI package to gain access to the account and publish rogue versions to the repository.

The latest safeguard added by PyPI aims to prevent this kind of account takeover (ATO) scenario and "minimize potential exposure if an email domain does expire and change hands, regardless of whether the account has 2FA enabled." It's worth noting that the attacks are only applicable to accounts that have registered using email addresses with a custom domain name.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

PyPI said it's making use of [Fastly's Status API](https://domainr.com/docs/api/v2/status#status-results) to query the status of a domain every 30 days and mark the corresponding email address as unverified if it has expired.

Users of the Python package manager are being advised to enable two-factor authentication (2FA) and add a second verified email address from another notable domain, such as Gmail or Outlook, if the accounts only have a single verified email address from a custom domain name.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Domain Security](https://thehackernews.com/search/label/Domain%20Security)[Open Source](https://thehackernews.com/search/label/Open%20Source)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[software security](https://thehackernews.com/search/label/software%20security)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)[two-factor authentication](https://thehackernews.com/search/label/two-factor%20authentication)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure th...