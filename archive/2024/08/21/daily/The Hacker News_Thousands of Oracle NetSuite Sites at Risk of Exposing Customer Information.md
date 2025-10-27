---
title: Thousands of Oracle NetSuite Sites at Risk of Exposing Customer Information
url: https://thehackernews.com/2024/08/thousands-of-oracle-netsuite-sites-at.html
source: The Hacker News
date: 2024-08-21
fetch_date: 2025-10-06T18:08:53.296855
---

# Thousands of Oracle NetSuite Sites at Risk of Exposing Customer Information

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

# [Thousands of Oracle NetSuite Sites at Risk of Exposing Customer Information](https://thehackernews.com/2024/08/thousands-of-oracle-netsuite-sites-at.html)

**Aug 20, 2024**Ravie LakshmananEnterprise Security / Data Breach

[![Oracle NetSuite Sites](data:image/png;base64... "Oracle NetSuite Sites")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4s-cid3VsxVmEYlGPKkLJXI6iwtQ0-xtNnf2fXxzP0FTXoedzXMQtL4Cw-HDYqDB1bAnaiiAA2HMSXP-VHjnaOGqfvGVm6hweYuYlbJq1WjWhn1eum43xhOhOWI-9dQW4lsbkm0MIZGY0e2ueGY71Kwx9eOE9Cak20LTU2aOQkZVaDlVy6vaLINPchJSS/s790-rw-e365/oracle.png)

Cybersecurity researchers are warning about the discovery of thousands of externally-facing Oracle NetSuite e-commerce sites that have been found susceptible to leaking sensitive customer information.

"A potential issue in NetSuite's SuiteCommerce platform could allow attackers to access sensitive data due to misconfigured access controls on custom record types (CRTs)," AppOmni's Aaron Costello [said](https://appomni.com/blog/oracle-netsuite-data-exposure-analysis/).

It's worth emphasizing here that the issue is not a security weakness in the NetSuite product, but rather a customer misconfiguration that can lead to leakage of confidential data. The information exposed includes full addresses and mobile phone numbers of registered customers of the e-commerce sites.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack scenario detailed by AppOmni exploits CRTs that employ table-level access controls with the "No Permission Required" access type, which grants unauthenticated users access to data by making use of NetSuite's record and search APIs.

That said, for this attack to succeed, there are a number of prerequisites, the foremost being need for the attacker to know the name of CRTs in use.

To mitigate the risk, it's recommended that site administrators tighten access controls on CRTs, set sensitive fields to "None" for public access, and consider temporarily taking impacted sites offline to prevent data exposure.

"The easiest solution from a security standpoint may involve changing the Access Type of the record type definition to either 'Require Custom Record Entries Permission' or 'Use Permission List,'" Costello said.

The disclosure comes as Cymulate detailed a way to manipulate the credential validation process in Microsoft Entra ID (formerly Azure Active Directory) and circumvent authentication in hybrid identity infrastructures, allowing attackers to sign in with high privileges inside the tenant and establish persistence.

The attack, however, requires an adversary to have admin access on a server hosting a Pass-Through Authentication (PTA) agent, a module that allows users to sign in to both on-premises and cloud-based applications using Entra ID. The issue is rooted in Entra ID when syncing multiple on-premises domains to a single Azure tenant.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This issue arises when authentication requests are mishandled by pass-through authentication (PTA) agents for different on-prem domains, leading to potential unauthorized access," security researchers Ilan Kalendarov and Elad Beber [said](https://cymulate.com/blog/exploiting-pta-credential-validation-in-azure-ad/).

"This vulnerability effectively turns the PTA agent into a double agent, allowing attackers to log in as any synced AD user without knowing their actual password; this could potentially grant access to a global admin user if such privileges were assigned."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[E-commerce Security](https://thehackernews.com/search/label/E-commerce%20Security)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Identity Management](https://thehackernews.com/search/label/Identity%20Management)[oracle](https://thehackernews.com/search/label/oracle)[Oracle NetSuite](https://thehackernews.com/search/label/Oracle%20NetSuite)[threat detection](https://thehackernews.com/search/label/threat%20detection)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "Firs...