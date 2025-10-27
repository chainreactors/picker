---
title: OWASP Global AppSec Dublin 2023: WorldWide and Threat Modeling
url: https://blog.mindedsecurity.com/2023/02/owasp-global-appsec-dublin-2023.html
source: IMQ Minded Security Blog
date: 2023-02-25
fetch_date: 2025-10-04T08:04:21.044038
---

# OWASP Global AppSec Dublin 2023: WorldWide and Threat Modeling

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

## Friday, February 24, 2023

# OWASP Global AppSec Dublin 2023: WorldWide and Threat Modeling

#

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjFLx0cRigZarMDU3cDATxMC-R7AGDiaFphYyupun9tdWOLr2-tIElV-EaI1pNQ05JDy_t87ASsYPXzZmwMCqyIZK37eHnN_QTm8OsknM6ZgEIHuY9ze8QZj9aj_jKtaR0zt2QerKquPHjcEkfwXw7rRt0RhWJBzK_LEv7efkUS10O9WRUmwOBUzv0E1Q)](https://blogger.googleusercontent.com/img/a/AVvXsEjFLx0cRigZarMDU3cDATxMC-R7AGDiaFphYyupun9tdWOLr2-tIElV-EaI1pNQ05JDy_t87ASsYPXzZmwMCqyIZK37eHnN_QTm8OsknM6ZgEIHuY9ze8QZj9aj_jKtaR0zt2QerKquPHjcEkfwXw7rRt0RhWJBzK_LEv7efkUS10O9WRUmwOBUzv0E1Q)

The OWASP Global AppSec Dublin 2023 conference was a truly inspiring event for anyone involved in application security. As an attendee, I was able to catch up with OWASP colleagues and hear from experts on a range of topics.

In particular, there were two themes that really stood out to me: *worldwide* and *threat modeling*.

#### OWASP: The Open Worldwide Application Security Project

During the conference, the OWASP Board made an exciting announcement regarding the meaning of the letter "W" in OWASP. Traditionally, the "W" in OWASP has stood for "Web," reflecting the organization's initial focus on web application security. The Board announced they are changing the meaning of the "W" to "Worldwide," reflecting the global nature of the OWASP project and its mission.

This change is significant because it recognizes that application security is no longer limited to just web applications. With the proliferation of mobile and IoT devices, cloud computing, and other emerging technologies, application security has become a much broader concern. By changing the meaning of the "W" to "Worldwide," OWASP is acknowledging this reality and expanding its focus to include all types of applications.

The change in the meaning of the "W" in OWASP from "Web" to "Worldwide" is a significant development for the organization and the application security community as a whole. It reflects the evolving nature of application security and the importance of the global community in addressing these challenges. I am excited to see how this change will shape the future of OWASP and its mission to make software security visible worldwide.

####

#### Threat Modeling

Threat modeling is a structured approach for identifying, quantifying, and addressing the security risks associated with an application. In recent years, there has been a growing interest in this area, and the conference featured a keynote and two talks on the subject.

The conference had a keynote, a training session and 2 talks regarding threat modeling. The keynote, “A Taste of Privacy Threat Modeling” by Kim Wuyts, focused on threat modeling privacy. Ms. Wuyts spoke about how to identify potential privacy threats and how to mitigate those risks. She also provided insights into best practices for threat modeling in a privacy context.

Other talks at the event emphasized practical approaches on Threat Modeling that are essential for companies to adopt in order to develop more secure products and services. These presentations provided valuable insights and actionable recommendations that can help organizations improving their security posture and better protect their customers' data and privacy.

Threat modeling is not a new concept. In fact, it has been around for quite some time. However, it has only recently gained traction within the application security community. This is likely due to the increasing number of data breaches and cyber attacks that have occurred in recent years. Organizations are now more aware than ever of the need to secure their applications against potential threats.

Since the inception of o...