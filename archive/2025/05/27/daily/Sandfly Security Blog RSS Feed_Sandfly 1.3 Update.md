---
title: Sandfly 1.3 Update
url: https://sandflysecurity.com/blog/sandfly-1-3-update
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:27:48.451976
---

# Sandfly 1.3 Update

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 1.3 Update

22 July 2018

Product Update

A new version of Sandfly has been released. Version 1.3 has the following changes:

* Container OS was switched from Alpine to Ubuntu Minimal for better compatibility and more up to date packages.
* TLS 1.1 has been disabled across the board. Only TLS 1.2 and 1.3 will be supported going forward which will cover all modern browsers.
* Sandflies renamed to be more consistent and descriptive.
* Sandfly Process Persistence Cron Malicious and Sandfly Process Persistence At Job Malicious sandflies will also flag executable files inside these directories along with the standard malware persistence checks.
* New sandflies to search for running processes out of unusual system directories like /lost+found or /boot.
* Expanded checks for legacy rootkits from the leaked NSA source code repositories.
* New sandfly checks for SUID/SGID system shells.
* Expanded checks for SUID/SGID system editors which can be left behind for future escalation attacks by intruders.
* Performance and reliability fixes.
* We are adding many new sandflies now to detect an ever increasing list of threats against Linux. If you have any questions about the update, please contact us.

We recommend you upgrade to take advantage of the above by following the simple instructions here:

[Upgrading Sandfly](https://docs.sandflysecurity.com/docs/upgrading-sandfly)

Thank you for using Sandfly.

---

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