---
title: New RansomExx Ransomware Variant Rewritten in the Rust Programming Language
url: https://thehackernews.com/2022/11/new-ransomexx-ransomware-variant.html
source: The Hacker News
date: 2022-11-25
fetch_date: 2025-10-03T23:45:54.651717
---

# New RansomExx Ransomware Variant Rewritten in the Rust Programming Language

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

# [New RansomExx Ransomware Variant Rewritten in the Rust Programming Language](https://thehackernews.com/2022/11/new-ransomexx-ransomware-variant.html)

**Nov 24, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs2_a02HgaWg8D0cBLBNdKovmiU2o_GaQAI2_w5gX_o_LDFw07DsCHsvcVy91Y03jQstz271la30bZQeiLtFKyKc0ULBtUmpHcz1RXNQ_WXgyfPzDslA6Vn7vSZFdSOL8j8R7PydQb7WZXk_GVItyQEvm1HkZyZ3BW68KAH8syuY8IqaMqRDxMPIaq/s790-rw-e365/rasnowmare.png)

The operators of the RansomExx ransomware have become the latest to develop a new variant fully rewritten in the Rust programming language, following other strains like [BlackCat](https://thehackernews.com/2022/06/blackcat-ransomware-gang-targeting.html), [Hive](https://thehackernews.com/2022/07/hive-ransomware-upgrades-to-rust-for.html), and [Luna](https://thehackernews.com/2022/07/new-rust-based-ransomware-family.html).

The latest version, dubbed RansomExx2 by the threat actor known as Hive0091 (aka DefrayX), is primarily designed to run on the Linux operating system, although it's expected that a Windows version will be released in the future.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

RansomExx, also known as Defray777 and Ransom X, is a [ransomware](https://www.emsisoft.com/en/blog/41027/ransomware-profile-ransomexx/) [family](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-ransomexx) that's known to be active since 2018. It has since been linked to a number of attacks on government agencies, manufacturers, and other high-profile entities like Embraer and GIGABYTE.

"Malware written in Rust often benefits from lower [antivirus] detection rates (compared to those written in more common languages) and this may have been the primary reason to use the language," IBM Security X-Force researcher Charlotte Hammond [said](https://securityintelligence.com/posts/ransomexx-upgrades-rust/) in a report published this week.

RansomExx2 is functionally similar to its C++ predecessor and it takes a list of target directories to encrypt as command line inputs.

Once executed, the ransomware recursively goes through each of the specified directories, followed by enumerating and encrypting the files using the [AES-256 algorithm](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).

A ransom note containing the demand is ultimately dropped in each of the encrypted directory upon completion of the step.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development illustrates a new trend where a growing number of malicious actors are building malware and ransomware with [lesser-known programming languages](https://thehackernews.com/2021/07/hackers-turning-to-exotic-programming.html) like Rust and Go, which not only offer increased cross-platform flexibility but can also evade detection.

"RansomExx is yet another major ransomware family to switch to Rust in 2022," Hammond explained.

"While these latest changes by RansomExx may not represent a significant upgrade in functionality, the switch to Rust suggests a continued focus on the development and innovation of the ransomware by the group, and continued attempts to evade detection."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)[Rust Programming Language](https://thehackernews.com/search/label/Rust%20Programming%20Language)[Windows](https://thehackernews.com/search/label/Windows)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Lin...