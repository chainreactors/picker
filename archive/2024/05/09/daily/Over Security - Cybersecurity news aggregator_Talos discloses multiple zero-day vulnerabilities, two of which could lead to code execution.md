---
title: Talos discloses multiple zero-day vulnerabilities, two of which could lead to code execution
url: https://blog.talosintelligence.com/vulnerability-roundup-zero-days-may-8-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-09
fetch_date: 2025-10-06T17:18:32.004940
---

# Talos discloses multiple zero-day vulnerabilities, two of which could lead to code execution

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

![](/content/images/2024/05/vuln-roundup-1.png)

# Talos discloses multiple zero-day vulnerabilities, two of which could lead to code execution

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Wednesday, May 8, 2024 12:00

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Research team recently disclosed three zero-day vulnerabilities that are still unpatched as of Wednesday, May 8.

Two vulnerabilities in this group — one in the Tinyroxy HTTP proxy daemon and another in the stb\_vorbis.c file library — could lead to arbitrary code execution, earning both issues a CVSS score of 9.8 out of 10. While we were unable to reach the maintainers, the Tinyroxy maintainers have since [patched](http://patched/) the issue.

Another zero-day exists in the Milesight UR32L wireless router.

These vulnerabilities have all been disclosed in adherence to [Cisco’s third-party vulnerability disclosure timeline](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html#:~:text=If%20a%20vulnerability%20is%20found,PGP%20keys%20for%20encrypted%20email.) after the associated vendors did not meet the 90-day deadline for a patch or communication.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

# Use-after-free vulnerability in Tinyproxy daemon

*Discovered by Dimitrios Tatsis.*

The Tinyproxy HTTP proxy daemon contains a vulnerability that could lead to arbitrary code execution.

Tinyproxy is meant to be used in smaller networking environments. It was originally released more than a dozen years ago.

A use-after-free vulnerability, [TALOS-2023-1889](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1889) (CVE-2023-49606), exists in the `Connection` header provided by the client. An adversary could make an unauthenticated HTTP request to trigger this vulnerability, setting off the reuse of previously freed memory, which leads to memory corruption and could lead to remote code execution. This issue has been [patched](http://patched/), though Talos initially released it as a zero-day when no patch was available.

# Milesight UR32L firmware update vulnerability

*Discovered by Francesco Benvenuto.*

The Milesight UR32L wireless router contains a vulnerability that could force the device to implement any firmware update, regardless of its legitimacy.

[TALOS-2023-1852](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1852) (CVE-2023-47166) exists because the UR32L, an industrial cellular router, never checks the validity of the uploaded firmware. This could allow an adversary to upgrade the router with arbitrary firmware they created.

Talos has previously covered how an adversary could chain together [several other vulnerabilities in the UR32L](https://blog.talosintelligence.com/talos-discovers-17-vulnerabilities-in-milesight/) to completely take over the device. Talos released 22 security advisories in July 2023, nine of which have a CVSS score greater than 8.

# Buffer overflow vulnerability in open-source single-header file library could lead to arbitrary code execution

*Discovered by Emmanuel Tacheau.*

A heap-based buffer overflow vulnerability exists in the comment functionality of stb \_vorbis.c, an open-source, single-header file library used to decode Ogg Vorbis non-proprietary audio files. Ogg Vorbis is an open-source, patent- and royalty-free, general-purpose compressed audio format.

[TALOS-2023-1846](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1846) (CVE-2023-47212) is triggered if an adversary sends the target a specially crafted .ogg file, which can lead to an out-of-bounds write. With enough heap grooming, an adversary could use this vulnerability to achieve arbitrary code execution.

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
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_repo...