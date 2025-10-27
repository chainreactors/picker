---
title: New Zero-Day Flaw in Apache OFBiz ERP Allows Remote Code Execution
url: https://thehackernews.com/2024/08/new-zero-day-flaw-in-apache-ofbiz-erp.html
source: The Hacker News
date: 2024-08-07
fetch_date: 2025-10-06T18:06:17.742096
---

# New Zero-Day Flaw in Apache OFBiz ERP Allows Remote Code Execution

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

# [New Zero-Day Flaw in Apache OFBiz ERP Allows Remote Code Execution](https://thehackernews.com/2024/08/new-zero-day-flaw-in-apache-ofbiz-erp.html)

**Aug 06, 2024**Ravie LakshmananEnterprise Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6z03tPT6k-6mpiOgUoksJJxdNimYFqqogPJiPVpjyJ5GGSA3I-NhvltV2FinTF0mfVbQUdlAKR9vOnmfU5j3BkA8cuK2ls7p2-bpurEsJRUalWbP1YqInS-o1G73Qza8BHDLY2xYBaRezSRQdRItCrVtb1WbsxPkJDlG9GT_b0aQAOiCqsoGjD32aJMoZ/s790-rw-e365/apache.png)

A new zero-day pre-authentication remote code execution vulnerability has been disclosed in the Apache OFBiz open-source enterprise resource planning (ERP) system that could allow threat actors to achieve remote code execution on affected instances.

Tracked as **[CVE-2024-38856](https://nvd.nist.gov/vuln/detail/CVE-2024-38856)**, the flaw has a CVSS score of 9.8 out of a maximum of 10.0. It affects Apache OFBiz versions prior to 18.12.15.

"The root cause of the vulnerability lies in a flaw in the authentication mechanism," SonicWall, which discovered and reported the shortcoming, said in a statement.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This flaw allows an unauthenticated user to access functionalities that generally require the user to be logged in, paving the way for remote code execution."

CVE-2024-38856 is also a patch bypass for [CVE-2024-36104](https://nvd.nist.gov/vuln/detail/CVE-2024-36104), a path traversal vulnerability that was addressed in early June with the release of 18.12.14.

SonicWall described the flaw as residing in the override view functionality that exposes critical endpoints to unauthenticated threat actors, who could leverage it to achieve remote code execution via specially crafted requests.

"Unauthenticated access was allowed to the ProgramExport endpoint by chaining it with any other endpoints that do not require authentication by abusing the override view functionality," security researcher Hasib Vhora [said](https://blog.sonicwall.com/en-us/2024/08/sonicwall-discovers-second-critical-apache-ofbiz-zero-day-vulnerability/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as another critical path traversal vulnerability in OFBiz that could result in remote code execution ([CVE-2024-32113](https://nvd.nist.gov/vuln/detail/CVE-2024-32113)) has since come under [active exploitation](https://thehackernews.com/2024/08/mirai-botnet-targeting-ofbiz-servers.html) to deploy the Mirai botnet. It was patched in May 2024.

In December 2023, SonicWall also [disclosed](https://thehackernews.com/2023/12/critical-zero-day-in-apache-ofbiz-erp.html) a then-zero-day flaw in the same software (CVE-2023-51467) that made it possible to bypass authentication protections. It was subsequently subjected to a large number of exploitation attempts.

### Update

The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on August 7, 2024, [added](https://www.cisa.gov/news-events/alerts/2024/08/07/cisa-adds-two-known-exploited-vulnerabilities-catalog) CVE-2024-32113 to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, requiring federal agencies to apply the fixes by August 28, 2024.

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

[Apache](https://thehackernews.com/search/label/Apache)[Authentication bypass](https://thehackernews.com/search/label/Authentication%20bypass)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[ERP System](https://thehackernews.com/search/label/ERP%20System)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](dat...