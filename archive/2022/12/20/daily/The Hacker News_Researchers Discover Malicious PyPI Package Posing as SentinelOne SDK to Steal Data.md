---
title: Researchers Discover Malicious PyPI Package Posing as SentinelOne SDK to Steal Data
url: https://thehackernews.com/2022/12/researchers-discover-malicious-pypi.html
source: The Hacker News
date: 2022-12-20
fetch_date: 2025-10-04T02:01:18.929956
---

# Researchers Discover Malicious PyPI Package Posing as SentinelOne SDK to Steal Data

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

# [Researchers Discover Malicious PyPI Package Posing as SentinelOne SDK to Steal Data](https://thehackernews.com/2022/12/researchers-discover-malicious-pypi.html)

**Dec 19, 2022**Ravie LakshmananSoftware Security / Supply Chain

[![Malicious PyPI package](data:image/png;base64... "Malicious PyPI package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe6FVqtp3OdWdhFrufG0NJ49souZoGhbbqTePSFAtz1uDm5ycQ45nqWYQCt8XjyEUObK6p6TH_C5YURPje5AkTbj2mOe8G_ruC6ZlMJw_tIBa8pzUzK_cN_HCE8fk5ZzGp7n1AE61qFHnE2Owp8QTyLO7cEAtM1Z3Rf_ZXKEu8Clb75nq-wHPVB0sZ/s790-rw-e365/pypi-malware.png)

Cybersecurity researchers have discovered a new malicious package on the Python Package Index (PyPI) repository that impersonates a software development kit (SDK) for SentinelOne, a major cybersecurity company, as part of a campaign dubbed **SentinelSneak**.

The package, named [SentinelOne](https://pypi.org/project/SentinelOne/) and now taken down, is said to have been published between December 8 and 11, 2022, with nearly two dozen versions pushed in quick succession over a period of two days.

It claims to offer an easier method to access the [company's APIs](https://www.sentinelone.com/faq/#:~:text=What%20is%20SentinelOne%20API%3F), but harbors a malicious backdoor that's engineered to amass sensitive information from development systems, including access credentials, SSH keys, and configuration data.

What's more, the threat actor has also been observed releasing two more packages with similar naming variations – [SentinelOne-sdk](https://pypi.org/project/sentinelone-sdk/) and [SentinelOneSDK](https://pypi.org/project/SentineloneSDK/) – underscoring the [continued threats](https://thehackernews.com/2022/12/hackers-bombard-open-source.html) lurking in open source repositories.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The SentinelOne imposter package is just the latest threat to leverage the PyPI repository and underscores the growing threat to software supply chains, as malicious actors use strategies like 'typosquatting' to exploit developer confusion and push malicious code into development pipelines and legitimate applications," ReversingLabs threat researcher Karlo Zanki [said](https://blog.reversinglabs.com/blog/sentinelsneak-malicious-pypi-module-poses-as-security-sdk) in a report shared with The Hacker News.

What's notable about the fraudulent package is it mimics a [legitimate SDK](https://www.sentinelone.com/faq/#:~:text=What%20is%20SentinelOne%20API%3F) that's offered by SentinelOne to its customers, potentially tricking developers into downloading the module from PyPI.

[![Malicious PyPI package](data:image/png;base64... "Malicious PyPI package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFJRNLbi9GagUb0J2RhE27nBtfyvNTU4VdFOMonhjILyM0eK-Jrc_IQK20IqYLkB-xuG94aaAeFVItrjzh-yrimbVw7_l_Rm4NLZO3sZCGoZGL4g7BLQQkfkeFjmuXZPWPShmrAHd9LwOw-fIiNJQnAMuyPXPbe_hpacnNPwXIYg6SvFLnNs6mr7vA/s790-rw-e365/code.png)

The software supply chain security company noted that the SDK client code may have been "likely obtained from the company by way of a legitimate customer account."

Some of the data exfiltrated by the malware to a remote server include shell command execution history, SSH keys, and other files of interest, indicating an attempt on the part of the threat actor to siphon sensitive information from development environments.

It's not immediately clear if the package was weaponized as part of an active supply chain attack, although it has been downloaded more than 1,000 times prior to its removal.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

When reached for comment, SentinelOne told The Hacker News that it's "not involved with the recent malicious Python package leveraging our name," and that the threat actors were not successful in their attempts.

"Attackers will put any name on their campaigns that they think may help them deceive their intended targets, however this package is not affiliated with SentinelOne in any way," the company said. "Our customers are secure, we have not seen any evidence of compromise due to this campaign, and PyPI has removed the package."

The findings come as ReversingLabs' State of Software Supply Chain Security report [found](https://blog.reversinglabs.com/blog/the-state-of-software-supply-chain-security) that the PyPI repository has witnessed a nearly 60% decrease in malicious package uploads in 2022, dropping to 1,493 packages from 3,685 in 2021.

On the contrary, the npm JavaScript repository saw a 40% increase to nearly 7,000, making it the "biggest playground for malicious actors." In all, rogue package trends since 2020 have exhibited a 100 times rise in npm and more than 18,000% in PyPI.

"Though small in scope and of little impact, this campaign is a reminder to development organizations of the persistence of software supply chain threats," Zanki said. "As with previous malicious campaigns, this one plays on tried and true social engineering tactics to confuse and mislead developers into downloading a malicious module."

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

[API Security](https:/...