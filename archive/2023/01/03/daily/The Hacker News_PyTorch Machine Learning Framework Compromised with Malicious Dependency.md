---
title: PyTorch Machine Learning Framework Compromised with Malicious Dependency
url: https://thehackernews.com/2023/01/pytorch-machine-learning-framework.html
source: The Hacker News
date: 2023-01-03
fetch_date: 2025-10-04T02:56:01.207984
---

# PyTorch Machine Learning Framework Compromised with Malicious Dependency

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

# [PyTorch Machine Learning Framework Compromised with Malicious Dependency](https://thehackernews.com/2023/01/pytorch-machine-learning-framework.html)

**Jan 02, 2023**Ravie LakshmananSupply Chain / Machine Learning

[![PyTorch Machine Learning](data:image/png;base64... "PyTorch Machine Learning")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifiFY4TB4xInGZvI7gizGIvPBUZbr9Egk3zV-NefK97gEBfE_67-u41jrPzOlaz7iS94W4hu0BamT55Wb3QxIoK69F_mYwYhM9fVaNVFrzMt0csy-wjD7fDViYLZCBN8-BP1zKl_7pqUNJbEXYYRdKYgJWc6DSJVTeQ2EFLN5rh6KuBwY-h29g2_0R/s790-rw-e365/python.png)

The maintainers of the PyTorch package have warned users who have installed the nightly builds of the library between December 25, 2022, and December 30, 2022, to uninstall and download the latest versions following a [dependency confusion attack](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html).

"PyTorch-nightly Linux packages installed via pip during that time installed a dependency, **torchtriton**, which was compromised on the Python Package Index (PyPI) code repository and ran a malicious binary," the PyTorch team [said](https://pytorch.org/blog/compromised-nightly-dependency/#how-to-check-if-your-python-environment-is-affected) in an alert over the weekend.

PyTorch, analogous to Keras and TensorFlow, is an open source Python-based machine learning framework that was originally developed by Meta Platforms.

The PyTorch team said that it became aware of the malicious dependency on December 30, 4:40 p.m. GMT. The supply chain attack entailed uploading the malware-laced copy of a legitimate dependency named torchtriton to the Python Package Index (PyPI) code repository.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Since package managers like pip check public code registries such as PyPI for a package before private registries, it allowed the fraudulent module to be installed on users' systems as opposed to the actual version pulled from the third-party index.

"The attacker took advantage of the fact that PyTorch consumes several dependency packages from a dedicated package index and the fact that the package manager 'pip' prioritizes the PyPI package index above other indices," Checkmarx researcher Zack Tzachi [said](https://medium.com/checkmarx-security/py-torch-a-leading-ml-framework-was-poisoned-with-malicious-dependency-e30f88242964).

The rogue version, for its part, is engineered to exfiltrate system information, including environment variables, the current working directory, and host name, in addition to accessing the following files -

* /etc/hosts
* /etc/passwd
* The first 1,000 files in $HOME/\*
* $HOME/.gitconfig
* $HOME/.ssh/\*

Aqua Security, in its own [analysis](https://blog.aquasec.com/pytorch-dependency-confusion-administered-malware) of the bogus torchtriton module, said the package is almost 100% identical to its legitimate counterpart except for one crucial change that enables it to run a malicious binary called triton for harvesting the sensitive data.

In a statement shared with Bleeping Computer, the owner of the domain to which the stolen data was transmitted [claimed](https://www.bleepingcomputer.com/news/security/pytorch-discloses-malicious-dependency-chain-compromise-over-holidays/) it was part of an ethical research exercise and that all the data has since been deleted.

As mitigations, torchtriton has been removed as a dependency and replaced with pytorch-triton. A dummy package has also been registered on PyPI [as a placeholder](https://thehackernews.com/2022/10/new-timing-attack-against-npm-registry.html) to prevent further abuse.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This is not the real torchtriton package but uploaded here to discover dependency confusion vulnerabilities," reads a [message](https://pypi.org/project/torchtriton/#history) on the PyPI page for torchtriton. "You can get the real torchtriton from https://download.pytorch[.]org/whl/nightly/torchtriton/."

The development also comes as JFrog disclosed details of another package known as [cookiezlog](https://jfrog.com/blog/pypi-malware-creators-are-starting-to-employ-anti-debug-techniques/) that has been observed utilizing anti-debugging techniques to resist analysis, marking the first time such mechanisms have been incorporated in PyPI malware.

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

[Dependency Confusion](https://thehackernews.com/search/label/Dependency%20Confusion)[machine learning](https://thehackernews.com/search/label/machine%20learning)[PyTorch](https://thehackernews.com/search/label/PyTorch)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)...