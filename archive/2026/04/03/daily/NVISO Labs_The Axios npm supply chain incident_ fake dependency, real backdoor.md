---
title: The Axios npm supply chain incident: fake dependency, real backdoor
url: https://blog.nviso.eu/2026/04/03/the-axios-npm-supply-chain-incident-fake-dependency-real-backdoor/
source: NVISO Labs
date: 2026-04-03
fetch_date: 2026-04-04T04:16:19.481405
---

# The Axios npm supply chain incident: fake dependency, real backdoor

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [AI Security](https://blog.nviso.eu/category/ai-security/)
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# The Axios npm supply chain incident: fake dependency, real backdoor

[Thomas Papaloukas](https://blog.nviso.eu/author/thomas-papaloukas/ "Posts by Thomas Papaloukas")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Uncategorized](https://blog.nviso.eu/category/uncategorized/), [Windows](https://blog.nviso.eu/category/windows/), [Threat Hunting](https://blog.nviso.eu/category/threat-hunting/)

April 3, 2026April 3, 2026
7 Minutes

On March 31, 2026, two malicious Axios versions (1.14.1 and 0.30.4) were briefly published to npm via a compromised maintainer account. The only change performed was the addition of a trojanized dependency, whose postinstall script deployed a cross‑platform RAT (for macOS, Windows, and Linux). Although the Axios packages were removed within hours, multiple hits were observed in our MDR service, mainly across developer workstations and Docker containers. In this blog post, we briefly walk through the details of the incident, share our observations, and provide KQL hunting queries used to identify and assess exposure across our MDR customers.

## Brief Incident Summary

An adversary obtained access to the lead maintainer’s npm account and managed to publish two Axios versions (1.14.1 and 0.30.4). Both of these versions injected a malicious dependency under the name *plain-crypto-js@4.2.1* with a postinstall dropper (*setup.js*) [1].

The dropper fetched OS-specific payloads from the C2 depending on the platform it was attempting to infect, and once the payload was retrieved it proceeded with clearing forensic traces and artifacts. The payloads fall under the classification of *Remote Access Trojans (RAT)* based on their observed capabilities (e.g., system reconnaissance, remote command execution). John Hammond from Huntress has an elaborate technical overview of these payloads in their blog post, taking a deep dive into the infection chain [2].

![How the attack works](https://blog.nviso.eu/wp-content/uploads/2026/04/image.png)

*Figure 1: Technical Details of the Attack – socket.dev [1]*

## Evidence Observed

During these incidents, our SOC observed the following process tree. The postinstall dropper *setup.js* was executed via *node.exe*, which then initiated the rest of the process chain.

![Incident process tree](https://blog.nviso.eu/wp-content/uploads/2026/04/image-3-1024x406.png)

*Figure 2: Incident Process Tree*

In a nutshell, after the execution of the postinstall script and the identification of the host OS as Windows, the location of *powershell.exe* binary is determined using the command `where PowerShell`. The binary is then copied to *“C:\ProgramData\wt.exe”*. Microsoft Defender for Endpoint (MDE) detects this activity, as copying the PowerShell binary to “*C:\ProgramData\wt.exe”* triggers an alert named “*System executable renamed and launched*“.

Subsequently, a VBS script named *6202033.vbs* is created. Its purpose is to download the second stage PowerShell script *6202033.ps1*, from the C2 infrastructure. The VBS script downloads and runs *6202033.ps1* (via *wt.exe* – the now renamed PowerShell executable) and immediately deletes itself. The PowerShell script is also deleted after its execution.

Key behaviors we observed from the second stage PowerShell script are:

1. System information discovery
   * OS version
   * File system enumeration
   * Local system enumeration
2. Preparation for the persistence mechanism
   * Creation of “*C:\ProgramData\system.bat*“, a batch script that, when executed, uses PowerShell to execute commands retrieved from the C2 infrastructure
3. Persistence mechanism created using the following registry key
   * Registry key: *HKEY\_CURRENT\_USER\USER\_SID\Software\Microsoft\Windows\CurrentVersion\Run*
   * Value name: *MicrosoftUpdate*
   * Value data: *C:\ProgramData\system.bat*
4. Communication towards the C2 infrastructure
   * *hxxp[://]sfrclak[.]com:8000/6202033*

The consistent reuse of the “6202033” file-naming convention (“*sfrclak[.]com:8000/6202033″, 6202033.vbs, 6202033.ps1*) by the attacker can be used to perform initial scoping using the Device Timeline in Defender.

## Hunting Queries

Based on the information gathered thus far and the observed process chain, the following queries were compiled to assist us in scoping more of our MDR tenants who may have been impacted by this supply chain attack.

Note that the second query does not rely solely on IOCs; rather, it relies on the expected process execution steps, so further investigation may be required. That being said, the false-positive rate is expected to be low.

```
let Time = 7d;
let NetworksEvents = DeviceNetworkEvents
| where Timestamp > ago(Time)
| where RemoteUrl has_any ("sfrclak.com","callnrwise.com","calltan.com") or RemoteIP in ("142.11.206.73","23.254.167.216");
let ProcessEvents = DeviceProcessEvents
| where Timestamp > ago(Time)
| where ActionType == "ProcessCreated"
| where FileName == "wt.exe"
| where ProcessCommandLine has " -w hidden";
let FileEvents = DeviceFileEvents
| where Timestamp > ago(Time)
| where FileName has_any ("plain-crypto-js","6202033.ps1","6202033.vbs") or FolderPath contains @"/Library/Caches/com.apple.act.mond" or FolderPath contains "/tmp/ld.py" or SHA256 in ("e49c2732fb9861548208a78e72996b9c3c470b6b562576924bcc3a9fb75bf9ff","e10b1fa84f1d6481625f741b69892780140d4e0e7769e7491e5f4d894c2e0e09","ed8560c1ac7ceb6983ba995124d5917dc1a00288912387a6389296637d5f815c","f7d335205b8d7b20208fb3ef93ee6dc817905dc3ae0c10a0b164f4e7d07121cd","59336a964f110c25c112bcc5adca7090296b54ab33fa95c0744b94f8a0d80c0f","5bb67e88846096f1f8d42a0f0350c9c46260591567612ff9af46f98d1b7571cd","58401c195fe0a6204b42f5f90995ece5fab74ce7c69c67a24c61a057325af668","92ff08773995ebc8d55ec4b8e1a225d0d1e51efa4ef88b8849d0071230c9645a","617b67a8e1210e4fc87c92d1d1da45a2f311c08d26e89b12307cf583c900d101","fcb81618bb15edfdedfb638b4c08a2af9cac9ecfa551af135a8402bf980375cf");
let RegistryEvents = DeviceRegistryEvents
| where Timestamp > ago(Time)
| where RegistryKey has @"Software\Microsoft\Windows\CurrentVersion\Run"
| where RegistryValueName =~ "MicrosoftUpdate"
| where RegistryValueData =~ @"C:\ProgramData\system.bat";
union NetworksEvents, ProcessEvents, FileEvents, RegistryEven...