---
title: Foxit, LibRaw vulnerabilities
url: https://blog.talosintelligence.com/foxit-libraw-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-16
fetch_date: 2026-04-17T04:50:43.212603
---

# Foxit, LibRaw vulnerabilities

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/vuln_roundup.jpg)

# Foxit, LibRaw vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, April 16, 2026 15:00

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one Foxit Reader vulnerability, and six LibRaw file reader vulnerabilities.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Foxit use-after-free vulnerability**

*Discovered by KPC of Cisco Talos.*

Foxit Reader allows users to view, edit, and sign PDF documents, among other features. Foxit aims to be one of the most feature-rich PDF readers on the market, and contains many similar functions to that of Adobe Acrobat Reader.

[TALOS-2026-2365](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2365) (CVE-2026-3779) is a use-after-free vulnerability in the way Foxit Reader handles an Array object. A specially crafted JavaScript code inside a malicious PDF document can trigger this vulnerability, which can lead to memory corruption and result in arbitrary code execution. An attacker needs to trick the user into opening the malicious file to trigger this vulnerability.

## **LibRaw heap-based buffer overflow and integer overflow vulnerabilities**

*Discovered by Francesco Benvenuto of Cisco Talos.*

LibRaw is a library and user interface for processing RAW file types and metadata created by digital cameras. Talos analysts found 6 vulnerabilities in LibRaw.

[TALOS-2026-2330](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2330) (CVE-2026-20911), [TALOS-2026-2331](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2331) (CVE-2026-21413), [TALOS-2026-2358](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2358) (CVE-2026-20889), and [TALOS-2026-2359](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2359) (CVE-2026-24660) are heap-based buffer overflow vulnerabilities in LibRaw, and [TALOS-2026-2363](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2363) (CVE-2026-24450) and [TALOS-2026-2364](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2364) (CVE-2026-20884) are integer overflow vulnerabilities. Specially crafted malicious files can lead to heap buffer overflow in all cases. An attacker can provide a malicious file to trigger these vulnerabilities.

##### Share this post

#### Related Content

[### TP-Link, Canva, HikVision vulnerabilities

March 26, 2026 14:34

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed a vulnerability in HikVision, as well as 10 in TP-Link, and 19 in Canva.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage](/tp-link-canva-hikvision-vulnerabilities/)

[### DirectX, OpenFOAM, Libbiosig vulnerabilities

March 11, 2026 16:26

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in the BioSig Project Libbiosig library and OpenCFD OpenFOAM, as well as an unpatched vulnerability in Microsoft DirectX.](/directx-openfoam-libbiosig-vulnerabilities/)

[### Foxit, Epic Games Store, MedDreams vulnerabilities

January 22, 2026 08:54

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Foxit PDF Editor, one in the Epic Games Store, and twenty-one in MedDream PACS.](/foxi-and-epic-games/)

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
  + ...