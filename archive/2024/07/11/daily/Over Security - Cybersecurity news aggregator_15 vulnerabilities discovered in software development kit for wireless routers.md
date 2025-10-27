---
title: 15 vulnerabilities discovered in software development kit for wireless routers
url: https://blog.talosintelligence.com/vulnerability-roundup-july-10-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-11
fetch_date: 2025-10-06T17:46:43.748142
---

# 15 vulnerabilities discovered in software development kit for wireless routers

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

![](/content/images/2024/07/vuln-roundup.png)

# 15 vulnerabilities discovered in software development kit for wireless routers

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Wednesday, July 10, 2024 12:00

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Research team recently discovered 15 vulnerabilities in the Realtek rtl819x Jungle software development kit used in some small and home office wireless routers.

This SDK uses the discontinued, open-source Boa as its web server. Talos researchers discovered these vulnerabilities in the Jungle SDK while researching other vulnerabilities in the LevelOne WBR-6013 wireless router, which are also covered in this blog post.

Realtek has patched these issues in the SDK, all in adherence to [Cisco’s third-party vulnerability disclosure policy,](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html) while LevelOne has declined to release a fix.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

# Multiple vulnerabilities in Realtek rtl819x Jungle SDK

*Discovered by Francesco Benvenuto and Kelly Patterson.*

The Realtek rtl819x Jungle software development kit contains 15 vulnerabilities, some of which could lead to arbitrary execution. The SDK uses Boa — a deprecated, open-source software — as a webserver.

The LevelOne WBR-6013, a small and home office (SOHO) wireless router, uses Jungle as its SDK.

Multiple stack-based buffer overflow vulnerabilities arise if an adversary sends a specially crafted set of HTTP requests to the targeted device:

* [TALOS-2023-1875](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1875) (CVE-2023-49073)
* [TALOS-2023-1876](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1876) (CVE-2023-48270)
* [TALOS-2023-1878](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1878) (CVE-2023-49595)
* [TALOS-2023-1895](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1895) (CVE-2023-50243, CVE-2023-50244)
* [TALOS-2023-1891](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1891) (CVE-2023-45215)
* [TALOS-2023-1892](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1892) (CVE-2023-47856)
* [TALOS-2023-1893](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1893) (CVE-2023-50239, CVE-2023-50240)
* [TALOS-2023-1894](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1894) (CVE-2023-41251)
* [TALOS-2023-1903](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1903) (CVE-2023-50330)
* [TALOS-2023-1904](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1904) (CVE-2023-49867)

Another vulnerability, [TALOS-2024-1911](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1911) (CVE-2024-21778), is a heap-based buffer overflow issue that exists if an adversary sends a specially crafted .dat. An attacker could exploit this vulnerability to execute arbitrary code.

Two other issues – [TALOS-2023-1877](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1877) (CVE-2023-45742) and [TALOS-2023-1899](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1899) (CVE-2023-50381, CVE-2023-50383, CVE-2023-50382) -- can also lead to arbitrary code execution, but in these cases, are caused by a series of malicious HTTP requests.

[TALOS-2023-1872](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1872) (CVE-2023-47677) could allow an attacker to carry out a cross-site request forgery attack if they send a specially crafted network packet to the targeted device. This vulnerability could force an authenticated user to submit requests to the device.

And finally, [TALOS-2023-1874](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1874) (CVE-2023-34435) could allow an adversary to update the device to a new version of its firmware without the user knowing, potentially allowing them to deploy a malicious update.

# Vulnerabilities in LevelOne router could lead to remote code execution

*Discovered by Francesco Benvenuto.*

The LevelOne WBR-6013 wireless router contains two vulnerabilities that could lead to remote code execution.

[TALOS-2023-1871](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1871) (CVE-2023-46685) is a hardcoded password vulnerability in the router’s telnetd service. A text file contains the hash of the users’ passwords, which an adversary could access and then use to completely take over a device.

This router also uses Boa as a web server, which by default has the ‘/boafrm/formSysCmd’ API. While there is no LevelOne documentation about this API's existence, an adversary could still reach the API to execute arbitrary commands in the device. An adversary could send a specially crafted network packet to exploit [TALOS-2023-1873](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1873) (CVE-2023-49593).

LevelOne has declined to release a patch for these issues.

# Grandstream GXP2135 command injection vulnerability

*Discovered by Matthew Bernath.*

The Grandstream GXP2135 voice-over-IP phone contains a command injection vulnerability that could lead to arbitrary command execution.

[TALOS-2024-1978](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1978) (CVE-2024-32937) exists if an adversary sends a specially crafted network packet to the targeted device. The attacker could manipulate the vulnerable configuration on the device by authenticating to a web server first, or by carrying out an adversary-in-the-middle attack to co...