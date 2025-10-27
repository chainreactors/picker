---
title: Hitchhiker’s Guide to Managed Security
url: https://blog.compass-security.com/2025/01/hitchhikers-guide-to-managed-security/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-15
fetch_date: 2025-10-06T20:13:29.143398
---

# Hitchhiker’s Guide to Managed Security

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Hitchhiker’s Guide to Managed Security](https://blog.compass-security.com/2025/01/hitchhikers-guide-to-managed-security/ "Hitchhiker’s Guide to Managed Security")

[January 14, 2025](https://blog.compass-security.com/2025/01/hitchhikers-guide-to-managed-security/ "Hitchhiker’s Guide to Managed Security")
 /
[Felix Aeppli](https://blog.compass-security.com/author/faeppli/ "Posts by Felix Aeppli")
 /
[0 Comments](https://blog.compass-security.com/2025/01/hitchhikers-guide-to-managed-security/#respond)

Over the past few years, we have had the opportunity to conduct several Purple Teaming exercises together with our customers. Some of the customers have their own Blue Team, others use an external provider for this service. Sometimes it is a mix, where an external company supports the internal Blue Team in its daily tasks.

Particularly after Purple Teaming exercises involving external providers, we often see a mismatch between the customer’s expectations and the service provided. This does not necessarily mean that the service provider has done a poor job, but rather that the customer expected something more, something different.

We have had many heated discussions in our office about how this mismatch between customer expectations and the actual service provided comes about. From these discussions, combined with our experience from our past Purple Teaming exercises, we compiled this blog post to share our take on how to prevent the most prevalent issues as early as possible.

Before we get into the details, we would like to point out that this blog is not intended to be a bashing of such service providers! On the contrary, we believe that these services are essential for companies that lack the size and capabilities to operate their own Blue Team. Rather, we want to turn a lose-lose situation into a win-win situation for both, the customer and the service provider.

No time to read this post? Download our one-pager PDF:

[Hitchhikers\_Guide\_to\_Managed\_Security\_v1.0](https://blog.compass-security.com/wp-content/uploads/2025/01/Hitchhikers_Guide_to_Managed_Security_v1.0.pdf)[Download](https://blog.compass-security.com/wp-content/uploads/2025/01/Hitchhikers_Guide_to_Managed_Security_v1.0.pdf)

## Where it all starts – Evaluation of a Service Provider

### Nomen est omen?

```
tl;dr:
Understand the technical detection capabilities and limitations of the service being offered.

Key questions:
- What are the provided detection capabilities?
- Is the service (solely) on a commercial product?
- Is it possible to implement custom detection logic?
- What kind of log sources can be ingested by the provider?
```

As you may have noticed, in our introduction to this blog we just mentioned a “service”. The reason for this is that there are many different names for such a “service”. Here are some examples we have come across:

* Managed Detection and Response (MDR)
* Security Operations Center (SOC)
* Security Operations Center as a Service (SOCaaS)
* Managed Security Service Provider (MSSP)

As far as we know, there is no clear definition of these terms and what they encompass, so we were never sure what to expect. It is probably fair to assume that customers feel the same way. So how can these services be compared and what can be expected?

In our experience, one of the key differentiators between various provider models is the scope of the underlying detection capabilities. There are mainly two types that we encountered:

1. EDR based detection capabilities based on commercial products
2. EDR based + additional custom detection capabilities developed by the service provider

Both types of service have their place. Services based solely on an EDR are more cost-effective, but lack the ability to implement complex custom detection rules. Also, additional existing security devices such as firewalls, web application firewalls, proxies, etc. may not be able to be integrated into such a solution, restricting the coverage for possible detections. Nevertheless, depending on the size, complexity and threat model of your environment, this type of service may be more than enough. The important thing is that you, as the customer, have a clear understanding of the provided detection capabilities.

### Does it fit?

```
tl;dr:
The provided coverage of the service should fit your environment.

Key questions:
- Does the service reflect your threat model?
- Are all key aspects of your IT infrastructure and critical assets covered by the service?
- Does the time coverage of the service match your business model and availability?
```

Now that you understand the potential detection capabilities that can be provided, the big question is whether it fits your environment or not. There are three main points to consider:

1. The service should be chosen according to your threat model
2. The service should cover all major/relevant aspects of your IT infrastructure and especially your critical assets
3. The service availability should align with your business model

#### Threat Model

To choose the right service and service level, you need to understand your threat model. Is the main threat a ransomware attack or do you fear a more targeted attack on your infrastructure and users? Lies your main concern with the availability of your services or rather with the confidentiality of your data (or both)? What assets are crucial to your company’s ability to operate?

Depending on your threat model the necessary service might look different.

#### IT Infrastructure Coverage

As implied previously, an EDR-only approach may be sufficient for your environment and threat model. Still you need to check if the EDR solution can be installed on all your different operating systems. If a substantial part of your infrastructure is operated on Linux, but the EDR solution of your provider only runs on Windows, this could prove problematic. An other example might be that a provider offers extensive coverage of cloud infrastructures, but has little to no detection capabilities for on-premise systems.

However, if you have a more complex environment and critical assets to protect, you may need to consider further detection capabilities beyond an EDR solution.

Suppose you have a database server with sensitive customer data that is accessible through a web application. You want to know if someone has gained unauthorized access to the database and extracted this sensitive data. How hard can that be, right? Well, do you know which log files you need to build a detection logic for that?

* Operating system logs
* Database logs
* Web server logs
* Firewall logs
* Web Application Firewall logs
* etc.

The point is that writing custom detection logic is not a simple task. So if you require such use cases, the provided service must at least be able to ingest these logs. In the best case the service already provides such use cases that can be implemented or adapted to your environment.

#### Service Availability

We encountered many different service availability models during our Purple Teaming engagements:

* 7×24
* 7×10
* 5×11
* 5×10
* 5×8
* etc.

Obviously these different models have different price tags attached, and usually more is better from a security perspective. However, the main point here is that the chosen model should fit your business model and your availability.

Lets assume you have chosen the 7×24 model. On a ...