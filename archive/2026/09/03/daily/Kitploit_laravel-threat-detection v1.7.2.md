---
title: laravel-threat-detection v1.7.2
url: https://kitploit.com/en/posts/github-jay123anta-laravel-threat-detection-v172
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:38.859739
---

# laravel-threat-detection v1.7.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12500/dcc6164cecd26fecabe91d424f162fcc412e8627c2e09c4036806662b313f1d8.png)

New releaseSep 3, 2026

# laravel-threat-detection v1.7.2

Passive Laravel middleware that detects and logs SQL injection, XSS, RCE, bot scanners, and 175+ attack patterns. Features a built-in dashboard, Slack alerts, REST API, and geo-enrichment. IDS, not WAF.

Share

[![Latest Version](https://img.shields.io/packagist/v/jayanta/laravel-threat-detection.svg?style=flat-square)](https://packagist.org/packages/jayanta/laravel-threat-detection)
[![Tests](https://img.shields.io/github/actions/workflow/status/jay123anta/laravel-threat-detection/tests.yml?branch=main&style=flat-square&label=tests)](https://github.com/jay123anta/laravel-threat-detection/actions/workflows/tests.yml)
[![PHPStan Level 5](https://img.shields.io/badge/PHPStan-level%205-brightgreen?style=flat-square)](https://github.com/jay123anta/laravel-threat-detection/actions/workflows/tests.yml)
[![Code Style Pint](https://img.shields.io/badge/code%20style-Pint-orange?style=flat-square)](https://github.com/jay123anta/laravel-threat-detection/actions/workflows/tests.yml)
[![Total Downloads](https://img.shields.io/packagist/dt/jayanta/laravel-threat-detection.svg?style=flat-square)](https://packagist.org/packages/jayanta/laravel-threat-detection)
[![PHP Version](https://img.shields.io/packagist/php-v/jayanta/laravel-threat-detection?style=flat-square)](https://packagist.org/packages/jayanta/laravel-threat-detection)
[![License](https://img.shields.io/packagist/l/jayanta/laravel-threat-detection.svg?style=flat-square)](https://github.com/jay123anta/laravel-threat-detection/blob/main/LICENSE)

# Laravel Threat Detection

**Security monitoring and attack logging for Laravel. Detect and log SQL injection,
XSS, RCE, directory traversal, bot scanners and `/wp-admin`-style recon probes —
every hostile request recorded to your database with full application context.
It's an IDS, not a WAF: it never blocks, filters, or modifies a request.**

![Install the package, send three attacks — SQL injection, directory traversal, XSS — every one returns HTTP 200 because nothing is blocked, and all three are already counted in threat-detection:stats](https://raw.githubusercontent.com/jay123anta/laravel-threat-detection/main/art/demo.gif)

### Are you here because you saw something like this?

root@kitploit:~

```
GET /wp-admin/setup-config.php          404   — on a site that isn't WordPress
GET /.env                               404   — someone wants your database password
GET /?id=1' UNION SELECT password FROM  200   — SQL injection against a real route
GET /phpmyadmin/index.php               404   — scanning for an admin panel
```

Those requests are already reaching your Laravel app. Your access log shows the URL
and the status code, and nothing else — not the decoded payload, not which of your
routes was targeted, not whether the same IP has tried forty other things this hour.

This package answers those questions. Drop it into any Laravel 10–13 app and it starts
scanning every HTTP request against 150+ attack patterns, scoring each match by
confidence and writing it to your database — with a built-in dashboard, Slack alerts,
geo-enrichment, and fail2ban/blocklist exports. No request is ever blocked. Think
security camera, not a lock: it shows you exactly who's probing your routes, how
often, and with what techniques.

> Extracted from a production app and battle-tested on real traffic. 335 tests, no runtime
> dependencies beyond Laravel itself, and no internet connection required for detection.
>
> Upgrading? See [UPGRADING.md](https://github.com/jay123anta/laravel-threat-detection/blob/main/UPGRADING.md). Contributing? See [CONTRIBUTING.md](https://github.com/jay123anta/laravel-threat-detection/blob/main/CONTRIBUTING.md).

## Get started in under a minute

root@kitploit:~

```
composer require jayanta/laravel-threat-detection
php artisan vendor:publish --tag=threat-detection-migrations
php artisan migrate
```

Then add the middleware to your `web` group (one line in `bootstrap/app.php` on Laravel 11+,
or `app/Http/Kernel.php` on Laravel 10) — full snippet in [Quick Start](#quick-start) below.
That's it; detection is live.

root@kitploit:~

```
php artisan threat-detection:doctor   # confirms it is actually recording
```

---

## Where it fits: IDS vs WAF vs edge

This package is a **passive, application-level IDS** — it watches and records, it doesn't
block. It's meant to sit *alongside* a WAF or edge service, not replace one. Each layer sees
something the others can't:

|  | **This package** (app IDS) | **WAF** (mod\_security, Cloudflare WAF) | **Edge / CDN** (Cloudflare) |
| --- | --- | --- | --- |
| Blocks malicious requests | ❌ logs only | ✅ | ✅ |
| Full app context (exact route, decoded payload, authenticated user) | ✅ | ⚠️ partial | ❌ |
| Built-in dashboard + threat log in your DB | ✅ | ⚠️ varies | ⚠️ edge only |
| App-specific detections (e.g. Aadhaar / PAN / IFSC PII) | ✅ custom patterns | ❌ | ❌ |
| Works offline / no external service | ✅ | ⚠️ depends | ❌ |
| Stops traffic before it reaches your app | ❌ | ✅ edge | ✅ |
| Setup | one `composer require` | medium–high | low–medium |
| Cost | free, MIT | varies | free tier + paid |

**The short version:** an edge/WAF is your lock on the door; this is the security camera
*inside*, with the app context to tell you exactly what's being tried on which route, by
whom, and how often. Use it to feed real decisions — fail2ban bans, rate limits,
geo-blocking — with data your edge layer never sees.

### What it deliberately is NOT

* **Not a WAF.** It never blocks, filters, or modifies a request. Use Cloudflare,
  mod\_security, or a real WAF for enforcement. (No edge layer to hand off to? The
  [operator-side helpers](#acting-on-the-data-operator-side-blocking) expose the
  package's decisions so you can write your own five-line blocking middleware —
  the enforcement code stays yours, not the package's.)
* **Not a replacement for secure coding.** Parameterized queries, input validation, and
  output escaping are your actual defenses. This package assumes your code is already
  secure and gives you *visibility*, not protection.
* **Not an edge service.** If you can put Cloudflare in front, do — then add this for the
  application-level detail edge services can't see.

### So what do you actually do with it?

The most common question about a detector that never blocks. Four answers, in
increasing order of effort:

| You want to | Use | Effort |
| --- | --- | --- |
| See what's hitting you | The [dashboard](#dashboard) or `threat-detection:stats` | none, it's already running |
| Ban repeat offenders at the firewall | [`threat-detection:export-fail2ban`](#artisan-commands) — pipe to a cron | one line |
| Deny at the web server | [`threat-detection:export-blocklist`](#artisan-commands) → nginx/apache directives | one line |
| Refuse requests in-app | [Operator-side helpers](#acting-on-the-data-operator-side-blocking) — `isBlocklisted()`, `isDdosThresholdExceeded()` | ~10 lines of your own middleware |
| React in real time | The [`ThreatDetected` event](#threatdetected-event) — Telegram, SIEM, PagerDuty | a listener |

The package supplies the intelligence; you supply the refusal. That split is
deliberate — enforcement code that lives in your app is code you can read,
test and turn off, and it means a detection bug can never take your site down.

### How it compares to other Laravel security packages

These solve different problems and compose well — the table is about picking the
right tool, no...