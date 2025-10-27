---
title: Google Fixes GCP Composer Flaw That Could've Led to Remote Code Execution
url: https://thehackernews.com/2024/09/google-fixes-gcp-composer-flaw-that.html
source: The Hacker News
date: 2024-09-17
fetch_date: 2025-10-06T18:32:25.656503
---

# Google Fixes GCP Composer Flaw That Could've Led to Remote Code Execution

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

# [Google Fixes GCP Composer Flaw That Could've Led to Remote Code Execution](https://thehackernews.com/2024/09/google-fixes-gcp-composer-flaw-that.html)

**Sep 16, 2024**Ravie LakshmananCloud Security / Vulnerability

[![Google Fixes GCP Composer Flaw](data:image/png;base64... "Google Fixes GCP Composer Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRoDBfOdQJn_bHwmkL_f-lZ8TS1G0P_O06R2XrqEe9IdgoN3PVWkadlX-sra6zB-0PeKmsVNQlGbE5J-sNQ92P1txkhE0CXR61mdSh0fQVwyz98uERjUlT-I9ArEhakZ3QV6YUUrwUKnbYg7Q9xJgpd-qXLAvpydWvbRJt930wMu7JFvz4b9lCeIyovQoy/s790-rw-e365/flaw.png)

A now-patched critical security flaw impacting Google Cloud Platform (GCP) Composer could have been exploited to achieve remote code execution on cloud servers by means of a supply chain attack technique called dependency confusion.

The vulnerability has been codenamed **CloudImposer** by Tenable Research.

"The vulnerability could have allowed an attacker to hijack an internal software dependency that Google pre-installs on each Google Cloud Composer pipeline-orchestration tool," security researcher Liv Matan said in a [report](https://www.tenable.com/blog/cloudimposer-executing-code-on-millions-of-google-servers-with-a-single-malicious-package) shared with The Hacker News.

Dependency confusion (aka substitution attack), which was [first documented](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html) by security researcher Alex Birsan in February 2021, refers to a type of software supply chain compromise in which a package manager is tricked into pulling a malicious package from a public repository instead of the intended file of the same name from an internal repository.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

So, a threat actor could stage a large-scale supply chain attack by [publishing](https://blog.gitguardian.com/dependency-confusion-attacks/) a counterfeit package to a public package repository with the same name as a package internally developed by companies and with a higher version number.

This, in turn, causes the package manager to [unknowingly download](https://orca.security/resources/blog/dependency-confusion-supply-chain-attacks/) the malicious package from the public repository instead of the private repository, effectively replacing the existing package dependency with its rogue counterpart.

The problem [identified](https://www.tenable.com/security/research/tra-2024-18) by Tenable is similar in that it could be abused to upload a malicious package to the Python Package Index (PyPI) repository with the name "google-cloud-datacatalog-lineage-producer-client," which could then be preinstalled on all Composer instances with elevated permissions.

While Cloud Composer requires that the package in question is version-pinned (i.e., version 0.1.0), Tenable found that using the "--extra-index-url" argument during a "pip install" command prioritizes fetching the package from the public registry, thereby opening the door to dependency confusion.

Armed with this privilege, attackers could execute code, exfiltrate service account credentials, and move laterally in the victim's environment to other GCP services.

Following responsible disclosure on January 18, 2024, it was fixed by Google in May 2024 by ensuring that the package is only installed from a private repository. It has also added the extra precaution of verifying the package's checksum in order to confirm its integrity and validate that it has not been tampered with.

The Python Packaging Authority (PyPA) is said to have been aware of the risks posed by the "--extra-index-url" argument since at least March 2018, urging users to skip using PyPI in cases where the internal package needs to be pulled.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Packages are expected to be unique up to name and version, so two wheels with the same package name and version are treated as indistinguishable by pip," a PyPA member [noted](https://github.com/pypa/pip/issues/5045) at the time. "This is a deliberate feature of the package metadata, and not likely to change."

Google, as part of its fix, now also recommends that developers use the "--index-url" argument instead of the "–extra-index-url" argument and that GCP customers make use of an Artifact Registry virtual repository when requiring multiple repositories.

"The '--index-url' argument reduces the risk of dependency confusion attacks by only searching for packages in the registry that was defined as a given value for that argument," Matan said.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Dependency Confusion](https://thehackernews.com/search/label/Dependency%20Confusion)[Google Cloud Platform](https://thehackernews.com/search/label/Google%20Cloud%20Platform)[Python](https://thehackernews.com/search/label/Python)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[supply chain attack](https://thehackernews.com/search/label/supply%...