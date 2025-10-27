---
title: A Cool New Project: Semgrep Rules for Android Apps Security
url: https://blog.mindedsecurity.com/2023/06/a-cool-new-project-semgrep-rules-for.html
source: IMQ Minded Security Blog
date: 2023-06-22
fetch_date: 2025-10-04T11:47:06.613206
---

# A Cool New Project: Semgrep Rules for Android Apps Security

[Subscribe our newsletter](https://mindedsecurity.com/newsletter)

[Minded Security](https://mindedsecurity.com)

* Industry
  + [Automotive/Maritime](https://mindedsecurity.com/industry/automotive-maritime/ "Automotive/Maritime")
  + [Financial](https://mindedsecurity.com/industry/financial/ "Financial")
  + [GDO](https://mindedsecurity.com/industry/gdo/ "GDO")
  + [Industrial Control Systems](https://mindedsecurity.com/industry/industrial-control-systems/ "Industrial Control Systems")
  + [IoT Security](https://mindedsecurity.com/industry/iot-security/ "IoT Security")
  + [Healthcare](https://mindedsecurity.com/industry/healthcare/ "Healthcare")
  + [Government](https://mindedsecurity.com/industry/government/ "Government")
* [Services](https://mindedsecurity.com/our-services/ "Services")
  + [Training](https://mindedsecurity.com/our-services/training/ "Training")
    - [Security Hackaton](https://mindedsecurity.com/services/training/security-hackaton/ "Security Hackaton")
    - [Advanced On-site Training](https://mindedsecurity.com/services/training/advanced-on-site-training/ "Advanced On-site Training")
    - [BlueClosure Training](https://mindedsecurity.com/services/training/blueclosure-training/ "BlueClosure Training")
    - [High Level Training](https://mindedsecurity.com/services/training/high-level-training/ "High Level Training")
    - [Webinar](https://mindedsecurity.com/services/training/webinar/ "Webinar")
  + [Testing](https://mindedsecurity.com/our-services/testing/ "Testing")
    - [Manual Secure Code Review](https://mindedsecurity.com/services/testing/manual-secure-code-review/ "Manual Secure Code Review")
    - [Manual WAPT](https://mindedsecurity.com/services/testing/manual-wapt/ "Manual WAPT")
    - [Cloud Security Testing](https://mindedsecurity.com/services/testing/cloud-security-testing/ "Cloud Security Testing")
    - [IoT Security](https://mindedsecurity.com/services/testing/iot-security/ "IoT Security")
    - [API Security](https://mindedsecurity.com/services/testing/api-security/ "API Security")
    - [Mobile Security Assessment](https://mindedsecurity.com/services/testing/mobile-security-assessment/ "Mobile Security Assessment")
    - [Client Side Assessment](https://mindedsecurity.com/services/testing/client-side-assessment/ "Client Side Assessment")
  + [Consulting](https://mindedsecurity.com/our-services/consulting/ "Consulting")
    - [Software Security Advisory](https://mindedsecurity.com/services/consulting/software-security-advisory/ "Software Security Advisory")
    - [5D Framework](https://mindedsecurity.com/services/consulting/5d-framework/ "5D Framework")
    - [Threat Modeling](https://mindedsecurity.com/services/consulting/threat-modeling/ "Threat Modeling")
    - [Secure Design](https://mindedsecurity.com/services/consulting/secure-design/ "Secure Design")
    - [Secure Architecture Review](https://mindedsecurity.com/services/consulting/secure-architecture-review/ "Secure Architecture Review")
    - [Secure Coding Guidelines](https://mindedsecurity.com/services/consulting/secure-coding-guidelines/ "Secure Coding Guidelines")
    - [Fixing Support](https://mindedsecurity.com/services/consulting/fixing-support/ "Fixing Support")
    - [Outsourcing Development Governance](https://mindedsecurity.com/services/consulting/outsourcing-development-governance/ "Outsourcing Development Governance")
  + [Request a brochure](https://mindedsecurity.com/request-a-brochure/ "Request a brochure")
* Resources
  + [Blog](https://blog.mindedsecurity.com/ "Blog")
  + [News](https://mindedsecurity.com/category/news/ "News")
  + [Videos](https://mindedsecurity.com/videos/ "Videos")
  + [Research](https://mindedsecurity.com/research/ "Research")
  + [Advisories](https://mindedsecurity.com/research/advisories/ "Advisories")
* [About us](https://mindedsecurity.com/our-mission/ "About us")
  + [The Company](https://mindedsecurity.com/the-company/ "The Company")
  + [Contact us](https://mindedsecurity.com/contact-us/ "Contact us")
  + [Newsletter](https://mindedsecurity.com/newsletter/ "Newsletter")
  + [Jobs](https://mindedsecurity.com/jobs/ "Jobs")
  + [Privacy Policy](https://mindedsecurity.com/privacy-policy/ "Privacy Policy")

## IMQ Minded Security Blog

[skip to main](#main)  |
[skip to sidebar](#sidebar)

## Wednesday, June 21, 2023

# A Cool New Project: Semgrep Rules for Android Apps Security

[![Android Logo with a key like shape to introduce security.](https://blogger.googleusercontent.com/img/a/AVvXsEiL6HespqFZ1OGFnsE4OchEw6H3FVjCY0hgeeCzdUpAqd373AeLElvHAcEFIE_lbc6KUSwkSf8ZEW65_r1Eq3R_VFVDFCjr6Boug-p-AITviNgw52nR9gnur2LjCmxaqxTbtlW6Dpb83pH6BDgmPPtaNle6fhCHldOLmYTXFsgZCmK-MTU-Yb0FDNQM72w=w320-h180)](https://blogger.googleusercontent.com/img/a/AVvXsEiL6HespqFZ1OGFnsE4OchEw6H3FVjCY0hgeeCzdUpAqd373AeLElvHAcEFIE_lbc6KUSwkSf8ZEW65_r1Eq3R_VFVDFCjr6Boug-p-AITviNgw52nR9gnur2LjCmxaqxTbtlW6Dpb83pH6BDgmPPtaNle6fhCHldOLmYTXFsgZCmK-MTU-Yb0FDNQM72w)

In today's digital landscape, **mobile application security** has become an **paramount concern**.

With the increasing number of threats targeting ***Android*** applications and the stored personal data, developers and security professionals alike are seeking robust solutions to fortify their code against potential vulnerabilities.

That's why speeding up the time and minimizing the effort in the identification of mobile security issues has become definitely important.

We are excited to introduce our [new project](https://github.com/mindedsecurity/semgrep-rules-android-security), focused on creating [Semgrep](https://semgrep.dev/) rules specifically designed to enhance the security of Android apps.

**[Semgrep Rules for Android Application Security](https://github.com/mindedsecurity/semgrep-rules-android-security)**

The project provides a new set of specific rules for [OWASP Mobile Security Testing Guide (MSTG)](https://owasp.org/www-project-mobile-app-security/), that will help to find security issues using [static code analysis (SAST)](https://www.gartner.com/en/information-technology/glossary/static-application-security-testing-sast).

### The Project

The OWASP Mobile Security Testing Guide (MSTG) is an invaluable resource for assessing the security posture of mobile applications. It provides comprehensive guidelines and best practices to identify and address potential security weaknesses. However, manually conducting these tests can be time-consuming and prone to human error.

**This is where this project come into play.**

By creating a set of Semgrep rules based on the OWASP Mobile Security Testing Guide, we aim to automate and streamline the security testing process for Android applications.

These rules act as a way to shift left in the SDLC of Mobile apps, enabling developers and security practitioners to efficiently identify and mitigate vulnerabilities in their code.

With Semgrep's static analysis capabilities and the knowledge base of the MSTG, we can significantly enhance the effectiveness and efficiency of mobile apps security assessments.

Our project bridges the gap between theory and practice, empowering developers to build robust and resilient Android applications while ensuring that security remains a top priority.

### Status

Since the beginning of the project to the present stage, we have continuously strived to deliver a solution to empower developers and security practitioners and defend against evolving threats and safeguard user data.

The actual status of our project shows where it's going to be improved and where the semgrep version limitation is a blocker to create a useful rule is [shown here](https://github.com/mindedsecurity/semgrep-rules-android-security/blob/main/status.md), and every improvement will be updated as soon as it will be implemented.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi5DdVzmfmrek3mjIbtKgiL0LU_K0vqZ7Z2al25enaw4OQDfpP8TZaGAzrmYSGKsZUIpWanaq6lTi77aCFFBJMucJ0gXiCxJDjYphosnLNWOPFNQoAStlEbEVgmRh5U8KoSWkVYgqQuRgyEWh8wVIM3qkgQ...