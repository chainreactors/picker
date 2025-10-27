---
title: Critical Flaw in Cisco IP Phone Series Exposes Users to Command Injection Attack
url: https://thehackernews.com/2023/03/critical-flaw-in-cisco-ip-phone-series.html
source: The Hacker News
date: 2023-03-03
fetch_date: 2025-10-04T08:33:44.154401
---

# Critical Flaw in Cisco IP Phone Series Exposes Users to Command Injection Attack

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

# [Critical Flaw in Cisco IP Phone Series Exposes Users to Command Injection Attack](https://thehackernews.com/2023/03/critical-flaw-in-cisco-ip-phone-series.html)

**Mar 02, 2023**Ravie LakshmananEnterprise Security / Network Security

[![Cisco IP Phone](data:image/png;base64... "Cisco IP Phone")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl-qohNH4V4gI0u-vsrL_3MAAflocpEghlUoSOFrFRpzVYba1VnfaGnupQBOklMO1B0hn03bvuiDoysw0c36oirplhz-n_PbvXZWCVEMTS2Lt4xvW5g6_kTggj_FGMKXGy8UqznxN0EnEJ6op4GvonLE5_ApDK2lgg-Qt4JXDCv9yg7z2yKo79cRIR/s790-rw-e365/ip-phone.png)

Cisco on Wednesday rolled out [security updates](https://sec.cloudapps.cisco.com/security/center/publicationListing.x) to address a critical flaw impacting its IP Phone 6800, 7800, 7900, and 8800 Series products.

The vulnerability, tracked as CVE-2023-20078, is rated 9.8 out of 10 on the CVSS scoring system and is described as a command injection bug in the web-based management interface arising due to insufficient validation of user-supplied input.

Successful exploitation of the bug could allow an unauthenticated, remote attacker to inject arbitrary commands that are executed with the highest privileges on the underlying operating system.

"An attacker could exploit this vulnerability by sending a crafted request to the web-based management interface," Cisco [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ip-phone-cmd-inj-KMFynVcP) in an alert published on March 1, 2023.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also patched by the company is a high-severity denial-of-service (DoS) vulnerability affecting the same set of devices, as well as the Cisco Unified IP Conference Phone 8831 and Unified IP Phone 7900 Series.

CVE-2023-20079 (CVSS score: 7.5), also a result of insufficient validation of user-supplied input in the web-based management interface, could be abused by an adversary to cause a DoS condition.

While Cisco has released Cisco Multiplatform Firmware version 11.3.7SR1 to resolve CVE-2023-20078, the company said it does not plan to fix CVE-2023-20079, as both the Unified IP Conference Phone models have entered end-of-life (EoL).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The company said it's not aware of any malicious exploitation attempts targeting the flaw. It also said the flaws were discovered during internal security testing.

The advisory comes as Aruba Networks, a subsidiary of Hewlett Packard Enterprise, released an update to ArubaOS to [remediate](https://www.arubanetworks.com/assets/alert/ARUBA-PSA-2023-002.txt) multiple unauthenticated command injection and stack-based buffer overflow flaws (from CVE-2023-22747 through CVE-2023-22752, CVSS scores: 9.8) that could result in code execution.

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

[Cisco IP Phones](https://thehackernews.com/search/label/Cisco%20IP%20Phones)[Command Injection](https://thehackernews.com/search/label/Command%20Injection)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64...