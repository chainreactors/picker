---
title: Windows Registry Forensics Cheat Sheet 2025
url: https://www.cybertriage.com/blog/windows-registry-forensics-cheat-sheet-2025/
source: Instapaper: Unread
date: 2025-06-12
fetch_date: 2025-10-06T22:56:12.039522
---

# Windows Registry Forensics Cheat Sheet 2025

[Skip to content](#primary)

[cyber-triage-logo](https://www.cybertriage.com/)

Primary Menu

* [Platform](https://www.cybertriage.com/features/)
  + - * [Workflow](https://www.cybertriage.com/how-cyber-triage-works/)
      * [Benefits](https://www.cybertriage.com/benefits/)
      * [Why Cyber Triage](https://www.cybertriage.com/why-cyber-triage-digital-forensics-tool/)
      * [Compare Versions](https://www.cybertriage.com/features/versions/)
      * [Cyber Triage for Teams](https://www.cybertriage.com/team-version/)
    - * #### Key Features
      * [The Collector](https://www.cybertriage.com/cyber-triage-dfir-collector/)
      * [Artifact Scoring](https://www.cybertriage.com/features/prioritize-with-cyber-triage/)
      * [Malware Detection](https://www.cybertriage.com/malware-forensics-tool/)
      * [Ransomware Detection](https://www.cybertriage.com/features/ransomware/)
      * [Server API](https://www.cybertriage.com/team-rest-api/)
    - * #### EDR
      * [EDR + Cyber Triage](https://www.cybertriage.com/edr/)
      * [EDR Evasion 101](https://www.cybertriage.com/blog/how-edr-evasion-works-attacker-tactics/)
    - * #### Integrations
      * [EDR Powershell Script](https://www.cybertriage.com/deployer-script/)
      * [Integrated Capabilities](https://www.cybertriage.com/features/integrations/)
      * [Malware Scanner for Autopsy](https://www.cybertriage.com/autopsy-malware-module/)
* [Use Cases](https://www.cybertriage.com/benefits/)
  + [SOC Endpoint Investigation](https://www.cybertriage.com/soc-alert-investigation/)
  + [Consultants](https://www.cybertriage.com/benefits/consultants/)
  + [SOC DFIR Teams](https://www.cybertriage.com/benefits/internal-incident-responders/)
  + [Law Enforcement - Intrusions](https://www.cybertriage.com/benefits/law-enforcement/)
  + [Law Enforcement - ICAC (Trojan Defense)](https://www.cybertriage.com/detect-remote-access-for-icac-and-trojan-defense/)
* [Pricing](https://www.cybertriage.com/pricing/)
  + [Buy Cyber Triage](https://www.cybertriage.com/pricing/)
  + [Buy Malware Scanning Boosts](https://www.cybertriage.com/boost-checkout/)
  + [Buy Autopsy Malware Scanner Module](https://www.cybertriage.com/autopsy-checkout/)
  + [Buy Rapid Endpoint Triage Service](https://www.sleuthkitlabs.com/rapid_checkout/)
* [Resources](https://www.cybertriage.com/online-response-training/)
  + - * [Blog](https://www.cybertriage.com/blog/)
      * [Webinars](https://www.cybertriage.com/events/)
      * [Videos](https://www.cybertriage.com/videos/)
      * [Intro to DFIR Blog Series](https://www.cybertriage.com/intro-to-cyber-incident-response/)
      * [Cyber RespondIR Newsletter](https://www.cybertriage.com/sign-up-for-the-cyber-respondir/)
    - * [Rapid Endpoint Triage Service](https://www.cybertriage.com/services/#rapid)
      * [Training](https://www.cybertriage.com/training/)
    - * #### Recent Releases
      * [3.15 (Defender Telemetry, Access Control, IRIS)](https://www.cybertriage.com/blog/cyber-triage-3-15-import-defender-telemetry-more-soc-features/)
      * [3.14 (Tactics, Hayabusa, Baselining)](https://www.cybertriage.com/blog/3-14-release-brings-new-uis-hayabusa-baselining-and-much-more/)
      * [3.13 (MemProcFS, S3 Reading)](https://www.cybertriage.com/blog/releases/3-13-adds-memprocfs-and-extends-the-s3-and-recorded-future-sandbox-integrations/)
      * [3.12 (Data Exfil, USB, Validation)](https://www.cybertriage.com/blog/releases/3-12-adds-data-exfiltration-detection-usb-devices-and-easier-validation/)
* [About](https://www.cybertriage.com/about/)
  + [About](https://www.cybertriage.com/about/)
  + [Team](https://www.cybertriage.com/team/)
  + [Contact](https://www.cybertriage.com/contact/)
* [Start Free Trial](https://www.cybertriage.com/download-eval/)

# Windows Registry Forensics Cheat Sheet 2025

* June 2, 2025
* **[Chris Ray](https://www.cybertriage.com/team/chris-ray/)**

Save. This. Post. Our expert staff has compiled an up-to-date and comprehensive **Windows Registry forensics cheat sheet**, and it might be just what you need for your next investigation.

**Jump to a section…**
[What Is a Windows Registry Forensics Cheat Sheet?](#What Is a Windows Registry Forensics Cheat Sheet?)
[Core Windows Registry Hives and Their Forensic Value](#Core Windows Registry Hives and Their Forensic Value)
[Key Registry Artifacts by Forensic Purpose](#Key Registry Artifacts by Forensic Purpose)
[Recommended Tools for Registry Analysis](#Recommended Tools for Registry Analysis)
[Windows Forensics Investigation Tips](#Windows Forensics Investigation Tips)

## **What Is a Windows Registry Forensics Cheat Sheet?**

This document is an overview of key components of Windows Registry forensics, **including:**

* Registry hives
* Registry artifacts
* Registry analysis tools
* Registry forensics tips

If you’d like to us to add something to our Windows forensics cheat sheet, [please contact us](https://www.cybertriage.com/contact/).

## **Core Windows Registry Hives and Their Forensic Value**

Each Windows registry hive is a file that stores **config settings** and **system/user data**, and these are essential sources in forensic investigations.

As DFIR expert [Chris Ray](https://www.linkedin.com/in/chris-ray-88175a21/) explains, “Windows Registry is a key source of forensic data because of its function within the system. It’s used as a repository to store system and application settings, configurations, preferences, usage telemetry, and more.”

**Breakdown of each:**

| **NTUSER.DAT** | |
| --- | --- |
| **Location** | ``` C:Users<username>NTUSER.DAT ``` |
| **Loaded under** | ``` HKEY_USERS<SID> ``` |
| **Forensic value** | Tracks user-specific settings and activity. |
| **Contains** | * [**UserAssist**](https://www.cybertriage.com/blog/userassist-forensics-2025/): Tracks program execution for apps with GUI components or app/LNK files launched via the Windows UI. * [**RunMRU**](https://www.cybertriage.com/blog/how-to-investigate-runmru-2025/): Tracks program execution for commands run via Windows run dialog. * [**OpenSaveMRU**](https://www.cybertriage.com/artifact/windows-opensave-mru-artifact/): Tracks files opened/saved via Windows Open/Save dialog. * [**OfficeMRU**](https://www.cybertriage.com/artifact/office-mru-registry/): Tracks most recently used files for each Office app. Ex: Word, Excel, PowerPoint. * [**LastVistedMRU**](https://www.forensafe.com/blogs/lastvisitedmru.html): Tracks applications that have used the Windows Open/Save dialog, along with last location opened for each app. * [**RecentDocs**](https://www.forensafe.com/blogs/recentdocs.html): Tracks recently accessed files and folders opened. Used to populate various “recent” tables in Windows. * [**WordWheelQuery**](https://www.4n6post.com/2023/02/registry-wordwheelquery.html): Tracks an ordered list of search strings put into Windows File Explorer search box. * [**TypedPaths**](https://forensafe.com/blogs/typedpaths.html): Tracks paths typed into File Explorer path bar directly by a user * [**ShellBags**](https://www.cybertriage.com/blog/shellbags-forensic-analysis-2025/): Includes UNC path based data. Can show evidence of users opening folders. * [**MountPoints2**](https://docs.velociraptor.app/artifact_references/pages/windows.registry.mountpoints2/): Tracks mounted USB and network shares. * [**User-specific installed apps**](https://github.com/keydet89/RegRipper3.0/blob/bdf7ac2500a41319479846fe07202b7e8a61ca1f/plugins/uninstall.pl#L4): Tracks what apps have been installed for the user instead of system-wide. * **User-specific Autorun entries**: User-specific persistence in the Registry. Ex: Run/RunOnce keys. |

| **UsrClass.dat** | |
| --- | --- |
| **Location** | ``` C:Users<username>AppDataLocalMicrosoftWindowsUsrClass.dat ``` |
| **Loaded under** | ``` HKEY_USERS<SID>_Classes ``` |
| **Forensic value** | Mainly stores user-specific shell settings and mappings. |
| **Contains** | * [**ShellBag**](https://www.cybertriage.com/blog/shellbags-for...