---
title: BlockEDRTraffic – EDR Evasive Lateral Movement Tool
url: https://www.darknet.org.uk/2025/09/blockedrtraffic-edr-evasive-lateral-movement-tool/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2025-09-06
fetch_date: 2025-10-02T19:44:09.574241
---

# BlockEDRTraffic – EDR Evasive Lateral Movement Tool

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# BlockEDRTraffic – EDR Evasive Lateral Movement Tool

September 5, 2025

Views: 695

BlockEDRTraffic is a pair of Windows proof-of-concept tools that prevent Endpoint Detection and Response (EDR) agents from sending network telemetry. It supports two approaches. One executable creates inbound and outbound block rules with Windows Defender Firewall. The other creates per-application IPv4 and IPv6 filters with Windows Filtering Platform.

![BlockEDRTraffic - EDR Evasive Lateral Movement Tool](https://www.darknet.org.uk/wp-content/uploads/2025/09/BlockEDRTraffic-EDR-Evasive-Lateral-Movement-Tool-640x427.jpg)

This requires high integrity and SeDebugPrivilege, enumerating running processes, matching them against an embedded blacklist, and then applying network blocks only for those targets. The tools do not disable or tamper with security products. They only add filtering rules and include a cleanup mode that removes the rules they created.

While defenders typically focus on event logs or kernel hooks, network telemetry remains a blind spot. BlockEDRTraffic creates a brief window of stealth, aligning with tools like [**AutoPwnKey**, which avoids API calls via user simulation](https://www.darknet.org.uk/2025/06/autopwnkey-av-evasion-via-simulated-user-interaction/) and [**BEOTM**, which simulates EDR behaviour for testing bypasses](https://www.darknet.org.uk/2024/01/best-edr-of-the-market-beotm-endpoint-detection-and-response-testing-tool/).

## Features

The repository currently lists Microsoft Defender Antivirus, Microsoft Defender for Endpoint, and Elastic EDR as supported targets and exposes process definitions in source so operators can extend the blacklist.

* **Two evasion paths.** Windows Defender Firewall rule creation or Windows Filtering Platform filters for per-process blocking.
* **Privilege checks.** Verifies elevated integrity and SeDebugPrivilege before acting.
* **Target discovery.** Resolves full image paths for blacklist matching and shows what will be blocked.
* **Scoped cleanup**. Removes only the rules and filters created by the tool.
* **Extensible targets**. The EDR process list lives in the source code for easy updates.

## Installation

The repository provides Visual Studio project files. Build with Visual Studio 2022 on a Windows development host.

<code>Clone the repo: https://github.com/0xJs/BlockEDRTraffic
Open BlockTraffic.sln in Visual Studio 2022
Build Release x64 to produce WindowsDefenderFirewall.exe and WindowsFilteringPlatform.exe</code>

|  |  |
| --- | --- |
| 1  2  3 | <code>Clone the repo: https://github.com/0xJs/BlockEDRTraffic  Open BlockTraffic.sln in Visual Studio 2022  Build Release x64 to produce WindowsDefenderFirewall.exe and WindowsFilteringPlatform.exe</code> |

Ensure execution occurs under a sufficiently privileged context to manipulate EDR processes in memory.

## Usage

Use the `-e` parameter to block all EDR processes:

PS C:\ > .\WindowsDefenderFirewall.exe
Usage: WindowsDefenderFirewall.exe -e / -d
Options:
-e Enable - Block blacklisted EDR processes
-d Disable - Remove blocked firewall rules created by this tool
-h - Display this help message

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | PS C:\ > .\WindowsDefenderFirewall.exe  Usage: WindowsDefenderFirewall.exe -e / -d  Options:  -e Enable  - Block blacklisted EDR processes  -d Disable - Remove blocked firewall rules created by this tool  -h         - Display this help message |

Use the `--edr` parameter to block all EDR processes or use the `-e` parameter to block a specific process

PS C:\ > .\WindowsFilteringPlatform.exe
Usage: WindowsFilteringPlatform.exe -e / -d / --edr
Options:
--edr - Block traffic of blacklisted EDR processes
-e &lt;PROCESS> - Block traffic of specified process
-d - Remove blocked firewall rules created by this tool
-h - Display this help message

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | PS C:\ > .\WindowsFilteringPlatform.exe  Usage: WindowsFilteringPlatform.exe -e / -d  / --edr  Options:  --edr          - Block traffic of blacklisted EDR processes  -e &lt;PROCESS>   - Block traffic of specified process  -d             - Remove blocked firewall rules created by this tool  -h             - Display this help message |

## Attack Scenario

During a red team engagement, an operator gains access to a host via phishing. They need to run BloodHound queries and move laterally using native PowerShell.

1. Run **WindowsDefenderFirewall.exe** **or WindowsFilteringPlatform.exe** to suppress EDR network calls.
2. Immediately execute [**Invoke-BloodHound**](https://www.darknet.org.uk/2019/06/bloodhound-hacking-active-directory-trust-relationships/) and [**PsMapExec**](https://www.darknet.org.uk/2025/07/psmapexec-powershell-command-mapping-for-lateral-movement/) to enumerate user sessions and pivot quietly.
3. Once the duration expires, EDR telemetry resumes, with minimal traces of evasive activity.

This allows the red team to move aggressively during a short stealth window while minimising exposure.

## Red Team Relevance

BlockEDRTraffic fills the critical niche between payload obfuscation (e.g. [Shell3r](https://www.darknet.org.uk/2025/05/shell3r-powerful-shellcode-obfuscator-for-offensive-security/)) and lateral movement tools. It doesn’t replace endpoint agents but turns them silent long enough to operate under the radar.

When paired with host-based detection like [**Falco**, which monitors syscall behaviours in containers](https://www.darknet.org.uk/2025/05/falco-real-time-threat-detection-for-linux-and-containers/) but may miss network gaps, BlockEDRTraffic demonstrates how adversaries might exploit lower reliability in network telemetry.

## Conclusion

BlockEDRTraffic provides red teams with two reliable methods to mute EDR telemetry for a short operational window, utilising native Windows capabilities. It focuses on scoped per-process filtering, includes cleanup, and keeps changes transparent and auditable. Use it to validate detection depth beyond simple process monitoring and to measure how quickly defenders notice that their agent has gone quiet.

You can read more or download BlockEDRTraffic here: <https://github.com/0xJs/BlockEDRTraffic>

## Related Posts:

* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [AI-Powered Malware - The Next Evolution in Cyber Threats](https://www.darknet.org.uk/2025/05/ai-powered-malware-the-next-evolution-in-cyber-threats/)
* [Best Open Source HIDS Tools for Linux in 2025…](https://www.darknet.org.uk/2025/05/best-open-source-hids-tools-for-linux-in-2025-compared-ranked/)
* [Emerging Threats ETOpen - Anti-malware IDS/IPS Ruleset](https://www.darknet.org.uk/2016/08/emerging-threats-etopen-anti-malware-idsips-ruleset/)
* [Understanding the Deep Web, Dark Web, and Darknet…](https://www.darknet.org.uk/2025/04/understanding-...