---
title: Patch Tuesday, January 2026 Edition
url: https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-14
fetch_date: 2026-01-15T03:32:03.082019
---

# Patch Tuesday, January 2026 Edition

Advertisement

[![](/b-ninjio/9.png)](https://ninjio.com/lp46d-krebs/)

Advertisement

[![](/b-knowbe4/45.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, January 2026 Edition

January 13, 2026

[13 Comments](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/#comments)

**Microsoft** today issued patches to plug at least 113 security holes in its various **Windows** operating systems and supported software. Eight of the vulnerabilities earned Microsoft’s most-dire “critical” rating, and the company warns that attackers are already exploiting one of the bugs fixed today.

![](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

January’s Microsoft zero-day flaw — [CVE-2026-20805](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-20805) — is brought to us by a flaw in the **Desktop Window Manager** (DWM), a key component of Windows that organizes windows on a user’s screen. **Kev Breen**, senior director of cyber threat research at **Immersive**, said despite awarding CVE-2026-20805 a middling CVSS score of 5.5, Microsoft has confirmed its active exploitation in the wild, indicating that threat actors are already leveraging this flaw against organizations.

Breen said vulnerabilities of this kind are commonly used to undermine [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization) (ASLR), a core operating system security control designed to protect against buffer overflows and other memory-manipulation exploits.

“By revealing where code resides in memory, this vulnerability can be chained with a separate code execution flaw, transforming a complex and unreliable exploit into a practical and repeatable attack,” Breen said. “Microsoft has not disclosed which additional components may be involved in such an exploit chain, significantly limiting defenders’ ability to proactively threat hunt for related activity. As a result, rapid patching currently remains the only effective mitigation.”

**Chris Goettl**, vice president of product management at **Ivanti**, observed that CVE-2026-20805 affects all currently supported and extended security update supported versions of the Windows OS. Goettl said it would be a mistake to dismiss the severity of this flaw based on its “Important” rating and relatively low CVSS score.

“A risk-based prioritization methodology warrants treating this vulnerability as a higher severity than the vendor rating or CVSS score assigned,” he said.

Among the critical flaws patched this month are two **Microsoft Office** remote code execution bugs ([CVE-2026-20952](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-20952) and [CVE-2026-20953](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-20953)) that can be triggered just by viewing a booby-trapped message in the Preview Pane.

Our October 2025 Patch Tuesday [“End of 10” roundup](https://krebsonsecurity.com/2025/10/patch-tuesday-october-2025-end-of-10-edition/) noted that Microsoft had removed a modem driver from all versions after it was discovered that hackers were abusing a vulnerability in it to hack into systems. **Adam Barnett** at **Rapid7** said Microsoft today removed another couple of modem drivers from Windows for a broadly similar reason: Microsoft is aware of functional exploit code for an elevation of privilege vulnerability in a very similar modem driver, tracked as [CVE-2023-31096](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2023-31096).

“That’s not a typo; this vulnerability was originally published via MITRE over two years ago, along with a credible public writeup by the original researcher,” Barnett said. “Today’s Windows patches remove agrsm64.sys and agrsm.sys. All three modem drivers were originally developed by the same now-defunct third party, and have been included in Windows for decades. These driver removals will pass unnoticed for most people, but you might find active modems still in a few contexts, including some industrial control systems.”

According to Barnett, two questions remain: How many more legacy modem drivers are still present on a fully-patched Windows asset; and how many more elevation-to-SYSTEM vulnerabilities will emerge from them before Microsoft cuts off attackers who have been enjoying “living off the land[line] by exploiting an entire class of dusty old device drivers?”

“Although Microsoft doesn’t claim evidence of exploitation for CVE-2023-31096, the relevant 2023 write-up and the 2025 removal of the other Agere modem driver have provided two strong signals for anyone looking for Windows exploits in the meantime,” Barnett said. “In case you were wondering, there is no need to have a modem connected; the mere presence of the driver is enough to render an asset vulnerable.”

Immersive, Ivanti and Rapid7 all called attention to [CVE-2026-21265](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21265), which is a critical Security Feature Bypass vulnerability affecting Windows Secure Boot. This security feature is designed to protect against threats like rootkits and bootkits, and it relies on a set of certificates that are set to expire in June 2026 and October 2026. Once these 2011 certificates expire, Windows devices that do not have the new 2023 certificates can no longer receive Secure Boot security fixes.

Barnett cautioned that when updating the bootloader and BIOS, it is essential to prepare fully ahead of time for the specific OS and BIOS combination you’re working with, since incorrect remediation steps can lead to an unbootable system.

“Fifteen years is a very long time indeed in information security, but the clock is running out on the Microsoft root certificates which have been signing essentially everything in the Secure Boot ecosystem since the days of Stuxnet,” Barnett said. “Microsoft issued replacement certificates back in 2023, alongside CVE-2023-24932 which covered relevant Windows patches as well as subsequent steps to remediate the Secure Boot bypass exploited by the BlackLotus bootkit.”

Goettl noted that **Mozilla** has released updates for **Firefox** and **Firefox ESR** resolving a total of 34 vulnerabilities, two of which are suspected to be exploited (CVE-2026-0891 and CVE-2026-0892). Both are resolved in Firefox 147 (MFSA2026-01) and CVE-2026-0891 is resolved in Firefox ESR 140.7 (MFSA2026-03).

“Expect **Google Chrome** and **Microsoft Edge** updates this week in addition to a high severity vulnerability in Chrome WebView that was resolved in the January 6 Chrome update (CVE-2026-0628),” Goettl said.

As ever, the [SANS Internet Storm Center](https://isc.sans.edu/forums/diary/January%202026%20Microsoft%20Patch%20Tuesday%20Summary/32624/) has a per-patch breakdown by severity and urgency. Windows admins should keep an eye on [askwoody.com](https://www.askwoody.com/2026/january-2026-updates/) for any news about patches that don’t quite play nice with everything. If you experience any issues related installing January’s patches, please drop a line in the comments below.

*This entry was posted on Tuesday 13th of January 2026 07:47 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [CVE-2023-31096](https://krebsonsecurity.com/tag/cv...