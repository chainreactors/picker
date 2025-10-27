---
title: Packagist Repository Hacked: Over a Dozen PHP Packages with 500 Million Compromised
url: https://thehackernews.com/2023/05/packagist-repository-hacked-over-dozen.html
source: The Hacker News
date: 2023-05-06
fetch_date: 2025-10-04T11:43:15.750371
---

# Packagist Repository Hacked: Over a Dozen PHP Packages with 500 Million Compromised

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

# [Packagist Repository Hacked: Over a Dozen PHP Packages with 500 Million Installs Compromised](https://thehackernews.com/2023/05/packagist-repository-hacked-over-dozen.html)

**May 05, 2023**Ravie LakshmananProgramming / Software Security

[![Packagist](data:image/png;base64... "Packagist")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiPQmf1Z13NTi9ksBKGfYXEhsbWj6IK6iPhkvjD7NsiwgK2wi558axFxnD1Kwb0UJJ9YOar3fYDyOY0l_1mcOvZsW1Mm6Ecodp8y5Ldk1mkIUgdN2886XLyLzAq5g_dLKW-LvszBq41mpEPEMcHUi-flSo6Nq58cwnL-9-AZX_3wqyMzewOJx-_9iv/s790-rw-e365/php-hack.jpg)

PHP software package repository Packagist revealed that an "attacker" gained access to four inactive accounts on the platform to hijack over a dozen packages with over 500 million installs to date.

"The attacker forked each of the packages and replaced the package description in [composer.json](https://thehackernews.com/2022/10/researchers-report-supply-chain.html) with their own message but did not otherwise make any malicious changes," Packagist's Nils Adermann [said](https://blog.packagist.com/packagist-org-maintainer-account-takeover/). "The package URLs were then changed to point to the forked repositories."

The four user accounts are said to have had access to a total of 14 packages, including multiple Doctrine packages. The incident took place on May 1, 2023. The complete list of impacted packages is as follows -

* acmephp/acmephp
* acmephp/core
* acmephp/ssl
* doctrine/doctrine-cache-bundle
* doctrine/doctrine-module
* doctrine/doctrine-mongo-odm-module
* doctrine/doctrine-orm-module
* doctrine/instantiator
* growthbook/growthbook
* jdorn/file-system-cache
* jdorn/sql-formatter
* khanamiryan/qrcode-detector-decoder
* object-calisthenics/phpcs-calisthenics-rules
* tga/simhash-php

Security researcher Ax Sharma, writing for Bleeping Computer, [revealed](https://www.bleepingcomputer.com/news/security/researcher-hijacks-popular-packagist-php-packages-to-get-a-job/) that the changes were made by an anonymous penetration tester with the pseudonym "neskafe3v1" in an attempt to land a job.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The attack chain, in a nutshell, made it possible to modify the Packagist page for each of these packages to a namesake GitHub repository, effectively altering the installation workflow used within Composer environments.

Successful exploitation meant that developers downloading the packages would get the forked version as opposed to the actual contents.

Packagist said that no additional malicious changes were distributed, and that all the accounts were disabled and their packages restored on May 2, 2023. It's also urging users to enable two-factor authentication (2FA) to secure their accounts.

"All four accounts appear to have been using shared passwords leaked in previous incidents on other platforms," Adermann noted. "Please, do not reuse passwords."

The development comes as cloud security firm Aqua identified thousands of exposed cloud software registries and repositories containing more than 250 million artifacts and over 65,000 container images.

The misconfigurations stem from mistakenly connecting registries to the internet, allowing anonymous access by design, using default passwords, and granting upload privileges to users that could be abused to poison the registry with malicious code.

"In some of these cases, anonymous user access allowed a potential attacker to gain sensitive information, such as secrets, keys, and passwords, which could lead to a severe software supply chain attack and poisoning of the software development life cycle (SDLC)," researchers Mor Weinberger and Assaf Morag [disclosed](https://blog.aquasec.com/250m-artifacts-exposed-via-misconfigured-registries) late last month.

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

[Packagist](https://thehackernews.com/search/label/Packagist)[PHP](https://thehackernews.com/search/label/PHP)[software security](https://thehackernews.com/search/label/software%20security)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-20...