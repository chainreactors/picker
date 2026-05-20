---
title: TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities
url: https://blog.talosintelligence.com/tp-link-photoshop-openvpn-norton-vpn-vulnerabilities/
source: Over Security
date: 2026-05-19
fetch_date: 2026-05-20T06:05:02.354969
---

# TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/05/vuln_roundup.jpg)

# TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Tuesday, May 19, 2026 11:39

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed eight vulnerabilities in TP-Link, and one each in Adobe Photoshop, OpenVPN, and Gen Digital's Norton VPN.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html), except the Norton VPN vulnerability, which was discovered in-use before a patch was available.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **TP-Link vulnerabilities**

*Discovered by Lilith >\_> of Cisco Talos.*

The TP-Link Archer AX53 is a dual band gigabit Wi-Fi router. Talos has disclosed eight vulnerabilities, as follows:

[TALOS-2025-2302](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2302) (CVE-2026-30814) is a stack-based buffer overflow vulnerability in the tmpServer opcode 0x436 functionality of Tp-Link AX53 v1.0 1.3.1 Build 20241120 rel.54901(5553). A specially crafted set of network packets can lead to arbitrary code execution. An attacker can send packets to trigger this vulnerability.

[TALOS-2025-2303](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2303) (CVE-2026-30815) is an OS command injection vulnerability in the OpenVPN configuration restore script\_security functionality of Tp-Link Archer AX53 v1.0 1.3.1 Build 20241120 rel.54901(5553). A specially crafted configuration value can lead to arbitrary command execution. An attacker can upload a malicious file to trigger this vulnerability.

[TALOS-2025-2304](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2304) (CVE-2026-30816) is an external config control vulnerability in the OpenVPN configuration restore crt.sed functionality of Tp-Link Archer AX53 v1.0 1.3.1 Build 20241120 rel.54901(5553). A specially crafted configuration value can lead to arbitrary file reading. An attacker can upload a malicious file to trigger this vulnerability.

[TALOS-2025-2305](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2305) (CVE-2026-30817) is an external config control vulnerability in the OpenVPN configuration restore route\_up functionality of Tp-Link Archer AX53 v1.0 1.3.1 Build 20241120 rel.54901(5553). A specially crafted configuration value can lead to arbitrary file reading. An attacker can upload a malicious file to trigger this vulnerability.

[TALOS-2025-2306](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2306) (CVE-2026-30818) is an OS command injection vulnerability exists in the dnsmasq configuration restore dhcpscript functionality of Tp-Link Archer AX53 v1.0 1.3.1 Build 20241120 rel.54901(5553). A specially crafted configuration value can lead to arbitrary command execution. An attacker can upload a malicious file to trigger this vulnerability.

[TALOS-2025-2307](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2307), [TALOS-2025-2308](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2308), and [TALOS-2025-2309](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2309) are OS command injection vulnerabilities in the OpenVPN configuration restore client\_disconnect, client\_connect, and route\_up functionalities of Tp-Link Archer AX53 v1.0 1.3.1 Build 20241120 rel.54901(5553). A specially crafted configuration value can lead to arbitrary command execution. An attacker can upload a malicious file to trigger this vulnerability.

## **Photoshop vulnerabilities**

*Discovered by KPC of Cisco Talos.*

Adobe Photoshop is a popular digital photo manipulation and illustration program with a wide array of features for personal and business use cases.

[TALOS-2025-2274](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2274) (CVE-2026-34632) is a privilege escalation vulnerability in the installation process of Adobe Photoshop via the Microsoft Store. The vulnerable version of the installer is Photoshop\_Set-Up.exe 2.11.0.30. A low-privilege user can replace files during the installation process, which may result in elevation of privileges.

## **OpenVPN vulnerabilities**

*Discovered by Emma Reuter of Cisco ASIG.*

OpenVPN is an open source SSL VPN with remote access, site-to-site VPNs, WiFi security, enterprise load balancing, failover, and granular access control features available.

[TALOS-2026-2381](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2381) (CVE-2026-35058) is a reachable assertion vulnerability in the TLS Crypt v2 Client Key Extraction functionality of OpenVPN 2.6.x and 2.8\_git. A specially crafted network packet can lead to a denial of service. An attacker can send a sequence of malicious packets to trigger this vulnerability.

## **Gen Digital Norton VPN vulnerabilities**

*Discovered by KPC of Cisco Talos.*

Gen Digital's Norton VPN client is a proprietary tool for private proxy network information exchange.

[TALOS-2025-2276](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2276) (CVE-2025-58074) is a privilege escalation vulnerability in the installation process of Norton VPN via the Microsoft Store. A low-privilege user can replace files during the installation process, which may result in deletion of arbit...