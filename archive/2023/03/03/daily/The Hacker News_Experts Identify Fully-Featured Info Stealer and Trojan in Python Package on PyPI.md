---
title: Experts Identify Fully-Featured Info Stealer and Trojan in Python Package on PyPI
url: https://thehackernews.com/2023/03/experts-identify-fully-featured-info.html
source: The Hacker News
date: 2023-03-03
fetch_date: 2025-10-04T08:33:41.617614
---

# Experts Identify Fully-Featured Info Stealer and Trojan in Python Package on PyPI

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

# [Experts Identify Fully-Featured Info Stealer and Trojan in Python Package on PyPI](https://thehackernews.com/2023/03/experts-identify-fully-featured-info.html)

**Mar 02, 2023**Ravie LakshmananSoftware Security / CodingSec

[![Python Package on PyPI](data:image/png;base64... "Python Package on PyPI")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj07sG1daECtzoh5GovzhXuUeHZGaALlsSvTVUobQhXFE_bTeJubKrSR2NbIiOBj5WUMJlz0RRKrqw_dNyBYxFfEbQj-IbjkVVRF1S7TuqemiY3VnoYV-EtrMrhamCBH8QbH6cutnEAz8mAxg3WEqtunruLRpT8fnAEmXYcGHRRtcyy3Wb1veAPZsV/s790-rw-e365/python.png)

A malicious Python package uploaded to the Python Package Index (PyPI) has been found to contain a fully-featured information stealer and remote access trojan.

The package, named **colourfool**, was identified by Kroll's Cyber Threat Intelligence team, with the company calling the malware **Colour-Blind**.

"The 'Colour-Blind' malware points to the democratization of cybercrime that could lead to an intensified threat landscape, as multiple variants can be spawned from code sourced from others," Kroll researchers Dave Truman and George Glass [said](https://www.kroll.com/en/insights/publications/cyber/pypi-packages-deliver-python-remote-access-tools) in a report shared with The Hacker News.

colourfool, like [other rogue Python modules](https://thehackernews.com/2023/02/python-developers-warned-of-trojanized.html) discovered in recent months, conceals its malicious code in the setup script, which points to a ZIP archive payload hosted on Discord.

The file contains a Python script (code.py) that comes with different modules designed to log keystrokes, steal cookies, and even disable security software.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware, besides performing defense evasion checks to determine if it's being executed in a sandbox, establishes persistence by means of a Visual Basic script and uses transfer[.]sh for data exfiltration.

"As a method of remote control, the malware starts a Flask web application, which it makes accessible to the internet via Cloudflare's reverse tunnel utility 'cloudflared,' bypassing any inbound firewall rules," the researchers said.

The use of Cloudflare tunnels mirrors [another campaign](https://thehackernews.com/2023/01/malicious-pypi-packages-using.html) that was disclosed by Phylum last month which made use of six fraudulent packages to distribute a stealer-cum-RAT dubbed poweRAT.

"There are strong similarities between the malware in that they both use Flask and Cloudflare," Truman told The Hacker News. "However, whilst the Phylum researched malware relies on PowerShell for much of its key functionality, 'Colour-Blind' is nearly entirely written in Python."

"Combine this with the functionality presented by the Flask web application performing different actions, rather than the newer malware adding to the functionality of the older, it could mean that the relationship is more in the form of the different threat actors sharing ideas, resources or code, rather than an evolution of a code base being developed by a single actor," Truman added.

The trojan is feature rich and is capable of gathering passwords, terminating applications, taking screenshots, logging keystrokes, opening arbitrary web pages on a browser, executing commands, capturing crypto wallet data, and even snooping on victims via the web camera.

[![Python Package on PyPI](data:image/png;base64... "Python Package on PyPI")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT10ja1E7tghWuY8ebvhV4Fpx0QAqCd4LYUPKO2hVqGtUJSrAsFd6VOr_x8RY8kgQ-OHHkYBiJUrKJi6eQxq4eg4b6BqnfVGsdMw62B0wPaL2n1Rbh3JphpVPlDukMl57gH4OaAAwU_ybOw1Ba40wuwW39957VG2sZ3LbxLjEDTU3SG4ElbPsf5pbg/s790-rw-e365/malware.png)

The findings come as threat actors are leveraging the source code associated with [W4SP stealer](https://thehackernews.com/2022/12/w4sp-stealer-discovered-in-multiple.html) to spawn copycat versions that are [distributed](https://blog.sonatype.com/how-stolen-information-stealers-are-fueling-an-underground-market) via Python packages like ratebypass, imagesolverpy, and [3m-promo-gen-api](https://thehackernews.com/2023/02/researchers-uncover-obfuscated.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

What's more, Phylum [discovered](https://blog.phylum.io/phylum-discovers-go-based-rat-spark-being-distributed-on-pypi) three additional packages – called pycolured, pycolurate, and colurful – that have been used to deliver a Go-based remote access trojan referred to as [Spark](https://github.com/XZB-1248/Spark).

Adding to the attacks targeting PyPI, the software supply chain security firm also [revealed details](https://blog.phylum.io/phylum-discovers-another-attack-on-pypi) of a massive attack campaign wherein unknown threat actors published as many as 1,138 packages to deploy a Rust executable, which is then used to drop additional malware binaries.

"The risk/reward proposition for attackers is well worth the relatively minuscule time and effort, if they can land a whale with a fat crypto wallet," the Phylum research team [said](https://blog.phylum.io/a-pypi-typosquatting-campaign-post-mortem).

"And the loss of a few bitcoin pales in comparison to the potential damage of the loss of a developer's SSH keys in a large enterprise such as a corporation or government."

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
[**Share on Reddit](#...