---
title: Microsoft Patches More Than 1,400 Security Flaws
url: https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/
source: Over Security
date: 2026-10-13
fetch_date: 2026-10-14T06:53:01.789711
---

# Microsoft Patches More Than 1,400 Security Flaws

Advertisement

[![](/b-doppel/17.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

[![](/b-flashpoint/6.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Patches More Than 1,400 Security Flaws

October 13, 2026

[3 Comments](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/#comments)

**Microsoft** today issued updates to fix more than 1,400 security vulnerabilities in its **Windows** operating systems and other software. Today’s epic patch batch dwarfs September’s record of nearly 1,000 fixes, which was already about ten times the normal monthly patch load from Redmond.

![](https://krebsonsecurity.com/wp-content/uploads/2020/08/windowsec.png)

Just one of the weaknesses patched this week is considered a “zero day,” or already exploited in the wild. [CVE-2026-96951](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-96951) is a security feature bypass in the **Windows Shell** that affects Windows 10 and 11 systems, as well as some Server versions.

Windows 10 users might be wondering if they can still expect security updates after this month. Microsoft had been slated to stop shipping updates for Windows 10 systems in October 2025, but ended up adding another year of free updates after considerable pushback. A few months ago, Microsoft [quietly extended that support](https://www.windowscentral.com/microsoft/windows-10/microsoft-quietly-extends-windows-10s-extra-security-updates-program-for-free-users-can-now-stay-on-windows-10-until-october-2027-securely) for another year (until October 2027).

At least 78 of the flaws fixed this month are rated “critical,” meaning they could be exploited with little or no action by the user, and most of those critical bugs allow an attacker to execute code of their choice on the vulnerable system.

While Microsoft said there are no signs anyone is exploiting it yet, a security feature bypass in the .NET Framework ([CVE-2026-108398](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-108398)) was publicly disclosed prior to today, potentially giving attackers advance time to work out how to exploit the bug.

**Satnam Narang** at **Tenable** said the number of flaws fixed this month far surpasses the previous record-setting year 2020, when Microsoft patched 1,261 CVEs.

“We’ve now crossed the 4,000 CVE mark with two months left to go,” he said.

Microsoft credits large language models for the high volume of bug discovery, and presumably AI gets credit for many of the patches used to fix these flaw. Meanwhile, security experts have been warning that these unusually large patch volleys from Microsoft are placing extra strain on corporate security teams, which often have to test individual updates before deploying them across a network to ensure the fixes don’t cause problems for other software.

**Tyler Reguly**, associate director of security research and development at **Fortra**, notes that just 26 Microsoft vulnerabilities appeared in the “Known Exploited Vulnerabilities” (KEV) catalog maintained by the U.S. Cybersecurity & Infrastructure Security Agency (CISA) so far this year, and security teams would do well to prioritize patching those 26 vulnerabilities first.

“Security leaders should focus on exploitable risk, and ask whether their teams have the clarity, capacity and support to act,” Reguly said.

Which vulnerabilities deserve the most scrutiny in your organization? The folks at **Cisco Talos** have [a useful roundup](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-october-2026/) of the more noteworthy flaws that Microsoft fixed today, and of course the **SANS Internet Storm Center** has [a reliable roundup](https://isc.sans.edu/diary/October%202026%20Microsoft%20Patch%20Tuesday/33422) that indexes vulnerabilities by severity, CVE number and affected software.

*This entry was posted on Tuesday 13th of October 2026 07:24 PM*

[Security Tools](https://krebsonsecurity.com/category/security-tools/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[.NET](https://krebsonsecurity.com/tag/net/) [Cisco Talos](https://krebsonsecurity.com/tag/cisco-talos/) [CVE-2026-108398](https://krebsonsecurity.com/tag/cve-2026-108398/) [CVE-2026-96951](https://krebsonsecurity.com/tag/cve-2026-96951/) [Fortra](https://krebsonsecurity.com/tag/fortra/) [microsoft](https://krebsonsecurity.com/tag/microsoft/) [Patch Tuesday October 2026](https://krebsonsecurity.com/tag/patch-tuesday-october-2026/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [Tyler Reguly](https://krebsonsecurity.com/tag/tyler-reguly/) [Windows 10 updates](https://krebsonsecurity.com/tag/windows-10-updates/) [Windows shell](https://krebsonsecurity.com/tag/windows-shell/)

Post navigation

[← FBI Arrests Executive at Ransomware Negotiation Firm](https://krebsonsecurity.com/2026/10/fbi-arrests-founder-of-ransomware-negotiation-firm/)

## 3 thoughts on “Microsoft Patches More Than 1,400 Security Flaws”

1. Richard Boyce [October 13, 2026](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/#comment-661211)

   One has to wonder how big the backlog of flaws is at this point. Maybe this month’s increase in the number of fixes just reflects an increasing number of people working on these fixes, and that they already have enough flaws to keep them all busy for a long time. Oh to be a fly on the wall.

   [Reply](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/?replytocom=661211#respond) →
2. Ron [October 13, 2026](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/#comment-661259)

   Why do I still own and use a computer for my business?

   [Reply](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/?replytocom=661259#respond) →

   1. [Fred Flamer](http://seniorsecured.org) [October 14, 2026](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/#comment-661272)

      For every invention, product, or process that man creates, several other problems are created for him. There never seems to be an end. I am glad that humans are actually testing the vulns that are discovered by LLMs, but for how long will that be the case? How long until the LLMs themselves well be checking there own vuln discoveries, testing and deploying with no human involvement…….

      [Reply](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/?replytocom=661272#respond) →

### Leave a Reply [Cancel reply](/2026/10/microsoft-patches-more-than-1400-security-flaws/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Δ

Advertisement

[![](/b-doppel/19.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

Mailing List

[Subscribe here](/subscribe/)

Search KrebsOnSecurity

Search for:

Recent Posts

* [Microsoft Patches More Than 1,400 Security Flaws](https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/)
* [FBI Arrests Executive at Ransomware Negotiation Firm](https:...