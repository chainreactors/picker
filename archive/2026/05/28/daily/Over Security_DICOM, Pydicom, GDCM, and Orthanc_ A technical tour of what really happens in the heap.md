---
title: DICOM, Pydicom, GDCM, and Orthanc: A technical tour of what really happens in the heap
url: https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:10.767197
---

# DICOM, Pydicom, GDCM, and Orthanc: A technical tour of what really happens in the heap

[Blog](/)

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

# DICOM, Pydicom, GDCM, and Orthanc: A technical tour of what really happens in the heap

By
[Emmanuel Tacheau](https://blog.talosintelligence.com/author/emmanuel/)

Thursday, May 28, 2026 06:00

[Vulnerability Deep Dive](https://blog.talosintelligence.com/category/vulnerability-deep-dive/)

Over the last decade, DICOM parsing has become an active research topic. The reason is simple: DICOM is both critical and complicated. Hospitals rely on DICOM-based PACS systems, and those systems often automatically ingest files received over the network. That means malformed data could directly trigger vulnerable decoders — the holy grail of attack surfaces for those studying robustness.

This white paper presents a concrete case study demonstrating the creation of a heap overflow vulnerability through the exploitation of the DICOM file format. The objective is to show how an Orthanc server can be targeted during the image upload process, resulting in an out-of-bounds write.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/05/DICOM2026_buttonbg-3.jpg)

## DICOM, Pydicom, GDCM, and Orthanc

A technical tour of what really happens
in the heap

[Download now](https://blog.talosintelligence.com/content/files/2026/05/DICOM2026-2.pdf)

##### Share this post

#### Related Content

[### “Good enough” emulation: Fuzzing a single thread to uncover vulnerabilities

February 18, 2026 06:00

A Talos researcher used targeted emulation of the Socomec DIRIS M-70 gateway’s Modbus thread to uncover six patched vulnerabilities, showcasing efficient tools and methods for IoT security testing.](/good-enough-emulation/)

[### ReVault! When your SoC turns against you… deep dive edition

August 9, 2025 09:00

Talos reported 5 vulnerabilities to Broadcom and Dell affecting both the ControlVault3 Firmware and its associated Windows APIs that we are calling “ReVault”.](/revault-when-your-soc-turns-against-you-2/)

[### Decrement by one to rule them all: AsIO3.sys driver exploitation

June 26, 2025 06:00

Cisco Talos uncovered and analyzed two critical vulnerabilities in ASUS' AsIO3.sys driver, highlighting serious security risks and the importance of robust driver design.](/decrement-by-one-to-rule-them-all/)

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