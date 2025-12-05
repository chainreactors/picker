---
title: Socomec DIRIS Digiware M series and Easy Config, PDF XChange Editor vulnerabilities
url: https://blog.talosintelligence.com/socomec-diris-digiware-m-series-and-easy-config-pdf-xchange-editor-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-04
fetch_date: 2025-12-05T03:18:41.311570
---

# Socomec DIRIS Digiware M series and Easy Config, PDF XChange Editor vulnerabilities

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

![](/content/images/2025/12/vuln-roundup.webp)

# Socomec DIRIS Digiware M series and Easy Config, PDF XChange Editor vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, December 4, 2025 15:23

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed an out-of-bounds read vulnerability in PDF XChange Editor, and ten vulnerabilities in Socomec DIRIS Digiware M series and Easy Config products.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **PDF XChange vulnerabilities**

*Discovered by KPC of Cisco Talos.*

PDF XChange Editor is freemium software used to create, edit, digitally sign, and otherwise handle PDF files. Talos discovered [TALOS-2025-2280](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2280) (CVE-2025-58113), an out-of-bounds read vulnerability in the EMF functionality of PDF-XChange Co. Ltd PDF-XChange Editor 10.7.3.401. By using a specially crafted EMF file, an attacker could exploit this vulnerability to perform an out-of-bounds read, potentially leading to the disclosure of sensitive information.

## **Socomec vulnerabilities**

*Discovered by Kelly Patterson of Cisco Talos.*

Talos discovered nine vulnerabilities in the Socomec DIRIS Digiware M-70 version 1.6.9. DIRIS Digiware M series are multifunction communication gateways that act as a point of access to Digiware systems, combining power supply and communication control monitoring.

One disclosed vulnerability is also in the Socomec Easy Config System. This software is used to configure and monitor Socomec power monitoring and control equipment.

### Socomec DIRIS Digiware M Series

[TALOS-2024-2115](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2115) (CVE-2024-48894) is a cleartext transmission vulnerability. Specially crafted HTTP requests can lead to a disclosure of sensitive information. An attacker can sniff network traffic to trigger this vulnerability.

[TALOS-2024-2116](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2116) (CVE-2024-53684) is a cross-site request forgery. A specially crafted HTTP request can lead to unauthorized access. An attacker can stage a malicious webpage to trigger this vulnerability.

[TALOS-2024-2118](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2118) (CVE-2024-49572) is a denial-of-service vulnerability. A specially crafted network packet can lead to denial of service and weaken credentials, resulting in default documented credentials being applied to the device. An attacker can send an unauthenticated packet to trigger this vulnerability.

[TALOS-2024-2119](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2119) (CVE-2024-48882) is a denial-of-service vulnerability. A specially crafted network packet can lead to denial of service. An attacker can send an unauthenticated packet to trigger this vulnerability.

[TALOS-2025-2138](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2138) (CVE-2025-20085) is a denial-of-service vulnerability. A specially crafted network packet can lead to denial of service and weaken credentials, resulting in default documented credentials being applied to the device. An attacker can send an unauthenticated packet to trigger this vulnerability.

[TALOS-2025-2139](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2139) (CVE-2025-23417) is a denial-of-service vulnerability. A specially crafted network packet can lead to denial of service. An attacker can send an unauthenticated packet to trigger this vulnerability.

[TALOS-2025-2248](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2248) (CVE-2025-54848-CVE-2025-54851) is a denial-of-service vulnerability in the Modbus TCP and Modbus RTU over TCP functionalities. A specially crafted series of network requests can lead to a denial of service. An attacker can send a sequence of unauthenticated packets to trigger this vulnerability.

[TALOS-2025-2251](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2251) (CVE-2025-55221-CVE-2025-55222) is a denial-of-service vulnerability in the Modbus TCP and Modbus RTU over TCP USB Function functionalities. A specially crafted network packet can lead to a denial of service. An attacker can send an unauthenticated packet to trigger this vulnerability.

[TALOS-2025-2152](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2152) (CVE-2025-26858) is a buffer overflow vulnerability in the Modbus TCP functionality. A specially crafted set of network packets can lead to denial of service. An attacker can send a sequence of unauthenticated packets to trigger this vulnerability.

### Socomec Easy Config System

[TALOS-2024-2117](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2117) (CVE-2024-45370) is an authentication bypass vulnerability in the User profile management functionality. A specially crafted database record can lead to unauthorized access. An attacker can modify a local database to trigger this vulnerability.

##### Share this post

#### Related Content

[### Dell ControlVault, Lasso, GL.iNet vulnerabilities

November 26, 2025 13:36

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed five vulnerabilities in Dell ControlVault 3 firmware and...