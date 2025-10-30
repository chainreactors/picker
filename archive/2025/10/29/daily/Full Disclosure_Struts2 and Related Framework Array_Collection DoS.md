---
title: Struts2 and Related Framework Array/Collection DoS
url: https://seclists.org/fulldisclosure/2025/Oct/22
source: Full Disclosure
date: 2025-10-29
fetch_date: 2025-10-30T03:13:01.372231
---

# Struts2 and Related Framework Array/Collection DoS

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# Struts2 and Related Framework Array/Collection DoS

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 26 Oct 2025 11:05:30 +0000

---

```
Struts2 has, since its inception and to today, contained a significant denial of service (DoS) vulnerability stemming
from how the Struts2 default deserialiser parses and deserialises arrays, collections (including maps), and related
objects.  Specifically, Struts2 and related frameworks allow attackers to specify indices and adhere to the
user-supplied indices such that attackers can make arbitrarily large data structures with extremely tiny requests.

For example, the Super Vulnerable Java Application (SVJA) - a free, open-source Java-based "web application" designed
to showcase this and other vulnerabilities and available at https://github.com/theronielanddaronpodcastshow/svja - has
a `/api/files` action (the corresponding code is at `src/main/java/local/rdps/svja/action/FilesAction.java`) that
accepts a Collection of FileVO objects.  Attackers can stuff the files variable, creating an arbitrarily large
collection by simply specifying an index:

Request:
GET /svja/api/files?fileName=%2fetc%2fpasswd&files%5b0%5d.file=%2fetc%2fpasswd&files%5b100%5d.file=%2fetc%2fgroups
HTTP/1.1
Host: 127.0.0.1:8080
Cookie: svjatoken=mgwaZrNJsoKPMjvyB4pA7gf08NYWA7g1VT4K

Response:
HTTP/1.1 200
Cache-Control: no-cache
Expires: 0
Pragma: No-cache
Content-Type: application/json;charset=UTF-8
Content-Language: en-GB
Content-Length: 12645
Date: Sun, 26 Oct 2025 10:40:39 GMT
Keep-Alive: timeout=20
Connection: keep-alive

{"file": {"contents": "cm<<REDACTED>>", "file": "/etc/passwd", "fileSize": 2943, "fullPath": "/etc/passwd"},
"fileName": "/etc/passwd", "files": [{"contents": "cm<<REDACTED>>", "file": "/etc/passwd", "fileSize": 2943,
"fullPath": "/etc/passwd"}, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
null, null, null, null, {"contents": "cm<<REDACTED>>", "file": "/etc/passwd", "fileSize": 2943, "fullPath":
"/etc/passwd"}], "mayCreate": true, "mayDestroy": false, "mayIndex": true, "mayPatch": false, "mayShow": true,
"mayUpdate": true}

Importantly, the attack specifies two indices - 0 and 100.  While some systems, to include Apache Struts, don't require
the first index to produce a collection of 101 objects (almost all of which are `null`), some attempt to mitigate this
vulnerability by taking the first index specified and using it as "0", then making all other indices relative to that
anchor point.  By doing both 0 and 100, the attack ensures that for such deserialisers, a collection of 101 objects is
created.

Attackers can leverage this part of the vulnerability to create arrays, collections, and related data structures of
such sizes that the information system runs out of memory, that the size exceeds the maximum allowed, causing the
application or even the server to crash.

A variation of this attack exists against most deserialisers, including those in which the attacker cannot specify the
index.  For example, most JSON deserialisers will, by default, accept `null` values, specifically deserialising into
the identified variable and setting it to `null`.  Attackers can create arbitrarily large collections and arrays by
simply stuffing the JSON array with null entries.  To take the above example, if, instead, the parameters are contained
within the body and formatted as JSON, the attack would look more like this:

{"fileName": "/etc/passwd", "files":
[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]}

The majority of deserialisers would then, by default, create a Collection composed of `n` `null`s, where `n` is the
number of `null` items in the JSON array and will do this even if it wouldn't otherwise deserialise a `null` (e.g., it
would not deserialise `"fileName": "null"` to set said variable to `null`, instead using the variable's default value).
 This means that while attacks are larger than the first attack presented - the one where indices can be specified (via
URL parameters, plaintext forms, multi-part forms, and URL-encoded forms, for example) - it is more certain to affect a
given deserialiser and can even be used against those that allow specifying indices.  Moreover, since most websites
allow large bodies, it becomes easy for attackers to create collections, arrays, and the like with thousands, hundreds
of thousands, millions, or greater `null` entities.  Even when only thousands can be created, attackers merely have to
make concurrent requests with said payload to achieve the same result - out of memory exceptions that crash the service.

Ultimately, so long as the deserialiser allows attackers to specify indices and honours said specification or allows
attackers to specify `null`s in data structures, the deserialiser is vulnerable to this attack.  This vulnerability is
known to affect a wide number of libraries, frameworks, and systems.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **Struts2 and Related Framework Array/Collection DoS** *Daniel Owens via Fulldisclosure (Oct 28)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclis...