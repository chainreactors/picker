---
title: Dell ControlVault, Lasso, GL.iNet vulnerabilities
url: https://blog.talosintelligence.com/dell-controlvault-lasso-gl-inet-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-26
fetch_date: 2025-11-27T03:12:48.868572
---

# Dell ControlVault, Lasso, GL.iNet vulnerabilities

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

![](/content/images/2025/11/vuln-roundup.webp)

# Dell ControlVault, Lasso, GL.iNet vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, November 26, 2025 13:36

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Dell ControlVault 3 firmware and its associated Windows software, four vulnerabilities in Entr'ouvert Lasso, and one vulnerability in GL.iNet Slate AX.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Dell vulnerabilities**

*Discovered by Philippe Laulheret of Cisco Talos.*

The Dell ControlVault is a hardware-based security solution designed for user authentication functions. Talos reported five vulnerabilities, as follows:

* [TALOS-2025-2173](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2173) (CVE-2025-31649) is a hard-coded password vulnerability. A specially crafted ControlVault API call can lead to an execution of privileged operation.
* [TALOS-2025-2174](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2174) (CVE-2025-31361) is a privilege escalation vulnerability. A specially crafted WinBioControlUnit API call can lead to privilege escalation.
* [TALOS-2025-2175](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2175) (CVE-2025-36460-CVE-2025-36463) covers multiple out-of-bounds read and write vulnerabilities. A specially crafted WinBioControlUnit API call can lead to memory corruption.
* [TALOS-2025-2188](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2188) (CVE-2025-32089) is a buffer overflow vulnerability. A specially crafted ControlVault API call can lead to an arbitrary code execution.
* [TALOS-2025-2189](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2189) (CVE-2025-36553) is a buffer overflow vulnerability. A specially crafted ControlVault API call can lead to memory corruption.

## **Entr'ouvert Lasso vulnerabilities**

*Discovered by Keane O'Kelley and another member of Cisco Advanced Security Initiative Group.*

Lasso is a free (GNU General Public License) C library that defines processes for federated identities, single sign-on, and related protocols.

[TALOS-2025-2193](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2193) (CVE-2025-47151) is a type confusion vulnerability, where a specially crafted SAML response can lead to an arbitrary code execution.

[TALOS-2025-2194](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2194) (CVE-2025-46404), [TALOS-2025-2195](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2195) (CVE-2025-46784), and [TALOS-2025-2196](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2196) (CVE-2025-46705) are denial of service vulnerabilities. Specially crafted SAML responses can lead to a denial of service in all three cases.

## **GL.iNet Slate AX vulnerability**

*Discovered by Lilith >\_> of Cisco Talos.*

Slate AX (GL-AXT1800) is a Wi-Fi 6GB travel router. Cisco Talos discovered a firmware downgrade vulnerability, [TALOS-2025-2230](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2230) (CVE-2025-44018), in the OTA Update functionality. A specially crafted .tar file can lead to a firmware downgrade. An attacker can perform a man-in-the-middle attack to trigger this vulnerability.

##### Share this post

#### Related Content

[### TruffleHog, Fade In and BSAFE Crypto-C vulnerabilities

November 4, 2025 09:26

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in Dell BSAFE, two in Fade In screenwriting software, and one in Trufflehog.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort](/trufflehog-fade-in-and-bsafe-crypto-c-vulnerabilities/)

[### Open PLC and Planet vulnerabilities

October 15, 2025 13:39

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one vulnerability in the OpenPLC logic controller and four vulnerabilities in the Planet WGR-500 router.
For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org, and our latest Vulnerability Advisories are always](/open-plc-and-planet-vulnerabilities/)

[### Nvidia and Adobe vulnerabilities

October 1, 2025 14:37

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Nvidia and one in Adobe Acrobat.
The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-party vulnerability disclosure policy.
For Snort coverage that can detect the exploitation](/nvidia-and-adobe-vulnerabilities/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://...