---
title: Mandating Security by Design: Sekoia’s Blueprint for the EU Cyber Resilience Act
url: https://blog.sekoia.io/mandating-security-by-design-sekoias-blueprint-for-the-eu-cyber-resilience-act/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-11
fetch_date: 2025-12-12T03:22:54.960320
---

# Mandating Security by Design: Sekoia’s Blueprint for the EU Cyber Resilience Act

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/ "SOC Insights & Other News")

# Mandating Security by Design: Sekoia’s Blueprint for the EU Cyber Resilience Act

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Arnaud Dechoux and Maxime Arandel](#molongui-disabled-link)
December 11 2025

0

10 minutes reading

## Introduction

The European Union (EU) continues to solidify its cybersecurity landscape through ambitious, horizontal regulations. In addition to the NIS 2 Directive and the Digital Operational Resilience Act (DORA), the [**Cyber Resilience Act (CRA)**](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) establishes a comprehensive framework aimed at securing products with digital elements (PDEs) placed on the internal market.

The CRA, which entered into force on December 10, 2024, addresses two major concerns: the historically low level of cybersecurity in digital products and the lack of accessible information for users to make secure choices. Its primary objective is to ensure that hardware and software products are developed with fewer vulnerabilities and that manufacturers uphold security throughout the product’s lifecycle.

At Sekoia, a leading European cybersecurity technology provider, we recognize the CRA as a fundamental shift toward accountability and resilience, complementing the existing requirements faced by critical entities under NIS 2 and DORA. This blog post serves as a preliminary implementation guide, designed to provide clarity on the CRA’s practical application. We begin by enumerating the known requirements, follow this with an internal assessment by checking these requirements against our current operational processes, and conclude by detailing which aspects of our solution can assist our customers in meeting specific CRA obligations.

At the end of the blogpost, enjoy also a short CRA quiz to test your knowledge!

## The core mandate of the Cyber Resilience Act

The CRA directly impacts manufacturers, importers, and distributors of products with digital elements (PDEs). It establishes essential cybersecurity requirements that must be met *before* a product is placed on the market, and maintained *throughout* its predetermined support period.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/12/CRA_blogpost_covered_entities.png)

Key obligations for manufacturers include:

### 1. Security by design and risk assessment

Manufacturers must design, develop, and produce PDEs to ensure an appropriate level of cybersecurity based on identified risks. This mandatory cybersecurity risk assessment must be documented and continuously updated throughout the support period. Products must, where applicable, be made available without known exploitable vulnerabilities and include a **secure by default configuration**.

### 2. Comprehensive vulnerability management

A robust vulnerability handling process is mandatory. This includes identifying and documenting vulnerabilities and components, notably by producing a **Software Bill of Materials (SBOM)** in a machine-readable format. Manufacturers must address and remediate vulnerabilities without delay and provide security updates, generally free of charge, for the entire support period.

### 3. Defining the support period

Manufacturers must determine a support period reflecting the product’s expected use time. This period must be **at least five years**, unless the product’s expected lifetime is shorter. Security updates must be available throughout this period.

### 4. Mandatory reporting of incidents and vulnerabilities (VAEs)

A crucial provision, applicable starting **September 11, 2026**, mandates manufacturers to simultaneously notify actively exploited vulnerabilities (VAEs) and severe incidents impacting the product’s security:

* An **early warning notification** must be submitted within **24 hours** of becoming aware of the VAE or severe incident.
* A comprehensive notification follows within 72 hours.
* A final report must be provided within 14 days (for VAEs after the fix is available) or one month (for severe incidents).

Notifications must be submitted via national CSIRT and the Single Reporting Platform (SRP) administered by ENISA- currently under development. For certain cases involving for instance national security and defense, delayed notifications are provided under specific conditions.

### 5. Conformity and certification

All products must undergo a conformity assessment and affix the CE marking before being placed on the EU market. Depending on the product’s criticality, this assessment may require third-party verification by a Notified Body or certification.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/12/CRA_blogpost_key_requirements-1.png)

## Sekoia’s position under the CRA

As a European-based cybersecurity company providing an AI SOC platform, Sekoia is directly concerned by the CRA. According to first analysis and pending further legal analysis, our offering falls under the definition of a PDE.

Based on the categorization criteria set out in Annex III of the CRA, **Security Information and Event Management (SIEM) systems** are specifically listed as **Important Products, Class I**. As our AI SOC platform is the fusion of SIEM, XDR, SOAR and CTI, this classification subjects Sekoia to stricter requirements regarding conformity assessment compared to general products, unless compliance is demonstrated through certification.

Among other products in the Important / Class I category are browsers, VPN, anti-malicious software, IAM, but also routers and operating systems… Important products Class II includes firewalls, IDPS and tamper-resistant microcontrollers, while Critical products are Hardware Devices with security boxes, smart meter gateways and sma...