---
title: Field Notes: EtherRAT Distributed Through a Legitimate Intune Workflow
url: https://dfir.ch/posts/field_notes_etherrat/
source: Over Security
date: 2026-10-14
fetch_date: 2026-10-15T06:45:08.352116
---

# Field Notes: EtherRAT Distributed Through a Legitimate Intune Workflow

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Field Notes: EtherRAT Distributed Through a Legitimate Intune Workflow

14 Oct 2026

**Table of Contents**

* + [Introduction](#introduction)
* [Scoping the Infection](#scoping-the-infection)
* [Intune as an Unintentional Distribution Mechanism](#intune-as-an-unintentional-distribution-mechanism)
* [Tracing the Initial Download](#tracing-the-initial-download)
* [Post-Compromise Activity](#post-compromise-activity)
* [A Second Malicious Advanced IP Scanner Repository](#a-second-malicious-advanced-ip-scanner-repository)
* [Correlation with EtherRAT](#correlation-with-etherrat)
* [Conclusion](#conclusion)

### Introduction

The investigation began with a `Microsoft Defender for Endpoint` alert for suspicious screen capture activity involving PowerShell. Examining the process ancestry revealed a larger execution chain involving `FbtRYX8x.exe`, a renamed `Node.js` runtime communicating with several public Ethereum RPC providers. The observed behavior was consistent with `EtherRAT`, a Node.js-based backdoor previously documented by [Atos Threat Research Center](https://atos.net/en/lp/cybershield/etherrat-distribution-spoofing-administrative-tools-via-github-facades), [The DFIR Report](https://thedfirreport.com/2026/05/11/flash-alert-etherrat-and-tuktuk-c2-end-in-the-gentleman-ransomware/), and [Malwarebytes](https://www.malwarebytes.com/blog/threat-intel/2026/06/inside-a-malicious-infrastructure-delivering-etherrat-phishing-pages-and-malicious-software).

Further hunting identified the same malware on four managed endpoints, all of which had received a malicious MSI through Microsoft Intune. The deployment itself was not the result of an identified compromise of Intune. Instead, the customer had imported what appeared to be a legitimate `Advanced IP Scanner` installer into its existing software distribution workflow, inadvertently deploying the malware to multiple systems.

Retracing activity on the earliest affected endpoint led to a Bing search for “advanced ip scanner msi” and a GitHub repository impersonating the software vendor. The repository was no longer available during the investigation, but browser artefacts preserved evidence of the visit. This Field Note examines the relationship between the initial software lure, the malicious MSI, and the legitimate Intune deployment process that subsequently distributed the payload.

![Defender Alert](/images/field_notes_etherrat/defender.png "Defender Alert")

Figure 1: Microsoft Defender for Endpoint alert for suspicious screen capture activity

## Scoping the Infection

Analysis of the execution chain identified an obfuscated PowerShell script staged in a randomized directory under `%LOCALAPPDATA%`. In the initial case, the script was executed from `C:\Users\username\AppData\Local\WwajyG9wqS3U\aWhXKGlA.ps1` and handled the preparation of the Node.js runtime used by the subsequent malware stage. It first checked for an existing `Node.js` installation and, if none was available, retrieved a legitimate Node.js distribution from the official website. The downloaded archive was extracted into the staging directory before the runtime was launched with `DdkExG1tIy.ini` as an argument (obfuscated JavaScript - the .ini extension is solely to blend in, but is executed by node.exe).

Hunting for related activity identified four affected systems with a similar execution chain, including the same payload filename and connections to public Ethereum RPC providers. Three endpoints used identical copies of a downloaded `Node.js` runtime, whereas the fourth reused an existing installation by copying `C:\Program Files\nodejs\node.exe` to `C:\Program Files\nodejs\FbtRYX8x.exe`. Consequently, the executable hash differed on the fourth system despite the otherwise consistent execution behavior, illustrating why hunting exclusively for the hash of the renamed runtime would have missed part of the infection.

The malware repeatedly contacted several public Ethereum RPC providers over TCP/443:

* eth.merkle[.]io
* rpc.mevblocker[.]io
* eth-mainnet.public.blastapi[.]io
* eth.drpc[.]org
* mainnet.gateway.tenderly[.]co
* ethereum-rpc.publicnode[.]com
* rpc.flashbots[.]net

## Intune as an Unintentional Distribution Mechanism

Examining the MSI installation process ancestry revealed that the affected endpoints had received the package through the Windows MDM application deployment mechanism rather than through independent user execution. Defender telemetry showed `msiexec.exe` being launched through `MDMAppInstaller.exe` and `omadmclient.exe`, using the expected silent MSI installation switches to install the package without user interaction.

The MSI was associated with ProductCode `{6FB2BB4F-67D5-4B13-8829-001C1E5E05DF}`. Local installation metadata contained an apparently randomized display name `(9FAj2kCcNs)` and publisher `(nAQUEdLa)`, with version 7.5.12.0. Querying the Intune application inventory revealed an application registered as Advanced IP Scanner with the same ProductCode and version, connecting the suspicious endpoint installation to a package managed through Intune.

```
Connect-MgGraph -Scopes "DeviceManagementApps.Read.All"

Get-MgDeviceAppManagementMobileApp -All |
    Where-Object {
        $_.AdditionalProperties['@odata.type'] -eq
        '#microsoft.graph.windowsMobileMSI'
    } |
    Select-Object DisplayName, @{
        Name = 'ProductCode'
        Expression = { $_.AdditionalProperties['productCode'] }
    }, @{
        Name = 'Version'
        Expression = { $_.AdditionalProperties['productVersion'] }
    }

Name                ProductCode                            Version
----                -----------                            -------
Advanced IP Scanner {6FB2BB4F-67D5-4B13-8829-001C1E5E05DF} 7.5.12.0
```

Reviewing the installations across the four affected systems showed that the package had been distributed over approximately one month. The customer confirmed that the MSI had been imported into Intune as an apparently legitimate Advanced IP Scanner installer and subsequently assigned to managed devices. Rather than requiring every affected user to encounter the original malicious download, the attacker-controlled installer had entered an existing administrative deployment process, which then distributed the malware to additional endpoints.

## Tracing the Initial Download

To understand how the malicious installer entered the software deployment process, we examined browser artefacts from the earliest affected endpoint. Five days before the first known malicious installation through Intune, Chromium history records showed a Bing search for `advanced ip scanner msi`, followed by visits to `https://github.com/AdvancedIPScanner/download`. The repository presented itself as a distribution point for Advanced IP Scanner and advertised MSI-based enterprise deployment.

The repository had been removed by the time of the investigation, preventing us from examining the originally advertised installer. However, the retained browser history confirmed that the user had visited a repository impersonating Advanced IP Scanner five days before the first known malicious Intune installation. While this sequence provides a plausible explanation for how the MSI entered the environment, we could not conclusively determine whether the original download matched the package subsequently deployed through Intune.

## Post-Compromise Activity

Following execution, Defender telemetry showed the malware collecting information about the local system, including the Windows locale, installed antivirus products, GPU information, domain membership, Machine GUID, and available logical disks. Additional commands such as `net session` and `net use` were observed, indicating attempts to enumerate accessible sessions and network resources.

On one endpoint, the execution chain also invoked PowerShell to captur...