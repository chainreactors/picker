---
title: Libbiosig, Grassroot DiCoM, Smallstep step-ca vulnerabilities
url: https://blog.talosintelligence.com/libbiosig-grassroot-dicom-smallstep-step-ca-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-17
fetch_date: 2025-12-18T03:20:42.744712
---

# Libbiosig, Grassroot DiCoM, Smallstep step-ca vulnerabilities

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

![](/content/images/2025/12/vuln-roundup-1.webp)

# Libbiosig, Grassroot DiCoM, Smallstep step-ca vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, December 17, 2025 16:02

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed vulnerabilities in Biosig Project Libbiosig, Grassroot DiCoM, and Smallstep step-ca.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html), except for Grassroot, as the DiCoM vulnerabilities are zero-days.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Libbiosig vulnerability**

*Discovered by Mark Bereza of Cisco Talos.*

BioSig is an open source software library for biomedical signal processing. The BioSig Project seeks to encourage research in biomedical signal processing by providing open source software tools.

[TALOS-2025-2296](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2296) (CVE-2025-66043-CVE-2025-66048) includes several stack-based buffer overflow vulnerabilities in the MFER parsing functionality of the Biosig Project libbiosig 3.9.1. An attacker can supply a specially crafted MFER file to trigger these vulnerabilities, possibly leading to arbitrary code execution.

## **Grassroot DiCoM vulnerabilities**

*Discovered by Emmanuel Tacheau of Cisco Talos.*

Grassroots DiCoM is a C++ library for DICOM medical files, accessible from Python, C#, Java, and PHP. It supports RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax. Talos found three out-of-bounds read vulnerabilities in DiCoM. An attacker can provide a malicious file to trigger these vulnerabilities.

* [TALOS-2025-2210](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2210) (CVE-2025-53618-CVE-2025-53619) can lead to an information leak.
* [TALOS-2025-2211](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2211) (CVE-2025-52582) can lead to an information leak.
* [TALOS-2025-2214](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2214) (CVE-2025-48429) can lead to leaking heap data.

## **Smallstep step-ca vulnerabilities**

*Discovered by Stephen Kubik of the Cisco Advanced Security Initiatives Group (ASIG).*

Smallstep step-ca is a TLS-secured online Certificate Authority (CA) for X.509 and SSH certificate management. [TALOS-2025-2242](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2242) (CVE-2025-44005) is an authentication bypass vulnerability in step-ca. An attacker can bypass authorization checks and force a Step-CA ACME or SCEP provisioner to create certificates without completing certain protocol authorization checks.

##### Share this post

#### Related Content

[### Socomec DIRIS Digiware M series and Easy Config, PDF XChange Editor vulnerabilities

December 4, 2025 15:23

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed an out-of-bounds read vulnerability in PDF XChange Editor, and ten vulnerabilities in Socomec DIRIS Digiware M series and Easy Config products.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s](/socomec-diris-digiware-m-series-and-easy-config-pdf-xchange-editor-vulnerabilities/)

[### Dell ControlVault, Lasso, GL.iNet vulnerabilities

November 26, 2025 13:36

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Dell ControlVault 3 firmware and its associated Windows software, four vulnerabilities in Entr'ouvert Lasso, and one vulnerability in GL.iNet Slate AX.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors,](/dell-controlvault-lasso-gl-inet-vulnerabilities/)

[### TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities

November 4, 2025 09:26

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Dell BSAFE, two in Fade In screenwriting software, and one in Trufflehog.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort](/trufflehog-fade-in-and-bsafe-crypto-c-vulnerabilities/)

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
  + [Talos Intelligence Blog](https://blo...