---
title: ConnectWise Suspends Cloud Backup After Attackers Compromise Microsoft 365 Tenants
url: https://thehackernews.com/2026/10/connectwise-suspends-cloud-backup-after.html
source: The Hacker News
date: 2026-10-18
fetch_date: 2026-10-19T07:07:52.210344
---

# ConnectWise Suspends Cloud Backup After Attackers Compromise Microsoft 365 Tenants

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [ConnectWise Suspends Cloud Backup After Attackers Compromise Microsoft 365 Tenants](https://thehackernews.com/2026/10/connectwise-suspends-cloud-backup-after.html)

**Ravie Lakshmanan**Oct 18, 2026Cloud Security / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxTJ5xsWsmrBmF1q18Gi5uaokNeC6-M0VbSf0T5X3KMQH7QGMhC7mz4XB6TUJuE7P9tjknMAqaGQ-Iz_7UuQ-NdKKXJTgqLhHMipRcd57VUOpwfJ2xxO8Hq_PX8hotdp_KZddNDzfQFw3bLHbYYLasThNbqGlidzhZ485ApBIKh2KUgn4g6PeBbhMwhc0T/s1700-nu-rw-lo-l85-e365/ms-connect.jpg)

ConnectWise on Saturday [said](https://www.connectwise.com/company/trust/advisories) it has disabled seven ConnectWise application identities as it continues its investigation into an incident in which unknown threat actors [obtained unauthorized access to the application identities](https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html) and compromised Microsoft 365 tenants.

The disabled identities are listed below -

* ConnectWise Cloud Backup - 506e08f9-6e9a-4da4-942b-a099a03644ae
* ConnectWise Cloud Management - 2399d300-6fca-4e6a-a686-399fefe75b83
* ConnectWise Cloud Management - MS Teams - 24205314-2b89-4e07-a2a4-579e898a5640
* ConnectWise Cloud Management - Exchange Online - b78f6a77-d4e5-46fb-87e5-d1648bd02519
* ConnectWise Cloud Management - MS Graph - 0de14c77-b9b0-4137-9360-34878a929827
* ConnectWise Cloud Management - Partner Center - 412dcf96-176d-4b3a-a1b0-4981ad66971e
* ConnectWise Cloud Management - SharePoint Online - b2b55f5b-7758-4719-8d8f-88ae172e6bdb

The IT management software provider said it took the action on October 17, 2026, at 07:00 UTC, adding it has also suspended Cloud Backup service by revoking certificates used for affected application connections across all users.

"Disabling the affected connections prevents new authentication through those connections; it does not reverse changes previously made inside a tenant," it said.

"The affected shared Cloud Backup credentials are no longer valid. Previously issued access tokens may remain usable until they expire or are otherwise invalidated. Any unauthorized credentials, permissions, or other access established through separate identities require additional review and remediation."

ConnectWise also noted that scheduled backups are not running, and access to affected backup archives and restoration capabilities remains unavailable. However, it emphasized that existing archives remain encrypted, isolated, and preserved, and that there is no evidence they were breached or accessed by the attackers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Out of an abundance of caution, the company said it has temporarily taken SaaS Security and Cloud Management offline while it completes its review of the incident.

Furthermore, the company revealed that it [identified the issue](https://status.connectwise.com/pages/incident/619cf82551fec9053d612f09/6ad263692dc48705ab3da2cb) on October 14, 2026, through its "advanced cybersecurity monitoring and diligence," prompting it to activate internal and external incident investigation and response actions.

"Since implementing these mitigations, we have not observed successful threat activity in the environments we monitor," it said. "This finding does not establish the status of downstream customer environments, which, by design, we cannot directly observe."

At this stage, it's unclear if a product vulnerability contributed to the compromise of the application identities. The exact credential-exposure mechanism is the subject of an ongoing analysis, ConnectWise added.

The attack is particularly dangerous as it allows an attacker to abuse the application's credentials to access customers' Microsoft 365 environments without having to steal each customer's password individually. By using the stolen application credential to authenticate as that application, the attacker can request access tokens from Microsoft Entra ID based on the application's existing permissions.

Depending on the permissions assigned to the application, this could enable the attacker to potentially access other Microsoft services, including mailboxes, SharePoint documents, Teams messages, and directory information.

With ConnectWise's applications operating with extensive permissions to perform backups and management tasks, the theft of the credential allows the threat actor to authenticate as the application itself and expand their access by adding it to the Global Administrator role, adding client secrets to other trusted applications in the tenant, and creating new applications and granting them permissions.

By doing so, the client secrets offer a way to authenticate as that application and establish persistence, providing an alternative means to regain access to the compromised environment even if the original compromised credential is later revoked.

### Second, Targeted Wave of Attempts Observed

"We last observed malicious sign-ins from the original address on October 15 at 08:45 UTC, with targeted, manual activity continuing until about 14:20 UTC that day," Jon Semon, Principal Security Operations Analyst at Huntress, told The Hacker News.

"ConnectWise has said access to Cloud Backup is shut off, and if so, activity through that service should have stopped. However, if the threat actor was able to add credentials to applications in Microsoft tenants, those credentials would let them keep access and act as the application."

Huntress said it has not identified new malicious activity since October 15, but there is no evidence that the stoppage was the result of public disclosure.

"We have high confidence the threat actor also targeted the ConnectWise Cloud Management apps for Exchange Online, Microsoft Teams, and SharePoint, and we have confirmed abuse of the Teams app in one tenant," Semon said. "Those apps do not appear to have been disabled by ConnectWise, so ...