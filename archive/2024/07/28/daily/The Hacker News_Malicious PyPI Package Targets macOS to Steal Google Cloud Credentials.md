---
title: Malicious PyPI Package Targets macOS to Steal Google Cloud Credentials
url: https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html
source: The Hacker News
date: 2024-07-28
fetch_date: 2025-10-06T17:42:07.969505
---

# Malicious PyPI Package Targets macOS to Steal Google Cloud Credentials

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

# [Malicious PyPI Package Targets macOS to Steal Google Cloud Credentials](https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html)

**Jul 27, 2024**Ravie LakshmananCybersecurity / Cloud Security

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj80K3BGTz7k9XFNIo5AP_zHn4qE7G7ld3PGmEKWJXV5CGz2mvy_DzzafZMXf3sVqMMxzjjHVIhP4puQQ-iNnBCxgUsFdeAg7p3FnkchgJGqmnpZqiqw_ZZfTPlPvTDPV7x0IcRIvd-FMdY1jpRGCgODr2WHrbpFH1GHLbKYpvKbuuqfaGLprQ9mpIpqVMk/s790-rw-e365/macos.png)

Cybersecurity researchers have discovered a malicious package on the Python Package Index (PyPI) repository that targets Apple macOS systems with the goal of stealing users' Google Cloud credentials from a narrow pool of victims.

The package, named "lr-utils-lib," attracted a total of [59 downloads](https://www.pepy.tech/projects/lr-utils-lib) before it was taken down. It was uploaded to the registry in early June 2024.

"The malware uses a list of predefined hashes to target specific macOS machines and attempts to harvest Google Cloud authentication data," Checkmarx researcher Yehuda Gelb [said](https://checkmarx.com/blog/malicious-python-package-targets-macos-developers-to-access-their-gcp-accounts/) in a Friday report. "The harvested credentials are sent to a remote server."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

An important aspect of the package is that it first checks if it has been installed on a macOS system, and only then proceeds to compare the system's Universally Unique Identifier (UUID) against a hard-coded list of 64 hashes.

If the compromised machine is among those specified in the predefined set, it attempts to access two files, namely application\_default\_credentials.json and credentials.db, located in the ~/.config/gcloud directory, which contain Google Cloud authentication data.

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWmay1lFPtNVLArsOzFOYwnir-mCFNfGRGOZaGmt7gAymWUXODPeaSovODRD5nMjQ9ofmxSlJmeOA2SqMH-QtG8J4U-gJVAcFlpjTpo-V-j-lsU9KPsslgViUuWf7KgIHkkFbxdgjJV9pyJXNx6b3Us8szriPkZA6dQxz6eY4vV3posIeTyAAwOyPNFpnG/s790-rw-e365/apple.png)

The captured information is then transmitted over HTTP to a remote server "europe-west2-workload-422915[.]cloudfunctions[.]net."

Checkmarx said it also found a fake profile on LinkedIn with the name "Lucid Zenith" that matched the package's owner and falsely claimed to be the CEO of Apex Companies, suggesting a possible social engineering element to the attack.

Exactly who is behind the campaign is currently not known. However, it comes more than two months after cybersecurity firm Phylum [disclosed](https://thehackernews.com/2024/05/malicious-python-package-hides-sliver.html) details of another supply chain attack involving a Python package called "requests-darwin-lite" that was also found to unleash its malicious actions after checking the UUID of the macOS host.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

These campaigns are a sign that threat actors have prior knowledge of the macOS systems they want to infiltrate and are going to great lengths to ensure that the malicious packages are distributed only to those particular machines.

It also speaks to the tactics malicious actors employ to distribute lookalike packages, aiming to deceive developers into incorporating them into their applications.

"While it is not clear whether this attack targeted individuals or enterprises, these kinds of attacks can significantly impact enterprises," Gelb said. "While the initial compromise usually occurs on an individual developer's machine, the implications for enterprises can be substantial."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[MacOS](https://thehackernews.com/search/label/MacOS)[Malware](https://thehackernews.com/search/label/Malware)[Python](https://thehackernews.com/search/label/Python)[social engineering](https://thehackernews.com/search/label/social%20engineering)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Foun...