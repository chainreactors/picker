---
title: Bloomberg Comdb2 null pointer dereference and denial-of-service vulnerabilities
url: https://blog.talosintelligence.com/bloomberg-comdb2-null-pointer-dereference-and-denial-of-service-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-25
fetch_date: 2025-10-06T23:50:47.581071
---

# Bloomberg Comdb2 null pointer dereference and denial-of-service vulnerabilities

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

![](/content/images/2025/07/vuln-roundup-1.webp)

# Bloomberg Comdb2 null pointer dereference and denial-of-service vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, July 24, 2025 10:03

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Bloomberg Comdb2.

Comdb2 is an open source, high-availability database developed by Bloomberg. It supports features such as clustering, transactions, snapshots, and isolation. The implementation of the database utilizes optimistic locking for concurrent operation.

The vulnerabilities mentioned in this blog post have been patched by the vendor, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## Comdb2 vulnerabilities

*Discovered by a member of Cisco Talos.*

Three null pointer dereference vulnerabilities exist in Bloomberg Comdb2 8.1. Two vulnerabilities ([TALOS-2025-2197](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2197) (CVE-2025-36520) and [TALOS-2025-2201](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2201) (CVE-2025-35966)) are in protocol buffer message handling, which can lead to denial of service. An attacker can simply connect to a database instance over TCP and send the crafted message to trigger this vulnerability. [TALOS-2025-2199](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2199) (CVE-2025-48498) is in the distributed transaction component. A specially crafted network packet can lead to a denial of service. An attacker can send packets to trigger this vulnerability.

There are also two denial-of-service vulnerabilities:

* [TALOS-2025-2198](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2198) (CVE-2025-46354) exists in the Distributed Transaction Commit/Abort Operation of Bloomberg Comdb2 8.1. A specially crafted network packet can lead to a denial of service. An attacker can send a malicious packet to trigger this vulnerability.
* [TALOS-2025-2200](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2200) (CVE-2025-36512) exists in the Bloomberg Comdb2 8.1 database when handling a distributed transaction heartbeat. A specially crafted protocol buffer message can lead to a denial of service. An attacker can simply connect to a database instance over TCP and send the crafted message to trigger this vulnerability.

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
...