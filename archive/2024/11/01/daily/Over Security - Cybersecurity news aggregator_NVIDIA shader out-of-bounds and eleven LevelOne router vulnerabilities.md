---
title: NVIDIA shader out-of-bounds and eleven LevelOne router vulnerabilities
url: https://blog.talosintelligence.com/nvidia-shader-out-of-bounds-and-level1-2/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-01
fetch_date: 2025-10-06T19:19:43.042087
---

# NVIDIA shader out-of-bounds and eleven LevelOne router vulnerabilities

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

# NVIDIA shader out-of-bounds and eleven LevelOne router vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Thursday, October 31, 2024 11:29

[Vulnerability Roundup](https://blog.talosintelligence.com/category/vulnerability-roundup/)

Cisco Talos' Vulnerability Research team recently discovered five Nvidia out-of-bounds access vulnerabilities in shader processing, as well as eleven LevelOne router vulnerabilities spanning a range of possible exploits.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

**NVIDIA Graphics remote out-of-bounds execution vulnerabilities**

*Discovered by Piotr Bania.*

NVIDIA Graphics drivers are software for NVIDIA Graphics GPU installed on the PC. They are used to communicate between the operating system and the GPU device. This software is required in most cases for the hardware device to function properly.

Talos discovered multiple out-of-bounds read vulnerabilities in Nvidia that could be triggered remotely in virtualized environments, via web browser, potentially leading to disclosure of sensitive information and further memory corruption. Researchers used RemoteFX; while recently deprecated by Microsoft, some older machines may still use this software.

Advisories related to these vulnerabilities:
[TALOS-2024-1955](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1955) (CVE-2024-0121)
[TALOS-2024-2012](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2012) (CVE-2024-0117)
[TALOS-2024-2013](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2013) (CVE-2024-0118)
[TALOS-2024-2014](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2014) (CVE-2024-0120)
[TALOS-2024-2015](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2015) (CVE-2024-0119)

**LevelOne wireless SOHO router vulnerabilities**

*Discovered by Patrick DeSantis and Francesco Benvenuto*.

Eleven vulnerabilities of different types were discovered in the LevelOne WBR-6012 SOHO router.

The LevelOne WBR-6012 is a low-cost wireless SOHO router, marketed as an easy-to-configure and operate internet gateway for homes and small offices.

Talos discovered these vulnerabilities in the R0.30e6 version of the router:

[TALOS-2024-1979](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1979) (CVE-2024-28875,CVE-2024-31151): Hard-coded credentials exist in the web service, allowing attackers to gain unauthorized access during the first 30 seconds post-boot. Used with other vulnerabilities that force a reboot, time restrictions for exploitation can be greatly reduced. An undocumented user account with hard-coded credentials also exists.

[TALOS-2024-1981](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1981) (CVE-2024-24777): A cross-site request forgery vulnerability exists in the web application, and a specially crafted HTTP request can lead to unauthorized access. An attacker can stage a malicious web page to trigger this vulnerability.

[TALOS-2024-1982](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1982) (CVE-2024-31152): An improper resource allocation vulnerability exists due to improper resource allocation within the web application. A series of HTTP requests can cause a reboot, which could lead to network service interruptions and access to a backdoor account.

[TALOS-2024-1983](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1983) (CVE-2024-32946): A cleartext transmission vulnerability exists, and sensitive information is transmitted via FTP and HTTP services, exposing it to network sniffing attacks.

[TALOS-2024-1984](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1984) (CVE-2024-33699): A weak authentication vulnerability exists in the web application firmware, which allows attackers to change the administrator password to gain higher privileges without knowing the current administrator password.

[TALOS-2024-1985](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1985) (CVE-2024-33603): An information disclosure in the web application allows unauthenticated users to access an undocumented verbose system log page and obtain sensitive data, such as memory addresses and IP addresses for login attempts. This flaw could lead to session hijacking due to the device's reliance on IP addresses for authentication.

[TALOS-2024-1986](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1986) (CVE-2024-33626): A web application information disclosure vulnerability can reveal sensitive information, such as the Wi-Fi WPS PIN, through a hidden page accessible by an HTTP request. Disclosure of this information could enable attackers to connect to the device's Wi-Fi network.

[TALOS-2024-1996](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1996) (CVE-2024-23309): An authentication bypass vulnerability results from the web application’s reliance on client IP addresses for authentication. Attackers can spoof an IP address to gain unauthorized access without a session token.

[TALOS-2024-1997](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1997) (CVE-2024-28052): A buffer overflow vulnerability can be caused by specially crafted HTTP POST requests with URIs containing 1,454 or more characters, not starting with “upn” or “upg”.

[TALOS-2024-1998](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1998) (CVE-2024-33700): An improper input validation within the FTP functionality can enable attackers to cause denial of service through a series of malformed FTP commands.

[TALOS-2024-2001](ht...