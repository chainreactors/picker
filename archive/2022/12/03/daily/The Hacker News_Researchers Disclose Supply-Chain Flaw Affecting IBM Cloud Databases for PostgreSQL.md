---
title: Researchers Disclose Supply-Chain Flaw Affecting IBM Cloud Databases for PostgreSQL
url: https://thehackernews.com/2022/12/researchers-disclose-supply-chain-flaw.html
source: The Hacker News
date: 2022-12-03
fetch_date: 2025-10-04T00:26:35.909370
---

# Researchers Disclose Supply-Chain Flaw Affecting IBM Cloud Databases for PostgreSQL

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

# [Researchers Disclose Supply-Chain Flaw Affecting IBM Cloud Databases for PostgreSQL](https://thehackernews.com/2022/12/researchers-disclose-supply-chain-flaw.html)

**Dec 02, 2022**Ravie LakshmananKubernetes / Cloud Security

[![Supply-Chain Flaw](data:image/png;base64... "Supply-Chain Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgZbW2cp0e-p4EX0QTxiK4EBxzi5NdqCGzkBkzkOXrYc5qBdR7jdXLzIwWaOuqDls5E-Mio2-JlT-pxumEw1K50rgRBopLlCGamnOY15TathJjxwoah4fJksT6FIYXzsuinvl5iYEou5SnEDbTmUJvXaQPj4wpzp0syFPle73Kcu-uQH0VYumM0_3cXg/s790-rw-e365/hack.png)

IBM has fixed a high-severity security vulnerability affecting its Cloud Databases (ICD) for PostgreSQL product that could be potentially exploited to tamper with internal repositories and run unauthorized code.

The privilege escalation flaw (CVSS score: 8.8), dubbed "**Hell's Keychain**" by cloud security firm Wiz, has been described as a "first-of-its-kind supply-chain attack vector impacting a cloud provider's infrastructure."

Successful exploitation of the bug could enable a malicious actor to remotely execute code in customers' environments and even read or modify data stored in the PostgreSQL database.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The vulnerability consists of a chain of three exposed secrets (Kubernetes service account token, private container registry password, CI/CD server credentials) coupled with overly permissive network access to internal build servers," Wiz researchers Ronen Shustin and Shir Tamari [said](https://www.wiz.io/blog/hells-keychain-supply-chain-attack-in-ibm-cloud-databases-for-postgresql).

Hell's Keychain commences with an SQL injection flaw in ICD that grants an attacker superuser (aka "ibm") privileges, which is then used to execute arbitrary commands on the underlying virtual machine hosting the database instance.

This capability is weaponized to access a Kubernetes API token file, allowing for broader post-exploitation efforts that involve pulling container images from IBM's private container registry, which stores images related to ICD for PostgreSQL, and scanning those images for additional secrets.

[![IBM Cloud Databases for PostgreSQL](data:image/png;base64... "IBM Cloud Databases for PostgreSQL")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcCT87Fs2OFRy2zaB1eZQ0qjYk1rmT5GAiPlCGaasii72Hu520vF3P2fExIEeAWG0kcT9HtzxIuocuGJyeae_25yg1S6dIieItxvh6zDxafZO0lftwxWuL7-KIkTh7nmsIA9VI4gkKcDv7PHW6Ar_mT7F6JkmXL8BjGyiNvcCDHbC_yG-8hK5yVW41/s790-rw-e365/inside.gif)

"Container images typically hold proprietary source code and binary artifacts that are the company's intellectual property," the researchers explained. "They can also contain information that an attacker could leverage to find additional vulnerabilities and perform lateral movement within the service's internal environment."

Wiz said it was able to extract internal artifact repository and FTP credentials from the image manifest files, effectively permitting unfettered read-write access to trusted repositories and IBM build servers.

An attack of this kind could have severe ramifications, as it enables the adversary to overwrite arbitrary files that are used in the build process of the PostgreSQL image, which would then be installed on every database instance.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The American technology giant, in an [independent advisory](https://www.ibm.com/support/pages/node/6842111), said that all IBM Cloud Databases for PostgreSQL instances were potentially impacted by the bug, but noted that it found no evidence of malicious activity.

It further stated that the fixes have been automatically applied to customer instances and that no further action is required. The mitigations were rolled out on August 22 and September 3, 2022.

"These vulnerabilities could have been exploited by a malicious actor as part of an extensive exploit chain culminating in a supply-chain attack on the platform," the researchers said.

To mitigate such threats, it's recommended that organizations monitor their cloud environments for scattered credentials, enforce network controls to prevent access to production servers, and safeguard against container registry scraping.

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

[Cloud Database](https://thehackernews.com/search/label/Cloud%20Database)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[PostgreSQL](https://thehackernews.com/search/label/PostgreSQL)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-r...