---
title: Understanding HTTP Request Smuggling with Hop-to-Hop Headers
url: https://payatu.com/blog/http-request-smuggling/
source: Payatu
date: 2023-04-01
fetch_date: 2025-10-04T11:20:32.960563
---

# Understanding HTTP Request Smuggling with Hop-to-Hop Headers

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

# Understanding HTTP Request Smuggling with Hop-to-Hop Headers

![](https://secure.gravatar.com/avatar/a1ffd2d0beb7e01a1b58d08b1e887204a970d7f90775aba800e76780cf687bfa?s=96&d=mm&r=g)

* [Mukund Kedia](https://payatu.com/author/mukund-kedia/)
* [March 31, 2023](https://payatu.com/2023/03/31/)

![HTTP Request Smuggling](https://i0.wp.com/payatu.com/wp-content/uploads/2023/03/MicrosoftTeams-image-30.png?fit=2084%2C1024&ssl=1)

We have seen HTTP request smuggling attacks by modifying the Content-Length and Transfer-Encoding header. These methods exploit the execution of the headers on the client-side and server side. However, there’s also another way of performing this attack by using hop-to-hop headers. In this blog, we will discuss this technique in complete detail.

Table of Contents

Toggle

* [What are Hop-to-Hop Headers?](#What_are_Hop-to-Hop_Headers)
* [Using Content-Length as Hop-to-Hop Header](#Using_Content-Length_as_Hop-to-Hop_Header)
* [Server-side Caching at Edge Nodes](#Server-side_Caching_at_Edge_Nodes)
  + [What is Server-Side Caching?](#What_is_Server-Side_Caching)
* [What are Edge Nodes?](#What_are_Edge_Nodes)
* [Conclusion](#Conclusion)

This requires intermediate proxy servers between the client and the main server. We will also briefly discuss server-side cache poisoning using the techniques mentioned above. This way of exploiting the server-side cache was found by Francesco Mariani and Jacopo Tediosi in a private bug bounty program of Akamai CDN.

## **What are Hop-to-Hop Headers?**

[Hop-to-hop headers](https://datatracker.ietf.org/doc/html/rfc2068#section-13.5.1...