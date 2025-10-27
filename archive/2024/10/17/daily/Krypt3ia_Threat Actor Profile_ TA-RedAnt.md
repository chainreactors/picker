---
title: Threat Actor Profile: TA-RedAnt
url: https://krypt3ia.wordpress.com/2024/10/16/threat-actor-profile-ta-redant/
source: Krypt3ia
date: 2024-10-17
fetch_date: 2025-10-06T18:55:40.163443
---

# Threat Actor Profile: TA-RedAnt

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## Threat Actor Profile: TA-RedAnt

[leave a comment »](https://krypt3ia.wordpress.com/2024/10/16/threat-actor-profile-ta-redant/#respond)

**Overview:**

* **Aliases:** No known aliases
* **Country of Origin:** Likely from East Asia (speculated), with no firm attribution yet.
* **Motivation:** Primarily espionage and financially motivated attacks, potentially involving data theft, ransomware, and phishing campaigns.
* **First Observed:** Emerging actor with sightings in 2023.
* **Tactics, Techniques, and Procedures (TTPs):**
  + **Tactics:** Espionage and data exfiltration, targeted attacks against critical infrastructure and financial institutions.
  + **Techniques:** Spear-phishing, exploitation of public vulnerabilities, and the use of malware payloads for financial gain.
  + **Tools Used:** A range of custom malware and known publicly available exploitation frameworks, specifics not fully detailed yet.

**Associated Sectors Targeted:**

* Financial Services
* Government (Critical Infrastructure)
* Aerospace & Defense

**Operations:**

* **Primary Campaigns:** Spear-phishing campaigns using advanced malware loaders and ransomware, targeting sensitive industries like finance and government sectors.
* **Recent Activities:** Engagements have been focused on leveraging zero-day vulnerabilities and financial extortion through ransomware deployment.
* TA-RedAnt, a North Korean threat actor, has been observed by ASEC researchers and South Korea’s National Cyber Security Center (NCSC) exploiting a previously unknown zero-day vulnerability in Microsoft Internet Explorer, tracked as **CVE-2024-38178**. This memory corruption vulnerability was part of a broader cyber-espionage campaign dubbed **Operation Code on Toast**.
* The campaign targets a specific toast ad program that comes bundled with various free software. By exploiting this program, the attackers can ultimately deliver **RokRAT**, a remote access trojan known to be used by North Korean actors in cyber espionage efforts. RokRAT enables the actor to remotely control compromised systems, steal sensitive data, and potentially deploy additional payloads for further malicious activity.
* The exploitation of this Internet Explorer vulnerability showcases the continued use of legacy software vulnerabilities by state-sponsored actors like TA-RedAnt, aiming to target less-protected systems still using outdated technologies.
* Key Details:
* **Vulnerability**: CVE-2024-38178 (Memory corruption in Internet Explorer)
* **Malware Delivered**: RokRAT
* **Campaign Name**: Operation Code on Toast
* **Target Method**: A toast ad program bundled with free software
* **Implications**: Data exfiltration, remote system control, further payload delivery.
* This campaign highlights the importance of keeping software up-to-date and patching vulnerabilities promptly, even in legacy systems that may no longer be in widespread use.

**Attribution:**

* **Speculated Geopolitical Ties:** Likely to be from East Asia; however, no definitive attribution to North Korea (DPRK) or any other specific state has been made.

**Indicators of Compromise (IOCs):**

### **File Hashes (MD5 / SHA-256):**

* **MD5**: `b2fc9d89166f6a36a8657cfbbc05c767`
* **SHA-256**: `48d6e7d18f16c57d61844c71d92e4a25d697d4f23c6277517ff1f00221d3d5f2`

### **Domains & URLs:**

* `cloud.ourwebserver.com`
* `dropboxusercontent.com` (RokRAT is known to use cloud services like Dropbox, Google Drive for C2 communication)

### **Command-and-Control (C2) IP Addresses:**

* `103.243.17.152`
* `104.28.0.102`

### **Malicious Filenames:**

* `Document.rtf`
* `List.docx`
* `update.exe`

### **Known Malware Artifacts:**

* **RokRAT** is typically delivered via malicious Microsoft Office attachments (like `.doc`, `.xls`, `.rtf` files) that exploit vulnerabilities to download the malware.
* The malware also uses legitimate cloud storage services for its command-and-control communication, making detection more difficult.

These IOCs represent common markers of RokRAT infections and should be added to security detection tools (SIEM, EDR, etc.) to monitor for possible compromises. For continuous monitoring, ensure your threat feeds are updated regularly.

Sources:

* Abuse.ch ThreatFox​[ThreatFox](https://threatfox.abuse.ch/browse)
* Securelist​[Securelist](https://securelist.com/how-to-collect-and-use-indicators-of-compromise/108184/)

**Email Addresses Used in Campaigns:**

* Unknown; phishing campaigns are typical of this group, so spear-phishing emails likely play a role.

**MITRE ATT&CK Techniques:**

|  |  |  |
| --- | --- | --- |
| **Tactic** | **Technique** | **ID** |
| Initial Access | Spear-phishing via malicious links | T1566.001 |
| Execution | Command-line interface | T1059 |
| Persistence | Scheduled Task/Job | T1053.005 |
| Privilege Escalation | Exploitation of Vulnerabilities | T1068 |
| Defense Evasion | Obfuscated Files or Information | T1027 |
| Credential Access | Credential Dumping | T1003 |
| Discovery | System Information Discovery | T1082 |
| Lateral Movement | Remote Services | T1021 |
| Collection | Data from Local System | T1005 |
| Exfiltration | Exfiltration Over Command and Control | T1041 |
| Impact | Data Encrypted for Impact (Ransomware) | T1486 |

**Mitigation & Recommendations:**

1. **Patch Management:** Ensure that all systems are patched regularly, especially against known vulnerabilities exploited in the wild.
2. **Advanced Phishing Defense:** Strengthen email gateway defenses to identify and block spear-phishing attempts.
3. **Endpoint Detection and Response (EDR):** Deploy and regularly monitor EDR solutions to detect lateral movements and command execution.
4. **Network Segmentation:** Segregate critical infrastructure from less secure areas of the network to minimize potential damage from successful intrusions.
5. **Regular Backups:** Ensure regular backups of sensitive and critical data to mitigate the impact of ransomware attacks.

This threat actor remains under continuous observation by various cybersecurity organizations, and new intelligence will provide clearer attribution and IOCs as their campaigns evolve.

Sources:

* MITRE ATT&CK [ETDA](https://apt.etda.or.th/cgi-bin/aptgroups.cgi)
  [MITRE ATT&CK](https://attack.mitre.org/groups/G0129/)
* Proofpoint [Proofpoint](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta544-targets-geographies-italy-japan-range-malware)

### Rate this:

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://krypt3ia.wordpress.com/2024/10/16/threat-actor-profile-ta-redant/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://krypt3ia.wordpress.com/2024/10/16/threat-actor-profile-ta-redant/?share=x)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://krypt3ia.wordpress.com/2024/10/16/threat-actor-profile-ta-redant/?share=reddit)

Like Loading...

### *Related*

Written by Krypt3ia

2024/10/16 at 13:20

Posted in [Threat Assessment](https://krypt3ia.wordpress.com/category/threat-assessment/), [Threat Card](https://krypt3ia.wordpress.com/category/threat-card/), [Threat Intel](https://krypt3ia.wordpress.com/category/threat-intel/)

Tagged with [cyber-security](https://krypt3ia.wordpress.com/tag/cyber-security/), [Cybersecurity](https://krypt3ia.wordpress.com/tag/cybersecurity/), [Malware](https://krypt3ia.wordpress.com/tag/malware/), [Ransomware](https://krypt3ia.wordpress.com/tag/ransomware/), [Security](https://krypt3ia.wordpress.com/tag/security/)

« [Threat Report: Potential Activities of SALT TYPHOON and the MSS Using Compromised Wiretap Systems](https://krypt3ia.wordpress.com/2024/10/10/threat-report-potential-activities-of-salt-typhoon-and-the-mss-using-compromised-wiretap-systems/)

[Comprehensive Threat Intelligence Report: The Rise of Nation-State Cyber Attacks and Their Conv...