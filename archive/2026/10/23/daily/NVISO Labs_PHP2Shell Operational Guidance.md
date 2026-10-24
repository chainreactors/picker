---
title: PHP2Shell Operational Guidance
url: https://blog.nviso.eu/2026/10/23/php2shell-operational-guidance/
source: NVISO Labs
date: 2026-10-23
fetch_date: 2026-10-24T06:45:59.142605
---

# PHP2Shell Operational Guidance

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# PHP2Shell Operational Guidance

[Patrick Lodder](https://blog.nviso.eu/author/patrick-lodder/)

[Exploitation](https://blog.nviso.eu/category/exploitation/), [Incident Response](https://blog.nviso.eu/category/incident-response/), [Vulnerability](https://blog.nviso.eu/category/vulnerability/)

October 23, 2026October 23, 2026
8 Minutes

First published on 22 October 2026, last updated on 23 October 2026 at 16:45 CEST. This public operational guidance is provided to customers and published for the benefit of the wider community. TLP:AMBER information is disclosed through regular channels.

**TL;DR**

* **What:** Two critical PHP vulnerabilities where disclosed, [CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) (RCE via OOM corruption) and [CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) (RCE via stale global state), collectively **PHP2Shell**. Both rated CVSS v4.0 9.2 (Critical). A third, lower-risk CVE (CVE-2026-115560) was disclosed on 23 October and will ship in the regular release cycle.
* **Who’s affected:** Any PHP installation serving web requests, including PHP-FPM, Apache with mod\_php, php-cgi, FrankenPHP, and LiteSpeed. Particular attention for Apache mod\_php, where unauthenticated exploitation has been demonstrated.
* **Exploitation status:** Active exploitation attempts observed by Amazon, Cloudflare, WatchTowr, and NVISO. No confirmed successful compromises or reliable public exploit yet, but PoC claims are circulating.
* **What to do:** Patch to PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35 immediately, prioritising internet-facing systems. Where patching is delayed, apply PHP’s vulnerability-specific mitigations (full details below). Verify that web-server processes are actually using the patched runtime.

## **What happened?**

On 20 October 2026, information about two critical vulnerabilities in PHP surfaced publicly ahead of their planned coordinated disclosure. The vulnerabilities, tracked as CVE-2026-109618 and CVE-2026-109619, have each received a CVSS v4.0 score of 9.2 (Critical).

In response, the PHP security team announced an emergency security release scheduled for 21 October 2026 at 14:00 UTC (16:00 CEST), with the possibility of an earlier release if technical details become public or active exploitation is detected.

Both vulnerabilities are reported to potentially allow unauthenticated remote code execution (RCE). Successful exploitation could enable a remote attacker to execute malicious code on a vulnerable server, potentially compromising the applications and data hosted on it.

On 21 October 2026 at 13:30 UTC (15:30 CEST), the PHP security team released emergency patches addressing both vulnerabilities.

The following are the minimum fixed upstream PHP versions:

|  |  |
| --- | --- |
| **PHP branch** | **Fixed version** |
| PHP 8.5 | **8.5.12** |
| PHP 8.4 | **8.4.27** |
| PHP 8.3 | **8.3.36** |
| PHP 8.2 | **8.2.35** |
| PHP 8.1 and older | No standard upstream release; vendor backports or migration required |

On 23 October 2026, the PHP security team released an informational advisory about another vulnerability: CVE-2026-115560. This vulnerability requires specific combinations of configuration and application code. Because the PHP security team assesses the exploitation of this vulnerability as unlikely, the patch will be released in the regular release cycle, rather than an emergency patch like CVE-2026-109618 and CVE-2026-109619.

## **Why should organisations be concerned?**

PHP is one of the most widely used server-side programming languages for web development. It underpins many websites, content management systems (CMS), e-commerce platforms, customer portals, and business applications.

Popular platforms such as WordPress, Drupal, Joomla, and Magento rely on PHP to execute application logic. Unlike a vulnerability affecting a specific plugin or individual web application, a vulnerability in PHP
itself may affect multiple applications that rely on the same underlying runtime. This makes the potential attack surface particularly broad.

Organisations may also be running PHP without necessarily being aware of it. PHP runtimes can be embedded in legacy applications, hosting environments, internal management portals, containers, and third-party software.

The potential consequences of successful remote code execution include:

* **Unauthorised server access:** Attackers may execute commands within the security context of the affected PHP process.
* **Data theft:** Sensitive information, application secrets, credentials, or customer data accessible to that process could be exposed.
* **Website compromise:** Attackers can modify application content, deploy malicious scripts, or establish persistence through webshells.
* **Operational disruption:** Compromised applications could be taken offline, manipulated, or used to facilitate further attacks.
* **Lateral movement:** A compromised server could provide an initial foothold for attacks against other connected systems.

## **What do we know about these vulnerabilities?**

Three vulnerabilities have been associated with the PHP2Shell disclosure:

| **Identifier** | **Severity** | **Impact** |
| --- | --- | --- |
| **CVE-2026-109618** | CVSS v4.0 9.2 – Critical | RCE via OOM corruption |
| **CVE-2026-109619** | CVSS v4.0 9.2 – Critical | RCE via stale global state |
| **CVE-2026-115560** | *Unknown* | RCE |

The PHP team [provided the following mitigation steps:](https://www.php.net/archive/2026.php)

> If you cannot update immediately: while only an update is a complete solution, the following
> measures reduce exposure to specific attack paths but do not make an installation safe.
>
> * RCE via OOM corruption (CVE-2026-109618):
>   + Set `memory_limit=-1`, preferably in a way applications cannot override, such as `php_admin_value` in the FPM pool or Apache configuration, and check that no pool, directory or application setting puts a finit...