---
title: SEC Consult SA-20250422-0:: Local Privilege Escalation via DLL Search Order Hijacking
url: https://seclists.org/fulldisclosure/2025/May/17
source: Full Disclosure
date: 2025-05-18
fetch_date: 2025-10-06T22:27:42.314972
---

# SEC Consult SA-20250422-0:: Local Privilege Escalation via DLL Search Order Hijacking

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250422-0:: Local Privilege Escalation via DLL Search Order Hijacking

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 8 May 2025 08:39:24 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250422-0 >
=======================================================================
              title: Local Privilege Escalation via DLL Search Order Hijacking
            product: Ivanti Endpoint Manager Security Scan (Vulscan) Self
Update
 vulnerable version: EPM 2022 SU6 and previous, EPM 2024
      fixed version: EPM 2022 SU7 and EPM 2024 SU1
         CVE number: CVE-2025-22458
             impact: High
           homepage: https://www.ivanti.com/
              found: 2025-02-07
                 by: Paul Serban (Eviden)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"EPM Patch and Compliance Manager uses an auto update feature in order to make
sure that all vulnerability scanning files are up to date with the core
server.
This ensures compatibility between the files and the latest definitions as
well
as compatibility with the files on the core.  The Security Scan (Vulscan) is
what does the update."

Source:
https://forums.ivanti.com/s/article/About-Patch-Manager-Self-Update?language=en_US

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

Vulnerability overview/description:
-----------------------------------
1) DLL Search Order Hijacking (CVE-2025-22458)
The EPM Security Scan (Vulscan) Self Update is vulnerable to DLL Hijacking.
When it is installed on a client machine, by default, it creates a scheduled
task as SYSTEM that when run, tries to load non-existent ZIP files from
ProgramData. A malicious DLL can be inserted into one of the ZIP files which
will be unzipped to and loaded from Program Files (x86) allowing malicious
actors with low privileges to escalate to SYSTEM and due to the recurrence
of the scheduled task, also gain persistence.

Proof of concept:
-----------------
1) DLL Search Order Hijacking (CVE-2025-22458)
In the screenshot below the scheduled task "LANDESK Agent Health Bootstrap
Task"
is seen to be running as SYSTEM on the client machine.

<01_scheduled_task_as_system.png>

By default it is set to run daily at 9 PM.

<02_scheduled_task_recurrence.png>

This scheduled task runs the vulscan.exe binary that scans to make sure
that all vulnerability scanning files are up to date with the core Ivanti
server.

<03_scheduled_task_command.png>

Every scan run by this agent saves a log in the following location:

C:\ProgramData\LANDesk\Log\vulscan.log

The ProgramData folder allows any authenticated user to read and write
into it. While reading the log, the following lines indicate that some
files are not found.

Thu, 10 Feb 2025 21:00:19 Info: Core did not find file
RebootBehavior_Apply.zip
Thu, 10 Feb 2025 21:00:19 Last status: File not found on core
Thu, 10 Feb 2025 21:00:19 Info: Core did not find file
AlertSettingsBehavior_Apply.zip
Thu, 10 Feb 2025 21:00:19 Last status: File not found on core
Thu, 10 Feb 2025 21:00:19 Info: Core did not find file
InventorySettingsBehavior_Apply.zip
Thu, 10 Feb 2025 21:00:19 Last status: File not found on core
Thu, 10 Feb 2025 21:00:19 Info: Core did not find file
ClientConnectivityBehavior_Apply.zip
Thu, 10 Feb 2025 21:00:19 Last status: File not found on core
Thu, 10 Feb 2025 21:00:19 Info: Core did not find file
PortalManagerBehavior_Apply.zip
Thu, 10 Feb 2025 21:00:19 Last status: File not found on core
<snipped for brevity>
Thu, 10 Feb 2025 21:00:19 GetFileHash: could not find
"C:\ProgramData\vulScan\RebootBehavior_Apply.zip"
Thu, 10 Feb 2025 21:00:19 GetFileHash: could not find
"C:\ProgramData\vulScan\AlertSettingsBehavior_Apply.zip"
Thu, 10 Feb 2025 21:00:19 GetFileHash: could not find
"C:\ProgramData\vulScan\InventorySettingsBehavior_Apply.zip"
Thu, 10 Feb 2025 21:00:19 GetFileHash: could not find
"C:\ProgramData\vulScan\ClientConnectivityBehavior_Apply.zip"
Thu, 10 Feb 2025 21:00:19 GetFileHash: could not find
"C:\ProgramData\vulScan\PortalManagerBehavior_Apply.zip"
Thu, 10 Feb 2025 21:00:19 Self update: files are up to date.

