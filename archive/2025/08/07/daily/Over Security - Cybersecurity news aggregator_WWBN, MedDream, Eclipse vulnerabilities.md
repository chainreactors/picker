---
title: WWBN, MedDream, Eclipse vulnerabilities
url: https://blog.talosintelligence.com/wwbn-meddream-eclipse-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-07
fetch_date: 2025-10-07T00:49:27.509442
---

# WWBN, MedDream, Eclipse vulnerabilities

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

![](/content/images/2025/07/vuln-roundup-2.webp)

# WWBN, MedDream, Eclipse vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, August 6, 2025 08:00

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed seven vulnerabilities in WWBN AVideo, four in MedDream, and one in an Eclipse ThreadX module.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **WWBN XSS, race condition, incomplete blacklist vulnerabilities**

*Discovered by Claudio Bozzato of Cisco Talos.*

WWBN AVideo is a video streaming platform with hosting, management, and video monetization features.

Talos found five cross-site scripting (XSS) vulnerabilities in WWBN AVideo 14.4 and dev master commit 8a8954ff:

* [TALOS-2025-2205](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2205) (CVE-2025-46410)
* [TALOS-2025-2206](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2206) (CVE-2025-53084)
* [TALOS-2025-2207](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2207) (CVE-2025-50128)
* [TALOS-2025-2208](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2208) (CVE-2025-36548)
* [TALOS-2025-2209](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2209) (CVE-2025-41420)

A specially crafted HTTP request can lead to arbitrary Javascript execution in all five cases. An attacker must get a user to visit a webpage to trigger these vulnerabilities.

Additionally, Talos identified two vulnerabilities that, when chained together, can lead to arbitrary code execution:

[TALOS-2025-2212](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2212) (CVE-2025-25214) A race condition vulnerability exists in the aVideoEncoder.json.php unzip functionality of WWBN AVideo 14.4 and dev master commit 8a8954ff. A series of specially crafted HTTP requests can lead to arbitrary code execution.

[TALOS-2025-2213](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2213) (CVE-2025-48732) An incomplete blacklist exists in the .htaccess sample of WWBN AVideo 14.4 and dev master commit 8a8954ff. A specially crafted HTTP request can lead to arbitrary code execution. An attacker can request a .phar file to trigger this vulnerability.

## **MedDream**

*Discovered by Emmanuel Tacheau and Marcin Noga of Cisco Talos.*

MedDream PACS Premium is a DICOM 3.0 compliant picture archiving and communication system for the medical industry. The PACS server provides connectivity to all DICOM modalities (CR, DX, CT, MR, US, XA, etc.).

Talos found four unique MedDreams PACS Premium vulnerabilities.

[TALOS-2025-2154](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2154) (CVE-2025-26469) is an incorrect default permissions vulnerability in the CServerSettings::SetRegistryValues functionality of MedDream PACS Premium 7.3.3.840. A specially crafted application can decrypt credentials stored in a configuration-related registry key. An attacker can execute a malicious script or application to exploit this vulnerability.

[TALOS-2025-2156](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2156) (CVE-2025-27724) is a privilege escalation vulnerability in the login.php functionality of meddream MedDream PACS Premium 7.3.3.840. A specially crafted .php file can lead to elevated capabilities. An attacker can upload a malicious file to trigger this vulnerability.

[TALOS-2025-2176](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2176) (CVE-2025-32731) is a reflected XSS vulnerability in the radiationDoseReport.php functionality of meddream MedDream PACS Premium 7.3.5.860. A specially crafted malicious URL can lead to arbitrary JavaScript code execution. An attacker can provide a crafted URL to trigger this vulnerability.

[TALOS-2025-2177](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2177) (CVE-2025-24485) is a server-side request forgery (SSRF) vulnerability in the cecho.php functionality of MedDream PACS Premium 7.3.5.860. A specially crafted HTTP request can lead to SSRF. An attacker can make an unauthenticated HTTP request to trigger this vulnerability.

## **Eclipse ThreadX FileX integer underflow vulnerability**

*Discovered by Kelly Patterson of Cisco Talos.*

Eclipse ThreadX is an embedded development suite for an advanced real-time operating system (RTOS) that provides efficient performance for resource-constrained devices.

[TALOS-2024-2088](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2088) is a buffer overflow vulnerability in the FileX RAM disk driver functionality of Eclipse ThreadX FileX git commit 1b85eb2. A specially crafted set of network packets can lead to code execution. An attacker can send a sequence of requests to trigger this vulnerability.

##### Share this post

#### Related Content

[### Nvidia and Adobe vulnerabilities

October 1, 2025 14:37

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Nvidia and one in Adobe Acrobat.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage that can detect the exploitation](/nvidia-and-adobe-vulnerabilities/)

[##...