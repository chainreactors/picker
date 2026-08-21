---
title: Critical NetScaler Flaw Can Bypass Authentication on Certain Gateway and AAA Servers
url: https://thehackernews.com/2026/08/critical-netscaler-flaw-can-bypass.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:09.082493
---

# Critical NetScaler Flaw Can Bypass Authentication on Certain Gateway and AAA Servers

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Critical NetScaler Flaw Can Bypass Authentication on Certain Gateway and AAA Servers](https://thehackernews.com/2026/08/critical-netscaler-flaw-can-bypass.html)

**Ravie Lakshmanan**Aug 20, 2026Network Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoCXrYMA_j7aJrrdIZKt2gQwTWYXhhHZTfBvrNcgpLLBTa5hzcmDNguBKwBhiD8p7kO5K2OeQYVbIPg2HHDBwu9LNzR6oAFE-znmFWIgjY_XzA0qdy-rA8XzV_uGvsxLWRNXCyyOlUKdDV0LGrXPN15wxYsTuZslyecGQ1cqE2OKdX5cocpp74uXenwdj0/s1700-e365/citrix.jpg)

Citrix has [released](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-netscaler-adc-and-netscaler-gateway-vulnerabilities-r1602/) updates to address two security flaws impacting NetScaler ADC and NetScaler Gateway deployments, including a critical-severity authentication bypass vulnerability.

According to the cloud computing and virtualization technology company, the issues [affect](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696939) customer-managed NetScaler ADC and NetScaler Gateway, including certain FIPS and NDcPP builds, as well as SecurAccess ZTNA Hybrid deployments that use customer-managed NetScaler instances.

It bears noting that the vulnerabilities do not apply to Citrix-managed cloud services or Citrix-managed Adaptive Authentication, as the necessary updates have already been applied. The list of impacted NetScaler versions is below -

* NetScaler ADC and NetScaler Gateway 14.1 BEFORE 14.1-73.32
* NetScaler ADC and NetScaler Gateway 13.1 BEFORE 13.1-63.21
* NetScaler ADC FIPS BEFORE 14.1-73.32 FIPS
* NetScaler ADC FIPS and NDcPP BEFORE 13.1-37.277

The first of the two vulnerabilities is CVE-2026-19489 (CVSS score: 8.8), a memory overflow vulnerability that may lead to unpredictable behavior or denial-of-service (DoS). However, it applies only when Session Initiation Protocol Application Layer Gateway (SIP ALG) is enabled on a Large Scale NAT (LSN) group configuration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

CVE-2026-19490 (CVSS score: 9.3), the more severe of the two, is an authentication bypass vulnerability that affects appliances configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or an AAA virtual server, assuming the following version-specific requirements are met -

* 14.1-43.56 or later - Applicable only when configured with a SAML action AND NetScaler is configured with Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA vserver
* 14.1-66.68-FIPS or later - Applicable only when configured with a SAML action AND NetScaler is configured with Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA vserver
* 14.1-43.55 or earlier - Applicable when configured with Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy ) or AAA vserver
* 13.1-61.28 or later - Applicable only when configured with a SAML action
* 13.1-61.27 or earlier - Applicable when configured with Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA vserver
* 13.1 FIPS - Applicable when configured with Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA vserver

"Customers should also review their configurations to determine whether the documented preconditions apply," Citrix said. "Prioritization should be based on exposure, deployment role, and whether the affected configuration is enabled."

For CVE-2026-19489, customers can check if their device meets the precondition by inspecting their NetScaler configuration for the specified string -

* add lsn group.\*sipalg.\*

Similarly, for CVE-2026-19490, customers can verify their NetScaler configuration for the below string -

* add authentication samlAction.\* (SAML action configuration)
* add authentication vserver .\* or add vpn vserver .\* (for AAA or VPN vserver)

"Additionally, this vulnerability can be mitigated by using signatures if you are using NetScaler Console (Service or on-prem) and if the NetScaler firmware version is higher than 14.1-60.52 and 13.1-63.16 or higher, which have a feature called [Global Deny Lists](https://community.citrix.com/techzone-blogs/netscaler/netscaler-global-deny-list-always-on-protection-for-the-threats-you-havent-modeled-yet-r1254/#2_Unconditional_evaluation_in_the_request_pipeline__3e5a90) that consumes the signatures and automatically applies the signatures to NetScaler appliances managed via NetScaler Console," Citrix said. "The feature is enabled by default."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The updates are available in the following versions -

* NetScaler ADC and NetScaler Gateway 14.1-73.32 or later
* NetScaler ADC and NetScaler Gateway 13.1-63.21 or later
* NetScaler ADC FIPS 14.1-73.32 FIPS or later
* NetScaler ADC FIPS and NDcPP 13.1-37.277 or later

Citrix has credited Samarth Vashisht from the pen-test team at JPMorgan Chase for discovering and reporting the flaws. Although there is no evidence that the shortcomings have been exploited in the wild, newly disclosed Citrix vulnerabilities have been a lucrative target for attackers.

Last month, an insufficient input validation vulnerability in NetScaler ADC and NetScaler Gateway ([CVE-2026-8451](https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html), CVSS score: 8.8) witnessed active exploitation efforts less than 24 hours of public disclosure.

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
...