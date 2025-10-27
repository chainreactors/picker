---
title: Today I Learned - Device Discovery
url: https://dfir.ch/posts/today_i_learned_device_discovery/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:06.591509
---

# Today I Learned - Device Discovery

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

# Today I Learned - Device Discovery

27 Apr 2024

**Table of Contents**

* [Introduction](#introduction)
* [Suspicious (?) PowerShell code](#suspicious--powershell-code)
* [Scanner Arguments](#scanner-arguments)
* [Functions](#functions)
* [Conclusion](#conclusion)

## Introduction

A client contacted us following an alert triggered by their Network Detection and Response sensor (NDR), which flagged suspicious network behavior originating from a server within their internal network. The detected activity resembled a port scan, suggesting that the server might have been compromised and was possibly being exploited by an attacker for initial reconnaissance. What added to the concern was the specific choice of ports scanned during the activity.

![Port Scan Alert](/images/device_discovery/ports.png "Port Scan Alert")

Figure 1: Port Scan Alert

The presence of an Endpoint Detection and Response (EDR) agent on the (compromised) machine at the time of the incident provided sufficient evidence to gain insights into the observed behavior.

## Suspicious (?) PowerShell code

At roughly the same time that the NDR sensor detected the port scan, the server conducting the scan executed the following PowerShell code:

```
powershell.exe -ExecutionPolicy Bypass -NoProfile -NonInteractive -Command
    "& {
        $OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
        $scriptFileStream = [System.IO.File]::Open(
        'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{616BC9C3-49C9-4A18-8B5E-1C65CE6EBCEB}.ps1',
        [System.IO.FileMode]::Open,
        [System.IO.FileAccess]::Read,
        [System.IO.FileShare]::Read
    )
    $calculatedHash = Microsoft.PowerShell.Utility\Get-FileHash 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{616BC9C3-49C9-4A18-8B5E-1C65CE6EBCEB}.ps1' -Algorithm SHA256
    if (!($calculatedHash.Hash -eq '5ce37c7f722cac86ac220eed509b95adab18c9d40c5768bcb2ec6dddacb93fc4')) {
        exit 323
    }
    Start-Transcript -Path 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Temp\PSScriptOutputs\PSScript_Transcript_{616BC9C3-49C9-4A18-8B5E-1C65CE6EBCEB}.txt'
    . 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{616BC9C3-49C9-4A18-8B5E-1C65CE6EBCEB}.ps1' -ParamsAsBase64 LgUAA..
}"
```

At first glance, this appears to be a genuine script from Microsoft, likely a component of Defender for Endpoint. Let’s delve deeper into our analysis, focusing on the code snippet below. Here, the file *PSScript\_{616BC9C3-49C9-4A18-8B5E-1C65CE6EBCEB}.ps1* is invoked, with a chunk of base64 data passed as an argument (designated by *ParamsAsBase64*).

You will notice that Microsoft signs these PowerShell scripts and checks the hash as additional validation in case of tampering and re-signing with a locally trusted certificate. Also, some of these scripts do not work if PowerShell Constrained Language Mode is enabled. [Matt Graeber](https://twitter.com/mattifestation) has authored an insightful article detailing how Microsoft Defender for Endpoint ensures script integrity before execution, which you can find [here](https://gist.github.com/mattifestation/11fb1bd37fff9a80803d7b39a43553ee).

```
powershell.exe -ExecutionPolicy Bypass -NoProfile -NonInteractive
-File "C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Downloads\PSScript_{616BC9C3-49C9-4A18-8B5E-1C65CE6EBCEB}.ps1"
-ParamsAsBase64
ew0KICAg[..]]Q0YxTUZFck9NQT09Ig0KfQ==
```

## Scanner Arguments

The *ParamsAsBase64* argument from above, after base64 decoding it, reads as follows:

```
{
    "ScannerArgs": {
        "IpsToScan": "10.130.98.5,10.130.96.226,10.130.99.89,10.130.98.6,10.130.96.232,10.130.96.37",
        "Guid": "475ed155-ce48-46ea-8466-5489cf6348ff",
        "MachineId": "95f285b3763d4b1fc10561b995cc2b74bfb91a8e",
        "MachineConnections": [
            {
                "DefaultGatewayMac": "12-01-00-00-01-01",
                "AdapterId": "{6D85E743-83F4-47C4-A477-0260EC3BFCFC}",
                "NetworkNames": ["ad.<redacted>.ch"]
            }
        ],
        "ScannedDeviceId": "70294f0dc07b1491d90ef528a3c481dd455654c4",
        "ExpirationDateTime": "2024-04-19T01:26:02.1473403Z",
        "CvesToScan": ["CVE-2021-44228", "CVE-2022-22965"],
        "TargetMacs": [
            "00-50-56-8F-2C-60",
            "00-50-56-92-9E-5F",
            "00-50-56-92-57-FA",
            "00-50-56-8F-6F-3E",
            "00-50-56-8F-33-FA",
            "94-18-82-E6-C1-20"
        ],
        "DeviceIdsToScan": [
            "c0ef68382d2a1f331cd7d6b8b307a386de3b81a0",
            "a461e63997cab20ec26bca7729a8e49458f68a2e",
            "861d22a2963689dcfeb051f99712ee3fb34f72ec",
            "c47197940984ad1006f8a21c1a285af42a252981",
            "8311c1acaf8f63d0529adef45441c336e15f85fa",
            "70294f0dc07b1491d90ef528a3c481dd455654c4"
        ]
    },
    "Cert": "MIIFgzCCA2ugAwIBAgIT
}
```

We see the IPs, some CVEs to scan for, and the (redacted) network name(s). This is interesting (and useful) information, as we are still trying to understand if the alert raised by the NDR agent is, in fact, legitimate or if the server is compromised and somebody is scanning the network from our customer.

## Functions

Below is a brief excerpt highlighting some of the functions called within the PowerShell code (though not an exhaustive list):

* Scan-UdpTcpPorts
* Scan-Vnc
* Scan-SLP
* Scan-WinRm
* Scan-RpcInterfaceMapper

It may not be apparent initially, but those functions are part of [Device discovery](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/device-discovery-faq) from Microsoft Defender for Endpoint. [Here](https://jeffreyappel.nl/defender-for-endpoint-discovery-discover-the-unmanaged-part-of-the-corporate-network/) is a good introduction.

The complete list of scanned protocols, according to the [Device discovery frequently asked questions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/device-discovery-faq?view=o365-worldwide):
*When a device is configured to run Standard discovery, exposed services are being probed by using the following protocols: ARP, FTP, HTTP, HTTPS, ICMP, LLMNR, NBNS, RDP, SIP, SMTP, SNMP, SSH, Telnet, UPNP, WSD, SMB, NBSS, IPP, PJL, RPC, mDNS, DHCP, AFP, CrestonCIP, IphoneSync, WinRM, VNC, SLP, LDAP.*

## Conclusion

As the outlined analysis steps have shown, the portscan was, in fact, legitimate. We found out that **Device discovery** from Microsoft Defender for Endpoint scans the network for open ports or CVEs, which might look like a port scan to an NDR device. However, based on the article referenced above: *As opposed to malicious activity, which would typically scan the entire network from a few compromised devices, Microsoft Defender for Endpoint’s Standard discovery probing is initiated from all onboarded Windows devices making the activity benign and non-anomalous.*

Tell this the NDR sensor ;)

---

*What I learned today: Short blog posts about novel information for me. Thanks to Nathan McNulty (<https://twitter.com/NathanMcNulty>) for proofreading this post.*

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).