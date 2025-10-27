---
title: Researchers Uncover PyPI Package Hiding Malicious Code Behind Image File
url: https://thehackernews.com/2022/11/researchers-uncover-pypi-package-hiding.html
source: The Hacker News
date: 2022-11-11
fetch_date: 2025-10-03T22:26:23.983360
---

# Researchers Uncover PyPI Package Hiding Malicious Code Behind Image File

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

# [Researchers Uncover PyPI Package Hiding Malicious Code Behind Image File](https://thehackernews.com/2022/11/researchers-uncover-pypi-package-hiding.html)

**Nov 10, 2022**Ravie Lakshmanan

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDKozAAVrzxcnQaY1nyeIo-yfxeHUDxcmpI3Behh3zOv7ZFFLHxBky2gkeEeCK27p6iknqlu3KL2Q0ukHsudjjZxrwBZUZPd1QwrPyg3aOMPqoT9b0A4B9fg9VMWg0NmZfompwA-xvY0hTrgaIFhH4wXebFqGf4srHtffLxOWG8HFTCJguT0KxcIgc/s790-rw-e365/python.jpg)

A malicious package discovered on the Python Package Index (PyPI) has been found employing a steganographic trick to conceal malicious code within image files.

The package in question, named "**apicolor**," was uploaded to the Python third-party repository on October 31, 2022, and described as a "Core lib for REST API," according to Israeli cybersecurity firm [Check Point](https://research.checkpoint.com/2022/check-point-cloudguard-spectral-exposes-new-obfuscation-techniques-for-malicious-packages-on-pypi/). It has since been [taken down](https://pypi.org/project/apicolor/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Apicolor, like other [rogue packages](https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html) detected recently, harbors its malicious behavior in the setup script used to specify metadata associated with the package, such as its dependencies.

This takes the form of a second package called "judyb" as well as a seemingly harmless PNG file ("8F4D2uF.png") hosted on Imgur, an image-sharing service.

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdiM98aRJgokVhi33oVVUl99FUEh_IYNBupmj5yN-d36QZ8YHvA0f4vxkY0v5RuCf1Zz36kqgkUKVSLlxFY64CJcAIp8GDncJONV2SbPMUayhoPWr-dT1WZ8ujERkeB0tyFAYM42VM4IsHPcBSi5UzUvAiVPfNawm_tXH-IKgiVwtJfiZNFefkiyZw/s790-rw-e365/APICOLOR.jpg)

"The judyb code turned out to be a steganography module, responsible [for] hiding and revealing hidden messages inside pictures," Check Point explained.

The attack chain entails using the judyb package to extract obfuscated Python code embedded within the downloaded image, which, upon decoding, is designed to retrieve and execute a malicious binary from a remote server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development is part of an ongoing trend where threat actors are increasingly setting their sights on the open source ecosystem to exploit the trust associated with third-party software to mount supply chain attacks.

Even more troublingly, such malicious libraries can be incorporated into other open source projects and published on GitHub, effectively broadening the scope and scale of the attacks.

"These findings reflect careful planning and thought by a threat actor, who proves that obfuscation techniques on PyPI have evolved," the company said.

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

[PyPI Repository](https://thehackernews.com/search/label/PyPI%20Repository)[Python Package Index](https://thehackernews.com/search/label/Python%20Package%20Index)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zer...