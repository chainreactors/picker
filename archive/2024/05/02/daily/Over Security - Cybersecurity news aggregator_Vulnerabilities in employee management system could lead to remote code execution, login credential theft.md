---
title: Vulnerabilities in employee management system could lead to remote code execution, login credential theft
url: https://blog.talosintelligence.com/vulnerability-roundup-may-1-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-02
fetch_date: 2025-10-06T17:17:36.745084
---

# Vulnerabilities in employee management system could lead to remote code execution, login credential theft

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

![](/content/images/2024/05/vuln-roundup.png)

# Vulnerabilities in employee management system could lead to remote code execution, login credential theft

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Wednesday, May 1, 2024 12:00

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Research team has disclosed more than a dozen vulnerabilities over the past three weeks, five in a device that allows employees to check in and out of their shifts, and another that exists in an open-source library used in medical device imaging files.

The Peplink Smart Reader contains several vulnerabilities, including one issue that could allow an adversary to obtain the administrator’s login credentials and the MD5-hashed version of their password.

Talos also recently helped to responsibly disclose and patch other vulnerabilities in the Foxit PDF Reader and two open-source libraries that support the processing and handling of DICOM files.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

# Code execution, information disclosure vulnerabilities in Peplink Smart Reader

*Discovered by Matt Wiseman.*

The Peplink Smart Reader is an internet-connected device associated with the PepXIM Time-Logging and Security System. Companies’ employees use this device to check in and out of their shifts, allowing administrators to keep track of time cards and pay. It also can control access to certain buildings, and even public transportation.

There are two information disclosure vulnerabilities, [TALOS-2023-1863](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1863) (CVE-2023-43491) and [TALOS-2023-1865](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1865) (CVE-2023-45209), that are triggered if an adversary sends a specially crafted HTTP message to the targeted device.

If successful, the attacker could eventually view the active administrator’s username and MD5-hased password. And in the case of TALOS-2023-1865, it goes a step further, potentially allowing the adversary to view wireless network credentials, network configuration details and SNMP configuration details.

With those credentials (or admin credentials obtained by other means), an adversary could exploit [TALOS-2023-1868](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1868) (CVE-2023-40146), a privilege escalation vulnerability in the Smart Reader. An adversary could execute a specially crafted command line argument to cause a limited-shell escape and execute unblocked, default busybox functionality to eventually gain access to an uninhibited root shell.

[TALOS-2023-1866](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1866) (CVE-2023-45744) is also triggered by a specially crafted HTTP request, but in this case, could allow an adversary to manipulate certain configuration settings on the device.

The most serious of the issues Talos discovered in the Smart Reader is [TALOS-2023-1867](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1867) (CVE-2023-39367), a command injection vulnerability that could allow an attacker to execute arbitrary commands. This vulnerability has a 9.1 CVSS score out of 10. An authenticated attacker can leverage this vulnerability to execute arbitrary commands on the device with root privileges and elevate their access to the vulnerable system.

# Silicon Labs Gecko Platform invalid pointer dereference vulnerability

*Discovered by Kelly Patterson.*

An invalid pointer dereference vulnerability exists in the HTTP server header parsing functionality of the Silicon Labs Gecko Platform.

The Gecko Platform SDK is the collection of Silicon Labs’ wireless software development kits and Gecko Platform into an integrated package. It allows users to develop applications inside Silicon Labs’ internet-of-things software ecosystem.

[TALOS-2024-1945](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1945) (CVE-2023-51391) is triggered if an adversary sends the target a specially crafted network packet, which could lead to a denial-of-service condition.

# Incorrect type conversion vulnerability in open-source library for DICOM files

*Discovered by Emmanuel Tacheau.*

There is an incorrect type conversion vulnerability in OFFIS DCMTK, an open-source library often used to manage, store and convert DICOM files. DICOM is the commonly used file type to transfer, send and store medical imaging files, such as X-rays and ultrasounds.

Hospitals and companies use DCMTK for various purposes, ranging from product testing to being a building block for research projects, prototypes and commercial products.

[TALOS-2024-1957](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1957) (CVE-2024-28130) could allow an adversary to execute arbitrary code on the targeted machine if they trick the user into opening a specially crafted file.

# Out-of-bounds write vulnerabilities in Grassroots DICOM library

*Discovered by Emmanuel Tacheau.*

Another open-source library for handling DICOM files, Grassroots DiCoM, contains three out-of-bounds writer vulnerabilities.

[TALOS-2024-1944](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1944) (CVE-2024-25569) and [TALOS-2024-1935](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1935) (CVE-2024-22373) can be triggered if an adversary tricks the target into opening a specially crafted, malicious DICOM file, eventually allowing them to read out-of-bounds memory.

[TALOS-2024-1924](https://talosintelligence.com/vulnerability_reports/TALOS-202...