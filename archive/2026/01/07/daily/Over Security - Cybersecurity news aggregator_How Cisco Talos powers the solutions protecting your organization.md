---
title: How Cisco Talos powers the solutions protecting your organization
url: https://blog.talosintelligence.com/how-cisco-talos-powers-the-solutions-protecting-your-organization/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-07
fetch_date: 2026-01-08T03:30:41.107958
---

# How Cisco Talos powers the solutions protecting your organization

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2025/12/Talos_integrations_header.jpg)

# How Cisco Talos powers the solutions protecting your organization

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/),
[Kri Dontje](https://blog.talosintelligence.com/author/kri/),
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/),
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Wednesday, January 7, 2026 06:00

[The Need to Know](/category/the-need-to-know/)

Cisco Talos is Cisco’s threat intelligence and security research organization that powers Cisco’s product portfolio with that intelligence. While we are well known for the security research in our blog, [vulnerability discoveries](https://www.talosintelligence.com/vulnerability_reports), and our [o](https://blog.talosintelligence.com/a-refresher-on-talos-open-source-tools/)[pen-source software](https://blog.talosintelligence.com/a-refresher-on-talos-open-source-tools/), you may not be aware of exactly how our know-how protects Cisco customers.

Talos’ core mission is to understand the broad threat landscape and distill the massive amount of telemetry we ingest into actionable intelligence. This intelligence is put to use in detecting and defending against threats with speed and accuracy, providing incident response and empowering our customers, constituents, and communities with context-rich actionable cyber intelligence. Under the hood of [Cisco’s security portfolio](https://www.cisco.com/site/uk/en/products/security/index.html), you will find our reputation and detection services applying our real time intelligence to detect and block threats.

## Defending networks

Possibly our best-known service is the Cisco Talos Network Intrusion Prevention system, widely known as [SNORT®](https://www.snort.org/). Snort performs deep packet inspection on network traffic, using advanced signature-based detection to identify known threats. In addition, its machine learning-powered component, SnortML, helps detect and block attempts to exploit zero-day vulnerabilities, providing robust protection against both familiar and emerging network attacks.

## Securing the web

The core of securing our customers across our product portfolio is Cisco Talos Web Filtering Service. This service considers the reputation and [categorization](https://www.talosintelligence.com/categories) of domains, IP addresses, and indicators surrounding the URL. The service can proactively block web traffic to sites that have a poor reputation or that serve content in contravention of a customer’s web use policy.

The Cisco Talos DNS Security service augments our web filtering by defending specific attacks at the DNS layer. It detects domains used by threat actors for command and control (C2), data exfiltration, and phishing attacks. Behind the scenes, our machine learning algorithms constantly analyze patterns in the DNS traffic to identify new malicious domains to add to our own intelligence.

## Protecting your inbox

Cisco Talos Email Filtering analyzes a wide range of indicators within email to determine if it is malicious, spam, or a genuine email. This includes assessing the sender’s domain and IP reputation and behavior, examining URLs and the content they reference, and evaluating the body of the email, header, and any attachments. By combining these factors, our email filtering can identify benign messages, spam, phish, as well as other unwanted messages.

Cisco Talos Email Threat Prevention goes one step further than DMARC, the standard for properly handling emails with inaccurate sender data, by analyzing anomalies in email traffic patterns with AI, to identify when brands are being impersonated. This technology can detect when an email is likely to be a phish or a business email compromise attempt.

## Detecting malware

Talos provides two complementary technologies to detect malware: Cisco Talos Antivirus and Cisco Talos Malware Protection. The former provides signature and pattern detection of malware within files to identify known malware, similar to our ClamAV open-source product. The latter goes further, checking the dispositions of unknown files and looking for suspicious behavior on the machine. This layered approach allows us to quickly spot and contain threats while our researchers scour telemetry for any indications that a bad actor has gained access to a device.

We also provide Orbital queries and scripts, a platform by which administrators can collect information from networked devices and use their own queries (or those provided by us) to hunt for devices that are insecure, out of policy, or potentially affected by a security incident.

## Summary

You can find Talos’ intelligence integrated into a wide variety of Cisco products:

![](https://blog.talosintelligence.com/content/images/2025/12/Talos_integrations_table-1-.jpg)

Our published research and threat intelligence reports represent just a small part of the work we do at Talos. The many hours our researchers, analysts, and engineers spend researching the threat environment and developing systems to detect and block attacks bear fruit in the components that we deploy as part of the Cisco Security portfolio. Our intelligence and know-how protect Cisco Security customers from threats, brand new or decades old.

*Note*: *You can benefit from the experience of our analysts directly through a* [*Cisco Talos Incident Response*](https://talosintelligence.com/incident_response) *(Talos IR) retainer. While Talos IR can provide relevant threat information and expert emergency incident response, you can also use our proactive services to help prepare your systems, support and train your team, or actively hunt for bad guys on your network.*

##### Share this post

#### Related Content

[### UAT-8099: Chinese-speaking cybercrime grou...