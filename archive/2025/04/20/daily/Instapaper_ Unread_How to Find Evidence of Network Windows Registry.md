---
title: How to Find Evidence of Network Windows Registry
url: https://www.cybertriage.com/blog/how-to-find-evidence-of-network-windows-registry/
source: Instapaper: Unread
date: 2025-04-20
fetch_date: 2025-10-06T22:04:51.044285
---

# How to Find Evidence of Network Windows Registry

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

# How to Find Evidence of Network Windows Registry

* April 17, 2025
* **[Chris Ray](https://www.cybertriage.com/team/chris-ray/)**

The network need not be a mystery. Learn how to find evidence of network Windows Registry from DFIR expert Chris Ray.

Let’s get to it!

**Jump to…**

[What Is “Network Evidence” in the Windows Registry?](#What Is "Network Evidence" in the Windows Registry?)
[Forensic Relevance of “Network Evidence”](#Forensic Relevance of “Network Evidence”)
[Where to Find Evidence of Network Windows Registry](#Where to Find Evidence of Network Windows Registry)
[Keep Learning Registry Forensics](#Keep Learning Registry Forensics)

## **What Is “Network Evidence” in the Windows Registry?**

Network evidence in the Windows Registry refers to the traces, configurations, and historical data related to a system’s network activity.

This evidence is **embedded in various Registry hives** and **reveals:**

| Data Found in Windows Registry |
| --- |
| * MAC addresses of adapters. * Saved Wi-Fi profiles and SSIDs. * Proxy settings and internet configurations. * Adapter names and physical/virtual status. * Network interfaces (wired, wireless, virtual). * IP address configurations (DHCP, static, etc.). * Connected domains, networks, and workgroups. * First and last connection times when joining a network. |

This evidence is scattered across SYSTEM, SOFTWARE, and user-specific hives, and can be correlated with other system artifacts (event logs, file access, etc.).

## **Forensic Relevance of “Network Evidence”**

Network data in the Windows Registry can be crucial for:

|  |  |
| --- | --- |
| **Attribution and Presence** | * Determine where a device was used based on known Wi-Fi SSIDs. * Identify if a system is connected to a specific network, router, or location. * Correlate saved networks with user travel or physical location. |
| **Timeline Construction** | * Use DHCP lease times to help correlate hostname to IP mapping during lease period. * Reveal first and last seen dates for a network profile. |
| **System Configuration and Misuse** | * Confirm if a proxy was manually set (often used in malware/espionage). * Detect use of static IPs or custom DNS, possibly for exfiltration or bypassing monitoring. * Detect unexpected/malicious firewall settings and rules |
| **Malware and Persistence** | * Malware may register network adapters or modify Internet settings via the Registry. |

## **Where to Find Evidence of Network Windows Registry**

### Network Interface Information

Key information you can get network interface artifacts:

* IP configuration info for each interface.
* MAC address for each interface.
* List of interfaces installed on the system.

Let’s look at each in detail:

#### IP Config Info for Each Interface

![tcpip interface](https://www.cybertriage.com/wp-content/uploads/2025/04/tcpip_interface-800x442.png)

```
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\
```

Each subkey represents IP configuration data for an interface. The subkey name represents the interface GUID used to uniquely identify that interface and can be used to correlate information between other artifacts.

**Key data each interface can contain:**

| **Info** | **Notes** |
| --- | --- |
| **Was IP Info Statically/ Dynamically Assigned** | * “EnableDHCP”  with value of 1 means DHCP is enabled on interface. |
| **IP Address** | * IP address can be obtained from “IPAddress” or “DHCPIPAddress” depending on if statically or dynamically assigned. |
| **SubnetMask** | * Subnetmask can be obtained from “SubnetMask” or “DHCPSubnetMask” depending on if statically or dynamically assigned. |
| **DHCP Leasing Info** | * “LeaseObtainedTime”: Represents epoch time DHCP lease was obtained. * “LeaseTermianteTime”: Represents epoch time DHCP lease is up. * “Lease”: Represents length of lease in seconds. |
| **DNS Server** | * DNS Server IP can be obtained from “NameServer” or “DHCPNameServer” depending on if it was statically or dynamically assigned. |
| **DNS Connection suffix** | * DNS connection suffix can be obtained from “Domain” or “DHCPDomain” depending on if it was statically or dynamically assigned. |

#### MAC Address for Each Interfa...