---
title: W4SP Stealer Discovered in Multiple PyPI Packages Under Various Names
url: https://thehackernews.com/2022/12/w4sp-stealer-discovered-in-multiple.html
source: The Hacker News
date: 2022-12-25
fetch_date: 2025-10-04T02:30:24.331937
---

# W4SP Stealer Discovered in Multiple PyPI Packages Under Various Names

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

# [W4SP Stealer Discovered in Multiple PyPI Packages Under Various Names](https://thehackernews.com/2022/12/w4sp-stealer-discovered-in-multiple.html)

**Dec 24, 2022**Ravie LakshmananSoftware Security / Supply Chain

[![PyPI Packages](data:image/png;base64... "PyPI Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBy6_BXkP_fBeJ0AtJPPA6jIo-ZbcKCdSZc8PgUUqwH_FDXz1wqYKobt65gOjaIAAdZWAX9GqJpaW1d-blK8qkU9KpxkXNmYlPpNarqffUkoGabvkB0MTAbC4BF9nFZ-d0BX11F70cuv2l08SOInAZK1bOuIuGec-Q7VwEfaSsJuTv5RLI9GZmRqBO/s790-rw-e365/code-hacking.png)

Threat actors have published yet another round of malicious packages to Python Package Index (PyPI) with the goal of delivering information-stealing malware on compromised developer machines.

Interestingly, while the malware goes by a variety of names like ANGEL Stealer, Celestial Stealer, Fade Stealer, Leaf $tealer, PURE Stealer, Satan Stealer, and @skid Stealer, cybersecurity company Phylum found them all to be copies of [W4SP Stealer](https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html).

W4SP Stealer primarily functions to siphon user data, including credentials, cryptocurrency wallets, Discord tokens, and other files of interest. It's created and published by an actor who goes by the aliases BillyV3, BillyTheGoat, and billythegoat356.

"For some reason, each deployment appears to have simply tried to do a find/replace of the W4SP references in exchange for some other seemingly arbitrary name," the researchers [said](https://blog.phylum.io/phylum-discovers-new-stealer-variants-in-burgeoning-pypi-supply-chain-attack) in a report published earlier this week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The 16 rogue modules are as follows: modulesecurity, informmodule, chazz, randomtime, proxygeneratorbil, easycordey, easycordeyy, tomproxies, sys-ej, py4sync, infosys, sysuptoer, nowsys, upamonkws, captchaboy, and proxybooster.

The campaign distributing W4SP Stealer [gained traction](https://thehackernews.com/2022/11/w4sp-stealer-constantly-targeting.html) around October 2022, although indications are that it may have started as far back as August 25, 2022. Since then dozens of [additional bogus packages](https://thehackernews.com/2022/12/malware-strains-targeting-python-and.html) containing [W4SP Stealer](https://blog.phylum.io/w4sp-stealer-update-theyre-still-at-it) have been published on PyPI by the persistent threat actors.

The latest iteration of the activity, for what it's worth, makes no obvious to hide its nefarious intentions, except in the case of chazz, which leverages the package to download obfuscated Leaf $tealer malware hosted on the klgrth[.]io paste service.

It's worth noting that previous versions of the attack chains have also been spotted fetching next-stage Python code directly from a public GitHub repository that then drops the credential stealer.

The surge in new copycat variants dovetails with GitHub's takedown of the repository that held the original W4SP Stealer source code, indicating that cybercriminals likely not affiliated with the operation are also weaponizing the malware to attack PyPI users.

"Open-source ecosystems such as PyPI, NPM, and the like are huge easy targets for these kinds of actors to try and deploy this kind of malware on," the researchers said. Their attempts will only become more frequent, more persistent, and most sophisticated."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The software supply chain security firm, which [kept tabs](https://blog.phylum.io/into-the-w4sps-nest-pypi-malware) on the threat actor's Discord channel, further noted that a previously flagged package under the name of [pystyle](https://github.com/billythegoat356/pystyle) was trojanized by BillyTheGoat to distribute the stealer.

The module has not only racked up [thousands of downloads](https://pypistats.org/packages/pystyle) each month, but also started off as an innocuous utility in September 2021 to help users style console output. The malicious modifications were introduced in versions 2.1 and 2.2 released on October 28, 2022.

These two versions, which were live on PyPI for about an hour before they were pulled, are alleged to have gotten 400 downloads, BillyTheGoat told Phylum in an "unsolicited correspondence." The [latest version](https://pypi.org/project/pystyle/#history) available in the repository is 2.9.

"Just because a package is benign today and has shown a history of being benign for years does not mean it will remain this way," the researchers [cautioned](https://blog.phylum.io/into-the-w4sps-nest-pypi-malware). "Threat actors have shown tremendous patience in building legitimate packages, only to poison them with malware after they have become sufficiently popular."

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

[Malware](https://thehackernews.com/search/label/Malware)[PyPI Package](https://thehackernews.com/search/label/PyPI%20Package)[Python Package Index](https://thehackernews.com/search/label/Python%20Package%20Index)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](dat...