---
title: Sandfly 5.5.4 - North Korean Rootkit Decloaking
url: https://sandflysecurity.com/blog/sandfly-5-5-4-north-korean-rootkit-decloaking
source: Sandfly Security Blog RSS Feed
date: 2025-09-29
fetch_date: 2025-10-02T20:50:21.243600
---

# Sandfly 5.5.4 - North Korean Rootkit Decloaking

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.5.4 - Chinese Rootkit Decloaking

28 September 2025

Product Update

Sandfly 5.5.4 can further decloak the recently released suspected Chinese stealth rootkit targeting Korea on Linux. Additionally, we have expanded legacy device support and fixed bugs affecting drift detection.

### Decloaking Chinese Kernel Module Rootkit

The recent release of a suspected Chinese Linux stealth rootkit (detailed in [our blog post here](https://sandflysecurity.com/blog/leaked-north-korean-linux-stealth-rootkit-analysis)) gave rise to some additional detection opportunities in this 5.5.4 release. In particular, while we had no trouble finding this rootkit on prior versions, we've now added the ability to complete decloak the module being hidden on affected hosts.

The new detection module is named *kernel\_module\_vmalloc\_artifact* and will find kernel modules from this rootkit and variants (such as Reptile), that have hidden themselves. If we see a module hidden with these methods we will alert and tell you the module name hiding so security teams can investigate. Below we see the rootkit using the default name *vmwfxs* on an host.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Chinese Rootkit Hidden Module Decloak](https://www.datocms-assets.com/56687/1759092195-rootkit-kernel-module-vmalloc-artifact.png?auto=format&dpr=2&q=60&w=920 "Chinese Rootkit Hidden Module Decloak")

This new detection combines with other detections we already deployed making this rootkit very obvious if it's operating on a host. Below are the alerts we generate from the active rootkit in idle mode waiting for backdoor activation.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Chinese/North Korean Rootkit Alarm from Sandfly](https://www.datocms-assets.com/56687/1759092377-rootkit-alerts.png?auto=format&dpr=2&q=60&w=920 "Chinese/North Korean Rootkit Alarm from Sandfly")

### Expanded Legacy Device Coverage

Sandfly has the widest and most complete coverage of Linux in the industry. We are further expanding our coverage to more embedded devices with this release, including some that are well over a decade old. With Sandfly 5.5.4 we now support legacy and modern devices running Dropbear SSH and even more ARM processors than before.

### Drift Detection Bug Fix

We fixed a bug in drift detection profiles where alerts could be added to a known-good profile by accident. This bug would happen if users had valid alerts, but selected non-alerts to add to a profile. In this case, valid alerts may be added to the known-good profile resulting in them also being ignored. This is a corner case situation that would not likely affect most customers, but if you think you were affected it may require re-building drift profiles to resolve. Please reach out to customer support with any questions if you think you are in this small potential group of users.

### False Positives on New Linux Distros

New Linux distributions such as Debian 13 are moving away from legacy log files for login auditing such as *wtmp* and *utmp*. We have corrected false alarms happening when we see these files missing as they won't be on Linux systems going forward.

### UI Bug Fixes

We have made small changes to the UI to fix other bugs and improve operation.

### Upgrading Sandfly

Sandfly 5.5.4 has important detection updates and bug fixes and we recommend customers upgrade at their convenience.

Please be sure to see our documentation on the new features and capabilities:

[Sandfly Documentation](https://docs.sandflysecurity.com)

Customers wishing to upgrade can follow the instructions here:

[Upgrading Sandfly](https://docs.sandflysecurity.com/docs/upgrading-sandfly)

If you have any questions, please [reach out to us](https://www.sandflysecurity.com/contact-us/) or [get your own version of Sandfly](https://sandflysecurity.com/get-sandfly) to try out today.

Thank you for using Sandfly.

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