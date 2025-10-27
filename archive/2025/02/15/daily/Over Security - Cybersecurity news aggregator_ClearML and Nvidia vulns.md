---
title: ClearML and Nvidia vulns
url: https://blog.talosintelligence.com/clearml-and-nvidia-vulns/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-15
fetch_date: 2025-10-06T20:38:07.585644
---

# ClearML and Nvidia vulns

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

![](/content/images/2025/02/vuln-roundup.webp)

# ClearML and Nvidia vulns

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Friday, February 14, 2025 11:55

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed two vulnerabilities in ClearML and four vulnerabilities in Nvidia.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## ClearML XSS and information disclosure vulnerabilities

*Discovered by Edwin Molenaar of Cisco Meraki.*

ClearML contains two vulnerabilities. ClearML is an open-source AI platform that supports the entire AI development lifecycle from research to production. It is designed to integrate with existing tools and infrastructures, allowing developers and DevOps teams to build, train and deploy models at scale.

[TALOS-2024-2110](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2110) (CVE-2024-39272) is a cross-site scripting vulnerability. A specially crafted HTTP request can allow an attacker to upload HTML files to a dataset through an existing ClearML account. The files can later be rendered within the browser of an authenticated ClearML user and execute JavaScript.

[TALOS-2024-2112](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2112) (CVE-2024-43779) is an information disclosure vulnerability. A specially crafted HTTP request can lead to an attacker reading vaults that have been previously disabled, possibly leaking sensitive credentials. An attacker can send a series of HTTP requests to trigger this vulnerability.

## Nvidia memory corruption and heap-based buffer overflow vulnerabilities

*Discovered by Dimitrios Tatsis.*

The nvJPEG2000 library is provided by NVIDIA as a high-performance JPEG2000 encoding and decoding library. The prerequisite is a CUDA enabled GPU in the system that allows faster processing than traditional CPU implementations.

[TALOS-2024-2080](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2080) (CVE-2024-0142) and  [TALOS-2024-2095](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2095) (CVE-2024-0143) are memory corruption vulnerabilities. A specially crafted JPEG2000 file can lead to an out-of-bounds write with arbitrary data which can lead to further memory corruption and arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

[TALOS-2024-2108](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2108) (CVE-2024-0144) and [TALOS-2024-2113](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2113) (CVE-2024-0145) are heap-based buffer overflow vulnerabilities in the Ndecomp field handling and parameter. A specially crafted JPEG2000 file can lead to memory corruption and arbitrary code execution. An attacker can provide a malicious file to trigger these vulnerabilities.

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
  + [S...