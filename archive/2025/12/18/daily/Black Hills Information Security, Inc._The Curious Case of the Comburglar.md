---
title: The Curious Case of the Comburglar
url: https://www.blackhillsinfosec.com/the-curious-case-of-the-comburglar/
source: Black Hills Information Security, Inc.
date: 2025-12-18
fetch_date: 2025-12-19T03:22:27.661140
---

# The Curious Case of the Comburglar

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [OLD](https://www.blackhillsinfosec.com/backdoorsandbreachesold/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

18
Dec
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Troy Wojewoda](https://www.blackhillsinfosec.com/category/author/troy-wojewoda/)

# [The Curious Case of the Comburglar](https://www.blackhillsinfosec.com/the-curious-case-of-the-comburglar/)

By [Troy Wojewoda](https://www.blackhillsinfosec.com/category/author/troy-wojewoda/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/12/Blog-Header-The-Curious-Case-of-the-Comburglar-1024x576.png)

---

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/12/ComBurglar-1024x619.jpg)

During a recent Breach Assessment engagement, BHIS discovered a highly stealthy and persistent intrusion technique utilized by a threat actor to maintain Command-and-Control (C2) within the client’s network. The attacker had modified Scheduled Tasks in the environment to use a ***ComHandler*** to create and execute a method within a registered Component Object Model *(COM)*[1](#52311159-2584-4cd7-986a-5e9ebf0dfa71), leveraging custom surrogate DLL files for code execution. The attacker particularly targeted tasks named *User\_Feed\_Synchronization-{GUID}* to carry out this technique. BHIS currently tracks this activity under the moniker *UKC-1230*.

This technique allowed the threat actor to remain persistent in the environment for at least seven months. BHIS also found evidence in the wild that indicates the attacker and associated threat activity have been in use for over a year, with related artifacts dating back nearly two years, as early as January 31, 2024.

## **Investigative Discoveries**

During the collection phase of the Breach Assessment, BHIS was made aware of an alert that had fired in the customer’s SOC – an alert on a file hash from an incident that occurred a month prior to the engagement with BHIS.

SHA256 Hash: `407d179f920342312dd526abc8a194b2620d0b19a95032dd36eeb70ec3bf5d65`

Filename: `C:\ProgramData\Microsoft\Windows\{0759c13d-5d0f-4513-8707-98a6cc3536d5}.dll`

BHIS performed a triage collection and analyzed the system. Pivoting on the *GUID* value associated with the DLL name, a scheduled task named *User\_Feed\_Synchronization-{0759c13d-5d0f-4513-8707-98a6cc3536d5}* was uncovered. BHIS inspected the task’s contents which revealed the use of a ***ComHandler*** to execute code.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/12/User_Feed_task-malicious.png)

**Malicious ComHandler Setting – User\_Feed\_Synchronization Scheduled Task**

This configuration setting was highly suspicious because although ***ComHandler*** activity can be common in certain scheduled tasks on Windows OS’s, it is atypical for tasks of *User\_Feed\_Synchronization-{GUID}*.

For comparative purposes, a normal/benign *User\_Feed\_Synchronization-{GUID}*configuration references the Windows executable file, `msfeedsync.exe` at `C:\WINDOWS\system32\msfeedsync.exe` This scheduled task type is a legacy carryover from earlier Windows OS’s and is still found on supported versions of the OS today.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/12/User_Feed_task-benign.png)

**Normal/Benign Command Setting in User\_Feed\_Synchronization Scheduled Task**

## **Following the ComHandler Action**

A *COM* object is typically an in-process *COM* server (a surrogate DLL, as determined by the *ClassId* lookup in the Windows Registry); it cannot run on its own and requires a host process to execute its code. This host process is `dllhost.exe`, also known as the *COM Surrogate* process, and is a necessary component of the Microsoft Windows OS. It acts as a generic host process for surrogate DLLs.

Knowing the *ClassId* value, the following registry path can be used to determine where on disk the associated DLL resides:

`Registry::HKEY_CLASSES_ROOT\CLSID\{<ClassId-value>}\InprocServer32`
The following PowerShell command was used during the Breach Assessment to query the registry key’s value at
`Registry::HKEY_CLASSES_ROOT\CLSID\{0759c13d-5d0f-4513-8707-98a6cc3536d5}\InprocServer32`

|  |
| --- |
| `Get-ItemProperty -Path 'Registry::HKEY_CLASSES_ROOT\CLSID\{0759c13d-5d0f-4513-8707-98a6cc3536d5}\InprocServer32’    (default)    : C:\ProgramData\Microsoft\Windows\{0759c13d-5d0f-4513-8707-98a6cc3536d5}.dll` |

The default value of the *\InprocServer32*key pointed to the attacker attributed DLL file at`C:\ProgramData\Microsoft\Windows\{0759c13d-5d0f-4513-8707-98a6cc3536d5}.dll`

BHIS used the following yara rule to scan the environment which uncovered several additional compromised hosts.

|  |
| --- |
| `rule Detect_COMHandler_ClassId_GUID  {      meta:          description = "Detects COM handler ClassId with any GUID inside XML scheduled task files" ...