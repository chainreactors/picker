---
title: Microsoft May 2026 Patch Tuesday, (Tue, May 12th)
url: https://isc.sans.edu/diary/rss/32980
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-12
fetch_date: 2026-05-13T05:47:26.498901
---

# Microsoft May 2026 Patch Tuesday, (Tue, May 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/32976)
* [next](/diary/32982)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Microsoft May 2026 Patch Tuesday](/forums/diary/Microsoft%2BMay%2B2026%2BPatch%2BTuesday/32980/)

**Published**: 2026-05-12. **Last Updated**: 2026-05-12 18:29:36 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BMay%2B2026%2BPatch%2BTuesday/32980/#comments)

Today's Microsoft patch Tuesday fixes 137 different vulnerabilities. In addition, the update addresses 137 Chromium-related issues affecting Microsoft Edge.

There are no already disclosed or already exploited vulnerabilities included in today's patches. I removed the Chromium issues from the table below and included only the 137 Microsoft issues to make it more readable.

Note that issues related to Microsoft Azure are labeled as "no customer action required.

Significant Vulnerabilities of interest:

CVE-2026-41103: This vulnerability affects the Microsoft SSO Plugin for Jira & Confluence. Exploitation could lead to an elevation of privileges. With ongoing supply chain attacks, development and CI/CD tools like Jira and Confluence are popular targets.

CVE-2026-41089: A preauthentication remote code execution vulnerability in the Netlogon service will always be a juicy target, worth some AI tokens to write an exploit for.

Other critical vulnerabilities include the usual Word and Microsoft Office issues.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Core Tampering Vulnerability | | | | | | | |
| [CVE-2026-32175](/vuln.html?cve=2026-32175) | No | No | - | - | Important | 4.3 | 3.8 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32177](/vuln.html?cve=2026-32177) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-35433](/vuln.html?cve=2026-35433) | No | No | - | - | Important | 7.3 | 6.4 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-42899](/vuln.html?cve=2026-42899) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure AI Foundry Elevation of Privilege Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-35435](/vuln.html?cve=2026-35435) | No | No | - | - | Critical | 8.6 | 7.5 |
| Azure Cloud Shell Spoofing Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-35428](/vuln.html?cve=2026-35428) | No | No | - | - | Critical | 9.6 | 8.3 |
| Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40381](/vuln.html?cve=2026-40381) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure DevOps Information Disclosure Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-42826](/vuln.html?cve=2026-42826) | No | No | - | - | Critical | 10.0 | 8.7 |
| Azure Logic Apps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42823](/vuln.html?cve=2026-42823) | No | No | - | - | Important | 9.9 | 8.6 |
| Azure Machine Learning Notebook Spoofing Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-32207](/vuln.html?cve=2026-32207) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-33833](/vuln.html?cve=2026-33833) | No | No | - | - | Important | 8.2 | 7.1 |
| Azure Managed Instance for Apache Cassandra Remote Code Execution Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-33109](/vuln.html?cve=2026-33109) | No | No | - | - | Critical | 9.9 | 8.6 |
| [CVE-2026-33844](/vuln.html?cve=2026-33844) | No | No | - | - | Critical | 9.0 | 7.8 |
| Azure Monitor Action Group Notification System Elevation of Privilege Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-41105](/vuln.html?cve=2026-41105) | No | No | - | - | Critical | 8.1 | 7.1 |
| Azure Monitor Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32204](/vuln.html?cve=2026-32204) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Monitor Agent Metrics Extension Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42830](/vuln.html?cve=2026-42830) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure SDK for Java Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-33117](/vuln.html?cve=2026-33117) | No | No | - | - | Important | 9.1 | 7.9 |
| Copilot Chat (Microsoft Edge) Information Disclosure Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-33111](/vuln.html?cve=2026-33111) | No | No | - | - | Critical | 7.5 | 6.5 |
| Data Deduplication Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41095](/vuln.html?cve=2026-41095) | No | No | - | - | Important | 7.8 | 6.8 |
| GitHub Copilot and Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-41109](/vuln.html?cve=2026-41109) | No | No | - | - | Important | 8.8 | 7.7 |
| Internet Key Exchange (IKE) Protocol Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-35424](/vuln.html?cve=2026-35424) | No | No | - | - | Important | 7.5 | 6.5 |
| M365 Copilot Information Disclosure Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-26129](/vuln.html?cve=2026-26129) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-26164](/vuln.html?cve=2026-26164) | No | No | - | - | Critical | 7.5 | 6.5 |
| M365 Copilot for Desktop Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41614](/vuln.html?cve=2026-41614) | No | No | - | - | Important | 6.2 | 5.4 |
| Microsoft 365 Copilot for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41100](/vuln.html?cve=2026-41100) | No | No | - | - | Important | 4.4 | 3.9 |
| Microsoft Cryptographic Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40377](/vuln.html?cve=2026-40377) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Data Formulator Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-41094](/vuln.html?cve=2026-41094) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Dynamics 365 Business Central Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40417](/vuln.html?cve=2026-40417) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Dynamics 365 Customer Insights Elevation of Privilege Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-33821](/vuln.html?cve=2026-33821) | No | No | - | - | Critical | 7.7 | 6.7 |
| Microsoft Dynamics 365 On-Premises Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-42898](/vuln.html?cve=2026-42898) | No | No | - | - | Critical | 9.9 | 8.6 |
| [CVE-2026-42833](/vuln.html?cve=2026-42833) | No | No | - | - | Important | 9.1 | 7.9 |
| Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42838](/vuln.html?cve=2026-42838) | No | No | - | - | Important | 5.4 | 4.7 |
| Microsoft Edge (Chromium-based) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-41107](/vuln.html?cve=2026-41107) | No | No | - | - | Moderate | 7.4 | 6.4 |
| Microsoft Edge (Chromium-based) for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-42891](/vuln.html?cve=2026-42891) | No | No | - | - | Moderate | 6.5 | 5.7 |
| [CVE-2026-35429](/vuln.html?cve=2026-35429) | No | No | - | - | Moderate | 4.3 | 3.9 |
| [CVE-2026-40416](/vuln.html?cve=2026-40416) | No | No | - | - | Low | 4.3 | 3.8 |
| Microsoft Enterprise Security Token Service (ESTS) Spoofing Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-40379](/vuln.html?cve=2026-40379) | No | No | - | - | Critical | 9.3 | 8.1 |
| Microsoft Excel In...