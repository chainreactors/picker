---
title: Microsoft, Adobe, Apple, and Foxit vulnerabilities
url: https://blog.talosintelligence.com/microsoft-adobe-apple-and-foxit-vulnerabilities/
source: Over Security
date: 2026-10-07
fetch_date: 2026-10-08T08:08:10.662745
---

# Microsoft, Adobe, Apple, and Foxit vulnerabilities

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

# Microsoft, Adobe, Apple, and Foxit vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, October 7, 2026 15:27

[Vulnerability Roundup](https://blog.talosintelligence.com/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in Adobe, Apple, Foxit Reader, and Microsoft.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

### Adobe Photoshop privilege escalation vulnerability

[TALOS-2026-2360](https://www.talosintelligence.com/vulnerability_reports/TALOS-2026-2360) (CVE-2026-48388) is a privilege escalation vulnerability in the Installation functionality of Photoshop (version(s): Photoshop\_Set-Up.exe version 2.11.0.30). An attacker can replace files with a specially crafted malformed file to trigger this vulnerability and lead to privilege escalation.

### Apple macOS CoreWLAN information disclosure vulnerability

[TALOS-2026-2376](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2376) is an information disclosure vulnerability in the CoreWLAN functionality of macOS (version(s): 26.3.1(25D2128)). An attacker can call a sequence of APIs to trigger this vulnerability.

### Foxit Reader code execution and use-after-free vulnerabilities

[TALOS-2026-2420](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2420) (CVE-2026-57256) is a code execution vulnerability in the Javascript checkbox CBF\_Widget functionality of Foxit Reader (version(s): 2026.1.1.36485). A specially crafted malformed file provided by an attacker can lead to remote code execution.

[TALOS-2026-2446](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2446) (CVE-2026-91799) is a use-after-free vulnerability in the way Foxit Reader handles an Array object. A specially crafted JavaScript code inside a malicious PDF document can trigger this vulnerability, which can lead to memory corruption and result in arbitrary code execution.

### Microsoft Windows out-of-bounds, use-after-free, and type confusion vulnerabilities

[TALOS-2026-2443](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2443) (CVE-2026-50475) is an out-of-bounds pointer offset vulnerability in the Microsoft Windows NETIO.sys driver. A specially crafted I/O request packet (IRP) can cause disclosure of sensitive information.

[TALOS-2026-2426](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2426) (CVE-2026-58613) is a use-after-free vulnerability in Windows Cloud Files Mini Filter Driver (version(s): 10.0.26100.8457 (WinBuild.160101.0800)). A specially crafted sequence of Cloud Filter API calls, executed with a dedicated application, can lead to privilege escalation.

[TALOS-2026-2445](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2445) (CVE-2026-80093) is a type confusion vulnerability in Windows Cloud Files Mini Filter Driver (version(s): 10.0.26100.8457 (WinBuild.160101.0800) and 10.0.26100.8655 (WinBuild.160101.0800)). A specially crafted sequence of Cloud Filter API calls can lead to type confusion. An attacker can execute a dedicated application to trigger this vulnerability.

[TALOS-2026-2427](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2427) (CVE-2026-49177) is an out-of-bounds read vulnerability in Microsoft Windows tcpip.sys driver. A specially crafted I/O request packet (IRP) can cause an arbitrary out-of-bounds read, potentially leading to information disclosure or a denial-of-service condition.

##### Share this post

#### Related Content

[### WolfSSL, GeoVision, VTK vulnerabilities

July 9, 2026 14:52

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in WolfSSF, fourteen in GeoVision, and one vulnerability in VTK-DICOM.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage that](/wolfssl-vulnerabilities/)

[### MediaArea heap-based buffer overflow vulnerabilities

May 27, 2026 10:00

Talos researchers find 4 heap-based buffer overflow vulnerabilities in MediaArea's MediaInfoLib.](/mediaarea-heap-based-buffer-overflow-vulnerabilities/)

[### TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities

May 19, 2026 11:39

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed eight vulnerabilities in TP-Link, and one each in Adobe Photoshop, OpenVPN, and Gen Digital's Norton VPN.](/tp-link-photoshop-openvpn-norton-vpn-vulnerabilities/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://talosintelligence.com/incident_response)
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligen...