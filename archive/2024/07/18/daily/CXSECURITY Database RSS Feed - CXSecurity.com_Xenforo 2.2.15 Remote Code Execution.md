---
title: Xenforo 2.2.15 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024070035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-18
fetch_date: 2025-10-06T17:38:29.314581
---

# Xenforo 2.2.15 Remote Code Execution

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
|  |  | |  | | --- | | **Xenforo 2.2.15 Remote Code Execution** **2024.07.17**  Credit:  **[EgiX](https://cxsecurity.com/author/EgiX/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-38458](https://cxsecurity.com/cveshow/CVE-2024-38458/ "Click to see CVE-2024-38458")**  CWE: **N/A** | |

-----------------------------------------------------------------------
XenForo <= 2.2.15 (Template System) Remote Code Execution Vulnerability
-----------------------------------------------------------------------
[-] Software Link:
https://xenforo.com
[-] Affected Versions:
Version 2.2.15 and prior versions.
[-] Vulnerability Description:
XenForo implements a template system which gives complete control over
the layout of XenForo pages. Through these templates, it might be
possible to call certain "callback methods", however there is a sort
of "sandbox" which allows to solely call read-only methods: a method
is to be considered read-only when it begins with one of the allowed
prefixes, such as "get" or "filter". Malicious users might be able to
bypass this "sandbox" by abusing the getRepository() method from the
XF\Mvc\Entity\Manager class in order to get an instance object of the
XF\Util\Arr class, and from there they can abuse its filterRecursive()
static method in order to execute arbitrary callbacks or functions
(internally, this method calls the array\_filter() PHP function with an
attacker-controlled "callback" parameter). As such, this can be
exploited to e.g. execute arbitrary OS commands by using a payload
like the following within a template, which will try to execute the
passthru() PHP function passing to it the string "whoami" as argument,
potentially resulting in the execution of the "whoami" command on the
web server:
{{ $xf.app.em.getRepository('XF\Util\Arr').filterRecursive(['whoami'],'passthru')
}}
Successful exploitation of this vulnerability requires an account with
permissions to administer styles or widgets.
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
assigned the name CVE-2024-38458 to this vulnerability.
[-] Credits:
Vulnerability discovered by Egidio Romano.
[-] Other References:
https://xenforo.com/community/threads/222133
https://ssd-disclosure.com/ssd-advisory-xenforo-rce-via-csrf/
[-] Original Advisory:
http://karmainsecurity.com/KIS-2024-06

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024070035)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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