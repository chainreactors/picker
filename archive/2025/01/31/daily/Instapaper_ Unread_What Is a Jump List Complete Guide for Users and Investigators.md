---
title: What Is a Jump List Complete Guide for Users and Investigators
url: https://www.cybertriage.com/blog/what-is-a-jump-list/
source: Instapaper: Unread
date: 2025-01-31
fetch_date: 2025-10-06T20:15:19.462393
---

# What Is a Jump List Complete Guide for Users and Investigators

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

# What Is a Jump List?

* January 29, 2025

What is a jump list? The answer depends on who you are. For general users, they’re a way to access recently used files. For investigators, they’re a means to understand user behavior.

But no matter who you are, this definitive guide will help you utilize jump lists effectively for what you need.

**Jump to…**

[What Is a Jump List?](#What Is a Jump List 2?)
[What Is Jump List Cache?](#What Is Jump List Cache 2?)
[When Jump Lists Can Miss Data](#When Jump Lists Can Miss Data)
[How to Enable Jump Lists](#How to Enable Jump Lists)
[How to Disable Jump Lists](#How to Disable Jump Lists)
[How to Add Items to a Jump List](#How to Add Items to a Jump List)
[What Programs Use Jump Lists?](#What Programs Use Jump Lists?)
[Recommended Resources](#Recommended Resources)

## **What Is a Jump List?**

A jump list provides quick access to files, folders, and application-specific tasks used recently or frequently. It’s a Windows feature introduced in Windows 7 to improve productivity by streamlining access to frequently used resources. You can view a jump list for a given app through the Taskbar, Start menu, or keyboard shortcuts.

| **How to Access Jump Lists** | | |
| --- | --- | --- |
| [![Taskbar access image.](https://www.cybertriage.com/wp-content/uploads/2025/01/Taskbar_Access_Image-362x800.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Taskbar_Access_Image.png)Right-click the app icon in the taskbar to view the taskbar jump list. | [![Start menu access image.](https://www.cybertriage.com/wp-content/uploads/2025/01/Start_Menu_Access_Image-800x756.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Start_Menu_Access_Image.png)Look for the app in the Start menu. To view the jump list, right-click or hover over it. | [![Hotkey jump list access. ](https://www.cybertriage.com/wp-content/uploads/2025/01/Hotkey-Example-1-1.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Hotkey-Example-1-1.png)Use Win + Alt + [Taskbar Number] to view the Taskbar app’s jump list. |

| **What Jump Lists Show** | | |
| --- | --- | --- |
| [![Jump list example 1.](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Ex_1-367x800.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Ex_1.png) | [![Jump list example 2.](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Ex_2.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Ex_2.png) | [![Jump list example 3.](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Ex_3.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Ex_3.png) |
| Jump lists show recent or pinned items and shortcuts to common actions. | | |

Digital investigators analyze the user activity — including files accessed and timestamps — contained in jump lists.

|  |  |
| --- | --- |
| [![Cyber Triage jump list 1.](https://www.cybertriage.com/wp-content/uploads/2025/01/Cyber_Triage_Jumplist_1-800x377.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Cyber_Triage_Jumplist_1.png) | [![Cyber Triage jump list 2.](https://www.cybertriage.com/wp-content/uploads/2025/01/Cyber_Triage_Jumplist_2-800x611.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Cyber_Triage_Jumplist_2.png) |

This helps investigators build a digital timeline of files, folders, and websites a user has accessed over time.

**Note for Investigators**
We do not recommend that investigators focus on memorizing the differences among jump lists, Prefetch, MUICache, and other “Data Artifacts.” There are many types, and they get confusing. Instead, we suggest focusing on higher-level computing concepts during investigations. DFIR expert Brian Carrier: “You don’t care about jump lists. What you really want to know is which users accessed which resources at what time. This is a higher-level concept that cuts across multiple Data Artifact types. This is about all the ‘Data Accessed.’” To learn more about a modern approach to analyzing jump lists, read “[Jump List Forensics 2025](https://www.cybertriage.com/blog/jump-list-forensics-2025/).”

Cyber Triage is investigation software built to handle the details of data artifacts — like j...