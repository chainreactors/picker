---
title: Understanding and Modifying the Hermes Bytecode
url: https://payatu.com/blog/understanding-modifying-hermes-bytecode/
source: Payatu
date: 2024-11-12
fetch_date: 2025-10-06T19:16:39.555410
---

# Understanding and Modifying the Hermes Bytecode

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

# Understanding and Modifying the Hermes Bytecode

![](https://secure.gravatar.com/avatar/1c3c1f8f424ec712ac584a5c1f0738a815c34b7c128be175b810ff8ca205d9b1?s=96&d=mm&r=g)

* [Vedant Wayal](https://payatu.com/author/vedant-wayal/)
* [November 11, 2024](https://payatu.com/2024/11/11/)

![](https://i0.wp.com/payatu.com/wp-content/uploads/2024/11/4-Understanding-and-Modifying-the-Hermes-Bytecode.jpg?fit=2400%2C1200&ssl=1)

The **React Native Pentesting for Android Masterclass** has taught us [how to edit and patch React Native apps](https://payatu.com/blog/editing-and-patching-react-native-applications/%E2%86%97) in the previous blog. Let’s now move on to the Hermes bytecode.

Table of Contents

Toggle

* [Understanding Hermes bytecode](#Understanding_Hermes_bytecode)
* [Let’s look at some key elements in the Hermes bytecode and try to make some sense:](#Lets_look_at_some_key_elements_in_the_Hermes_bytecode_and_try_to_make_some_sense)
  + [Oper[1]: String(strNumber)](#Oper1_StringstrNumber)
  + [createElement:](#createElement)
  + [LoadConstInt:](#LoadConstInt)
  + [Relational Operators Identification:](#Relational_Operators_Identification)
  + [Find a function name with a string:](#Find_a_function_name_with_a_string)
* [The Comparison:](#The_Comparison)
* [Steps:](#Steps)
* [Root detection bypass](#Root_detection_bypass)
* [What is JailMonkey?](#What_is_JailMonkey)
* [Bonus:](#Bonus)

The React Native team created their own JavaScript engine, Hermes, which runs React Native applications. The JS source code is often compiled into the Hermes bytecode.

[Hermes](https://hermesengine.dev/)...