---
title: Microsoft January 2025 Patch Tuesday, (Tue, Jan 14th)
url: https://isc.sans.edu/diary/rss/31590
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-15
fetch_date: 2025-10-06T20:13:48.692736
---

# Microsoft January 2025 Patch Tuesday, (Tue, Jan 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31586)
* [next](/diary/31592)

# [Microsoft January 2025 Patch Tuesday](/forums/diary/Microsoft%2BJanuary%2B2025%2BPatch%2BTuesday/31590/)

**Published**: 2025-01-14. **Last Updated**: 2025-01-14 18:40:40 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BJanuary%2B2025%2BPatch%2BTuesday/31590/#comments)

This month's Microsoft patch update addresses a total of 209 vulnerabilities, including 12 classified as critical. Among these, 3 vulnerabilities have been actively exploited in the wild, and 5 have been disclosed prior to the patch release, marking them as zero-days. The updates span various components, with significant attention required for vulnerabilities that could lead to privilege escalation and remote code execution. Users and administrators are strongly advised to prioritize the application of these patches to safeguard against potential threats and maintain system integrity.

**Noteworthy Vulnerabilities:**

**Windows Hyper-V NT Kernel Integration VSP Elevation of Privilege Vulnerability ([CVE-2025-21333](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21333))** along with CVE-2025-21334 and CVE-2025-21335 are a serious security issue that has been exploited in the wild, although it has not been publicly disclosed. This vulnerability has a CVSS score of 7.8 and is rated as Important due to its potential impact, which allows an attacker to gain SYSTEM privileges through elevation of privilege. The vulnerability affects the Windows Hyper-V NT Kernel Integration VSP, and successful exploitation could lead to significant security breaches. Users and administrators are advised to apply any available patches or mitigation strategies to protect against potential attacks leveraging this vulnerability.

**Microsoft Access Remote Code Execution Vulnerability ([CVE-2025-21186](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21186))** is a disclosed zero-day vulnerability with a severity rating of Important and a CVSS score of 7.8, though it is not currently being exploited in the wild. This vulnerability allows for remote code execution, where an attacker can execute arbitrary code on a victim's machine by convincing them, through social engineering, to download and open a specially crafted file. Despite the attack vector being local, the term "Remote" in the title refers to the attacker's location. The vulnerability poses a significant risk as it could lead to unauthorized code execution on affected systems. The recommended remediation involves applying the update that blocks potentially malicious extensions from being sent via email, thereby mitigating the risk of exploitation.

**Windows App Package Installer Elevation of Privilege Vulnerability ([CVE-2025-21275](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21275))** is a disclosed zero-day vulnerability with a severity rating of Important and a CVSS score of 7.8. Although it has not been exploited in the wild, this vulnerability poses a significant risk as it allows an attacker to gain SYSTEM privileges through elevation of privilege. The vulnerability affects the Windows App Package Installer, and successful exploitation could lead to unauthorized access and control over affected systems. Users and administrators are advised to apply necessary patches and follow security best practices to mitigate potential risks associated with this vulnerability.

**Microsoft Access Remote Code Execution Vulnerability ([CVE-2025-21366](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21366))** is a disclosed zero-day vulnerability with a severity rating of Important and a CVSS score of 7.8, although it is not currently exploited in the wild. This vulnerability allows for remote code execution, where an attacker can execute arbitrary code on a victim's system by convincing them to download and open a specially crafted file, despite the attack vector being local. The vulnerability is mitigated by updates that block potentially malicious extensions from being sent via email, thereby preventing the execution of harmful code.

**Microsoft Access Remote Code Execution Vulnerability ([CVE-2025-21395](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21395))** is a disclosed zero-day vulnerability with a severity rating of Important and a CVSS score of 7.8, though it is not currently being exploited in the wild. This vulnerability allows for remote code execution, where an attacker, located remotely, can execute arbitrary code on a victim's machine by convincing them to download and open a specially crafted file, despite the attack vector being local. The vulnerability is mitigated by an update that blocks potentially malicious extensions from being sent via email, thereby preventing the execution of harmful code.

**Windows Themes Spoofing Vulnerability ([CVE-2025-21308](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21308))** is a disclosed zero-day vulnerability with a severity rating of Important and a CVSS score of 6.5, though it is not currently exploited in the wild. This spoofing vulnerability requires user interaction, where an attacker must convince a user to load and manipulate a malicious file, typically through enticements in emails or instant messages. Systems that have disabled NTLM are not affected, and mitigation strategies include applying group policies to block NTLM hashes. Specifically, enabling the policy to restrict NTLM traffic to remote servers can mitigate this issue for remote SMB location clients or servers. This vulnerability highlights the importance of secure configurations and user awareness to prevent potential exploitation.

**Windows OLE Remote Code Execution Vulnerability ([CVE-2025-21298](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21298))** is a critical vulnerability with a CVSS score of 9.8, which has not been exploited in the wild nor disclosed publicly, making it a potential zero-day threat. This vulnerability allows for remote code execution, posing a significant risk if exploited. An attacker could leverage this vulnerability in an email attack scenario by sending a specially crafted email to a victim using an affected version of Microsoft Outlook. The attack could be triggered either by the victim opening the email or by the Outlook application displaying a preview of it, potentially allowing the attacker to execute arbitrary code on the victim's machine. Object Linking and Embedding (OLE), the technology involved, facilitates embedding and linking to documents and other objects, which is central to this vulnerability's exploitation method.

**Windows Reliable Multicast Transport Driver (RMCAST)** Remote Code Execution Vulnerability ([CVE-2025-21307](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21307)) is a critical vulnerability with a CVSS score of 9.8, which has not been exploited in the wild nor disclosed publicly as a zero-day. This vulnerability allows an unauthenticated attacker to execute remote code by sending specially crafted packets to a Windows Pragmatic General Multicast (PGM) open socket on the server, without requiring any user interaction. The vulnerability is only exploitable if there is a program actively listening on a PGM port. To mitigate this risk, it is recommended to protect access to any open PGM ports at the network level, such as using a firewall, and to avoid exposing a PGM receiver to the public internet.

This summary of Microsoft's monthly updates highlights critical vulnerabilities requiring immediate attention. Notably, the W...