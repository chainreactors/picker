---
title: TP-Link, Canva, HikVision vulnerabilities
url: https://blog.talosintelligence.com/tp-link-canva-hikvision-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-26
fetch_date: 2026-03-27T04:33:10.100826
---

# TP-Link, Canva, HikVision vulnerabilities

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

![](/content/images/2026/03/vuln_roundup-1.jpg)

# TP-Link, Canva, HikVision vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, March 26, 2026 14:34

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed a vulnerability in HikVision, as well as 10 in TP-Link, and 19 in Canva.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html).

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## **Canva Affinity vulnerabilities**

*Discovered by KPC of Cisco Talos.*

Canva Affinity is a free-to-use tool for pixel and vector art manipulation used in graphic and document design.

Talos researchers found 19 vulnerabilities in Affinity. Eighteen of them are out-of-bounds read vulnerabilities in the EMF functionality of Canva Affinity. By using a specially crafted EMF file, an attacker could exploit these vulnerabilities to perform an out-of-bounds read, potentially leading to the disclosure of sensitive information.

* [TALOS-2025-2311](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2311) (CVE-2025-64776)
* [TALOS-2025-2310](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2310) (CVE-2025-64301)
* [TALOS-2025-2300](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2300) (CVE-2025-64733)
* [TALOS-2025-2319](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2319) (CVE-2025-66042)
* [TALOS-2025-2321](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2321) (CVE-2025-62403)
* [TALOS-2025-2314](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2314) (CVE-2025-58427)
* [TALOS-2025-2298](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2298) (CVE-2025-62500)
* [TALOS-2025-2299](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2299) (CVE-2025-61979)
* [TALOS-2025-2317](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2317) (CVE-2025-61952)
* [TALOS-2025-2316](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2316) (CVE-2025-47873)
* [TALOS-2025-2318](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2318) (CVE-2025-66503)
* [TALOS-2025-2324](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2324) (CVE-2026-20726)
* [TALOS-2025-2301](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2301) (CVE-2025-66000)
* [TALOS-2025-2320](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2320) (CVE-2025-65119)
* [TALOS-2025-2325](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2325) (CVE-2026-22882)
* [TALOS-2025-2315](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2315) (CVE-2025-66617)
* [TALOS-2025-2313](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2313) (CVE-2025-66633)
* [TALOS-2025-2312](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2312) (CVE-2025-64735)

The last vulnerability is [TALOS-2025-2297](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2297) (CVE-2025-66342), a type confusion vulnerability in the EMF functionality of Canva Affinity. A specially crafted EMF file can trigger this vulnerability, which can lead to memory corruption and result in arbitrary code execution.

## **TP-Link vulnerabilities**

*Discovered by Lilith >\_> of Cisco Talos.*

The TP-Link Archer AX53 is a dual band gigabit Wi-Fi router. Talos researchers found 10 vulnerabilities in the router functionality.

[TALOS-2025-2290](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2290) (CVE-2025-62673) is a stack-based buffer overflow vulnerability in the tdpServer ssh port update functionality of Tp-Link AX53. A specially crafted network packet can lead to stack-based buffer overflow.

These eight vulnerabilities exist in the tmpServer opcode of the AX53:

* [TALOS-2025-2283](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2283) (CVE-2025-59482): Buffer overflow
* [TALOS-2025-2284](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2284) (CVE-2025-62405): Stack-based buffer overflow
* [TALOS-2025-2285](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2285) (CVE-2025-59487): Write-what-where
* [TALOS-2025-2286](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2286) (CVE-2025-61983): Out-of-bounds write
* [TALOS-2025-2287](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2287) (CVE-2025-62404): Stack-based buffer overflow
* [TALOS-2025-2288](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2288) (CVE-2025-61944): Out-of-bounds write
* [TALOS-2025-2289](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2289) (CVE-2025-58455): Stack-based buffer overflow
* [TALOS-2025-2294](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2294) (CVE-2025-58077): Heap-based buffer overflow

A specially crafted set of network packets can be sent to trigger these vulnerabilities, which can lead to arbitrary code execution.

[TALOS-2025-2291](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2291) (CVE-2025-62501) is a misconfiguration vulnerability in the SSH Hostkey functionality. A specially crafted man-in-the-middle attack can lead to credentials leak.

## **HikVision buffer overflow vulnerability**

*Discovered by a member of Cisco Talos.*

HikVision creates AI-trained...