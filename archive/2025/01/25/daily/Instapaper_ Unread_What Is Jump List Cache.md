---
title: What Is Jump List Cache
url: https://www.cybertriage.com/blog/what-is-jump-list-cache/
source: Instapaper: Unread
date: 2025-01-25
fetch_date: 2025-10-06T20:13:43.024575
---

# What Is Jump List Cache

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

# What Is Jump List Cache?

* January 23, 2025

This post explains the technical aspects of jump lists for IT, cybersecurity, and digital forensics professionals.

**It answers questions like:**

* What is jump list cache?
* How are jump list caches structured?
* What applications use jump lists?

So if you want to understand the details of this data artifact, you’re in the right place.

Let’s get started.

**Jump to…**

[What Is A Jump List?](#What Is A Jump List?)
[What Is Jump List Cache?](#What Is Jump List Cache?)
[More on the Forensic Value of Jump Lists](#More on the Forensic Value of Jump Lists)
[Where Are Jump List Caches Stored?](#Where Are Jump List Caches Stored?)
[How Are Jump List Caches Structured?](#How Are Jump List Caches Structured?)
[How to Access Jump Lists](#How to Access Jump Lists)
[What Applications Use Jump Lists?](#What Applications Use Jump Lists?)
[Top Jump List Analysis Tools](#Top Jump List Analysis Tools)
[Analyzing Jump Lists with Cyber Triage](#Analyzing Jump Lists with Cyber Triage)
[How to Do Jump List Analysis in 2025](#How to Do Jump List Analysis in 2025)

## **What Is A Jump List?**

A [jump list](https://learn.microsoft.com/en-us/uwp/api/windows.ui.startscreen.jumplist?view=winrt-26100&redirectedfrom=MSDN) is a system-provided menu that gives quick access to recently and frequently opened files on a per-application basis. Additionally, jumplists provide users with easy access to common tasks or custom actions if an application chooses to provide such features. You can access them via the Taskbar, Start menu, or keyboard shortcut. Microsoft introduced jump lists in Windows 7, and it is still supported by the [desktop device family](https://learn.microsoft.com/en-us/uwp/api/windows.ui.startscreen.jumplist?view=winrt-26100).

**Jump list menus display:**

1. User interactions with files, folders, and websites

[![Jump list of frequently used files example. ](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_frequent_Files_Example.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_frequent_Files_Example.png)

2. User executions of common application tasks

[![Jump lists tasks example.](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Tasks_Example.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Tasks_Example.png)

3. User executions of custom-defined actions specific to an app

|  |  |
| --- | --- |
| [![Custom jump list example 1.](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Custom_List1.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Custom_List1.png) | [![Custom jump list example 2.](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Custom_List2.png)](https://www.cybertriage.com/wp-content/uploads/2025/01/Jumplist_Custom_List2.png) |
| The user behavior displayed on the jump list menu varies by app. This is because each app defines jump list activity differently. | |

## **What Is Jump List Cache?**

A jump list cache is the data used to create the jump list menus. It contains information like paths to recently accessed files, timestamps for file access, number of times files were accessed, and the applications used to access files. This data can be valuable for digital investigators when they want to understand [user activity on a system](https://www.cybertriage.com/blog/jump-list-forensics-2025/).

## **More on the Forensic Value of Jump Lists**

DFIR expert [Brian Carrier](https://www.linkedin.com/in/carrier4n6/) explains: “Jump lists provide insight into understanding what files a user has accessed, how often files have been accessed, and when they were last accessed. This can be useful when trying to establish user behavior patterns which can be correlated with evidence from other data artifacts.”

## **Where Are Jump List Caches Stored?**

Jump list cache data can be stored in two different locations depending on the functionality implemented in an application’s jump list.

| **Where Jump List Caches Are Stored** |
| --- |
| %appdata%\microsoft\windows\recent\automaticdestinations\\*.automaticDestinations-ms |
| %appdata%\microsoft\windows\recent\customdestinations\\*.customDestin...