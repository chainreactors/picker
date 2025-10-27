---
title: Bypassing Certificate Pinning on Flutter-based Android Apps. A new guide.
url: https://blog.mindedsecurity.com/2024/05/bypassing-certificate-pinning-on.html
source: IMQ Minded Security Blog
date: 2024-05-08
fetch_date: 2025-10-06T17:16:13.008464
---

# Bypassing Certificate Pinning on Flutter-based Android Apps. A new guide.

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

## Tuesday, May 7, 2024

# Bypassing Certificate Pinning on Flutter-based Android Apps. A new guide.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiLZOgVn35LqPDpfHUk6wcqLOjrvV6JioR2CPitS6-4WhuB6jSaudX8wXAwTaHk3U7ebucLS-R5vO6GRTF2dC-cjzUcm-qv1IQLhkB-zDUYLavj06fTkgqAbwsix1lSP2klyN8rqETtdsCcQFAv_FOKE9AGSNQ0TOyi3q5sxBSkyE_lhziAZbmO1DDnroxg)](https://blogger.googleusercontent.com/img/a/AVvXsEiLZOgVn35LqPDpfHUk6wcqLOjrvV6JioR2CPitS6-4WhuB6jSaudX8wXAwTaHk3U7ebucLS-R5vO6GRTF2dC-cjzUcm-qv1IQLhkB-zDUYLavj06fTkgqAbwsix1lSP2klyN8rqETtdsCcQFAv_FOKE9AGSNQ0TOyi3q5sxBSkyE_lhziAZbmO1DDnroxg)

One of the preliminary activities when analyzing mobile application, *more usually than not*, is to be able to sniff HTTP/S traffic via **a MitM proxy**.

This is quite straightforward in the case of naive applications, but can be quite challenging when applications use [certificate pinning](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning) techniques. In this post I'll try to explain the methodology I used to make this possible for a **Flutter-based** **Android** sample application in a reliable way.

#### **Introduction**

It was indeed the need to *bypass* a certificate validation on a *Flutter framework* during a mobile application penetration testing activity for a customer of ours, that led to this research.

As a first approach, as usual, we tried [some](https://github.com/NVISOsecurity/disable-flutter-tls-verification/blob/main/disable-flutter-tls.js) of the [specific](https://blog.nviso.eu/2022/08/18/intercept-flutter-traffic-on-ios-and-android-http-https-dio-pinning/%20https%3A//blog.nv) [exploits](https://iso.eu/2019/08/13/intercepting-traffic-from-android-flutter-applications/)/[bypasses](https://alijujara.medium.com/proxying-traffic-on-android-flutter-applications-d3f70655df66) we found on the web.

Alas, in this case, they failed.

Some of the main concepts that are going to be explained, actually, overlap in what those articles contain; what it differs is the technique used for identifying and hooking at runtime the routine used for certificate verification.

While minimizing effort was a key objective in bypassing certificate pinning controls, the chosen approach turned out to be overly generic.  Unlike pattern matching techniques, which can be tailored to specific scenarios, this method becomes unreliable across different platforms, architectures, and even builds.

While the article's findings may not address all the case studies, it proposes an effective methodology that can be readily applied, with minimal adjustments, to similar scenarios.

Moreover, as a different approach, [reFlutter](https://github.com/Impact-I/reFlutter) would be a valid tool for such a similar job. Anyway, as it statically patches code to deactivate runtime checks, if the mobile application was signed and/or had file integrity checks, static approach would definitely be challenging.

In the next paragraphs, we're going to cover the following topics:

* Why Flutter is so different
* Flutter based APK structure
* Force traffic forwarding to my proxy
* Diving into BoringSSL source code
* Reverse-engineering on libflutter.so
* Frida hooking script

Finally, in order to give some testbed, we created a basic Flutter application which fetches data from the URL [https://dummy.restapi.example.ltd/api/v1/employees](https://dummy.restapiexample.com/api/v1/employees), using code that correctly implements **[certificate pinning](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)**.

The entire application code, the build and the [Frida](https://frida.re/) script are available on Github at the following link:

<http...