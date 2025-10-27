---
title: Secure Web Gateway 10.2.11 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023010049
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-29
fetch_date: 2025-10-04T05:06:39.631921
---

# Secure Web Gateway 10.2.11 Cross Site Scripting

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Secure Web Gateway 10.2.11 Cross Site Scripting** **2023.01.28**  Credit:  **[RedTeam](https://cxsecurity.com/author/RedTeam/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0214](https://cxsecurity.com/cveshow/CVE-2023-0214/ "Click to see CVE-2023-0214")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

RedTeam Pentesting identified a vulnerability which allows attackers to
craft URLs to any third-party website that result in arbitrary content
to be injected into the response when accessed through the Secure Web
Gateway. While it is possible to inject arbitrary content types, the
primary risk arises from JavaScript code allowing for cross-site
scripting.
Details
=======
Product: Secure Web Gateway
Affected Versions: 10.2.11, potentially other versions
Fixed Versions: 10.2.17, 11.2.6, 12.0.1
Vulnerability Type: Cross-Site Scripting
Security Risk: high
Vendor URL: https://www.skyhighsecurity.com/en-us/products/secure-web-gateway.html
Vendor Status: fixed version released
Advisory URL: https://www.redteam-pentesting.de/advisories/rt-sa-2022-002
Advisory Status: published
CVE: CVE-2023-0214
CVE URL: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0214
Introduction
============
"Skyhigh Security Secure Web Gateway (SWG) is the intelligent,
cloud-native web security solution that connects and secures your
workforce from malicious websites and cloud apps—from anywhere, any
application, and any device."
(from the vendor's homepage)
More Details
============
The Secure Web Gateway's (SWG) block page, which is displayed when a
request or response is blocked by a rule, can contain static files such
as images, stylesheets or JavaScript code. These files are embedded
using special URL paths. Consider the following excerpt of a block page:
------------------------------------------------------------------------
<html>
<!-- FileName: index.html
Language: [en]
-->
<!--Head-->
<head>
<meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
<meta http-equiv="X-UA-Compatible" content="IE=7" />
<title>McAfee Web Gateway - Notification</title>
<script src="/mwg-internal/de5fs23hu73ds/files/javascript/sw.js" type="text/javascript" ></script>
<link rel="stylesheet" href="/mwg-internal/de5fs23hu73ds/files/default/stylesheet.css" />
</head>
------------------------------------------------------------------------
Static content is loaded from URL paths prefixed with
"/mwg-internal/de5fs23hu73ds/". It was discovered that paths with this
prefix are intercepted and directly handled by the SWG no matter on
which domain they are accessed. While the prefix can be configured in
the SWG, attackers can also obtain it using another currently
undisclosed vulnerability.
By reverse engineering the file "libSsos.so" and analysing JavaScript
code, it was possible to derive the API of the "Ssos" plugin's
"SetLoginToken" action. Through the following call using the
command-line HTTP client curl, the behaviour of the plugin was further
analysed:
------------------------------------------------------------------------
$ curl --proxy http://192.168.1.1:8080 -i 'https://gateway.example.com/mwg-internal/de5fs23hu73ds/plugin?target=Ssos&action=SetLoginToken&v=v&c=c&p=p'
HTTP/1.0 200 OK
P3P: p
Connection: Keep-Alive
Set-Cookie: MwgSso=v; Path=/; Max-Age=240;
Content-Type: application/javascript
Content-Length: 2
X-Frame-Options: deny
c;
------------------------------------------------------------------------
The response embeds the values of the three URL parameters "v", "c" and
"p". The value for "p" is embedded as value of the "P3P" header, the
value of "c" as the response body and the value of "v" as the value
of the cookie "MwgSso".
It is also possible to include newline or carriage return characters in
the parameter value which are not encoded in the output. Consequently,
if the value of the parameter "p" contains a line break, arbitrary
headers can be injected. If two line breaks follow, an arbitrary body
can be injected. If a suitable "Content-Length" header is injected, the
remaining headers and body of the original response will be ignored by
the browser. This means that apart from the initial "P3P" header, an
arbitrary response can be generated. For example, a page containing
JavaScript code could be returned, resulting in a cross-site scripting
attack.
Consequently, attackers can construct URL paths that can be appended to
any domain and cause an arbitrary response to be returned if the URL is
accessed through the SWG. This could be exploited by distributing such
URLs or even by offering a website which performs an automatic redirect
to any other website using such a URL. As a result, the SWG exposes its
users to self-induced cross-site scripting vulnerabilities in any
website.
Proof of Concept
================
In the following request, the "p" parameter is used to inject suitable
"Content-Type" and "Content-Length" headers, as well as an arbitrary
HTML response body.
------------------------------------------------------------------------
$ curl --proxy http://192.168.1.1:8080 'https://gateway.example.com/mwg-internal/de5fs23hu73ds/plugin?target=Ssos&action=SetLoginToken&v=v&c=c&p=p%0aContent-Type: text/html%0aContent-Length: 27%0a%0a<h1>RedTeam Pentesting</h1>'
HTTP/1.0 200 OK
P3P: p
Content-Type: text/html
Content-Length: 27
<h1>RedTeam Pentesting</h1>
------------------------------------------------------------------------
As mentioned above, the HTTP response body could also include JavaScript
code designed to interact with the domain specified in the URL resulting
in a cross-site scripting vulnerability.
Workaround
==========
None.
Fix
===
According to the vendor, the vulnerability is mitigated in versions
10.2.17, 11.2.6 and 12.0.1 of the Secure Web Gateway. This was not
verified by RedTeam Pentesting GmbH. The vendor's security bulletin can
be found at the following URL:
https://kcm.trellix.com/corporate/index?page=content&id=SB10393
Security Risk
=============
The vulnerability could be used to perform cross-site scripting attacks
...