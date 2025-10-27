---
title: Nmap Cheatsheet
url: https://www.blackhillsinfosec.com/nmap-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:22.154394
---

# Nmap Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/), [Nmap](https://www.blackhillsinfosec.com/tag/nmap/)

# [Nmap Cheatsheet](https://www.blackhillsinfosec.com/nmap-cheatsheet/)

Written by [Alireza Liaghat](https://www.linkedin.com/in/alireza-lia/) || Reviewed by [Dale Hobbs](https://www.linkedin.com/in/dale-hobbs/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_9.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**Nmap Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_Nmap_3.pdf)

Find the tool here: <https://nmap.org/>

---

Nmap is a powerful open-source tool commonly used by system/network administrators and security professionals to perform network discovery, security auditing, and basic vulnerability assessment. Nmap allows you to quickly identify live hosts, open ports, running services, operating systems, and potential security risks within a network. This cheatsheet provides a reference to essential Nmap commands, scanning techniques, and common use cases to help streamline your network reconnaissance and troubleshooting tasks.

## The Nmap Formula

**Nmap + Target + Type + Port + Detection + Timing + Scripts + Evasion**

### **TARGET**

**What do you want to scan?**

| Example | Description | Use Case |
| --- | --- | --- |
| `192.168.x.x` | Scan the specified IP address | Used when there is only one target IP address. |
| `domain.com` | Scan the specified domain | Used when there is only one target domain. |
| `-iL target.txt` | Scan from a list of host addresses | Used when searching a known range of hosts. |
| `--unique` | Scans each address only once | Used in combination with lists. Avoids duplicate scans to speed up the scan. |
| `-n` | No DNS resolution | Speeds up scanning by skipping reverse DNS resolution. |

### **TYPE**

**How do you want to scan?**

| Example | Description | Use Case |
| --- | --- | --- |
| `-sT` | Full TCP 3-Way Handshake Scan | Most reliable scan. Use when not worried about firewalls. |
| `-sS` | “Stealth” scan. Impartial 3-Way Handshake | Does not establish a full handshake. “Dumb” firewalls will only see this as regular poor connection. |
| `-sU` | Scan using UDP | Preferred for scanning DNS (53), SNMP (161), DHCP (67), TFTP (69), etc. |

### **PORT**

**What port do you want to scan?**

| Example | Description | Use Case |
| --- | --- | --- |
| `-p 80,443` | Scans only the comma-separated ports | Useful for when scanning a host for a specific attack surface. |
| `-p 1-65535` | Scans all possible ports | Useful for all ports in use, including ephemeral (temporary) ports. |

### **DETECTION**

**What do you want to detect?**

| Example | Description | Use Case |
| --- | --- | --- |
| `-sV` | Probe for service/version | Useful for when mapping and identifying a network |
| `--version-light` | Try the most likely probes for detection | Useful for when mapping and identifying a network. |
| `--version-all` | Try every available probe (max intensity) | Useful for when mapping and identifying a network.. |
| `-O` | OS Detection | Useful for when mapping and identifying a network. |

### **TIMING**

**How fast do you want to scan?**

| Example | Description | Use Case |
| --- | --- | --- |
| `--max-rate 5` | Sends a maximum of 5 probes per second | Limits network traffic to avoid disruptions to the network. |
| `--scan-delay 1` | Adds 1 second delay between probes | Limits network traffic to avoid disruptions to the network. |
| `--host-timeout 1` | Give up on a particular port after 1 second | Limits network traffic and useful for slow responding devices. |

### **SCRIPTS**

**What additional scripts do you want?**

| Example | Description | Use Case |
| --- | --- | --- |
| `--script=whois` | Spoofs the source IP address | Used when mapping a network. |
| `--scripts=smb-enum-shares` | Adds random data to packets | Identifies SMB shares that might be exposed. |
| `--script=vulners` | Uses a proxy to scan | Identifies known/unpatched vulnerabilities in a network. |

### **EVASION**

**How sneaky do you want to be?**

| E...