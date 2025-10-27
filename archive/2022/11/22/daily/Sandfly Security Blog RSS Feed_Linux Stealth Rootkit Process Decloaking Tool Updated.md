---
title: Linux Stealth Rootkit Process Decloaking Tool Updated
url: https://sandflysecurity.com/blog/linux-stealth-rootkit-process-decloaking-tool-updated
source: Sandfly Security Blog RSS Feed
date: 2022-11-22
fetch_date: 2025-10-03T23:23:11.720591
---

# Linux Stealth Rootkit Process Decloaking Tool Updated

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Linux Stealth Rootkit Process Decloaking Tool Updated

21 November 2022

Linux Forensics

Decloaking Linux stealth rootkits that are hiding processes from view is easy with our free tool *sandfly-processdecloak* which has been updated below:

[sandfly-processdecloak on Github](https://github.com/sandflysecurity/sandfly-processdecloak)

This free tool is able to quickly decloak process hiding activity from Loadable Kernel Module (LKM) stealth rootkits on most Linux distributions and architectures. It has the following features:

* Works instantly without hooking into the kernel and causing system stability or compatibility risks.
* Static build so incident response teams can deploy even onto systems with compromised shared libraries to investigate an incident and get accurate results.
* Multi-architecture build scripts for Intel, AMD, Arm and MIPS processors.

## How Does It Work?

We us a concept called PID busting. Basically we look at what the */proc* table in Linux says is running for processes. Then, we iterate through available process IDs and see if they match. If there is a mismatch, then there is high likelihood a rootkit is hiding something from observation.

Below you can see what the process listing command *ps* shows on an infected system. There is a process that has been hidden, but it won't show up with command line tools.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux stealth rootkit hiding a process from listing.](https://www.datocms-assets.com/56687/1668993842-process-decloak-ps-listing-no-pid.png?auto=format&dpr=2&q=60&w=920 "Linux stealth rootkit hiding a process from listing.")

After running *sandfly-processdecloak* the hidden PID becomes immediately apparent.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![sandfly-processdecloak instantly decloaks hidden process on Linux.](https://www.datocms-assets.com/56687/1668993564-process-decloak-backdoor-found.png?auto=format&dpr=2&q=60&w=920 "sandfly-processdecloak instantly decloaks hidden process on Linux.")

## Investigating Suspicious Process

Once the PID has been decloaked, you can use standard process investigation methods to see what is happening. Please see this article for how to do process forensics on Linux:

[Basic Linux Malware Process Forensics for Incident Responders](https://sandflysecurity.com/blog/basic-linux-malware-process-forensics-for-incident-responders/)

## Automate Stealth Rootkit Detection Agentlessly

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly finds Linux stealth rootkit hidden process.](https://www.datocms-assets.com/56687/1668994524-sandfly-decloaked-linux-rootkit.png?auto=format&dpr=2&q=60&w=920 "Sandfly finds Linux stealth rootkit hidden process.")

The free tool can be easily scripted for automated checks, but a far easier way to do this is let Sandfly's agentless security platform do it for you 24/7. We not only can decloak hidden processes, but can also find thousands of other threats against your Linux systems without loading any endpoint agents. Check out our [free license or contact us](https://sandflysecurity.com/get-sandfly/) for a full trial.

---

Post Tags:

[Linux Forensics](/blog/tag/linux-forensics)[Rootkits](/blog/tag/rootkits)[Malware](/blog/tag/malware)

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