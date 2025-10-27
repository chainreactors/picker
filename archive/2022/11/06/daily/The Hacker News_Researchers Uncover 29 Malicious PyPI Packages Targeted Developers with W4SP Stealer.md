---
title: Researchers Uncover 29 Malicious PyPI Packages Targeted Developers with W4SP Stealer
url: https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html
source: The Hacker News
date: 2022-11-06
fetch_date: 2025-10-03T21:50:51.406082
---

# Researchers Uncover 29 Malicious PyPI Packages Targeted Developers with W4SP Stealer

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

# [Researchers Uncover 29 Malicious PyPI Packages Targeted Developers with W4SP Stealer](https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html)

**Nov 05, 2022**Ravie Lakshmanan

[![W4SP Stealer](data:image/png;base64... "W4SP Stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzXHremxMPv6xKza9t6S8bcQQcE-P9qg7TAMEtDqgFp0wi_x6_DLtNAJGJ12E_WeA6-9Xiecr2AHt6eeUH-67laEZkLZUFWsN_1I3fwdlJ0UPuwaRv1MecxS06n3shCyGMOkpgjDwsPsbKEB7blrX2qX4FMjyREMliuKclCzZEBnJm0Gku_aQ-LcS5/s790-rw-e365/python.jpg)

Cybersecurity researchers have uncovered 29 packages in Python Package Index (PyPI), the official third-party software repository for the Python programming language, that aim to infect developers' machines with a malware called **W4SP Stealer**.

"The main attack seems to have started around October 12, 2022, slowly picking up steam to a concentrated effort around October 22," software supply chain security company Phylum [said](https://blog.phylum.io/phylum-discovers-dozens-more-pypi-packages-attempting-to-deliver-w4sp-stealer-in-ongoing-supply-chain-attack) in a report published this week.

The list of offending packages is as follows: typesutil, typestring, sutiltype, duonet, fatnoob, strinfer, pydprotect, incrivelsim, twyne, pyptext, installpy, faq, colorwin, requests-httpx, colorsama, shaasigma, stringe, felpesviadinho, cypress, pystyte, pyslyte, pystyle, pyurllib, algorithmic, oiu, iao, curlapi, type-color, and pyhints.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Collectively, the packages have been downloaded more than 5,700 times, with some of the libraries (e.g., twyne and colorsama) relying on typosquatting to trick unsuspecting users into downloading them.

The fraudulent modules repurpose existing legitimate libraries by inserting a malicious [import statement](https://docs.python.org/3/reference/import.html) in the packages' "[setup.py](https://thehackernews.com/2022/09/warning-pypi-feature-executes-code.html)" script to launch a piece of Python code that fetches the malware from a remote server.

[W4SP Stealer](https://github.com/loTus04/W4SP-Stealer), an open source Python-based trojan, comes with capabilities to pilfer files of interest, passwords, browser cookies, system metadata, Discord tokens, as well as data from the MetaMask, Atomic and Exodus crypto wallets.

This is not the first time W4SP Stealer has been delivered through seemingly benign packages in the PyPI repository. In August, Kaspersky [uncovered](https://securelist.com/two-more-malicious-python-packages-in-the-pypi/107218/) two libraries named pyquest and ultrarequests that were found to deploy the malware as a final payload.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings illustrate [continued](https://thehackernews.com/2022/08/10-credential-stealing-python-libraries.html) [abuse](https://snyk.io/blog/pypi-malware-discord-roblox-credential-payment-info/) of [open source](https://blog.phylum.io/phylum-detects-active-typosquatting-campaign-targeting-npm-developers) [ecosystems](https://www.secure.software/infographic/reversinglabs-nvd-analysis-2022-a-call-to-action-on-software-supply-chain-security) to propagate malicious packages that are designed to harvest sensitive information and make way for [supply chain attacks](https://thehackernews.com/2022/10/google-launches-guac-open-source.html).

"As this is an ongoing attack with constantly changing tactics from a determined attacker, we suspect to see more malware like this popping up in the near future," Phylum noted.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[Python Package Index](https://thehackernews.com/search/label/Python%20Package%20Index)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-...