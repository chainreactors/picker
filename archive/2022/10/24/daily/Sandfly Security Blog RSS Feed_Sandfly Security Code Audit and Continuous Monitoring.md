---
title: Sandfly Security Code Audit and Continuous Monitoring
url: https://www.sandflysecurity.com/blog/sandfly-security-code-audit-and-continuous-monitoring
source: Sandfly Security Blog RSS Feed
date: 2022-10-24
fetch_date: 2025-10-03T20:43:13.222719
---

# Sandfly Security Code Audit and Continuous Monitoring

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly Security Code Audit and Continuous Monitoring

23 October 2022

Product Update

Sandfly is proactive about protecting the security of our customers and has recently completed an external code audit of our on-host forensic engines with no significant security issues. Further, all builds use Veracode to do automatic static and dynamic analysis during our development cycle. Using manual and automated audits provides assurance to customers that our product is safe and following industry best practices to prevent attacks.

## Cure53 Code Audit

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1662549597-cure53-logo.png?auto=format&dpr=2&q=60&w=920)

Sandfly engaged [Cure53](https://www.cure53.de/) to conduct an extensive code review of our on-host forensic engines. Cure53 is a highly respected firm that has conducted audits of many products such as [VPN clients and password managers](https://cure53.de/#publications) used by millions of people.

The audit encompassed a complete code review as well as analysis for attack vectors that could lead to privilege escalation or other problems during execution. The audit consisted of two phases:

* White box penetration tests against the Sandfly implementation and binary.
* Complete source code audit against the Sandfly forensic engines.

## White Box Penetration Tests

A "white box" test means that auditors have access to the source code so that they can analyze and prepare attacks with full knowledge of the underlying system. This is different than "black box" testing where the auditors have no visibility into the code and have to attempt to blindly exploit potential problems. The primary difference is with white box testing the attacks can be far more focused and efficient without risk of missing obvious problems as nothing is hidden.

Cure53 reports the following from the white box testing phase of Sandfly:

> *Throughout the binary review phase, no particularly noteworthy attack vectors or weaknesses were discovered. In addition, the entire scan process was traced using Linux’s syscall tracing facilities to ensure any potential attack vectors were discovered.The most significant security risk naturally stems from the fact that Sandfly runs with super-user privileges. Given its passive nature, however, the testing team was unable to detect any vulnerabilities that would otherwise allow for privilege escalation from low to root by abusing the Sandfly binary.*Cure53 Sandfly Security Audit

## Source Code Audits

Cure53 also conducted a full source code audit of the Sandfly binary. During this review no significant findings were found. Remediation was applied to a small handful of low-impact issues.

> *In summary, no significant privilege-escalation vectors were identified in the assigned time frame of the audit. Notably, the Sandfly agent itself only performs passive actions on the host and does not perform any active actions that would otherwise be exploitable by a malicious actor to cause harm on the system.*Cure53 Sandfly Security Audit

They conclude:

> *In conclusion, the scope components under scrutiny by the testing team for this audit appear robust from a security perspective. Cure53 is pleased to report that no other concerning or worrisome findings were detected. Following the successful mitigation of the relevant issues enumerated in this report, the platform will undoubtedly be well safeguarded for production use.*Cure53 Sandfly Security Audit

## Veracode Automatic Dynamic and Static Code Audit

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1662520600-verified.png?auto=format&dpr=2&q=60&w=920)

In addition to manual code reviews, Sandfly uses Veracode to perform automatic dynamic and static code audits to every build. Any problems detected are investigated and addressed without allowing any them to be delivered to customers. We are listed as part of the Veracode vendor directory below:

[Veracode Verified Directory for Sandfly Security](https://www.veracode.com/verified/directory/sandfly-security)

## Reports Available to Customers

The Cure53 and Veracode reports are available to licensed customers and those evaluating Sandfly for licensing. Please [contact us](https://www.sandflysecurity.com/contact-us/) if you'd like a copy of these reports.

---

Post Tags:

[Product Update](/blog/tag/product-update)[News](/blog/tag/news)

Share this post:

[← Return to Blog](/blog)

---

#### Contact Us

---

+64 3 3792313[4 Ash Street Christchurch, New Zealand 8011](https://goo.gl/maps/9cFto1o6GNa9RK6S9)

#### Connect With Us

---

#### Product Navigation

---

* [Threat Detection](/platform/threat-detection)
* [SSH Key Monitoring](/platform/ssh-key-monitoring)
* [Password Auditing](/platform/password-auditing)
* [Drift Detection](/platform/drift-detection)
* [Incident Response](/platform/incident-response)
* [Requirements & Installation](/resources/requirements-installation)

#### General Navigation

---

* [Our Company](/about-us/our-company)
* [Partners](/about-us/partner)
* [Under Attack?](/under-attack)
* [Contact Us](/contact-us)
* [Let’s Connect](/request-a-meeting)
* [Manage My Subscription](https://billing.sandflysecurity.com/p/login/28o7tJe2vbLNfEA9AA)

#### Sign-up For Updates

---

First Name

First Name

Last Name

Last Name

Email

Email

Subscribe

© 2025 Sandfly Security, Ltd. [End User License Agreement](/end-user-license-agreement) & [Privacy Policy](/privacy-policy). This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

[![Veracode Verified Standard](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fveracode-verified-standard-white.d24ef83e.png&w=384&q=75 "Veracode Verified Standard")](https://www.veracode.com/verified/directory/sandfly-security)