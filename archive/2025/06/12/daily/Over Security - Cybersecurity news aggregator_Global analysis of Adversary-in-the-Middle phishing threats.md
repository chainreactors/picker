---
title: Global analysis of Adversary-in-the-Middle phishing threats
url: https://blog.sekoia.io/global-analysis-of-adversary-in-the-middle-phishing-threats/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-12
fetch_date: 2025-10-06T22:55:24.831606
---

# Global analysis of Adversary-in-the-Middle phishing threats

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Global analysis of Adversary-in-the-Middle phishing threats

This report explores current trends in the AitM phishing landscape and the prevalence of leading kits.

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue, Grégoire Clermont and Sekoia TDR](#molongui-disabled-link)
June 11 2025

0

21 minutes reading

**This blogpost is an abridged version of the report. The full version is available as a PDF.**

[Download the full report](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/06/Sekoia_io___Global_analysis_of_Adversary_in_the_Middle_phishing_threats.pdf)

## Table of contents

* [Introduction](#h-introduction)
* [Key takeaways](#h-key-takeaways)
* [Glossary of AitM terminology](#h-glossary-of-aitm-terminology)
* [Adversary-in-the-Middle (AitM) phishing attacks](#h-adversary-in-the-middle-aitm-phishing-attacks)
  + [Social engineering lures](#h-social-engineering-lures)
  + [Common TTPs](#h-common-ttps)
  + [Business Email Compromise (BEC) attacks](#h-business-email-compromise-bec-attacks)
* [Phishing-as-a-Service ecosystem](#h-phishing-as-a-service-ecosystem)
  + [Typology of PhaaS offerings](#h-typology-of-phaas-offerings)
  + [Timeline of prominent PhaaS](#h-timeline-of-prominent-phaas)
  + [Tools and services to set up phishing attacks](#h-tools-and-services-to-set-up-phishing-attacks-nbsp)
* [Investigating AitM phishing threats: methods and findings](#h-investigating-aitm-phishing-threats-methods-and-findings)
  + [TDR monitoring of AitM phishing threats](#h-tdr-monitoring-of-aitm-phishing-threats)
  + [Sekoia.io telemetry](#h-sekoia-io-telemetry)
  + [Most relevant phishing kits](#h-most-relevant-phishing-kits)
* Sheets for phishing kits* Detection opportunities
    + Authentication logs analysis
    + Network traffic monitoring* Conclusion* Perspective* Annexes* External references

## Introduction

In recent years, organisations have increasingly encountered **massive and more sophisticated phishing attacks** that primarily target Microsoft 365 and Google accounts **using Adversary-in-the-Middle (AitM) technique**. This growing trend has been amplified by the **proliferation of Phishing-as-a-Service (PhaaS) offerings in the cybercrime ecosystem.** These services provide access to advanced phishing kits for a wide range of cybercriminals, including those with limited technical skills, at a lower cost.

AitM phishing kits mainly aim to **harvest session cookies** from targeted services to **bypass the Multi Factor Authentication (MFA) process during subsequent logins**. To achieve this, AitM phishing servers relay user inputs, including usernames, passwords and MFA codes, to the legitimate authentication API while intercepting the returned session cookie. With that cookie, an attacker can replay the session, and access the victim’s account without needing to perform any further authentication. Such compromises frequently lead to **significant financial losses via Business Email Compromise (BEC) operations**, financial fraud, or even Big Game Hunting ransomware attacks.

The Sekoia Threat Detection & Research (TDR) team closely monitors the AitM phishing attacks and regularly provides technical reports on emerging kits that we uncover through our daily threat hunting routine. This **global report delves into the threat posed by AitM phishing**, offering both contextual and operational insights. Using our telemetry data and research findings, this report explores current trends in the AitM phishing landscape and the prevalence of leading kits.

Additionally, the report delivers valuable and actionable intelligence to help analysts detect, identify and investigate the AitM phishing threat. It highlights detection opportunities and includes concise sheets for the eleven most widespread AitM phishing kits as of Q1 2025.

## Key takeaways

* Since 2023, the TDR team has actively monitored Adversary-in-the-Middle (AitM) phishing threats by developing detection rules, uncovering adversary infrastructure, and tracking prevalent tactics, techniques, and procedures (TTPs).

* Sekoia’s TDR team has developed a methodology based on telemetry, adversaries’ infrastructure tracking, and campaigns monitoring to rank the most active AitM phishing threats from January to April 2025.

* According to this methodology, the most widespread phishing kits are Tycoon 2FA, Storm-1167, NakedPages, Sneaky 2FA, EvilProxy, and Evilginx.

* Over the past months, threat actors have rapidly adopted new TTPs in high volume AitM phishing campaigns, transitioning from QR codes to HTML attachments and more recently to SVG files for link distribution.

* Numerous fully-featured and turnkey AitM phishing kits are readily available within the cybercrime ecosystem, offered at low cost and requiring minimal technical expertise.

* The cybercrime ecosystem specialising in AitM phishing and Business Email Compromise (BEC) attacks is becoming increasingly professional, providing a broader suite of products and services.

* This report includes an overview sheet for 11 relevant AitM phishing kits, providing analysts with technical details, tracking and detection opportunities.

## Glossary of AitM terminology

Understanding Adversary-in-the-Middle (AitM) phishing involves grasping several technical concepts. To facilitate this comprehension, we have compiled a glossary of key terms associated with this threat.

* **Phishing-as-a-Service (PhaaS)**

Phishing-as-a-Service is a subscription-based model that provides cybercriminals with access to phishing kits and associated services. Most PhaaS platforms also offer additional features, such as anti-bot webpages, HTML and SVG attachment templates, and data forwarding to Telegram bots.

* **O...