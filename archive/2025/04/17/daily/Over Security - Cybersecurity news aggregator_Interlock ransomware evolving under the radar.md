---
title: Interlock ransomware evolving under the radar
url: https://blog.sekoia.io/interlock-ransomware-evolving-under-the-radar/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-17
fetch_date: 2025-10-06T22:08:55.089608
---

# Interlock ransomware evolving under the radar

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Interlock ransomware evolving under the radar

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR](#molongui-disabled-link)
April 16 2025

0

27 minutes reading

## Introduction

**Interlock** is a **ransomware** intrusion set first observed in September 2024 that conducts Big Game Hunting and double extortion campaigns. Interlock cannot be classified as a “Ransomware-as-a-Service” (RaaS) group, as no advertisements for recruiting affiliates or information about affiliates have been found as of March 2025. As many other ransomware groups, Interlock has a Data Leak Site (DLS) called “**Worldwide Secrets Blog**” exposing victim’s data, and providing a way to negotiate the ransom price to the victims.

Although Interlock operators continue to regularly claim new victims on their DLS, they have published fewer names —  24 victims since September 2024, including 6 in 2025 —  compared to the most active ransomware groups currently operating. Indeed, ransomware such as Clop, RansomHub, Akira, Babuk, Lynx, Qilin, and Fog, each claimed more than one hundred victims in the first quarter of 2025. The companies impacted by the Interlock ransomware span various sectors across North America and Europe, indicating that the target selection is primarily opportunistic.

Interlock employs a **multi-stage attack chain**, starting by compromising legitimate websites that deliver fake browser updates, such as Google Chrome or MS Edge installers. These fake installers execute a PowerShell backdoor facilitating the execution of multiple tools, and ultimately leading to the ransomware payload delivery.

Since the apparition of the Interlock ransomware, Sekoia Threat Detection & Research (TDR) team observed its operators evolving, improving their **toolset**, and leveraging new techniques such as **ClickFix** to deploy the ransomware payload. They also used new tools such as LummaStealer and BerserkStealer. This report describes the malware and techniques used by Interlock operators and updates the knowledge of this threat following the Talos report in November 2024.

## Fake updaters for initial access

Since the emergence of the Interlock ransomware, its operators were observed using fake updaters hosted on compromised websites to deceive victims into downloading and executing the payload themselves. These installers are, in fact, PyInstaller files designed to mislead users. When the fake updater is manually launched by the victim, it downloads and executes a legitimate installer file according to the masqueraded product (a legitimate Google Chrome installer or MS Edge installer), while also running an embedded PowerShell script, which functions as a simple first-stage backdoor.

This PowerShell script operates in an infinite loop, continuously executing HTTP requests to specified hosts, with a failover logic between domain names and IP addresses in case of errors. It gathers system information, communicates with remote hosts, downloads and executes files, and, in recent versions, offers functionality for executing arbitrary commands and establishing persistence.

At the launch, the script verifies whether it has been executed with specific arguments. If only a single argument is provided, it relaunches itself with an additional argument ‘1’ to ensure the script runs in a detached mode without a visible window.

The system information is collected using various PowerShell commands. The following information are collected:

* The version of the script which is written in a constant;
* User context (SYSTEM, Admin or User privileges) by using  [Security.Principal.WindowsIdentity]::GetCurrent();
* System information via systeminfo;
* Processes and services via tasklist /svc;
* Active services via Get-Service;
* Available drives via Get-PSDrive;
* ARP table via arp -a.

After collecting system information, the script applies an XOR operation to the data using a hardcoded key, then compresses it with the Gzip algorithm and prefixes the final buffer with a fixed 32b integer.

The formatted system information is sent to the Command-and-Control (C2) server using an HTTP POST request on the `/init1234` URL path. Then the server can respond “ooff” which is a terminate command.

The C2 server can also send a .exe or .dll file (the type is determined by the last byte of the response). The file is decoded using XOR and saved in a randomly named folder within %AppData%. It is then executed directly in the case of a .exe file or via rundll32 in the case of a .dll. Unfortunately, the TDR team was not able to retrieve the payload returned by the C2 server, but multiple files corresponding to the expected response were observed. These files are described further below.

Multiple versions of this PowerShell RAT were observed from version 1 to version 11. Later versions of the script implements a atst command to establish persistence by creating a HKCU\Software\Microsoft\Windows\CurrentVersion\Run registry key to relaunch itself at startup. This version (V11) is also able to get and execute a Windows command from the C2.

In one of the last observed PowerShell backdoor, the requested domains are the following:

```
sublime-forecasts-pale-scored.trycloudflare[.]com
washing-cartridges-watts-flags.trycloudflare[.]com
investigators-boxing-trademark-threatened.trycloudflare[.]com
fotos-phillips-princess-baker.trycloudflare[.]com
casting-advisors-older-invitations.trycloudflare[.]com
complement-parliamentary-chairs-hc.trycloudflare[.]com
```

C2 domains used by the PowerShell backdoor v7-v9

All observed domains are subdomains from trycloudflare.com, a legitimate Cloudflare service. TryCloudflare enables the creation of tunnels to test applications locally without permanently exposing them to the Internet. By querying trycloudflare.com domains for a resp...