---
title: Microsoft February 2025 Patch Tuesday, (Tue, Feb 11th)
url: https://isc.sans.edu/diary/rss/31674
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-12
fetch_date: 2025-10-06T20:40:06.231433
---

# Microsoft February 2025 Patch Tuesday, (Tue, Feb 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31668)
* [next](/diary/31676)

# [Microsoft February 2025 Patch Tuesday](/forums/diary/Microsoft%2BFebruary%2B2025%2BPatch%2BTuesday/31674/)

**Published**: 2025-02-11. **Last Updated**: 2025-02-11 20:02:21 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BFebruary%2B2025%2BPatch%2BTuesday/31674/#comments)

This month, Microsoft has released patches addressing a total of 141 vulnerabilities. Among these, 4 are classified as critical, highlighting the potential for significant impact if exploited. Notably, 2 vulnerabilities are currently being exploited in the wild, underscoring the urgency for immediate updates. Additionally, 1 vulnerability has been disclosed prior to this patch cycle, marking it as a zero-day. Users are strongly advised to prioritize these updates to safeguard their systems against potential threats.

**Significant Vulnerabilities**

**Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability ([CVE-2025-21418](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21418))**
This vulnerability, identified as CVE-2025-21418, has a severity rating of Important with a CVSS score of 7.8. It is currently being exploited in the wild but has not been publicly disclosed, making it a significant concern for affected systems. The vulnerability allows an attacker to gain SYSTEM privileges, thereby elevating their access and control over the compromised system. Immediate attention and remediation are advised to mitigate the risk posed by this vulnerability.

**Windows Storage Elevation of Privilege Vulnerability ([CVE-2025-21391](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21391))**
This is a disclosed vulnerability with a severity rating of Important and a CVSS score of 7.1, which is currently being exploited in the wild. This vulnerability allows an attacker to elevate their privileges to delete targeted files on a system, significantly impacting the integrity and availability of the system without compromising confidentiality. The exploitation of this vulnerability can lead to the deletion of critical data, potentially rendering services unavailable. Despite its exploitation, it has not been publicly disclosed as a zero-day, and users are advised to implement appropriate security measures to mitigate its impact.

**NTLM Hash Disclosure Spoofing Vulnerability ([CVE-2025-21377](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21377))**
This is a disclosed zero-day vulnerability with a severity rating of Important and a CVSS score of 6.5, though it is not currently exploited in the wild. This vulnerability can lead to a total loss of confidentiality by allowing an attacker to obtain a user's NTLMv2 hash, which could be used to authenticate as the user. Exploitation requires minimal user interaction, such as selecting or inspecting a malicious file. It affects all supported versions of Microsoft Windows, and despite the retirement of Internet Explorer 11 and the deprecation of Microsoft Edge Legacy, updates are necessary due to the continued use of the MSHTML and EdgeHTML platforms in various applications. To ensure full protection, users are advised to install both Security Only updates and IE Cumulative updates.

**Microsoft Dynamics 365 Sales Elevation of Privilege Vulnerability ([CVE-2025-21177](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21177))**
This vulnerability, identified as CVE-2025-21177, has not been exploited in the wild nor disclosed publicly, classifying it as a non-zero-day. It carries a severity rating of Critical with a CVSS score of 8.7, indicating a significant risk of elevation of privilege if exploited. Although the vulnerability could potentially allow attackers to gain unauthorized access and elevate their privileges within the Microsoft Dynamics 365 Sales environment, Microsoft has fully mitigated the issue, requiring no action from users. This CVE serves to enhance transparency regarding cloud service vulnerabilities.

**Windows Lightweight Directory Access Protocol (LDAP) Remote Code Execution Vulnerability ([CVE-2025-21376](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21376))**
This is a critical vulnerability with a CVSS score of 8.1, which has not been exploited in the wild nor disclosed publicly, thus not classified as a zero-day. This vulnerability allows for remote code execution, posing a significant threat if exploited. An unauthenticated attacker could exploit this vulnerability by sending a specially crafted request to a vulnerable LDAP server, potentially causing a buffer overflow. The attack complexity is high, as successful exploitation requires the attacker to win a race condition. Mitigation efforts should focus on securing LDAP servers and monitoring for unusual activity to prevent potential exploitation.

**Microsoft Excel Remote Code Execution Vulnerability ([CVE-2025-21381](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21381))**
This vulnerability, identified as CVE-2025-21381, has not been exploited in the wild nor disclosed publicly, making it a non-zero-day threat. It carries a severity rating of Critical with a CVSS score of 7.8, indicating a significant risk of remote code execution. Despite the CVSS metric indicating a local attack vector, the vulnerability allows an attacker to execute code remotely by convincing a user, through social engineering, to download and open a specially crafted file. The attack can be executed locally, with the Preview Pane serving as a potential attack vector. Users are advised to exercise caution when opening files from untrusted sources and to apply any available security updates to mitigate this risk.

**DHCP Client Service Remote Code Execution Vulnerability ([CVE-2025-21379](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21379))**
This vulnerability, identified as CVE-2025-21379, has not been exploited in the wild nor disclosed publicly, classifying it as a non-zero-day threat. It carries a severity rating of Critical with a CVSS score of 7.1, indicating a significant risk of remote code execution. The vulnerability requires a high attack complexity, necessitating a machine-in-the-middle (MITM) attack where the attacker must intercept the logical network path between the target and the resource. The attack vector is adjacent, meaning it is limited to systems on the same network segment, such as those connected to the same network switch or virtual network. This limitation prevents the attack from being executed across multiple networks, such as a WAN.

**Microsoft High Performance Compute (HPC) Pack Remote Code Execution Vulnerability ([CVE-2025-21198](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-21198))**
is a critical security flaw with a CVSS score of 9.0, rated as Important, and is currently neither exploited in the wild nor publicly disclosed. This vulnerability allows for remote code execution, requiring an attacker to have low privileges and access to the network connecting the targeted HPC clusters and nodes. The attack vector is adjacent, meaning it relies on intra-net or private network access rather than exposure to the public internet. Exploitation involves sending a specially crafted HTTPS request to the head node or Linux compute node, potentially allowing the attacker to execute code on other clusters or nodes connected to the targeted head node. The scope of the attack is changed, indicating that successful exploitation could lead to broader impacts beyond the initially compromised system.

**Windows ...