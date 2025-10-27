---
title: Researchers Uncover Vulnerabilities in AI-Powered Azure Health Bot Service
url: https://thehackernews.com/2024/08/researchers-uncover-vulnerabilities-in_0471960302.html
source: The Hacker News
date: 2024-08-14
fetch_date: 2025-10-06T18:13:20.208176
---

# Researchers Uncover Vulnerabilities in AI-Powered Azure Health Bot Service

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

# [Researchers Uncover Vulnerabilities in AI-Powered Azure Health Bot Service](https://thehackernews.com/2024/08/researchers-uncover-vulnerabilities-in_0471960302.html)

**Aug 13, 2024**Ravie LakshmananHealthcare / Vulnerability

[![AI-Powered Azure Health Bot Service](data:image/png;base64... "AI-Powered Azure Health Bot Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSe0dy4KxTTrbDUUTRZsUQBpO9XOoiKMJIxv_CC7S-G86Xx70AUu8yI5WqmXyJJbvnZEhSlBcvrKv_KBhRgPOiUa32fNZl8NKvh4sM-kQ6_QSow9hLOlRAH6t_2vHZK-5eaXNHGODzbpYPSA2vz88Kma71MirtDwKjRXgd2NTZNr1gmQPYZwUoamJy29sN/s790-rw-e365/ms.png)

Cybersecurity researchers have discovered two security flaws in Microsoft's Azure Health Bot Service that, if exploited, could permit a malicious actor to achieve lateral movement within customer environments and access sensitive patient data.

The critical issues, now patched by Microsoft, could have allowed access to cross-tenant resources within the service, Tenable said in a new [report](https://www.tenable.com/blog/compromising-microsofts-ai-healthcare-chatbot-service) shared with The Hacker News.

The Azure AI Health Bot Service is a [cloud platform](https://learn.microsoft.com/en-us/azure/health-bot/overview) that enables developers in healthcare organizations to build and deploy AI-powered virtual health assistants and create copilots to manage administrative workloads and engage with their patients.

This includes bots created by insurance service providers to allow customers to look up the status of a claim and ask questions about benefits and services, as well as bots managed by healthcare entities to help patients find appropriate care or look up nearby doctors.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Tenable's research specifically focuses on one aspect of the Azure AI Health Bot Service called [Data Connections](https://learn.microsoft.com/en-us/azure/health-bot/data_connection), which, as the name implies, offers a mechanism for integrating data from external sources, be it third parties or the service providers' own API endpoints.

While the feature has built-in safeguards to prevent unauthorized access to internal APIs, further investigation found that these protections could be bypassed by issuing redirect responses (i.e., 301 or 302 status codes) when configuring a data connection using an external host under one's control.

By setting up the host to respond to requests with a 301 redirect response destined for Azure's metadata service ([IMDS](https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service)), Tenable said it was possible to obtain a valid metadata response and then get hold of an access token for management.azure[.]com.

The token could then be used to list the subscriptions that it provides access to by means of a call to a Microsoft endpoint that, in turn, returns an internal subscription ID, which could ultimately be leveraged to list the accessible resources by calling another API.

Separately, it was also discovered that [another endpoint](https://learn.microsoft.com/en-us/azure/health-bot/data_connection#fhir-endpoint) related to integrating systems that support the Fast Healthcare Interoperability Resources ([FHIR](https://www.hl7.org/fhir/)) data exchange format was susceptible to the same attack as well.

Tenable said it reported its findings to Microsoft in June and July 2024, following which the Windows maker began rolling out fixes to all regions. There is no evidence that the issue was exploited in the wild.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The vulnerabilities raise concerns about how chatbots can be exploited to reveal sensitive information," Tenable said in a statement. "In particular, the vulnerabilities involved a flaw in the underlying architecture of the chatbot service, highlighting the importance of traditional web app and cloud security in the age of AI chatbots."

The disclosure comes days after Semperis detailed an attack technique called [UnOAuthorized](https://www.blackhat.com/us-24/briefings/schedule/#unoauthorized-a-technique-to-privilege-escalation-to-global-administrator-39231) that allows for privilege escalation using Microsoft [Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (formerly Azure Active Directory), including the ability to add and remove users from privileged roles. Microsoft has since plugged the security hole.

"A threat actor could have used such access to perform privilege elevation to Global Administrator and install further means of persistence in a tenant," security researcher Eric Woodruff [said](https://www.semperis.com/blog/unoauthorized-privilege-elevation-through-microsoft-applications/). "An attacker could also use this access to perform lateral movement into any system in Microsoft 365 or Azure, as well as any SaaS application connected to Entra ID."

### Update

Microsoft is tracking the vulnerability under the CVE identifier CVE-2024-38109 (CVSS score: 9.1), describing it as a privilege escalation flaw impacting the Azure Health Bot Service.

"An authenticated attacker can exploit a Server-Side Request Forgery (SSRF) vulnerability in Microsoft Azure Health Bot to elevate privileges over a network," the company [said](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38197) in an advisory released on August 13, 2024.

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
[**Share on Twitter]...