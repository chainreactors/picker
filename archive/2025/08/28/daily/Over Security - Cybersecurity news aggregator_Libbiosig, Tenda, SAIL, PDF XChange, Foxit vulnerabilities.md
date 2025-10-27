---
title: Libbiosig, Tenda, SAIL, PDF XChange, Foxit vulnerabilities
url: https://blog.talosintelligence.com/libbiosig-tenda-sail-pdf-xchange-foxit-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-28
fetch_date: 2025-10-07T00:49:05.471045
---

# Libbiosig, Tenda, SAIL, PDF XChange, Foxit vulnerabilities

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

![](/content/images/2025/08/vuln-roundup.webp)

# Libbiosig, Tenda, SAIL, PDF XChange, Foxit vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, August 27, 2025 14:07

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed ten vulnerabilities in BioSig Libbiosig, nine in Tenda AC6 Router, eight in SAIL, two in PDF-XChange Editor, and one in a Foxit PDF Reader.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Libbiosig vulnerabilities**

*Discovered by Mark Bereza and Lilith >\_> of Cisco Talos.*

BioSig is an open source software library for biomedical signal processing. The aim of the BioSig project is to foster research in biomedical signal processing by providing free and open source software tools for many different application areas. BioSig for C/C++ provides command line tools for data conversion, a library to access a number of data formats (libbiosig), and some experimental code for network transfer of biosignal data.

Talos discovered ten vulnerabilities in libbiosig, affecting both version 3.9.0 of the stable release and the latest commit on the Master Branch at the time of disclosure to the vendor, grouped here by vulnerability type:

Integer overflow:

* [TALOS-2025-2231](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2231) (CVE-2025-53518) exists in the ABF parsing functionality. A specially crafted ABF file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.
* [TALOS-2025-2233](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2233) (CVE-2025-52581) exists in the GDF parsing functionality. A specially crafted GDF file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

Stack-based buffer overflow:

* [TALOS-2025-2234](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2234) (CVE-2025-54480-54494) and [TALOS-2025-2236](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2236) (CVE-2025-46411) exist in the MFER parsing functionality. A specially crafted MFER file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

Heap-based buffer overflow:

* [TALOS-2025-2232](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2232) (CVE-2025-53853) exists in the ISHNE parsing functionality. A specially crafted ISHNE ECG annotations file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.
* [TALOS-2025-2235](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2235) (CVE-2025-53557) and [TALOS-2025-2237](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2237) (CVE-2025-53511) exist in the MFER parsing functionality. A specially crafted MFER file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.
* [TALOS-2025-2239](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2239) (CVE-2025-54462) exists in the Nex parsing functionality. A specially crafted .nex file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.
* [TALOS-2025-2240](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2240) (CVE-2025-48005) exists in the RHS2000 parsing functionality. A specially crafted RHS2000 file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

Out-of-bounds read:

* [TALOS-2025-2238](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2238) (CVE-2025-52461) exists in the Nex parsing functionality. A specially crafted .nex file can lead to an information leak. An attacker can provide a malicious file to trigger this vulnerability.

## **Tenda vulnerabilities**

*Discovered by Lilith >\_> of Cisco Talos.*

The Tenda AC6 is a popular and affordable dual-band gigabit WiFi Router available online, especially on Amazon. All vulnerabilities were found in Tenda AC6 V5.0 V02.03.01.110.

[TALOS-2025-2161](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2161) (CVE-2025-31355) is a firmware update vulnerability in the Firmware Signature Validation functionality of Tenda. A specially crafted malicious file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

Two unencrypted transmission of credentials vulnerabilities were found: [TALOS-2025-2162](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2162) (CVE-2025-27564) exists in the web portal authentication functionality, while [TALOS-2025-2167](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2167) (CVE-2025-31646) is in the Session Authentication Cookie functionality. Specially crafted network packets can lead to arbitrary authentication or authentication bypass, respectively. An attacker can sniff network traffic to trigger these vulnerabilities.

[TALOS-2025-2163](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2163) (CVE-2025-24322) is an unsafe default authentication vulnerability in the Initial Setup Authentication functionality of Tenda. A specially crafted...