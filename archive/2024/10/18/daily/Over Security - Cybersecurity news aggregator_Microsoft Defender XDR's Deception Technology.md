---
title: Microsoft Defender XDR's Deception Technology
url: https://dfir.ch/posts/defender_xdr_deception/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-18
fetch_date: 2025-10-06T18:54:41.272130
---

# Microsoft Defender XDR's Deception Technology

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

# Microsoft Defender XDR's Deception Technology

10 Oct 2024

**Table of Contents**

* [Introduction](#introduction)
* [Turn on Deception](#turn-on-deception)
* [Executed PowerShell code](#executed-powershell-code)

## Introduction

This week wasn’t the first time we’ve investigated a case where a customer reported suspicious accounts that couldn’t be linked to any employees. In this case, two domain admin users were found on the affected network, but neither is employed by the company. Both accounts had logged into nearly every device within the organization, which understandably caused concern among those responsible, prompting them to ask us to investigate further.

![Non-employed Domain Administrator](/images/deception/marcel.png "Non-employed Domain Administrator")

Figure 1: Non-employed Domain Administrator

A user on Reddit [reported](https://www.reddit.com/r/DefenderATP/comments/1eqeou3/found_defender_report_showing_weird_account_no/) the same behavior and asked for support:
*I was going through some reporting the other day and came across an account name. The name looks odd, so I started to investigate. I noticed this account is showing up on a lot of devices, however not all. [..] Found account Name: amol.paulson. This is not a service or user account we have or have created. Can’t be found in Azure AD, On Prem AD or any other tool we have. But it is listed in the report as a domain account.*

It turned out that these accounts and their activity were part of the [deception technology](https://learn.microsoft.com/en-us/defender-xdr/configure-deception) used by Microsoft Defender XDR.

## Turn on Deception

The deception capability is turned off by default and must be switched on explicitly (click [here](https://learn.microsoft.com/en-us/defender-xdr/configure-deception) for the official Microsoft documentation).

![Enabling the deception technology](/images/deception/deception.png "Enabling the deception technology")

Figure 2: Enabling the deception technology

*A default rule is automatically created and turned on when the deception capability is enabled. The default rule, which you can edit accordingly, automatically generates decoy accounts and hosts that are integrated into lures and plants these to all target devices in the organization. While the deception feature’s scope is set to all devices in the organization, lures are planted in Windows client devices only.*

![Default deception rule<](/images/deception/default_rule.png "Default deception rule<")

Figure 3: Default deception rule

The created user accounts (decoy accounts) are visible within the default rule. Figure 4 is a screenshot from our actual case (redacted usernames).

![Decoy users](/images/deception/default_rule_users.png "Decoy users")

Figure 4: Decoy users

## Executed PowerShell code

The user accounts do not indicate they are decoy accounts if you only examine their properties (without checking the deception default rule). However, a clue that a decoy account has logged in can be found in the PowerShell logs (the login is not over the network, but a local login). Just before a decoy account logs into a computer or server on the network, PowerShell code is executed on the machine. Below is a shortened version of the observed PowerShell code:

```
& {$OutputEncoding = [Console]::OutputEncoding =[System.Text.Encoding]::UTF8;
$scriptFileStream = [System.IO.File]::Open('C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{1E0A9F59-EA0B-4B34-989B-91D2E078DD9B}.ps1',
[System.IO.FileMode]::Open,
[System.IO.FileAccess]::Read,
[System.IO.FileShare]::Read);$calculatedHash = Microsoft.PowerShell.Utility\Get-FileHash 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{1E0A9F59-EA0B-4B34-989B-91D2E078DD9B}.ps1' -Algorithm SHA256;if (!($calculatedHash.Hash -eq '43b8ccd8e75be00830e975ee41773bf8d0640a9ed33838999c13798e9cbbd9f3')) { exit 323;};
Start-Transcript -Path 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Temp\PSScriptOutputs\PSScript_Transcript_{1E0A9F59-EA0B-4B34-989B-91D2E078DD9B}.txt';
. 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{1E0A9F59-EA0B-4B34-989B-91D2E078DD9B}.ps1' -Id 3f884218-6a5a-4d02-8032-32ed7f90339a
-Descriptor eyJEZXRlY3Rpb[..]m51bGx9}
```

The parameter `Descriptor` is a base64 encoded JSON blob, see below for a shortened version. Within the parameter `DetectionKeys`, we see the username of the decoy account that conducted the login.

```
{
  "DetectionKeys": [
    "chantal.redacted"
  ],
  "Content": "ewogICJTZ[..]IHRydWUKfQ==",
  "EntityPath": "",
  "EntityType": 6,
  "LureDeploymentContext": {
    "ExpirationUtc": "2024-10-11T12:43:09.0754269Z",
    "Id": "97c0397b-bea7-4e61-8623-956383ab6816",
    "CorrelationId": null
  },
  "FileAttributes": null
}
```

`Content`, in turn, contains yet another base64 JSON blob:

```
{
  "SerializedNlRecord": "HAAGABwAHgAAAAAAA[..]AKQAAAA==",
  "SoftwareExclusionListForDeployment": [],
  "UserRid": 942878775,
  "ShouldSuppressDummyLogin": true
}
```

There is limited publicly available information about all the parameters used within the JSON blobs. However, by analyzing the executed PowerShell code, we can determine that a decoy account was responsible for the login(s). This analysis can also be confirmed by cross-referencing the created default decoy accounts.

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).