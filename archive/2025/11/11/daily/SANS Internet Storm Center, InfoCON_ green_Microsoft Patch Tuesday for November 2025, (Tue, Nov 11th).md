---
title: Microsoft Patch Tuesday for November 2025, (Tue, Nov 11th)
url: https://isc.sans.edu/diary/rss/32468
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-11
fetch_date: 2025-11-12T03:12:57.609653
---

# Microsoft Patch Tuesday for November 2025, (Tue, Nov 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32464)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Microsoft Patch Tuesday for November 2025](/forums/diary/Microsoft%2BPatch%2BTuesday%2Bfor%2BNovember%2B2025/32468/)

**Published**: 2025-11-11. **Last Updated**: 2025-11-11 19:24:30 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2Bfor%2BNovember%2B2025/32468/#comments)

Today's Microsoft Patch Tuesday offers fixes for 80 different vulnerabilities. One of the vulnerabilities is already being exploited, and five are rated as critical.

Notable Vulnerabilities:

[CVE-2025-62215](/vuln.html?cve=2025-62215): This vulnerability is already being exploited. It is a privilege escalation vulnerability in the Windows Kernel. These types of vulnerabilities are often exploited as part of a more complex attack chain; however, exploiting this specific vulnerability is likely to be relatively straightforward, given the existence of prior similar vulnerabilities.

[CVE-2025-60274](/vuln.html?cve=2025-60274): A critical GDI+ remote execution vulnerability. GDI+ parses various graphics files. The attack surface is likely huge, as anything in Windows (Browsers, email, and Office Documents) will use this library at some point to display images. We also have a critical vulnerability in Direct-X [CVE-2025-60716](/vuln.html?cve=2025-60716). Microsoft classifies this as a privilege escalation issue, yet still rates it as critical.

[CVE-2025-62199](/vuln.html?cve=2025-62199): A code execution vulnerability in Microsoft Office. Another component with a huge attack surface that is often exploited.

Given the number and type of vulnerabilities, I would consider this patch Tuesday "lighter than normal". There are no "Patch Now" vulnerabilities, and I suggest applying these vulnerabilities in accordance with your vulnerability management program.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Agentic AI and Visual Studio Code Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62222](/vuln.html?cve=2025-62222) | No | No | - | - | Important | 8.8 | 7.7 |
| An issue was discovered in libarchive bsdtar before version 3.8.1 in function apply\_substitution in file tar/subst.c when processing crafted -s substitution rules. This can cause unbounded memory allocation and lead to denial of service (Out-of-Memory crash). | | | | | | | |
| [CVE-2025-60753](/vuln.html?cve=2025-60753) | No | No | - | - | Moderate | 5.5 | 5.2 |
| Azure Monitor Agent Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-59504](/vuln.html?cve=2025-59504) | No | No | - | - | Important | 7.3 | 6.4 |
| Configuration Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-47179](/vuln.html?cve=2025-47179) | No | No | - | - | Important | 6.7 | 5.8 |
| Customer Experience Improvement Program (CEIP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-59512](/vuln.html?cve=2025-59512) | No | No | - | - | Important | 7.8 | 6.8 |
| DirectX Graphics Kernel Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-60723](/vuln.html?cve=2025-60723) | No | No | - | - | Important | 6.3 | 5.5 |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-59506](/vuln.html?cve=2025-59506) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2025-60716](/vuln.html?cve=2025-60716) | No | No | - | - | Critical | 7.0 | 6.1 |
| Dynamics 365 Field Service (online) Spoofing Vulnerability | | | | | | | |
| [CVE-2025-62210](/vuln.html?cve=2025-62210) | No | No | - | - | Important | 8.7 | 7.6 |
| [CVE-2025-62211](/vuln.html?cve=2025-62211) | No | No | - | - | Important | 8.7 | 7.6 |
| GDI+ Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-60724](/vuln.html?cve=2025-60724) | No | No | - | - | Critical | 9.8 | 8.5 |
| GitHub Copilot and Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2025-62453](/vuln.html?cve=2025-62453) | No | No | - | - | Important | 5.0 | 4.4 |
| Host Process for Windows Tasks Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-60710](/vuln.html?cve=2025-60710) | No | No | - | - | Important | 7.8 | 6.8 |
| KubeVirt Affected by an Authentication Bypass in Kubernetes Aggregation Layer | | | | | | | |
| [CVE-2025-64432](/vuln.html?cve=2025-64432) | No | No | - | - | Moderate | 4.7 | 4.5 |
| KubeVirt Arbitrary Container File Read | | | | | | | |
| [CVE-2025-64433](/vuln.html?cve=2025-64433) | No | No | - | - | Moderate | 6.5 | 6.2 |
| KubeVirt Excessive Role Permissions Could Enable Unauthorized VMI Migrations Between Nodes | | | | | | | |
| [CVE-2025-64436](/vuln.html?cve=2025-64436) | No | No | - | - | Moderate |  |  |
| KubeVirt Improper TLS Certificate Management Handling Allows API Identity Spoofing | | | | | | | |
| [CVE-2025-64434](/vuln.html?cve=2025-64434) | No | No | - | - | Moderate | 4.7 | 4.5 |
| KubeVirt Isolation Detection Flaw Allows Arbitrary File Permission Changes | | | | | | | |
| [CVE-2025-64437](/vuln.html?cve=2025-64437) | No | No | - | - | Moderate | 5.0 | 4.7 |
| KubeVirt VMI Denial-of-Service (DoS) Using Pod Impersonation | | | | | | | |
| [CVE-2025-64435](/vuln.html?cve=2025-64435) | No | No | - | - | Moderate | 5.3 | 5.0 |
| Libxml2: namespace use-after-free in xmlsettreedoc() function of libxml2 | | | | | | | |
| [CVE-2025-12863](/vuln.html?cve=2025-12863) | No | No | - | - | Important | 7.5 | 7.1 |
| Microsoft Dynamics 365 (On-Premises) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-62206](/vuln.html?cve=2025-62206) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-60726](/vuln.html?cve=2025-60726) | No | No | - | - | Important | 7.1 | 6.2 |
| [CVE-2025-60728](/vuln.html?cve=2025-60728) | No | No | - | - | Important | 4.3 | 3.8 |
| [CVE-2025-59240](/vuln.html?cve=2025-59240) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2025-62202](/vuln.html?cve=2025-62202) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-60727](/vuln.html?cve=2025-60727) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62200](/vuln.html?cve=2025-62200) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62201](/vuln.html?cve=2025-62201) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62203](/vuln.html?cve=2025-62203) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62199](/vuln.html?cve=2025-62199) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2025-62216](/vuln.html?cve=2025-62216) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62205](/vuln.html?cve=2025-62205) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft OneDrive for Android Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-60722](/vuln.html?cve=2025-60722) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-59499](/vuln.html?cve=2025-59499) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62204](/vuln.html?cve=2025-62204) | No | No | - | - | Important | 8.0 | 7.0 |
| Microsoft Streaming Service Proxy Elevatio...