---
title: TeamPass v3.2.1.7
url: https://kitploit.com/en/posts/github-nilsteampassnet-teampass-3217
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:54:13.232580
---

# TeamPass v3.2.1.7

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F2983%2F76a61aea3e6b072e5d6026e19052eed290df88c01ba947b761896846a1e16477.png&w=3840&q=75)

New releaseAug 19, 2026

# TeamPass v3.2.1.7

Collaborative Passwords Manager

Share

[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

# TeamPass 3

TeamPass is a Collaborative Passwords Manager solution installed On-Premise.

[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

![](https://img.shields.io/github/stars/nilsteampassnet/TeamPass?style=social)
![](https://img.shields.io/github/license/nilsteampassnet/teampass)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
![](https://img.shields.io/docker/pulls/teampass/teampass?label=Docker%20Pulls)

![](https://img.shields.io/github/v/release/nilsteampassnet/Teampass)
![](https://img.shields.io/github/commits-since/nilsteampassnet/teampass/latest)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/nilsteampassnet/TeamPass/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/nilsteampassnet/TeamPass/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/nilsteampassnet/TeamPass/badges/build.png?b=master)](https://scrutinizer-ci.com/g/nilsteampassnet/TeamPass/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/nilsteampassnet/TeamPass/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)

> Copyright © 2009-2026, [Nils Laumaillé](https://github.com/nilsteampassnet/teampass/blob/HEAD/Nils%40Teampass.net)

* [Requirements](#requirements)
  + [About PHP versions](#about-php-versions)
* [Installation](#installation)
  + [Traditional Installation (Recommended)](#traditional-installation-recommended)
  + [Docker](#docker)
* [Documentation](#documentation)
* [Languages](#languages)
* [Licence Agreement](#licence-agreement)
* [Website](#website)
* [Bugs](#bugs)

## Requirements

* MySQL 5.7 or higher
* MariaDB 10.7 or higher
* PHP 8.2 or newer
* PHP extensions (required):
  + `openssl`
  + `mysqli`
  + `mbstring`
  + `bcmath`
  + `iconv`
  + `xml`
  + `gd`
  + `curl`
  + `gmp`
  + `ldap` (only if LDAP/AD authentication is used)
* PHP extensions (optional but recommended):
  + `apcu` — in-memory configuration cache, reduces database load on every request
  + `redis` — Redis-backed session storage for high-availability deployments
  + `pcntl` + `posix` — required to run the WebSocket daemon (real-time sync)
  + `opcache` — improves overall PHP performance

### About PHP versions

TeamPass follows active PHP support. The `master` branch requires **at least PHP 8.2** and is tested against PHP 8.3. Using the latest stable PHP release is strongly recommended for both security and performance.

## Installation

### Traditional Installation (Recommended)

Installing TeamPass directly on a PHP/MySQL server gives the best performance and the most control over your environment. This is the recommended approach for production deployments.

* 📖 [Official Installation Guide](https://documentation.teampass.net) — step-by-step instructions covering prerequisites, web server configuration, and first-run setup
* 📝 [Community article](https://www.valters.eu/teampass-a-self-hosted-password-manager-to-increase-organizations-cybersecurity/) — practical walkthrough for a typical Linux/Apache/MySQL stack
* 🎥 [Video tutorial](https://youtu.be/eXieWAIsGzc?feature=shared) — visual installation walkthrough

### Docker

Official images are available for containerized deployments. Docker is convenient for testing and isolated environments but may not deliver the same raw performance as a native installation.

* Docker Hub: `teampass/teampass`
* GitHub Container Registry: `ghcr.io/nilsteampassnet/teampass`
* 📖 [Docker Installation Guide](https://github.com/nilsteampassnet/teampass/blob/HEAD/docs/DOCKER.md) — configuration options, environment variables, and volumes
* 📖 [Migration Guide](https://github.com/nilsteampassnet/teampass/blob/HEAD/docs/DOCKER-MIGRATION.md) — upgrading from older Docker setups

## Documentation

> ✍️ [Documentation](https://documentation.teampass.net) is available.

**Key documentation:**

* [Docker Installation](https://github.com/nilsteampassnet/teampass/blob/HEAD/docs/DOCKER.md) - Complete Docker deployment guide
* [Docker Migration](https://github.com/nilsteampassnet/teampass/blob/HEAD/docs/DOCKER-MIGRATION.md) - Upgrade from older versions
* [Official Documentation](https://documentation.teampass.net) - Full user and admin guides
* [API Documentation](https://documentation.teampass.net/#/api/api-basic) - REST API reference

## Languages

TeamPass is currently available in 20 languages:

* CATALAN
* CHINESE
* CZECH
* DUTCH
* ENGLISH
* ESTONIAN
* FRENCH
* GERMAN
* HUNGARIAN
* ITALIAN
* JAPANESE
* NORWEGIAN
* PORTUGUESE
* PORTUGUESE (BR)
* ROMANIAN
* RUSSIAN
* SPANISH
* TURKISH
* UKRAINIAN
* VIETNAMESE

Languages strings are managed at [POEditor.com](https://poeditor.com/join/project?hash=0vptzClQrM).
Please participate to improving its translation by joining Teampass POEditor project.

## Licence Agreement

For detailed information on the licenses of our dependencies and our licence policy, please see [Detailed Licence Information](https://github.com/nilsteampassnet/teampass/blob/HEAD/licences/dependencies.licences.md).

## Website

Visit [Teampass.net](https://teampass.net/)

## Bugs

If you discover bugs, please report them in [Github Issues](https://github.com/nilsteampassnet/TeamPass/issues).

---

## Support & Community

* 💬 [Reddit Community](https://www.reddit.com/r/TeamPass/)
* 📧 [Email](/cdn-cgi/l/email-protection#6d0304011e2d19080c001d0c1e1e43030819)
* 🐛 [Issue Tracker](https://github.com/nilsteampassnet/TeamPass/issues)
* 📖 [Documentation](https://documentation.teampass.net)

[Read more](/en/tools/github/nilsteampassnet/teampass?expand=1)

## Categories

[Authentication & Authorization](/en/categories/authentication-authorization)[Password Cracking](/en/categories/password-cracking)[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Configuration Auditing](/en/categories/configuration-auditing)[Web Security](/en/categories/web-security)[Cloud Security](/en/categories/cloud-security)[DevSecOps](/en/categories/devsecops)[Privacy](/en/categories/privacy)[Identity & Access Management (IAM)](/en/categories/identity-access-management)[API Security](/en/categories/api-security)[Database Security](/en/categories/database-security)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

TeamPass v3.2.1.7 — Collaborative Passwords Manager | Kitploit