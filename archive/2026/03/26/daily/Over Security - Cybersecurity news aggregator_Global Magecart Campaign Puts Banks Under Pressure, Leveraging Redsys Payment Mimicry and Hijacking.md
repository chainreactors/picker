---
title: Global Magecart Campaign Puts Banks Under Pressure, Leveraging Redsys Payment Mimicry and Hijacking
url: https://any.run/cybersecurity-blog/banks-magecart-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-26
fetch_date: 2026-03-27T04:33:21.763727
---

# Global Magecart Campaign Puts Banks Under Pressure, Leveraging Redsys Payment Mimicry and Hijacking

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores for Bank Fraud ](/cybersecurity-blog/wp-content/uploads/2026/03/Magecart.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores for Bank Fraud

March 26, 2026

[Add comment](#comments-19577)
1443 views
9 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores for Bank Fraud

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/03/Magecart-1024x497.png)

  #### Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores for Bank Fraud

  1443
  0](/cybersecurity-blog/banks-magecart-campaign/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/Global-InfoSec-Awards-2026_cover-1024x497.png)

  #### ANY.RUN Recognized for Innovations and Market Leadership at Global InfoSec Awards 2026

  411
  0](/cybersecurity-blog/global-infosec-awards-2026/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/Kamasers-1024x497.png)

  #### Kamasers Analysis: A Multi-Vector DDoS Botnet Targeting Organizations Worldwide

  3210
  0](/cybersecurity-blog/kamasers-technical-analysis/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores for Bank Fraud

A large-scale magecart operation remained active for over 24 months, leveraging an infrastructure of 100+ domains. While the targeted victims are e-commerce websites, the actual pressure falls on [banks and payment systems](https://any.run/by-industry/finance/?utm_source=anyrunblog&utm_medium=article&utm_campaign=banks-magecart-campaign&utm_term=260326&utm_content=linktofinancelanding).

As [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=banks-magecart-campaign&utm_term=260326&utm_content=linktolanding)’s analysis shows, threat actors applied multi-step checkout hijacking, payment page mimicry, and WebSocket-based exfiltration of card data.

This report provides both executive-level insights and technical analysis of the campaign.

## Key Takeaways

* The campaign demonstrates **long-term persistence** (24+ months) supported by highly resilient infrastructure.

* **Banks** (not merchants) **bear the primary impact**, as stolen card data leads to fraud losses and reputational risk.

* Payment system mimicry (notably Redsys)**significantly increases attack success** by embedding fraud into trusted user flows.

* Use of **WebSocket exfiltration**reduces visibility in traditional security monitoring tools.

* Multi-stage, dynamically delivered payloads allow attackers to **adapt quickly**and evade disruption.

* The campaign is global but **regionally tailored**, leveraging localized payment ecosystems to enhance credibility.

## Campaign Overview

A large-scale magecart operation has been identified, active for at least 24 months and supported by over 100 domains. In observed cases, threat actors deployed a multi-stage checkout hijacking framework, incorporating:

* Payment step substitution

* WebSocket-based exfiltration of payment card data

* Payment page mimicry, including infrastructure-level impersonation of legitimate providers (notably Redsys)

* Dynamic frontend adaptation of payment interfaces matching different storefronts and scenarios

A total of 17 WooCommerce websites were infected between February 2024 and April 2025 and are likely linked to this campaign, reflecting its longevity and operational stability.

## Industrial and Regional Context Behind Global Impact

The geographic scope is of the campaign is global. Among the victims are organizations from at least 12 countries, including the United Kingdom and Denmark. However, there’s a notable concentration of such incidents in Spain, France, and United States.

Some cases are confirmed directly via telemetry and network traffic, while others are identified via infrastructural correlation.

From an [industry](https://any.run/cybersecurity-blog/industry-geo-threat-landscape/) perspective, mostly retail e-commerce companies were targeted, although in some cases, non-commercial organizations have been affected, too.

However, the primary pressure here falls on [banks](https://any.run/cybersecurity-blog/cyber-threat-intelligence-for-finance/), as cardholders faced financial exposure and their trust in payment systems suffered.

Protect your company with early visibility
To reduce dwell time, pressure, and losses

[Integrate ANY.RUN in your SOC](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=banks-magecart-campaign&utm_term=260326&utm_content=linktoenterprise#contact-sales)

## Why Redsys and Spanish Payment Context Stand Out

Despite the global impact, the ties to Spain and its payment ecosystem in particular are obvious in this magecart campaign.

Mimicry of RedSys, a payment system used in Spain, lies in the foundation of the attacks. The campaign infrastructure features domains and visual artifacts designed to fit Spanish payment context. In some cases, user payment flows included [legitimate](https://any.run/cybersecurity-blog/enterprise-phishing-analysis/) Redsys domain sis.redsys.es for added credibility.

The approach made the malicious activity of the campaign convincing within Spanish payment context.

## What Makes This Campaign Durable

**Payment Mimicry**

A significant portion of the infrastructure is registered via NICENIC INTERNATIONAL GROUP and disguised as legitimate web services, including analytics platforms, CDN resources, jQuery libraries, andpayment services. If you access them directly, they’ll act as technical placeholders...