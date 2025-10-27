---
title: MC LR Router and GoCast unpatched vulnerabilities
url: https://blog.talosintelligence.com/mc-lr-router-and-gocast-zero-day-vulnerabilities-2/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-10
fetch_date: 2025-10-06T19:40:59.011385
---

# MC LR Router and GoCast unpatched vulnerabilities

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

# MC LR Router and GoCast unpatched vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Monday, December 9, 2024 14:30

[Vulnerability Roundup](https://blog.talosintelligence.com/category/vulnerability-roundup/)

Cisco Talos' Vulnerability Research team recently discovered two vulnerabilities in MC Technologies LR Router and three vulnerabilities in the GoCast service.

These vulnerabilities have not been patched at time of this posting.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **MC Technologies OS command injection vulnerabilities**

*Discovered by Matt Wiseman of Cisco Talos.*

The MC-LR Router from MC Technologies supports IPsec and OpenVPN implementations, firewall capabilities, remote management via HTTP and SNMP, and configurable alerting via SMS and email, with two-port and four-port variants, includes models that support transparent serial-to-TCP translations and 1-in/1-out digital I/O.

Talos recently published two advisories detailing OS command injection vulnerabilities discovered in the MC-LR Router from MC Technologies. [TALOS-2024-1953](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1953) covers three vulnerabilities (CVE-2024-28025 through CVE-2024-28027), which are reachable through the I/O configuration functionality of the web interface. [TALOS-2024-1954](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1954) covers one vulnerability (CVE-2024-21786) in the importation of uploaded configuration files. All vulnerabilities may be triggered with an authenticated HTTP request.

## **GoCast authentication and OS command injection vulnerabilities**

*Discovered by Edwin Molenaar and Matt Street of Cisco Meraki.*

The GoCast tool provides BGP routing for advertisements from a host; it is commonly used for anycast-based load balancing for infrastructure service instances available in geographically diverse regions.

The GoCast HTTP API allows the registration and deregistration of apps without requiring authentication, shown in [TALOS-2024-1962](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1962) (CVE-2024-21855). The lack of authentication can be used to exploit [TALOS-2024-1960](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1960) (CVE-2024-28892) and [TALOS-2024-1961](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1961) (CVE-2024-29224), leading to OS command injection and arbitrary command execution.

##### Share this post

#### Related Content

[### Nvidia and Adobe vulnerabilities

October 1, 2025 14:37

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Nvidia and one in Adobe Acrobat.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage that can detect the exploitation](/nvidia-and-adobe-vulnerabilities/)

[### Libbiosig, Tenda, SAIL, PDF XChange, Foxit vulnerabilities

August 27, 2025 14:07

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed ten vulnerabilities in BioSig Libbiosig, nine in Tenda AC6 Router, eight in SAIL, two in PDF-XChange Editor, and one in a Foxit PDF Reader.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence](/libbiosig-tenda-sail-pdf-xchange-foxit-vulnerabilities/)

[### WWBN, MedDream, Eclipse vulnerabilities

August 6, 2025 08:00

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed seven vulnerabilities in WWBN AVideo, four in MedDream, and one in an Eclipse ThreadX module.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort](/wwbn-meddream-eclipse-vulnerabilities/)

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
  + [About Talos](https://talosin...