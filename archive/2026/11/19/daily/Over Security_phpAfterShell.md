---
title: phpAfterShell
url: https://depthfirst.com/phpaftershell
source: Over Security
date: 2026-11-19
fetch_date: 2026-11-20T09:23:02.952473
---

# phpAfterShell

[depthfirst](/)     Product      [Customers](/customer-stories)  [Research](/research)   Company

[Sign in](https://app.depthfirst.com)   [Get a demo](/book-a-demo)

[Platform   Your autonomous security command center](/platform)

[Code   Find vulnerabilities scanners were never built to see](/code)

[Supply Chain   Know what's reachable, not just what's present](/supply-chain)

[Secrets   Stop leaks before they leave the repo](/secrets)

[Agentic Pentesting   Find vulnerabilities in code that's already running](/agentic-pentesting)

[Dependency Firewall   Detect malicious behavior before it spreads through your environment](/dependency-firewall)

[About   Learn how we help teams uncover threats before attackers do](/company)

[Careers   We're growing the team](/company#careers)

[Partners   Become a depthfirst Partner](/partners)

[Blog   Insights, research, and security trends from our team](/blog)

[Events   Join us at conferences, webinars, and live security sessions](/events)

[Press kit   Brand assets and guidance for media and partners](/press-kit)

[depthfirst](/)    Open navigation

Product

[Platform   Your autonomous security command center](/platform)  [Code   Find vulnerabilities scanners were never built to see](/code)  [Supply Chain   Know what's reachable, not just what's present](/supply-chain)  [Secrets   Stop leaks before they leave the repo](/secrets)  [Agentic Pentesting   Find vulnerabilities in code that's already running](/agentic-pentesting)  [Dependency Firewall   Detect malicious behavior before it spreads through your environment](/dependency-firewall)

 [Customers](/customer-stories)  [Research](/research)

Company

[About   Learn how we help teams uncover threats before attackers do](/company)  [Careers   We're growing the team](/company#careers)  [Partners   Become a depthfirst Partner](/partners)  [Blog   Insights, research, and security trends from our team](/blog)  [Events   Join us at conferences, webinars, and live security sessions](/events)  [Press kit   Brand assets and guidance for media and partners](/press-kit)

[Sign in](https://app.depthfirst.com)   [Get a demo](/book-a-demo)

CVE-2026-126714 · CVSS v4.0 9.2 (Critical) found by depthfirst's security research team

# phpAfterShell

phpAfterShell is a critical flaw in PHP itself that can let a remote attacker run arbitrary code on your server. If your applications use PHP's default file-based sessions, an attacker could read or change the data, credentials, and customer records they handle, or disrupt the service.

## TL;DR

PHP has just released a fix for CVE-2026-126714 (CVSS v4.0: 9.2), a critical vulnerability we discovered in the interaction between upload progress and PHP’s file-based session handler. If a `pwrite()`/`ftruncate()` update is interrupted, PHP may leave behind a malformed session file that is later loaded by `session_start()`, yielding an arbitrary deserialization primitive. Chained with another of our PHP-native deserialization-to-RCE findings, this leads directly to remote code execution.

Any application running an affected PHP version with file-based sessions is exposed until PHP is upgraded.

Why it matters:

* PHP powers 68% of websites with a known server-side language ([W3Techs](https://w3techs.com/technologies/details/pl-php)).
* The flaw is in PHP itself, not in any one application or framework.
* The outcome is remote code execution.

## Security impact

**What is affected**

The vulnerability lives in PHP’s session handling with file-based storage, which is the default (`session.save_handler = files`).

* **PHP 8.5** < 8.5.13.
* **PHP 8.4** < 8.4.28.
* **PHP 8.3** < 8.3.37.
* **PHP 8.2** < 8.2.36.
* **PHP 8.1 and earlier** are end-of-life. The official 7.4, 8.0, and 8.1 EOL mitigation branches disable upload progress in the callback and are not affected.

The October 21 PHP releases (8.5.12, 8.4.27, 8.3.36, 8.2.35) do not contain the fix.

Applications that store sessions in Redis, a database, or another non-file handler are not affected by this specific defect. The full evaluation is in the PHP security advisory.

## Remediation

**Recommended action: Upgrade**

If you run an affected version, install the fixed release for your
branch. Rebuild any container images, redeploy, and confirm production is
running the new version.

| If you run | Upgrade to |
| --- | --- |
| PHP 8.5 < 8.5.13 | 8.5.13 |
| PHP 8.4 < 8.4.28 | 8.4.28 |
| PHP 8.3 < 8.3.37 | 8.3.37 |
| PHP 8.2 < 8.2.36 | 8.2.36 |
| PHP 8.1 or earlier | A supported branch |

PHP 8.1 and earlier are end-of-life. The official 7.4, 8.0, and 8.1 EOL
mitigation branches disable upload progress in the callback and are not
affected.

**If you cannot upgrade immediately: turn off session upload progress.**

Session upload progress is the easiest attack path. If your application
does not need the feature, disable it in `php.ini` and restart your PHP
workers. Also limit the untrusted data your application stores in
sessions.

```
session.upload_progress.enabled = 0
```

This removes the easiest path to the flaw, not the flaw itself. You still
need the upgrade.

## Check your exposure with depthfirst

depthfirst shows where affected PHP versions are in use and prioritizes findings. You can find affected PHP versions in your environment in five steps.

1. **Connect your repositories.** Add every repository that might contain PHP, including self-hosted tools and legacy services.
2. **Run a scan.** depthfirst reads the PHP version each repository declares. Findings appear after the next scan, or right away on a rescan.
3. **Open the language runtime findings.** Go to Issues, Dependencies, Language runtime. A repository on an affected PHP version shows a finding for CVE-2026-126714.
4. **Review each finding.** It shows the declared PHP version and the version to upgrade to. Treat every match as vulnerable.
5. **Confirm what is deployed.** A repository’s declared version can differ from production, so check the version serving web requests.

**Not a depthfirst customer?** We offer repository and container image scans for PHP exposure, and help assessing temporary mitigations for teams that cannot upgrade right away.

**[Get a scan →](/php-exposure-scan-and-mitigations)**

## Technical details

The bug lives in PHP’s file-based session storage. When PHP writes updated session data back to a session file, the write is not atomic. If it is interrupted partway through, the file keeps part of the new data and part of the old. On a later request PHP reads the file back and deserializes it, and the mixed contents can be made to parse as objects the attacker chose. A gadget chain in the application’s code turns those objects into code execution in the PHP worker process. Session upload progress is the easiest path to the bug, which is why disabling it is the interim mitigation.

The full root cause analysis and the patch are in our technical writeup:

**[Read the full technical analysis](/research/phpaftershell)**

## Credits

This vulnerability was discovered by depthfirst’s frontier AI models working with depthfirst researchers.

depthfirst reported the issue privately to the PHP project in late October 2026 and worked with PHP’s maintainers as they developed patches for all four supported branches. PHP published the fix and its advisory on November 19, 2026. We thank the PHP maintainers for their work throughout the disclosure process.

* PHP security advisory: [php.net announcement](https://www.php.net/)
* CVE: [CVE-2026-126714](https://www.cve.org/CVERecord?id=CVE-2026-126714)

## Open Defense Initiative

$5 million in platform credits to help maintainers of critical open source projects find and fix vulnerabilities before they’re exploited.

[Learn more](/open-defense)

## Frequently asked questions

* How do I know if I am affected?

  Check two things. First, the PHP version serving your web requests: anything older than 8.5.13, 8.4.28, 8.3.37, or 8.2.36 is affected. Second, your sessio...