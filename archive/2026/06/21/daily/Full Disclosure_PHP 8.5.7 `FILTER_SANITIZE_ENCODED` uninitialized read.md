---
title: PHP 8.5.7 `FILTER_SANITIZE_ENCODED` uninitialized read
url: https://seclists.org/fulldisclosure/2026/Jun/11
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:02.533795
---

# PHP 8.5.7 `FILTER_SANITIZE_ENCODED` uninitialized read

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# PHP 8.5.7 `FILTER\_SANITIZE\_ENCODED` uninitialized read

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Fri, 19 Jun 2026 09:52:32 +0330

---

```
# PHP 8.5.7 `FILTER_SANITIZE_ENCODED` uninitialized read

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-06-18
**Advisory:** https://fereidani.com/php-857-filtersanitizeencoded-uninitialized-read
**Contact:** https://fereidani.com/contact

## Description

In `ext/filter/sanitizing_filters.c`, the `php_filter_encode_url`
function leaves the `255`th byte (`0xFF`) of a transient array
uninitialized. An array of 256 bytes is populated using `memset(tmp,
1, sizeof(tmp) - 1)`, resulting in `tmp[255]` remaining uninitialized.
When `FILTER_SANITIZE_ENCODED` is applied, this array acts as a lookup
table to determine whether an input byte should be percent-encoded.
Consequently, whether the byte `0xFF` is encoded or left as-is depends
on whatever value happened to be on the stack.

## Proof of concept

```php
<?php
/*
 * FILTER_SANITIZE_ENCODED uninitialized read
(ext/filter/sanitizing_filters.c:73).
 *
 * php_filter_encode_url() does:
 *     unsigned char tmp[256];
 *     memset(tmp, 1, sizeof(tmp) - 1);   // sets tmp[0..254] = 1,
leaves tmp[255] UNINIT
 *     ...
 *     if (tmp[*s]) { percent-encode } else { keep }
 *
 * So byte 0xFF (index 255) is read UNINITIALIZED: whether it is percent-encoded
 * depends on whatever was on the stack. Every other byte is encoded
 * deterministically. Effect: inconsistent URL-encoding of 0xFF (low severity;
 * no crash / no memory corruption, just UB + nondeterministic sanitizing).
 *
 * Run:  php poc.php
 *   expect: 0xFF kept RAW (ff...) while 0xFE is correctly percent-encoded (%FE)
 */
$out = filter_var("\xff\xfeabc", FILTER_SANITIZE_ENCODED);
echo "in : ", bin2hex("\xff\xfeabc"), "\n";
echo "out: ", bin2hex($out), "\n";
echo "0xFF was kept raw and 0xFE was percent-encoded => tmp[255] read
uninitialized.\n";
```

Running the script results in:

```bash
in : fffe616263
out: ff254645616263
0xFF was kept raw and 0xFE was percent-encoded => tmp[255] read uninitialized.
```

## Impact

The impact is low. No crashes or memory corruption can occur as a
result of this bug. The sole impact is nondeterministic sanitizing of
the `0xFF` byte, which leads to inconsistent URL-encoding based on
uninitialized stack data unless it smartly gets used among other
vulnerabilities in a chain.

## Solution

Replace `sizeof(tmp) - 1` with `sizeof(tmp)` in the `memset` call in
`ext/filter/sanitizing_filters.c` to fully initialize the lookup
table.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

### Current thread:

* **PHP 8.5.7 `FILTER\_SANITIZE\_ENCODED` uninitialized read** *Khashayar Fereidani (Jun 20)*

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