---
title: PHP 8.5.7 `levenshtein()` signed-integer overflow
url: https://seclists.org/fulldisclosure/2026/Jun/14
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:01.710387
---

# PHP 8.5.7 `levenshtein()` signed-integer overflow

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# PHP 8.5.7 `levenshtein()` signed-integer overflow

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Fri, 19 Jun 2026 09:56:09 +0330

---

```
# PHP 8.5.7 `levenshtein()` signed-integer overflow

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-06-18
**Advisory:** https://fereidani.com/php-857-levenshtein-signed-integer-overflow
**Contact:** https://fereidani.com/contact

## Description

The `levenshtein()` function calculates the Levenshtein distance
between two strings, optionally accepting custom costs for insertion,
replacement, and deletion operations. In PHP 8.5.7, the implementation
lacks proper bounds checking for these cost parameters. When
exceptionally large values (such as `PHP_INT_MAX`) are provided, the
arithmetic operations within the `reference_levdist()` function in
`ext/standard/levenshtein.c` result in a signed-integer overflow. This
triggers undefined behavior in C and causes the function to return a
negative distance, which is mathematically invalid.

## Proof of concept

```php
<?php
/*
 * levenshtein() signed-integer overflow
 * File:  ext/standard/levenshtein.c  reference_levdist()  lines 47, 50, 53-58
 *
 * The user-supplied costs (cost_ins / cost_rep / cost_del, all zend_long) are
 * added with NO overflow check, e.g.:
 *     p1[i2]  = i2 * cost_ins;        // line 47
 *     p2[0]   = p1[0] + cost_del;     // line 50
 *     c1      = p1[i2 + 1] + cost_del;// line 54   <-- PHP_INT_MAX +
PHP_INT_MAX
 *     c2      = p2[i2] + cost_ins;    // line 58
 *
 * Result: signed overflow (undefined behaviour in C) producing a
 * NEGATIVE edit distance, a value that is mathematically impossible.
 */
var_dump(levenshtein('a',   'b',   PHP_INT_MAX, PHP_INT_MAX,
PHP_INT_MAX)); // int(-2)  (should be PHP_INT_MAX)
var_dump(levenshtein('a',   'abc', PHP_INT_MAX, PHP_INT_MAX,
PHP_INT_MAX)); // int(-4)
var_dump(levenshtein('a',   'b',   PHP_INT_MAX, 0,
PHP_INT_MAX)); // int(-2)
echo "All three distances are negative => signed overflow (expected >= 0).\n";
```

## Impact

The primary risk associated with this vulnerability is an application
logic flaw. Applications that rely on the `levenshtein()` function to
determine string similarity or calculate distance metrics might fail
to handle negative returns properly (for instance, treating a negative
number as `< threshold`). This can result in unexpected behavior,
incorrect data processing, or bypasses in business logic. Since it
involves integer overflow producing a negative result rather than a
memory corruption issue, the scope is generally limited to logic
disruption rather than arbitrary code execution.

## Solution

To effectively address this issue, bounds checking should be
implemented either on the cost parameters at the start of the
function, or during intermediate calculations. Utilizing safe
arithmetic macros provided by the Zend Engine can prevent the integer
overflow constraints from being violated:

```c
// Example: Adding overflow safeguards in ext/standard/levenshtein.c
if (UNEXPECTED(ZEND_SIGNED_ADD_OVERFLOWS(p1[i2 + 1], cost_del))) {
    php_error_docref(NULL, E_WARNING, "Levenshtein distance
calculation caused an integer overflow");
    // Handle error, e.g., return -1 or cap
}
```
An alternative and proactive measure is to restrict the inputs for
`cost_ins`, `cost_rep`, and `cost_del` before computing the distance,
ensuring that they wouldn't exceed `ZEND_LONG_MAX` when scaled
relative to the strings' lengths.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **PHP 8.5.7 `levenshtein()` signed-integer overflow** *Khashayar Fereidani (Jun 20)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")