---
title: Patch Tuesday, April 2026 Edition
url: https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-14
fetch_date: 2026-04-15T04:43:48.639579
---

# Patch Tuesday, April 2026 Edition

Advertisement

[![](/b-knowbe4/48.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

Advertisement

[![](/b-keeper/14.png)](https://www.keepersecurity.com/privileged-access-management/?utm_source=KrebsOnSecurity&utm_medium=Sponsored&utm_campaign=KrebsOnSecurity_020126&utm_id=Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, April 2026 Edition

April 14, 2026

[5 Comments](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/#comments)

**Microsoft** today pushed software updates to fix a staggering 167 security vulnerabilities in its **Windows** operating systems and related software, including a **SharePoint Server** zero-day and a publicly disclosed weakness in **Windows Defender** dubbed “**BlueHammer**.” Separately, **Google Chrome** fixed its fourth zero-day of 2026, and an emergency update for **Adobe Reader** nixes an actively exploited flaw that can lead to remote code execution.

![A picture of a windows laptop in its updating stage, saying do not turn off the computer. ](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

Redmond warns that attackers are already targeting [CVE-2026-32201](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-32201), a vulnerability in Microsoft SharePoint Server that allows attackers to spoof trusted content or interfaces over a network.

**Mike Walters**, president and co-founder of **Action1**, said CVE-2026-32201 can be used to deceive employees, partners, or customers by presenting falsified information within trusted SharePoint environments.

“This CVE can enable phishing attacks, unauthorized data manipulation, or social engineering campaigns that lead to further compromise,” Walters said. “The presence of active exploitation significantly increases organizational risk.”

Microsoft also addressed BlueHammer ([CVE-2026-33825](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-33825)), a privilege escalation bug in Windows Defender. According to BleepingComputer, the researcher who discovered the flaw [published exploit code for it](https://www.bleepingcomputer.com/news/security/disgruntled-researcher-leaks-bluehammer-windows-zero-day-exploit/) after notifying Microsoft and growing exasperated with their response. **Will Dormann**, senior principal vulnerability analyst at **Tharros**, says he [confirmed](https://infosec.exchange/%40wdormann/116404516592597593) that the public BlueHammer exploit code no longer works after installing today’s patches.

**Satnam Narang**, senior staff research engineer at **Tenable**, said April marks the second-biggest Patch Tuesday ever for Microsoft. Narang also said there are indications that a zero-day flaw Adobe patched in an emergency update on April 11 — [CVE-2026-34621](https://helpx.adobe.com/security/products/acrobat/apsb26-43.html) — has seen active exploitation since at least November 2025.

**Adam Barnett**, lead software engineer at **Rapid7**, called the patch total from Microsoft today “a new record in that category” because it includes nearly 60 browser vulnerabilities. Barnett said it might be tempting to imagine that this sudden spike was tied to the buzz around the announcement a week ago today of [Project Glasswing](https://www.anthropic.com/glasswing) — a much-hyped but still unreleased new AI capability from Anthropic that is reportedly quite good at finding bugs in a vast array of software.

But he notes that **Microsoft Edge** is based on the Chromium engine, and the Chromium maintainers acknowledge a wide range of researchers for the vulnerabilities which Microsoft republished last Friday.

“A safe conclusion is that this increase in volume is driven by ever-expanding AI capabilities,” Barnett said. “We should expect to see further increases in vulnerability reporting volume as the impact of AI models extend further, both in terms of capability and availability.”

Finally, no matter what browser you use to surf the web, it’s important to completely close out and restart the browser periodically. This is really easy to put off (especially if you have a bajillion tabs open at any time) but it’s the only way to ensure that any available updates get installed. For example, a Google Chrome update released earlier this month fixed 21 security holes, including the high-severity zero-day flaw [CVE-2026-5281](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5281).

For a clickable, per-patch breakdown, check out the **SANS Internet Storm Center** [Patch Tuesday roundup](https://isc.sans.edu/forums/diary/Microsoft%20Patch%20Tuesday%20April%202026./32898/). Running into problems applying any of these updates? Leave a note about it in the comments below and there’s a decent chance someone here will pipe in with a solution.

*This entry was posted on Tuesday 14th of April 2026 05:47 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Action1](https://krebsonsecurity.com/tag/action1/) [adobe reader](https://krebsonsecurity.com/tag/adobe-reader/) [Automox](https://krebsonsecurity.com/tag/automox/) [BlueHammer](https://krebsonsecurity.com/tag/bluehammer/) [CVE-2026-32201](https://krebsonsecurity.com/tag/cve-2026-32201/) [CVE-2026-33120](https://krebsonsecurity.com/tag/cve-2026-33120/) [CVE-2026-33825](https://krebsonsecurity.com/tag/cve-2026-33825/) [CVE-2026-34621](https://krebsonsecurity.com/tag/cve-2026-34621/) [Google Chrome](https://krebsonsecurity.com/tag/google-chrome/) [Mike Walters](https://krebsonsecurity.com/tag/mike-walters/) [Patch Tuesday April 2026](https://krebsonsecurity.com/tag/patch-tuesday-april-2026/) [Ryan Braunstein](https://krebsonsecurity.com/tag/ryan-braunstein/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [SharePoint Server](https://krebsonsecurity.com/tag/sharepoint-server/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [Will Dormann](https://krebsonsecurity.com/tag/will-dormann/)

Post navigation

[← Russia Hacked Routers to Steal Microsoft Office Tokens](https://krebsonsecurity.com/2026/04/russia-hacked-routers-to-steal-microsoft-office-tokens/)

## 5 thoughts on “Patch Tuesday, April 2026 Edition”

1. Andy Rosa [April 14, 2026](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/#comment-653342)

   Let’s get used to hundreds of patches per cycle. It’s going to get intense.

   [Reply](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/?replytocom=653342#respond) →

   1. [Catwhisperer](https://happycattech.com) [April 14, 2026](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/#comment-653355)

      In 2026, either you are forced to use this abomination by Corporate, by applications you Jones for, or are a person with possible masochistic inclinations, IMHO…

      [Reply](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/?replytocom=653355#respond) →
2. Stratocaster [April 14, 2026](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/#comment-653345)

   So Windows Defender didn’t prevent a bug in its own code?

   [Reply](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/?replytocom=653345#respond) →
3. Steve [April 14, 2026](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/#comment-653347)

   Regarding the browser vulnerabilities, I found it quite amusing that one of Edge’s newest features was something about h...