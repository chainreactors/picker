---
title: Writing a Burp Extension to Bypass Checksum
url: https://payatu.com/blog/writing-a-burp-extension-to-bypass-checksum/
source: Payatu
date: 2024-12-21
fetch_date: 2025-10-06T19:37:05.452960
---

# Writing a Burp Extension to Bypass Checksum

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

# Writing a Burp Extension to Bypass Checksum

![](https://secure.gravatar.com/avatar/a1ffd2d0beb7e01a1b58d08b1e887204a970d7f90775aba800e76780cf687bfa?s=96&d=mm&r=g)

* [Mukund Kedia](https://payatu.com/author/mukund-kedia/)
* [December 20, 2024](https://payatu.com/2024/12/20/)

![](https://i0.wp.com/payatu.com/wp-content/uploads/2024/12/Writing-a-Burp-Extension-to-Bypass-Checksum-1.jpg?fit=2400%2C1200&ssl=1)

## **Introduction**

Automation significantly enhances the efficiency and productivity of our work. It spares the human effort involved in doing a repetitive task manually. By writing a script, we can delegate our work to the computer’s processor, which is better suited to handle such repetitive tasks.

Table of Contents

Toggle

* [Introduction](#Introduction)
* [What is Checksum, and why do we need to bypass it?](#What_is_Checksum_and_why_do_we_need_to_bypass_it)
* [Process and Code to Bypass Checksum](#Process_and_Code_to_Bypass_Checksum)
  + [Index.html](#Indexhtml)
  + [Index.js](#Indexjs)
  + [Extension.py](#Extensionpy)
  + [Encryption.py](#Encryptionpy)
* [References for the code used in creating the Burp Extension](#References_for_the_code_used_in_creating_the_Burp_Extension)
* [Demo](#Demo)
* [Conclusion](#Conclusion)
* [References:](#References)

There are already many extensions available online to automate different things on Burp. Still, sometimes, we may encounter a situation where the available Burp extensions cannot help us because, this time, the automation script has to be made specifically for the application we are testing.

There are a few blogs written ...