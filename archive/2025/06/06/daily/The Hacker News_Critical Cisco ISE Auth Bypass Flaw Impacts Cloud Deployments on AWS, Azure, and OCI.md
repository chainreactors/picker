---
title: Critical Cisco ISE Auth Bypass Flaw Impacts Cloud Deployments on AWS, Azure, and OCI
url: https://thehackernews.com/2025/06/critical-cisco-ise-auth-bypass-flaw.html
source: The Hacker News
date: 2025-06-06
fetch_date: 2025-10-06T22:55:40.414878
---

# Critical Cisco ISE Auth Bypass Flaw Impacts Cloud Deployments on AWS, Azure, and OCI

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

# [Critical Cisco ISE Auth Bypass Flaw Impacts Cloud Deployments on AWS, Azure, and OCI](https://thehackernews.com/2025/06/critical-cisco-ise-auth-bypass-flaw.html)

**Jun 05, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![Cisco ISE Auth Bypass Flaw](data:image/png;base64... "Cisco ISE Auth Bypass Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxfrWnKi_t1de10_O7awp3NR-ZJz0cYU1vSVlAEYVa1FX9KFFa_jzNd1BHXbfdqOR7kpYMHhq0IIEC7d_6_otiRFJ6yXaN1BdersxzeHjZ7JygQdUjRDxENp3nz38-oBPEXGXhLcTUiac2RO8qdKoipYVETNwrUjPUz4cUaiz4Y8IVDMYIt3zu7Xh0XAdW/s790-rw-e365/cisco.jpg)

Cisco has released security patches to address a critical security flaw impacting the Identity Services Engine (ISE) that, if successfully exploited, could allow unauthenticated actors to carry out malicious actions on susceptible systems.

The security defect, tracked as **CVE-2025-20286**, carries a CVSS score of 9.9 out of 10.0. It has been described as a static credential vulnerability.

"A vulnerability in Amazon Web Services (AWS), Microsoft Azure, and Oracle Cloud Infrastructure (OCI) cloud deployments of Cisco Identity Services Engine (ISE) could allow an unauthenticated, remote attacker to access sensitive data, execute limited administrative operations, modify system configurations, or disrupt services within the impacted systems," the company [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-aws-static-cred-FPMjUcm7) in an advisory.

The networking equipment maker, which credited Kentaro Kawane of GMO Cybersecurity for reporting the flaw, noted it's aware of the existence of a proof-of-concept (PoC) exploit. There is no evidence that it has been maliciously exploited in the wild.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Cisco said the issue stems from the fact that credentials are improperly generated when Cisco ISE is being deployed on cloud platforms, causing different deployments to share the same credentials as long as the software release and cloud platform are the same.

Put differently, the static credentials are specific to each release and platform, but are not valid across platforms. As the company highlights, all instances of Cisco ISE release 3.1 on AWS will have the same static credentials.

However, credentials that are valid for access to a release 3.1 deployment would not be valid to access a release 3.2 deployment on the same platform. Furthermore, Release 3.2 on AWS would not have the same credentials as Release 3.2 on Azure.

Successful exploitation of the vulnerability could permit an attacker to extract the user credentials from the Cisco ISE cloud deployment and then use it to access Cisco ISE deployed in other cloud environments through unsecured ports.

This could ultimately allow unauthorized access to sensitive data, execution of limited administrative operations, changes to system configurations, or service disruptions. That said, Cisco ISE is only affected in cases where the Primary Administration node is deployed in the cloud. Primary Administration nodes that are on-premises are not impacted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The following versions are affected -

* AWS - Cisco ISE 3.1, 3.2, 3.3, and 3.4
* Azure - Cisco ISE 3.2, 3.3, and 3.4
* OCI - Cisco ISE 3.2, 3.3, and 3.4

While there are no workarounds to address CVE-2025-20286, Cisco is recommending that users restrict traffic to authorized administrators or run the "application reset-config ise" command to reset user passwords to a new value. However, it bears noting that running the command will reset Cisco ISE to the factory configuration.

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

[AWS](https://thehackernews.com/search/label/AWS)[cisco](https://thehackernews.com/search/label/cisco)[Cloud Infrastructure](https://thehackernews.com/search/label/Cloud%20Infrastructure)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Configuration Management](https://thehackernews.com/search/label/Configuration%20Management)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Microsoft Azure](https://thehackernews.com/search/label/Microsoft%20Azure)[network security](https://thehackernews.com/search/label/network%20security)[oracle](https://thehackernews.com/search/label/oracle)[Threat Mitigation](https://thehackernews.com/search/label/Threat%20Mitigation)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https...