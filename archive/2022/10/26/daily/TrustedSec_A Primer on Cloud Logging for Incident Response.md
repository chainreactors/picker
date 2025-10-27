---
title: A Primer on Cloud Logging for Incident Response
url: https://www.trustedsec.com/blog/a-primer-on-cloud-logging-for-incident-response/
source: TrustedSec
date: 2022-10-26
fetch_date: 2025-10-03T20:56:13.271083
---

# A Primer on Cloud Logging for Incident Response

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [A Primer on Cloud Logging for Incident Response](https://trustedsec.com/blog/a-primer-on-cloud-logging-for-incident-response)

October 25, 2022

# A Primer on Cloud Logging for Incident Response

Written by
TrustedSec

Cloud Assessment
Cloud Penetration Testing
Incident Response
Incident Response & Forensics
Penetration Testing
Security Testing & Analysis
Table-Top Exercises

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/APrimerOnCloudLogging_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695570516&s=195732e05edd3658558293008262156c)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#f6c98583949c939582cbb59e93959dd3c4c6998382d3c4c6829e9f85d3c4c69784829f959a93d3c4c69084999bd3c4c6a2848385829392a59395d3c4c7d0979b86cd9499928fcbb7d3c4c6a6849f9b9384d3c4c69998d3c4c6b59a998392d3c4c6ba9991919f9891d3c4c6909984d3c4c6bf98959f92939882d3c4c6a493858699988593d3c5b7d3c4c69e82828685d3c5b7d3c4b0d3c4b082848385829392859395d895999bd3c4b0949a9991d3c4b097db86849f9b9384db9998db959a998392db9a9991919f9891db909984db9f98959f92939882db8493858699988593 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fa-primer-on-cloud-logging-for-incident-response "Share on Facebook")
* [Share on X](http://twitter.com/share?text=A%20Primer%20on%20Cloud%20Logging%20for%20Incident%20Response%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fa-primer-on-cloud-logging-for-incident-response "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fa-primer-on-cloud-logging-for-incident-response&mini=true "Share on LinkedIn")

## **Overview**

This blog post will provide an overview of common log sources in Azure and AWS, along with associated storage and analysis options.

At a high level, cloud-based incidents can be categorized into host-based compromises (that is, compromises primarily involving virtual machines hosted in the cloud) and identity-based or resource-based compromises (compromises primarily involving cloud-native services and identities). These scenarios often overlap depending on the scope of an incident, but the investigative approaches are distinct. For example, a compromise of a public-facing virtual machine for cryptocurrency mining purposes warrants disk acquisition and analysis, but the scope of the compromise may not extend into other resources or identities in the tenant. On the other hand, investigating an identity compromise relies heavily on tenant logs and may not involve any virtual machine artifacts if no hosts were targeted by the threat actor.

The steps below represent a high-level approach to investigating cloud-based incidents originating from a compromised identity. This process can be reversed if the investigation originates from a compromised system.

* Review log sources containing events that affect identity and access.
  + In Azure, these events would include the Azure Active Directory (AD) Audit logs and Sign-in logs.
  + In AWS, these events would be included in CloudTrail.
* Review resource logs, such as logs from virtual machine creation or storage account access. These logs indicate whether a resource has been created or destroyed, or whether data has been written or read from a storage bucket. There could be many other resource logs to review if they were configured ahead of time.
* Review network logs to investigate network communications within the virtual network(s). These might come from the cloud provider solution or third-party firewalls, depending on the environment.
* If needed, perform traditional host-based forensic analysis.

## **Overview of Logs**

### **Azure**

In Azure, logs are organized into five categories:

* **Tenant logs**: These contain information about operations conducted by tenant-wide services—most notably, the Azure AD log, which contains audit logs, sign-in logs, and provisioning logs
* **Subscription logs**: Available under the 'Activity log' service, these contain information about resources being created, modified, or deleted.
* **Resource logs**: These can be generated by any resource, such as Network Security Groups (NSG) and Storage Accounts. Resource logs are disabled by default.
* **Operating System logs**: Generated by and collected from virtual machines or containers, these logs need to be configured manually.
* **Application logs**: These include custom logs enabled by the developer. As such, these need to be configured manually.

Azure provides four ways to collect or examine tenant, subscription, and resource logs:

* Viewed direct...