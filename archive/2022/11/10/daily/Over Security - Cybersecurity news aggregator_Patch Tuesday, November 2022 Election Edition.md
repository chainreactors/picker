---
title: Patch Tuesday, November 2022 Election Edition
url: https://krebsonsecurity.com/2022/11/patch-tuesday-november-2022-election-edition/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-10
fetch_date: 2025-10-03T22:17:07.998677
---

# Patch Tuesday, November 2022 Election Edition

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, November 2022 Election Edition

November 8, 2022

[14 Comments](https://krebsonsecurity.com/2022/11/patch-tuesday-november-2022-election-edition/#comments)

Let’s face it: Having “2022 election” in the headline above is probably the only reason anyone might read this story today. Still, while most of us here in the United States are anxiously awaiting the results of how well we’ve patched our Democracy, it seems fitting that **Microsoft Corp.** today released gobs of security patches for its ubiquitous **Windows** operating systems. November’s patch batch includes fixes for *a whopping six zero-day security vulnerabilities* that miscreants and malware are already exploiting in the wild.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

Probably the scariest of the zero-day flaws is [CVE-2022-41128](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41128), a “critical” weakness in the Windows scripting languages that could be used to foist malicious software on vulnerable users who do nothing more than browse to a hacked or malicious site that exploits the weakness. Microsoft credits **Google** with reporting the vulnerability, which earned a CVSS score of 8.8.

[CVE-2022-41073](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41073) is a zero-day flaw in the **Windows Print Spooler**, a Windows component that Microsoft has patched mightily over the past year. **Kevin Breen**, director of cyber threat research at **Immersive Labs**, noted that the print spooler has been a popular target for vulnerabilities in the last 12 months, with this marking the 9th patch.

The third zero-day Microsoft patched this month is [CVE-2022-41125](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41125), which is an “elevation of privilege” vulnerability in the Windows Cryptography API: Next Generation (CNG) Key Isolation Service, a service for isolating private keys. **Satnam Narang**, senior staff research engineer at **Tenable**, said exploitation of this vulnerability could grant an attacker SYSTEM privileges.

The fourth zero-day, [CVE-2022-41091](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41091), was previously disclosed and widely reported on in October. It is a Security Feature Bypass of “Windows Mark of the Web” – a mechanism meant to flag files that have come from an untrusted source.

The other two zero-day bugs Microsoft patched this month were for vulnerabilities being exploited in **Exchange Server**. News that these two Exchange flaws were being exploited in the wild [surfaced in late September 2022](https://krebsonsecurity.com/2022/09/microsoft-two-new-0-day-flaws-in-exchange-server/), and many were surprised when Microsoft let October’s Patch Tuesday sail by without issuing official patches for them (the company instead issued mitigation instructions that it was forced to revise multiple times). Today’s patch batch addresses both issues.

**Greg Wiseman**, product manager at **Rapid7**, said the Exchange flaw [CVE-2022-41040](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41040) is a “critical” elevation of privilege vulnerability, and [CVE-2022-41082](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41082) is considered Important, allowing Remote Code Execution (RCE) when PowerShell is accessible to the attacker.

“Both vulnerabilities have been exploited in the wild,” Wiseman said. “Four other CVEs affecting Exchange Server have also been addressed this month. Three are rated as Important, and [CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080) is another privilege escalation vulnerability considered Critical. Customers are advised to update their Exchange Server systems immediately, regardless of whether any previously recommended mitigation steps have been applied. The mitigation rules are no longer recommended once systems have been patched.”

**Adobe** usually issues security updates for its products on Patch Tuesday, but it did not this month. For a closer look at the patches released by Microsoft today and indexed by severity and other metrics, check out the [always-useful Patch Tuesday roundup](https://isc.sans.edu/forums/diary/Microsoft%2BNovember%2B2022%2BPatch%2BTuesday/29230/) from the **SANS Internet Storm Center**. And it’s not a bad idea to hold off updating for a few days until Microsoft works out any kinks in the updates: [AskWoody.com](https://www.askwoody.com/) usually has the lowdown on any patches that may be causing problems for Windows users.

As always, please consider backing up your system or at least your important documents and data before applying system updates. And if you run into any problems with these updates, please drop a note about it here in the comments.

*This entry was posted on Tuesday 8th of November 2022 08:50 PM*

[Time to Patch](https://krebsonsecurity.com/category/patches/)

[AskWoody](https://krebsonsecurity.com/tag/askwoody/) [CVE-2022-41073](https://krebsonsecurity.com/tag/cve-2022-41073/) [CVE-2022-41080](https://krebsonsecurity.com/tag/cve-2022-41080/) [CVE-2022-41082](https://krebsonsecurity.com/tag/cve-2022-41082/) [CVE-2022-41091](https://krebsonsecurity.com/tag/cve-2022-41091/) [CVE-2022-41125](https://krebsonsecurity.com/tag/cve-2022-41125/) [CVE-2022-41128](https://krebsonsecurity.com/tag/cve-2022-41128/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [Kevin Breen](https://krebsonsecurity.com/tag/kevin-breen/) [microsoft](https://krebsonsecurity.com/tag/microsoft/) [Microsoft Patch Tuesday November 2022](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-november-2022/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [windows](https://krebsonsecurity.com/tag/windows/) [Windows Print Spooler](https://krebsonsecurity.com/tag/windows-print-spooler/)

Post navigation

[← LinkedIn Adds Verified Emails, Profile Creation Dates](https://krebsonsecurity.com/2022/11/linkedin-adds-verified-emails-profile-creation-dates/)
[Lawsuit Seeks Food Benefits Stolen By Skimmers →](https://krebsonsecurity.com/2022/11/lawsuit-seeks-food-benefits-stolen-by-skimmers/)

## 14 thoughts on “Patch Tuesday, November 2022 Election Edition”

1. [Alfonso](http://N/A) [November 9, 2022](https://krebsonsecurity.com/2022/11/patch-tuesday-november-2022-election-edition/#comment-571014)

   I have unsubscribed from this site as much as 8 times. Have the screenshots telling me that I will get a confirmation mail. What’s up with that? What’s up with your site?

   1. Myrddin Emrys [November 9, 2022](https://krebsonsecurity.com/2022/11/patch-tuesday-november-2022-election-edition/#comment-571081)

      I can’t speak to Kreb’s site inner workings, but the most common reason that an unsubscribe fails to work is because the address you’re sending the request from isn’t the address that the content is being delivered to. Did you perhaps add +flags to your address, or do you have multiple addresses that redi...