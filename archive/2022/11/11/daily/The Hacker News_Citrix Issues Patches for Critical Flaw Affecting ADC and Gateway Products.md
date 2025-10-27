---
title: Citrix Issues Patches for Critical Flaw Affecting ADC and Gateway Products
url: https://thehackernews.com/2022/11/citrix-issues-patches-for-critical-flaw.html
source: The Hacker News
date: 2022-11-11
fetch_date: 2025-10-03T22:26:26.406104
---

# Citrix Issues Patches for Critical Flaw Affecting ADC and Gateway Products

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

# [Citrix Issues Patches for Critical Flaw Affecting ADC and Gateway Products](https://thehackernews.com/2022/11/citrix-issues-patches-for-critical-flaw.html)

**Nov 10, 2022**Ravie Lakshmanan

[![Citrix](data:image/png;base64... "Citrix")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl_Io9o_ss3jBoKV8NtT-zmyLwXCG7qjvOc3kB1P5gGAH-W_PScN3dFRDKCwa0yY4PPZafytqsKw1y1aWS_zT4RC0VW1uxp2mnTyTgOPtevIUIYQRZXSfCfksb54h3LZ5uGmJaqwkSsj2Kh1NpIuj8xniQMlNZ8Bcrhr9UTAB3FPhiGRiM4Jlx2rWZ/s790-rw-e365/citrix.jpg)

Citrix has released [security updates](https://support.citrix.com/article/CTX463706/citrix-gateway-and-citrix-adc-security-bulletin-for-cve202227510-cve202227513-and-cve202227516) to address a critical authentication bypass flaw in the application delivery controller (ADC) and Gateway products that could be exploited to take control of affected systems.

Successful exploitation of the issues could enable an adversary to gain authorized access, perform remote desktop takeover, and even circumvent defenses against login brute-force attempts under specific configurations.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

* **CVE-2022-27510** - Unauthorized access to Gateway user capabilities
* **CVE-2022-27513** - Remote desktop takeover via phishing
* **CVE-2022-27516** - User login brute-force protection functionality bypass

The following supported versions of Citrix ADC and Citrix Gateway are affected by the flaws -

* Citrix ADC and Citrix Gateway 13.1 before 13.1-33.47
* Citrix ADC and Citrix Gateway 13.0 before 13.0-88.12
* Citrix ADC and Citrix Gateway 12.1 before 12.1.65.21
* Citrix ADC 12.1-FIPS before 12.1-55.289
* Citrix ADC 12.1-NDcPP before 12.1-55.289

Exploitation, however, banks on the prerequisite that the appliances are either configured as a VPN (Gateway) or, alternatively, an authentication, authorization and accounting ([AAA](https://docs.citrix.com/en-us/citrix-adc/current-release/aaa-tm/how-citrix-adc-aaa-works.html)) virtual server in the case of CVE-2022-27516.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

One top of that, CVE-2022-27513 and CVE-2022-27516 also apply only when the RDP proxy feature and the user lockout functionality "Max Login Attempts" are set up, respectively.

The cloud computing and virtualization technology company said that no action is required from customers relying on cloud services managed directly by Citrix.

Jarosław Jahrek Kamiński, a researcher at Polish penetration testing firm Securitum, has been credited with discovering and reporting the vulnerabilities.

"Affected customers of Citrix ADC and Citrix Gateway are recommended to install the relevant updated versions of Citrix ADC or Citrix Gateway as soon as possible," Citrix said in an advisory.

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

[Authentication bypass](https://thehackernews.com/search/label/Authentication%20bypass)[Citrix](https://thehackernews.com/search/label/Citrix)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits De...