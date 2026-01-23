---
title: Foxit, Epic Games Store, MedDreams vulnerabilities
url: https://blog.talosintelligence.com/foxi-and-epic-games/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-22
fetch_date: 2026-01-23T03:33:11.138560
---

# Foxit, Epic Games Store, MedDreams vulnerabilities

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

# Foxit, Epic Games Store, MedDreams vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, January 22, 2026 08:54

[Vulnerability Roundup](https://blog.talosintelligence.com/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Foxit PDF Editor, one in the Epic Games Store, and twenty-one in MedDream PACS..

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Foxit privilege escalation and use-after-free vulnerabilities**

*Discovered by KPC of Cisco Talos.*

Foxit PDF Editor is a popular PDF handling platform for editing, e-signing, and collaborating on PDF documents. Talos found three vulnerabilities:

[TALOS-2025-2275](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2275) (CVE-2025-57779) is a privilege escalation vulnerability in the installation of Foxit PDF Editor via the Microsoft Store. A low-privilege user can replace files during the installation process, which may result in elevation of privileges.

[TALOS-2025-2277](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2277) (CVE-2025-58085) and [TALOS-2025-2278](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2278) (CVE-2025-59488)  are use-after-free vulnerabilities, one in the way Foxit Reader handles a Barcode field object, and one in the way Foxit Reader handles a Text Widget field object. A specially crafted JavaScript code inside a malicious PDF document can trigger these vulnerabilities, which can lead to memory corruption and result in arbitrary code execution. An attacker needs to trick the user into opening the malicious file to trigger these vulnerabilities. Exploitation is also possible if a user visits a specially crafted, malicious site if the browser plugin extension is enabled.

## **Epic Games local privilege escalation vulnerability**

*Discovered by KPC of Cisco Talos.*

Epic Games Store is a storefront application for purchasing and accessing video games. Talos found [TALOS-2025-2279](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2279) (CVE-2025-61973), a local privilege escalation vulnerability in the installation of Epic Games Store via the Microsoft Store. A low-privilege user can replace a DLL file during the installation process, which may result in elevation of privileges.

## **MedDream PACS reflected cross-site scripting vulnerabilities**

*Discovered by Marcin “Icewall” Noga of Cisco Talos.*

MedDream PACS server is a medical-integration system for archiving and communicating about DICOM 3.0 compliant images. Talos found 21 reflected cross-site scripting (XSS) vulnerabilities across several functions of MedDream PACS Premium 7.3.6.870. An attacker can provide a specially crafted URL to trigger these vulnerabilities, which can lead to arbitrary JavaScript code execution.

* [TALOS-2025-2253](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2253) (CVE-2025-54817): autoPurge functionality
* [TALOS-2025-2254](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2254) (CVE-2025-53516): downloadZip functionality
* [TALOS-2025-2255](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2255) (CVE-2025-54495): emailfailedjob functionality
* [TALOS-2025-2256](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2256) (CVE-2025-54157): encapsulatedDoc functionality
* [TALOS-2025-2257](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2257) (CVE-2025-54778): existingUser functionality
* [TALOS-2025-2258](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2258) (CVE-2025-46270): fetchPriorStudies functionality
* [TALOS-2025-2259](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2259) (CVE-2025-55071): modifyAnonymize functionality
* [TALOS-2025-2260](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2260) (CVE-2025-54852): modifyAeTitle functionality
* [TALOS-2025-2261](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2261) (CVE-2025-54814): modifyAutopurgeFilter functionality
* [TALOS-2025-2262](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2262) (CVE-2025-54861): modifyCoercion functionality
* [TALOS-2025-2263](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2263) (CVE-2025-57881): modifyEmail functionality
* [TALOS-2025-2264](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2264) (CVE-2025-58080): modifyHL7App functionality
* [TALOS-2025-2265](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2265) (CVE-2025-53854): modifyHL7Route functionality
* [TALOS-2025-2266](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2266) (CVE-2025-57787): modifyRoute functionality
* [TALOS-2025-2267](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2267) (CVE-2025-53707): modifyTranscript functionality
* [TALOS-2025-2268](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2268) (CVE-2025-54853): modifyUser functionality
* [TALOS-2025-2269](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2269) (CVE-2025-57786): notifynewstudy functionality
* [TALOS-2025-2270](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2270) (CVE-2025-44000): sendOruReport functionality
* [TALOS-2025-2271](https...