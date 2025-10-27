---
title: The vulnerabilities we uncovered by fuzzing µC/OS protocol stacks
url: https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-29
fetch_date: 2025-10-06T18:07:33.576995
---

# The vulnerabilities we uncovered by fuzzing µC/OS protocol stacks

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# The vulnerabilities we uncovered by fuzzing µC/OS protocol stacks

By
[Kelly Patterson](https://blog.talosintelligence.com/author/kelly/)

Wednesday, August 28, 2024 12:00

[Vulnerability Deep Dive](https://blog.talosintelligence.com/category/vulnerability-deep-dive/)

Hunting for vulnerabilities in industrial environments has become increasingly important as industrial control systems and critical infrastructure face threats from state-sponsored actors and ransomware groups hoping to cash out on million-dollar payments.

Fuzzing has long been one of our favorite ways to search for security issues or vulnerabilities in software, but when it comes to fuzzing popular systems used in ICS environments, it traditionally involved a custom hardware setup to fuzz the code in its native environment.

However, I recently created my own fuzzer after Weston Embedded made its full µC/OS protocol stack source code openly available in 2020. µC/OS (also stylized as MicroC/OS) is a real-time operating system commonly used in resource-constrained embedded systems like industrial control systems. The operating system uses a scheduling mechanism to ensure efficient task management in industrial environments, and we recently discovered multiple vulnerabilities in the system that could allow an adversary to carry out a range of malicious actions, including causing a denial of service or gaining the ability to execute arbitrary code on the system.

Today, we’re publishing a three-part look at how I created this fuzzer, the various hurdles I faced along the way, and how it used it to fuzz two different µC/OS protocol stacks. These individual posts are linked below.

* [Part 1: HTTP server fuzzing](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-1/)
* [Part 2: Handling multiple requests per test case](https://blog.talosintelligence.com/fuzzing-ucos-protocol-stacks-part-2/)
* [Part 3: TCP/IP server fuzzing, implementing a TAP driver](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-3/)

##### Share this post

#### Related Content

[### ReVault! When your SoC turns against you… deep dive edition

August 9, 2025 09:00

Talos reported 5 vulnerabilities to Broadcom and Dell affecting both the ControlVault3 Firmware and its associated Windows APIs that we are calling “ReVault”.](/revault-when-your-soc-turns-against-you-2/)

[### Decrement by one to rule them all: AsIO3.sys driver exploitation

June 26, 2025 06:00

Cisco Talos uncovered and analyzed two critical vulnerabilities in ASUS' AsIO3.sys driver, highlighting serious security risks and the importance of robust driver design.](/decrement-by-one-to-rule-them-all/)

[### Small praise for modern compilers - A case of Ubuntu printing vulnerability that wasn’t

February 10, 2025 08:30

During an earlier investigation of the macOS printing subsystem, IPP-USB protocol caught our attention. We decided to take a look at how other operating systems handle the same functionality.](/small-praise-for-modern-compilers-a-case-of-ubuntu-printing-vulnerability-that-wasnt/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://talosintelligence.com/incident_response)
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* + ###### Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* + ###### Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* + ###### Support
  + [Support Documentation](https://support.talosintelligence.com)
* + ###### Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)
  + [Cisco Security](https://www.cisco.com/c/en/us/products/security/product-listing.html)

###### Follow us

[![Cisco](https://blog.talosintelligence.com/assets/images/logo_cisco_white.svg)](http://tools.cisco.com/security/center/home.x)

©
Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our
[Privacy Policy.](http://www.cisco.com/web/siteassets/legal/privacy_full.html)