It looks like it is trying to find certain zip archives. It first
searches on the Core Ivanti server, then it looks in the ProgramData
folder. Since it can't find them in either location, it concludes
that it is up to date.

Further down into the log it can be seen that it tries to unzip the
same zip files from the ProgramData folder. It can't find them and
then loads DLL files from Program Files (x86). These DLL files have
the same name as the zip file.

Thu, 10 Feb 2025 21:00:20 Checking whether to unzip
'C:\ProgramData\vulScan\RebootBehavior_Apply.zip'.  Force: true
Thu, 10 Feb 2025 21:00:20 GetFileHash: could not find
"C:\ProgramData\vulScan\RebootBehavior_Apply.zip"
Thu, 10 Feb 2025 21:00:20 Loading applier dll: 'C:\Program Files
(x86)\LANDesk\LDClient\RebootBehavior_Apply.dll'
Thu, 10 Feb 2025 21:00:20 Check last error after load library.  Error: 126
Tue, 10 Feb 2025 21:00:36 Checking whether to unzip
'C:\ProgramData\vulScan\AlertSettingsBehavior_Apply.zip'.  Force: false
Tue, 10 Feb 2025 21:00:36 GetFileHash: could not find
"C:\ProgramData\vulScan\AlertSettingsBehavior_Apply.zip"
Tue, 10 Feb 2025 21:00:36 Loading applier dll: 'C:\Program Files
(x86)\LANDesk\LDClient\AlertSettingsBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:36 'PreApplyBehavior' is not in 'C:\Program Files
(x86)\LANDesk\LDClient\AlertSettingsBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:36 Calling 'ApplyBehavior' in 'C:\Program Files
(x86)\LANDesk\LDClient\AlertSettingsBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:36 Checking whether to unzip
'C:\ProgramData\vulScan\InventorySettingsBehavior_Apply.zip'.  Force: false
Tue, 10 Feb 2025 21:00:36 GetFileHash: could not find
"C:\ProgramData\vulScan\InventorySettingsBehavior_Apply.zip"
Tue, 10 Feb 2025 21:00:36 Loading applier dll: 'C:\Program Files
(x86)\LANDesk\LDClient\InventorySettingsBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:37 'PreApplyBehavior' is not in 'C:\Program Files
(x86)\LANDesk\LDClient\InventorySettingsBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:37 Calling 'ApplyBehavior' in 'C:\Program Files
(x86)\LANDesk\LDClient\InventorySettingsBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:38 Checking whether to unzip
'C:\ProgramData\vulScan\ClientConnectivityBehavior_Apply.zip'.  Force: false
Tue, 10 Feb 2025 21:00:38 GetFileHash: could not find
"C:\ProgramData\vulScan\ClientConnectivityBehavior_Apply.zip"
Tue, 10 Feb 2025 21:00:38 Loading applier dll: 'C:\Program Files
(x86)\LANDesk\LDClient\ClientConnectivityBehavior_Apply.dll'
Tue, 10 Feb 2025 21:00:38 Calling 'PreApplyBehavior' in 'C:\Program Files
(x86)\LANDesk\LDClient\ClientConnectivityBehavior_Apply.dll'
<snipped for brevity>
Wed, 10 Feb 2025 21:01:42 Checking whether to unzip
'C:\ProgramData\vulScan\PortalManagerBehavio...