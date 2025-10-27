---
title: How to Hack JWT using Burp Suite
url: https://payatu.com/blog/jwt-vulnerabilities/
source: Payatu
date: 2023-02-07
fetch_date: 2025-10-04T05:51:54.347871
---

# How to Hack JWT using Burp Suite

[Skip to content](#content)

[![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/Payatu_logo.png?fit=320%2C89&ssl=1)](https://payatu.com)

[![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/hamburger_logo.png?fit=35%2C28&ssl=1)](#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjE5OSIsInRvZ2dsZSI6ZmFsc2V9)

[![](https://i0.wp.com/payatu.com/wp-content/uploads/2022/06/hamburger_logo.png?fit=35%2C28&ssl=1)](#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjI0MSIsInRvZ2dsZSI6ZmFsc2V9)

* Services
  + [Product Security](https://payatu.com/product-security-assessment/)
  + [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  + [Red Team Assessment](https://payatu.com/red-team-assessment/)
  + [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  + [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  + [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  + [Code Review](https://payatu.com/code-review-service/)
  + [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  + [SOC Service](https://payatu.com/soc-service/)
  + [Web Application Security Testing](https://payatu.com/web-security-testing/)
  + [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  + [GRC](https://payatu.com/governance-risk-compliance/)
* Products
  + [EXPLIoT](https://expliot.io/)
  + [Cloudfuzz](https://cloudfuzz.io/)
* Who we are
  + [About Us](https://payatu.com/about-us/)
  + [Payatu Bandits](https://payatu.com/bandits/)
* Resources
  + [Advisory](https://payatu.com/advisory/)
  + [Blog](https://payatu.com/blog/)
  + [BugBazaar](https://payatu.com/bugbazaar/)
  + [Case Studies](https://payatu.com/case-studies/)
  + [Checklist](https://payatu.com/checklist/)
  + [CISO Corner](https://payatu.com/ciso-corner/)
  + [Datasheet](https://payatu.com/datasheet/)
  + [DVAPI](https://payatu.com/dvapi/)
  + [Ebooks](https://payatu.com/ebooks/)
  + [Infographics](https://payatu.com/infographics/)
  + [Masterclass](https://payatu.com/masterclass-series/)
  + [Media](https://payatu.com/media/)
  + [Securecodewiki](https://securecode.wiki/)
  + [Telegram Community](https://payatu.com/community/)
* [Contact Us](https://payatu.com/contact-us/)
* [CISO Corner](https://payatu.com/ciso-corner/)

* Services
  + [Product Security](https://payatu.com/product-security-assessment/)
  + [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  + [Red Team Assessment](https://payatu.com/red-team-assessment/)
  + [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  + [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  + [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  + [Code Review](https://payatu.com/code-review-service/)
  + [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  + [SOC Service](https://payatu.com/soc-service/)
  + [Web Application Security Testing](https://payatu.com/web-security-testing/)
  + [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  + [GRC](https://payatu.com/governance-risk-compliance/)
* Products
  + [EXPLIoT](https://expliot.io/)
  + [Cloudfuzz](https://cloudfuzz.io/)
* Who we are
  + [About Us](https://payatu.com/about-us/)
  + [Payatu Bandits](https://payatu.com/bandits/)
* Resources
  + [Advisory](https://payatu.com/advisory/)
  + [Blog](https://payatu.com/blog/)
  + [BugBazaar](https://payatu.com/bugbazaar/)
  + [Case Studies](https://payatu.com/case-studies/)
  + [Checklist](https://payatu.com/checklist/)
  + [CISO Corner](https://payatu.com/ciso-corner/)
  + [Datasheet](https://payatu.com/datasheet/)
  + [DVAPI](https://payatu.com/dvapi/)
  + [Ebooks](https://payatu.com/ebooks/)
  + [Infographics](https://payatu.com/infographics/)
  + [Masterclass](https://payatu.com/masterclass-series/)
  + [Media](https://payatu.com/media/)
  + [Securecodewiki](https://securecode.wiki/)
  + [Telegram Community](https://payatu.com/community/)
* [Contact Us](https://payatu.com/contact-us/)
* [CISO Corner](https://payatu.com/ciso-corner/)

* Services
  + [Product Security](https://payatu.com/product-security-assessment/)
  + [AI/ML Security Audit](https://payatu.com/ai-ml-security-audit/)
  + [Red Team Assessment](https://payatu.com/red-team-assessment/)
  + [Cloud Security Assessment](https://payatu.com/cloud-security-assessment/)
  + [Critical Infrastructure Assessment](https://payatu.com/critical-infrastructure-assessment-payatu/)
  + [DevSecOps Consulting](https://payatu.com/devsecops-consulting/)
  + [Code Review](https://payatu.com/code-review-service/)
  + [Mobile Application Security Testing](https://payatu.com/mobile-application-security-testing/)
  + [SOC Service](https://payatu.com/soc-service/)
  + [Web Application Security Testing](https://payatu.com/web-security-testing/)
  + [IoT Security Assessment](https://payatu.com/iot-security-testing/)
  + [GRC](https://payatu.com/governance-risk-compliance/)
* Products
  + [EXPLIoT](https://expliot.io/)
  + [Cloudfuzz](https://cloudfuzz.io/)
  + EXPLIoT is framework for IoT security testing and exploitation.
  + CloudFuzz is platform that lets you code for bugs by running your software with millions of test cases.
* Who we are
  + [About Us](https://payatu.com/about-us/)
  + [Payatu Bandits](https://payatu.com/bandits/)
* Resources
  + - * #### Resources
      * [Advisory](https://payatu.com/advisory/)
      * [Blog](https://payatu.com/blog/)
      * [Case Studies](https://payatu.com/case-studies/)
      * [Checklist](https://payatu.com/checklist/)
      * [CISO Corner](https://payatu.com/ciso-corner/)
      * [Datasheet](https://payatu.com/datasheet/)
      * [Ebooks](https://payatu.com/ebooks/)
      * [Masterclass](https://payatu.com/masterclass-series/)
      * [Media](https://payatu.com/media/)
    - * #### Tools
      * [BugBazaar](https://payatu.com/bugbazaar/)
      * [Securecodewiki](https://securecode.wiki/)
      * [DVAPI](https://payatu.com/dvapi/)
      * #### Community
      * [Telegram Community](https://payatu.com/community/)
  + - * [Infographics](https://payatu.com/infographics/)
* [Contact Us](https://payatu.com/contact-us/)
* [CISO Corner](https://payatu.com/ciso-corner/)

# How to Hack JWT using Burp Suite?

![](https://secure.gravatar.com/avatar/1803cdd694b7f7d38db666e7904b926b4684dee427c7ec9b36b8fdcf12157222?s=96&d=mm&r=g)

* [Vishal Saini](https://payatu.com/author/vishal-saini/)
* [February 6, 2023](https://payatu.com/2023/02/06/)

![JWT Vulnerabilities](https://i0.wp.com/payatu.com/wp-content/uploads/2023/02/Hacking-JWT-using-Burp-Suite.png?fit=2400%2C1200&ssl=1)

## What is JWT (JSON Web Token)?

JSON Web Token (JWT) is an open standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the **HMAC** algorithm) or a public/private key pair using **RSA** or **ECDSA**.

Table of Contents

Toggle

* [What is JWT (JSON Web Token)?](#What_is_JWT_JSON_Web_Token)
* [Structure of JWT](#Structure_of_JWT)
  + [Header](#Header)
  + [Payload](#Payload)
  + [Signature](#Signature)
* [How does JWT works](#How_does_JWT_works)
* [Type of Vulnerabilities in JWT and How to Find those Using Burp Suite](#Type_of_Vulnerabilities_in_JWT_and_How_to_Find_those_Using_Burp_Suite)

Signed tokens can verify the *integrity* of the claims contained within it, while encrypted tokens *hide* those claims from other parties. When tokens are signed using public/private key pairs, the signature also certifies that only the party holding the private key is the one that signed it.

JSON web token are mostly used as an authorization mechanism. As the JW...