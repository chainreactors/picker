---
title: Eclipse and STMicroelectronics vulnerabilities
url: https://blog.talosintelligence.com/eclipse-and-stmicroelectronics-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-17
fetch_date: 2025-10-06T22:08:11.309546
---

# Eclipse and STMicroelectronics vulnerabilities

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

![](/content/images/2025/03/vuln-roundup-1.webp)

# Eclipse and STMicroelectronics vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, April 16, 2025 08:00

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities found in Eclipse ThreadX and four vulnerabilities in the STMicroelectronics fork of ThreadX called X-CUBE-AZRTOS.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## Eclipse vulnerabilities

*Discovered by Kelly Patterson of Cisco Talos.*

Eclipse ThreadX is an embedded development suite including an operating system that provides performance for resource-constrained devices.

[TALOS-2024-2098](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2098) (CVE-2025-0726, CVE-2025-2260) A denial of service vulnerability exists in the NetX HTTP server functionality of Eclipse ThreadX NetX Duo git commit 6c8e9d1. A specially crafted network packet can lead to denial of service. An attacker can send a malicious packet to trigger this vulnerability.

Two integer underflow vulnerabilities exist in the HTTP server PUT request functionality of Eclipse ThreadX NetX Duo git commit 6c8e9d1, [TALOS-2024-2104](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2104) (CVE-2025-0727, CVE-2025-2259) and [TALOS-2024-2105](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2105) (CVE-2025-0728, CVE-2025-2258). Specially crafted network request packets can lead to denial of service. An attacker can send malicious packets to trigger these vulnerabilities.

## STMicroelectronics vulnerabilities

*Discovered by Kelly Patterson of Cisco Talos.*

STMicroelectronics is a European multinational semiconductor contract manufacturing and design company. They maintain a separate fork of ThreadX called X-CUBE-AZRTOS, used in their IDE for easy integration with STMicroelectronics hardware.

[TALOS-2024-2096](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2096) (CVE-2024-45064) is a buffer overflow vulnerability in the FileX Internal RAM interface functionality of STMicroelectronics X-CUBE-AZRTOS-WL 2.0.0. A specially crafted set of network packets can lead to code execution. An attacker can send a sequence of requests to trigger this vulnerability.

[TALOS-2024-2097](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2097) (CVE-2024-50384-CVE-2024-50385) is a denial-of-service vulnerability in the NetX Component HTTP server functionality. A specially crafted network packet can lead to denial of service. An attacker can send a malicious packet to trigger this vulnerability.

Two integer underflow vulnerabilities exist in the HTTP server PUT request functionality. For [TALOS-2024-2102](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2102) (CVE-2024-50594-CVE-2024-50595), a specially crafted series of network requests can lead to denial of service. An attacker can send a sequence of malicious packets to trigger this vulnerability. For [TALOS-2024-2103](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2103) (CVE-2024-50596-CVE-2024-50597), a specially crafted network packet can lead to denial of service. An attacker can send a malicious packet to trigger this vulnerability.

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
  + [Reactive Services](https:/...