---
title: Acrobat out-of-bounds and Foxit use-after-free PDF reader vulnerabilities found
url: https://blog.talosintelligence.com/acrobat-out-of-bounds-and-foxit-use-after-free-pdf-reader-vulnerabilities-found/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-20
fetch_date: 2025-10-06T19:39:54.186790
---

# Acrobat out-of-bounds and Foxit use-after-free PDF reader vulnerabilities found

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

![](/content/images/2024/12/vuln-roundup-1.webp)

# Acrobat out-of-bounds and Foxit use-after-free PDF reader vulnerabilities found

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, December 19, 2024 13:53

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Research team recently disclosed three out-of-bounds read vulnerabilities in Adobe Acrobat Reader, and two use-after-free vulnerabilities in Foxit Reader.

These vulnerabilities exist in Adobe Acrobat Reader and Foxit Reader, two of the most popular and feature-rich PDF readers on the market.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html). Adobe's patched this in version [24.005.20320](https://cisco-talos-blog.ghost.io/ghost/#/editor/post/675c9b70eabd160001b4ebb6), and Foxit's patch appears in PDF Editor version [12.1.9/11.2.12](https://cisco-talos-blog.ghost.io/ghost/#/editor/post/675c9b70eabd160001b4ebb6).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## Out-of-bounds read Adobe Acrobat Reader Vulnerabilities

*Discovered by  KPC.*

Specially crafted font files embedded into a PDF can trigger out-of-bounds memory reads in [TALOS-2024-2076](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2076) (CVE-2024-49534), [TALOS-2024-2070](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2070) (CVE-2024-49533), and [TALOS-2024-2064](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2064) (CVE-2024-49532), which could lead to the disclosure of sensitive information and further exploitation. An attacker must trick the user into opening a malicious file to trigger these vulnerabilities.

## Foxit object use-after-free vulnerabilities

*Discovered by KPC.*

Two use-after-free vulnerabilities exist in the way Foxit Reader handles certain objects. [TALOS-2024-2093](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2093) (CVE-2024-49576) and [TALOS-2024-2094](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2094) (CVE-2024-47810) can be triggered by malicious JavaScript code in a PDF file. An attack needs to either trick a user into opening the malicious file, or the user must navigate to a maliciously crafted website while the Foxit browser extension is enabled. This vulnerability can lead to memory corruption and result in arbitrary code execution.

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
  + [Support Document...