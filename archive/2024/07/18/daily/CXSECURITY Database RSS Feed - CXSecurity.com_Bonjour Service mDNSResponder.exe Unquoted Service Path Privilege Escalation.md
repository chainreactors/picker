---
title: Bonjour Service mDNSResponder.exe Unquoted Service Path Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2024070037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-18
fetch_date: 2025-10-06T17:38:26.324269
---

# Bonjour Service mDNSResponder.exe Unquoted Service Path Privilege Escalation

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
|  |  | |  | | --- | | **Bonjour Service mDNSResponder.exe Unquoted Service Path Privilege Escalation** **2024.07.17**  Credit:  **[bios](https://cxsecurity.com/author/bios/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Bonjour Service - 'mDNSResponder.exe' Unquoted Service
Path
# Discovery by: bios
# Discovery Date: 2024-15-07
# Vendor Homepage: https://developer.apple.com/bonjour/
# Tested Version: 3,0,0,10
# Vulnerability Type: Unquoted Service Path
# Tested on OS: Microsoft Windows 10 Home
# Step to discover Unquoted Service Path:
C:\>wmic service get name,displayname,pathname,startmode |findstr /i "auto"
|findstr /i /v "c:\windows\\" |findstr /i /v """
Bonjour Service
Bonjour Service
C:\Program Files\Blizzard\Bonjour Service\mDNSResponder.exe
Auto
C:\>systeminfo
Host Name: DESKTOP-HFBJOBG
OS Name: Microsoft Windows 10 Home
OS Version: 10.0.19045 N/A Build 19045
PS C:\Program Files\Blizzard\Bonjour Service> powershell -command
"(Get-Command .\mDNSResponder.exe).FileVersionInfo.FileVersion"
>>
3,0,0,10
#Exploit:
There is an Unquoted Service Path in Bonjour Services (mDNSResponder.exe) .
This may allow an authorized local user to insert arbitrary code into the
unquoted service path and escalate privileges.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024070037)

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