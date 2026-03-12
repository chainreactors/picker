---
title: DirectX, OpenFOAM, Libbiosig vulnerabilities
url: https://blog.talosintelligence.com/directx-openfoam-libbiosig-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-11
fetch_date: 2026-03-12T04:08:25.417591
---

# DirectX, OpenFOAM, Libbiosig vulnerabilities

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

![](/content/images/2026/03/vuln_roundup.jpg)

# DirectX, OpenFOAM, Libbiosig vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, March 11, 2026 16:26

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in the BioSig Project Libbiosig library and OpenCFD OpenFOAM, as well as an unpatched vulnerability in Microsoft DirectX.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html), apart from the DirectX vulnerability.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## Microsoft DirectX local privilege escalation vulnerability

*Discovered by KPC of Cisco Talos.*

The Microsoft DirectX End-User Runtime installs runtime libraries from the legacy DirectX SDK for some certain games. It comes pre-installed on Windows XP Service Pack 2, Windows Server 2003 Service Pack 1, Windows Vista, Windows 7, Windows 8.0, Windows 8.1, Windows 10, and Windows Server equivalents.

Talos discovered a local privilege escalation vulnerability in the installation process of DirectX End-User Runtime: [TALOS-2025-2293](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2293) (CVE-2025-68623). A low-privileged user can replace an executable file during the installation process, which may result in unintended elevation of privileges.

## **OpenFOAM arbitrary code execution vulnerability**

*Discovered by Dimitrios Tatsis of Cisco Talos.*

OpenFOAM is an open-source computational fluid dynamics (CFD) software developed primarily by OpenCFD Ltd.

Talos discovered [TALOS-2025-2292](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2292) (CVE-2025-61982), an arbitrary code execution vulnerability in the Code Stream directive functionality of OpenCFD OpenFOAM 2506. A specially crafted OpenFOAM simulation file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger this vulnerability.

## **Libbiosig out-of-bounds read, heap-based buffer overflow vulnerabilities**

*Discovered by Mark Bereza of Cisco Talos.*

BioSig is an open source software library for biomedical signal processing. The BioSig Project seeks to encourage research in biomedical signal processing by providing open source software tools. Libbiosig is a library dependency for BioSig.

Talos discovered [TALOS-2025-2323](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2323) (CVE-2025-64736), an out-of-bounds read vulnerability in the ABF parsing functionality of The Biosig Project libbiosig 3.9.2 and Master Branch (5462afb0). A specially crafted .abf file can lead to an information leak. An attacker can provide a malicious file to trigger this vulnerability.

Talos also discovered two heap-based buffer overflow vulnerabilities, [TALOS-2026-2361](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2361) (CVE-2026-22891) and [TALOS-2026-2362](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2362) (CVE-2026-20777), in the Intan CLP parsing and Nicolet WFT parsing functionalities of the BioSig Project, respectively. A specially crafted CLP or WFT file can lead to arbitrary code execution. An attacker can provide a malicious file to trigger these vulnerabilities.

##### Share this post

#### Related Content

[### Foxit, Epic Games Store, MedDreams vulnerabilities

January 22, 2026 08:54

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Foxit PDF Editor, one in the Epic Games Store, and twenty-one in MedDream PACS.](/foxi-and-epic-games/)

[### Libbiosig, Grassroot DiCoM, Smallstep step-ca vulnerabilities

December 17, 2025 16:02

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in Biosig Project Libbiosig, Grassroot DiCoM, and Smallstep step-ca.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy, except for Grassroot, as the DiCoM vulnerabilities](/libbiosig-grassroot-dicom-smallstep-step-ca-vulnerabilities/)

[### Socomec DIRIS Digiware M series and Easy Config, PDF XChange Editor vulnerabilities

December 4, 2025 15:23

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed an out-of-bounds read vulnerability in PDF XChange Editor, and ten vulnerabilities in Socomec DIRIS Digiware M series and Easy Config products.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s](/socomec-diris-digiware-m-series-and-easy-config-pdf-xchange-editor-vulnerabilities/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://talosintelligence.com/incident_response)
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_respo...