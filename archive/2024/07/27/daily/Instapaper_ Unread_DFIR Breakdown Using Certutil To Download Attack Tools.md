---
title: DFIR Breakdown Using Certutil To Download Attack Tools
url: https://www.cybertriage.com/blog/dfir-breakdown-using-certutil-to-download-attack-tools/
source: Instapaper: Unread
date: 2024-07-27
fetch_date: 2025-10-06T17:45:11.882231
---

# DFIR Breakdown Using Certutil To Download Attack Tools

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

# DFIR Breakdown: Using Certutil To Download Attack Tools

* July 24, 2024
* **[Chris Ray](https://www.cybertriage.com/team/chris-ray/)**

Windows certutil is a Windows utility that is used by threat actors to, amongst other things, download files. It’s an example of a Living of the Land Binary (LOLBin) that is used during an attack to achieve some malicious goal while using as many native programs as possible.

This blog post will focus on using certutils to download files and what DFIR artifacts are created from this activity. These artifacts are important because they can provide evidence about tools a threat actor downloaded and used.

We will cover the following topics:

* Certutil basics
* How to download attack tools using certutil
* DFIR artifacts created after certutil file download
* How Cyber Triage helps

# Certutil Basics

[Certutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil) is a command line tool that ships with Windows and its primary responsibility is to view and manage certificates on Windows Systems. Cryptographic certificates are used to verify signed executables, remote servers, and web domains.

Attackers historically abused Certutil to install their own certificates on a system. Unit42 has one such example [here](https://unit42.paloaltonetworks.com/retefe-banking-trojan-targets-sweden-switzerland-and-japan/).

But, it is also used to encode/decode base64, download files, and write to Alternate Data Streams. Examples of each of these use cases can be found documented under MITREs [certutil software](https://attack.mitre.org/software/S0160/) ATT&CK category.

# How To Download Attack Tools Using Certutil

Certutils command line arguments can be found in the Microsoft documentation [here](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil). However, it is not obvious how to use a combination of arguments in such a way that allows an adversary to download a given file. Luckily the fantastic [LOLBAS Project](https://github.com/LOLBAS-Project/LOLBAS/blob/master/README.md) has taken care of documenting all of the interesting ways certutil can be abused [here](https://lolbas-project.github.io/lolbas/Binaries/Certutil/).

There are different sets of arguments that will download a file:

* ```
  certutil.exe -verifyctl -f http://7-zip.org/a/7z1604-x64.exe
  ```
* ```
  certutil.exe -urlcache -split -f http://7-zip.org/a/7z1604-x64.exe
  ```

Both of them will download the specified URL and save the file to the current working directory.

Note that the above commands may fail to execute due to AV products blocking such activity, but attackers may disable Defender so that it doesn’t stop it.

When using the “-verifyctl” argument, you will notice some “verification” errors. These are expected because it is trying to verify a Certificate Trust List (CTL), but we didn’t point it to a CTL.  We can see the 7zip installer is downloaded to the current directory. The file will be named based on its SHA1 hash and a .bin extension.

![](https://www.cybertriage.com/wp-content/uploads/2024/07/2024-7-certutil-1-800x427.png)

The “-urlcache” version of the command will name the downloaded file with the same name as the file referenced in the URL.

![](https://www.cybertriage.com/wp-content/uploads/2024/07/2024-7-certutil-2-800x424.png)

# DFIR Artifacts Created After certutil File Download

There are two main groups of DFIR artifacts that we can find on an endpoint when it comes to certutil activity related to downloading files:

* Process artifacts
* CryptNetURLCache files

The first artifact is process execution history. There are many artifacts that record what processes ran and we’ll want to focus on the ones that store arguments so that we know if certutil was used to download files. One example of this is process creation events (4688) in the security event log.

A second place is to look at the CryptNetURLCache folders. This cache keeps a copy of files downloaded via certutil along with some metadata about where the file was downloaded from and first/last download times.

These artifacts exist at the following locations:

* Content: Contains copies of any file...