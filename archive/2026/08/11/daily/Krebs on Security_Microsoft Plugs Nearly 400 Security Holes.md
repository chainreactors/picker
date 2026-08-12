---
title: Microsoft Plugs Nearly 400 Security Holes
url: https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/
source: Krebs on Security
date: 2026-08-11
fetch_date: 2026-08-12T04:02:57.647288
---

# Microsoft Plugs Nearly 400 Security Holes

Advertisement

[![](/b-flashpoint/5.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

Advertisement

[![](/b-cape/2.jpg)](https://www.cape.co/?utm_source=Krebs&utm_medium=Banner&utm_campaign=Krebs_Display_Footer_Mobile)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Microsoft Plugs Nearly 400 Security Holes

August 11, 2026

[5 Comments](https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/#comments)

**Microsoft** today released updates to remedy at least 398 security vulnerabilities in its **Windows** operating systems and supported software, including one weakness that is already being actively exploited and two others that were publicly detailed prior to today.

![](https://krebsonsecurity.com/wp-content/uploads/2026/08/workingonpc.png)

Image: Shutterstock, Mallika Home Studio.

August’s overstuffed bundle of patch joy from Microsoft did not eclipse its recording breaking release of [more than 570 security updates last month](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/), but it is double June’s then-record batch of [nearly 200 fixes](https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/#more-73788). Microsoft has attributed the recent patch deluge to vulnerability discoveries aided by artificial intelligence, and experts roundly agree that Windows users should get used to the idea of Patch Tuesdays (the second Tuesday of each month) covering hundreds of newly discovered security flaws.

Fully 42 of the 398 flaws that Microsoft patched today earned Redmond’s most-dire “critical” rating, meaning they are severe enough that malware or malcontents could exploit them to gain remote control over a Windows computer with little to no help from the user.

The sole known “zero day” bug fixed by Microsoft this month is [CVE-2026-68820](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-68820), a privilege escalation weakness in a core Windows component called **afd.sys**, which the security firm **Automox** describes as “the driver behind Windows socket connections on effectively every endpoint.”

“This isn’t a front-door bug,” Automox’s **Landon Miles** [wrote](https://www.automox.com/blog/patch-fix-tuesday-august-2026) in a Patch Tuesday blog post. “It’s step two in a chain: an attacker phishes their way into a low-privilege foothold, then uses the driver flaw to take the box. The 7.0 score reflects the high attack complexity, because race conditions are fiddly. The exploit has to be thrown over and over until the timing lands. Someone is clearly landing it anyway.”

[CVE-2026-62832](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-62832) is another privilege escalation flaw that Microsoft has labeled likely to be exploited; this flaw, in the Windows User Profile Service, may be related to the recent [“LegacyHive” public disclosure](https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723) from the prolific bug hunter known as **Nightmare Eclipse**. The other publicly disclosed flaw is [CVE-2026-72971](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-72971), a low-impact local tampering vulnerability that Microsoft reckons is unlikely to be exploited.

Other major software makers are likewise increasing their patch volumes and cadence thanks to AI, including **Adobe** which last month moved to twice-monthly security bulletins published on the 2nd and 4th Tuesday of each month. **Cisco**, **Google**, **Mozilla** and **Oracle** also are shipping updates far more frequently and abundantly.

By all accounts, AI is quite good at finding security holes in software. But for now at least, patching the resulting bugpocalypse remains a heavily human-centric endeavor, and the jury is still out on whether AI technologies will turn out to be as good at fixing vulnerabilities as they are at finding and exploiting them. This is an important question when one considers that these same AI technologies also are suggesting fixes for the vulnerabilities they find.

Researchers at **1Password** recently [examined](https://1password.com/blog/why-ai-generated-patches-still-require-human-review) what happens when different large language models (LLMs) generate vulnerability patches for newly disclosed, complex vulnerabilities. They found the LLMs produced patches that failed to fix the flaw or added a new weakness in the process (or both) more than half the time.

**Ed Skoudis**, president of the **SANS Technology Institute**, said his team has seen excellent results using AI to generate patches, provided there are humans in the loop to test the suggested fixes and push for iterative improvements.

“AI is rapidly becoming astonishingly good at finding vulnerabilities, but this research shows that fixing them is a very different problem,” Skoudis wrote in a SANS newsletter today. “Don’t expect one-shot AI patching to work reliably. Instead, iterate, test, challenge, improve, and verify. AI can be an extraordinary patching partner, but today it still needs a skilled human at the keyboard.”

**Tyler Reguly** at **Fortra** says while reports of Microsoft patching hundreds of vulnerabilities in one go have prompted some organizations to try to patch faster, it’s important to bear in mind that only one of the almost 400 bugs addressed today is known to be actively exploited. Reguly suggested security leaders check in with their teams to see how they’re handling the increasing workloads, which often involve testing fixes before deploying them in production environments.

“If you’re a chief security officer talk to your teams about how they are shifting or modifying their workflows to better accommodate the patching shift that we’re seeing and support them across various organizational units by enabling the changes they want to see made,” Reguly said. “There’s no need to rush these updates, no matter what various vendors and organizations try to tell you. You need to make sure that you are rolling out safe updates that will not negatively impact your systems.”

Speaking of the humans behind the keyboards, don’t neglect to backup your system and/or data before applying this month’s monster patch load. The day after each month’s Patch Tuesday is sometimes derisively referred to as Reboot Wednesday, but it generally doesn’t hurt to wait a few days to apply these huge update bundles because it sometimes takes a couple of days for the occasional misbehaving patch to get ironed out properly by Microsoft.

For a clickable, per-patch breakdown by severity and urgency, check out [this roundup](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20August%202026/33236) from the SANS Internet Storm Center.

*This entry was posted on Tuesday 11th of August 2026 05:28 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[1Password](https://krebsonsecurity.com/tag/1password/) [afd.sys](https://krebsonsecurity.com/tag/afd-sys/) [Automox](https://krebsonsecurity.com/tag/automox/) [CVE-2026-62832](https://krebsonsecurity.com/tag/cve-2026-62832/) [CVE-2026-68820](https://krebsonsecurity.com/tag/cve-2026-68820/) [CVE-2026-72971](https://krebsonsecurity.com/tag/cve-2026-72971/) [Ed Skoudis](https://krebsonsecurity.com/tag/ed-skoudis/) [Landon Miles](https://krebsonsecurity.com/tag/landon-miles/) [Microsoft Patch Tuesday August 2026](https://krebsonsecurity.com/tag/microsoft-patch-t...