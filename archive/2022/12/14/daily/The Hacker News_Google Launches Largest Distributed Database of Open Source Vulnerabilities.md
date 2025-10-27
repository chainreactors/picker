---
title: Google Launches Largest Distributed Database of Open Source Vulnerabilities
url: https://thehackernews.com/2022/12/google-launches-largest-distributed.html
source: The Hacker News
date: 2022-12-14
fetch_date: 2025-10-04T01:28:53.498652
---

# Google Launches Largest Distributed Database of Open Source Vulnerabilities

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

# [Google Launches OSV-Scanner Tool to Identify Open Source Vulnerabilities](https://thehackernews.com/2022/12/google-launches-largest-distributed.html)

**Dec 13, 2022**Ravie LakshmananOpen Source / Vulnerability Database

[![OSV-Scanner](data:image/png;base64... "OSV-Scanner")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis6oAWStQsLIkq7eQ6yKYLfR9X7BAk70-AhJERFb7YRdEsu2xKG-0YqkBQ85JWGckWc6_ZLnN_mwFOTMsOQ07faoSNtA47RZOVCv3eEVel-EAduFV3dRS4Y8aoyDW7aTs2DGG0jQ5NTcdEHUZHCfEcHnAxq-80IOcKwJKLZ-N0lTLHPWy2NQBrTE9i/s790-rw-e365/OSV.png)

Google on Tuesday announced the open source availability of **OSV-Scanner**, a scanner that aims to offer easy access to vulnerability information about various projects.

The [Go-based tool](https://github.com/google/osv-scanner), powered by the Open Source Vulnerabilities ([OSV](https://osv.dev/list)) database, is designed to connect "a project's list of dependencies with the vulnerabilities that affect them," Google software engineer Rex Pan in a [post](https://security.googleblog.com/2022/12/announcing-osv-scanner-vulnerability.html) shared with The Hacker News.

"The OSV-Scanner generates reliable, high-quality vulnerability information that closes the gap between a developer's list of packages and the information in vulnerability databases," Pan added.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The idea is to identify all the transitive dependencies of a project and highlight relevant vulnerabilities using data pulled from OSV.dev database.

Google further stated that the open source platform supports 16 ecosystems, counting all major languages, Linux distributions (Debian and Alpine), as well as Android, Linux Kernel, and [OSS-Fuzz](https://github.com/google/oss-fuzz).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitWA5nGALsIVrl9bo3t73bPXmpRlRu5Lgu3b1IX_lp4DrrcjoUAmiaEC2ifr6dQbw3MKB9keiqkp2x_n5zmoxlMFv510ldazRBqiJYPY8c4Huhh0I7CRp9mfu4bsSQL1oa1Y_DdxbkU7uEO1D5QAf4wLferO94jLmI19nS8KqmWQ-RtFxtyrmSv5DQ/s790-rw-e365/google-1.png)

The result of this expansion is that OSV.dev is a repository to more than 38,000 advisories, up from 15,000 security alerts a year ago, with Linux (27.4%), Debian (23.2%), PyPI (9.5%), Alpine (7.9%), and npm (7.1%) taking up the top five slots.

As for the next steps, the internet giant noted it's working to incorporate support for C/C++ flaws by building a "high quality database" that involves adding "precise commit level metadata to CVEs."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxyQf2fr8kNCpInqwN-okCGaREwlFA8qoZr-OCw_aAPVe3LpWMhD-RkGkiBxxf3gVoaukuOWIaWes0GRs7LryVUs6bknXFm3D-mxL2w4rU-h4hxjRb9Maz49JxKE1q8R6jwLVR4hE_OUY6IDeE19hzBxlIJnJhKFfOsca18_8FbLXRLshu0VtkT9xT/s790-rw-e365/database.png)

OSV-Scanner arrives nearly two months after Google launched [GUAC](https://thehackernews.com/2022/10/google-launches-guac-open-source.html) – short for Graph for Understanding Artifact Composition – to complement Supply chain Levels for Software Artifacts ([SLSA](https://slsa.dev/) or "salsa") as part of its efforts to [harden software supply chain security](https://thehackernews.com/2022/12/malware-strains-targeting-python-and.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Last week, Google also published a new "[Perspectives on Security](https://blog.google/technology/safety-security/new-insights-for-defending-the-software-supply-chain/)" report calling on organizations to develop and deploy a common SLSA framework to prevent tampering, [improve integrity](https://www.sigstore.dev/), and secure packages against potential threats.

Other recommendations laid out by the company include taking on additional open source security responsibilities and adopting a more holistic approach to addressing risks such as those presented by the [Log4j vulnerability](https://thehackernews.com/2021/12/new-apache-log4j-update-released-to.html) and the [SolarWinds incident](https://thehackernews.com/2021/01/heres-how-solarwinds-hackers-stayed.html) in recent years.

"Software supply chain attacks typically require strong technical aptitude and long-term commitment to pull off," the company said. "Sophisticated actors are more likely to have both the intent and capability to conduct these types of attacks."

"Most organizations are vulnerable to software supply chain attacks because attackers take the time to target third-party providers with trusted connections to their customers' networks. They then use that trust to burrow deeper into the networks of their ultimate targets."

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

[Google](https://thehackernews.com/search/label/Google)[linux](https://thehackernews.com/search/label/linux)[Open Source](https://thehackernews.com/search/label/Open%20Source)[OSV-Scanner](https://thehackernews.com/search/label/OSV-Scanner)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix...