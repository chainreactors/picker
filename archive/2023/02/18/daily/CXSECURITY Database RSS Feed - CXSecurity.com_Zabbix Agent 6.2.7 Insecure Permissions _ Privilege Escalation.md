---
title: Zabbix Agent 6.2.7 Insecure Permissions / Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-18
fetch_date: 2025-10-04T07:19:27.957874
---

# Zabbix Agent 6.2.7 Insecure Permissions / Privilege Escalation

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
|  |  | |  | | --- | | **Zabbix Agent 6.2.7 Insecure Permissions / Privilege Escalation** **2023.02.17**  Credit:  **[mmg](https://cxsecurity.com/author/mmg/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Zabbix agents - Insecure Permissions on non-default installation directory location
# Discovery by: mmg
# Discovery Date: 2023-01-23
# Vendor Homepage: https://www.zabbix.com/download\_agents
# Software Link Zabbix agent : https://cdn.zabbix.com/zabbix/binaries/stable/6.2/6.2.7/zabbix\_agent-6.2.7-windows-amd64-openssl.msi
# Software Link Zabbix agent 2 : https://cdn.zabbix.com/zabbix/binaries/stable/6.2/6.2.7/zabbix\_agent2-6.2.7-windows-amd64-openssl.msi
# Tested Version: Zabbix agent and Zabbix agent 2 (v6.2.6, v6.2.7 and older versions)
# Vulnerability Type: Local Privilege Escalation
# Tested on OS: Windows 10 Pro Version 22H2 (OS Build 19045.2486) x64 version
# CVSSv3 Vectors : https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
# CVE N/A
# Step to discover:
Go to Start and type powershell.
Enter the following command and press Enter:
Get-WmiObject win32\_service | ?{ $\_.Name -like '\*zabbix\*' -and $\_.Pathname -notlike "\*C:\Program Files\*"}| select Name,PathName
# Example of a vulnerable installation
Name PathName
---- --------
Zabbix Agent "C:\Software\Zabbix Agent\zabbix\_agentd.exe" --config "C:\Software\Zabbix Agent\zabbix\_agentd.conf"
Zabbix Agent 2 "D:\software\Zabbix Agent 2\zabbix\_agent2.exe" -c "D:\software\Zabbix Agent 2\zabbix\_agent2.conf" -f=false
# Exploit:
A vulnerability was found in Zabbix Agents on non-default installation directory location.
The Zabbix Agent executables have incorrect permissions, allowing a local unprivileged user to replace it
with a malicious file that will be executed with "LocalSystem" privileges which will result in complete
compromise of Confidentiality, Integrity and Availability.
# Timeline
Jan 23, 2023 - Reported to Zabbix
Feb 1, 2023 - Zabbix does not consider this a vulnerability
Feb 6, 2023 - Requested official approval to disclose it
Feb 8, 2023 - Zabbix agrees with public disclosure
Feb 13, 2023 - Public disclosure

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020030)

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