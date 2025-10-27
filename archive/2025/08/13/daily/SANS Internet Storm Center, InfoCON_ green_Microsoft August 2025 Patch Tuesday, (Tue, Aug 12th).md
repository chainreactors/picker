---
title: Microsoft August 2025 Patch Tuesday, (Tue, Aug 12th)
url: https://isc.sans.edu/diary/rss/32192
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-13
fetch_date: 2025-10-07T01:01:32.145854
---

# Microsoft August 2025 Patch Tuesday, (Tue, Aug 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32186)
* [next](/diary/32196)

# [Microsoft August 2025 Patch Tuesday](/forums/diary/Microsoft%2BAugust%2B2025%2BPatch%2BTuesday/32192/)

**Published**: 2025-08-12. **Last Updated**: 2025-08-12 18:30:52 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BAugust%2B2025%2BPatch%2BTuesday/32192/#comments)

This month's Microsoft patch update addresses a total of 111 vulnerabilities, with 17 classified as critical. Among these, one vulnerability was disclosed prior to the patch release, marking it as a zero-day. While none of the vulnerabilities have been exploited in the wild, the critical ones pose significant risks, including remote code execution and elevation of privilege. Users are strongly advised to apply the updates promptly to safeguard their systems against potential threats.

**Windows Kerberos Elevation of Privilege Vulnerability** ([CVE-2025-53779](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53779)) is a disclosed zero-day vulnerability with a CVSS score of 7.2, rated as Moderate in severity. Although it has not been exploited in the wild, it poses a significant risk as it allows an attacker to gain domain administrator privileges. To exploit this vulnerability, an attacker would need high privileges, specifically access to certain attributes of the dMSA, such as msds-groupMSAMembership and msds-ManagedAccountPrecededByLink. These attributes enable the attacker to utilize the dMSA and specify a user that the dMSA can act on behalf of, potentially compromising the security of the domain.

**Windows Graphics Component Remote Code Execution Vulnerability** ([CVE-2025-50165](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-50165)) is a critical vulnerability with a CVSS score of 9.8, which has not been exploited in the wild nor disclosed publicly as a zero-day. This vulnerability allows for remote code execution, posing a significant threat due to its ability to be exploited without any user interaction. The attack vector is network-based, and the vulnerability arises from an uninitialized function pointer being called when decoding a JPEG image, which can be embedded in Office and third-party documents or files. Successful exploitation could enable an attacker to execute arbitrary code remotely, highlighting the critical need for immediate attention and remediation to prevent potential exploitation.

**GDI+ Remote Code Execution Vulnerability** ([CVE-2025-53766](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53766)) is a critical vulnerability with a CVSS score of 9.8, which has not been exploited in the wild nor disclosed publicly as a zero-day. This vulnerability allows for remote code execution on web services parsing documents with specially crafted metafiles, without requiring any user interaction or privileges from the attacker. The attack vector is network-based, meaning an attacker could exploit this vulnerability by uploading such documents to web services, potentially leading to significant security breaches. The Preview Pane is not considered an attack vector for this vulnerability, and mitigation strategies should focus on securing web services against unauthorized document uploads.

**Azure Portal Elevation of Privilege Vulnerability** ([CVE-2025-53792](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53792)) is a critical vulnerability with a CVSS score of 9.1, which has not been exploited in the wild nor disclosed publicly, thus not qualifying as a zero-day. This vulnerability allows for elevation of privilege, potentially enabling unauthorized access to sensitive resources within the Azure Portal. Despite its critical severity, Microsoft has already fully mitigated this vulnerability, and no further action is required from users of the service. The CVE was issued to provide transparency regarding the vulnerability and its resolution, aligning with Microsoft's commitment to greater transparency in cloud service security.

**Windows NTLM Elevation of Privilege Vulnerability** ([CVE-2025-53778](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53778)) is a critical vulnerability, identified as CVE-2025-53778, has not been exploited in the wild nor disclosed publicly as a zero-day. It carries a CVSS score of 8.8, indicating its high severity. The vulnerability allows an attacker to elevate their privileges to SYSTEM level, posing a significant risk to affected systems. Although currently not exploited, organizations are advised to implement mitigation strategies to prevent potential exploitation and ensure the security of their systems.

**Microsoft Office Remote Code Execution Vulnerability** ([CVE-2025-53731](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53731)) is a critical vulnerability with a CVSS score of 8.4, which has neither been exploited in the wild nor disclosed as a zero-day. This vulnerability allows for remote code execution, meaning an attacker can execute arbitrary code on the affected system, although the attack must be initiated locally. The Preview Pane in Microsoft Office serves as an attack vector, enabling the execution of malicious code when a user previews a compromised document. Despite the remote nature of the attacker's location, the exploit requires local execution, posing significant security risks if not addressed. Users are advised to apply necessary patches and updates to mitigate potential threats.

**Microsoft Word Remote Code Execution Vulnerability** ([CVE-2025-53733](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53733)) is a critical vulnerability with a CVSS score of 8.4, which has not been exploited in the wild nor disclosed publicly, thus not qualifying as a zero-day. This vulnerability allows for remote code execution, although the attack vector is local, meaning the attacker or victim must execute code from the local machine. The Preview Pane in Microsoft Word serves as an attack vector for this vulnerability, potentially enabling arbitrary code execution. Users are advised to apply all relevant updates for their software to mitigate this risk, as multiple update packages may be necessary to fully address the vulnerability.

**Microsoft Office Remote Code Execution Vulnerability** ([CVE-2025-53740](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53740)) is a critical vulnerability that has not been exploited in the wild nor disclosed publicly, making it a potential zero-day threat. With a CVSS score of 8.4, this vulnerability allows for remote code execution, posing a significant risk to systems running Microsoft Office. Despite the attack vector being local, the term "Remote" refers to the attacker's location, indicating that the exploit can be initiated by executing code on the local machine. The Preview Pane in Microsoft Office is identified as a potential attack vector, which could be leveraged by attackers to execute arbitrary code. Users are advised to remain vigilant and apply necessary security measures to mitigate potential risks associated with this vulnerability.

**Microsoft Word Remote Code Execution Vulnerability** ([CVE-2025-53784](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-53784)) is a critical vulnerability with a CVSS score of 8.4, which has not been exploited in the wild nor disclosed publicly, thus not qualifying as a zero-day. This vulnerability allows for remote code execution, meaning an attacker can execute arbitrary code on the affected system, although the attack must be initiated locally. The vulnerability is particula...