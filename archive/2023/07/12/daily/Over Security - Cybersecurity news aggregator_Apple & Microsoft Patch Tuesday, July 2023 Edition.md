---
title: Apple & Microsoft Patch Tuesday, July 2023 Edition
url: https://krebsonsecurity.com/2023/07/apple-microsoft-patch-tuesday-july-2023-edition/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:57:19.211867
---

# Apple & Microsoft Patch Tuesday, July 2023 Edition

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Apple & Microsoft Patch Tuesday, July 2023 Edition

July 11, 2023

[12 Comments](https://krebsonsecurity.com/2023/07/apple-microsoft-patch-tuesday-july-2023-edition/#comments)

**Microsoft Corp.** today released software updates to quash 130 security bugs in its **Windows** operating systems and related software, including at least five flaws that are already seeing active exploitation. Meanwhile, **Apple** customers have their own zero-day woes again this month: On Monday, Apple issued (and then quickly pulled) an emergency update to fix a zero-day vulnerability that is being exploited on **MacOS** and **iOS** devices.

![](https://krebsonsecurity.com/wp-content/uploads/2023/07/applegear.png)

On July 10, Apple pushed a “Rapid Security Response” update to fix a code execution flaw in the Webkit browser component built into iOS, iPadOS, and macOS Ventura. Almost as soon as the patch went out, Apple pulled the software because it was reportedly causing problems loading certain websites. *MacRumors* [says](https://www.macrumors.com/2023/07/10/apple-pulls-ios-16-5-1-macos-13-4-1-rsrs/) Apple will likely re-release the patches when the glitches have been addressed.

Launched in May, Apple’s Rapid Security Response updates are designed to address time-sensitive vulnerabilities, and this is the second month Apple has used it. July marks the sixth month this year that Apple has released updates for zero-day vulnerabilities — those that get exploited by malware or malcontents before there is an official patch available.

If you rely on Apple devices and don’t have automatic updates enabled, please take a moment to check the patch status of your various iDevices. The latest security update that includes the fix for the zero-day bug should be available in **iOS/iPadOS 16.5.1**, **macOS 13.4.1**, and **Safari 16.5.2**.

On the Windows side, there are at least four vulnerabilities patched this month that earned high CVSS (badness) scores and that are already being exploited in active attacks, according to Microsoft. They include [CVE-2023-32049](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-32049), which is a hole in **Windows SmartScreen** that lets malware bypass security warning prompts; and [CVE-2023-35311](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-35311) allows attackers to bypass security features in **Microsoft Outlook**.

The two other zero-day threats this month for Windows are both privilege escalation flaws. [CVE-2023-32046](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-32046) affects a core Windows component called MSHTML, which is used by Windows and other applications, like **Office**, Outlook and **Skype**. [CVE-2023-36874](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36874) is an elevation of privilege bug in the **Windows Error Reporting Service**.

Many security experts expected Microsoft to address a fifth zero-day flaw — [CVE-2023-36884](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36884) — a remote code execution weakness in Office and Windows.

“Surprisingly, there is no patch yet for one of the five zero-day vulnerabilities,” said **Adam Barnett**, lead software engineer at Rapid7. “Microsoft is actively investigating publicly disclosed vulnerability, and promises to update the advisory as soon as further guidance is available.”

Barnett notes that Microsoft links exploitation of this vulnerability with **Storm-0978**, the software giant’s name for a cybercriminal group based out of Russia that is identified by the broader security community as [RomCom](https://blogs.blackberry.com/en/2023/06/romcom-resurfaces-targeting-ukraine).

“Exploitation of CVE-2023-36884 may lead to installation of the eponymous RomCom trojan or other malware,” Barnett said. “[Microsoft] suggests that RomCom / Storm-0978 is operating in support of Russian intelligence operations. The same threat actor has also been associated with ransomware attacks targeting a wide array of victims.”

Microsoft’s [advisory on CVE-2023-36884](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36884) is pretty sparse, but it does include a Windows registry hack that should help mitigate attacks on this vulnerability. Microsoft has also published [a blog post](https://www.microsoft.com/en-us/security/blog/2023/07/11/storm-0978-attacks-reveal-financial-and-espionage-motives/) about phishing campaigns tied to Storm-0978 and to the exploitation of this flaw.

Barnett said it’s while it’s possible that a patch will be issued as part of next month’s Patch Tuesday, Microsoft Office is deployed just about everywhere, and this threat actor is making waves.

“Admins should be ready for an out-of-cycle security update for CVE-2023-36884,” he said.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

Microsoft also today released new details about how it plans to address the existential threat of malware that is cryptographically signed by…wait for it….Microsoft.

In late 2022, security experts at **Sophos**, **Trend Micro** and **Cisco** warned that ransomware criminals were using signed, malicious drivers in an attempt to evade antivirus and endpoint detection and response (EDR) tools.

In a blog post today, Sophos’s **Andrew Brandt** [wrote](https://news.sophos.com/en-us/2023/07/11/microsoft-revokes-malicious-drivers-in-patch-tuesday-culling/) that Sophos identified 133 malicious Windows driver files that were digitally signed since April 2021, and *found 100 of those were actually signed by Microsoft.* Microsoft [said](https://msrc.microsoft.com/update-guide/vulnerability/ADV220005) today it is taking steps to ensure those malicious driver files can no longer run on Windows computers.

As KrebsOnSecurity noted in [last month’s story on malware signing-as-a-service](https://krebsonsecurity.com/2023/06/ask-fitis-the-bear-real-crooks-sign-their-malware/), code-signing certificates are supposed to help authenticate the identity of software publishers, and provide cryptographic assurance that a signed piece of software has not been altered or tampered with. Both of these qualities make stolen or ill-gotten code-signing certificates attractive to cybercriminal groups, who prize their ability to add stealth and longevity to malicious software.

**Dan Goodin** at *Ars Technica* contends that whatever Microsoft may be doing to keep maliciously signed drivers from running on Windows is being bypassed by hackers using open source software that is popular with video game cheaters.

“The software comes in the form of two software tools that are available on GitHub,” Goodin [explained](https://arstechnica.com/security/2023/07/hackers-exploit-gaping-windows-loophole-to-give-their-malware-kernel-access/). “Cheaters use them to digitally sign malicious system drivers so they can modify video games in ways that give the player an unfair advantage. The drivers clear the considerable hurdle required for the cheat code to run inside the Windows kernel, the fortified layer of the operating system reserved for the most critical and sensitive functions.”

Meanwhile, researchers at Cisco’s Talos security team f...