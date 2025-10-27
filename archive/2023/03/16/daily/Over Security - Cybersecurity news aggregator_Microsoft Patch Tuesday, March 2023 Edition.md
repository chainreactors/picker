---
title: Microsoft Patch Tuesday, March 2023 Edition
url: https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-16
fetch_date: 2025-10-04T09:47:00.611234
---

# Microsoft Patch Tuesday, March 2023 Edition

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patch Tuesday, March 2023 Edition

March 15, 2023

[31 Comments](https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/#comments)

**Microsoft** on Tuesday released updates to quash at least 74 security bugs in its **Windows** operating systems and software. Two of those flaws are already being actively attacked, including an especially severe weakness in **Microsoft Outlook** that can be exploited without any user interaction.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

The Outlook vulnerability ([CVE-2023-23397](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397)) affects all versions of Microsoft Outlook from 2013 to the newest. Microsoft said it has seen evidence that attackers are exploiting this flaw, which can be done without any user interaction by sending a booby-trapped email that triggers automatically when retrieved by the email server — *before the email is even viewed in the Preview Pane*.

While CVE-2023-23397 is labeled as an “Elevation of Privilege” vulnerability, that label doesn’t accurately reflect its severity, said **Kevin Breen**, director of cyber threat research at **Immersive Labs**.

Known as an NTLM relay attack, it allows an attacker to get someone’s NTLM hash [Windows account password] and use it in an attack commonly referred to as “[Pass The Hash](https://en.wikipedia.org/wiki/Pass_the_hash).”

“The vulnerability effectively lets the attacker authenticate as a trusted individual without having to know the person’s password,” Breen said. “This is on par with an attacker having a valid password with access to an organization’s systems.”

Security firm **Rapid7** points out that this bug affects self-hosted versions of Outlook like **Microsoft 365 Apps for Enterprise**, but Microsoft-hosted online services like **Microsoft 365** are *not* vulnerable.

The other zero-day flaw being actively exploited in the wild — [CVE-2023-24880](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24880) — is a “Security Feature Bypass” in **Windows SmartScreen**, part of Microsoft’s slate of endpoint protection tools.

Patch management vendor **Action1** notes that the exploit for this bug is low in complexity and requires no special privileges. But it does require some user interaction, and can’t be used to gain access to private information or privileges. However, the flaw can allow other malicious code to run without being detected by SmartScreen reputation checks.

**Dustin Childs**, head of threat awareness at Trend Micro’s **Zero Day Initiative**, said CVE-2023-24880 allows attackers to create files that would bypass Mark of the Web (MOTW) defenses.

“Protective measures like SmartScreen and Protected View in Microsoft Office rely on MOTW, so bypassing these makes it easier for threat actors to spread malware via crafted documents and other infected files that would otherwise be stopped by SmartScreen,” Childs said.

Seven other vulnerabilities Microsoft patched this week earned its most-dire “critical” severity label, meaning the updates address security holes that could be exploited to give the attacker full, remote control over a Windows host with little or no interaction from the user.

Also this week, Adobe released eight patches addressing a whopping 105 security holes across a variety of products, including **Adobe Photoshop**, **Cold Fusion**, **Experience Manager**, **Dimension**, **Commerce**, **Magento**, **Substance 3D Stager**, **Cloud Desktop Applicatio**n, and **Illustrator**.

For a more granular rundown on the updates released today, see the [SANS Internet Storm Center roundup](https://isc.sans.edu/diary/Microsoft%20March%202023%20Patch%20Tuesday/29634). If today’s updates cause any stability or usability issues in Windows, [AskWoody.com](https://www.askwoody.com/2023/march-madness-here-we-come/) will likely have the lowdown on that.

Please consider backing up your data and/or imaging your system before applying any updates. And feel free to sound off in the comments if you experience any problems as a result of these patches.

*This entry was posted on Wednesday 15th of March 2023 11:19 AM*

[Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[CVE-2023-23397](https://krebsonsecurity.com/tag/cve-2023-23397/) [CVE-2023-24880](https://krebsonsecurity.com/tag/cve-2023-24880/) [Dustin Childs](https://krebsonsecurity.com/tag/dustin-childs/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [Kevin Breen](https://krebsonsecurity.com/tag/kevin-breen/) [Microsoft 365 Apps for Enterprise](https://krebsonsecurity.com/tag/microsoft-365-apps-for-enterprise/) [Microsoft Patch Tuesday March 2023](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-march-2023/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [Windows SmartScreen](https://krebsonsecurity.com/tag/windows-smartscreen/) [Zero Day Initiative](https://krebsonsecurity.com/tag/zero-day-initiative/)

Post navigation

[← Two U.S. Men Charged in 2022 Hacking of DEA Portal](https://krebsonsecurity.com/2023/03/two-us-men-charged-in-2022-hacking-of-dea-portal/)
[Feds Charge NY Man as BreachForums Boss “Pompompurin” →](https://krebsonsecurity.com/2023/03/feds-charge-ny-man-as-breachforums-boss-pompompurin/)

## 31 thoughts on “Microsoft Patch Tuesday, March 2023 Edition”

1. Mike Miller [March 15, 2023](https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/#comment-580057)

   Although not explicitly stated, I’m assuming that the scary bug discussed at the start of the post (CVE-2023-23397) would not affect Outlook that is based on a single PC, i.e., Outlook 2016 rather than the subscription/cloud-based version Outlook 365. Is that correct? (I’ve already installed the latest MS security update, so either way I’m probably OK.)

   1. Erich [March 16, 2023](https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/#comment-580125)

      It does affect
   2. [Mike Walters, Action1](https://www.action1.com/) [March 17, 2023](https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/#comment-580173)

      Hi Mike, according to the updates list for CVE-2023-23397 (source: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397>), the bug discussed affects all versions of MS Outlook from 2013 onwards, including Outlook 2016. Therefore, it’s important to stay vigilant and keep your software updated. It’s great to hear that you’ve already installed the latest MS security update – well done!
2. [Steve](http://n/a) [March 15, 2023](https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/#comment-580062)

   I use hotmail from a Mac, does this affect me? Obviously I can’t patch my non-windows computer. Does/will Microsoft fix this ‘globally’? i.e. I don’t have to do anything? I’m migrating to gmail, but still use hotmail somewhat. Thanks

   1. mealy [March 16, 2023](https://krebsonsecurity.com/2023/03/microsoft-patch-tuesday-march-2023-edition/#comment-580098)

      “S...