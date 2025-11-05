---
title: TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities
url: https://blog.talosintelligence.com/trufflehog-fade-in-and-bsafe-crypto-c-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-04
fetch_date: 2025-11-05T03:12:20.583974
---

# TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities

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

![](/content/images/2025/10/vuln-roundup-1.webp)

# TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Tuesday, November 4, 2025 09:26

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Dell BSAFE, two in Fade In screenwriting software, and one in Trufflehog.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Fade In out-of-bounds write vulnerabilities**

*Discovered by Piotr Bania of Cisco Talos.*

Fade In is a cross-platform text handling software for screenwriters.

[TALOS-2025-2250](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2250) (CVE-2025-53855) is an out-of-bounds write vulnerability in the XML parser functionality of GCC Productions Inc. Fade In 4.2.0. A specially crafted .fadein file can lead to an out-of-bounds write.

[TALOS-2025-2252](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2252) (CVE-2025-53814) is a use-after-free vulnerability in the XML parser functionality of GCC Productions Inc. Fade In 4.2.0. A specially crafted .xml file can lead to heap-based memory corruption.

## **TruffleHog arbitrary code execution vulnerability**

*Discovered by Adam Reiser of Cisco ASIG.*

TruffleHog is a detection system for code repositories and ticket systems that finds exposed sensitive information, such as API keys and passwords. This vulnerability is described in an [accompanying article](https://trufflesecurity.com/blog/contributor-spotlight-adam-reiser-of-cisco-talos) on the Truffle Security website. The vuln is an arbitrary code execution vulnerability in the Git functionality of TruffleHog 3.90.2, [TALOS-2025-2243](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2243) (CVE-2025-41390). A specially crafted repository can lead to a arbitrary code execution. An attacker can provide a malicious repository to trigger this vulnerability.

## **Dell BSAFE integer overflow, underflow, and stack overflow vulnerabilities**

*Discovered by Jason Crowder.*

Dell BSAFE Crypto-C is FIPS-140 validated cryptography development kit for C/C++ environments. In cooperation with Jason Crowder, Talos published three vulnerabilities in the Dell BSAFE Crypto-C module. This product is at end of service; the vulnerable versions were added to an existing CVE.

[TALOS-2025-2140](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2140) (CVE-2019-3728) is an integer overflow vulnerability, and [TALOS-2025-2141](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2141) (CVE-2019-3728) is an integer underflow vulnerability. In both cases, a specially crafted ASN.1 record can lead to an out-of-bounds read. An attacker can provide a malformed ASN.1 record to trigger this vulnerability.

[TALOS-2025-2142](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2142) (CVE-2019-3728) is a stack overflow vulnerability. A specially crafted ASN.1 record can lead to denial of service.

##### Share this post

#### Related Content

[### Open PLC and Planet vulnerabilities

October 15, 2025 13:39

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one vulnerability in the OpenPLC logic controller and four vulnerabilities in the Planet WGR-500 router.
For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org, and our latest Vulnerability Advisories are always](/open-plc-and-planet-vulnerabilities/)

[### Nvidia and Adobe vulnerabilities

October 1, 2025 14:37

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Nvidia and one in Adobe Acrobat.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage that can detect the exploitation](/nvidia-and-adobe-vulnerabilities/)

[### Libbiosig, Tenda, SAIL, PDF XChange, Foxit vulnerabilities

August 27, 2025 14:07

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed ten vulnerabilities in BioSig Libbiosig, nine in Tenda AC6 Router, eight in SAIL, two in PDF-XChange Editor, and one in a Foxit PDF Reader.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence](/libbiosig-tenda-sail-pdf-xchange-foxit-vulnerabilities/)

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
* + ###### Securit...