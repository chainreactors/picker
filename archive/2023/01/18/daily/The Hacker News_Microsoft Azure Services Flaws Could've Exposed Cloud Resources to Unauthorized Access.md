---
title: Microsoft Azure Services Flaws Could've Exposed Cloud Resources to Unauthorized Access
url: https://thehackernews.com/2023/01/microsoft-azure-services-flaws-couldve.html
source: The Hacker News
date: 2023-01-18
fetch_date: 2025-10-04T04:11:41.856551
---

# Microsoft Azure Services Flaws Could've Exposed Cloud Resources to Unauthorized Access

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

# [Microsoft Azure Services Flaws Could've Exposed Cloud Resources to Unauthorized Access](https://thehackernews.com/2023/01/microsoft-azure-services-flaws-couldve.html)

**Jan 17, 2023**Ravie LakshmananCloud Security / Bug Report

[![Microsoft Azure Services](data:image/png;base64... "Microsoft Azure Services")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzDIX0mKDDTl8b5U35Cv72fGLjNOaay_fbcni0Zry8T-uu3Lps8y2eX2-YlPcaKiJ7ytY-JCFJGvhoh7eks922quPbKdIzPThjY7a2Rf7eFWECoxC2QVUIOcgHir73VMowg-uxBAEq-Qj4nXZhXC_NhQymWHn6XwLwHbT7RcKLCGbPLeHrEHAvXNfA/s790-rw-e365/azure.png)

Four different Microsoft Azure services have been found vulnerable to server-side request forgery ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)) attacks that could be exploited to gain unauthorized access to cloud resources.

The security issues, which were discovered by Orca between October 8, 2022 and December 2, 2022 in Azure API Management, Azure Functions, Azure Machine Learning, and Azure Digital Twins, have since been addressed by Microsoft.

"The discovered Azure SSRF vulnerabilities allowed an attacker to scan local ports, find new services, endpoints, and sensitive files - providing valuable information on possibly vulnerable servers and services to exploit for initial entry and the location of sensitive information to target," Orca researcher Lidor Ben Shitrit [said](https://orca.security/resources/blog/ssrf-vulnerabilities-in-four-azure-services) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Two of the vulnerabilities affecting Azure Functions and Azure Digital Twins could be abused without requiring any authentication, enabling a threat actor to seize control of a server without even having an Azure account in the first place.

SSRF attacks could have [serious consequences](https://learn.snyk.io/lessons/ssrf-server-side-request-forgery/javascript/) as they enable a malicious interloper to read or update internal resources, and worse, pivot to other parts of the network, breach otherwise unreachable systems to extract valuable data.

Three of the flaws are rated Important in severity, while the SSRF flaw impacting Azure Machine Learning is rated Low in severity. All the weaknesses can be leveraged to manipulate a server to mount further attacks against a susceptible target.

A brief summary of the four vulnerabilities is as follow -

* Unauthenticated SSRF on Azure Digital Twins Explorer via a flaw in the /proxy/blob endpoint that could be exploited to get a response from any service that's suffixed with "blob.core.windows[.]net"
* Unauthenticated SSRF on Azure Functions that could be exploited to enumerate local ports and access internal endpoints
* Authenticated SSRF on Azure API Management service that could be exploited to list internal ports, including one associated with a source code management service that could then be used to access sensitive files
* Authenticated SSRF on Azure Machine Learning service via the /datacall/streamcontent endpoint that could be exploited to fetch content from arbitrary endpoints

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

To mitigate such threats, organizations are recommended to validate all input, ensure that servers are configured to only allow necessary inbound and outbound traffic, avoid misconfigurations, and adhere to the principle of least privilege ([PoLP](https://en.wikipedia.org/wiki/Principle_of_least_privilege)).

"The most notable aspect of these discoveries is arguably the number of SSRF vulnerabilities we were able to find with only minimal effort, indicating just [how prevalent they are](https://orca.security/resources/blog/oracle-server-side-request-forgery-ssrf-attack-metadata/) and the risk they pose in cloud environments," Ben Shitrit said.

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

[Microsoft Azure](https://thehackernews.com/search/label/Microsoft%20Azure)[unauthorized access](https://thehackernews.com/search/label/unauthorized%20access)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-...