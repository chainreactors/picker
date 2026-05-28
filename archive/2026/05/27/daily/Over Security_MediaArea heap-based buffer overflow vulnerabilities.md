---
title: MediaArea heap-based buffer overflow vulnerabilities
url: https://blog.talosintelligence.com/mediaarea-heap-based-buffer-overflow-vulnerabilities/
source: Over Security
date: 2026-05-27
fetch_date: 2026-05-28T06:02:43.015250
---

# MediaArea heap-based buffer overflow vulnerabilities

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

# MediaArea heap-based buffer overflow vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, May 27, 2026 10:00

[Vulnerability Roundup](https://blog.talosintelligence.com/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed four vulnerabilities in MediaArea MediaInfoLib library.

The vulnerabilities mentioned in this blog post have been patched by their respective vendor, in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **MediaArea vulnerabilities**

*Discovered by Dimitrios Tatsis of Cisco Talos.*

MediaArea produces digital media analysis open-source software, as well as support tools for file investigation. MediaInfoLib provides a UI for technical and tag data for video and audio media files. Talos discovered four vulnerabilities in MediaInfoLib.

[TALOS-2026-2367](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2367) (CVE-2026-25104), [TALOS-2026-2368](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2368) (CVE-2026-25713), [TALOS-2026-2371](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2371) (CVE-2026-28764), and [TALOS-2026-2374](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2374) (CVE-2026-22554) are heap-based buffer overflow vulnerabilities in various functionalities of MediaInfoLib (version(s): 26.01). All can lead to arbitrary code execution. An attacker can provide a malicious file to trigger these vulnerabilities.

##### Share this post

#### Related Content

[### TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities

May 19, 2026 11:39

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed eight vulnerabilities in TP-Link, and one each in Adobe Photoshop, OpenVPN, and Gen Digital's Norton VPN.](/tp-link-photoshop-openvpn-norton-vpn-vulnerabilities/)

[### Foxit, LibRaw vulnerabilities

April 16, 2026 15:00

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one Foxit Reader vulnerability, and six LibRaw file reader vulnerabilities.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage that can detect the](/foxit-libraw-vulnerabilities/)

[### TP-Link, Canva, HikVision vulnerabilities

March 26, 2026 14:34

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed a vulnerability in HikVision, as well as 10 in TP-Link, and 19 in Canva.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage](/tp-link-canva-hikvision-vulnerabilities/)

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