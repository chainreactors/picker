---
title: Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks
url: https://thehackernews.com/2026/03/citrix-urges-patching-critical.html
source: The Hacker News
date: 2026-03-24
fetch_date: 2026-03-25T04:18:09.606938
---

# Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks

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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks](https://thehackernews.com/2026/03/citrix-urges-patching-critical.html)

**Ravie Lakshmanan**Mar 24, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMCnGCq_DsAE40JVqQy2HjOcbqucRBcpx0JOpEQM9SZplWbse_yzvfQGRG8Uux9NVkQhQrHYzTIlb3b58b47kkLOfIBcxeaMVT7SlUjBSr3URnME7qL5P3ZqJgVw3bGX0NY_hYsvhAbTTJ7PZk-mmpl949AALvrsV0JkZEQD82ah-B2jlOBz-oGC-P4xaY/s1700-e365/citrix.jpg)

Citrix has released [security updates](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696300) to address two vulnerabilities in [NetScaler](https://docs.netscaler.com/en-us/citrix-adc/current-release/getting-started-with-citrix-adc.html) ADC and NetScaler Gateway, including a critical flaw that could be exploited to leak sensitive data from the application.

The vulnerabilities are listed below -

* **CVE-2026-3055** (CVSS score: 9.3) - Insufficient input validation leading to memory overread
* **CVE-2026-4368** (CVSS score: 7.7) - Race condition leading to user session mixup

Cybersecurity company Rapid7 [said](https://www.rapid7.com/blog/post/etr-cve-2026-3055-citrix-netscaler-adc-and-netscaler-gateway-out-of-bounds-read/) that CVE-2026-3055 refers to an out-of-bounds read that could be exploited by unauthenticated remote attackers to leak potentially sensitive information from the appliance's memory.

However, for exploitation to be successful, the Citrix ADC or Citrix Gateway appliance must be configured as a SAML Identity Provider (SAML IDP), which means default configurations are unaffected. To determine if the device has been configured as a SAML IDP Profile, Citrix is urging customers to inspect their NetScaler Configuration for the specified string: "add authentication samlIdPProfile .\*"

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

CVE-2026-4368, on the other hand, requires the appliance to be configured as a gateway (i.e., SSL VPN, ICA Proxy, CVPN, and RDP Proxy) or an Authentication, Authorization, and Accounting ([AAA](https://docs.netscaler.com/en-us/citrix-adc/current-release/aaa-tm.html)) server. Customers can check the NetScaler Configuration to ascertain if their devices have been configured as either of the nodes -

* AAA virtual server - add authentication vserver .\*
* Gateway - add vpn vserver .\*

The vulnerabilities affect NetScaler ADC and NetScaler Gateway versions 14.1 before 14.1-66.59 and 13.1 before 13.1-62.23, as well as NetScaler ADC 13.1-FIPS and 13.1-NDcPP before 13.1-37.262. Users are advised to apply the latest updates as soon as possible for optimal protection.

While there is no evidence that the shortcomings have been exploited in the wild, security flaws in NetScaler devices have been repeatedly exploited by threat actors ([CVE-2023-4966](https://thehackernews.com/2023/11/lockbit-ransomware-exploiting-critical.html), aka Citrix Bleed, [CVE-2025-5777](https://thehackernews.com/2025/06/citrix-bleed-2-flaw-enables-token-theft.html), aka Citrix Bleed 2, [CVE-2025-6543, and CVE-2025-7775](https://thehackernews.com/2025/08/citrix-patches-three-netscaler-flaws.html)), making it imperative that users take steps to update their instances.

"CVE-2026-3055 allows unauthenticated attackers to leak and read sensitive memory from NetScaler ADC deployments. If it sounds familiar, it's because it is – this vulnerability sounds suspiciously similar to Citrix Bleed and Citrix Bleed 2, which continue to represent a trauma event for many," watchTowr CEO and founder Benjamin Harris told The Hacker News.

"NetScalers are [critical solutions](https://labs.watchtowr.com/is-it-citrixbleed4-well-no-is-it-good-also-no-citrix-netscalers-memory-leak-rxss-cve-2025-12101/) that have been continuously targeted for initial access into enterprise environments. While the advisory just went live, defenders need to act quickly. Anyone running impacted versions needs to patch urgently. Imminent exploitation is highly likely."

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

[Citrix](https://thehackernews.com/search/label/Citrix), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Data Leakage](https://thehackernews.com/search/label/Data%20Leakage), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [NetScaler](https://thehackernews.com/search/label/NetScaler), [network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials](data:image/svg+xml;base64... "FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials")

FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials](https://thehackernews.com/2026/03/fortigate-devices-exploited-to-breach.html)

[![Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days](data:image/svg+xml;base64... "Microsoft Patches 84 Flaws in M...