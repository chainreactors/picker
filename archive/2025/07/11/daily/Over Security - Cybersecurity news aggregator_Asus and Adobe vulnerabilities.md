---
title: Asus and Adobe vulnerabilities
url: https://blog.talosintelligence.com/asus-and-adobe-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-11
fetch_date: 2025-10-06T23:49:35.920366
---

# Asus and Adobe vulnerabilities

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

![](/content/images/2025/07/vuln-roundup.webp)

# Asus and Adobe vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, July 10, 2025 11:24

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed two vulnerabilities each in Asus Armoury Crate and Adobe Acrobat products.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## Asus Armoury Crate stack-based buffer overflow and authorization bypass  vulnerabilities

*Discovered by Marcin "Icewall" Noga of Cisco Talos.*

These vulnerabilities were recently covered in a deep-dive post, [Decrement by one to rule them all](https://blog.talosintelligence.com/decrement-by-one-to-rule-them-all/).

Asus Armoury Crate is a software utility used to manage Asus and ROG lighting, performance, and updates.

[TALOS-2025-2144](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2144) (CVE-2025-1533) is a stack-based buffer overflow vulnerability in the AsIO3.sys kernel driver of Asus Armoury Crate 5.9.13.0. A specially crafted I/O request packet (IRP) can lead to stack-based buffer overflow. An unprivileged attacker can run a program from user mode to trigger this vulnerability.

[TALOS-2025-2150](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2150) (CVE-2025-3464) is an authorization bypass vulnerability in the AsIO3.sys functionality of Asus Armoury Crate 5.9.13.0. A specially crafted hard link can lead to an authorization bypass. An attacker can create a hard link to trigger this vulnerability.

## Adobe Acrobat Reader out-of-bounds read and use-after-free vulnerabilities

*Discovered by KPC of Cisco Talos.*

Adobe Acrobat Reader is one of the most popular PDF reading software currently available. Talos found an out-of-bounds read vuln, [TALOS-2025-2159](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2159) (CVE-2025-43578), in the Font functionality of Adobe Acrobat Reader 2025.001.20435. A specially crafted font file embedded into a PDF can trigger this vulnerability which can lead to disclosure of sensitive information.

[TALOS-2025-2170](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2170) (CVE-2025-43576) is a use-after-free vulnerability in the annotation object processing functionality of Adobe Acrobat Reader 2025.001.20435. A specially crafted Javascript code inside a malicious PDF document can trigger reuse of a previously freed object, which can lead to memory corruption and could result in arbitrary code execution.

An attacker needs to trick the user into opening the malicious file to trigger either of these vulnerabilities.

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
  + [Threat Source Newsletter](ht...