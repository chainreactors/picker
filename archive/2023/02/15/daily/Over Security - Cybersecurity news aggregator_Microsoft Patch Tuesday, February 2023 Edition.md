---
title: Microsoft Patch Tuesday, February 2023 Edition
url: https://krebsonsecurity.com/2023/02/microsoft-patch-tuesday-february-2023-edition/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-15
fetch_date: 2025-10-04T06:40:35.540390
---

# Microsoft Patch Tuesday, February 2023 Edition

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, February 2023 Edition

February 14, 2023

[15 Comments](https://krebsonsecurity.com/2023/02/microsoft-patch-tuesday-february-2023-edition/#comments)

**Microsoft** is sending the world a whole bunch of love today, in the form of patches to plug dozens of security holes in its **Windows** operating systems and other software. This year’s special Valentine’s Day Patch Tuesday includes fixes for a whopping three different “zero-day” vulnerabilities that are already being used in active attacks.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

Microsoft’s security advisories are somewhat sparse with details about the zero-day bugs. Redmond flags [CVE-2023-23376](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23376) as an “Important” elevation of privilege vulnerability in the **Windows Common Log File System Driver**, which is present in Windows 10 and 11 systems, as well as many server versions of Windows.

“Sadly, there’s just a little solid information about this privilege escalation,” said **Dustin Childs**, head of threat awareness at Trend Micro’s **Zero Day Initiative**. “Microsoft does note that the vulnerability would allow an attacker to exploit code as SYSTEM, which would allow them to completely take over a target. This is likely being chained with a remote code execution bug to spread malware or ransomware. Considering this was discovered by Microsoft’s Threat Intelligence Center, it could mean it was used by advanced threat actors. Either way, make sure you test and roll these fixes quickly.”

The zero-day [CVE-2023-21715](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21715) is a weakness in **Microsoft Office** that Redmond describes as a “security feature bypass vulnerability.”

“Microsoft lists this as under active exploit, but they offer no info on how widespread these exploits may be,” Childs said. “Based on the write-up, it sounds more like a privilege escalation than a security feature bypass, but regardless, active attacks in a common enterprise application shouldn’t be ignored. It’s always alarming when a security feature is not just bypassed but exploited. Let’s hope the fix comprehensively addresses the problem.”

The third zero-day flaw already seeing exploitation is [CVE-2023-21823](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21823), which is another elevation of privilege weakness — this one in the **Microsoft Windows Graphic** component. Researchers at cybersecurity forensics firm **Mandiant** were credited with reporting the bug.

**Kevin Breen**, director of cyber threat research at **Immersive Labs**, pointed out that the security bulletin for CVE-2023-21823 specifically calls out **OneNote** as being a vulnerable component for the vulnerability.

“In recent weeks, we have seen an increase in the use of OneNote files as part of [targeted malware campaigns](https://www.bleepingcomputer.com/news/security/hackers-now-use-microsoft-onenote-attachments-to-spread-malware/),” Breen said. “Patches for this are delivered via the app stores and not through the typical formats, so it’s important to double check your organization’s policies.”

Microsoft fixed another Office vulnerability in [CVE-2023-21716](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21716), which is a **Microsoft Word** bug that can lead to remote code execution — even if a booby-trapped Word document is merely viewed in the preview pane of **Microsoft Outlook**. This security hole has a CVSS (severity) score of 9.8 out of a possible 10.

Microsoft also has more valentines for organizations that rely on **Microsoft Exchange Server** to handle email. Redmond patched three Exchange Server flaws ([CVE-2023-21706](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21706), [CVE-2023-21707](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21707), and [CVE-2023-21529](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21529)), all of which Microsoft says are remote code execution flaws that are likely to be exploited.

Microsoft said authentication is required to exploit these bugs, but then again threat groups that attack Exchange vulnerabilities also tend to phish targets for their Exchange credentials.

Microsoft isn’t alone in dropping fixes for scary, ill-described zero-day flaws. Apple on Feb. 13 released an update for iOS that [resolves a zero-day vulnerability in Webkit](https://arstechnica.com/gadgets/2023/02/actively-exploited-webkit-vulnerability-fixed-in-ios-16-3-1-macos-13-2-1-updates/), Apple’s open source browser engine. **Johannes Ullrich** at the **SANS Internet Storm Center** notes that in addition to the WebKit problem, Apple fixed a privilege escalation issue. Both flaws are fixed in iOS 16.3.1.

“This privilege escalation issue could be used to escape the browser sandbox and gain full system access after executing code via the WebKit vulnerability,” Ullrich warned.

On a lighter note (hopefully), Microsoft drove the final nail in the coffin for **Internet Explorer 11 (IE11)**. According to Redmond, the out-of-support IE11 desktop application was permanently disabled on certain versions of Windows 10 on February 14, 2023 through a **Microsoft Edge** update.

“All remaining consumer and commercial devices that were not already redirected from IE11 to Microsoft Edge were redirected with the Microsoft Edge update. Users will be unable to reverse the change,” Microsoft [explained](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/internet-explorer-11-desktop-app-retirement-faq/ba-p/2366549). “Additionally, redirection from IE11 to Microsoft Edge will be included as part of all future Microsoft Edge updates. IE11 visual references, such as the IE11 icons on the Start Menu and taskbar, will be removed by the June 2023 Windows security update (“B” release) scheduled for June 13, 2023.”

For a more granular rundown on the updates released today, see [the SANS Internet Storm Center roundup](https://isc.sans.edu/diary/Microsoft%20February%202023%20Patch%20Tuesday/29548). If today’s updates cause any stability or usability issues in Windows, AskWoody.com will likely have the lowdown on that.

Please consider backing up your data and/or imaging your system before applying any updates. And feel free to sound off in the comments if you experience any problems as a result of these patches.

*This entry was posted on Tuesday 14th of February 2023 04:01 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2023-21529](https://krebsonsecurity.com/tag/cve-2023-21529/) [CVE-2023-21706](https://krebsonsecurity.com/tag/cve-2023-21706/) [CVE-2023-21707](https://krebsonsecurity.com/tag/cve-2023-21707/) [CVE-2023-21715](https://krebsonsecurity.com/tag/cve-2023-21715/) [CVE-2023-21716](https://krebsonsecurity.com/tag/cve-2023-21716/) [CVE-2023-21823](https://krebsonsecurity.com/tag/cve-2023-21823/) [CVE-2023-23376](https://krebsonsecurity.com/tag/cve-2023-23376/) [Dustin Childs](https://krebsonsecurity.c...