---
title: Researchers Detail Azure SFX Flaw That Could've Allowed Attackers to Gain Admin Access
url: https://thehackernews.com/2022/10/researchers-detail-azure-sfx-flaw-that.html
source: The Hacker News
date: 2022-10-20
fetch_date: 2025-10-03T20:26:20.062102
---

# Researchers Detail Azure SFX Flaw That Could've Allowed Attackers to Gain Admin Access

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

# [Researchers Detail Azure SFX Flaw That Could've Allowed Attackers to Gain Admin Access](https://thehackernews.com/2022/10/researchers-detail-azure-sfx-flaw-that.html)

**Oct 19, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-Qj4H60yBEMC5f-_0JGD02J2wg0ZC_FI9TiEt-_4u9MqG5akmevGn28p1vkyeEok0GuDb1cmCeS-dKv4s9E9MAyuemdwhbNSyLxRxEo4ASVcE07gf6uHoE6u0DVBxU0iIkAyqu0iUBYeL9ZqCg6o6FL-pAlkZMqJQQ2RJ3GPav1RL0F1B98MWXdph/s790-rw-e365/xss.jpg)

Cybersecurity researchers have shared more details about a now-patched security flaw in Azure Service Fabric Explorer (SFX) that could potentially enable an attacker to gain administrator privileges on the cluster.

The vulnerability, tracked as [CVE-2022-35829](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-35829), carries a CVSS severity rating of 6.2 and was addressed by Microsoft as part of its [Patch Tuesday updates](https://thehackernews.com/2022/10/microsoft-patch-tuesday-fixes-new.html) last week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Orca Security, which [discovered and reported](https://orca.security/resources/blog/fabrixss-vulnerability-azure-fabric-explorer) the flaw to the tech giant on August 11, 2022, dubbed the vulnerability **FabriXss** (pronounced "fabrics"). It impacts Azure Fabric Explorer version 8.1.316 and prior.

SFX is described by Microsoft as an [open-source tool](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-visualizing-your-cluster) for inspecting and managing [Azure Service Fabric](https://azure.microsoft.com/en-us/products/service-fabric/#overview) clusters, a distributed systems platform that's used to build and deploy microservices-based cloud applications.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlv6AcbH6jn-NIGnUXG3TWO9cCNMzXDiRP8ek0A2v-JjjKpWBDbHF0T2_zCD0BIIGmD6w4zpCTDGDqHPLQ4JPvLVgzMOWuxeZ3ywScMhF6jKNn4ypJShVSUfchScSpXSfWOVZ0FaUT9ajPZjDuQBm-GqzLg4n83nC0UaYwrMloG7RMp_JTnT_SAhck/s790-rw-e365/1.jpg)

The vulnerability is rooted in the fact that a user with [permissions](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-fabric-settings#securityclientaccess) to "Create Compose Application" through the SFX client can leverage the privileges to create a rogue app and abuse a stored cross-site scripting ([XSS](https://www.imperva.com/learn/application-security/cross-site-scripting-xss-attacks/)) flaw in the "Application name" field to slip the payload.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Armed with this exploit, an adversary can send the specially crafted input during the application creation step, eventually leading to its execution.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjo7yU5UFWOJmEjrm0lhcjgdLF336mtXD309IUavrO_XOamR_ZquJWhrotBSY8rd5VgFJ_ijYoCRM3P0nzcwkJ9h4n0gfMwxqqqFMasL_1BXTFRDi9doHCNqLw2MkbNwDz2OvoJWG7jvzIMRt15bi29m5sNikAXhtw95kcEfvsxGlwh3Ec0dzOOlawm/s790-rw-e365/demo.gif)

"This includes performing a Cluster Node reset, which erases all customized settings such as passwords and security configurations, allowing an attacker to create new passwords and gain full [Administrator permissions](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-security-roles)," Orca Security researchers Lidor Ben Shitrit and Roee Sagi said.

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

[Azure](https://thehackernews.com/search/label/Azure)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Network...