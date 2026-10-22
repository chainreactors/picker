---
title: Two critical RCEs in PHP core
url: https://blog.talosintelligence.com/two-critical-rces-in-php-core/
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:25.113700
---

# Two critical RCEs in PHP core

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

# Two critical RCEs in PHP core

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Wednesday, October 21, 2026 11:10

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)

Cisco Talos is tracking the disclosure of two unauthenticated remote code execution (RCE) flaws in PHP core, dubbed “php2shell”, triggered by a plain HTTP request and exploitable before any application code runs, affecting every PHP build since 5.4. Based on the entities involved in the disclosure, artificial intelligence and associated technologies played a key role in the discovery of these vulnerabilities — yet another example of how these technologies are forcing change across the landscape, most notably on patching processes for organizations because of the wave of vulnerabilities being disclosed.

Cisco customers are covered with the Cisco Talos Network Intrusion Prevention (SNORT®) signatures 67359 and 67360. These rules are also available in the Community Ruleset for open-source customers. Please refer to the following recommendations, detection, and coverage guidance for more information.

## Details

CVE-2026-109618 and CVE-2026-109619 are both critical vulnerabilities with a CVSS v4.0 score of 9.2.

* CVE-2026-109618 occurs when out-of-memory handling interrupts PHP while internal request data is only partially initialized. Request cleanup may then treat invalid data as valid.
* CVE-2026-109619 occurs when a stale internal state is reused after its backing memory has already been freed, before normal initialization resets it.

## Impact

The potential blast radius is enormous and extends across the PHP ecosystem. The vulnerability sits in PHP core, so applications running affected versions — including WordPress, Drupal, Magento, Shopware, WooCommerce, and Laravel, plus PHP sites hosted through cPanel or Plesk — may be exposed. Note that many older branches will no longer receive fixes, so customers are urged to upgrade to a supported version as soon as possible.

Talos regularly investigates threat actor exploitation of vulnerabilities. State-sponsored and affiliated threat actors, as well as ransomware and other financially motivated groups, all employ tactics to exploit RCE. Talos assesses that all industries running PHP applications are at risk for exploitation if systems remain unpatched.

PHP 8.1 and older are end of life (EOL), and PHP 8.2 security support ends Dec. 31, 2026. Talos’ initial estimates based on open-source intelligence show a significant corpus of PHP systems that will not receive a patch (~50%). If your organization is running PHP 8.1 or older, Talos very strongly advises immediate update to PHP 8.2 or later. There is no patch for PHP 8.1 or older.

Talos is actively monitoring the impact of these CVEs and has not seen them being exploited in the wild yet (as of October 21, 2026 14:00 UTC/10:00 a.m. ET).

## Recommendations and detection guidance

Talos strongly recommends all PHP users to upgrade to the [available fixed releases](https://www.php.net/downloads.php). There are no intermediate or temporary controls that provide comprehensive protection; however, [PHP advises](https://www.php.net/archive/2026.php#2026-10-21-5) that the following measure may reduce exposure to specific attack paths:

[**CVE-2026-109618**](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)

* Set memory\_limit=-1, preferably in a way applications can't override, such as php\_admin\_value in the FPM pool or Apache configuration, and check that no pool, directory or application setting puts a finite limit back. This removes the controllable PHP memory limit failure, but an underlying allocation failure can still reach the vulnerable path.
* Set a low post\_max\_size. For applications that don't require file uploads, set post\_max\_size = 8M. If file uploads are necessary, set post\_max\_size = 32M. Keep upload\_max\_filesize below post\_max\_size. Consider enforcing limits at the web server or proxy level for decoded request size, input field count, multipart part count, header count, and nesting depth. These limits must also cover requests without a usable Content-Length.
* Use a container or cgroup limit as an availability boundary, preferably with a policy that kills only the affected worker. Do not substitute RLIMIT\_AS or RLIMIT\_DATA, as these can cause the vulnerable allocation failure.

[**CVE-2026-109619**](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)

* Set session.upload\_progress.enabled=0 and restart every worker. Use php.ini, an FPM pool, or server configuration that applies before request parsing. Do not rely on ini\_set() or FPM .user.ini. This blocks the confirmed session paths but not other variants.
* On PHP 8.5, set fatal\_error\_backtraces=0 and restart every worker. This blocks the confirmed fatal backtrace path only.
* Remove invalid or deprecated settings applied per request that emit diagnostics before initialization. Hiding diagnostics with error\_reporting, display\_errors, or @ does not help.
* Fix attacker-reachable fatal errors and execution timeouts, including failures in callbacks, upload or import processing, and cleanup.

This is another vulnerability that owes its origin to AI and its associated technologies. As we move through 2026, the wave of vulnerabilities and related patches is building. Talos advises organizations to work on a triaged process for prioritizing vulnerabilities with a specific focus on public-facing systems and vulnerabilities that are under active exploitation. The glaring need to prioritize vulnerabilities along with a streamlined process for rolling out patching strongly indicates that the historic trend of “baking in” patches before deployment is not going to survive the AI era.

The true impact of this vulnerability...