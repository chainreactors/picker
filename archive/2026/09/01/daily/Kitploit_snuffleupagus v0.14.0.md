---
title: snuffleupagus v0.14.0
url: https://kitploit.com/en/posts/github-jvoisin-snuffleupagus-v0140
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:06.406883
---

# snuffleupagus v0.14.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4272/0a35c7647f7bd3121717b79a1b9c2fe60b1717f5a33f3967bd34d91cf4c83a7f.png)

New releaseSep 1, 2026

# snuffleupagus v0.14.0

Security module for php7 and php8 - Killing bugclasses and virtual-patching the rest!

Share

# [![Snuffleupagus' logo](https://raw.githubusercontent.com/jvoisin/snuffleupagus/main/doc/source/_static/sp.png)](https://snuffleupagus.readthedocs.io/) Snuffleupagus

#### Security module for php7 and php8 - Killing bugclasses and virtual-patching the rest!

[![Testing PHP7 on various Linux distributions](https://github.com/jvoisin/snuffleupagus/actions/workflows/distributions_php7.yml/badge.svg)](https://github.com/jvoisin/snuffleupagus/actions/workflows/distributions_php7.yml)
[![Testing PHP8 on various Linux distributions](https://github.com/jvoisin/snuffleupagus/actions/workflows/distributions_php8.yml/badge.svg)](https://github.com/jvoisin/snuffleupagus/actions/workflows/distributions_php8.yml)
[![Coverity](https://scan.coverity.com/projects/13821/badge.svg?flat=1)](https://scan.coverity.com/projects/jvoisin-snuffleupagus)
[![CII Best Practises](https://bestpractices.coreinfrastructure.org/projects/1267/badge)](https://bestpractices.coreinfrastructure.org/projects/1267)
[![readthedocs.org](https://readthedocs.org/projects/snuffleupagus/badge/?version=latest)](http://snuffleupagus.readthedocs.io/?badge=latest)
[![coveralls](https://coveralls.io/repos/github/jvoisin/snuffleupagus/badge.svg?branch=main)](https://coveralls.io/github/jvoisin/snuffleupagus?branch=main)
[![twitter](https://img.shields.io/badge/twitter-follow-blue.svg)](https://twitter.com/dustriorg)
[![Packaging status](https://repology.org/badge/tiny-repos/php:snuffleupagus.svg)](https://repology.org/project/php%3Asnuffleupagus/versions)
[![CodeQL](https://github.com/jvoisin/snuffleupagus/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/jvoisin/snuffleupagus)

[Key Features](#key-features) •
[Download](#download) •
[Examples](#examples) •
[Documentation](https://snuffleupagus.readthedocs.io/) •
[License](https://github.com/jvoisin/snuffleupagus/blob/main/LICENSE) •
[Thanks](#thanks)

Snuffleupagus is a [PHP 7+ and 8+](https://secure.php.net/) module designed to
drastically raise the cost of attacks against websites, by killing entire bug
classes. It also provides a powerful virtual-patching system, allowing
administrator to fix specific vulnerabilities and audit suspicious behaviours
without having to touch the PHP code.

## Key Features

* No [noticeable performance impact](https://dustri.org/b/snuffleupagus-030-dentalium-elephantinum.html)
* Powerful yet simple to write virtual-patching rules
* Killing several classes of vulnerabilities
  + [Unserialize-based](https://www.owasp.org/images/9/9e/Utilizing-Code-Reuse-Or-Return-Oriented-Programming-In-PHP-Application-Exploits.pdf) code execution
  + [`mail`-based](https://blog.ripstech.com/2016/roundcube-command-execution-via-email/) code execution
  + Cookie-stealing [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting)
  + File-upload based code execution
  + Weak PRNG
  + [XXE](https://en.wikipedia.org/wiki/XML_external_entity_attack)
  + Filter based remote code execution and assorted shenanigans
* Several hardening features
  + Automatic `secure` and `samesite` flag for cookies
  + Bundled set of rules to detect post-compromissions behaviours
  + Global [strict mode](https://secure.php.net/manual/en/migration70.new-features.php#migration70.new-features.scalar-type-declarations) and type-juggling prevention
  + Whitelisting of [stream wrappers](https://secure.php.net/manual/en/intro.stream.php)
  + Preventing writeable files execution
  + Whitelist/blacklist for `eval`
  + Enforcing TLS certificate validation when using [curl](https://secure.php.net/manual/en/book.curl.php)
  + Request dumping capability
* A relatively sane code base:
  + A [comprehensive](https://coveralls.io/github/jvoisin/snuffleupagus?branch=main) test suite close to 100% coverage
  + Every commit is tested on [several distributions](https://gitlab.com/jvoisin/snuffleupagus/pipelines)
  + An `clang-format`-enforced code style
  + A [comprehensive documentation](https://snuffleupagus.rtfd.io)
  + Usage of [coverity](https://scan.coverity.com/projects/jvoisin-snuffleupagus), codeql, [scan-build](https://clang-analyzer.llvm.org/scan-build.html), …

## Download

We've got a [download
page](https://snuffleupagus.readthedocs.io/download.html), where you can find
packages for your distribution, but you can of course just `git clone` this
repo, or check the releases on [github](https://github.com/jvoisin/snuffleupagus/releases).

## Examples

We're providing [various example rules](https://github.com/jvoisin/snuffleupagus/tree/main/config),
that are looking like this:

root@kitploit:~

```
# Harden the `chmod` function
sp.disable_function.function("chmod").param("mode").value_r("^[0-9]{2}[67]$").drop();

# Mitigate command injection in `system`
sp.disable_function.function("system").param("command").value_r("[$|;&`\\n]").drop();
```

Upon violation of a rule, you should see lines like this in your logs:

root@kitploit:~

```
[snuffleupagus][0.0.0.0][disabled_function][drop] The execution has been aborted in /var/www/index.php:2, because the return value (0) of the function 'strpos' matched a rule.
```

## Documentation

We've got a [comprehensive website](https://snuffleupagus.readthedocs.io/) with
all the documentation that you could possibly wish for. You can of course
[build it yourself](https://github.com/jvoisin/snuffleupagus/tree/main/doc).

## Thanks

Many thanks to:

* The [Suhosin project](https://suhosin.org) for being a **huge** source of inspiration
* [NBS System](https://www.nbs-system.com) for initially sponsoring the development
* [Suhosin-ng](https://github.com/sektioneins/suhosin-ng) for their
  [experimentations](https://github.com/sektioneins/suhosin-ng/wiki/News)
  and [contributions](https://github.com/jvoisin/snuffleupagus/commits?author=bef),
  as well as [NLNet](https://nlnet.nl/project/Suhosin-NG/) for sponsoring it
* All [our contributors](https://github.com/jvoisin/snuffleupagus/graphs/contributors)

[Read more](/en/tools/github/jvoisin/snuffleupagus?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Code Analysis](/en/categories/code-analysis)[Web Security](/en/categories/web-security)[Misconfiguration](/en/categories/misconfiguration)

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