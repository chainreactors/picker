---
title: Jenkins Security Alert: New Security Flaws Could Allow Code Execution Attacks
url: https://thehackernews.com/2023/03/jenkins-security-alert-new-security.html
source: The Hacker News
date: 2023-03-09
fetch_date: 2025-10-04T09:03:33.531573
---

# Jenkins Security Alert: New Security Flaws Could Allow Code Execution Attacks

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

# [Jenkins Security Alert: New Security Flaws Could Allow Code Execution Attacks](https://thehackernews.com/2023/03/jenkins-security-alert-new-security.html)

**Mar 08, 2023**Ravie LakshmananOpen Source / Automation Tool

[![Jenkins Security Alert](data:image/png;base64... "Jenkins Security Alert")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAU88DKbsfQojJpA-5ZrcCnWOB0ycSthuPbnsEq4e8dw6CTQ9EYQ05cHZ9Ra2W7d6B-O9Zh9ChZtQGe4BC-WoXYJCaR3jYFnK9cmcpq2amJSUMWOmxzTAwxE1baDmsDelD6QZ1N9BFAeKQKfAWmvSRSqRQwnXYak0j6yAh0U3v3elr1k1D6_2WgAlt/s790-rw-e365/Jenkins.png)

A pair of severe security vulnerabilities have been disclosed in the Jenkins open source automation server that could lead to code execution on targeted systems.

The flaws, tracked as [CVE-2023-27898](https://nvd.nist.gov/vuln/detail/CVE-2023-27898) and [CVE-2023-27905](https://nvd.nist.gov/vuln/detail/CVE-2023-27905), impact the Jenkins server and Update Center, and have been collectively christened **CorePlague** by cloud security firm Aqua. All versions of Jenkins versions prior to 2.319.2 are vulnerable and exploitable.

"Exploiting these vulnerabilities could allow an unauthenticated attacker to execute arbitrary code on the victim's Jenkins server, potentially leading to a complete compromise of the Jenkins server," the company said in a [report](https://blog.aquasec.com/jenkins-server-vulnerabilities) shared with The Hacker News.

The shortcomings are the result of how Jenkins processes plugins available from the [Update Center](https://www.jenkins.io/templates/updates/), thereby potentially enabling a threat actor to upload a plugin with a malicious payload and trigger a cross-site scripting (XSS) attack.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Once the victim opens the '[Available Plugin Manager](https://www.jenkins.io/doc/book/managing/plugins/)' on their Jenkins server, the XSS is triggered, allowing attackers to run arbitrary code on the Jenkins Server utilizing the [Script Console API](https://www.jenkins.io/doc/book/managing/script-console/)," Aqua said.

Since it's also a case of stored XSS wherein the JavaScript code is injected into the server, the vulnerability can be activated without having to install the plugin or even visit the URL to the plugin in the first place.

Troublingly, the flaws could also affect self-hosted Jenkins servers and be exploited even in scenarios where the server is not publicly accessible over the internet since the public Jenkins Update Center could be "injected by attackers."

The attack, however, banks on the prerequisite that the rogue plugin is compatible with the Jenkins server and is surfaced on top of the main feed on the "Available Plugin Manager" page.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This, Aqua said, can be rigged by "uploading a plugin that contains all plugin names and popular keywords embedded in the description," or artificially boost the download counts of the plugin by submitting requests from fake instances.

Following responsible disclosure on January 24, 2023, patches have been [released](https://www.jenkins.io/security/advisory/2023-03-08/) by Jenkins for [Update Center](https://github.com/jenkins-infra/update-center2/releases/tag/update-center2-3.15) and [server](https://www.jenkins.io/download/). Users are recommended to update their Jenkins server to the latest available version to mitigate potential risks.

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

[Cross-site Scripting](https://thehackernews.com/search/label/Cross-site%20Scripting)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Jenkins](https://thehackernews.com/search/label/Jenkins)[xss](https://thehackernews.com/search/label/xss)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target ...