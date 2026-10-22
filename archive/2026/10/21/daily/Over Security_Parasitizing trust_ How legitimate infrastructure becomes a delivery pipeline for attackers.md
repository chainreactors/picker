---
title: Parasitizing trust: How legitimate infrastructure becomes a delivery pipeline for attackers
url: https://blog.talosintelligence.com/parasitizing-trust-how-legitimate-infrastructure-becomes-a-delivery-pipeline-for-attackers/
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:31.804623
---

# Parasitizing trust: How legitimate infrastructure becomes a delivery pipeline for attackers

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/parasitizingtrust.jpg)

# Parasitizing trust: How legitimate infrastructure becomes a delivery pipeline for attackers

By
[Diana Brown](https://blog.talosintelligence.com/author/diana/)

Wednesday, October 21, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)

* Legitimate infrastructure has become a powerful delivery mechanism for attackers, carrying the inherent trust they once had to build. As Cisco Talos explored in our previous research on [weaponizing software-as-a-service (SaaS) notification pipelines](https://blog.talosintelligence.com/weaponizing-saas-notification-pipelines/), these platforms are increasingly repurposed as proxies for malicious intent.
* Talos has since tracked a significant acceleration in this trend, observing abuse across more than 25 distinct legitimate platforms in the past year.
* The abused infrastructure included collaboration, productivity, file-sharing, survey, payment and AI-related platforms.
* This demonstrates that attackers are not limiting themselves to traditional phishing infrastructure or lookalike domains. Instead, they are systematically subverting the very tools businesses trust.

## **Order notification abuse**

Talos recently analyzed two order notification campaigns abusing Staples and Dell transactional email pipelines. Together, these campaigns accounted for roughly 1,400 messages observed by Talos.

The malicious element was not the outer sender identity, like a simple forged sender or lookalike domain. It was the content of the legitimate order notification workflow rendered. The suspicious content appeared inside the notification itself, in fields that would normally contain shipping information. The attacker’s objective was to use a trusted retail pipeline to create urgency around a high-value purchase and push the recipient toward an attacker-controlled phone number.

In the first campaign, the message appeared as a Staples order confirmation from "support@orders.staples.com” with the subject line, “Here’s your Staples order #9939818875. Thanks for shopping with us.” The body displayed a plausible purchase for an Apple iPad, including order number, delivery timing, pricing, billing information and standard Staples footer content. The suspicious element was embedded in the order details: “Helpline 806 283 7712,” “Order Confirmed,” and the Staples corporate address appeared in fields normally associated with shipping or billing information.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/email-1.jpg)

Figure 1. Staples order notification

The structure of the message matters. The attacker was not trying to persuade the user to click a crude phishing link. Instead, the message created the impression that an expensive order had already been placed and that the fastest way to resolve it was to call the embedded “helpline.” The desired user action was a phone call. Once the victim moved from email to voice, the attacker could continue the scam through social engineering, payment manipulation, credential theft, or remote assistance fraud.

The headers reinforced the trust problem. The Staples message showed DKIM alignment for “orders.staples.com” and DMARC passed for the visible Staples domain. The message also passed through forwarding and re-encapsulation paths, including Proton Mail, Microsoft 365, and downstream enterprise mail infrastructure. These hops complicate provenance analysis, but they do not change the core issue: Authentication helped establish that the outer message was credible, while offering no assurance that the phone number or transaction context was legitimate.

The second campaign used the same pattern in a Dell order received notification. The message was sent from “Dell | Order Received <received@order.dellcom>” with the subject line, “We have your order | Dell Purchase ID: 2009829958247.” The body presented a purchase for Microsoft Project Standard 2024, totaling $736.09. As with the Staples example, the suspicious content appeared in transaction fields. The “Ship To” and “Bill To” sections included “Confirmed Order,” “Helpline 808 232 6397,” and “Call Our Sales Team”.

The Dell message used the same psychological lever: an unexpected high-value purchase, a legitimate-looking order template, and a phone number positioned as the path to resolution. The attacker did not need the recipient to trust a new domain or unfamiliar brand. The message borrowed credibility from Dell’s order pipeline and redirected the recipient toward attacker-controlled contact information.

Authentication results showed DKIM passing for Dell-related infrastructure and DMARC passing for “order.dell.com”. As with the Staples sample, forwarding artifacts and SRS-style return paths appeared as the message moved through Microsoft and enterprise mail infrastructure. But the malicious intent did not live in an obviously forged sender. It lived inside the rendered order content.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/email-2.jpg)

Figure 2. Dell order notification

These campaigns illustrate the same trust-boundary failure described in [our earlier research](https://blog.talosintelligence.com/weaponizing-saas-notification-pipelines/) on platform-as-a-proxy (PaaP) abuse. In those cases, attackers placed malicious content into SaaS fields that trusted platforms later rendered into notifications. Here, the same concept appears in commerce infrastructure, in the retailer’s order pipeline. The attacker supplies the intent, while the trusted system performs the delivery.

From a defensive perspective, sender authentication is necessary, but it is not sufficient. SPF, DKIM, and DMARC help answer wh...