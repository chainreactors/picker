---
title: Deprecation of Linux Kernels Prior to 3.2 in Sandfly 5.8
url: https://sandflysecurity.com/blog/deprecation-of-linux-kernels-prior-to-32-in-sandfly-58
source: Sandfly Security Blog RSS Feed
date: 2026-07-15
fetch_date: 2026-07-16T04:57:32.837835
---

# Deprecation of Linux Kernels Prior to 3.2 in Sandfly 5.8

[Meet Sandfly @ Black Hat 2026 · Free 3-month Pro license. Claim Now](/blog/sandfly-is-coming-to-black-hat-usa-2026)

[Partners](/partners)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Deprecation of Linux Kernels Prior to 3.2 in Sandfly 5.8

14 July 2026

Product Update

The latest 5.8 release of Sandfly deprecates support for scanning hosts running Linux kernels older than version 3.2. This includes older distributions such as CentOS 6 and RHEL 6, along with any legacy systems running on kernels older than 3.2.

We apologize for not communicating this change directly in our release notes and want to provide a critical update to our customers here.

### Why Are Older Kernels Being Deprecated?

Under the hood, Sandfly is built using the Go programming language, designed by Google for exceptional compatibility, memory safety, and high performance.

Over time, the Go runtime has evolved to introduce new features, patch security vulnerabilities, and improve system efficiency. Previously, we maintained backwards compatibility by backporting important fixes, understanding that many customers relied on legacy systems. Unfortunately, the volume of changes reached a point where maintaining secure compatibility while continuing to build new features was no longer feasible.

As a result, we have transitioned to the latest Go version, which permanently ends support for Linux kernels older than 3.2.

### Supported Distributions

As of this writing, major Linux distributions that feature kernel 3.2 or later include:

* Ubuntu 12.04 and later
* Debian 7 and later
* Red Hat Enterprise Linux (RHEL) 7 and later
* CentOS 7 and later
* Other distributions released in the 2013–2014 timeframe or later

If you are running distributions such as CentOS 6 or RHEL 6, Sandfly 5.8 will no longer be able to scan them unless their kernel has been upgraded to version 3.2 or higher.

### Guidance for Sandfly 5.7 Users

We understand that some organizations must maintain kernels older than 3.2 for legacy operations. If this applies to your environment, **we recommend remaining on Sandfly 5.7 and deferring your upgrade to 5.8.** However, we strongly advise upgrading the underlying kernels on these legacy hosts as soon as possible to ensure ongoing security and compatibility.

### Thank You for Your Continued Support

We know that system deprecations impact your operations, and we tried to defer this transition for as long as possible. Ultimately, we had to make a choice between delivering essential security and performance enhancements for our core product and continuing to support legacy environments.

If you have any questions or need assistance navigating these changes, please reach out to our support team—we are always happy to help.

We have updated our [Operational FAQ](https://docs.sandflysecurity.com/docs/operational-faq#what-is-the-oldest-os-or-kernel-that-sandfly-can-scan) with additional details regarding this change.

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
* [Partners](/partners)
* [Under Attack?](/under-attack)
* [Contact Us](/contact-us)
* [Meet with Sandfly Security](/request-a-meeting)
* [Manage My Subscription](https://billing.sandflysecurity.com/p/login/28o7tJe2vbLNfEA9AA)

#### Sign-up For Updates

---

© 2026 Sandfly Security, Ltd. [End User License Agreement](/end-user-license-agreement) & [Privacy Policy](/privacy-policy). This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

[![Veracode Verified Standard](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fveracode-verified-standard-white.0wl0q8_t1q1d6.png&w=384&q=75 "Veracode Verified Standard")](https://www.veracode.com/verified/directory/sandfly-security)

Get the latest product updates and research delivered to your inbox.

Email

Email

Subscribe