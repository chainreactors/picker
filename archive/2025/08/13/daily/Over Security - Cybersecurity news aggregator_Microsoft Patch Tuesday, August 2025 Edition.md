---
title: Microsoft Patch Tuesday, August 2025 Edition
url: https://krebsonsecurity.com/2025/08/microsoft-patch-tuesday-august-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-13
fetch_date: 2025-10-07T00:48:17.083170
---

# Microsoft Patch Tuesday, August 2025 Edition

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, August 2025 Edition

August 12, 2025

[19 Comments](https://krebsonsecurity.com/2025/08/microsoft-patch-tuesday-august-2025-edition/#comments)

**Microsoft** today released updates to fix more than 100 security flaws in its **Windows** operating systems and other software. At least 13 of the bugs received Microsoft’s most-dire “critical” rating, meaning they could be abused by malware or malcontents to gain remote access to a Windows system with little or no help from users.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

August’s patch batch from Redmond includes an update for [CVE-2025-53786](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53786), a vulnerability that allows an attacker to pivot from a compromised **Microsoft Exchange Server** directly into an organization’s cloud environment, potentially gaining control over **Exchange Online** and other connected **Microsoft Office 365** services. Microsoft first warned about this bug on Aug. 6, saying it affects **Exchange Server 2016** and **Exchange Server 2019**, as well as its flagship **Exchange Server Subscription Edition**.

**Ben McCarthy**, lead cyber security engineer at **Immersive**, said a rough search reveals approximately 29,000 Exchange servers publicly facing on the internet that are vulnerable to this issue, with many of them likely to have even older vulnerabilities.

McCarthy said the fix for CVE-2025-53786 requires more than just installing a patch, such as following Microsoft’s manual instructions for creating a dedicated service to oversee and lock down the hybrid connection.

“In effect, this vulnerability turns a significant on-premise Exchange breach into a full-blown, difficult-to-detect cloud compromise with effectively living off the land techniques which are always harder to detect for defensive teams,” McCarthy said.

[CVE-2025-53779](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53779) is a weakness in the **Windows Kerberos** authentication system that allows an unauthenticated attacker to gain domain administrator privileges. Microsoft credits the discovery of the flaw to Akamai researcher **Yuval Gordon**, who dubbed it “**BadSuccessor**” in [a May 2025 blog post](https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory). The attack exploits a weakness in “delegated Managed Service Account” or dMSA — a feature that was introduced in **Windows Server 2025**.

Some of the critical flaws addressed this month with the highest severity (between 9.0 and 9.9 CVSS scores) include a remote code execution bug in the **Windows GDI+** component that handles graphics rendering ([CVE-2025-53766](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53766)) and [CVE-2025-50165](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-50165), another graphics rendering weakness. Another critical patch involves [CVE-2025-53733](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-53733), a vulnerability in **Microsoft Word** that can be exploited without user interaction and triggered through the Preview Pane.

One final critical bug tackled this month deserves attention: [CVE-2025-53778](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53778), a bug in **Windows NTLM**, a core function of how Windows systems handle network authentication. According to Microsoft, the flaw could allow an attacker with low-level network access and basic user privileges to exploit NTLM and elevate to SYSTEM-level access — the highest level of privilege in Windows. Microsoft rates the exploitation of this bug as “more likely,” although there is no evidence the vulnerability is being exploited at the moment.

Feel free to holler in the comments if you experience problems installing any of these updates. As ever, the **SANS Internet Storm Center** has its [useful breakdown](https://isc.sans.edu/diary/Microsoft%20August%202025%20Patch%20Tuesday/32192) of the Microsoft patches indexed by severity and CVSS score, and [AskWoody.com](https://www.askwoody.com/2025/august-2025-security-updates/) is keeping an eye out for Windows patches that may cause problems for enterprises and end users.

## GOOD MIGRATIONS

Windows 10 users out there likely have noticed by now that Microsoft really wants you to upgrade to Windows 11. The reason is that after the Patch Tuesday on October 14, 2025, Microsoft will stop shipping free security updates for **Windows 10** computers. The trouble is, many PCs running Windows 10 do not meet the hardware specifications required to install **Windows 11**(or they do, but just barely).

If the experience with Windows XP is any indicator, many of these older computers will wind up in landfills or else will be left running in an unpatched state. But if your Windows 10 PC doesn’t have the hardware chops to run Windows 11 and you’d still like to get some use out of it safely, consider installing a newbie-friendly version of Linux, like **Linux Mint**.

Like most modern Linux versions, Mint will run on anything with a 64-bit CPU that has at least 2GB of memory, although 4GB is recommended. In other words, it will run on almost any computer produced in the last decade.

There are many versions of Linux available, but Linux Mint is likely to be the most intuitive interface for regular Windows users, and it is largely configurable without any fuss at the text-only command-line prompt. Mint and other flavors of Linux come with **LibreOffice**, which is an open source suite of tools that includes applications similar to Microsoft Office, and it can open, edit and save documents as Microsoft Office files.

If you’d prefer to give Linux a test drive before installing it on a Windows PC, you can always just download it to a removable USB drive. From there, reboot the computer (with the removable drive plugged in) and select the option at startup to run the operating system from the external USB drive. If you don’t see an option for that after restarting, try restarting again and hitting the F8 button, which should open a list of bootable drives. [Here’s a fairly thorough tutorial](https://www.youtube.com/watch?v=_qZI6i21jB4) that walks through exactly how to do all this.

And if this is your first time trying out Linux, relax and have fun: The nice thing about a “live” version of Linux (as it’s called when the operating system is run from a removable drive such as a CD or a USB stick) is that none of your changes persist after a reboot. Even if you somehow manage to break something, a restart will return the system back to its original state.

*This entry was posted on Tuesday 12th of August 2025 06:14 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Akamai](https://krebsonsecurity.com/tag/akamai/) [BadSuccessor](https://krebsonsecurity.com/tag/badsuccessor/) [Ben McCarthy](https://krebsonsecurity.com/tag/ben-mccarthy/) [CVE-2025-50165](https://krebsonsecurity.com/tag/cve-2025-50165/) [CVE-2025-53733](https://krebsonsecurity.com/tag/cve-2025-53733/) [CVE-2025-53766](https://krebsonsecurity.com/tag/cve-2025-53766/) [CVE-2025-53778](https://krebsonsecurity.com...