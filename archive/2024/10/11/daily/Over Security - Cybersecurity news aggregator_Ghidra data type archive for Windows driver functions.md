---
title: Ghidra data type archive for Windows driver functions
url: https://blog.talosintelligence.com/ghidra-data-type-archive-for-windows-drivers/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-11
fetch_date: 2025-10-06T18:55:31.716104
---

# Ghidra data type archive for Windows driver functions

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

![](/content/images/2024/10/GenericCiscoTalos-Header.jpg)

# Ghidra data type archive for Windows driver functions

By
[Chris Neal](https://blog.talosintelligence.com/author/chris-neal/)

Thursday, October 10, 2024 06:00

While reverse-engineering Windows drivers with Ghidra, it is common to encounter a function or data type that is not recognized during disassembly.

This is because Ghidra does not natively include the majority of the definitions for data types and functions used by Windows drivers.

Thankfully, these problems can usually be solved by importing Ghidra data type archive files (.gdt) that contain the relevant definitions.

However, it is not uncommon that the definitions in question aren’t available in a preexisting .gdt file, meaning a new definition must be created manually. Additionally, in some cases, the function or data type may be undocumented by Microsoft, making the process of creating a new definition a more tedious process.

To aid analysts in reverse engineering Windows drivers, Cisco Talos is releasing a GDT file on GitHub that contains various definitions for functions and data types that have been created as needed during our analysis of malicious drivers, as they were not present in the commonly used data type archives.

It is important to note that this archive is not intended to contain all undocumented Windows functions or serve as a replacement for other available data type archives, but as a supplement to them. This is a long-term project that will continue to grow when new definitions are created by our analysts and added to the public release.

The archive can be found [here](https://github.com/Cisco-Talos/Windows-drivers-GDT-file) on our GitHub repository.

##### Share this post

#### Related Content

[### UAT-8099: Chinese-speaking cybercrime group targets high-value IIS for SEO fraud

October 2, 2025 06:00

Cisco Talos is disclosing details on UAT-8099, a Chinese-speaking cybercrime group mainly involved in SEO fraud and theft of high-value credentials, configuration files, and certificate data.](/uat-8099-chinese-speaking-cybercrime-group-seo-fraud/)

[### IR Trends Q2 2025: Phishing attacks persist as actors leverage compromised valid accounts to enhance legitimacy

July 31, 2025 06:00

Phishing remained the top initial access method in Q2 2025, while ransomware incidents see the emergence of new Qilin tactics.](/ir-trends-q2-2025/)

[### IR Trends Q1 2025: Phishing soars as identity-based attacks persist

April 28, 2025 06:00

This quarter, phishing attacks surged as the primary method for initial access. Learn how you can detect and prevent pre-ransomware attacks.](/ir-trends-q1-2025/)

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